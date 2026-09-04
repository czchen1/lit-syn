#!/usr/bin/env python3
"""Score, classify, and index harvested ANKTIVA/N-803 formulation-and-route literature.

Retention rules (title+abstract regex scoring):
  n803_bladder     N-803/ALT-803/nogapendekin records in a bladder/intravesical setting -
                   the approved use under evaluation.
  n803_systemic    the same molecule in any other indication, kept only when it carries
                   route, PK, formulation or systemic-toxicity signal, because that is
                   where IV/SC exposure to this exact construct is characterised.
  il15_route       IL-15 agonist papers that carry route, PK or systemic-toxicity signal,
                   i.e. what IV/SC exposure to this class actually does.
  intravesical_pk  intravesical papers with a pharmacokinetic, dilution, dwell-time or
                   urine-chemistry readout - the quantitative basis for the 50-mL step.
  intravesical_bio intravesical delivery of proteins/biologics/gene therapy, where the
                   urothelial barrier and formulation enhancers determine feasibility.
  local_vs_systemic explicit local-versus-systemic route comparisons for immune agonists.
  landmark         reviews/guidelines that define instillation technique or the class.

Writes index.tsv sorted by category then year (desc), plus curated.json.
"""
import html
import json
import re
from collections import Counter

BASE = "/home/ubuntu/repos/lit-syn/papers/anktiva-formulation-intravesical-vs-iv"

# ---------------------------------------------------------------- agent context
N803_AGENT = re.compile(
    r"(\bN-?803\b|\bALT-?803\b|nogapendekin|inbakicept|ANKTIVA|"
    r"IL-?15 ?N72D|IL-?15N72D|IL-?15 ?super-?agonist|interleukin-?15 super-?agonist|"
    r"IL-?15 ?/ ?IL-?15R ?alpha|IL-?15Ra ?Su|IL-?15R ?alpha sushi)", re.I)
IL15_AGENT = re.compile(
    r"(interleukin-?1?5\b|\bIL-?15\b|rhIL-?15|hetIL-?15|heterodimeric IL-?15|"
    r"\bRLI\b|SO-?C101|NIZ ?985|XmAb ?24306|NKTR-?255|efbalropendekin|"
    r"IL-?15 (receptor )?agonist)", re.I)
IVES_AGENT = re.compile(
    r"(intravesical\w*|bladder instillation|instill\w+ into the bladder|"
    r"intravesic\w+|bladder infusion|intracavitary (bladder|vesical))", re.I)
CYTOKINE_AGENT = re.compile(
    r"(cytokine|interleukin|interferon|\bIL-?[0-9]{1,2}\b|\bTNF\b|GM-?CSF|"
    r"immune agonist|immunostimulant|TLR agonist|STING agonist)", re.I)

