#!/usr/bin/env python3
"""Score, classify, and index harvested GD2 CAR-T toxicity literature.

Retention rules (title+abstract regex scoring):
  gd2_specific        GD2-directed agent (CAR or antibody) AND a toxicity/organ signal.
  cart_toxicity       any CAR/engineered-cell therapy with toxicity evidence in the
                      title and a strong toxicity score — mechanism, incidence,
                      grading or management that transfers to a GD2 product.
  cns_route           locoregional/ICV/intrathecal CNS cell therapy with a safety signal.
  pharmacology        inflammation-, cytokine- or critical-illness-driven changes in
                      drug handling (CYP suppression, clearance) and explicit DDI work,
                      even without CAR-T context — the interaction layer of the question.

Writes index.tsv sorted by category then year (desc), plus curated.json.
"""
import html
import json
import re
from collections import Counter

BASE = "/home/ubuntu/repos/lit-syn/papers/gd2-car-t-toxicity"

# ---------------------------------------------------------------- agent context
GD2_AGENT = re.compile(
    r"\b(GD2\b|GD2-|disialoganglioside|14[.\s]?g2a|14G2a|hu14\.18|ch14\.18|dinutuximab|"
    r"naxitamab|3F8\b|GD2-CART01|anti-GD2)", re.I)
CART_AGENT = re.compile(
    r"\b(CAR[ -]?T\b|CAR[ -]?T[- ]cells?|chimeric antigen receptor|CAR[- ]NK|CAR[- ]NKT|"
    r"CAR[- ]macrophage|engineered T cells?|TCR[- ]engineered|adoptive (cell|T[- ]cell) "
    r"(therapy|transfer)|immune effector cells?|bispecific T[- ]cell engager|blinatumomab)", re.I)
CELLTHER = re.compile(r"\b(CAR|T[- ]cell|NK cell|cell therapy|cellular (therapy|immunotherapy))", re.I)

# ---------------------------------------------------------------- toxicity domains
TOX_PATTERNS = {
    "cytokine_release_syndrome": r"\b(cytokine release syndrome|\bCRS\b|cytokine storm|"
        r"hypercytokinemia|tocilizumab|siltuximab|anakinra|capillary leak|"
        r"interleukin[- ]6|IL[- ]6\b|ferritin|C[- ]reactive protein)",
    "neurotoxicity": r"\b(neurotoxic\w*|ICANS|immune effector cell[- ]associated neurotoxicity|"
        r"CRES\b|encephalopath\w+|seizure|status epilepticus|cerebral (o?edema)|"
        r"tumou?r inflammation[- ]associated neurotoxicity|\bTIAN\b|intracranial pressure|"
        r"hydrocephalus|external ventricular drain|obstructive hydrocephalus|"
        r"posterior fossa|brainstem (o?edema|dysfunction)|aphasia|tremor|"
        r"cranial (nerve|neuropathy)|CARTOX)",
    "on_target_off_tumor": r"\b(on[- ]target,? off[- ]tumou?r|off[- ]tumou?r toxicity|"
        r"neuropathic pain|allodynia|peripheral neuropath\w+|nerve (pain|injury)|"
        r"normal tissue expression|healthy tissue|melanocyte|retinal|ocular toxicity|"
        r"pruritus|dermatologic)",
    "hepatic": r"\b(hepatotoxic\w*|liver (injury|dysfunction|failure|enzyme|toxicity)|"
        r"hepatic (dysfunction|injury|impairment|failure|toxicity)|transaminas\w+|"
        r"transaminitis|\bALT\b|\bAST\b|aminotransferase|hyperbilirubin\w+|bilirubin|"
        r"sinusoidal obstruction syndrome|veno[- ]occlusive|Child[- ]Pugh|"
        r"hepatic clearance|hypoalbumin\w+)",
    "renal_electrolyte": r"\b(acute kidney injury|\bAKI\b|nephrotoxic\w*|renal "
        r"(dysfunction|impairment|failure|insufficiency|clearance)|creatinine|"
        r"glomerular filtration|dialysis|tumou?r lysis syndrome|hyponatr\w+|"
        r"\bSIADH\b|hypophosphat\w+|hypokal\w+|electrolyte|fluid overload|"
        r"augmented renal clearance)",
    "hematologic_coagulopathy": r"\b(cytopeni\w+|\bICAHT\b|neutropeni\w+|thrombocytopeni\w+|"
        r"an?emia|aplasia|marrow (suppression|recovery)|h?ematopoietic recovery|"
        r"coagulopath\w+|disseminated intravascular coagulation|\bDIC\b|fibrinogen|"
        r"D[- ]dimer|bleeding|h?emorrhage|thrombos\w+|transfusion)",
    "hlh_mas": r"\b(h?emophagocytic|\bHLH\b|macrophage activation syndrome|\bMAS\b|"
        r"IEC[- ]HS|carHLH|hyperferritin\w+)",
    "cardiopulmonary": r"\b(cardiotoxic\w*|cardiac (dysfunction|toxicity|event)|arrhythmi\w+|"
        r"ejection fraction|\bQT\b|myocardi\w+|hypotension|vasopressor|"
        r"respiratory failure|hypox\w+|pulmonary o?edema|\bARDS\b|"
        r"mechanical ventilation|intensive care)",
    "infection_immune": r"\b(infection\w*|febrile neutropenia|sepsis|septic|"
        r"hypogammaglobulin\w+|immune reconstitution|opportunistic|"
        r"antimicrobial prophylaxis|viral reactivation|cytomegalovirus|"
        r"B[- ]cell aplasia|immunosuppress\w+)",
    "drug_interaction_pk": r"\b(drug[- ]drug interaction|drug interaction|"
        r"cytochrome P450|CYP3A4?|CYP1A2|CYP2C\d|pharmacokinetic\w*|drug metabolism|"
        r"drug clearance|concomitant medication|polypharmacy|therapeutic drug monitoring|"
        r"dose adjustment|protein binding|hepatic (metabolism|extraction))",
    "steroids_immunomodulation": r"\b(corticosteroid|dexamethasone|methylprednisolone|"
        r"glucocorticoid|steroid (use|exposure|refractory)|anakinra|ruxolitinib|"
        r"dasatinib|emapalumab|cyclophosphamide.*fludarabine|lymphodeplet\w+)",
    "mitigation_engineering": r"\b(safety switch|inducible caspase|iCasp9|iC9\b|rimiducid|"
        r"suicide gene|EGFRt|RQR8|logic gate|\bAND gate\b|affinity[- ]tun\w+|"
        r"E101K|armou?red CAR|dose escalation|split dosing|fractionated dosing)",
    "grading_management": r"\b(ASTCT|consensus (grading|guideline)|grading (system|criteria)|"
        r"management (algorithm|guideline|recommendation)|CTCAE|"
        r"toxicity management|supportive care|risk (stratification|factor)s? for)",
}

