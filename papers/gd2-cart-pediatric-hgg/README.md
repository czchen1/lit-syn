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
- `pdfs/` — downloaded open-access PDFs where available. Several PMC endpoints currently return CAPTCHA / anti-bot pages in our environment; those rows are marked `download_blocked; see URL` (same convention as the H3G34 corpus).

## Scope notes

This collection prioritizes papers that directly inform GD2-CAR design choices for pediatric CNS glioma. Adult solid-tumor GD2-CAR papers and the broader CAR-T literature are included only when they establish a mechanism (tonic signaling, exhaustion, co-stimulation) that is design-relevant for the 14g2a scFv. GD2 chemistry and antibody discovery papers are noted as references but not downloaded in full.

## Cross-references to the H3G34 corpus

- H3G34 tumors arise in GSX2/DLX+ interneuron progenitors (Chen 2020, Liu 2024 in the H3G34 corpus). GD2 expression in this GABAergic / neuronal-lineage state has not been systematically published and is the key empirical unknown before any GD2-targeted therapy in DHG-H3G34.
- The H3G34 cGAS/STING activation phenotype (Haase 2022) and altered immune microenvironment (Hu 2022) are relevant priors for a CAR-T trial in this disease.
