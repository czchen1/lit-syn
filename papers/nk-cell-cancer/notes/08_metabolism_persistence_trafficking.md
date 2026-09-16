# Metabolic fitness, persistence, trafficking and the solid-tumour microenvironment

This is where NK therapy still fails, and where 2024–2026 work is concentrated.

## Metabolism is a therapeutic axis, not a biomarker

- Cytokine-driven glycolysis and OXPHOS are required for NK effector function; amino-acid-dependent cMyc
  expression is the checkpoint (PMID 29904050).
- **Obesity** drives PPAR-dependent lipid accumulation that paralyses NK metabolism and antitumour responses
  (Michelet 2018, PMID 30420624) — a patient-selection and pretreatment consideration.
- **TGF-β** represses mTOR (PMID 26884601) and drives NK metabolic dysfunction in human metastatic breast cancer
  (PMID 33568351).
- **Hypoxia** impairs cytotoxicity via SHP-1-mediated attenuation of STAT3/ERK (PMID 33123602) and via
  HIF-1α-dependent transcriptional reprogramming, whose deletion unleashes tumour-infiltrating NK activity
  (PMID 32445619); IL-2 activation can partially override hypoxic inhibition in myeloma marrow
  (PMID 23724099).
- **Autophagy** is required for NK function — C/EBPβ-dependent autophagy inhibition impairs NK cells in cancer
  (PMID 39609420) — while autophagy *in the tumour cell* degrades granzyme B and confers resistance
  (PMID 24101526).
- **Nutrient and metabolite competition:** vitamin B6 restriction by pancreatic cancer cells (PMID 37931287),
  glutamine deprivation via myCAF exosomal PWAR6 in colorectal liver metastasis (PMID 39696364), and
  lactate-driven lysine **lactylation** of NK proteins, which can be targeted to reinforce cytotoxicity
  (PMID 40494934).
- **Mitochondria:** the mitochondrial apoptosis pathway determines killing efficiency at physiological E:T
  ratios, and targeting it augments NK immunotherapy (Pan 2022, PMID 35447071); mitochondrial dynamics in the
  TME are reviewed at PMID 41075850.
- **Engineering response:** the clearest demonstration that this is actionable is CAR-NK relapse caused by loss
  of metabolic fitness and rescued by cytokine engineering (PMID 37494448); DHA supplementation
  (PMID 38526128) and fasting-induced niche remodelling (PMID 38878769) are non-genetic levers.

**Manufacturing link:** expansion conditions set the metabolic starting point. mbIL-21 feeder expansion
increases metabolic activation (PMID 31624330), and cryopreservation depletes it (see
`09_cryopreservation_potency_and_release.md`), so "metabolic fitness" is partly a process attribute that could
be released against.

## Persistence in vivo

- Without support, infused NK cells persist days; with lymphodepletion plus cytokine support they expand
  measurably in a minority of patients (10% → 27% with Treg depletion, PMID 24719405).
- Cell-intrinsic IL-15 changes the picture: IL-15-armoured CD19 CAR-NK cells were detectable long-term in
  preclinical models (PMID 28725044) and CAR19/IL-15 NK persistence was a defined secondary endpoint in the
  phase 1/2 trial (PMID 38238616).
- CIML differentiation confers weeks-long enhanced responsiveness and measurable in vivo expansion in patients
  (PMID 35349491).
- Intrinsic survival programmes matter too: 2B4 signalling inhibits NK apoptosis via pERK/BCL-2
  (PMID 37516949), and *CISH*/Regnase-1/TIPE2 edits all improve persistence or intratumoral accumulation.

## Trafficking and infiltration

- **Chemokine receptor engineering** is the direct approach: CCR7 acquisition by trogocytosis redirects expanded
  NK cells to lymph nodes (PMID 22498742); CCR7 co-delivery with a CAR by electroporation (PMID 31114587);
  CXCR3 drives NK infiltration and plasticity in colorectal liver metastasis (PMID 40168086). Homing biology is
  reviewed comprehensively at PMID 35768424.
- **Physical and stromal barriers:** cancer-associated fibroblasts act as decoys that absorb NK cytotoxicity in
  breast cancer (PMID 40052789); melanoma-associated fibroblasts reshape NK phenotype (PMID 19934056);
  αv-integrin/TGF-β signalling limits activity against glioblastoma stem cells (PMID 34138753).
- **Suppressive cell networks:** Tregs inhibit NK cells in a TGF-β-dependent manner (PMID 16230475); MDSCs
  suppress NK cells via NKp30 in hepatocellular carcinoma (PMID 19551844); tumour-associated NK cells can
  themselves drive MDSC-mediated tolerance through IL-6/STAT3 (PMID 38748775) — a reminder that infused NK
  cells are not unconditionally beneficial.
- **Rapid functional loss on entry:** NK cells become impaired within hours of entering the tumour
  (PMID 38267402), which argues that trafficking without accompanying resistance engineering is insufficient.
- **The NK–dendritic-cell axis** is the main indirect mechanism of benefit: NK cells recruit cDC1 via
  chemokines (Böttcher 2018, PMID 29429633) and an NK–DC axis defines checkpoint-therapy-responsive tumours
  (Barry 2018, PMID 29942093). This supports combining NK products with T-cell-directed therapy rather than
  positioning them as alternatives.

## Practical implications

1. Release-test metabolic/functional fitness (post-thaw 3D migration or serial-killing capacity), not just
   viability and single-round cytotoxicity.
2. Engineer for the microenvironment: TGF-β resistance, HIF-1α/hypoxia tolerance, lactate/lactylation
   resistance, and where relevant a chemokine receptor matched to the target tissue.
3. For solid tumours, consider intratumoral/intracavitary administration — the HER2 CAR-NK glioblastoma trial
   injected cells into the resection cavity (PMID 37148198), bypassing trafficking entirely.
4. Expect and exploit the NK→DC→T-cell axis when designing combination regimens.
