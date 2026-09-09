#!/usr/bin/env python3
"""Curate the raw Europe PMC harvest into index.tsv + curated.json.

Pipeline:
  1. Drop records that are not usable evidence (retractions, comments, case
     reports, abstract-less stubs, haematology-only work, TCGA-style prognostic
     signature papers with no therapeutic content).
  2. Re-assign each record to a TME axis from its own title/abstract vocabulary
     (the harvest domain is only a fallback), and tag evidence level, disease
     context and immunotherapy-resistance relevance.
  3. Score by citation impact (age-normalised), venue tier, evidence level and
     resistance relevance, then take the top records per axis under quotas that
     guarantee clinical, review and 2024+ representation in every axis.
"""
import csv
import html
import json
import math
import os
import re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw_harvest.json")
TSV = os.path.join(HERE, "index.tsv")
CURATED = os.path.join(HERE, "curated.json")

PER_AXIS = 13
PER_AXIS_OVERRIDE = {"general_tme_modulation": 22, "clinical_resistance": 18}
MIN_YEAR_FOUNDATIONAL = 1990

TIER1 = {
    "nature", "science", "cell", "cancer cell", "nature medicine", "nature cancer",
    "immunity", "nature immunology", "cancer discovery", "science translational medicine",
    "the new england journal of medicine", "science immunology", "cell metabolism",
    "nature reviews cancer", "nature reviews clinical oncology", "nature reviews immunology",
    "the lancet oncology", "journal of clinical oncology", "nature biotechnology",
    "nature nanotechnology", "cancer immunology research", "the journal of experimental medicine",
    "the journal of clinical investigation", "annals of oncology", "cell reports medicine",
    "journal for immunotherapy of cancer", "clinical cancer research", "cancer research",
    "nature communications", "science advances", "the lancet", "jama oncology",
    "molecular cancer", "signal transduction and targeted therapy", "gut", "hepatology",
    "gastroenterology", "blood", "neuro-oncology", "embo molecular medicine",
    "proceedings of the national academy of sciences of the united states of america",
}

# ------------------------------------------------------------------ exclusions
DROP_PUBTYPE = {"retracted publication", "comment", "editorial", "case reports",
                "published erratum", "retraction of publication", "news"}
DROP_TITLE = [
    "prognostic signature", "prognostic model", "prognostic index", "risk signature",
    "risk model", "risk score", "prognostic value", "predictive nomogram", "nomogram",
    "bioinformatic analysis", "bioinformatics analysis", "integrated analysis of",
    "identification of a novel prognostic", "lncrna signature", "mirna signature",
    "related genes signature", "gene signature predicts prognosis", "pan-cancer analysis",
    "mendelian randomization", "bibliometric", "scientometric", "protocol for a",
    "study protocol", "corrigendum", "erratum", "editorial:", "comment on",
    "hallmarks of cancer",
    "response to", "letter to the editor", "retracted", "expression of concern",
]
HEME = ["leukemia", "leukaemia", "lymphoma", "myeloma", "myelodysplastic",
        "myelofibrosis", "hodgkin", "aml", "cll", "all patients with acute"]
SOLIDWORDS = [
    "solid tumor", "solid tumour", "carcinoma", "adenocarcinoma", "melanoma", "glioma",
    "glioblastoma", "sarcoma", "neuroblastoma", "mesothelioma", "breast cancer",
    "lung cancer", "colorectal", "pancreatic", "ovarian", "gastric", "hepatocellular",
    "renal cell", "prostate cancer", "head and neck", "bladder", "esophageal",
    "oesophageal", "cervical cancer", "endometrial", "cholangiocarcinoma", "brain tumor",
    "brain tumour", "urothelial", "solid malignan", "melanoma", "nsclc", "pdac", "tnbc",
]

