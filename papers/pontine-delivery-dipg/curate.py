#!/usr/bin/env python3
"""Score, classify, and index harvested pontine/brainstem delivery literature.

Inclusion logic (title+abstract regex scoring):
  disease_score  — brainstem/pons/DIPG/DMG specificity
  modality_score — concrete delivery route/technique content
  A record is retained when it is either
    (a) brainstem/pontine-specific AND carries any delivery signal, or
    (b) a strong, generalizable CNS delivery-technique paper (high modality
        score) that informs pontine delivery even if not brainstem-specific.
Writes index.tsv sorted by category then year (desc).
"""
import html
import json
import re
from collections import Counter

BASE = "/home/ubuntu/repos/lit-syn/papers/pontine-delivery-dipg"

DISEASE_PATTERNS = {
    "dipg_dmg": r"\b(diffuse intrinsic pontine glioma|DIPG|DIPGs|diffuse midline glioma|DMG\b|H3\s?K27M|H3K27-altered|H3\.3\s?K27M)",
    "brainstem": r"\b(brainstem|brain stem|pons\b|pontine|ponto|medulla oblongata|midbrain|thalamic glioma|fourth ventricle)",
    "pediatric_hgg": r"\b(pediatric high-grade glioma|paediatric high-grade glioma|pHGG|pediatric glioma|paediatric glioma|childhood glioma)",
    "other_cns": r"\b(glioblastoma|glioma|medulloblastoma|ependymoma|leptomeningeal|Parkinson|amyotrophic lateral sclerosis|spinal muscular atrophy|leukodystrophy|multiple sclerosis|CNS tumou?r|brain tumou?r)",
}

MODALITY_PATTERNS = {
    "convection_enhanced_delivery": r"\b(convection[- ]enhanced delivery|CED\b|interstitial infusion|intratumou?ral infusion|intraparenchymal infusion|positive[- ]pressure infusion)",
    "focused_ultrasound": r"\b(focused ultrasound|MRgFUS|LIFU\b|sonication|microbubble|sonodynamic|histotripsy|ultrasound[- ]mediated)",
    "intra_arterial": r"\b(intra[- ]?arterial|superselective|SIACI|osmotic (blood[- ]brain barrier|BBB) disruption|mannitol|basilar artery infusion|endovascular (delivery|infusion))",
    "intrathecal_csf": r"\b(intrathecal|intraventricular|intracerebroventricular|intra[- ]?CSF|Ommaya|intracisternal|lumbar puncture delivery|glymphatic)",
    "cell_therapy_delivery": r"\b(CAR[ -]?T|chimeric antigen receptor|locoregional (delivery|administration)|neural stem cell|mesenchymal stem cell|cell[- ]based (delivery|carrier)|NK cell (infusion|therapy))",
    "viral_vector": r"\b(oncolytic|adeno[- ]associated virus|\bAAV\b|adenovirus|DNX-2401|herpes simplex virus|poliovirus|reovirus|lentiviral vector|viral vector)",
    "nanoparticle": r"\b(nanoparticle|nanocarrier|liposom|lipid nanoparticle|\bLNP\b|micelle|dendrimer|exosome|extracellular vesicle|polymeric nanop|nanomedicine)",
    "intranasal": r"\b(intranasal|nose[- ]to[- ]brain|olfactory (route|delivery)|trigeminal (route|pathway))",
    "systemic_bbb_pharmacology": r"\b(blood[- ]brain barrier|blood[- ]tumou?r barrier|brain penetrat|P[- ]glycoprotein|ABCB1|ABCG2|efflux transporter|unbound brain|Kp,?uu|CSF penetration|pharmacokinetic)",
    "implant_depot_device": r"\b(implant|Gliadel|carmustine wafer|wafer|hydrogel|drug[- ]eluting|refillable|indwelling catheter|subcutaneous port|microdevice|microneedle|depot)",
    "imaging_dosimetry_modeling": r"\b(real[- ]time (MR|MRI)|co[- ]infusion|surrogate tracer|dosimetry|computational model|finite element|simulation of (infusion|distribution)|diffusion tensor|volume of distribution|Vd/Vi|biodistribution)",
    "surgical_access": r"\b(stereotactic biopsy|brainstem biopsy|catheter (placement|trajectory|design)|safe entry zone|transcerebellar|trajectory planning|neuronavigation|robot[- ]assisted|frameless)",
    "radiation_combined": r"\b(re[- ]?irradiation|radiotherapy|radiosensitiz|brachytherapy|boron neutron capture|radioimmunotherapy|radiolabel|radiation[- ]induced (permeability|BBB))",
    "antibody_conjugate_shuttle": r"\b(antibody[- ]drug conjugate|\bADC\b|immunotoxin|receptor[- ]mediated transcytosis|transferrin receptor|BBB shuttle|molecular Trojan horse|bispecific.*(transport|shuttle))",
}

