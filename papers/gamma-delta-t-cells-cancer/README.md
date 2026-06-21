# γδ T cells in cancer — literature synthesis

Curated collection of the published literature on **gamma‑delta (γδ) T cells in cancer**, with an emphasis on the **translational / immunotherapeutic** angle: how γδ T cells recognize and kill tumors, when they instead promote tumor growth, and how they are being expanded, engineered, and dosed as a cancer therapy.

## Scope

This collection captures studies in which human (or, for mechanism, murine) γδ T cells are studied **in the context of cancer** — antitumor (and protumor) biology, antigen recognition, prognostic associations, ex‑vivo expansion, genetic engineering (CAR‑γδ, TCR‑transfer, bispecific engagers), and clinical trials. It is built around the therapeutic question *"can γδ T cells be turned into a cancer medicine, and how?"* rather than around γδ biology in infection/autoimmunity (those appear only where directly relevant).

## Directory structure

- `index.tsv` — curated metadata for all **1,125 papers** identified, with category, topic/cancer tags, IDs (PMID/DOI/PMCID), download status, and local paths.
- `pdfs/` — open‑access PDFs of main texts (**552 papers**, retrieved from the Europe PMC / PMC open‑access subset).
- `supplements/` — extracted supplementary documents (PDF/DOCX/XLSX/CSV) for OA papers that have them, pruned of large binary/image/video/raw‑data files (≤12 MB per file, ≤25 MB per paper) to keep the repository tractable.
- `notes/` — thematic synthesis notes (see index below).
- `REPORT.md` — a single end‑to‑end synthesis consolidating and expanding the notes, organized as **Biology → Recognition → Effector function → Dual role → Manufacturing → Engineering → Clinical → Discussion**.

## Notes index

- `notes/00_overview.md` — the landscape: eras and inflection points, corpus statistics, conventions, glossary.
- `notes/01_biology_and_subsets.md` — γδ T cell ontogeny, the Vδ1 / Vδ2 / Vδ3 subset framework, tissue distribution, and the "adaptive‑like" vs "innate‑like" axis.
- `notes/02_antigen_recognition.md` — phosphoantigen sensing through BTN3A1/BTN2A1, NKG2D and other NK‑receptor ligands, TCR ligands, and stress‑surveillance.
- `notes/03_antitumor_effector_mechanisms.md` — perforin/granzyme, death‑receptor (TRAIL/FasL) killing, CD16/ADCC, cytokine output, and professional antigen‑presentation.
- `notes/04_dual_role_and_protumor.md` — the "double‑edged sword": IL‑17⁺ γδ T17 cells, MDSC/neutrophil recruitment, immunosuppressive γδ subsets, and the prognosis literature.
- `notes/05_expansion_and_adoptive_platforms.md` — aminobisphosphonate/IL‑2 expansion, artificial‑APC and feeder systems, Vδ1 (DOT‑cell) expansion, and allogeneic off‑the‑shelf manufacturing.
- `notes/06_engineering_car_tcr_engagers.md` — CAR‑γδ, defined‑TCR transfer (TEGs), antibody‑TCR fusions, bispecific γδ‑engagers, and armoring.
- `notes/07_clinical_trials.md` — the clinical record: autologous Vγ9Vδ2 trials, allogeneic products (ADI‑001, DOT cells, GDX/GDT), CAR‑γδ, agonist antibodies, and outcomes.
- `notes/08_combinations_and_resistance.md` — combination with checkpoint blockade, ADCC mAbs, bisphosphonates, radiation, and oncolytic virus; mechanisms of tumor resistance/escape.
- `notes/09_cancer_specific_findings.md` — tumor‑type‑specific findings (hematologic vs solid tumors).
- `notes/10_per_paper_extractions.md` — capsule summaries of landmark and representative primary papers.

## Identification strategy

Two complementary PubMed E‑utils queries were combined and de‑duplicated:

1. *therapy core* — `("gamma delta T cell*" OR "gammadelta T cell*" OR "γδ T cell*" OR "Vδ2" OR "Vgamma9" OR "Vγ9") AND (immunotherap* OR adoptive OR "cell therapy" OR CAR OR "chimeric antigen receptor") AND (cancer OR tumor* OR tumour* OR malignan* OR neoplas*)` — all fields searched as `[tiab]`.
2. *CAR/engineering* — `("gamma delta" OR gammadelta OR γδ OR Vδ1 OR Vδ2 OR Vγ9Vδ2) AND ("CAR-T" OR "CAR T" OR "chimeric antigen receptor")`.

1,126 unique PMIDs were retrieved (records span 1990s–2026). Metadata was pulled via NCBI E‑utils `efetch`; PMC IDs were taken from the PubMed records; PDFs and supplementary files were retrieved from the **Europe PMC open‑access subset** (`europepmc.org/articles/PMC…?pdf=render` and the `supplementaryFiles` REST endpoint). Records without a PMCID (`no_pmcid`) or whose PMC entry is not in the OA subset (`not_available_oa`) are catalogued in `index.tsv` but have no local PDF.

## Caveats

- The corpus is defined by a title/abstract keyword search, so it includes a small tail of tangential papers (e.g. broad immune‑landscape or panel‑design papers that merely mention γδ cells). Category tags in `index.tsv` are heuristic (assigned by keyword/pub‑type matching) and are meant for navigation, not as ground truth.
- Several landmark papers cited in the notes/report predate or fall outside the OA subset and are referenced by author/year/PMID without a local PDF.
- This is a literature synthesis, **not medical advice**.
