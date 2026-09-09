#!/usr/bin/env python3
"""Download open-access full-text XML from Europe PMC for the highlight subset.

The six-month corpus is far too large to mirror in full, so full text is fetched only
for rows that have a PMCID and are either (a) prospective clinical trial reports
(clinical_phase1/2/3) or (b) tier-1/tier-2 preclinical or evidence-synthesis records,
up to MAX_FILES. Writes fulltext/<firstauthor>_<year>_pmid<pmid>.xml, records the path in
`fulltext_xml`, and flips `status` to `fulltext_xml` on success.
"""
import csv
import os
import re
import sys
import time
import urllib.request

BASE = "/home/ubuntu/repos/lit-syn/papers/recent-cancer-therapies-2026"
IDX = os.path.join(BASE, "index.tsv")
FT = os.path.join(BASE, "fulltext")
os.makedirs(FT, exist_ok=True)

MAX_FILES = int(sys.argv[1]) if len(sys.argv) > 1 else 700
TRIAL_EVIDENCE = {"clinical_phase3", "clinical_phase2", "clinical_phase1"}


def first_author(authors):
    if not authors:
        return "anon"
    a = authors.split(",")[0].split(" ")[0]
    return re.sub(r"[^a-z0-9]", "", a.lower()) or "anon"


def wanted(r):
    if not (r.get("pmcid") or "").strip():
        return False
    if r["evidence"] in TRIAL_EVIDENCE:
        return True
    return r["tier"] in ("1", "2")


def main():
    with open(IDX) as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        cols = reader.fieldnames
        rows = list(reader)
    todo = [r for r in rows if wanted(r)]
    # trials first, then by tier, so the cap falls on the least important records
    todo.sort(key=lambda r: (r["evidence"] not in TRIAL_EVIDENCE, int(r["tier"]), r["date"]))
    todo = todo[:MAX_FILES]
    ok = fail = 0
    for r in todo:
        pmcid = r["pmcid"].strip()
        pid = pmcid if pmcid.upper().startswith("PMC") else "PMC" + pmcid
        url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pid}/fullTextXML"
        fname = f"{first_author(r['authors'])}_{r['year']}_pmid{r['pmid'] or pmcid}.xml"
        dest = os.path.join(FT, fname)
        if os.path.exists(dest) and os.path.getsize(dest) > 2000:
            r["fulltext_xml"] = f"fulltext/{fname}"
            r["status"] = "fulltext_xml"
            ok += 1
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "lit-syn/1.0"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = resp.read()
            if data and len(data) > 2000 and b"<article" in data[:5000].lower():
                with open(dest, "wb") as f:
                    f.write(data)
                r["fulltext_xml"] = f"fulltext/{fname}"
                r["status"] = "fulltext_xml"
                ok += 1
            else:
                fail += 1
        except Exception:
            fail += 1
        time.sleep(0.34)

    with open(IDX, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"fulltext downloaded: {ok}, unavailable: {fail}, eligible: {len(todo)}")


if __name__ == "__main__":
    main()
