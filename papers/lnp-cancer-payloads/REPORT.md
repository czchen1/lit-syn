# LNP delivery of novel cancer payloads — consolidated synthesis

A single end-to-end reference over the 157-paper corpus indexed in `index.tsv` (2008–2026). It consolidates the topical notes (`notes/00`–`notes/09`) and adds cross-cutting analysis along two axes: **what is encoded** (the payload) and **how it is delivered/targeted**. For per-paper capsules see `notes/09_per_paper_extractions.md`.

## Executive summary

- The field has shifted from "LNP = mRNA vaccine" to "LNP = programmable in-body factory": the patient's own cells transiently produce a therapeutic protein, edit, or fate-change. 102 of 157 curated papers are from 2025–2026.
- A small number of payloads recur because they are *potent but historically undeliverable*: **IL-12** (toxic as systemic protein), **CARs** (otherwise needing ex vivo manufacture), **lost tumour suppressors** (undruggable by small molecules), and **genome editors** (needing multi-component, cell-specific delivery). For each, the LNP solves the historical blocker by localising and time-limiting expression.
- The dominant engineering contribution is **redirecting the LNP away from its default hepatic tropism** — via lipid chemistry (lung/spleen/extrahepatic) and surface ligands (T cell, macrophage, HSC, tumour-cell).
- Clinical validation exists but is early: mRNA-2752 (phase 1, OX40L+IL-23+IL-36γ) and MTS105 (GPC3 TCE, FIH underway) are the anchors; in vivo CAR-T is the most active near-clinical frontier (multiple 2025-ASH reviews).

## Corpus and methods

Five PubMed E-utils queries (verbatim in `README.md`) targeting in vivo CAR, TF/reprogramming, gene editing, saRNA/circRNA, and mRNA-agent payloads returned 951 unique records. Regex bucketing over title+abstract plus manual review enforced three inclusion criteria — explicit LNP/lipidoid carrier, cancer indication, non-vaccine encoded payload — yielding 157 papers. PMCIDs were resolved via the NCBI PMC ID converter (94/157), and DOIs back-filled from NCBI EFetch XML (157/157). Full text was acquired as 14 open-access PDFs and 73 Europe PMC full-text XML files (EBI REST `fullTextXML`); the remaining 83 are `metadata_only` (NCBI PMC PDF endpoints sit behind a browser proof-of-work challenge unreachable from the build environment). Topic tags are multi-label; `category` is the single primary bucket.

## Part I — The payloads

### I.1 In vivo / in situ CAR (notes/01)
Encoded payload = CAR or chimeric switch receptor; effector = T cell, macrophage, NK, or alveolar macrophage. Cargo is usually transient mRNA (safety/redosing) but sometimes integrating minicircle-DNA + transposase (durability, Bimbo 2025 PMID 40659448). Single-IV-dose in situ FAP-CAR-T can exceed adoptive transfer of 10⁷ ex vivo CAR-T (Bajbouj 2026 PMID 41686204). CAR-M is favoured for solid tumours (tumour-tropism, low CRS). In-patient products lack pre-infusion QC, motivating PET-reporter co-delivery (Zhang 2025 PMID 40493195).

### I.2 Cytokines and immunomodulators (notes/02)
IL-12 dominates; the literature is really about *localising* it — intratumoural/IP/intravesical route, liver- or lung-restricted tropism, macrophage homing (β-glucan), replicon/circRNA amplification, or prodrug-lipid co-delivery (Shi 2026 PMID 41851499). Cocktails (IL-12/15/18/Casp1; OX40L/IL-23/IL-36γ) and interferons (IFN-α fusion, IFNα2-lung) extend the theme. Dose-limiting hepatotoxicity is the recurrent toxicity, managed by dose/targeting.

### I.3 Secreted antibodies / engagers (notes/03)
mRNA/saRNA-encoded BiTEs, macrophage engagers, nanobody-BiTEs, antibody-cytokine fusions expressed in situ — liver as a deliberate factory for systemic engager titres (MTS105, Huang 2025 PMID 41397962), or local IP/CNS expression to limit BiTE toxicity. Nanobody/VHH formats preferred over scFv for expression robustness.

