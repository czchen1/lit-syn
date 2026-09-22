#!/usr/bin/env python3
"""Harvest low-pressure / negative-pressure hydrocephalus (LPH / NePH) literature
from Europe PMC.

Scope: ventriculomegaly with symptoms of raised pressure that persist or worsen at
normal, low or sub-atmospheric intracranial pressure and that only reverse with
CSF drainage below atmospheric pressure (Pang & Altschuler 1994). Also harvested:

  * the mechanistic literature the entity rests on (brain turgor / viscoelasticity,
    transmantle pressure, cortical subarachnoid space, CSF leaks, venous drainage,
    biomechanical models, MR elastography);
  * treatment techniques (sub-zero external ventricular drainage, neck wrapping /
    jugular compression, Trendelenburg, active/negative-pressure shunts, ETV,
    third-ventriculostomy failures, custom low-resistance catheters);
  * precipitating settings (skull-base surgery with CSF leak, lumbar puncture in
    shunted children, subarachnoid haemorrhage, tumours, craniectomy / sinking
    skin flap, shunt over- and under-drainage);
  * the historical 1965-1985 usage of "low-pressure hydrocephalus" as a synonym
    for normal-pressure hydrocephalus (Adams/Hakim), which the curation step tags
    separately so it is not confused with the modern entity;
  * adjacent differentials (slit-ventricle syndrome, overdrainage, intracranial
    hypotension) — one citation-ranked page only, for framing.

Because the entity is rare (a few hundred records in total) every query is swept
over all years with cursor pagination, in citation order; a `recent` sweep
(2015-2026) offsets citation lag for new case series. Output: raw_harvest.json
(consumed by curate.py) and harvest.log.
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "raw_harvest.json")
LOG = os.path.join(HERE, "harvest.log")

ALL = "(SRC:MED OR SRC:PMC OR SRC:PPR)"
RECENT = "FIRST_PDATE:[2015-01-01 TO 2026-12-31] AND (SRC:MED OR SRC:PMC OR SRC:PPR)"


def phrase(term):
    return '"' + term.replace('"', "") + '"'


def concept(term):
    """Title-or-abstract match for one term; 'a & b' requires co-occurrence."""
    if " & " in term:
        return "(" + " AND ".join(concept(p.strip()) for p in term.split(" & ")) + ")"
    q = phrase(term)
    return f"(TITLE:{q} OR ABSTRACT:{q})"


def any_of(terms):
    return "(" + " OR ".join(concept(t) for t in terms) + ")"


def title_any(terms):
    return "(" + " OR ".join(f"TITLE:{phrase(t)}" for t in terms) + ")"


HYDRO = any_of([
    "hydrocephalus", "hydrocephalic", "ventriculomegaly", "ventricular enlargement",
    "ventricular dilatation", "ventricular dilation", "enlarged ventricles",
    "ventricular size", "shunt", "shunted", "ventriculostomy", "ventricular drainage",
    "ventricular drain", "CSF diversion", "cerebrospinal fluid diversion",
])
LOWP = any_of([
    "low pressure", "low-pressure", "negative pressure", "negative-pressure",
    "very low pressure", "subatmospheric", "sub-atmospheric", "subzero", "sub-zero",
    "below atmospheric", "low intracranial pressure", "normal or low intracranial pressure",
    "inappropriately low", "negative intracranial pressure", "low ICP",
])
CORE_TITLE = title_any([
    "low-pressure hydrocephalus", "low pressure hydrocephalus", "low-pressure hydrocephalic",
    "low pressure hydrocephalic", "negative-pressure hydrocephalus",
    "negative pressure hydrocephalus", "very low pressure hydrocephalus",
    "very low-pressure hydrocephalus", "low or negative pressure hydrocephalus",
    "low- or negative-pressure hydrocephalus", "low- and negative-pressure hydrocephalus",
    "low-pressure acute hydrocephalus", "SILPAH", "negative-pressure hydrocephalic",
])
CORE_ANY = any_of([
    "low-pressure hydrocephalus", "low pressure hydrocephalus", "low-pressure hydrocephalic state",
    "low pressure hydrocephalic state", "negative-pressure hydrocephalus",
    "negative pressure hydrocephalus", "very low pressure hydrocephalus",
    "very low-pressure hydrocephalus", "negative pressure hydrocephalic",
    "low-pressure hydrocephalic", "inappropriately low-pressure acute hydrocephalus",
    "inappropriately low pressure acute hydrocephalus", "SILPAH",
    "low or negative pressure hydrocephalus", "low- or negative-pressure hydrocephalus",
    "low- and negative-pressure hydrocephalus", "low and negative pressure hydrocephalus",
])

QUERIES = {
    # ------------------------------------------------------------- the entity itself
    "core_lph": [
        CORE_TITLE,
        CORE_ANY,
        f'{HYDRO} AND {any_of(["subatmospheric", "sub-atmospheric", "subzero", "sub-zero", "below atmospheric pressure", "negative pressure drainage", "negative-pressure drainage", "negative intracranial pressure", "subatmospheric drainage", "drainage below zero"])}',
        f'{HYDRO} AND {any_of(["symptomatic low intracranial pressure", "low intracranial pressure & ventriculomegaly", "low intracranial pressure & ventricular enlargement", "low intracranial pressure & ventricular dilatation", "normal or low intracranial pressure & ventric", "paradoxical ventriculomegaly", "paradoxical ventricular enlargement", "ventriculomegaly despite", "ventricular enlargement despite", "enlarged ventricles despite", "persistent ventriculomegaly & external ventricular drain", "ventriculomegaly & functioning shunt", "ventriculomegaly & patent shunt", "ventricular dilatation & patent shunt", "ventricular enlargement & functioning shunt"])}',
    ],
    # ------------------------------------------------------------- pathophysiology
    "mechanism_biomechanics": [
        f'{HYDRO} AND {any_of(["brain turgor", "viscoelastic", "viscoelasticity", "brain elasticity", "brain stiffness", "brain compliance", "parenchymal compliance", "tissue compliance", "poroelastic", "hysteresis", "non-linear dynamics", "pressure-volume relationship & ventric", "elastance & ventric"])}',
        f'{HYDRO} AND {any_of(["transmantle pressure", "transmantle gradient", "transmantle pressure gradient", "transmantle", "pressure gradient & ventricle & subarachnoid", "cortical subarachnoid space", "subarachnoid space & ventricular enlargement", "Rekate", "ventricular volume regulation"])}',
        f'{HYDRO} AND {any_of(["mathematical model & ventric", "computational model & ventric", "biomechanical model", "finite element & ventric", "Windkessel", "biomechanical instability", "brain-CSF interface", "hydrodynamic model & ventric", "pulsatile & ventricular enlargement", "pulsation & ventricular enlargement"])}',
        f'{HYDRO} AND {any_of(["MR elastography", "magnetic resonance elastography", "elastography & brain", "brain stiffness & shunt", "stiffness & ventric"])}',
        f'{HYDRO} AND {any_of(["venous drainage & ventric", "venous hypertension & ventric", "venous outflow & ventric", "cerebral venous overdrainage", "venous overdrainage", "venous collapse & ventric", "jugular venous & ventric", "sagittal sinus pressure & ventric", "Bateman"])}',
    ],
    # ------------------------------------------------------------- treatment
    "treatment_techniques": [
        f'{HYDRO} AND {any_of(["neck wrapping", "neck wrap", "cervical wrap", "jugular compression & ventric", "Trendelenburg & ventric", "head-down & ventric", "head down position & ventric", "flat positioning & ventric", "negative-pressure shunt", "negative pressure shunt", "active pumping shunt", "pumping shunt", "programmable valve & low pressure", "lowest setting & ventric", "zero pressure & shunt", "custom-made catheter & hydrocephalus", "large bore catheter & ventric", "low-resistance & shunt"])}',
        f'{LOWP} AND {any_of(["external ventricular drainage", "external ventricular drain", "EVD", "ventriculostomy", "lumbar drain", "lumbar drainage", "CSF drainage", "cerebrospinal fluid drainage", "ventriculoperitoneal shunt", "shunt revision", "endoscopic third ventriculostomy", "ETV", "shunt malfunction", "shunt failure"])} AND {HYDRO}',
        f'{HYDRO} AND {any_of(["titrated drainage & ventric", "titration & external ventricular", "gradual weaning & drain & ventric", "weaning & external ventricular drainage", "drainage level & ventric", "drain height & ventric", "intracranial pressure monitoring & low pressure & ventric", "ICP monitoring & low-pressure"])}',
    ],
    # ------------------------------------------------------------- settings / etiology
    "etiology_settings": [
        f'{HYDRO} AND {any_of(["cerebrospinal fluid leak", "CSF leak", "CSF fistula", "cerebrospinal fluid fistula", "dural defect & ventric", "pseudomeningocele & ventric", "CSF hypovolemia & ventric", "cerebrospinal fluid hypovolemia", "cerebrospinal fluid depletion", "skull base surgery & ventric", "cranial base & ventric", "transsphenoidal & ventric", "endoscopic endonasal & ventric"])} AND {LOWP}',
        f'{HYDRO} AND {any_of(["lumbar puncture & shunt & low pressure", "lumbar puncture & shunted", "lumbar puncture & ventriculomegaly", "lumbar puncture-induced", "lumbar puncture & negative pressure", "lumbar drain & ventriculomegaly", "lumbar drainage & ventriculomegaly", "overdrainage & ventriculomegaly", "over-drainage & ventriculomegaly"])}',
        f'{HYDRO} AND {any_of(["decompressive craniectomy", "craniectomy", "cranioplasty", "sinking skin flap", "syndrome of the trephined", "paradoxical herniation", "hemispherectomy", "hemicraniectomy"])} AND {LOWP}',
        f'{HYDRO} AND {any_of(["subarachnoid hemorrhage", "subarachnoid haemorrhage", "aneurysm", "intraventricular hemorrhage", "posterior fossa tumor", "posterior fossa tumour", "third ventricle", "aqueductal stenosis", "Chiari", "meningitis", "hemangioblastoma", "pineal", "pituitary", "craniopharyngioma", "meningioma", "arachnoid cyst", "trapped fourth ventricle", "isolated fourth ventricle", "spinal surgery", "tethered cord"])} AND {CORE_ANY}',
    ],
    # ------------------------------------------------------------- adjacent entities
    "adjacent_differentials": [
        f'{title_any(["slit ventricle syndrome", "slit-ventricle syndrome", "slit ventricle", "shunt overdrainage", "overdrainage", "over-drainage", "siphoning", "antisiphon", "anti-siphon"])} AND {HYDRO}',
        f'{title_any(["intracranial hypotension", "CSF hypotension", "cerebrospinal fluid hypotension", "low CSF pressure", "low cerebrospinal fluid pressure"])} AND {HYDRO}',
        f'{title_any(["hydrocephalus"])} AND {title_any(["classification", "definition", "pathophysiology", "pathogenesis", "biomechanics", "theory", "hydrodynamics", "should know", "wrong question", "revisited", "review"])} AND {any_of(["intracranial pressure", "transmantle", "compliance", "subarachnoid", "venous"])}',
    ],
    # ------------------------------------------------------------- historical NPH usage
    "historical_lph_as_nph": [
        f'{title_any(["low-pressure hydrocephalus", "low pressure hydrocephalus", "low-pressure hydrocephalic", "low pressure hydrocephalic"])} AND FIRST_PDATE:[1900-01-01 TO 1993-12-31]',
        f'{any_of(["low-pressure hydrocephalus", "low pressure hydrocephalus"])} AND {any_of(["normal pressure hydrocephalus", "normal-pressure hydrocephalus", "dementia", "Hakim", "Adams", "occult hydrocephalus", "communicating hydrocephalus", "gait disturbance", "incontinence"])} AND FIRST_PDATE:[1900-01-01 TO 1999-12-31]',
    ],
}

PAGE = 100
SWEEPS = [
    ("all_years", ALL, 4),
    ("recent", RECENT, 2),
]
# Framing-only domains get one page per sweep so they do not swamp the corpus.
PAGE_CAP = {"adjacent_differentials": 1}


def request_json(url):
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "lit-syn/1.0"})
            with urllib.request.urlopen(req, timeout=180) as resp:
                return json.load(resp)
        except Exception as exc:
            sys.stderr.write(f"  retry {attempt}: {exc}\n")
            time.sleep(4 + 4 * attempt)
    return None


def epmc_top_cited(query, pages):
    out, hits, cursor = [], 0, "*"
    for _ in range(pages):
        params = urllib.parse.urlencode({
            "query": query, "format": "json", "pageSize": PAGE,
            "resultType": "core", "sort": "CITED desc", "cursorMark": cursor,
        })
        data = request_json(f"{EPMC}?{params}")
        # Europe PMC intermittently answers a valid query with hitCount 0; re-ask.
        for _retry in range(3):
            if cursor != "*" or data is None or data.get("hitCount", 0) > 0:
                break
            time.sleep(3)
            data = request_json(f"{EPMC}?{params}")
        if data is None:
            break
        hits = hits or data.get("hitCount", 0)
        results = data.get("resultList", {}).get("result", [])
        out.extend(results)
        nxt = data.get("nextCursorMark")
        if len(results) < PAGE or not nxt or nxt == cursor:
            break
        cursor = nxt
        time.sleep(0.34)
    return out, hits


def clean(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text)).strip()


def venue_of(rec):
    ji = rec.get("journalInfo", {}) or {}
    return (ji.get("journal", {}).get("title", "")
            or ji.get("journal", {}).get("medlineAbbreviation", "")
            or rec.get("journalTitle", "")
            or (rec.get("bookOrReportDetails", {}) or {}).get("publisher", ""))


def ingest(seen, results, domain, sweep):
    new = 0
    for rec in results:
        key = rec.get("pmid") or rec.get("doi") or rec.get("id")
        if not key:
            continue
        if key in seen:
            seen[key]["also_domains"].add(domain)
            continue
        new += 1
        seen[key] = {
            "domain": domain,
            "also_domains": set(),
            "sweep": sweep,
            "pmid": rec.get("pmid", ""),
            "pmcid": rec.get("pmcid", ""),
            "doi": rec.get("doi", ""),
            "title": clean(rec.get("title", "")).rstrip("."),
            "abstract": clean(rec.get("abstractText", "")),
            "authors": rec.get("authorString", ""),
            "venue": venue_of(rec),
            "year": rec.get("pubYear", ""),
            "date": rec.get("firstPublicationDate", ""),
            "isOA": rec.get("isOpenAccess", "N"),
            "inEPMC": rec.get("inEPMC", "N"),
            "cited": rec.get("citedByCount", 0),
            "pubType": (rec.get("pubTypeList", {}) or {}).get("pubType", []),
            "src": rec.get("source", ""),
        }
    return new


def main():
    seen = {}
    log = open(LOG, "a")
    for domain, queries in QUERIES.items():
        for i, q in enumerate(queries):
            for sweep, scope, pages in SWEEPS:
                pages = min(pages, PAGE_CAP.get(domain, pages))
                results, hits = epmc_top_cited(f"({q}) AND {scope}", pages)
                new = ingest(seen, results, domain, sweep)
                msg = (f"{sweep:10s} {domain}[{i}]: hits={hits} "
                       f"fetched={len(results)} new={new} total={len(seen)}\n")
                sys.stderr.write(msg)
                log.write(msg)
                log.flush()
                time.sleep(0.34)

    out = []
    for v in seen.values():
        v["also_domains"] = "|".join(sorted(v["also_domains"]))
        v["pubType"] = "|".join(v["pubType"]) if isinstance(v["pubType"], list) else str(v["pubType"])
        out.append(v)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=0)
    print(f"total unique records: {len(out)}")
    log.write(f"total unique records: {len(out)}\n")
    log.close()


if __name__ == "__main__":
    main()
