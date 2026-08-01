# Naeimi Kararoudi lab — NK and γδ T cell expansion / culture conditions

Literature + IP synthesis on Meisam Naeimi Kararoudi's (DVM, PhD; formerly Nationwide Children's
CRISPR/Gene Editing Core, now Cincinnati Children's; CARTx Therapeutics) work on **NK cells and
γδ T cells**, focused on **expansion and culture conditions** as they appear in publications,
supplementary/STAR methods, and patents.

The motivating question: he verbally stated that for γδ T cells you want a **short TCR expansion
period** (too long → exhausted cells) and should instead use **feeder cells that provide JAK/STAT
stimulation**. This collection checks that statement against his own publications and patents and
against the wider γδ T cell manufacturing literature.

## Directory structure

- `index.tsv` — curated papers, patents, and tech-transfer listings with the specific culture
  parameters extracted into the `notes` column.
- `notes/expansion_protocol_walkthrough.md` — step-by-step walkthrough of both expansion protocols with verbatim quotes from the patent, the Portillo Methods, and the NK STAR Methods.
- `notes/protocol_B_clean.md` — **start here for Protocol B.** Clean single-source, patent-only
  step list with every line tagged worked-example / description / claim, plus a change log.
- `notes/protocol_B_patent_verified.md` — line-by-line verification of the patent protocol against
  the full text: what is exemplified vs claimed vs merely described, plus 11 internal
  inconsistencies / drafting defects found in the filing. **Supersedes the Protocol B sections of
  the walkthrough where they disagree.**
- `notes/naeimi_gdT_nk_expansion_synthesis.md` — the synthesis: decoding of the verbal statement,
  the mbIL-21/STAT3 NK platform it is built on, the two coexisting γδ process designs, a
  head-to-head against other γδ manufacturing platforms, and open questions.
- `pdfs/` — open-access PDFs (see download note).

## Short answer

His statement maps almost literally onto patent **WO2025123022A1**: γδ T cells are primed on
plate-bound anti-CD3 for a deliberately bounded window (claimed "at least 2 days"; spec allows
6 h – 7 d), then handed off to **K562.mbIL21.4-1BBL** feeders (clinical-grade **CStX-002**) at ≥2:1 with
100 IU/mL IL-2 every ~48 h. (The patent never actually recites that these feeders are *irradiated* —
see the verification note; Portillo and the NK protocol both do.) "JAK/STAT stimulation" = membrane-bound
IL-21 → JAK1/JAK3 → **STAT3** (plus 4-1BBL → NF-κB), the same engine the Lee lab built for NK cells
(Denman 2012: 47,967-fold vs 825-fold for mbIL-15, with *lengthened* rather than shortened
telomeres). The feeder phase is also claimed independently as the state that makes γδ T cells
**susceptible to CRISPR/AAV6 gene editing**.

Caveat worth carrying: his only peer-reviewed γδ paper (Portillo et al., *OncoImmunology* 2025)
uses **no TCR agonist at all** and runs **≥5 weeks**, yields Vδ1-dominant products, and its own
discussion says shortening the expansion may be advantageous because long expansion could cause
γδ exhaustion. So "short" refers to the **TCR-agonist phase**; total culture duration is still an
open variable in his own work. Full reasoning and evidence grading in the synthesis note.

## Download note

Patent full text and open-access article full text were read via Google Patents and Europe PMC.
Publisher PDF endpoints (Taylor & Francis, AACR, PMC) returned anti-bot/interstitial HTML rather
than valid PDFs in this environment, so rows are marked `no_open_pdf_added` with the URL rather
than committing invalid files.
