#!/usr/bin/env python3
"""Download open-access full-text XML for indexed rows with a PMCID.

Europe PMC serves most records, but returns an empty body for some open-access
articles (e.g. author-manuscript deposits), so NCBI E-utilities is used as a
fallback. Writes fulltext/<firstauthor>_<year>_pmid<pmid>.xml, records the path in
the `fulltext_xml` column and flips `status` to `fulltext_xml` on success.
"""
import csv
import os
import re
import time
import urllib.request

BASE = "/home/ubuntu/repos/lit-syn/papers/anktiva-formulation-intravesical-vs-iv"
IDX = os.path.join(BASE, "index.tsv")
FT = os.path.join(BASE, "fulltext")
os.makedirs(FT, exist_ok=True)

COLS = ["category", "authors", "title", "venue", "year", "pmid", "doi", "pmcid",
        "url", "fulltext_xml", "topics", "status"]
UA = {"User-Agent": "lit-syn/1.0 (literature synthesis; contact via repository)"}
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pid}/fullTextXML"
EUTILS = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
          "?db=pmc&id={num}&rettype=xml&retmode=xml")


def first_author(authors):
    if not authors:
        return "anon"
    a = authors.split(",")[0].split(" ")[0]
    return re.sub(r"[^a-z0-9]", "", a.lower()) or "anon"


def looks_like_article(data):
    if not data or len(data) < 2000:
        return False
    head = data[:5000].lower()
    return b"<article" in head or b"<pmc-articleset" in head


def download(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as resp:
            data = resp.read()
        return data if looks_like_article(data) else None
    except Exception:
        return None


def main():
    rows = list(csv.DictReader(open(IDX), delimiter="\t"))
    ok = fail = 0
    for r in rows:
        pmcid = (r.get("pmcid") or "").strip()
        if not pmcid:
            continue
        pid = pmcid if pmcid.upper().startswith("PMC") else "PMC" + pmcid
        fname = f"{first_author(r['authors'])}_{r['year']}_pmid{r['pmid'] or pid}.xml"
        dest = os.path.join(FT, fname)
        if os.path.exists(dest) and os.path.getsize(dest) > 2000:
            r["fulltext_xml"] = f"fulltext/{fname}"
            r["status"] = "fulltext_xml"
            ok += 1
            continue

        data = download(EPMC.format(pid=pid))
        if data is None:
            time.sleep(0.4)
            data = download(EUTILS.format(num=pid[3:]))
        if data is None:
            fail += 1
        else:
            with open(dest, "wb") as f:
                f.write(data)
            r["fulltext_xml"] = f"fulltext/{fname}"
            r["status"] = "fulltext_xml"
            ok += 1
        time.sleep(0.4)

    with open(IDX, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, delimiter="\t")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"fulltext downloaded: {ok}, unavailable: {fail}")


if __name__ == "__main__":
    main()