# ------------------------------------------------------------------ axis rules
AXES = [
    ("myeloid_macrophage", [
        "tumor-associated macrophage", "tumour-associated macrophage", "tam ",
        "macrophage polariz", "macrophage polaris", "macrophage reprogram",
        "m2 macrophage", "m1 macrophage", "csf1r", "csf-1r", "pexidartinib",
        "cd47", "sirpalpha", "sirp-alpha", "sirpa", "magrolimab", "evorpacept",
        "cd40 agonist", "anti-cd40", "trem2", "marco", "lilrb", "ilt4", "mertk",
        "myeloid-derived suppressor", "mdsc", "tumor-associated neutrophil",
        "neutrophil extracellular trap", "cxcr2", "il-8 blockade", "anti-il-8",
        "monocyte", "microglia", "car macrophage", "efferocytosis", "phagocytosis",
        "myeloid checkpoint", "myeloid cell", "pi3k gamma", "pi3kgamma", "eganelisib",
        "bexmarilimab", "clever-1", "ccr2", "tasquinimod",
    ]),
    ("treg_suppressive_lymphoid", [
        "regulatory t cell", "treg", "foxp3", "ccr8", "anti-cd25", "mogamulizumab",
        "tnfr2", "regulatory b cell", "breg", "gitr", "ox40", "icos agonist",
        "4-1bb agonist", "t cell exhaustion", "t-cell exhaustion", "exhausted t cell",
        "tox ", "tcf1", "tcf-1", "progenitor exhausted", "stem-like t cell",
        "tissue-resident memory", "nk cell dysfunction", "innate lymphoid",
        "gamma delta t", "botensilimab",
    ]),
    ("caf_stroma_ecm", [
        "cancer-associated fibroblast", "caf", "fibroblast activation protein", "fap",
        "myofibroblast", "stellate cell", "desmoplas", "extracellular matrix",
        "matrix stiffness", "collagen", "hyaluron", "lysyl oxidase", "loxl2",
        "solid stress", "interstitial fluid pressure", "matrix remodel",
        "focal adhesion kinase", "integrin", "tgf-beta", "tgf-\u03b2", "tgfbeta",
        "bintrafusp", "galunisertib", "vactosertib", "nis793", "srk-181", "pegph20",
        "hedgehog inhibitor", "vismodegib", "stroma-target", "stromal reprogram",
        "defactinib", "losartan",
    ]),
    ("vasculature_hypoxia", [
        "vascular normaliz", "vascular normalis", "vessel normaliz", "tumor vasculature",
        "tumour vasculature", "angiogen", "vegf", "angiopoietin", "pericyte",
        "high endothelial venule", "endothelial anergy", "tumor perfusion", "hypoxia",
        "hypoxic", "hif-1", "hif-2", "hif1a", "belzutifan", "evofosfamide",
        "carbonic anhydrase ix", "oxygenation", "reoxygenation", "bevacizumab",
        "lenvatinib", "cabozantinib", "ivonescimab", "trebananib",
    ]),
    ("metabolic_tme", [
        "cd73", "cd39", "adenosine", "a2a receptor", "a2ar", "oleclumab",
        "ciforadenant", "etrumadenant", "ido1", "indoleamine", "epacadostat",
        "kynurenine", "tdo2", "arginase", "arginine deprivation", "glutaminase",
        "glutamine antagonist", "telaglenastat", "lactate", "lactic acid", "acidosis",
        "acidic microenvironment", "glycolysis", "mct1", "mct4", "oxphos",
        "fatty acid oxidation", "lipid metabolism", "cholesterol metabolism",
        "immunometabolism", "metabolic reprogramming", "nutrient competition",
        "ketogenic diet", "caloric restriction", "fasting", "obesity", "exercise",
        "metformin", "statin", "propranolol", "beta-blocker", "chronic stress",
        "nad+", "nicotinamide", "methionine", "serine",
    ]),
    ("innate_agonists", [
        "sting", "cgas", "tlr agonist", "tlr7", "tlr8", "tlr9", "tlr3",
        "poly(i:c)", "poly-iclc", "imiquimod", "resiquimod", "cpg", "vidutolimod",
        "cmp-001", "tilsotolimod", "lefitolimod", "bo-112", "rig-i", "mda5",
        "aim2", "inflammasome", "type i interferon", "type-i interferon",
        "innate immune agonist", "interferon gene",
    ]),
    ("cytokine_engineering", [
        "il-2 variant", "il-2 mutein", "not-alpha il-2", "engineered il-2",
        "bempegaldesleukin", "nemvaleukin", "pd1-il2v", "il-15 superagonist", "n-803",
        "nogapendekin", "decoy-resistant il-18", "il-12", "interleukin-12", "il-18",
        "il-21", "il-10", "pegilodecakin", "immunocytokine", "antibody-cytokine",
        "cytokine prodrug", "masked cytokine", "l19-il2", "cytokine armor",
        "anti-il-6", "tocilizumab", "canakinumab", "il-1beta", "lif blockade",
        "tumor-targeted cytokine",
    ]),
    ("trafficking_tls", [
        "tertiary lymphoid", "lymphoid neogenesis", "t cell infiltration",
        "t-cell infiltration", "lymphocyte infiltration", "immune cell infiltration",
        "t cell trafficking", "t-cell trafficking", "lymphocyte homing", "chemokine",
        "cxcl9", "cxcl10", "cxcl13", "ccl5", "ccl21", "cxcr3", "cxcr4", "cxcl12",
        "plerixafor", "motixafortide", "nox-a12", "immune contexture", "light ",
        "tnfsf14",
    ]),
    ("antigen_presentation_ifn", [
        "antigen presentation", "mhc class i", "mhc-i", "hla loss", "beta-2 microglobulin",
        "b2m", "tap1", "nlrc5", "jak1", "jak2", "interferon-gamma signal",
        "ifn-gamma signal", "interferon signal", "immunoediting", "antigen loss",
        "neoantigen", "beta-catenin", "pten loss", "stk11", "lkb1", "keap1",
        "serpinb9", "immunoproteasome",
    ]),
    ("epigenetic_priming", [
        "epigenetic therapy", "dnmt", "azacitidine", "decitabine", "guadecitabine",
        "hdac", "entinostat", "domatinostat", "mocetinostat", "ezh2", "tazemetostat",
        "lsd1", "bet inhibitor", "setdb1", "kdm5", "viral mimicry",
        "endogenous retrovirus", "epigenetic priming", "epigenetic reprogramming",
        "dna methylation",
    ]),
    ("radiation_chemo_priming", [
        "abscopal", "radiotherapy", "radiation therapy", "stereotactic body",
        "sbrt", "flash radiotherapy", "radiation-induced", "immunogenic cell death",
        "chemoimmunotherapy", "metronomic chemotherapy", "cyclophosphamide",
        "gemcitabine", "oxaliplatin", "in situ vaccine", "radioimmuno",
    ]),
    ("intratumoral_oncolytic", [
        "intratumoral", "intratumoural", "in situ vaccination", "oncolytic",
        "talimogene", "t-vec", "vusolimogene", "engineered bacteria", "salmonella",
        "clostridium novyi", "listeria",
    ]),
    ("microbiome", [
        "microbiome", "microbiota", "fecal microbiota", "faecal microbiota",
        "akkermansia", "live biotherapeutic", "cbm588", "mrx0518", "probiotic",
        "intratumoral bacteria", "short-chain fatty acid", "antibiotic",
    ]),
    ("tme_directed_delivery", [
        "nanoparticle", "nanomedicine", "hydrogel", "microenvironment-responsive",
        "tme-responsive", "ph-responsive", "ros-responsive", "enzyme-responsive",
        "mmp-responsive", "protease-activated", "masked antibody", "probody",
        "conditionally active", "logic-gated", "lipid nanoparticle", "drug delivery",
        "ferroptosis", "pyroptosis", "cuproptosis",
    ]),
    ("cell_therapy_tme", [
        "car t", "car-t", "chimeric antigen receptor", "car nk", "car-nk", "tcr-t",
        "tcr-engineered", "tumor-infiltrating lymphocyte", "til therapy",
        "adoptive cell therapy", "armored car", "armoured car", "lifileucel",
        "switch receptor", "hypoxia-inducible car",
    ]),
    ("physical_modulation", [
        "focused ultrasound", "histotripsy", "microbubble", "sonodynamic",
        "photodynamic", "photothermal", "photoimmunotherapy", "hyperthermia",
        "cryoablation", "radiofrequency ablation", "irreversible electroporation",
        "tumor treating fields", "convection-enhanced delivery",
        "blood-brain barrier opening", "blood-tumor barrier",
    ]),
    ("spatial_profiling", [
        "single-cell rna", "scrna-seq", "single cell rna", "spatial transcriptomic",
        "imaging mass cytometry", "multiplex immunofluorescence", "codex",
        "spatial proteomic", "single-cell atlas", "spatial multi-omic", "immune atlas",
        "multiomic", "multi-omic",
    ]),
    ("clinical_resistance", [
        "resistance to immunotherapy", "immunotherapy resistance",
        "resistance to immune checkpoint", "checkpoint inhibitor resistance",
        "anti-pd-1 resistance", "primary resistance", "acquired resistance",
        "immune escape", "immune evasion", "immunoresistance", "hyperprogression",
        "rechallenge", "refractory to immunotherapy", "cold tumor", "cold tumour",
        "immune desert", "immune exclusion", "immune-excluded", "non-inflamed",
    ]),
]
AXIS_ORDER = [a for a, _ in AXES] + ["general_tme_modulation"]