# Categories in report order. First matched (by score, then this order) wins.
CATEGORY_ORDER = [
    "convection_enhanced_delivery",
    "focused_ultrasound",
    "intra_arterial",
    "intrathecal_csf",
    "cell_therapy_delivery",
    "viral_vector",
    "nanoparticle",
    "intranasal",
    "implant_depot_device",
    "antibody_conjugate_shuttle",
    "systemic_bbb_pharmacology",
    "imaging_dosimetry_modeling",
    "surgical_access",
    "radiation_combined",
]

# Modalities that constitute a *route/technique* contribution (as opposed to
# background pharmacology) -- used for the generalizable-technique pathway.
CORE_ROUTES = {
    "convection_enhanced_delivery", "focused_ultrasound", "intra_arterial",
    "intrathecal_csf", "intranasal", "implant_depot_device",
    "antibody_conjugate_shuttle", "nanoparticle", "viral_vector",
    "cell_therapy_delivery",
}

# For the related-disease pathway only invasive/physical routes count: generic
# nanomedicine or nose-to-brain reviews in neurodegeneration add no pontine
# delivery evidence, whereas catheter, CSF-port and FUS experience does.
DIRECT_ROUTES = {
    "convection_enhanced_delivery", "intrathecal_csf", "focused_ultrasound",
    "intra_arterial", "implant_depot_device",
}
DIRECT_ADMIN = re.compile(
    r"\b(convection[- ]enhanced|intraparenchymal|intraputaminal|intrastriatal|"
    r"intrathecal|intraventricular|intracerebroventricular|intracisternal|Ommaya|"
    r"catheter|port|pump|implant|focused ultrasound|intra[- ]?arterial|infusion)", re.I)

# non-oncologic CNS diseases whose direct-delivery experience transfers to the pons
NEURO_DISEASE = re.compile(
    r"\b(Parkinson|AADC|aromatic L-amino acid decarboxylase|Gaucher|glucocerebrosidase|"
    r"spinal muscular atrophy|nusinersen|onasemnogene|amyotrophic lateral sclerosis|"
    r"Huntington|Alzheimer|leukodystroph|mucopolysaccharidos|lysosomal storage|"
    r"neuronal ceroid lipofuscinos|CLN2|cerliponase|Canavan|Rett syndrome|"
    r"essential tremor|drug-resistant epilepsy|enzyme replacement)", re.I)

TUMOR = re.compile(r"\b(glioma|glioblastoma|GBM\b|medulloblastoma|ependymoma|brain tumou?r|CNS tumou?r|brain metasta|neuro-?oncolog|leptomeningeal)", re.I)

EXCLUDE = re.compile(
    r"\b(pontine (infarct|stroke|hemorrhage|haemorrhage)|central pontine myelinolysis|"
    r"pontine tegmental|auditory brainstem response|brainstem auditory evoked|"
    r"brainstem death|brain death|pontine micturition|"
    r"pontocerebellar hypoplasia|arteriovenous fistula|acute ischemic stroke|"
    r"thrombolysis|tenecteplase|alteplase|thrombectomy|pontine perforator|"
    r"locked-in syndrome|olivopontocerebellar)", re.I)

