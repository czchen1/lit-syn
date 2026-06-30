# 08 — LNP engineering and targeting (the delivery layer)

72 of 157 papers carry an LNP-engineering tag, because for novel cancer payloads the *delivery* is usually the contribution. The default LNP goes to the liver; almost every payload above (CAR cells, lung/brain tumours, T cells, macrophages, HSCs) needs that redirected. This note catalogues the engineering levers that recur across the collection.

## Ionizable-lipid discovery

- **Functional/structural lipid libraries with phenotypic screens.** Fluorinated ionizable lipids — Xu 2026 (PMID 41819724) screened 80, lead A1F5C5 with 5 fluorines uniquely conferring membrane-fusion-driven endosomal escape for macrophage delivery; Liao 2026 (PMID 41510588) used ML-guided SAR over 120 degradable lipids to design fluorinated-aromatic LNPs for mRNA+siRNA co-delivery.
- **ML / Bayesian optimisation of composition.** Hiraki 2026 (PMID 41887390) used Bayesian optimisation to find HSC-targeting LNPs; ML feature-importance recurs as a design method.

## Organ-selective and extrahepatic tropism

- **Lung.** Tian 2026 (*Nat Biomed Eng*, PMID 41845088) — 444-lipid "LuT" library; top "tripod-like" lipids (quaternary-amine head, three alkyl legs, short handle) give >90% lung selectivity and 9.2× CRISPR editing vs DOTAP-SORT. Marschhofer 2026 (PMID 41506374) optimised pulmonary CRISPR LNPs for intratracheal mucus penetration.
- **Atomic-level tropism switching.** Duan 2026 (PMID 41386688) — a nitrogen-to-sulfur head-group swap on ALC-0315 redirects from liver to lung, and a 1:2 blend with the parent lipid gives spleen targeting (and antigen-specific CTLs).
- **Brain / BBB.** Goo 2026 (PMID 42297114) — single-ligand GLUT1-targeting mannose-cholesterol LNPs (~30 mol% ligand, DC-cholesterol restoring >90% encapsulation) for BBB transcytosis + glioblastoma uptake delivering PTEN mRNA.
- **Spleen / extrahepatic generally.** Streiber 2026 (PMID 41913646) — organic-solvent-free, PEG- and ethanol-free, water-based LNPs (PMeOx stealth) that prefer extrahepatic tissue and transfect primary human immune cells for CRISPR.

## Cell-type targeting ligands

Antibody/nanobody and small-ligand decoration is ubiquitous: anti-CD5 (Bajbouj 2026, Zhang 2025), anti-CD8 VHH (Lemgart 2026), anti-CD7/anti-CD3 (Bimbo 2025), F4/80 (Chen 2026), EGFR (Masarwy 2025), CD44 peptide / hyaluronate (Zeng 2026, Kim 2026), mannose for macrophages (Wang 2025), AS1411 aptamer/nucleolin (Xu 2026), β-glucan for Peyer's-patch M-cell→macrophage routing (Luo 2026). Park 2025 (PMID 39908463) uses an apolipoprotein fusion to *spontaneously* coat LNPs with a targeting antibody.

## Cargo chemistry: co-delivery, PEG replacement, responsiveness

- **Co-encapsulation of multiple species** — two mRNAs (engager + cytokine; Che 2026), mRNA+siRNA (Hu 2026, Liao 2026), Cas9 mRNA + multiple sgRNAs (Wang 2026), or core-/surface-separated dual loading: Gabelmann 2025 (PMID 40412659) lipopolyplexes screen 18 polymer cores and find surface-loaded mRNA more transfection-efficient and shear-resistant than core-loaded.
- **PEG alternatives** to mitigate anti-PEG immunity and add targeting: hyaluronate-DMG (Kim 2026), PMeOx (Streiber 2026).
- **Stimulus-responsive release.** pH-responsive charge-reversal + glutathione-triggered antibody release (Zhang 2026 BiME); stiffness-gated fusion-membrane carriers for selective cytoplasmic delivery to soft tumour cells (Chen 2026); prodrug ionizable lipids that release a small-molecule (IDO inhibitor) intracellularly alongside the mRNA (Shi 2026, PMID 41851499).
- **Biocompatibility upgrades.** CRISPR LNP-spherical-nucleic-acids (Han 2025, PMID 40906807) add a DNA shell for higher uptake and lower cytotoxicity; cssDNA scaffolds (Hu 2026) lower vector immunogenicity vs plasmid.

## Recurring quality metrics

Across papers the reported critical attributes are consistent: hydrodynamic diameter <120–150 nm, low PDI (~0.1), near-neutral/negative zeta potential, >80–90% encapsulation, plus phenotypic readouts (transfection %, editing %, endosomal-escape mechanism by cryo-TEM/imaging). Hepatotoxicity and weight loss at high mRNA dose are the most common safety findings, generally managed by dose reduction or organ/cell targeting rather than payload change.

This delivery layer is what makes the payload-specific notes (01–07) feasible; consult them for the therapeutic application of each formulation.
