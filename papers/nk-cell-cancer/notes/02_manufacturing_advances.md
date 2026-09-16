# The manufacturing advances that matter, with numbers

Dose and post-thaw fitness are the two manufacturing outputs that determine whether a good design becomes a good
product. This note ranks the process advances by how much they change those two outputs.

## 1. Membrane-bound ligand presentation solved the dose problem (2009–2016)

The single most consequential manufacturing lineage in the field. Soluble cytokines cannot reproduce sustained,
contact-dependent costimulation; engineered K562 feeders can.

| Platform | Ligands | Reported yield | Source |
|---|---|---|---|
| K562-mb15-41BBL | membrane IL-15 + 4-1BBL | median **21.6-fold** NK in 7 days (5.1–86.6, n=50) | Imai/Fujisaki 2009, PMID 19383914 |
| K562-mb15-41BBL in G-Rex | + gas-permeable static culture | up to **19 × 10⁹** NK cells in 8–10 days from unseparated apheresis | Lapteva 2012, PMID 22900959 |
| K562-mbIL21-41BBL aAPC | membrane IL-21 + 4-1BBL | **~1,848-fold** (fresh CB) / **~2,389-fold** (cryopreserved CB) in 14 days, >95% purity | Shah 2013, PMID 24204673 |
| mbIL-21 feeder line ("NKF") | membrane IL-21 | **>10,000-fold** at 5 weeks, with increased metabolic activation | PMID 31624330 |
| K562-OX40L + short soluble IL-21 | OX40L | robust expansion via OX40–OX40L | PMID 31105701 |
| EBV-LCL feeders | — | clinical-grade cytotoxic NK, upregulated activating receptors and death-receptor ligands | PMID 19308771 |

Two things to take from the table. First, **IL-21 replaced IL-15 as the expansion ligand** because it buys
proliferative capacity without terminal differentiation — and the mbIL-21 platform also raises metabolic
activation (PMID 31624330), which is the attribute that later predicts in vivo durability (PMID 37494448).
Second, the vessel is not a detail: the same feeder in a gas-permeable vessel produced a ~1,000× larger absolute
yield (PMID 22900959).

Cost of feeders: an irradiated tumour-derived line inside the process means a GMP feeder bank, irradiation
validation and residual-feeder-cell release testing.

## 2. Cell-free mimics of feeders (the advance that removes the feeder liability)

**PM21 particles** — plasma-membrane particles from K562-mb21-41BBL cells — give feeder-like expansion (mean
~825-fold) with in vivo biodistribution data (PMID 27059202), and with added cytokines yield memory-like
characteristics plus improved survival from one process (PMID 38711506). This is the most mature "feeder benefit
without feeder cells" route and is the strongest candidate to make the feeder-versus-feeder-free argument moot.

Feeder-free alternatives worth knowing: automated feeder-free closed-system bioreactor expansion of clinical-
grade NK cells (PMID 20795758), feeder-free expansion integrated with non-viral editing of **cryopreserved**
primary NK cells (PMID 33433623), and a 2025 review categorising cytokine-only, immobilised-ligand and
nanoparticle aAPC-mimic strategies against feeder-based yield (PMID 41089682).

## 3. Media and supplements are a potency variable, not a procurement detail

A 2025 Cytotherapy study screened six media (RPMI 1640, KBM581, SCGM, NK MACS, X-VIVO 15, AIM-V) against four
supplements (FBS, human AB serum, human platelet lysate, Immune Cell Serum Replacement) with feeders, reading out
viability, fold expansion, cytotoxicity, immunophenotype **and** transcriptome (PMID 39570247). Medium/supplement
choice changed both yield and phenotype. The practical implication is unwelcome: expansion data are not portable
between labs running different media, which is a large part of why the platform comparison in §6 is missing.

## 4. Automation and closure moved NK manufacturing from artisanal to process

- **CliniMACS Prodigy**: selection → activation → expansion → transduction in one closed device, used with
  autologous feeders + IL-21 for clinical-grade NK and anti-CD123 CAR-NK (PMID 28810809).
- **End-to-end automated primary CAR-NK manufacture** for AML has been demonstrated (PMID 38253870) — the
  relevant milestone is that CAR-NK production no longer requires an open, operator-dependent process.
- **Feeders raise transduction, not just proliferation** (PMID 35222382; engineered feeders displaying screened
  costimulatory molecules + IL-21 improve both, PMID 40325497). Delivery method and expansion platform therefore
  have to be co-optimised; choosing them independently leaves efficiency on the table.
- **Gene delivery** options now include baboon-envelope pseudotyped lentivirus (used in a clinical CD19-BBz
  CAR-NK product, PMID 40251398), alpharetroviral vs lentiviral head-to-head (PMID 32117200), mRNA/plasmid
  electroporation (PMID 31114587), Cas9 RNP electroporation reaching ~90% editing of primary NK (PMID 31704085),
  and site-specific knock-in that combines a knockout with a knock-in in one edit (PMID 35135865,
  PMID 38493479).

## 5. Scale-up is finally displacing scale-out

Flask/bag processes scale by multiplication; bioreactors scale by volume. Process development for NK expansion in
**aerated stirred bioreactors** (PMID 40808775) plus recent scalable NK/CAR-NK bioreactor process work is the
current frontier, and it is where the field is thinnest — almost all published yield data come from static
vessels, and virtually none from edited or CAR-transduced cells in stirred systems.

For iPSC products the analogous advance is **clinical-scale, feeder-free differentiation** (PMID 23515118,
PMID 31396935), with the caveat that differentiation strategy itself changes phenotype and cytotoxicity
(PMID 39445004) — i.e. the differentiation protocol is a critical process parameter, not a preamble.

## 6. What the manufacturing literature still cannot tell you

- **No head-to-head platform comparison.** Nobody has run feeder cells vs PM21 particles vs feeder-free media on
  shared donors with one potency assay and one cryopreservation step. Every yield comparison across papers is
  confounded by medium, vessel, donor and assay.
- **Non-comparable potency reporting.** Expansion fold, E:T ratio, target line and assay format differ so widely
  that quantitative meta-analysis is not possible — a real limitation of this corpus, not just of this review.
- **Cryopreservation is under-reported in exactly the papers that need it.** Clinical papers rarely report
  post-thaw function, despite the evidence that it is where potency is lost (PMID 33067467) — see
  `03_failure_modes.md` and `05_potency_and_release.md`.
- **Cost of goods is essentially absent**, even though it is the central argument for allogeneic, cord-blood and
  iPSC approaches.
