#!/usr/bin/env python3
"""Curate the raw Europe PMC harvest into index.tsv + curated.json.

Pipeline:
  1. Drop records that are not usable NK-cell-therapy evidence (retractions,
     comments, case reports, abstract-less stubs, prognostic-signature and
     bibliometric papers, records that merely mention NK cells in passing,
     non-oncology NK immunology).
  2. Re-assign each record to an axis from its own title/abstract vocabulary
     (the harvest domain is only a fallback), and tag evidence level, disease
     context, cell source and whether the paper reports a manufacturing /
     culture method.
  3. Score by citation impact (age-normalised), venue tier, evidence level,
     recency and manufacturing relevance, then take the top records per axis
     under quotas that guarantee clinical, preclinical and review representation.
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

PER_AXIS = 18
PER_AXIS_OVERRIDE = {
    "car_nk_engineering": 32,
    "expansion_feeders": 30,
    "clinical_nk": 28,
    "cytokine_support": 24,
    "nk_phenotype_states": 26,
    "gene_editing_knockouts": 24,
    "nk_engagers": 20,
    "cryo_qc_manufacturing": 20,
    "nk_cell_sources": 20,
    "metabolism_persistence": 18,
    "general_nk_therapy": 22,
}
MIN_YEAR = 1975

TIER1 = {
    "nature", "science", "cell", "cancer cell", "nature medicine", "nature cancer",
    "immunity", "nature immunology", "cancer discovery", "science translational medicine",
    "the new england journal of medicine", "science immunology", "cell stem cell",
    "nature reviews cancer", "nature reviews clinical oncology", "nature reviews immunology",
    "nature reviews drug discovery", "the lancet oncology", "journal of clinical oncology",
    "nature biotechnology", "cancer immunology research", "the journal of experimental medicine",
    "the journal of clinical investigation", "annals of oncology", "cell reports medicine",
    "journal for immunotherapy of cancer", "clinical cancer research", "cancer research",
    "nature communications", "science advances", "the lancet", "jama oncology",
    "blood", "blood advances", "leukemia", "haematologica", "bone marrow transplantation",
    "molecular therapy", "cytotherapy", "neuro-oncology", "cell reports",
    "signal transduction and targeted therapy", "embo molecular medicine",
    "proceedings of the national academy of sciences of the united states of america",
    "frontiers in immunology", "oncoimmunology", "molecular therapy oncolytics",
    "journal of hematology & oncology", "biology of blood and marrow transplantation",
    "transplantation and cellular therapy",
}

# ------------------------------------------------------------------ exclusions
DROP_PUBTYPE = {"retracted publication", "comment", "editorial", "case reports",
                "published erratum", "retraction of publication", "news"}
DROP_TITLE = [
    "prognostic signature", "prognostic model", "prognostic index", "risk signature",
    "risk model", "risk score", "prognostic value", "predictive nomogram", "nomogram",
    "bioinformatic analysis", "bioinformatics analysis", "integrated analysis of",
    "lncrna signature", "mirna signature", "gene signature", "pan-cancer analysis",
    "mendelian randomization", "bibliometric", "scientometric", "study protocol",
    "protocol for a", "corrigendum", "erratum", "editorial:", "comment on",
    "letter to the editor", "retracted", "expression of concern", "reply",
    # ILC2/ILC3 biology is a different lineage question from NK effector therapy
    "group 2 innate lymphoid", "group 3 innate lymphoid", "ilc2", "ilc3",
    "intestinal inflammation", "inflammatory bowel", "interleukin-22",
    # NK/T-cell lymphoma is a malignancy of NK lineage, not NK-cell therapy
    "nk/t-cell lymphoma", "nk/t cell lymphoma", "natural killer/t-cell lymphoma",
    "extranodal natural killer", "nk-cell lymphoma", "nk cell leukemia",
    "large granular lymphocytic leukemia",
]
# NK biology outside oncology sneaks in through the cytokine and phenotype queries.
DROP_CONTEXT = ["covid-19", "sars-cov-2", "hepatitis b virus infection", "hiv-1 infection",
                "malaria", "tuberculosis", "pregnancy", "preeclampsia", "endometriosis",
                "recurrent spontaneous abortion", "multiple sclerosis", "lupus",
                "rheumatoid arthritis", "atherosclerosis", "influenza", "cytomegalovirus retinitis",
                "asthma", "type 1 diabetes", "graft rejection & kidney"]

# ------------------------------------------------------------------ axis rules
AXES = [
    ("nk_phenotype_states", [
        "cd56bright", "cd56dim", "cd56 bright", "nk cell subset", "nk subsets",
        "adaptive nk", "nkg2c+", "memory-like nk", "memory nk", "nk cell memory",
        "nk cell differentiation", "nk cell maturation", "nk cell education",
        "licensing", "nk cell heterogeneity", "nk cell diversity", "tissue-resident nk",
        "tumor-infiltrating nk", "intratumoral nk", "nk cell repertoire", "cd57",
        "g-nk", "fcrgamma", "fcepsilonri", "kir repertoire", "single-cell rna",
        "scrna-seq", "mass cytometry", "cytof", "high-dimensional", "nk cell atlas",
        "nk cell dysfunction", "nk cell exhaustion", "exhausted nk", "dysfunctional nk",
        "nk cell senescence", "nk cell anergy", "nk cell fitness", "innate lymphoid cell",
        "nk cell phenotype", "nk cell state", "transcriptional program",
    ]),
    ("nk_cell_sources", [
        "cord blood nk", "umbilical cord", "peripheral blood nk", "ipsc-nk",
        "ipsc-derived nk", "induced pluripotent", "ink cell", "cd34+", "progenitor-derived nk",
        "nk-92", "nk92", "khyg", "nk cell line", "placental", "off-the-shelf",
        "allogeneic nk", "autologous nk", "donor selection", "kir-ligand mismatch",
        "hank", "tank", "universal donor", "cell source", "haplobank",
    ]),
    ("car_nk_engineering", [
        "car-nk", "car nk", "chimeric antigen receptor", "car-engineered",
        "car-expressing nk", "costimulatory domain", "dap10", "dap12", "2b4",
        "nkg2d car", "car construct", "transmembrane domain", "signaling domain",
        "lentiviral transduction", "baev", "baboon envelope", "retroviral transduction",
        "sleeping beauty", "transposon", "mrna electroporation", "aav",
        "trac locus", "site-specific integration",
        "synthetic receptor", "logic-gated", "switch receptor", "chimeric receptor",
        "car-t versus car-nk", "engineered nk cell",
    ]),
    ("nk_engagers", [
        "trike", "bike", "bispecific killer", "trispecific killer", "nk cell engager",
        "nkce", "innate cell engager", "afm13", "afm24", "nkp46 engager", "cd16 engager",
        "tetraspecific", "bispecific antibody & nk", "engager molecule",
    ]),
    ("gene_editing_knockouts", [
        "cish", "cis knockout", "socs3", "tgfbr2", "dominant negative tgf",
        "adam17", "cd16 shedding", "non-cleavable cd16", "nkg2a knockout",
        "klrc1", "tigit knockout", "pd-1 knockout", "cblb", "cbl-b", "zeb2",
        "ahr ", "regnase", "zc3h12a", "smad3", "knockout nk", "gene-edited nk",
        "crispr", "cas9", "base editing", "knockout", "knock-out", "gene editing",
        "crispr screen", "genome-wide screen", "checkpoint deletion", "deletion of",
        "silencing", "gene disruption",
    ]),
    ("metabolism_persistence", [
        "nk cell metabolism", "metabolic fitness", "metabolic reprogramming",
        "glycolysis", "oxphos", "oxidative phosphorylation", "fatty acid",
        "lipid accumulation", "cholesterol", "mitochondrial", "hypoxia",
        "hif-1alpha", "nutrient", "glutamine", "srebp", "mtor", "autophagy",
        "persistence in vivo", "nk cell survival", "apoptosis of nk",
    ]),
    ("cytokine_support", [
        "il-15", "interleukin-15", "il-15 superagonist", "n-803", "alt-803",
        "nogapendekin", "sil-15", "membrane-bound il-15", "mbil15", "il-15ralpha",
        "transpresentation", "il-21", "interleukin-21", "il-12", "il-18",
        "decoy-resistant il-18", "il-2 ", "interleukin-2", "cytokine-induced memory-like",
        "preactivation", "cytokine armoring", "armored nk", "autocrine",
        "cytokine cocktail", "cytokine stimulation",
    ]),
    ("expansion_feeders", [
        "nk cell expansion", "expansion of nk", "expanded nk", "ex vivo expansion",
        "large-scale expansion", "clinical-scale", "feeder cell", "feeder-free",
        "k562-mbil21", "41bbl", "4-1bbl", "mb15", "pm21", "plasma membrane particle",
        "ebv-lcl", "irradiated feeder", "aapc", "artificial antigen presenting",
        "g-rex", "gas-permeable", "bioreactor", "rocking motion", "wave bag",
        "serum-free", "xeno-free", "platelet lysate", "nk macs", "culture medium",
        "culture system", "expansion protocol", "fold expansion", "prodigy",
        "automated manufacturing", "closed system", "gmp-compliant", "gmp manufacturing",
        "manufacturing process", "process development", "scale-up", "cost of goods",
    ]),
    ("cryo_qc_manufacturing", [
        "cryopreservation", "cryopreserved", "freeze-thaw", "post-thaw", "dmso",
        "shelf-life", "formulation", "potency assay", "release testing",
        "release criteria", "critical quality attribute", "comparability",
        "vector copy number", "master cell bank", "identity testing", "sterility",
        "quality control", "cell product characterization", "fresh versus cryopreserved",
    ]),
    ("checkpoints_inhibitory", [
        "nkg2a", "monalizumab", "hla-e", "kir blockade", "lirilumab", "iph2101",
        "anti-kir", "tigit", "pvrig", "cd112r", "tim-3", "lag-3", "pd-1", "pd-l1",
        "cd96", "cd226", "siglec-7", "siglec-9", "inhibitory receptor",
        "nkg2d ligand shedding", "soluble mica", "mica shedding", "b7-h6",
        "cd73", "adenosine", "prostaglandin e2", "ido", "immune evasion",
        "resistance to nk", "nk cell escape", "mhc class i",
    ]),
    ("adcc_combinations", [
        "adcc", "antibody-dependent cellular cytotoxicity", "rituximab", "trastuzumab",
        "cetuximab", "dinutuximab", "obinutuzumab", "fc engineering", "afucosylated",
        "fcgr3a", "cd16 polymorphism", "checkpoint inhibitor combination",
        "radiotherapy", "chemotherapy", "lymphodepletion", "proteasome inhibitor",
        "bortezomib", "hdac inhibitor", "ezh2", "epigenetic", "combination therapy",
    ]),
    ("trafficking_solid_tme", [
        "trafficking", "homing", "infiltration", "chemokine receptor", "cxcr2",
        "ccr7", "cxcr4", "cxcr3", "intratumoral delivery", "intraperitoneal",
        "intracranial", "locoregional", "tumor microenvironment", "tumour microenvironment",
        "immunosuppressive microenvironment", "mdsc", "regulatory t cell",
        "cancer-associated fibroblast", "extracellular matrix", "solid tumor",
        "solid tumour",
    ]),
    ("clinical_nk", [
        "phase 1", "phase i ", "phase 2", "phase ii", "phase 1/2", "first-in-human",
        "clinical trial", "patients", "haploidentical", "infusion", "adoptive transfer",
        "ft500", "ft516", "ft576", "ft596", "nkx101", "nkx019", "snk01", "ab-101",
        "cynk-001", "gda-201", "gtb-3550", "cytokine release syndrome",
        "graft-versus-host", "complete remission", "objective response",
    ]),
]
AXIS_ORDER = [a for a, _ in AXES] + ["general_nk_therapy"]

DISEASES = [
    ("aml_mds", ["acute myeloid leukemia", "acute myeloid leukaemia", "aml", "myelodysplastic"]),
    ("lymphoma_cll", ["lymphoma", "chronic lymphocytic", "cll", "b-cell malignanc"]),
    ("myeloma", ["multiple myeloma", "myeloma"]),
    ("all_peds_heme", ["acute lymphoblastic", "b-all", "t-all"]),
    ("gbm_cns", ["glioblastoma", "glioma", "brain tumor", "brain tumour", "medulloblastoma",
                 "diffuse midline", "cns tumor", "brain metasta"]),
    ("neuroblastoma_sarcoma", ["neuroblastoma", "sarcoma", "osteosarcoma", "ewing",
                               "rhabdomyosarcoma"]),
    ("ovarian", ["ovarian"]),
    ("breast", ["breast cancer", "tnbc", "triple-negative"]),
    ("lung", ["lung cancer", "non-small cell lung", "nsclc"]),
    ("gi", ["colorectal", "gastric", "pancreatic", "hepatocellular", "liver cancer",
            "esophageal", "cholangiocarcinoma", "peritoneal"]),
    ("gu", ["renal cell", "prostate", "bladder", "urothelial"]),
    ("hnscc_melanoma", ["head and neck", "melanoma"]),
]

MANUF_WORDS = [
    "expansion", "expanded", "manufactur", "gmp", "feeder", "culture", "cultured",
    "bioreactor", "scale-up", "cryopreserv", "closed system", "clinical-scale",
    "potency assay", "release testing", "process development", "serum-free",
    "xeno-free", "medium", "media", "protocol", "fold increase", "fold expansion",
    "cell product", "prodigy", "cost of goods",
]
ENGINEER_WORDS = [
    "car", "chimeric antigen receptor", "crispr", "knockout", "knock-in", "gene-edited",
    "transduc", "electropor", "transposon", "lentivir", "retrovir", "engineered",
    "il-15", "il-21", "membrane-bound", "armored", "switch receptor", "trike", "bike",
    "engager", "base editing",
]
# A record has to be about NK cells as effectors/therapeutics, not merely mention them.
NK_RELEVANCE = [
    "nk cell", "nk cells", "nk-cell", "natural killer", "car-nk", "car nk", "nk-92",
    "nk92", "ipsc-nk", "innate lymphoid", "nkg2d", "nkg2a", "nkp46", "nkp30", "nkp44",
    "cd16", "kir", "trike", "bike",
]
NK_TITLE_WORDS = [
    "nk cell", "nk cells", "nk-cell", "nk-cells", "natural killer", "car-nk", "car nk",
    "nk-92", "nk92", "ipsc-nk", "nkg2d", "nkg2a", "nkp46", "nkp30", "cd16", "kir",
    "trike", "bike", "innate immune effector", "adcc",
]

TRIAL_PUBTYPES = ("clinical trial", "randomized controlled trial", "observational study")
REVIEW_WORDS = ["review", "perspective", "overview", "we discuss", "here we review",
                "current landscape", "state of the art"]
PRECLIN_WORDS = ["mice", "mouse", "murine", "xenograft", "nsg", "syngeneic", "orthotopic",
                 "in vivo", "organoid", "tumor-bearing", "tumour-bearing", "pdx"]
METHOD_WORDS = ["protocol", "we developed a", "we established", "process", "platform",
                "workflow", "manufacturing", "expansion of", "closed", "scalable"]


def has(text, needles):
    return any(n in text for n in needles)


def norm_title(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def evidence_of(rec, text, pt):
    if has(pt, TRIAL_PUBTYPES) or re.search(r"phase (1|2|3|i|ii|iii|1b|1/2)\b", text):
        return "clinical_trial"
    if "meta-analysis" in pt or "systematic review" in pt:
        return "systematic_review"
    if "review" in pt and "research-article" not in pt:
        return "review"
    if has(text, MANUF_WORDS) and has(text, METHOD_WORDS) and not has(text, PRECLIN_WORDS):
        return "process_method"
    if has(text, ["patients", "patient samples", "primary samples", "resected",
                  "biopsies", "donors"]) and has(
            text, ["single-cell", "scrna", "cohort", "ex vivo from patients",
                   "primary nk cells from"]):
        return "translational_human"
    if has(text, PRECLIN_WORDS):
        return "preclinical"
    if has(rec["title"].lower(), REVIEW_WORDS):
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
        return fallback if fallback in AXIS_ORDER else "general_nk_therapy"
    top, n = scores.most_common(1)[0]
    if n < 3:
        return "general_nk_therapy"
    if fallback in scores and scores[fallback] >= n - 1:
        return fallback
    return top


def disease_of(text):
    tags = [name for name, keys in DISEASES if has(text, keys)]
    if not tags:
        return "pan-cancer"
    return ";".join(tags[:3])


def venue_tier(venue):
    return 1 if venue.strip().lower() in TIER1 else 2


def keep(rec, text, pt):
    if not rec["title"] or len(rec["abstract"]) < 180:
        return False
    if has(pt, DROP_PUBTYPE):
        return False
    tl = rec["title"].lower()
    if has(tl, DROP_TITLE):
        return False
    if not has(text, NK_RELEVANCE):
        return False
    # NK cells must be a subject of the work, not an incidental mention.
    if not has(tl, NK_TITLE_WORDS) and text.count("nk cell") + text.count("natural killer") < 5:
        return False
    if has(text, DROP_CONTEXT) and not has(tl, ["cancer", "tumor", "tumour", "leukemia",
                                                "leukaemia", "lymphoma", "myeloma",
                                                "carcinoma", "melanoma", "glioma"]):
        return False
    if not has(text, ["cancer", "tumor", "tumour", "leukemia", "leukaemia", "lymphoma",
                      "myeloma", "carcinoma", "melanoma", "glioma", "sarcoma",
                      "neuroblastoma", "malignan", "antitumor", "antitumour",
                      "anti-tumor", "anti-tumour", "oncolog"]):
        return False
    try:
        year = int(rec["year"])
    except ValueError:
        return False
    return year >= MIN_YEAR


def score(rec, evidence, manuf, engineered, tier):
    year = int(rec["year"])
    age = max(1, 2026 - year)
    cited = rec["cited"] or 0
    s = 2.2 * math.log1p(cited) + 1.4 * math.log1p(cited / age)
    s += 3.0 if tier == 1 else 0.0
    s += {"clinical_trial": 3.4, "systematic_review": 1.2, "translational_human": 2.4,
          "process_method": 3.0, "review": 1.0, "preclinical": 1.8, "mechanistic": 0.8}[evidence]
    s += 1.2 if manuf else 0.0
    s += 0.8 if engineered else 0.0
    if year >= 2024:
        s += 2.0
    if year >= 2022:
        s += 0.8
    if rec["sweep"] == "foundational" and year <= 2015:
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
    quotas = [("clinical_trial", 3), ("process_method", 3), ("preclinical", 3),
              ("translational_human", 2), ("review", 2)]
    for ev, cap in quotas:
        for r in cands:
            if len(chosen) >= limit:
                break
            if r in chosen or r["evidence"] != ev or seen_ev[ev] >= cap:
                continue
            chosen.append(r)
            seen_ev[ev] += 1
    recent = [r for r in cands if int(r["year"]) >= 2024 and r not in chosen]
    for r in recent[:5]:
        if len(chosen) < limit:
            chosen.append(r)
    for r in cands:
        if len(chosen) >= limit:
            break
        if r not in chosen:
            chosen.append(r)
    chosen.sort(key=lambda r: -r["score"])
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
        evidence = evidence_of(rec, text, pt)
        manuf = has(text, MANUF_WORDS)
        engineered = has(text, ENGINEER_WORDS)
        tier = venue_tier(rec["venue"])
        item = dict(rec)
        item.update({
            "axis": axis,
            "evidence": evidence,
            "manufacturing": "yes" if manuf else "no",
            "engineered": "yes" if engineered else "no",
            "disease": disease_of(text),
            "tier": tier,
            "url": url_of(rec),
        })
        item["score"] = round(score(rec, evidence, manuf, engineered, tier), 2)
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

    cols = ["axis", "evidence", "disease", "manufacturing", "engineered", "authors",
            "title", "venue", "year", "cited", "pmid", "doi", "pmcid", "url",
            "local_fulltext", "status"]
    with open(TSV, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
        w.writerow(cols)
        for item in curated:
            w.writerow([
                item["axis"], item["evidence"], item["disease"], item["manufacturing"],
                item["engineered"], item["authors"], item["title"], item["venue"],
                item["year"], item["cited"], item["pmid"], item["doi"], item["pmcid"],
                item["url"], "", "oa_xml" if item["inEPMC"] == "Y" else "metadata_only",
            ])

    print(f"raw={len(raw)} dropped={dropped} pool={sum(len(v) for v in by_axis.values())} "
          f"curated={len(curated)}")
    for axis in AXIS_ORDER:
        sel = [r for r in curated if r["axis"] == axis]
        pool = len(by_axis.get(axis, []))
        if sel:
            evs = Counter(r["evidence"] for r in sel)
            print(f"  {axis:26s} {len(sel):3d}/{pool:4d}  {dict(evs)}")


if __name__ == "__main__":
    main()