# route / delivery context (not itself a toxicity, but the modifier the question is about)
ROUTE_PATTERNS = {
    "icv_intraventricular": r"\b(intracerebroventricular|intraventricular|intra[- ]?CSF|"
        r"Ommaya|Rickham|intrathecal|intracisternal|ventricular (catheter|reservoir)|"
        r"lumbar (puncture|intrathecal))",
    "locoregional_cns": r"\b(locoregional|loco[- ]regional|intratumou?ral|intracavitary|"
        r"intracranial (delivery|administration|injection)|convection[- ]enhanced)",
    "systemic_iv": r"\b(intravenous(ly)?|systemic(ally)? (administered|infusion|delivery))",
}

DISEASE_PATTERNS = {
    "neuroblastoma": r"\b(neuroblastom\w+|high[- ]risk neuroblastoma)",
    "dmg_dipg": r"\b(diffuse midline glioma|diffuse intrinsic pontine glioma|DIPG|H3\s?K27M|"
        r"H3K27[- ]altered|brainstem glioma|spinal cord glioma)",
    "other_solid": r"\b(osteosarcom\w+|Ewing|sarcom\w+|melanom\w+|small[- ]cell lung|"
        r"medulloblastom\w+|glioblastom\w+|retinoblastom\w+|"
        r"breast cancer|solid tumou?rs?)",
    "hematologic_malignancy": r"\b(leuk?emi\w+|lymphom\w+|myelom\w+|\bALL\b|\bDLBCL\b|\bCLL\b)",
    "pediatric": r"\b(pediatric|paediatric|children|childhood|infant|adolescent)",
}

