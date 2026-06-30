# Biodistribution, protein corona, and in vivo fate

## The protein corona as the true identity of an LNP

When an LNP enters the bloodstream, serum proteins immediately adsorb onto its surface, forming a "protein corona" that effectively becomes the particle's biological identity. The corona — not the synthetic surface — determines which receptors recognize the LNP and which cells internalize it.

## Corona composition drives organ tropism

Key findings from this corpus:

### Liver targeting (ApoE corona)
- Standard four-component LNPs (ionizable lipid + DSPC + cholesterol + PEG) adsorb apolipoprotein E (ApoE) → recognized by LDLR on hepatocytes.
- ApoE adsorption is enhanced by: neutral surface charge, low PEG density, DSPC as helper lipid.
- This is the "default" pathway; extrahepatic targeting means disrupting or replacing it.

### Lung targeting (complement/Ig corona)
- SORT cationic LNPs recruit complement C3, C4, vitronectin, and immunoglobulins (Dilliard et al. 2023).
- These opsonins promote uptake by lung endothelial cells via complement receptors and Fc receptors.

### Spleen targeting (fibronectin/fibrinogen corona)
- Anionic or zwitterionic LNPs recruit fibrinogen, fibronectin, and albumin.
- These proteins direct uptake by splenic marginal-zone macrophages and B cells.

## Measuring biodistribution

### Luciferase mRNA
- Most common reporter: Firefly or NanoLuc luciferase mRNA.
- IVIS (in vivo imaging system) whole-animal bioluminescence → organ-level distribution.
- Limitation: measures only cells that successfully translate mRNA, not total particle distribution.

### DNA barcodes
- Allow multiplexed biodistribution measurement (see notes/04).
- qPCR or sequencing of organ homogenates → quantitative per-organ delivery of 100+ formulations simultaneously.

### Radiolabeling / fluorescence
- ⁸⁹Zr-labeled or DiR-loaded LNPs for PET/fluorescence organ quantification.
- Measures total particle distribution (not just functional delivery).
- Disconnect between particle accumulation and functional mRNA expression is common and important.

## Particle-level vs functional delivery

A recurring theme: **organ accumulation ≠ functional delivery**. An LNP may accumulate in an organ (measured by lipid radiolabel or DNA barcode) but fail to deliver functional mRNA (measured by luciferase) if:
1. Endosomal escape is poor in that cell type.
2. The LNP is trapped in non-target cells (e.g., Kupffer cells capture liver-directed LNPs but don't express the cargo).
3. The cargo is degraded before translation.

Bian et al. (2024, PMID 38259198) demonstrate that sequence-activated fluorescent reporters can distinguish organ-level accumulation from cell-level functional delivery.

## Clearance and toxicity

- **First-pass hepatic clearance**: most IV-administered LNPs are cleared by liver within 1–4 hours.
- **Complement activation**: cationic LNPs (lung-targeting) activate complement more strongly → risk of CARPA (complement activation-related pseudoallergy).
- **Repeated dosing**: anti-PEG antibodies develop after 2–3 doses, accelerating clearance (the "ABC phenomenon").
- **Spleen as a sink**: the spleen captures a significant fraction of all LNPs regardless of targeting; improving liver-to-lung or liver-to-brain ratios often means reducing spleen uptake as well.

## Papers (selected)

- Dilliard SA et al. (2021) PMID 34272381 — Protein corona mechanism of SORT.
- Dilliard SA et al. (2023) PMID 37527764 — Corona composition for lung targeting.
- Bian Y et al. (2024) PMID 38259198 — Sequence-activated fluorescent reporters for organ-resolved delivery.
- Cheng Q et al. (2020) PMID 32251383 — Biodistribution of SORT LNPs across organs.
- Simonsen JB (2024) — Review of extrahepatic delivery strategies and corona effects.
