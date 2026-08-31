#!/usr/bin/env python3
"""Score, classify, and index harvested gamma-delta T-cell benchmarking literature.

Retention rules (title+abstract regex scoring):
  vd1_specific   Vdelta1 / Delta One T context plus any product, phenotype or
                 cytotoxicity signal - the closest comparators to a Vd1-enriched product.
  gdt_quant      any gamma-delta T-cell paper carrying a quantitative product or
                 killing readout (E:T ratio, % lysis, purity, fold expansion).
  dn_tcell       CD4-CD8- double-negative T-cell papers with a cytotoxicity or
                 product signal, gamma-delta or not - the DN gate is shared.
  landmark       reviews/consensus pieces defining the field's reference values.

Writes index.tsv sorted by category then year (desc), plus curated.json.
"""
import html
import json
import re
from collections import Counter

BASE = "/home/ubuntu/repos/lit-syn/papers/gdt-vd1-cytotoxicity-benchmarks"

# ---------------------------------------------------------------- agent context
GDT_AGENT = re.compile(
    r"(gamma[- ]?delta T|gammadelta T|γδ ?T|\bGD T cells?\b|TCR ?gamma[- ]?delta|"
    r"TCR ?γδ|\bTCRgd\b|V ?delta ?[12]\b|Vδ ?[12]\b|\bVd ?[12]\b|"
    r"V ?gamma ?9|Vγ ?9|\bVg9\b|delta one T|\bDOT cells?\b|"
    r"phosphoantigen|butyrophilin|\bBTN3A1\b|\bBTNL3\b)", re.I)
VD1_AGENT = re.compile(
    r"(V ?delta ?1\b|Vδ ?1\b|\bVd ?1\b|delta one T|\bDOT[- ]?cells?\b|\bDOT[- ]?CAR\b|"
    r"V ?gamma ?9[- ]?negative|non[- ]V ?delta ?2|Vdelta2[- ]?negative)", re.I)
DN_AGENT = re.compile(
    r"(CD4[- ]?/?\s?CD8[- ]?(double )?negative|CD4[-−]CD8[-−]|double[- ]negative T|"
    r"\bDNT cells?\b|\bDN T cells?\b|CD4 ?- ?CD8 ?- ?)", re.I)

