"""
Download PDFs from PubMed Central by solving the cloudpmc-viewer-pow JS challenge.

PMC fronts every PDF download with a small SHA-256 hashcash-style proof-of-work:
the browser must find a nonce N such that
    sha256(challenge + str(N)).hexdigest().startswith("0" * difficulty)
and present a cookie `cloudpmc-viewer-pow = <challenge>,<nonce>` on the
follow-up request. This script implements that handshake in pure Python so we
can download open-access PMC PDFs from CI / scripted environments.
"""
import argparse, hashlib, http.cookiejar, re, sys, urllib.error, urllib.request
from pathlib import Path

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
COOKIE_DOMAIN = "pmc.ncbi.nlm.nih.gov"


def _opener(jar):
    return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))


def _fetch(url, jar):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    return _opener(jar).open(req, timeout=60)


def _solve(challenge: str, difficulty: int) -> int:
    prefix = "0" * difficulty
    n = 0
    while True:
        if hashlib.sha256(f"{challenge}{n}".encode()).hexdigest().startswith(prefix):
            return n
        n += 1


def _set_pow_cookie(jar, name, challenge, nonce):
    jar.set_cookie(http.cookiejar.Cookie(
        version=0, name=name, value=f"{challenge},{nonce}",
        port=None, port_specified=False,
        domain=COOKIE_DOMAIN, domain_specified=True, domain_initial_dot=False,
        path="/", path_specified=True, secure=True, expires=None,
        discard=True, comment=None, comment_url=None, rest={},
    ))


def _find_pdf_path(pmcid: str, jar) -> str:
    """Scrape the article landing page for the relative pdf/<name>.pdf link."""
    html = _fetch(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/", jar).read().decode("utf-8", "replace")
    m = re.search(r'href="(pdf/[^"]+\.pdf)"', html)
    if not m:
        raise RuntimeError(f"No PDF link found on landing page for {pmcid}")
    return m.group(1)


def download_pmc_pdf(pmcid: str, outpath: Path) -> int:
    jar = http.cookiejar.CookieJar()
    pdf_rel = _find_pdf_path(pmcid, jar)
    pdf_url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/{pdf_rel}"

    body = _fetch(pdf_url, jar).read().decode("utf-8", "replace")
    chal = re.search(r'POW_CHALLENGE\s*=\s*"([^"]+)"', body)
    diff = re.search(r'POW_DIFFICULTY\s*=\s*"?(\d+)"?', body)
    name = re.search(r'POW_COOKIE_NAME\s*=\s*"([^"]+)"', body)
    if not chal:
        # Already a PDF (unlikely but possible if cookie persisted)
        outpath.write_bytes(body.encode("utf-8", "replace"))
        return outpath.stat().st_size

    nonce = _solve(chal.group(1), int(diff.group(1)) if diff else 4)
    _set_pow_cookie(jar, name.group(1) if name else "cloudpmc-viewer-pow", chal.group(1), nonce)

    data = _fetch(pdf_url, jar).read()
    if not data.startswith(b"%PDF"):
        raise RuntimeError(f"{pmcid}: response did not start with %PDF after PoW (got {data[:16]!r})")
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_bytes(data)
    return len(data)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pmcid", help="PMC accession, e.g. PMC6214371")
    ap.add_argument("outpath", type=Path, help="Output PDF path")
    args = ap.parse_args()
    n = download_pmc_pdf(args.pmcid, args.outpath)
    print(f"{args.pmcid}: wrote {args.outpath} ({n} bytes)")


if __name__ == "__main__":
    main()