DISEASES = [
    ("melanoma", ["melanoma"]),
    ("nsclc", ["non-small cell lung", "nsclc", "lung adenocarcinoma", "lung cancer"]),
    ("pdac", ["pancreatic ductal", "pancreatic cancer", "pdac", "pancreatic adenocarcinoma"]),
    ("crc", ["colorectal", "colon cancer", "rectal cancer", "mss ", "microsatellite stable"]),
    ("gbm_cns", ["glioblastoma", "glioma", "brain metastas", "medulloblastoma",
                 "diffuse midline", "cns tumor", "leptomeningeal"]),
    ("breast", ["breast cancer", "tnbc", "triple-negative breast"]),
    ("hcc_biliary", ["hepatocellular", "liver cancer", "cholangiocarcinoma", "biliary"]),
    ("rcc", ["renal cell", "kidney cancer"]),
    ("hnscc", ["head and neck"]),
    ("gi_other", ["gastric", "esophageal", "oesophageal", "gastroesophageal", "peritoneal"]),
    ("gu_other", ["prostate", "urothelial", "bladder"]),
    ("gyn", ["ovarian", "cervical", "endometrial"]),
    ("sarcoma_peds", ["sarcoma", "osteosarcoma", "neuroblastoma", "ewing"]),
    ("mesothelioma", ["mesothelioma"]),
]