# ---------------------------------------------------------------- domains
PATTERNS = {
    "cytotoxicity_et": r"\b(effector[ :/-]+to[ :/-]+target|effector ?: ?target|\bE ?: ?T\b|"
        r"E/T ratio|effector to target ratio|specific lysis|% ?lysis|percent lysis|"
        r"cytotox\w+ assay|killing assay|chromium[- ]51|51Cr|calcein|"
        r"luciferase[- ]based|xCELLigence|real[- ]time cell analysis|IncuCyte|"
        r"lactate dehydrogenase release|LDH release|\bkilling capacity\b|"
        r"serial killing|\bcytolytic\b)",
    "expansion_product": r"\b(expansion|expanded|fold[- ]expansion|manufactur\w+|"
        r"clinical[- ]grade|\bGMP\b|good manufacturing practice|bioreactor|"
        r"closed system|cell dose|release criteri\w+|feeder cells?|"
        r"artificial antigen[- ]presenting|zoledron\w+|pamidronat\w+|"
        r"aminobisphosphonat\w+|phosphoantigen|\bIPP\b|\bBrHPP\b|"
        r"isopentenyl pyrophosphate|\bOKT3\b|anti[- ]CD3|TransAct|"
        r"IL[- ]?(2|4|7|15|21)\b|purity|purif\w+|depletion|enrich\w+)",
    "phenotype_subsets": r"\b(phenotyp\w+|immunophenotyp\w+|\bCD27\b|\bCD45RA\b|\bCD62L\b|"
        r"na[iï]ve|central memory|effector memory|\bTEMRA\b|differentiation state|"
        r"\bNKG2D\b|\bDNAM[- ]?1\b|\bNKp(30|44|46)\b|\bCD16\b|granzyme|perforin|"
        r"\bTRAIL\b|Fas ?ligand|\bCD107a\b|degranulation|"
        r"exhaust\w+|\bPD[- ]?1\b|\bTIGIT\b|\bTIM[- ]?3\b|\bLAG[- ]?3\b|"
        r"repertoire|clonalit\w+|subset composition|frequency of)",
    "engineered": r"\b(chimeric antigen receptor|\bCAR[- ]?T\b|\bCAR\b|"
        r"TCR[- ]engineered|\bTEG\b|transduc\w+|electropor\w+|lentivir\w+|"
        r"bispecific|T[- ]cell engager|tribody|immunoligand|\bCRISPR\b|"
        r"gene[- ]edit\w+|knockout)",
    "clinical": r"\b(clinical trial|phase (1|I|1/2|I/II)\b|first[- ]in[- ]human|"
        r"patients? (received|treated|enrolled)|adoptive transfer|infusion|"
        r"haploidentical|stem cell transplant\w*|donor lymphocyte|"
        r"immune reconstitution|dose escalation|objective response|"
        r"complete remission|overall survival|safety and tolerability)",
    "target_disease": r"\b(leuk[ae]mi\w+|lymphom\w+|myelom\w+|blasts?\b|\bAML\b|\bALL\b|"
        r"\bCLL\b|solid tumou?rs?|glioma\w*|glioblastom\w+|neuroblastom\w+|"
        r"sarcom\w+|melanom\w+|colorect\w+|pancrea\w+|ovarian|breast cancer|"
        r"organoid|spheroid|patient[- ]derived xenograft|\bPDX\b)",
    "comparator": r"\b(compared (with|to)|versus\b|\bvs\.?\b|head[- ]to[- ]head|"
        r"benchmark\w*|standardi[sz]\w+|inter[- ]?(assay|laboratory) variabilit\w+|"
        r"\bNK cells?\b|alpha[- ]?beta T cells?|αβ T cells?|\bCIK cells?\b)",
}

# quantitative anchors: what makes a paper usable as a numeric benchmark
QUANT = re.compile(
    r"(\d{1,3}\s?(%|per ?cent)|\b\d{1,3}\s?:\s?1\b|\b1\s?:\s?\d{1,3}\b|"
    r"\b\d{1,4}[- ]fold\b|\bEC50\b|\bIC50\b|\bp\s?[<=]\s?0\.\d+)", re.I)
ET_EXPLICIT = re.compile(
    r"(effector[ :/-]+to[ :/-]+target|effector ?: ?target|\bE ?: ?T\b|E/T ratio|"
    r"\b(1|2|2\.5|3|4|5|10|20|25|50)\s?:\s?1\b)", re.I)

LANDMARKS = re.compile(
    r"\b(review|consensus|guideline|position paper|state of the art|perspective|"
    r"recommendations?|meta[- ]analysis|systematic review)\b", re.I)

EXCLUDE = re.compile(
    r"\b(cost[- ]effectiveness|bibliometric|patent landscape|market (access|analysis)|"
    r"health technology assessment|nursing (education|curriculum)|"
    r"gamma[- ]?delta (secretase|globulin)|gamma delta hydroxy|"
    r"delta[- ]?9[- ]?tetrahydro|photon|dosimetr\w+|"
    r"veterinary parasitolog\w+|Plasmodium (falciparum )?malaria vaccine trial)", re.I)

# The collection benchmarks anti-tumour cell products. Papers whose whole subject is an
# infectious or inflammatory disease describe gd T-cell biology in a setting where
# neither product purity nor E:T-anchored killing of tumour targets is reported.
THERAPY_CONTEXT = re.compile(
    r"\b(cancer|tumou?rs?|malignan\w+|leuk[ae]mi\w+|lymphom\w+|myelom\w+|"
    r"glioma\w*|glioblastom\w+|neuroblastom\w+|sarcom\w+|melanom\w+|carcinom\w+|"
    r"adoptive (cell|T[- ]cell|immuno)\w*|cell therapy|immunotherap\w+|"
    r"chimeric antigen receptor|\bCAR\b|T[- ]cell engager|cytotox\w+|"
    r"expansion|expanded|manufactur\w+|\bGMP\b|cell product)", re.I)