### I.4 Tumour-suppressor restoration (notes/04)
Full-length p53/PTEN/p21/LATS1/NDRG2 mRNA "replacement"; the distinguishing feature is route engineering to reach tumour cells (intravesical, intravitreal, transdermal, BBB-crossing). Frequently co-delivered with siRNA (PTEN mRNA + PARP1 siRNA) or paired with checkpoint blockade.

### I.5 Gene editing (notes/05)
Cas9 mRNA+sgRNA, RNP, pDNA-CRISPR, and DNA-free RNA/3′UTR editing (dCas13, Huang 2026 PMID 42303814). Cancer targets: SOX2, PLK1, KRAS-G12S, CDK4/6, and PD-1/TRAC/B2M for CAR-T engineering. The defining problem is extrahepatic, cell-specific editing, solved by ligand- and organ-targeted lipids and biocompatibility upgrades (LNP-SNA, lipopolyplex).

### I.6 Non-linear coding scaffolds (notes/06)
saRNA/replicon (amplify), circRNA (persist), RNAa (induce endogenous gene), cssDNA (de-immunise vector). All exist to beat the linear-mRNA dose/toxicity/durability trade-off; IL-12 is again the canonical beneficiary. The 2008–2013 RNAa prostate/bladder papers are the field's prehistory.

### I.7 Suicide enzymes and TF reprogramming (notes/07)
GDEPT enzymes (CD-UPRT + 5-FC) revived by circRNA delivery; TF enforcement (BATF, IRF8, NIK) and M2→M1 macrophage / β-catenin-axis reprogramming. Conditional enzyme/editing-induced death is preferred over constitutive toxins.

## Part II — The delivery layer (notes/08)

- **Lipid discovery**: fluorinated, fluorinated-aromatic, "tripod" lung lipids, N→S head-group switches, ML/Bayesian-optimised composition.
- **Organ tropism**: lung (tripod LuT, pulmonary CRISPR), spleen (lipid blends), brain (GLUT1/mannose), extrahepatic (solvent-free water-based, PEG/ethanol-free).
- **Cell targeting**: anti-CD5/CD3/CD7/CD8/VHH (T cells), F4/80 + mannose (macrophages), EGFR/CD44/HA (tumour cells), aptamer/nucleolin (nuclear), apolipoprotein-fusion auto-decoration.
- **Cargo chemistry**: multi-species co-encapsulation, PEG alternatives (HA-DMG, PMeOx), stimulus-responsive release (pH charge-reversal, GSH, stiffness-gating, prodrug-lipid), and biocompatibility scaffolds (LNP-SNA, cssDNA).
- **Quality metrics**: <120–150 nm, PDI ~0.1, >80–90% encapsulation, plus phenotypic transfection/editing readouts.

## Part III — Cross-cutting analysis

1. **Transient vs durable expression is the central design fork.** mRNA's decay is sold as safety in CAR/cytokine work but as a limitation when persistence matters, prompting moves to saRNA/circRNA (longer) or integrating DNA/transposase (permanent). Expect this fork to define the next wave of clinical programs.
2. **Toxic payloads drive delivery innovation.** Nearly every IL-12 paper is a localisation paper; the payload choice (IL-12) is essentially fixed and the novelty is the carrier/route. The same is true for BiTEs (CRS) and editors (off-target/off-tissue).
3. **Hepatic tropism: bug or feature.** Liver-targeting is exploited when the target is hepatic (GPC3 HCC) or when secreted-protein titre is the goal (engagers, fusions), but is the primary obstacle for solid-tumour editing and suppressor restoration — hence the large extrahepatic-lipid literature.
4. **Combination is the norm, monotherapy the exception.** Single-LNP co-delivery (two mRNAs, mRNA+siRNA, mRNA+Cas9+sgRNA) and pairing with checkpoint blockade or chemotherapy recur throughout.
5. **Open questions.** Durability/redosing schedules; immunogenicity of repeated dosing and of novel lipids; reproducible extrahepatic targeting in humans (vs mouse); manufacturing/QC of in-situ-generated cell products; and whether transient in vivo CAR can match ex vivo durability without integration.

## Provenance and limitations

This is a literature-curation artifact, not an experimental dataset. Abstract-derived capsules (notes/09) should be verified against full text via the DOI/PMID links in `index.tsv` before use. 83 papers are catalogued from metadata + abstract only because of environment-level access constraints (see README); all carry resolvable identifiers. Topic classification is regex-assisted and manually reviewed but multi-label and inevitably imperfect at the margins.
