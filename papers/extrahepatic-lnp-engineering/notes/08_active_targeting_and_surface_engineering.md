# Active targeting and surface engineering

## Passive vs active targeting

The formulation-based approaches in notes/01–03 (SORT, ionizable lipid headgroup/tail tuning) are **passive** or **intrinsic** targeting strategies — they alter the LNP's biophysical properties to change how the body distributes it. **Active targeting** adds a specific ligand to the LNP surface that binds a receptor on the desired target cell.

## Antibody-conjugated LNPs

### Anti-CD5 / anti-CD3 for T cells
The paradigm established by Rurik et al. (Nature 2022; in companion collection) uses anti-CD5 antibody conjugated to the PEG-lipid via maleimide–thiol chemistry. Several papers here optimize:
- Antibody fragment format (Fab, scFv, VHH/nanobody) — smaller formats reduce steric hindrance and improve LNP diffusion.
- Conjugation chemistry: maleimide–thiol (most common), click chemistry (DBCO-azide), SpyCatcher–SpyTag (for modular swapping).
- Antibody density on LNP surface: too low = no targeting; too high = steric crowding reduces PEG shielding.

### Anti-CD117 for HSCs
Targeting hematopoietic stem cells in bone marrow for gene editing (sickle cell, thalassemia context but LNP engineering principles apply).

### Anti-HER2 / anti-EGFR for tumors
Antibody-targeted LNPs for tumor delivery — limited by tumor penetration and the enhanced permeability and retention (EPR) debate.

## Peptide-targeted LNPs

### Peptide codes for organ selectivity
Chang et al. (2026): surface-displayed peptides swapped modularly to redirect the same core LNP to different organs — a "peptide code" approach.

### Cell-penetrating peptides (CPPs)
- TAT, penetratin, and other CPPs conjugated to PEG-lipid.
- Enhance cellular uptake but reduce organ specificity (CPPs are not cell-selective).
- Useful in combination with organ-targeted formulations to boost total transfection.

### Organ-homing peptides
- RGD (integrin-targeting, tumor vasculature).
- GALA (pH-responsive fusogenic peptide, enhances endosomal escape).
- ApoE-mimetic peptides (liver/brain targeting via LDLR).

## Small-molecule ligands

- **Mannose**: targets mannose receptor (CD206) on dendritic cells and macrophages.
- **Folate**: targets folate receptor (overexpressed on many cancer cells).
- **GalNAc**: targets asialoglycoprotein receptor (ASGPR) on hepatocytes — the gold standard for liver targeting but not useful for extrahepatic.
- **Hyaluronic acid**: targets CD44 (overexpressed on many tumor cells and activated macrophages).

## PEG-lipid engineering

The PEG-lipid is a double-edged sword:
- **Needed**: prevents opsonization, extends circulation half-life, controls particle size.
- **Problem**: inhibits cellular uptake and endosomal escape ("PEG dilemma").

Solutions:
- **Cleavable PEG**: acid-labile (orthoester, hydrazone), enzyme-cleavable (MMP-sensitive), or diffusible short-chain PEG (C14-PEG vs C18-PEG).
- **PEG density**: lower mol% (0.5–1.5%) for extrahepatic targets (slower clearance allows tissue accumulation) vs higher (3–5%) for inhaled formulations (mucus penetration).

## Papers (selected)

- Chang T et al. (2026) — Peptide codes for organ-selective mRNA delivery.
- Jin X et al. (2026) — Magnetic LNPs for targeted mRNA delivery.
- Wei C et al. (2026) — FAP-synergistic organ-targeted LNPs.
- Kularatne RN et al. (2022) PMID 35890195 — Rational design of antibody-conjugated LNPs.
- Liu S et al. (2021) PMID 33542471 — Membrane-destabilizing ionizable phospholipids.