# ---------------------------------------------------------------- domains
PATTERNS = {
    "route_comparison": r"\b(intravenous\w*|\bi\.?v\.?\b|subcutaneous\w*|\bs\.?c\.?\b|\bSQ\b|"
        r"intramuscular|route of administration|systemically administered|"
        r"systemic administration|parenteral)",
    "pharmacokinetics": r"\b(pharmacokinetic\w*|\bPK\b|C ?max|\bAUC\b|half[- ]life|t ?1/2|"
        r"clearance|bioavailab\w+|serum concentration\w*|plasma concentration\w*|"
        r"plasma level\w*|systemic exposure|systemic absorption|"
        r"below the (lower )?limit of quantitation|undetectable|"
        r"drug concentration\w*|urine concentration\w*|tissue concentration\w*)",
    "dilution_dwell": r"\b(dilut\w+|urine volume|residual urine|urine (output|production)|"
        r"diuresis|hydration|dehydrat\w+|fluid restrict\w+|"
        r"dwell time|retention time|instillation (time|volume)|contact time|"
        r"exposure time|voiding|urinary pH|urine pH|alkaliniz\w+|"
        r"sodium bicarbonate|osmolality|ionic strength|"
        r"instilled volume|50 ?mL|40-60 ?mL)",
    "formulation": r"\b(formulat\w+|excipient\w*|diluent|reconstitut\w+|admixture|"
        r"compatibilit\w+|in-?use stability|stabilit\w+|aggregat\w+|adsorpt\w+|"
        r"protein binding to|catheter|syringe|container closure|"
        r"hydrogel|in situ gel\w*|thermal gel|mucoadhesiv\w+|liposom\w+|"
        r"nanoparticle\w*|nanomedicine|sustained[- ]release|controlled[- ]release|"
        r"drug delivery system|chitosan|permeation enhancer|\bSyn3\b|"
        r"intravesical delivery system|pretzel)",
    "barrier_penetration": r"\b(urothelial permeabilit\w+|bladder permeabilit\w+|"
        r"permeation|penetrat\w+|barrier function|glycosaminoglycan|\bGAG layer\b|"
        r"umbrella cells|tight junction\w*|mucus|mucin|"
        r"molecular weight|molecular size|\bkDa\b|transmural)",
    "systemic_toxicity": r"\b(cytokine release syndrome|\bCRS\b|capillary leak|"
        r"systemic toxicit\w+|systemic side effects|hypotension|fever|pyrexia|chills|"
        r"dose[- ]limiting toxicit\w+|\bDLT\b|maximum tolerated dose|\bMTD\b|"
        r"grade [3-5] (adverse|toxicit)\w*|treatment[- ]emergent adverse)",
    "clinical": r"\b(clinical trial|phase (1|I|1b|Ib|1/2|I/II|2|II|3|III)\b|"
        r"first[- ]in[- ]human|patients? (received|treated|enrolled)|"
        r"complete response|recurrence[- ]free|disease[- ]free survival|"
        r"single[- ]arm|randomi[sz]ed|dose escalation)",
    "bladder_cancer": r"\b(bladder cancer|urothelial (carcinoma|cancer)|\bNMIBC\b|"
        r"non[- ]muscle[- ]invasive|carcinoma in situ|\bCIS\b|\bTa\b|\bT1\b|"
        r"transitional cell carcinoma|\bTURBT\b|BCG[- ]unresponsive|"
        r"bacillus Calmette|\bBCG\b)",
}

QUANT = re.compile(
    r"(\d+(\.\d+)? ?(ng|pg|µg|μg|mcg|mg|g)/(m?L|kg)|\d+ ?mL\b|\d+(\.\d+)? ?(h|hours?|min)\b|"
    r"\d{1,3}\s?%|\bp\s?[<=]\s?0\.\d+|\d+(\.\d+)?[- ]fold)", re.I)

LANDMARKS = re.compile(
    r"\b(review|narrative review|consensus|guideline\w*|position paper|"
    r"recommendations?|meta[- ]analysis|systematic review|"
    r"FDA approval summary|state of the art)\b", re.I)

EXCLUDE = re.compile(
    r"\b(cost[- ]effectiveness|bibliometric|patent landscape|market (access|analysis)|"
    r"health technology assessment|nursing (education|curriculum)|"
    r"quality of life questionnaire validation|"
    r"interleukin-?15 (polymorphism|gene variant)|"
    r"\bIL-?15 in (schizophrenia|depression|periodontitis)\b)", re.I)

# Intravesical / IL-15 papers about non-oncologic bladder or immune disease describe a
# setting where neither route selection for a tumour-directed agonist nor instillation
# pharmacokinetics is at issue.
OFF_TOPIC = re.compile(
    r"\b(interstitial cystitis|bladder pain syndrome|overactive bladder|"
    r"detrusor overactivity|neurogenic bladder|botulinum|urinary incontinence|"
    r"vesicoureteral reflux|enuresis|urolithiasis|benign prostatic|"
    r"celiac|coeliac|rheumatoid|psoriasi\w+|multiple sclerosis|"
    r"graft[- ]versus[- ]host prophylaxis|transplant rejection)", re.I)
ONCO_CONTEXT = re.compile(
    r"\b(cancer|tumou?r\w*|malignan\w+|carcinoma|neoplas\w+|oncolog\w+|"
    r"immunotherap\w+|antitumou?r|anti[- ]tumou?r|chemotherap\w+|"
    r"leuk[ae]mi\w+|lymphom\w+|melanom\w+|\bNMIBC\b|\bBCG\b)", re.I)

