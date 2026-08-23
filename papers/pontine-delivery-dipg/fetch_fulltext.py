#!/usr/bin/env python3
"""Download open-access full-text XML from Europe PMC for indexed rows with a PMCID.

Writes fulltext/<firstauthor>_<year>_pmid<pmid>.xml and records the path in the
`fulltext_xml` column, flipping `status` to `fulltext_xml` on success.
"""
import csv
import os
import re
import time
import urllib.request

BASE = "/home/ubuntu/repos/lit-syn/papers/pontine-delivery-dipg"
IDX = os.path.join(BASE, "index.tsv")
FT = os.path.join(BASE, "fulltext")
os.makedirs(FT, exist_ok=True)

COLS = ["category", "authors", "title", "venue", "year", "pmid", "doi", "pmcid",
        "url", "local_pdf", "fulltext_xml", "topics", "status"]


def first_author(authors):
    if not authors:
        return "anon"
    a = authors.split(",")[0].split(" ")[0]
    return re.sub(r"[^a-z0-9]", "", a.lower()) or "anon"


def main():
    rows = list(csv.DictReader(open(IDX), delimiter="\t"))
    ok = fail = 0
    for r in rows:
        pmcid = (r.get("pmcid") or "").strip()
        if not pmcid:
            continue
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
        w = csv.DictWriter(f, fieldnames=COLS, delimiter="\t")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"fulltext downloaded: {ok}, unavailable: {fail}")


if __name__ == "__main__":
    main()
