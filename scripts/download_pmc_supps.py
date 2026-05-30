"""Fetch PMC supplementary files using the same PoW handshake as scripts/download_pmc_pdf.py."""
import argparse
import hashlib
import http.cookiejar
import re
import sys
import urllib.request
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
    return _opener(jar).open(req, timeout=120)


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


# (output_filename, pmcid_numeric, bin_filename)
SUPP_FILES = [
    ("long_2015_supp1.pdf", "4458184", "NIHMS672402-supplement-1.pdf"),
    ("long_2015_supp2.xlsx", "4458184", "NIHMS672402-supplement-2.xlsx"),
    ("mount_2018_supp1.pdf", "6214371", "NIHMS939207-supplement-1.pdf"),
    ("mount_2018_supp2.pdf", "6214371", "NIHMS939207-supplement-2.pdf"),
    ("lynn_2019_supp_fig.pdf", "6944329", "NIHMS1541323-supplement-sup_fig.pdf"),
    ("lynn_2019_supp_tab1.xlsx", "6944329", "NIHMS1541323-supplement-sup_tab1.xlsx"),
    ("lynn_2019_supp_tab2.xlsx", "6944329", "NIHMS1541323-supplement-1541323_Sup_Tab2.xlsx"),
    ("majzner_2022_supp1.pdf", "8967714", "41586_2022_4489_MOESM1_ESM.pdf"),
    ("majzner_2022_supp2.pdf", "8967714", "41586_2022_4489_MOESM2_ESM.pdf"),
    ("majzner_2022_supp3.pdf", "8967714", "41586_2022_4489_MOESM3_ESM.pdf"),
    ("majzner_2022_supp_protocol.docx", "8967714", "41586_2022_4489_MOESM4_ESM.docx"),
    ("majzner_2022_supp_tab1.xlsx", "8967714", "41586_2022_4489_MOESM7_ESM.xlsx"),
    ("majzner_2022_supp_tab2.xlsx", "8967714", "41586_2022_4489_MOESM8_ESM.xlsx"),
    ("majzner_2022_supp_tab3.xlsx", "8967714", "41586_2022_4489_MOESM9_ESM.xlsx"),
    ("majzner_2022_supp_tab4.xlsx", "8967714", "41586_2022_4489_MOESM10_ESM.xlsx"),
    ("majzner_2022_supp_tab5.xlsx", "8967714", "41586_2022_4489_MOESM11_ESM.xlsx"),
    ("majzner_2022_supp_tab6.xlsx", "8967714", "41586_2022_4489_MOESM12_ESM.xlsx"),
    ("majzner_2022_supp_tab7.xlsx", "8967714", "41586_2022_4489_MOESM13_ESM.xlsx"),
    ("majzner_2022_supp_tab8.xlsx", "8967714", "41586_2022_4489_MOESM14_ESM.xlsx"),
    ("majzner_2022_supp_tab9.xlsx", "8967714", "41586_2022_4489_MOESM15_ESM.xlsx"),
    ("heczey_2017_supp1.pdf", "5589058", "mmc1.pdf"),
    ("heczey_2017_supp2.pdf", "5589058", "mmc2.pdf"),
]


def fetch_supp(pmcid_num: str, bin_name: str, outpath: Path, jar) -> int:
    pmcid = f"PMC{pmcid_num}"
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/instance/{pmcid_num}/bin/{bin_name}"

    for attempt in range(3):
        body = _fetch(url, jar).read()
        if body[:4] in (b"%PDF", b"PK\x03\x04", b"\xd0\xcf\x11\xe0"):
            outpath.parent.mkdir(parents=True, exist_ok=True)
            outpath.write_bytes(body)
            return len(body)
        text = body.decode("utf-8", "replace")
        chal = re.search(r'POW_CHALLENGE\s*=\s*"([^"]+)"', text)
        diff = re.search(r'POW_DIFFICULTY\s*=\s*"?(\d+)"?', text)
        name = re.search(r'POW_COOKIE_NAME\s*=\s*"([^"]+)"', text)
        if chal:
            nonce = _solve(chal.group(1), int(diff.group(1)) if diff else 4)
            _set_pow_cookie(jar, name.group(1) if name else "cloudpmc-viewer-pow", chal.group(1), nonce)
            continue
        # Not a PoW interstitial and not a binary; likely rate-limited
        if attempt < 2:
            import time
            time.sleep(30)
            continue
        raise RuntimeError(f"{pmcid}/{bin_name}: no PoW challenge and not a binary (got {body[:16]!r})")
    raise RuntimeError(f"{pmcid}/{bin_name}: exhausted retries")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("outdir", type=Path)
    ap.add_argument("--only", help="comma-separated list of output filenames to fetch")
    ap.add_argument("--delay", type=float, default=5.0, help="seconds between requests")
    args = ap.parse_args()
    import time
    only = set(args.only.split(",")) if args.only else None
    jar = http.cookiejar.CookieJar()
    fail = []
    for out_name, pmcid_num, bin_name in SUPP_FILES:
        if only and out_name not in only:
            continue
        outpath = args.outdir / out_name
        if outpath.exists() and outpath.stat().st_size > 5000:
            print(f"SKIP {out_name} (exists, {outpath.stat().st_size} bytes)", flush=True)
            continue
        try:
            n = fetch_supp(pmcid_num, bin_name, outpath, jar)
            print(f"OK   {out_name} ({n} bytes)", flush=True)
        except Exception as e:
            print(f"FAIL {out_name}: {e}", flush=True)
            fail.append(out_name)
        time.sleep(args.delay)
    if fail:
        print(f"\n{len(fail)} failures:")
        for f in fail:
            print(f"  - {f}")
        sys.exit(1)


if __name__ == "__main__":
    main()