# Landmark records that must be in the index regardless of scoring: the trials and
# mechanism papers the synthesis is built on. Matched on title.
LANDMARKS = re.compile(
    r"(GD2-CAR T Cell Therapy for H3K27M|Intravenous and intracranial GD2-CAR|"
    r"GD2-CART01|long-term fate of chimeric antigen receptor|"
    r"Virus-specific T cells engineered to coexpress|"
    r"without on-target off-tumou?r toxicity of GD2|"
    r"Fatal Encephalitis|anti-GD2 CAR T cells in H3-K27M|"
    r"Intracerebroventricular B7-H3|B7-H3-targeting CAR T cells|"
    r"Locoregional infusion of HER2-specific CAR T cells|"
    r"CARv3-TEAM-E|bivalent CAR T cells targeting EGFR|"
    r"inflammation-associated neurotoxicity|ASTCT Consensus Grading|"
    r"assessment and management of toxicities|"
    r"Endothelial Activation and Blood-Brain Barrier Disruption|"
    r"Monocyte-derived IL-1 and IL-6|abated by IL-1 blockade|"
    r"Hemophagocytic Lymphohistiocytosis-Like Syndrome|"
    r"hematotoxicity: mechanisms|CAR-HEMATOTOX|"
    r"Disease-Drug Interaction of Sarilumab|"
    r"Regulation of drug-metabolizing enzymes and transporters in inflammation|"
    r"Impact of Inflammation on Cytochromes P450 Activity in Pediatric)", re.I)

PRECLINICAL = re.compile(
    r"\b(mice|mouse|murine|\bNSG\b|xenograft|rat\b|rats\b|canine|dog\b|"
    r"non[- ]human primate|macaque|rhesus|cynomolgus|in vitro|in vivo|"
    r"syngeneic|immunocompetent model|humani[sz]ed mouse|organoid|"
    r"histopatholog\w+|preclinical)", re.I)
# Evidence that human subjects were actually treated/observed, as opposed to a
# preclinical paper whose discussion merely mentions patients.
CLINICAL = re.compile(
    r"\b(phase (1|2|3|I|II|III)\b|first[- ]in[- ]human|clinical trial|"
    r"patients (were|was|received|underwent|treated|enrolled|had)|"
    r"we (treated|enrolled|infused|report(ed)? \d+ patients)|"
    r"\d+ (patients|children|participants|subjects)|"
    r"case (series|report)|single[- ]arm|cohort of|"
    r"children and young adults|real[- ]world|registry|"
    r"retrospective (study|analysis|review)|prospective (study|trial|cohort))", re.I)

CATEGORY_ORDER = [
    "gd2_cart_clinical",
    "gd2_cart_preclinical",
    "cns_locoregional_delivery",
    "neurotoxicity",
    "cytokine_release_syndrome",
    "hlh_mas",
    "on_target_off_tumor",
    "hepatic",
    "renal_electrolyte",
    "hematologic_coagulopathy",
    "cardiopulmonary",
    "infection_immune",
    "drug_interaction_pk",
    "steroids_immunomodulation",
    "mitigation_engineering",
    "grading_management",
]

ORGAN_DOMAINS = {"hepatic", "renal_electrolyte", "hematologic_coagulopathy",
                 "cardiopulmonary", "hlh_mas"}

EXCLUDE = re.compile(
    r"\b(cost[- ]effectiveness|health technology assessment|budget impact|"
    r"market (access|analysis)|bibliometric|patent landscape|"
    r"nursing (education|curriculum)|questionnaire (of|survey of) (nurses|parents)|"
    r"GD2 synthase (structure|crystal)|ganglioside (analysis|extraction) method|"
    r"mass spectrometry (method|profiling) of ganglioside)", re.I)

# ---------------------------------------------------------------- pharmacology layer
# Only inflammation-driven changes in drug handling are wanted. Routine
# population-PK/dosing papers for individual antimicrobials in the ICU carry no
# information about how CAR-T-associated inflammation alters concomitant drugs.
PK_TITLE = re.compile(
    r"\b(cytochrome P450|CYP\s?\d|CYP[- ]mediated|drug[- ]metabolizing|drug metabolism|"
    r"drug[- ]drug interaction|disease[- ]drug interaction|drug interaction|"
    r"pharmacokinetic (alteration|change|variabilit|consequence)|metabolic clearance|"
    r"therapeutic protein.*interaction|dose (adjustment|modification))", re.I)
INFLAM_TITLE = re.compile(
    r"\b(inflammat\w+|cytokine|interleukin|IL[- ]6|tocilizumab|sarilumab|siltuximab|"
    r"acute[- ]phase|sepsis|septic|critical(ly)? ill|critical illness|"
    r"CAR[ -]?T|chimeric antigen receptor|monoclonal antibod\w+|therapeutic protein|"
    r"biologic\w*|immunotherap\w+|infection|rheumatoid|Crohn|colitis)", re.I)
