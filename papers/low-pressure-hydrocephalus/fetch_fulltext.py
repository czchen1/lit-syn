#!/usr/bin/env python3
"""Download open-access full-text XML from Europe PMC for curated rows.

Core low-/negative-pressure hydrocephalus rows are fetched first (systematic
reviews, then series, then case reports, which carry most of the ICP-titration
detail), then supporting axes. Local paths are written back into index.tsv and
curated.json.
"""
import csv
import json
import os
import re
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(HERE, "index.tsv")
CURATED = os.path.join(HERE, "curated.json")
FT = os.path.join(HERE, "fulltext")
os.makedirs(FT, exist_ok=True)

AXIS_PRIORITY = {"core_lph": 0, "treatment_techniques": 1, "etiology_settings": 1,
                 "mechanism_biomechanics": 2, "adjacent_differentials": 3,
                 "historical_lph_as_nph": 4}
EVIDENCE_PRIORITY = {"systematic_review": 0, "consensus_guideline": 0, "case_series": 1,
                     "case_series_or_cohort": 1, "review": 2, "case_report": 2,
                     "clinical_or_mechanistic_study": 3, "imaging_physiology_study": 3,
                     "experimental": 4, "computational_model": 4, "comment_letter": 5}
MAX_FETCH = 160


def first_author(authors):
    if not authors:
        return "anon"
    a = authors.split(",")[0].split(" ")[0]
    return re.sub(r"[^a-z0-9]", "", a.lower()) or "anon"


def fetch(pmcid):
    pid = pmcid if pmcid.upper().startswith("PMC") else "PMC" + pmcid
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pid}/fullTextXML"
    req = urllib.request.Request(url, headers={"User-Agent": "lit-syn/1.0"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return resp.read()


def main():
    rows = list(csv.DictReader(open(IDX), delimiter="\t"))
    order = sorted(range(len(rows)),
                   key=lambda i: (AXIS_PRIORITY.get(rows[i]["axis"], 9),
                                  EVIDENCE_PRIORITY.get(rows[i]["evidence"], 9),
                                  -int(rows[i]["cited"] or 0)))
    ok = fail = 0
    for i in order:
        r = rows[i]
        if ok >= MAX_FETCH:
            break
        pmcid = r["pmcid"].strip()
        if not pmcid:
            r["status"] = "metadata_only"
            continue
        r["status"] = "oa_unavailable"
        fname = f"{first_author(r['authors'])}_{r['year']}_pmid{r['pmid'] or pmcid}.xml"
        dest = os.path.join(FT, fname)
        if os.path.exists(dest) and os.path.getsize(dest) > 2000:
            r["local_fulltext"] = f"fulltext/{fname}"
            r["status"] = "oa_xml"
            ok += 1
            continue
        try:
            data = fetch(pmcid)
        except Exception:
            data = b""
        if data and len(data) > 2000 and b"<article" in data[:5000].lower():
            with open(dest, "wb") as f:
                f.write(data)
            r["local_fulltext"] = f"fulltext/{fname}"
            r["status"] = "oa_xml"
            ok += 1
        else:
            fail += 1
        time.sleep(0.34)

    with open(IDX, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    paths = {(r["pmid"] or r["pmcid"]): (r["local_fulltext"], r["status"]) for r in rows}
    curated = json.load(open(CURATED))
    for item in curated:
        item["local_fulltext"], item["status"] = paths.get(
            item["pmid"] or item["pmcid"], ("", "metadata_only"))
    with open(CURATED, "w") as f:
        json.dump(curated, f, indent=1)

    print(f"fulltext available: {ok}, unavailable: {fail}")


if __name__ == "__main__":
    main()