# health-services / utilization papers carry no delivery-methods content
OFF_TOPIC = re.compile(r"\b(technology appraisal|health (services|technology) (research|assessment)|"
                      r"utilization and treatment continuity|cost-effectiveness|insurance claims|"
                      r"questionnaire survey of (parents|clinicians)|"
                      r"glymphatic (differences|function) in healthy|healthy (adults|volunteers) at)", re.I)


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
        text = f"{rec['title']} {rec.get('abstract','')}"
        if not rec["title"]:
            continue
        if EXCLUDE.search(text) and not re.search(DISEASE_PATTERNS["dipg_dmg"], text, re.I):
            continue
        if OFF_TOPIC.search(text):
            continue

        # diagnostic case reports/imaging mimics carry no delivery content unless
        # the report is itself about a route
        if re.search(r"case report|illustrative case|mimick|differential diagnosis", rec["title"], re.I) \
                and not re.search(r"|".join(MODALITY_PATTERNS[k] for k in CORE_ROUTES), rec["title"], re.I):
            continue

        dhits = score(text, DISEASE_PATTERNS)
        mhits = score(text, MODALITY_PATTERNS)
        if not mhits:
            continue

        brainstem_specific = ("dipg_dmg" in dhits) or ("brainstem" in dhits)
        # title-level evidence is much stronger than abstract-level
        title_mhits = score(rec["title"], MODALITY_PATTERNS)
        route_hits = {k: v for k, v in mhits.items() if k in CORE_ROUTES}
        title_route_hits = {k: v for k, v in title_mhits.items() if k in CORE_ROUTES}

        modality_score = sum(route_hits.values()) + 2 * sum(title_route_hits.values())
        disease_score = 3 * dhits.get("dipg_dmg", 0) + 2 * dhits.get("brainstem", 0) \
            + dhits.get("pediatric_hgg", 0)

        keep = False
        rationale = ""
        if brainstem_specific and disease_score >= 2:
            # brainstem/DIPG-specific delivery paper: route, BBB pharmacology,
            # or the surgical/imaging technique that enables local delivery
            support = bool(title_mhits) or modality_score >= 2 or \
                ("systemic_bbb_pharmacology" in mhits and dhits.get("dipg_dmg"))
            if support:
                keep, rationale = True, "brainstem_specific"
        if not keep and title_route_hits and modality_score >= 8 and TUMOR.search(text):
            # generalizable CNS delivery-technique paper
            keep, rationale = True, "cns_technique"
        if not keep and NEURO_DISEASE.search(text) and modality_score >= 4 and \
                set(title_route_hits) & DIRECT_ROUTES and DIRECT_ADMIN.search(rec["title"]):
            # related-disease delivery paper (catheter/CSF/FUS experience transfers)
            keep, rationale = True, "related_disease"

        if not keep:
            continue

        # primary category: highest-scoring modality, tie-broken by CATEGORY_ORDER
        def cat_key(name):
            s = mhits.get(name, 0) + 2 * title_mhits.get(name, 0)
            return (-s, CATEGORY_ORDER.index(name) if name in CATEGORY_ORDER else 99)

        cats = sorted(mhits.keys(), key=cat_key)
        category = cats[0]

        topics = sorted(set(list(mhits.keys()) + [k for k in dhits if k != "other_cns"]))
        if rationale == "related_disease":
            topics.append("related_disease")
        if re.search(r"meeting abstract|conference abstract", rec.get("pubType", ""), re.I) or \
                re.match(r"[A-Z]{2,6}-\d{1,3}\.", rec["title"]):
            topics.append("meeting_abstract")
        rec.update({
            "category": category,
            "topics": ";".join(topics),
            "disease_score": disease_score,
            "modality_score": modality_score,
            "rationale": rationale,
        })
        kept.append(rec)

    # dedupe by normalized title (preprint + journal versions)
    by_title = {}
    for rec in kept:
        k = re.sub(r"[^a-z0-9]", "", rec["title"].lower())[:90]
        prev = by_title.get(k)
        if prev is None:
            by_title[k] = rec
        else:
            # prefer the journal (MED) version with a pmid
            if (rec.get("pmid") and not prev.get("pmid")) or rec.get("src") == "MED" and prev.get("src") == "PPR":
                by_title[k] = rec
    kept = list(by_title.values())

    kept.sort(key=lambda r: (CATEGORY_ORDER.index(r["category"]) if r["category"] in CATEGORY_ORDER else 99,
                             -int(r["year"] or 0), r["authors"][:20]))

    cols = ["category", "authors", "title", "venue", "year", "pmid", "doi", "pmcid",
            "url", "local_pdf", "fulltext_xml", "topics", "status"]
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
                   "", "", r["topics"], "metadata_only"]
            f.write("\t".join(c.replace("\t", " ") for c in row) + "\n")

    with open(f"{BASE}/curated.json", "w") as f:
        json.dump(kept, f, indent=1)

    print(f"kept {len(kept)} of {len(records)}")
    for c, n in Counter(r["category"] for r in kept).most_common():
        print(f"  {c}: {n}")
    print("rationale:", Counter(r["rationale"] for r in kept))
    print("years:", sorted(Counter(r["year"] for r in kept).items())[:5], "...")


if __name__ == "__main__":
    main()