PK_OFF_TOPIC = re.compile(
    r"\b(population pharmacokinetics?|dosing (simulation|optimi[sz]ation|regimen|strategy)|"
    r"meropenem|vancomycin|piperacillin|cefepime|ceftazidime|polymyxin|colistin|"
    r"gentamicin|amikacin|tobramycin|linezolid|daptomycin|fluconazole|caspofungin|"
    r"micafungin|melatonin|propolis|aflatoxin|biotoxin|herbal|flavonoid|"
    r"grapefruit|curcumin|pesticide|heavy metal|nanoparticle-induced|"
    r"continuous (renal|kidney) replacement therapy|neonatal (ICU|intensive)|"
    r"preterm infants?)", re.I)


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

        thits = score(text, TOX_PATTERNS)
        title_thits = score(rec["title"], TOX_PATTERNS)
        rhits = score(text, ROUTE_PATTERNS)
        title_rhits = score(rec["title"], ROUTE_PATTERNS)
        dhits = score(text, DISEASE_PATTERNS)
        if not thits:
            continue

        tox_score = sum(thits.values()) + 2 * sum(title_thits.values())
        gd2 = bool(GD2_AGENT.search(text))
        gd2_title = bool(GD2_AGENT.search(rec["title"]))
        cart = bool(CART_AGENT.search(text))
        icv = "icv_intraventricular" in rhits or "locoregional_cns" in rhits
        icv_title = bool(set(title_rhits) & {"icv_intraventricular", "locoregional_cns"})

        keep = False
        rationale = ""
        if gd2 and (cart or CELLTHER.search(text)) and tox_score >= 2:
            keep, rationale = True, "gd2_specific"
        elif gd2_title and tox_score >= 3:
            # anti-GD2 antibody toxicity: the on-target/off-tumour biology is shared
            keep, rationale = True, "gd2_specific"
        if not keep and cart and title_thits and tox_score >= 6:
            keep, rationale = True, "cart_toxicity"
        cns_context = bool(re.search(
            r"\b(CNS|central nervous system|brain|glioma|glioblastom\w+|medulloblastom\w+|"
            r"leptomening\w+|spinal|neuroblastom\w+|DIPG|midline glioma|intracranial)",
            text, re.I))
        if not keep and cart and icv and cns_context and \
                (icv_title or bool(title_thits)) and tox_score >= 3:
            keep, rationale = True, "cns_route"
        if not keep and not cart:
            # pharmacology layer: inflammation changing drug handling. Both halves of
            # the claim must be in the title, and drug-specific ICU dosing work is out.
            if PK_TITLE.search(rec["title"]) and INFLAM_TITLE.search(rec["title"]) \
                    and not PK_OFF_TOPIC.search(rec["title"]) \
                    and thits.get("drug_interaction_pk", 0) >= 2:
                keep, rationale = True, "pharmacology"
        if not keep and LANDMARKS.search(rec["title"]):
            keep, rationale = True, "landmark"
        if not keep:
            continue

        # ---- primary category
        def cat_key(name):
            s = thits.get(name, 0) + 2 * title_thits.get(name, 0)
            return (-s, CATEGORY_ORDER.index(name) if name in CATEGORY_ORDER else 99)

        cats = sorted(thits.keys(), key=cat_key)
        category = cats[0]
        # a paper reporting treated patients is clinical even when it also contains
        # the mouse work that preceded them
        preclin = bool(PRECLINICAL.search(text)) and not CLINICAL.search(text)
        # route trumps organ system: CSF-delivered cell therapy is the collection's axis
        if cart and icv and cns_context:
            category = "cns_locoregional_delivery"
        # GD2 identity trumps route: a GD2 trial stays with the GD2 trials
        if rationale in ("gd2_specific", "landmark") and gd2 and cart:
            category = "gd2_cart_preclinical" if preclin else "gd2_cart_clinical"

        topics = sorted(set(list(thits) + list(rhits) + list(dhits)))
        if gd2:
            topics.append("gd2_agent")
        topics.append("preclinical" if preclin else "clinical")
        if re.search(r"meeting abstract|conference abstract", rec.get("pubType", ""), re.I) or \
                re.match(r"[A-Z]{2,6}-\d{1,3}\.", rec["title"]):
            topics.append("meeting_abstract")
        if re.search(r"\breview\b|systematic review|meta[- ]analysis", rec.get("pubType", "") + " " + rec["title"], re.I):
            topics.append("review")
        if set(thits) & ORGAN_DOMAINS:
            topics.append("organ_function")

        rec.update({
            "category": category,
            "topics": ";".join(sorted(set(topics))),
            "tox_score": tox_score,
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
