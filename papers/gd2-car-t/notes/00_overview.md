# GD2 CAR-T literature landscape: overview

## Eras and inflection points

- **1985–2007 — antibody era**: Murine 14G2a and 3F8 antibodies; the chimeric ch14.18 (dinutuximab) and 14.18-IL2 immunocytokine emerge. None of these are "CAR-T"; they only matter here because their VL/VH domains become the dominant scFv sources for GD2 CARs.
- **2008 — first GD2 CAR-T trial (Pule, Louis et al., Nat Med 2008 / Mol Ther 2011)**: 11 neuroblastoma patients infused with autologous activated T cells (ATCs) and autologous EBV-specific cytotoxic T cells (CTLs) each carrying a first-generation 14g2a-CD3ζ retroviral CAR. Persistence of CAR-CTLs is longer than CAR-ATCs.
- **2014 — NKT cell platform (Heczey et al., Blood 2014)**: αGalCer-expanded Vα24-invariant NKT cells transduced with second/third-generation 14G2a CARs.
- **2015–2018 — tonic-signaling, exhaustion, costimulation choice (Long 2015, Quintarelli 2018)**: 14g2a-CD28-CD3ζ CAR T cells become exhausted ex vivo from antigen-independent tonic CAR clustering driven by scFv framework regions. Adding 4-1BB rescues fitness; combined CD28+OX40 (Heczey 2017 "GD2.CAR3") used in second clinical trial in NB.
- **2017–2018 — affinity-toxicity tension (Richman 2018, Mount 2018)**: A 14G2a "E101K" CDR3 affinity-matured variant causes lethal encephalitis in mice in CD28-CD3ζ form. The standard-affinity 14g2a-4-1BB-CD3ζ in T cells (Mount 2018) is potent against H3K27M+ DIPG without cognitive toxicity in mice.
- **2017 — armored CARs (Heczey 2017 Mol Ther)**: Inducible caspase-9 (iC9) added to the GD2-CAR3 cassette as a clinical safety switch.
- **2020–2023 — CAR-NKT trial era (Heczey 2020/2023 NM, Tian 2025)**: First-in-human Vα24+ CAR-NKT with armored IL-15 (GINAKIT trial) is safe and active in relapsed/refractory NB.
- **2020–2023 — pivotal Italian and UK trials (Straathof 2020 STM 1RG-CART, Del Bufalo 2023 NEJM GD2-CART01)**: Third-generation 14.G2a-CD28-OX40-CD3ζ + iC9 GD2-CART01 in 27 NB patients with 33% CR; the Bambino Gesù manufacturing platform becomes the most widely cited clinical-stage GD2-CAR-T product.
- **2022–2025 — CNS administration for DMG/DIPG (Majzner 2022, Monje 2025)**: GD2-4-1BB-CD3ζ retroviral CAR with iCasp9 made on the CliniMACS Prodigy with IL-7+IL-15+dasatinib priming, delivered intravenously and then intracerebroventricularly via Ommaya. Best-in-class clinical activity in diffuse midline gliomas.
- **2022–2025 — non-viral and TRAC knock-in (Mueller 2022, Balke-Want 2023, Cappabianca 2024, Foster 2025)**: CRISPR-Cas9 HDR or HITI insertion of an anti-GD2 CAR into the TRAC locus using nanoplasmid donor DNA; eliminates AAV and viral-vector manufacturing.
- **2024–2026 — armoring, logic gates and allogeneic (Glienke 2022 IL-18 TRUCK, Vogt 2025 hypoxia-actuated, Moghimi 2021 synNotch B7-H3 → GD2, Quintarelli 2025 donor-derived)**.

## Cell-product diversity in GD2 CAR-T

The collection captures **at least nine distinct effector cell platforms** all carrying a GD2-targeting CAR:

| Platform | Lead papers |
| --- | --- |
| Autologous αβ-T cells (PBMC) | Pule 2008, Louis 2011, Quintarelli 2018, Del Bufalo 2023, Majzner 2022, Monje 2025, Locatelli 2025, Li 2025 |
| Virus-specific T cells (EBV-CTL) | Pule 2008, Louis 2011, Caruana 2015, Tanaka 2017 |
| Vα24-invariant NKT cells | Heczey 2014, Xu 2019, Heczey 2020, Heczey 2023, Tian 2025 |
| γδ T cells (Vγ9Vδ2) | Capsomidis 2018, Caforio 2021 |
| NK cells (PB, expanded, NK92, iPSC-NK) | Esser 2012, Prapa 2015, Bodden 2023, Antonucci 2022, Chiavelli 2024 |
| iPSC-derived T or NK | various 2024–2026 papers |
| Donor-derived (allogeneic) | Quintarelli 2025, Locatelli 2025 |
| CAR-MSC | Chulanetra 2020, Caruana 2018 era |
| CAR-macrophage / CAR-microglia | recent 2024–2026 papers in collection |

## Construct conventions

Across most published GD2 CARs the canonical layout is:

```
[Signal peptide] — [VH/VL or VL/VH scFv, usually 14g2a-derived] — [Linker, (G4S)3 or 4] — [Hinge: CD8α, IgG1 CH2CH3, IgG4, IgD] — [TM: CD8α or CD28] — [Costim: CD28, 4-1BB, OX40, CD27, ICOS — alone, paired, or 3rd-gen tandem] — [CD3ζ ITAMs] (— [P2A] — [iCasp9 or RQR8 or IL-15 or C7R])
```

Variations along each segment and their measured consequences are detailed in `01_car_architecture.md`.

## Notes on this synthesis

- Capsule extractions in `09_per_paper_extractions.md` are not a full re-write of methods sections; they distill the design/construction/manufacturing-relevant claims and parameters (vector backbone, scFv source, hinge/TM, costim, signaling, route, cytokine support, T-cell activation reagent, transduction reagent, expansion media, closed-system platform, GMP / clinical-grade status, safety switch, dose). When a paper's methods are sparse on a parameter, the field is left as `—`.
- Direct quotations are kept to a sentence or two; longer passages are paraphrased and linked back to the PDF in `pdfs/` or supplement under `supplements/`.
- When information was only available in a supplementary methods file, that origin is flagged (e.g. *Methods (supp.)* or *Supp. Table S2*).
- For paywalled clinical-trial papers (Straathof 2020, Del Bufalo 2023, Heczey 2020/2023, Locatelli 2025 main paper), construct/manufacturing details are reconstructed from (a) the same group's adjacent preclinical and methodology papers in this collection, (b) the trial registration entries on ClinicalTrials.gov, (c) publicly available supplementary methods when downloadable from publishers, and (d) shared lineage with named clinical products (e.g. GD2-CART01).
