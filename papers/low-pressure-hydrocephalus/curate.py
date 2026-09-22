#!/usr/bin/env python3
"""Curate the raw Europe PMC harvest into index.tsv + curated.json.

Low-/negative-pressure hydrocephalus is a rare entity whose evidence base is
case reports, small series and a handful of mechanistic papers, so — unlike the
oncology collections in this repo — case reports, letters and editorials are
retained (they carry the definitional debate) and the core axis is kept in full
rather than quota-sampled. Supporting literature (biomechanics, treatment
technology, adjacent differentials) is filtered by vocabulary and capped.

Pipeline:
  1. Split records into (a) core — title/abstract names the entity, or describes
     ventriculomegaly with low / sub-atmospheric ICP; (b) historical — pre-1994
     use of "low-pressure hydrocephalus" as a synonym for normal-pressure
     hydrocephalus (Adams/Hakim), tagged separately so it is not read as the
     modern entity; (c) supporting — biomechanics, treatment technology,
     etiological settings, adjacent differentials.
  2. Drop errata, abstract-less non-core stubs, off-topic "negative pressure"
     (wound therapy, lower-body negative pressure, ventilation) and NPH-only work
     that never touches low pressure or brain compliance.
  3. Tag evidence class, population, precipitating setting and treatment
     technique from title/abstract vocabulary; score by relevance, citations
     (age-normalised) and recency; cap supporting axes.
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

MODERN_ENTITY_YEAR = 1994  # Pang & Altschuler, Neurosurgery 1994

CAP = {
    "core_lph": 200,
    "historical_lph_as_nph": 40,
    "mechanism_biomechanics": 50,
    "treatment_techniques": 30,
    "etiology_settings": 25,
    "adjacent_differentials": 30,
}
AXIS_ORDER = ["core_lph", "mechanism_biomechanics", "treatment_techniques",
              "etiology_settings", "adjacent_differentials", "historical_lph_as_nph"]

# Manual review after the vocabulary pass: core-axis records whose abstract
# mentions low/negative ICP + ventriculomegaly only incidentally are re-homed to
# the axis they actually inform, or dropped (None); a few supporting records
# cited in notes/ are pinned so caps cannot remove them.
MANUAL_AXIS = {
    "31464808": "mechanism_biomechanics",  # Dirrichs 2019, infant shear-wave elastography
    "34687356": "mechanism_biomechanics",  # Aunan-Diop 2022, MRE in NPH scoping review
    "21316637": "mechanism_biomechanics",  # Shulyakov 2011, age-dependent viscoelasticity
    "33631603": "mechanism_biomechanics",  # Wagshul 2021, MRE in early-onset hydrocephalus
    "26848844": "mechanism_biomechanics",  # Juge 2016, rat brain stiffness in hydrocephalus
    "21273925": "adjacent_differentials",  # Staykov 2011, lumboventricular pressure gradient
    "27581321": "mechanism_biomechanics",  # Barami 2016, cerebral venous overdrainage
    "26274984": "mechanism_biomechanics",  # Kim 2016, periventricular lucency poroelastic model
    "40258946": "mechanism_biomechanics",  # Nozaleda 2025, pulsation-driven glymphatic flow
    "22806081": "mechanism_biomechanics",  # Shulyakov 2012, acute experimental hydrocephalus
    "32331966": "mechanism_biomechanics",  # Solamen 2021, poroelastic MRE in NPH
    "26671218": "mechanism_biomechanics",  # Chou 2016, multi-compartment poroelastic model
    "7373397": "mechanism_biomechanics",   # Welch 1980, ICP in infants
    "26045579": "mechanism_biomechanics",  # Hatt 2015, MRE during jugular compression
    "30474714": "mechanism_biomechanics",  # Sainz 2019, venous hypertension / turgor
    "12111485": "treatment_techniques",    # Czosnyka 2002, UK shunt evaluation
    "24405071": "treatment_techniques",    # Chari 2014, Cambridge shunt lab
    "22153319": "adjacent_differentials",  # Eide 2012, ICP waves in overdrainage
    "23991845": "adjacent_differentials",  # Bateman 2013, hypertensive SVS
    "8194056": "mechanism_biomechanics",   # Rekate 1994, mathematical modelling
    "10068806": None,   # absent cistern sign / LP shunt function
    "10766893": None,   # cognition after shunting in spina bifida
    "11453379": None,   # ventriculopleural shunt + ventilation
    "7931383": None,    # mesencephalic cysts
    "9235521": None,    # perceptive activity (historical LPH, no abstract)
    "39305690": None,   # seizures after cranioplasty
    "37593330": None,   # papillary glioneuronal tumour (NPH-like)
    "39760505": None,   # titanium mesh exposure
    "34414834": "etiology_settings",  # post-traumatic hydrocephalus cohort
    "36994490": "etiology_settings",  # hydrocephalus in disorders of consciousness
}

CORE_RE = re.compile(
    r"(low|negative|very low|ultra-low|low-? ?(or|and) negative)[- ]pressure hydroceph"
    r"|hydrocephalus with (very )?low pressure|silpah|inappropriately low[- ]pressure"
    r"|very low pressure hydroceph|low-pressure acute hydroceph|negative-pressure hydroceph"
    r"|low pressure hydrocephalic|negative pressure hydrocephalic", re.I)
# Describes the phenomenon without naming it.
SECONDARY_RE = re.compile(
    r"(sub-?atmospheric|sub-?zero|negative|below atmospheric|below zero)[- ](pressure )?"
    r"(drain|drainage|evd|ventriculostomy|external ventricular|intracranial pressure|icp)"
    r"|negative intracranial pressure hydroceph"
    r"|(low|negative) (intracranial pressure|icp).{0,120}(ventriculomegaly|ventricular (enlargement|dilat)|enlarged ventric)"
    r"|(ventriculomegaly|ventricular (enlargement|dilat)|enlarged ventric).{0,120}(low|negative|normal or low) (intracranial pressure|icp)"
    r"|(ventriculomegaly|ventricular (enlargement|dilat)).{0,80}(patent|functioning|working|functional) shunt"
    r"|(patent|functioning|working) shunt.{0,80}(ventriculomegaly|ventricular (enlargement|dilat))"
    r"|symptomatic low intracranial pressure|low-pressure shunt .malfunction|brain turgor"
    r"|neck wrap|cervical (collar|wrap).{0,80}(ventric|hydroceph|shunt)|jugular (venous )?compression.{0,80}(ventric|hydroceph|shunt)"
    r"|(ventriculomegaly|ventricular enlargement) despite", re.I)
HYDRO_RE = re.compile(
    r"hydroceph|ventriculomegaly|ventricular (enlargement|dilat|size|volume)|enlarged ventric"
    r"|\bshunt|ventriculostomy|ventricular drain|csf diversion|cerebrospinal fluid diversion", re.I)
MECH_RE = re.compile(
    r"transmantle|brain turgor|viscoelastic|brain (elasticity|stiffness|compliance)|elastance"
    r"|pressure-volume|hysteresis|cortical subarachnoid space|ventricular volume regulation"
    r"|windkessel|mathematical model|computational model|finite[- ]element|poroelastic"
    r"|biomechanic|elastography|non-?linear dynamics|pulse[- ]wave encephalopathy"
    r"|venous (outflow|drainage|hypertension|collapse|overdrainage)|sagittal sinus pressure"
    r"|pressure gradient|classification of hydrocephalus|definition of hydrocephalus"
    r"|hydrodynamic|cerebrospinal compensatory reserve|compensatory reserve", re.I)
TREAT_RE = re.compile(
    r"external ventricular drain|ventriculostomy|evd\b|lumbar drain|shunt valve|programmable"
    r"|adjustable|anti-?siphon|siphon|gravitational|drainage level|drain height|titrat"
    r"|weaning|catheter|third ventriculostomy|\betv\b|intracranial pressure monitoring"
    r"|icp monitoring|negative[- ]pressure (shunt|pump)|pumping", re.I)
ADJ_RE = re.compile(
    r"slit[- ]ventricle|overdrainage|over-drainage|intracranial hypotension|csf hypotension"
    r"|low (csf|cerebrospinal fluid) pressure|siphon|craniocerebral disproportion", re.I)
HIST_RE = re.compile(r"low[- ]pressure hydroceph", re.I)
VENTRIC_RE = re.compile(r"ventriculomegaly|ventricular (enlargement|dilat)|enlarged ventric|hydroceph", re.I)
STRONG_MECH_RE = re.compile(
    r"transmantle|brain turgor|viscoelastic|elasticity|stiffness|compliance|elastance|pressure-volume"
    r"|hysteresis|cortical subarachnoid space|windkessel|elastography|biomechanic|finite[- ]element"
    r"|poroelastic|mathematical model|classification of hydrocephalus|definition of hydrocephalus"
    r"|venous (outflow|drainage|hypertension|collapse)|compensatory reserve|pulse[- ]wave encephalopathy", re.I)

DROP_PUBTYPE = {"published erratum", "retraction of publication", "retracted publication",
                "correction"}
DROP_TEXT = re.compile(
    r"lower[- ]body negative pressure|negative[- ]pressure wound|negative pressure ventilation"
    r"|negative pressure (room|isolation)|portosystemic|blalock|extracorporeal|pulmonary artery"
    r"|intraocular pressure|glaucoma|turtle|mitral|ophthalmic artery|hydrothorax"
    r"|\bascites\b|arteriovenous co2|minute ventilation|abdominal magnetic resonance elastography"
    r"|laparoscop|pneumoperitoneum|myocardial|uterine|cortical malformations in childhood"
    r"|phase-contrast mri: physics|foreign body|serotonin|lorazepam|citrobacter|staphylococcus"
    r"|superior mesenteric|coccidioid|hummingbird|lothian|high altitude|mucopolysaccharid"
    r"|hypoxanthine|tuberculoma|virchow-robin|akinetic mutism|dopamine agonist|neurocysticercosis"
    r"|endoplasmic reticulum|choroid plexus papilloma|spaceflight|microgravity|head-down tilt"
    r"|evoked (potential|response)|very low birth weight|hollow mandrin|intraoperative brain relaxation"
    r"|microcephalic|genetic signatures|brain barriers|pleural space|epidural effusion|arrhythmogenic"
    r"|syringomyelia|intrahepatic|upward migration|catheter kinking|arachnoid cysts|craniosynostosis"
    r"|tuberculous meningitis|ferritin|vestibular schwannoma|multiple sclerosis|management style among"
    r"|fifteen-minute consultation|acetazolamide and furosemide|frameless stereotactic|chiari pseudotumor"
    r"|brain injury rehabilitation|lumboperitoneal shunts for the treatment of normal"
    r"|human heart|intrathoracic pressure regulator|dermoid cyst", re.I)
PNEUMO_RE = re.compile(r"pneumocephalus", re.I)
NPH_RE = re.compile(r"normal[- ]pressure hydroceph|\binph\b|\bnph\b|idiopathic normal", re.I)

REVIEW_PT = ("review",)
SYSREV_RE = re.compile(r"systematic review|meta-analysis|systematic literature", re.I)
CASE_REPORT_RE = re.compile(r"case report|illustrative case|report of (a|one|two|three|2|3) cases?"
                            r"|a case of|\bcase:|video case|pearls & oy-sters|we (report|present|describe) (a|an|the case)", re.I)
SERIES_RE = re.compile(r"case series|\b\d+ (consecutive )?(patients|cases|children)\b|series of|cohort"
                       r"|retrospective (review|study|analysis)|prospective|consecutive|all patients", re.I)
EXPERIMENTAL_RE = re.compile(r"\b(dogs?|canine|cats?|feline|rats?|rabbits?|kaolin|animal model|experimental (hydrocephalus|normal))\b"
                             r"|in vitro|bench test|shunt evaluation laboratory|postmortem|cadaver", re.I)
MODEL_RE = re.compile(r"mathematical model|computational|finite[- ]element|simulation|lumped|poroelastic"
                      r"|windkessel|quantitative model|theoretical", re.I)
COMMENT_PT = ("letter", "comment", "editorial")
CONSENSUS_RE = re.compile(r"consensus|guideline", re.I)

PEDIATRIC_RE = re.compile(r"\b(child|children|pediatric|paediatric|infant|infants|neonat|newborn|boy|girl"
                          r"|adolescent|teenage|\d+[- ](year|month)[- ]old (boy|girl|child))", re.I)
ADULT_RE = re.compile(r"\badults?\b|\b\d{2}[- ]year[- ]old (man|woman|male|female)\b|elderly|\bmen\b|\bwomen\b", re.I)

SETTINGS = [
    ("sah_aneurysm", re.compile(r"subarachnoid h(a)?emorrhage|aneurysm|\bsah\b|vasospasm", re.I)),
    ("tumor_posterior_fossa", re.compile(r"tumou?r|glioma|medulloblastoma|ependymoma|hemangioblastoma"
                                         r"|meningioma|craniopharyngioma|pineal|papilloma|glioneuronal|metasta", re.I)),
    ("skull_base_csf_leak", re.compile(r"csf leak|cerebrospinal fluid leak|fistula|pseudomeningocele|skull base"
                                       r"|cranial base|transsphenoidal|endonasal|dural (tear|defect)|rhinorrh", re.I)),
    ("lumbar_puncture_or_drain", re.compile(r"lumbar (puncture|drain|drainage|csf)|spinal drain", re.I)),
    ("craniectomy_skin_flap", re.compile(r"craniectomy|cranioplasty|sinking (skin )?flap|trephined|hemispherectomy"
                                         r"|hemicraniectomy|paradoxical herniation|titanium mesh", re.I)),
    ("infection_inflammatory", re.compile(r"meningitis|ventriculitis|infection|sepsis|coccidio|tubercul", re.I)),
    ("trauma", re.compile(r"traumatic|head injury|\btbi\b|post-?traumatic", re.I)),
    ("intraventricular_hemorrhage", re.compile(r"intraventricular h(a)?emorrhage|\bivh\b|posth(a)?emorrhagic", re.I)),
    ("shunt_dependent_prior", re.compile(r"shunted|ventriculoperitoneal|shunt (malfunction|failure|revision)|vp shunt|\bvps\b", re.I)),
    ("aqueductal_obstructive", re.compile(r"aqueduct|obstructive hydroceph|non-?communicating|trapped|isolated fourth|fourth ventric", re.I)),
]
TREATMENTS = [
    ("subzero_evd", re.compile(r"sub-?atmospheric|sub-?zero|negative[- ]pressure (drain|evd|ventriculostomy|external)"
                               r"|below (atmospheric|zero)|negative (drainage )?(level|pressure) (drain|evd)|(drain|evd)[^.]{0,60}(negative|below zero|sub-?zero|-\d+ ?(cm|mm))", re.I)),
    ("titrated_evd", re.compile(r"titrat|external ventricular drain|ventriculostomy|\bevd\b|drainage level|gradual|weaning", re.I)),
    ("neck_wrapping", re.compile(r"neck wrap|cervical (collar|wrap)|jugular (venous )?compression|neck compression", re.I)),
    ("positioning", re.compile(r"trendelenburg|head-down|flat position|supine|bed rest|positioning", re.I)),
    ("etv", re.compile(r"third ventriculostomy|\betv\b|endoscopic", re.I)),
    ("shunt_or_valve", re.compile(r"shunt|valve|programmable|adjustable|anti-?siphon|siphon|catheter", re.I)),
    ("active_pump_shunt", re.compile(r"active pump|pumping|negative[- ]pressure shunt|improvised shunt|bernoulli|valveless", re.I)),
    ("icp_monitoring", re.compile(r"intracranial pressure monitor|icp monitor|pressure monitoring|infusion test|pressure-volume", re.I)),
    ("csf_leak_repair", re.compile(r"leak repair|repair of|dural repair|blood patch|fat graft|sealed|fistula (closure|repair)", re.I)),
    ("pharmacologic", re.compile(r"theophylline|acetazolamide|caffeine|aminophylline", re.I)),
    ("elastography_imaging", re.compile(r"elastography|phase-contrast|cine mri|frontal horn ratio|evans", re.I)),
]

TIER1 = {
    "journal of neurosurgery", "neurosurgery", "journal of neurosurgery. pediatrics",
    "lancet (london, england)", "brain : a journal of neurology", "neurology",
    "acta neurochirurgica", "child's nervous system : chns : official journal of the international society for pediatric neurosurgery",
    "british journal of neurosurgery", "world neurosurgery", "neurocritical care",
    "journal of clinical neuroscience : official journal of the neurosurgical society of australasia",
    "neurosurgical focus", "ajnr. american journal of neuroradiology", "journal of the neurological sciences",
    "journal of neurology, neurosurgery, and psychiatry", "fluids and barriers of the cns",
    "cerebrospinal fluid research", "journal of biomechanics", "epilepsia",
}


def norm_title(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def url_of(rec):
    if rec["pmcid"]:
        return f"https://pmc.ncbi.nlm.nih.gov/articles/{rec['pmcid']}/"
    if rec["pmid"]:
        return f"https://pubmed.ncbi.nlm.nih.gov/{rec['pmid']}/"
    if rec["doi"]:
        return f"https://doi.org/{rec['doi']}"
    return ""


def year_of(rec):
    try:
        return int(rec["year"])
    except (ValueError, TypeError):
        return 0


def classify_axis(rec, text, title):
    year = year_of(rec)
    if PNEUMO_RE.search(title) and not CORE_RE.search(title):
        return "adjacent_differentials"
    if CORE_RE.search(text) or (SECONDARY_RE.search(text) and VENTRIC_RE.search(text)):
        if year and year < MODERN_ENTITY_YEAR and HIST_RE.search(text) and not SECONDARY_RE.search(text):
            return "historical_lph_as_nph"
        if year >= MODERN_ENTITY_YEAR and HIST_RE.search(text) and NPH_RE.search(text) \
                and not CORE_RE.search(title) and not SECONDARY_RE.search(text) \
                and re.search(r"dementia|gait|incontinence|cerebral blood flow|cisternograph", text, re.I):
            return "historical_lph_as_nph"
        return "core_lph"
    if not HYDRO_RE.search(text):
        return None
    if year and year < MODERN_ENTITY_YEAR and HIST_RE.search(text):
        return "historical_lph_as_nph"
    if ADJ_RE.search(title):
        return "adjacent_differentials"
    if STRONG_MECH_RE.search(title) or (rec["domain"] == "mechanism_biomechanics"
                                        and MECH_RE.search(title) and STRONG_MECH_RE.search(text)):
        return "mechanism_biomechanics"
    if rec["domain"] == "treatment_techniques" and TREAT_RE.search(title) and \
            re.search(r"low[- ]pressure|negative[- ]pressure|sub-?atmospheric|zero|drainage (level|height)"
                      r"|titrat|siphon|weaning|programmable|adjustable|pressure monitoring|opening pressure", text, re.I):
        return "treatment_techniques"
    if rec["domain"] in ("etiology_settings", "treatment_techniques", "adjacent_differentials") and re.search(
            r"csf leak|cerebrospinal fluid leak|fistula|pseudomeningocele|paradoxical herniation"
            r"|lumbar puncture|lumbar drain|craniectomy|cranioplasty|sinking|trephined|hemispherectomy"
            r"|lumbar-ventricular|pressure discrepancy", title, re.I) and \
            re.search(r"low pressure|low-pressure|negative pressure|intracranial hypotension|ventriculomegaly"
                      r"|ventricular (enlargement|dilat)|hydroceph", text, re.I):
        return "etiology_settings"
    if rec["domain"] == "adjacent_differentials" and re.search(
            r"classification|definition|pathophysiology|pathogenesis|theory|revisited|wrong question|should\) know", title, re.I):
        return "adjacent_differentials"
    return None


def evidence_of(rec, text, title, pt):
    if any(p in pt for p in COMMENT_PT) and "research-article" not in pt:
        return "comment_letter"
    if CONSENSUS_RE.search(title):
        return "consensus_guideline"
    if SYSREV_RE.search(text) or "systematic review" in pt or "meta-analysis" in pt:
        return "systematic_review"
    if "case reports" in pt or "case-report" in pt or CASE_REPORT_RE.search(title):
        if SERIES_RE.search(text) and re.search(r"\b([2-9]|[1-9]\d+) (patients|cases|children|consecutive)\b", text, re.I):
            return "case_series"
        return "case_report"
    if EXPERIMENTAL_RE.search(text) and not re.search(r"\bpatients\b", title, re.I):
        return "experimental"
    if MODEL_RE.search(title) or (MODEL_RE.search(text) and rec["domain"] == "mechanism_biomechanics"
                                  and not re.search(r"\bpatients\b", title, re.I)):
        return "computational_model"
    if any(p in pt for p in REVIEW_PT) or re.search(r"\breview\b|overview|perspective|demystified|what we don", title, re.I):
        return "review"
    if SERIES_RE.search(text) or re.search(r"\bpatients\b|\bcases\b|children with", title, re.I):
        return "case_series_or_cohort"
    if re.search(r"elastography|mri|imaging|radiolog", title, re.I):
        return "imaging_physiology_study"
    return "clinical_or_mechanistic_study"


def population_of(text):
    ped, adult = bool(PEDIATRIC_RE.search(text)), bool(ADULT_RE.search(text))
    if ped and adult:
        return "mixed"
    if ped:
        return "pediatric"
    if adult:
        return "adult"
    return "unspecified"


def tags(text, table):
    return ";".join(name for name, rx in table if rx.search(text))


def keep(rec, text, axis, pt):
    if axis is None:
        return False
    if any(p in pt for p in DROP_PUBTYPE) or re.match(r"correction:|erratum", rec["title"], re.I):
        return False
    if not rec["title"]:
        return False
    if DROP_TEXT.search(text):
        return False
    # Conference abstract stubs (e.g. "RF25 | PMON113 ...")
    if re.match(r"^[A-Z]{1,4}\d+ \|", rec["title"]):
        return False
    if axis in ("core_lph", "historical_lph_as_nph"):
        return True
    if len(rec["abstract"]) < 150:
        return False
    # Supporting axes must engage with intracranial dynamics, not just NPH diagnostics.
    if NPH_RE.search(text) and not MECH_RE.search(text) and not ADJ_RE.search(text):
        return False
    return True


def score(rec, axis, evidence, text):
    year = year_of(rec) or 1990
    age = max(1, 2026 - year)
    cited = rec["cited"] or 0
    s = 2.0 * math.log1p(cited) + 1.2 * math.log1p(cited / age)
    s += 3.0 if rec["venue"].strip().lower() in TIER1 else 0.0
    s += {"systematic_review": 2.5, "consensus_guideline": 2.5, "case_series": 2.2,
          "case_series_or_cohort": 2.0, "review": 1.2, "case_report": 1.0,
          "experimental": 1.4, "computational_model": 1.2, "imaging_physiology_study": 1.2,
          "clinical_or_mechanistic_study": 1.0, "comment_letter": 0.3}[evidence]
    if CORE_RE.search(text):
        s += 4.0
    if CORE_RE.search(rec["title"]):
        s += 2.0
    if year >= 2020:
        s += 1.5
    if rec["inEPMC"] == "Y":
        s += 0.4
    if rec["pmid"] in MANUAL_AXIS:
        s += 100.0  # pinned after manual review
    return s


def main():
    raw = json.load(open(RAW))
    by_axis = defaultdict(list)
    seen_titles, seen_ids = set(), set()
    dropped = 0

    for rec in raw:
        rec["title"] = re.sub(r"<[^>]+>", "", html.unescape(rec["title"]))
        rec["abstract"] = re.sub(r"<[^>]+>", "", html.unescape(rec["abstract"]))
        text = f"{rec['title']} {rec['abstract']}"
        pt = rec["pubType"].lower()
        axis = classify_axis(rec, text, rec["title"])
        if rec["pmid"] in MANUAL_AXIS:
            axis = MANUAL_AXIS[rec["pmid"]]
        if not keep(rec, text, axis, pt):
            dropped += 1
            continue
        ident = rec["doi"].lower() or rec["pmid"]
        nt = norm_title(rec["title"])
        if (ident and ident in seen_ids) or nt in seen_titles:
            continue
        if ident:
            seen_ids.add(ident)
        seen_titles.add(nt)

        evidence = evidence_of(rec, text, rec["title"], pt)
        item = dict(rec)
        item.update({
            "axis": axis,
            "evidence": evidence,
            "population": population_of(text),
            "settings": tags(text, SETTINGS),
            "treatments": tags(text, TREATMENTS),
            "names_entity": "yes" if CORE_RE.search(text) else "no",
            "url": url_of(rec),
        })
        item["score"] = round(score(rec, axis, evidence, text), 2)
        by_axis[axis].append(item)

    curated = []
    for axis in AXIS_ORDER:
        rows = sorted(by_axis.get(axis, []), key=lambda r: -r["score"])[:CAP[axis]]
        curated.extend(rows)

    for item in curated:
        item.pop("also_domains", None)
    with open(CURATED, "w") as f:
        json.dump(curated, f, indent=1)

    cols = ["axis", "evidence", "population", "settings", "treatments", "names_entity",
            "authors", "title", "venue", "year", "cited", "pmid", "doi", "pmcid", "url",
            "local_fulltext", "status"]
    with open(TSV, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
        w.writerow(cols)
        for item in curated:
            w.writerow([
                item["axis"], item["evidence"], item["population"], item["settings"],
                item["treatments"], item["names_entity"], item["authors"], item["title"],
                item["venue"], item["year"], item["cited"], item["pmid"], item["doi"],
                item["pmcid"], item["url"], "",
                "oa_xml" if item["inEPMC"] == "Y" else "metadata_only",
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