OFF_TOPIC_DISEASE = re.compile(
    r"\b(malaria|Plasmodium|tuberculosis|\bBCG\b|Mycobacteri\w+|COVID|SARS[- ]CoV|"
    r"influenza|dengue|\bHIV\b|\bSIV\b|hepatitis [BC]\b|\bHBV\b|\bHCV\b|"
    r"cytomegalovirus|\bCMV\b|Epstein[- ]Barr|sepsis|"
    r"colitis|Crohn|psoriasi\w+|alopecia|rhinosinusitis|nasal polyp|asthma|"
    r"lichen planus|diabetes|obesity|atheroscleros\w+|multiple sclerosis|"
    r"encephalomyelitis|arthritis|celiac|coeliac|periodont\w+|dermatitis|"
    r"pregnan\w+|placental|wound healing|vaccinat\w+)", re.I)

CATEGORY_ORDER = [
    "vd1_products",
    "gdt_cytotoxicity_benchmarks",
    "expansion_protocols",
    "phenotype_subsets",
    "double_negative_t",
    "engineered_gdt",
    "clinical_translation",
    "assay_methodology_comparators",
]


def score(text, patterns):
    hits = {}
    for name, pat in patterns.items():
        n = len(re.findall(pat, text, flags=re.I))
        if n:
            hits[name] = n
    return hits


