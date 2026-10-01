# Expansion and adoptive‑transfer platforms

Turning γδ T cells into a medicine requires getting enough of the *right* cells in the *right* state. The manufacturing literature splits along the same Vγ9Vδ2 vs Vδ1 axis as the biology, and along autologous vs allogeneic.

## A. Vγ9Vδ2 expansion (the classic route)

Because Vγ9Vδ2 cells respond to phosphoantigen, they can be selectively expanded from PBMCs without sorting:

- **Aminobisphosphonate + IL‑2.** Zoledronate (or pamidronate) inhibits FPPS → intracellular IPP accumulates in monocytes/APCs → presented via BTN3A1 → selective Vγ9Vδ2 outgrowth. Plus IL‑2 over ~10–14 days this yields highly enriched Vγ9Vδ2 products. Foundational for clinical manufacturing (e.g. PMID 19016372 large‑scale zoledronate expansion from cancer patients; PMID 28239463 pulse‑zoledronate enhancement).
- **Synthetic phosphoantigens.** BrHPP (Phosphostim, IPH1101) and related agonists give more reproducible, GMP‑friendly expansion than bisphosphonates in some protocols.
- **Cytokine choice shapes phenotype.** IL‑2 is standard; adding/substituting **IL‑15** improves memory/persistence and antitumor fitness, while **IL‑18/IL‑12** push IFN‑γ. The IL‑2 vs IL‑15 trade‑off recurs across the corpus (e.g. PMID 42039157 review of IL‑15 vs IL‑2 divergent effects).
- **In‑vivo activation** (bypassing ex‑vivo culture): systemic zoledronate + low‑dose IL‑2 to expand endogenous Vγ9Vδ2 cells (PMID 20491785) — simple but limited by patient cell fitness and IL‑2 toxicity.

**Limitations:** repeated phosphoantigen stimulation drives Vγ9Vδ2 **senescence/exhaustion**; the subset can be scarce or dysfunctional in heavily pre‑treated patients; and in‑vivo activation gave mostly transient, modest clinical responses (see `07_clinical_trials.md`).

## B. Vδ1 / pan‑γδ expansion (Delta One T and beyond)

Vδ1 cells are not phosphoantigen‑responsive, so they require different mitogens:

- **DOT (Delta One T) protocol:** a two‑step, clinical‑grade method using **anti‑CD3 (OKT3) plus a defined cytokine cocktail** (e.g. IL‑4/IFN‑γ/IL‑21/IL‑1β/IL‑15 across phases) to selectively expand and differentiate **Vδ1** cells with high NCR (NKp30/NKp44) expression and potent cytotoxicity, while depleting αβ T cells for allogeneic safety (Almeida/Silva‑Santos; commercialized via GammaDelta Therapeutics / Lava / Takeda lineage).
- **Artificial APC / feeder systems:** engineered K562‑based aAPCs (expressing costimulatory ligands ± membrane IL‑15/IL‑21) and irradiated PBMC feeders expand total or Vδ1 γδ cells to clinical scale.
- **Agonist antibodies / bispecifics during culture** and **CD3 agonists** for non‑Vδ2 expansion.

Vδ1's appeal: tissue‑homing, **lactate/hypoxia resistance** (PMID 42106736), adaptive‑like clonal focusing, and lower γδ17 propensity — favored for solid tumors and off‑the‑shelf CAR products (ADI‑001).

## C. Allogeneic, off‑the‑shelf logic

The strongest strategic argument for γδ over αβ in cell therapy is **allogeneic use**: because γδ recognition is HLA‑independent, HLA‑mismatched γδ cells carry **low GvHD risk**, enabling banked, donor‑derived products. Requirements that recur in manufacturing papers:

- **αβ T‑cell depletion** (to remove GvHD‑causing cells) — often combined with **CD19/CD20 selection** or magnetic γδ‑TCR selection.
- **Scalable, closed‑system, GMP** expansion (feeders/aAPC or DOT), with cryopreservation and release testing.
- **Donor selection** (e.g. CMV serostatus shapes Vδ1 repertoire).
- Clinical‑grade **automated platforms** are now emerging, including for **CAR‑γδ** (PMID 42253960 automated CAR‑γδ manufacturing platform).

## D. Haploidentical / transplant‑adjacent use
Beyond engineered products, **haploidentical γδ cells** (or αβ‑depleted grafts enriched for γδ) have induced remissions in chemorefractory B‑NHL (PMID, "Haploidentical γδ T Cells Induce Complete Remission…"), and αβ/CD19‑depleted haplo‑HSCT enriches reconstituting γδ cells associated with better outcomes — a bridge between transplantation and γδ immunotherapy.

## Manufacturing decision summary
| Decision | Vγ9Vδ2 route | Vδ1/DOT route |
| --- | --- | --- |
| Mitogen | zoledronate/BrHPP + IL‑2 | OKT3 + cytokine cocktail / aAPC |
| Selectivity | high (intrinsic) | needs αβ depletion |
| Persistence lever | add IL‑15 | NCR‑high differentiation |
| Allogeneic | yes (deplete αβ) | yes (built‑in αβ depletion) |
| Main risk | exhaustion/senescence, γδ17 | harder/longer expansion |
