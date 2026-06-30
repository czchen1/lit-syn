# 01 — In vivo / in situ CAR and immune-cell engineering

The single largest "novel-payload" theme in the corpus is using LNPs to **manufacture engineered immune effectors inside the patient**, eliminating apheresis, ex vivo culture, viral vectors, and (often) lymphodepletion. The encoded payload is a CAR (or chimeric switch receptor), and the engineering problem is split between *what cell to hit* and *what to leave behind* (transient mRNA vs. integrating DNA).

## Target cell types

- **T cells (CAR-T).** The canonical approach uses antibody/nanobody-decorated LNPs to deliver CAR mRNA to circulating T cells. Hunter 2025 (*Science*, PMID 40536974) reprogrammed CD8 T-cell subsets with targeted LNPs (tLNPs); Lemgart 2026 (PMID 41691371) used a VHH-based anti-CD8 targeting moiety to deliver a CD22-CAR mRNA specifically to CD8 T cells for haematological malignancies; Zhang 2025 (PNAS, PMID 40493195) used anti-CD5 LNPs co-delivering CD19-CAR mRNA plus a PSMA "tag" mRNA, with IL-7 preconditioning, achieving tumour-free survival in 75% of lymphoma-bearing mice — matching ex vivo efficacy — and demonstrating PET trackability of the in situ product.
- **Macrophages (CAR-M).** Because macrophages are tumour-tropic, phagocytic, and carry low CRS risk, in situ CAR-M is heavily represented: Xu 2026 (*Biomaterials*, PMID 41819724) screened 80 fluorinated ionizable lipids (lead A1F5C5/F5-LNP) to deliver an hPSMA-CAR mRNA IV, reprogramming the TME and synergising with anti-PD-L1; Chen 2026 (PMID 41960698) used F4/80-antibody MPLA-LNPs for a TYRP1-CAR in choroidal melanoma; Wang 2025 (PMID 40425095) used mannose-modified mRNA-LNP to generate FAP-CAR-M that strip the fibrosis barrier in pancreatic cancer; Li 2026 (*Nat Commun*, PMID 42285952) nebulised a cascade-targeted liposome to reprogram alveolar macrophages into CAR-AMs for lung cancer.
- **Fibroblast-/stroma-directed.** Bajbouj 2026 (PMID 41686204) delivered FAP-CAR mRNA via anti-CD5 tLNP, generating FAP-CAR-T in >45% of splenic / >69% of circulating / >35% of tumour-infiltrating T cells from a *single IV dose*, with anti-tumour effect ≥ that of 1×10⁷ adoptively transferred retroviral CAR-T in pancreatic cancer.

## Cargo: transient mRNA vs. integrating DNA

- **mRNA (transient).** The majority. Framed explicitly as a safety/redosing advantage; CAR expression decays over days, limiting on-target/off-tumour toxicity and CRS, at the cost of requiring repeat dosing.
- **DNA + transposase (durable).** Bimbo 2025 (*JITC*, PMID 40659448) built "NCtx", an anti-CD7/anti-CD3 targeted LNP co-encapsulating minicircle DNA (CAR) + SB100x transposase mRNA, achieving genomic CAR integration and *stable* in vivo CAR-T from a single IV dose in two xenograft models — the first demonstration of targeted-LNP DNA delivery to T cells generating integrated CAR-T in vivo.
- **Switch/logic payloads.** Fu 2026 (PNAS, PMID 41843671) delivered dual circRNAs encoding a SIGLEC9-based chimeric switch receptor to macrophages, converting inhibitory Siglec–sialic-acid signalling into activating signal to sustain the M1/tumoricidal CAR-M phenotype in glioblastoma, deployed via an injectable NP-hydrogel around the resection cavity.

## Quality control of the in-patient product

A distinctive sub-theme is that in situ generation *bypasses pre-infusion QC*, motivating imaging readouts: Zhang 2025 (PMID 40493195) co-delivered a PSMA reporter mRNA to enable PET tracking of in situ CAR-T trafficking and persistence.

## Combination and conditioning

Recurring adjuncts: IL-7 preconditioning to support engineered T-cell expansion (Zhang 2025); checkpoint blockade (anti-PD-1/PD-L1) co-administration (Xu 2026, Zhang 2026 BiME); and pairing CAR-M stromal clearance with chemotherapy (Wang 2025, gemcitabine penetration).

## Landscape reviews

Four 2025–2026 reviews frame this space and are worth reading first: Hunter 2025 (*Science*, PMID 40536974); Vilcot 2026 "Turning the patient into their own CAR factory" (*HemaSphere*, PMID 42064385); and two 2025-ASH-meeting summaries comparing viral, RNA/LNP, non-viral DNA, and gene-writing in vivo CAR platforms (Wang 2026, PMID 42174685; Xue 2026, PMID 41857667). They consistently flag the central trade-offs: efficiency, durability/persistence, reversibility, scalability, and safety.

See also notes/05 (gene editing of CAR-T, e.g. LNP co-delivery of CAR mRNA + Cas9/sgRNA for PD-1/TRAC/B2M knockout, Wang 2026 PMID 40879055) and notes/08 (the cell- and organ-targeting LNP chemistry that makes all of the above possible).
