# Ex vivo expansion, feeders, media and GMP manufacturing

Dose is the binding constraint on NK therapy: NK cells are ~10% of blood lymphocytes, and clinical activity has
repeatedly tracked with cell dose and in vivo expansion. This axis is where the process-development literature
is densest (30 papers, 12 of them explicit process/method studies, plus the cryopreservation set in
`09_cryopreservation_potency_and_release.md`).

## Feeder-based expansion: the K562 engineering lineage

| Feeder | Ligands | Reported expansion | Source |
|---|---|---|---|
| K562-mb15-41BBL | membrane IL-15 + 4-1BBL | median 21.6-fold NK in 7 days (range 5.1–86.6, n=50) | Imai/Fujisaki 2009, PMID 19383914 |
| K562-mb15-41BBL in G-Rex | as above, gas-permeable static culture | up to 19 × 10⁹ NK cells in 8–10 days from unseparated apheresis | Lapteva 2012, PMID 22900959 |
| K562-mbIL21-41BBL (aAPC) | membrane IL-21 + 4-1BBL | ~1,848-fold (fresh CB) / ~2,389-fold (cryopreserved CB) in 14 days, >95% purity | Shah 2013, PMID 24204673 |
| "NKF" mbIL-21 feeder line | membrane IL-21 | >10,000-fold at 5 weeks, increased metabolic activation | PMID 31624330 |
| K562-OX40L + short soluble IL-21 | OX40L | robust expansion via OX40–OX40L axis | PMID 31105701 |
| Autologous feeder cells + IL-21 (Prodigy) | — | clinical-grade NK and anti-CD123 CAR-NK | PMID 28810809 |
| Engineered feeders displaying costimulatory molecules + IL-21 | screened combinations | improved expansion **and** transduction | PMID 40325497 |
| EBV-LCL feeders | — | clinical-grade cytotoxic NK with upregulated activating receptors and death-receptor ligands | PMID 19308771 |

Why membrane-bound presentation works: it delivers sustained, cell-contact-dependent signalling that soluble
cytokines cannot reproduce, which is why the 4-1BBL/IL-21 combination has survived 15 years of process
iteration. Feeders also **prime the cells for gene modification** — feeder-activated NK cells transduce and edit
far better than resting cells (PMID 35222382).

Feeder liabilities: an irradiated tumour-derived cell line in the process requires residual-cell testing,
irradiation validation and regulatory justification, plus a GMP feeder bank.

## Feeder-free and cell-free routes

- **PM21 particles** — plasma-membrane particles derived from K562-mb21-41BBL — give feeder-like expansion
  (mean ~825-fold ex vivo) with in vivo biodistribution data (PMID 27059202), and with added cytokines produce
  memory-like characteristics and better survival (PMID 38711506). This is the most mature "feeder benefits
  without feeder cells" platform.
- **Automated feeder-free bioreactor expansion** of clinical-grade NK cells in a closed system was demonstrated
  early (PMID 20795758) and remains the reference for feeder-free GMP.
- **Feeder-free expansion integrated with non-viral genome editing** of cryopreserved primary NK cells
  (PMID 33433623) shows the two constraints can be met simultaneously.
- A 2025 review categorises feeder-free strategies (cytokine combinations, immobilised ligands, nanoparticle and
  bead-based aAPC mimics) and their trade-offs against feeder-based yield (PMID 41089682).

## Media, serum and reagents

- **Direct comparison matters.** A 2025 Cytotherapy study screened RPMI 1640, KBM581, SCGM, NK MACS, X-VIVO 15
  and AIM-V, each with FBS, human AB serum, human platelet lysate or Immune Cell Serum Replacement, plus
  feeders, and read out viability, fold expansion, cytotoxicity, immunophenotype and transcriptome
  (PMID 39570247). Medium/supplement choice changed both yield and phenotype — it is not a neutral variable.
- Serum-free/xeno-free operation is required for GMP; platelet lysate and defined serum replacements are the
  practical substitutes for AB serum.
- GMP-compliant large-scale protocols for alloreactive NK products in AML are published with full release data,
  giving concrete comparators for yield and purity.

## Vessels, automation and scale

- **Gas-permeable static culture (G-Rex)** transformed achievable yields — 19 × 10⁹ cells from one apheresis
  product in 8–10 days (PMID 22900959) — and is used for cord-blood aAPC expansion too (PMID 24204673).
- **CliniMACS Prodigy** provides fully automated selection→activation→expansion→transduction in one closed
  device (PMID 28810809); automated primary CAR-NK manufacture for AML has been demonstrated end-to-end
  (PMID 38253870).
- **Stirred/aerated bioreactors** are the current frontier: process development for scalable NK expansion in
  aerated stirred bioreactors moves the field from *scale-out* (many flasks) to *scale-up* (one vessel)
  (PMID 40808775), and scalable NK/CAR-NK expansion process development in bioreactor systems is now being
  reported (2024).
- **Clinical-scale iPSC-NK differentiation** is its own manufacturing problem — spin-EB/feeder-free
  differentiation at clinical scale (PMID 23515118, PMID 31396935), with differentiation strategy affecting the
  resulting phenotype and cytotoxicity (PMID 39445004).

## What a modern NK manufacturing process looks like

1. **Starting material:** apheresis (CD3-depleted / CD56-selected), cord-blood unit, or iPSC master cell bank.
2. **Activation/expansion:** membrane IL-21/4-1BBL feeder cells or PM21 particles + IL-2/IL-15, in
   gas-permeable vessels or a closed automated system; 10–14 days typical, 100–2,000-fold expansion.
3. **Genetic modification (if any):** BaEV or lentiviral transduction, or Cas9 RNP electroporation, timed to the
   feeder-activation window.
4. **Programming:** terminal IL-12/15/18 preactivation for memory-like state.
5. **Harvest, formulate, cryopreserve:** DMSO-based or DMSO-free cryoprotectant, controlled-rate freeze.
6. **Release:** identity/purity (CD56+CD3−), viability, potency (cytotoxicity), residual feeder cells, vector
   copy number/editing efficiency, sterility, endotoxin, mycoplasma.

## Open process questions

- No head-to-head, multi-site comparison of feeder versus PM21 versus feeder-free media platforms using the
  same donors and the same potency assay.
- Expansion fold and cytotoxicity are reported inconsistently (different E:T ratios, targets, assay formats),
  which makes cross-paper yield comparisons unreliable.
- Bioreactor NK expansion data remain thin relative to flask/bag data, particularly for edited or
  CAR-transduced cells.
- Cost of goods is almost never reported, despite being the practical argument for allogeneic and iPSC products.