RESIST = [
    "resistance to immunotherapy", "immunotherapy resistance", "resistant to anti-pd",
    "resistance to immune checkpoint", "checkpoint inhibitor resistance",
    "anti-pd-1 resistance", "pd-1 resistance", "primary resistance", "acquired resistance",
    "refractory", "immune escape", "immune evasion", "immunoresistance",
    "hyperprogression", "cold tumor", "cold tumour", "immunologically cold",
    "immune desert", "immune exclusion", "immune-excluded", "non-inflamed",
    "unresponsive to checkpoint", "fail to respond", "non-responder", "nonresponder",
    "resensiti", "overcome resistance", "restore response", "rechallenge",
    "resistance mechanism", "sensitize", "sensitise",
]

# A record has to be about acting on / dissecting the microenvironment or
# immune response, not merely mention a tumour type.
RELEVANCE = [
    "microenvironment", "immunotherapy", "immune checkpoint", "checkpoint blockade",
    "checkpoint inhibitor", "anti-pd-1", "anti-pd-l1", "anti-ctla-4", "immune evasion",
    "immune escape", "antitumor immunity", "anti-tumor immunity", "antitumour immunity",
    "immunosuppressive", "immune infiltrat", "tumor immunity", "tumour immunity",
    "stroma", "tumor-associated macrophage", "tumour-associated macrophage",
    "regulatory t cell", "myeloid-derived suppressor", "t cell exhaustion",
    "t-cell exhaustion", "cancer-associated fibroblast", "tumor-infiltrating",
    "tumour-infiltrating", "immunologically cold", "immune exclusion", "cytotoxic t",
    "cd8+ t", "natural killer", "dendritic cell", "tumor immunology",
]
# Cross-cutting records are kept only if the title itself names an immune or
# microenvironment concept; otherwise unrelated landmark oncology papers drift in.
GENERAL_TITLE = [
    "immun", "microenvironment", "tumor micro", "tumour micro", "t cell", "t-cell",
    "macrophage", "myeloid", "fibroblast", "stroma", "checkpoint", "pd-1", "pd-l1",
    "ctla-4", "b7-h1", "lymphocyte", "dendritic cell", "nk cell", "cytokine",
    "chemokine", "inflamm", "metabolic competition", "cold and hot", "b cells",
]
# Broad disease overviews: informative but not TME-modulation evidence.
DROP_VENUE = ["disease primers", "cochrane", "cancer treatment reviews"]
DISEASE_ONLY_TITLE = re.compile(
    r"^(non-small[- ]cell lung|small[- ]cell lung|lung|breast|colorectal|colon|gastric|"
    r"pancreatic|ovarian|prostate|bladder|renal cell|hepatocellular|oesophageal|"
    r"esophageal|head and neck|cervical|endometrial|thyroid|melanoma|glioblastoma|"
    r"glioma|sarcoma|osteosarcoma|neuroblastoma|mesothelioma)?\s*(cancer|carcinoma|"
    r"tumour|tumor|melanoma|glioblastoma|glioma|sarcoma)?$")