CATEGORY_ORDER = [
    "n803_anktiva_bladder",
    "n803_systemic_other_indications",
    "il15_systemic_route_pk",
    "intravesical_pk_dilution",
    "intravesical_biologics_barrier",
    "formulation_delivery_systems",
    "local_vs_systemic_immunotherapy",
    "bladder_cancer_context",
    "reviews_guidelines",
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
        n803 = bool(N803_AGENT.search(text))
        il15 = bool(IL15_AGENT.search(text))
        ives = bool(IVES_AGENT.search(text))
        ives_title = bool(IVES_AGENT.search(rec["title"]))
        cyto = bool(CYTOKINE_AGENT.search(text))
        quant = bool(QUANT.search(text))
        onco = bool(ONCO_CONTEXT.search(text))
        off = bool(OFF_TOPIC.search(text)) and not ONCO_CONTEXT.search(rec["title"])

        signal = sum(hits.get(k, 0) for k in
                     ("route_comparison", "pharmacokinetics", "dilution_dwell",
                      "formulation", "barrier_penetration", "systemic_toxicity"))
        signal += 2 * sum(title_hits.get(k, 0) for k in
                          ("pharmacokinetics", "dilution_dwell", "formulation",
                           "barrier_penetration"))

        keep = False
        rationale = ""
        if off and not n803:
            keep = False
        elif n803 and (hits.get("bladder_cancer") or ives):
            keep, rationale = True, "n803_bladder"
        elif n803 and (hits.get("route_comparison") or hits.get("pharmacokinetics")
                       or hits.get("formulation") or hits.get("systemic_toxicity")):
            keep, rationale = True, "n803_systemic"
        elif il15 and onco and (hits.get("route_comparison") or hits.get("pharmacokinetics")
                                or hits.get("systemic_toxicity")) and signal >= 3:
            keep, rationale = True, "il15_route"
        elif ives and (hits.get("pharmacokinetics") or hits.get("dilution_dwell")) and quant \
                and signal >= 3:
            keep, rationale = True, "intravesical_pk"
        elif ives and (hits.get("formulation") or hits.get("barrier_penetration")) \
                and onco and signal >= 4:
            keep, rationale = True, "intravesical_bio"
        elif ives and cyto and hits.get("route_comparison") and onco and signal >= 3:
            keep, rationale = True, "local_vs_systemic"
        elif ives_title and LANDMARKS.search(rec["title"]) and onco and signal >= 3:
            keep, rationale = True, "landmark"
        if not keep:
            continue

        # ---- primary category: the molecule wins, then the quantitative axis that makes
        # a paper usable for the route/dilution argument, then context
        category = "bladder_cancer_context"
        if hits.get("bladder_cancer") and (hits.get("formulation") or hits.get("barrier_penetration")):
            category = "formulation_delivery_systems"
        if hits.get("barrier_penetration", 0) >= 2 and ives:
            category = "intravesical_biologics_barrier"
        if ives and (hits.get("dilution_dwell") or hits.get("pharmacokinetics", 0) >= 2):
            category = "intravesical_pk_dilution"
        if rationale == "local_vs_systemic":
            category = "local_vs_systemic_immunotherapy"
        if rationale == "il15_route":
            category = "il15_systemic_route_pk"
        if rationale == "landmark" and not hits.get("dilution_dwell"):
            category = "reviews_guidelines"
        if rationale == "n803_systemic":
            category = "n803_systemic_other_indications"
        if rationale == "n803_bladder":
            category = "n803_anktiva_bladder"

        topics = sorted(set(hits))
        if n803:
            topics.append("n803_alt803")
        if il15 and not n803:
            topics.append("il15_agonist")
        if ives:
            topics.append("intravesical")
        if hits.get("dilution_dwell"):
            topics.append("dilution_or_dwell")
        if hits.get("route_comparison") and hits.get("pharmacokinetics"):
            topics.append("route_pk")
        if quant:
            topics.append("quantitative")
        if re.search(r"\breview\b|systematic review|meta[- ]analysis|guideline",
                     rec.get("pubType", "") + " " + rec["title"], re.I):
            topics.append("review")
        if re.search(r"meeting abstract|conference abstract", rec.get("pubType", ""), re.I) or \
                re.match(r"[A-Z]{2,6}-\d{1,3}\.", rec["title"]):
            topics.append("meeting_abstract")
        if re.search(r"\b(mice|mouse|murine|rat|rats|dog|dogs|monkey|macaque|"
                     r"preclinical|in vivo model)\b", text, re.I):
            topics.append("preclinical")

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
