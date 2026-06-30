# 04 — Tumour-suppressor restoration

A conceptually clean 25-paper theme: many cancers are driven by *loss* of a tumour suppressor, and mRNA-LNP offers a way to transiently **re-supply the missing protein** ("tumour-suppressor replacement therapy") — something small molecules cannot do for a lost gene. The encoded payloads are full-length suppressor mRNAs, and the engineering problem is route- and tropism-driven delivery to the relevant tissue.

## Suppressors encoded

- **PTEN.** The most common. Restoring PTEN reverses checkpoint-inhibitor resistance and re-activates anti-tumour immunity. Kim 2026 (PMID 41386375) delivers PTEN mRNA via hyaluronate-conjugated LNP (HA replacing PEG) for *transdermal* CD44-targeted delivery in melanoma; Goo 2026 (PMID 42297114) delivers PTEN mRNA across the blood-brain barrier with a single-ligand GLUT1-targeting mannose-cholesterol LNP, extending median survival in orthotopic glioblastoma (33→49 days); Hu 2026 (PMID 41696631) co-delivers PTEN mRNA + PARP1 siRNA ("mPsiP@miLAND") in castration-resistant prostate cancer, exploiting a PTEN-loss/PARP1-high synthetic vulnerability.
- **p53 / TP53.** Chen 2026 (PMID 41546399) delivers p53 mRNA with a stiffness-gated fusion-membrane carrier for selective cytoplasmic delivery to soft tumour cells in breast cancer.
- **p21 / CDKN1A.** Zeng 2026 (PMID 42144924) delivers p21 mRNA-LNP **intravesically** for bladder cancer as a localised replacement therapy, restoring nuclear p21, reducing Rb phosphorylation, and suppressing orthotopic tumour growth while preserving urothelium.
- **LATS1.** Dong 2026 (PMID 41786044) delivers LATS1 mRNA **intravitreally** (SM-102 outperforming MC3 LNP) to restore Hippo-pathway suppression of YAP in uveal melanoma.
- **NDRG2.** Reznik 2024 (PMID 38919399) delivers NDRG2 via modified-LNP self-amplifying mRNA for drug-resistant/metastatic cancers.
- **NKX3-1, p21 via RNAa.** The earliest works (Ren 2013 PMID 23836514; Place 2012 PMID 23343884) *induce endogenous* suppressors with small-activating RNA rather than supplying mRNA (see notes/06).

## Delivery routes are the story

Because suppressor restoration must reach tumour cells (not just immune cells), this bucket is unusually rich in **route engineering**: intravesical (bladder), intravitreal (eye), transdermal (skin melanoma), BBB-crossing (brain), and intratumoural. Reporter-mRNA biodistribution showing tumour-localised, transient expression with limited systemic spread is a standard control (e.g. Zeng 2026, Dong 2026).

## Co-delivery and combination

- **mRNA + siRNA in one particle.** Hu 2026 (PTEN mRNA + PARP1 siRNA) and Liao 2026 (PMID 41510588, ML-designed fluorinated-aromatic LNP co-delivering a suppressor mRNA + siRNA against p53-loss/Nrf2-hyperactivation in sorafenib-resistant HCC) show single-LNP co-formulation of an "add-back" mRNA and a "knock-down" siRNA.
- **With checkpoint blockade.** Restored PTEN/p53 frequently induces immunogenic cell death and re-sensitises to anti-PD-1/PD-L1.

## Adjacent: oncogene/driver suppression delivered as RNA

Several "reprogramming via suppression" papers sit at the border of this bucket: Lehrich 2025 (*Nat Commun*, PMID 40442146) delivers an siRNA-LNP against CTNNB1 (β-catenin) in Wnt-active HCC, driving zonal reprogramming and re-engaged IFN signalling with ICI synergy (also tagged TF/reprogramming, notes/07). These show the same logic — re-set a driver axis with transient RNA — applied to oncogenes rather than re-supplying a suppressor.

See notes/06 (RNAa and saRNA suppressor induction) and notes/08 (the route-specific targeting lipids).