TRIAL_PUBTYPES = ("clinical trial", "randomized controlled trial", "observational study")
CLINICAL_WORDS = ["patients", "phase 1", "phase i", "phase 2", "phase ii", "phase 3",
                  "phase iii", "first-in-human", "neoadjuvant", "cohort", "trial",
                  "real-world", "biopsies", "biopsy"]
REVIEW_WORDS = ["review", "perspective", "overview", "we discuss", "here we review"]
PRECLIN_WORDS = ["mice", "mouse", "murine", "syngeneic", "orthotopic", "xenograft",
                 "in vivo", "organoid", "tumor-bearing", "tumour-bearing", "pdx"]


def has(text, needles):
    return any(n in text for n in needles)


def norm_title(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def evidence_of(rec, text, pt):
    if has(pt, TRIAL_PUBTYPES) or re.search(r"phase (1|2|3|i|ii|iii|1b|1/2)\b", text):
        return "clinical_trial"
    if "meta-analysis" in pt or "systematic review" in pt:
        return "systematic_review"
    if "review" in pt and not has(pt, ("research-article",)):
        return "review"
    if has(text, ["single-cell", "scrna", "spatial transcriptomic", "cohort",
                  "patient samples", "resected", "biopsies"]) and "patients" in text:
        return "translational_human"
    if has(text, PRECLIN_WORDS):
        return "preclinical"
    if "review" in pt or has(rec["title"].lower(), REVIEW_WORDS):
        return "review"
    return "mechanistic"


def assign_axis(title, abstract, fallback):
    """Title vocabulary decides the axis; abstract only breaks ties."""
    scores = Counter()
    for axis, keys in AXES:
        hits = 3 * sum(1 for k in keys if k in title) + sum(1 for k in keys if k in abstract)
        if hits:
            scores[axis] = hits
    if not scores:
        return fallback if fallback in AXIS_ORDER else "general_tme_modulation"
    top, n = scores.most_common(1)[0]
    # a title hit scores 3; anything weaker means the paper is cross-cutting
    # rather than an axis-specific contribution
    if n < 3:
        return "general_tme_modulation"
    # keep the harvest domain when it is a credible runner-up: it reflects the
    # query the record actually came from
    if fallback in scores and scores[fallback] >= n - 1:
        return fallback
    return top


def disease_of(text):
    tags = [name for name, keys in DISEASES if has(text, keys)]
    if not tags:
        return "pan-solid"
    return ";".join(tags[:3])


def venue_tier(venue):
    return 1 if venue.strip().lower() in TIER1 else 2


def keep(rec, text, pt):
    if not rec["title"] or len(rec["abstract"]) < 200:
        return False
    if has(pt, DROP_PUBTYPE):
        return False
    tl = rec["title"].lower()
    if has(tl, DROP_TITLE):
        return False
    if has(rec["venue"].lower(), DROP_VENUE):
        return False
    if DISEASE_ONLY_TITLE.match(tl.strip().rstrip(".")):
        return False
    if not has(text, RELEVANCE):
        return False
    try:
        year = int(rec["year"])
    except ValueError:
        return False
    if year < MIN_YEAR_FOUNDATIONAL:
        return False
    if has(tl, HEME) and not has(text, SOLIDWORDS):
        return False
    if not has(text, SOLIDWORDS) and not has(
            text, ["solid", "tumor microenvironment", "tumour microenvironment"]):
        return False
    return True


def score(rec, evidence, resistance, tier):
    year = int(rec["year"])
    age = max(1, 2026 - year)
    cited = rec["cited"] or 0
    s = 2.2 * math.log1p(cited) + 1.4 * math.log1p(cited / age)
    s += 3.0 if tier == 1 else 0.0
    s += {"clinical_trial": 3.2, "systematic_review": 1.4, "translational_human": 2.2,
          "review": 1.0, "preclinical": 1.6, "mechanistic": 0.8}[evidence]
    s += 2.0 if resistance else 0.0
    if year >= 2024:
        s += 1.5
    if rec["sweep"] == "foundational" and year <= 2014:
        s += 1.0
    if rec["inEPMC"] == "Y":
        s += 0.4
    return s


def url_of(rec):
    if rec["pmcid"]:
        return f"https://pmc.ncbi.nlm.nih.gov/articles/{rec['pmcid']}/"
    if rec["pmid"]:
        return f"https://pubmed.ncbi.nlm.nih.gov/{rec['pmid']}/"
    if rec["doi"]:
        return f"https://doi.org/{rec['doi']}"
    return ""


def select(cands, limit):
    """Top `limit` per axis with quotas so no axis is all-reviews or all-old."""
    cands.sort(key=lambda r: -r["score"])
    chosen, seen_ev = [], Counter()
    quotas = [("clinical_trial", 3), ("preclinical", 3), ("review", 3)]
    for ev, cap in quotas:
        for r in cands:
            if len(chosen) >= limit:
                break
            if r in chosen or r["evidence"] != ev or seen_ev[ev] >= cap:
                continue
            chosen.append(r)
            seen_ev[ev] += 1
    recent = [r for r in cands if int(r["year"]) >= 2024 and r not in chosen]
    for r in recent[:3]:
        if len(chosen) < limit:
            chosen.append(r)
    for r in cands:
        if len(chosen) >= limit:
            break
        if r not in chosen:
            chosen.append(r)
    chosen.sort(key=lambda r: (-r["score"],))
    return chosen


def main():
    raw = json.load(open(RAW))
    by_axis = defaultdict(list)
    seen_titles, seen_ids = set(), set()
    dropped = 0

    for rec in raw:
        rec["title"] = re.sub(r"<[^>]+>", "", html.unescape(rec["title"]))
        rec["abstract"] = re.sub(r"<[^>]+>", "", html.unescape(rec["abstract"]))
        text = f"{rec['title']} {rec['abstract']}".lower()
        pt = rec["pubType"].lower()
        if not keep(rec, text, pt):
            dropped += 1
            continue
        ident = rec["doi"].lower() or rec["pmid"]
        nt = norm_title(rec["title"])
        if ident in seen_ids or nt in seen_titles:
            continue
        seen_ids.add(ident)
        seen_titles.add(nt)

        axis = assign_axis(rec["title"].lower(), rec["abstract"].lower(), rec["domain"])
        if axis == "general_tme_modulation" and not has(rec["title"].lower(), GENERAL_TITLE):
            dropped += 1
            continue
        evidence = evidence_of(rec, text, pt)
        resistance = has(text, RESIST)
        tier = venue_tier(rec["venue"])
        item = dict(rec)
        item.update({
            "axis": axis,
            "evidence": evidence,
            "resistance": "yes" if resistance else "no",
            "disease": disease_of(text),
            "tier": tier,
            "url": url_of(rec),
        })
        item["score"] = round(score(rec, evidence, resistance, tier), 2)
        by_axis[axis].append(item)

    curated = []
    for axis in AXIS_ORDER:
        if not by_axis.get(axis):
            continue
        curated.extend(select(by_axis[axis], PER_AXIS_OVERRIDE.get(axis, PER_AXIS)))

    for item in curated:
        item.pop("also_domains", None)
    with open(CURATED, "w") as f:
        json.dump(curated, f, indent=1)

    cols = ["axis", "evidence", "disease", "resistance", "authors", "title", "venue",
            "year", "cited", "pmid", "doi", "pmcid", "url", "local_fulltext", "status"]
    with open(TSV, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
        w.writerow(cols)
        for item in curated:
            w.writerow([
                item["axis"], item["evidence"], item["disease"], item["resistance"],
                item["authors"], item["title"], item["venue"], item["year"],
                item["cited"], item["pmid"], item["doi"], item["pmcid"], item["url"],
                "", "oa_xml" if item["inEPMC"] == "Y" else "metadata_only",
            ])

    print(f"raw={len(raw)} dropped={dropped} pool={sum(len(v) for v in by_axis.values())} "
          f"curated={len(curated)}")
    for axis in AXIS_ORDER:
        sel = [r for r in curated if r["axis"] == axis]
        if sel:
            evs = Counter(r["evidence"] for r in sel)
            print(f"  {axis:26s} {len(sel):3d}  {dict(evs)}")


if __name__ == "__main__":
    main()
