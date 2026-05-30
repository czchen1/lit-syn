# GD2-targeted CAR-T for pediatric high-grade glioma — literature synthesis

Companion corpus to `papers/h3g34-diffuse-hemispheric-glioma/`. Curated papers covering:

- Anti-GD2 antibodies (14G2a / ch14.18 / dinutuximab, 3F8 / hu3F8 / naxitamab) and their use as CAR-T scFv binders
- GD2 expression and GD2-CAR T cell efficacy in pediatric CNS tumors (H3K27M DMG today, with extrapolation to H3G34 DHG)
- CAR-T engineering principles directly relevant to the 14g2a scFv: tonic signaling, exhaustion, co-stimulation (CD28 vs 4-1BB), and exhaustion-resistance strategies (c-Jun, AP-1 axis)
- Clinical neuroblastoma CAR-T trials that establish GD2-CAR feasibility, safety, and PD-1 combination logic

The goal is to support a "would GD2-CAR work in DHG-H3G34?" translational analysis, sitting next to the developmental / lineage / DNA-repair literature on G34 tumors.

## Directory structure

- `index.tsv` — curated paper metadata (matches the columns used in `papers/h3g34-diffuse-hemispheric-glioma/index.tsv`).
- `notes/gd2_cart_h3g34_translational_synthesis.md` — synthesis of the binder choice (14g2a vs hu3F8), CAR-T engineering tradeoffs, and design recommendations for a hypothetical H3G34 GD2-CAR program.
- `pdfs/` — downloaded open-access PDFs and supplementary files (PDF / xlsx / docx). PMC fronts every download with a small SHA-256 proof-of-work challenge (`cloudpmc-viewer-pow` cookie); see `scripts/download_pmc_pdf.py` (main article PDFs) and `scripts/download_pmc_supps.py` (supplementary files at `articles/instance/<num>/bin/<file>`) for pure-Python solvers used to fetch these from scripted environments.

## Supplementary data

Every paper for which PMC hosts supplementary files now has them downloaded alongside the main PDF, with filenames `<paper>_supp*.{pdf,xlsx,docx}`:

- **Long 2015** — `long_2015_supp1.pdf` (supplementary figures), `long_2015_supp2.xlsx` (gene expression / NanoString tables)
- **Mount 2018** — `mount_2018_supp1.pdf` (supplementary figures), `mount_2018_supp2.pdf` (supplementary methods)
- **Lynn 2019** — `lynn_2019_supp_fig.pdf` (supplementary figures, large), `lynn_2019_supp_tab1.xlsx`, `lynn_2019_supp_tab2.xlsx` (RNA-seq / ATAC-seq tables)
- **Majzner 2022** — `majzner_2022_supp1.pdf` through `majzner_2022_supp3.pdf` (supplementary figures and methods), `majzner_2022_supp_protocol.docx` (clinical trial protocol), `majzner_2022_supp_tab1.xlsx` through `majzner_2022_supp_tab9.xlsx` (patient-level data, antigen profiling, single-cell / cytokine tables)
- **Heczey 2017** — `heczey_2017_supp1.pdf`, `heczey_2017_supp2.pdf` (supplementary figures, methods, and patient data)

## Scope notes

This collection prioritizes papers that directly inform GD2-CAR design choices for pediatric CNS glioma. Adult solid-tumor GD2-CAR papers and the broader CAR-T literature are included only when they establish a mechanism (tonic signaling, exhaustion, co-stimulation) that is design-relevant for the 14g2a scFv. GD2 chemistry and antibody discovery papers are noted as references but not downloaded in full.

## Cross-references to the H3G34 corpus

- H3G34 tumors arise in GSX2/DLX+ interneuron progenitors (Chen 2020, Liu 2024 in the H3G34 corpus). GD2 expression in this GABAergic / neuronal-lineage state has not been systematically published and is the key empirical unknown before any GD2-targeted therapy in DHG-H3G34.
- The H3G34 cGAS/STING activation phenotype (Haase 2022) and altered immune microenvironment (Hu 2022) are relevant priors for a CAR-T trial in this disease.
