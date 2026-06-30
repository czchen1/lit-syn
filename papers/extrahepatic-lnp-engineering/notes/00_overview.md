# Overview — Extrahepatic / organ-targeted LNP engineering

## Landscape

This collection captures 189 papers (2013–2026; 147 from 2024–2026) on the enabling science behind **non-liver-directed lipid nanoparticle delivery** — the engineering challenge that determines whether the novel payloads catalogued in the companion `lnp-cancer-payloads` collection can actually reach their intended organ, tissue, or cell type.

The default tropism of conventional four-component LNPs (ionizable lipid + helper phospholipid + cholesterol + PEG-lipid) is hepatocytes, driven by ApoE adsorption and LDLR-mediated uptake. The papers here address how to redirect that tropism to lungs, spleen, brain, immune cells, and other tissues.

## Topic taxonomy

| Category | n | Core question |
|---|---|---|
| **organ_targeting** | 63 | How to formulate LNPs for selective organ delivery (SORT, charge tuning, helper-lipid ratios) |
| **lipid_engineering** | 42 | Design/synthesis of novel ionizable lipids, structure–activity relationships, combinatorial libraries |
| **extrahepatic** | 20 | Broad extrahepatic redirection strategies (not organ-specific) |
| **inhalation** | 13 | Nebulization, dry-powder, lung-targeted delivery via inhalation route |
| **lung_targeting** | 12 | Systemic IV-to-lung targeting via formulation chemistry |
| **spleen_targeting** | 10 | Spleen-selective formulations (immune priming, tolerance) |
| **ml_optimization** | 10 | ML/AI/HTS-driven lipid discovery and formulation optimization |
| **immune_cell_targeting** | 9 | T cell, macrophage, dendritic cell, NK cell, HSC targeting |
| **brain_targeting** | 9 | Blood–brain barrier crossing, CNS delivery strategies |
| **biodistribution** | 1 | Pure pharmacokinetics/biodistribution studies |

Cross-cutting topic tags (a paper may carry multiple):
- lipid_engineering (71), organ_targeting (63), extrahepatic (51), biodistribution (39)
- lung (32), lipid_library (28), ml_optimization (27), spleen (21)
- lung_targeting (18), endosomal (18), brain (17), spleen_targeting (16), inhalation (16)
- immune (13), immune_cell_targeting (10), targeting_ligand (10), brain_targeting (9)

## Temporal structure

- **2013–2019 (9 papers):** Foundational work — ionizable lipid SAR (Jayaraman/Maier 2012 era; our earliest is 2013), early combinatorial screens, first demonstration that ionizable-lipid pKa shifts organ tropism.
- **2020–2023 (33 papers):** SORT (Cheng et al. 2020, PMID 32251383) establishes that adding a fifth "SORT molecule" to any four-component LNP redirects delivery from liver → lung/spleen. Dilliard & Siegwart (2021) elucidate the protein-corona mechanism. DNA barcode-based in vivo screening (FIND, b-DNA) enables massively parallel lipid evaluation.
- **2024–2026 (147 papers):** Explosion of diversity — ML-designed lipid libraries (FALCON, transformer-based), multi-organ targeting via charge-laddered formulations, peptide/antibody-conjugated LNPs for cell-type specificity, inhaled/nebulized LNP for lung disease, brain-targeting via BBB-crossing ionizable lipids.

## Recurring design themes

1. **Ionizable-lipid headgroup pKa controls organ tropism.** Low pKa (6.0–6.4) → liver; higher pKa (6.5–7.0) → spleen; intermediate → lung. This is partly mediated by differential protein-corona composition.
2. **Permanent charge (SORT) overrides lipid-intrinsic tropism.** Cationic SORT molecules (e.g. DOTAP) redirect to lung; anionic SORT → spleen; zwitterionic helpers tune liver/spleen balance.
3. **Endosomal escape efficiency is organ-dependent.** A lipid that excels in hepatocytes may fail in lung epithelial cells — ionizable lipid libraries need to be screened in each target cell context.
4. **In vivo barcoded screening has replaced in vitro transfection** as the primary assay for lipid discovery. DNA/mRNA barcodes allow 100+ formulations to be tested in one animal.
5. **Machine learning accelerates lipid discovery.** Bayesian optimization, graph neural networks, and transformer models predict transfection efficiency and organ specificity from lipid structure.
6. **Route of administration is a lever, not just a delivery detail.** Inhalation, intrathecal, and intramuscular routes change the formulation requirements (mucus penetration, surfactant compatibility, stability).

## Conventions

- Papers are referenced by first author, year, and PMID.
- `category` is the primary topic; `topics` lists all applicable tags (semicolon-separated).
- `status`: `fulltext_xml` (58 papers with Europe PMC XML), `metadata_only` (131 papers catalogued from title+abstract+DOI/PMID).