def main():
    with open(f"{BASE}/raw_harvest.json") as f:
        records = json.load(f)

    kept = []
    for rec in records:
        rec["title"] = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html.unescape(rec["title"]))).strip()
        rec["abstract"] = re.sub(r"<[^>]+>", "", html.unescape(rec.get("abstract", "")))
        if not rec["title"]:
            continue
        text = f"{rec['title']} {rec['abstract']}"
        if EXCLUDE.search(text):
            continue

        hits = score(text, PATTERNS)
        title_hits = score(rec["title"], PATTERNS)
        gdt = bool(GDT_AGENT.search(text))
        gdt_title = bool(GDT_AGENT.search(rec["title"]))
        vd1 = bool(VD1_AGENT.search(text))
        dn = bool(DN_AGENT.search(text))
        quant = bool(QUANT.search(text))
        et = bool(ET_EXPLICIT.search(text))

        signal = sum(hits.get(k, 0) for k in
                     ("cytotoxicity_et", "expansion_product", "phenotype_subsets",
                      "engineered", "clinical"))
        signal += 2 * sum(title_hits.get(k, 0) for k in
                          ("cytotoxicity_et", "expansion_product", "phenotype_subsets"))

        onco = bool(THERAPY_CONTEXT.search(text))
        off_disease = bool(OFF_TOPIC_DISEASE.search(text)) and \
            not re.search(r"\b(cancer|tumou?rs?|leuk[ae]mi\w+|lymphom\w+|myelom\w+)", rec["title"], re.I)

        keep = False
        rationale = ""
        if off_disease and not (hits.get("expansion_product", 0) >= 3 and et):
            keep = False
        elif vd1 and onco and (hits.get("cytotoxicity_et") or hits.get("expansion_product")
                               or hits.get("engineered") or hits.get("clinical")):
            keep, rationale = True, "vd1_specific"
        elif gdt and onco and et and hits.get("cytotoxicity_et"):
            keep, rationale = True, "gdt_quant"
        elif gdt and onco and quant and signal >= 5:
            keep, rationale = True, "gdt_quant"
        elif dn and (gdt or hits.get("cytotoxicity_et") or hits.get("expansion_product")) \
                and onco and signal >= 3:
            keep, rationale = True, "dn_tcell"
        elif gdt_title and onco and LANDMARKS.search(rec["title"]) and signal >= 4:
            keep, rationale = True, "landmark"
        if not keep:
            continue

        # ---- primary category: the numeric axis wins, because a paper that anchors
        # killing to an explicit E:T ratio is usable as a benchmark whatever else it says
        category = "phenotype_subsets"
        if hits.get("phenotype_subsets", 0) < 2 and hits.get("expansion_product"):
            category = "expansion_protocols"
        if title_hits.get("expansion_product") or hits.get("expansion_product", 0) >= 4:
            category = "expansion_protocols"
        if hits.get("clinical", 0) >= 3 and hits.get("clinical", 0) > hits.get("cytotoxicity_et", 0):
            category = "clinical_translation"
        if hits.get("engineered", 0) >= 3 and (hits.get("cytotoxicity_et") or hits.get("clinical")):
            category = "engineered_gdt"
        if rationale == "dn_tcell" and not vd1:
            category = "double_negative_t"
        if rationale == "landmark" or (LANDMARKS.search(rec["title"]) and hits.get("comparator")):
            if not et:
                category = "assay_methodology_comparators"
        if vd1 and not et and category in ("phenotype_subsets", "expansion_protocols"):
            category = "vd1_products"
        if et and hits.get("cytotoxicity_et"):
            category = "gdt_cytotoxicity_benchmarks"

        topics = sorted(set(hits))
        if vd1:
            topics.append("vdelta1")
        if dn:
            topics.append("double_negative")
        if et:
            topics.append("et_ratio_reported")
        if quant:
            topics.append("quantitative")
        if re.search(r"\breview\b|systematic review|meta[- ]analysis",
                     rec.get("pubType", "") + " " + rec["title"], re.I):
            topics.append("review")
        if re.search(r"meeting abstract|conference abstract", rec.get("pubType", ""), re.I) or \
                re.match(r"[A-Z]{2,6}-\d{1,3}\.", rec["title"]):
            topics.append("meeting_abstract")

        rec.update({
            "category": category,
            "topics": ";".join(sorted(set(topics))),
            "signal": signal,
            "rationale": rationale,
        })
        kept.append(rec)

    # dedupe on normalized title (preprint + journal versions)
    by_title = {}
    for rec in kept:
        k = re.sub(r"[^a-z0-9]", "", rec["title"].lower())[:90]
        prev = by_title.get(k)
        if prev is None:
            by_title[k] = rec
        elif (rec.get("pmid") and not prev.get("pmid")) or \
                (rec.get("src") == "MED" and prev.get("src") == "PPR"):
            by_title[k] = rec
    kept = list(by_title.values())

    kept.sort(key=lambda r: (CATEGORY_ORDER.index(r["category"]) if r["category"] in CATEGORY_ORDER else 99,
                             -int(r["year"] or 0), r["authors"][:20]))

    cols = ["category", "authors", "title", "venue", "year", "pmid", "doi", "pmcid",
            "url", "fulltext_xml", "topics", "status"]
    with open(f"{BASE}/index.tsv", "w") as f:
        f.write("\t".join(cols) + "\n")
        for r in kept:
            if r.get("pmcid"):
                url = f"https://pmc.ncbi.nlm.nih.gov/articles/{r['pmcid']}/"
            elif r.get("doi"):
                url = f"https://doi.org/{r['doi']}"
            elif r.get("pmid"):
                url = f"https://pubmed.ncbi.nlm.nih.gov/{r['pmid']}/"
            else:
                url = ""
            row = [r["category"], r["authors"], r["title"], r["venue"], r["year"],
                   r.get("pmid", ""), r.get("doi", ""), r.get("pmcid", ""), url,
                   "", r["topics"], "metadata_only"]
            f.write("\t".join(c.replace("\t", " ") for c in row) + "\n")

    with open(f"{BASE}/curated.json", "w") as f:
        json.dump(kept, f, indent=1)

    print(f"kept {len(kept)} of {len(records)}")
    for c, n in Counter(r["category"] for r in kept).most_common():
        print(f"  {c}: {n}")
    print("rationale:", Counter(r["rationale"] for r in kept))


if __name__ == "__main__":
    main()
