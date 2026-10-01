#!/usr/bin/env python3
"""Mirror open-access full-text XML from Europe PMC for index.tsv rows with a PMCID."""
import csv, os, re, time, urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(BASE, "index.tsv")
FT = os.path.join(BASE, "fulltext")
COLS = ["category", "authors", "title", "venue", "year", "pmid", "doi", "pmcid", "url",
        "local_fulltext", "supp_pdf", "topics", "status"]
os.makedirs(FT, exist_ok=True)


def first_author(authors):
    if not authors:
        return "anon"
    a = authors.split(",")[0].split(" ")[0]
    return re.sub(r"[^a-z0-9]", "", a.lower()) or "anon"


def main():
    rows = list(csv.DictReader(open(IDX), delimiter="\t"))
    ok = fail = 0
    for r in rows:
        pmcid = r["pmcid"].strip()
        if not pmcid or r["status"] != "OA_available":
            continue
        pid = pmcid if pmcid.upper().startswith("PMC") else "PMC" + pmcid
        fname = f"{first_author(r['authors'])}_{r['year']}_pmid{r['pmid'] or pmcid}.xml"
        dest = os.path.join(FT, fname)
        if os.path.exists(dest) and os.path.getsize(dest) > 2000:
            r["local_fulltext"] = f"fulltext/{fname}"
            ok += 1
            continue
        url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pid}/fullTextXML"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "lit-syn/1.0"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = resp.read()
            if data and len(data) > 2000 and b"<article" in data[:5000].lower():
                with open(dest, "wb") as f:
                    f.write(data)
                r["local_fulltext"] = f"fulltext/{fname}"
                ok += 1
            else:
                fail += 1
        except Exception:
            fail += 1
        time.sleep(0.34)

    with open(IDX, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"full text mirrored: {ok}, unavailable: {fail}")


if __name__ == "__main__":
    main()
