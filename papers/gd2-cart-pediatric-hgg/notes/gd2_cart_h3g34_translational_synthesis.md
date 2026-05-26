# GD2-targeted CAR-T for DHG-H3G34: scFv choice, engineering tradeoffs, and translational priors

## Executive summary

GD2-targeted CAR-T cell therapy is the most clinically advanced antigen-directed cell therapy in pediatric CNS tumors today (Majzner 2022, Nature, intracerebroventricular GD2-CAR in H3K27M DMG). Translation to **diffuse hemispheric glioma, H3 G34-mutant (DHG-H3G34)** has three open questions:

1. **GD2 expression** on the DHG-H3G34 malignant compartment — particularly on GSX2/DLX+ interneuron-progenitor and GABAergic-lineage cells (Chen 2020, Liu 2024) — has not been systematically published.
2. **scFv choice**: the canonical 14g2a-derived binder dominates the GD2-CAR field; hu3F8 is a humanized, higher-affinity alternative with little CAR-specific clinical data.
3. **Exhaustion mitigation**: 14g2a CARs have a well-characterized tonic-signaling exhaustion phenotype (Long 2015); rescue strategies include 4-1BB co-stimulation, c-Jun overexpression (Lynn 2019), and affinity tuning.

## 1. Anti-GD2 binder choice for a CAR scFv

### 14g2a (parent of dinutuximab / ch14.18)

- Origin: murine 14.G2a (IgG2a class-switched from 14.18 IgG3); clinically used as the chimeric mouse-human IgG1 antibody **ch14.18 / dinutuximab** (FDA-approved Unituxin, 2015) and **ch14.18/CHO / dinutuximab beta** (EMA-approved).
- CAR usage: **the de facto standard GD2-CAR binder.** Published trials with 14g2a scFv-based CARs include:
  - Majzner et al. 2022 (H3K27M DMG, intracerebroventricular + IV)
  - Pule, Heczey, Brenner et al. (neuroblastoma, multiple iterations including PD-1 combination; Heczey 2017)
  - Del Bufalo et al. 2023 (NEJM, GD2-CART01 in neuroblastoma, retroviral 14g2a-based CAR)
  - Mount et al. 2018 (preclinical GD2-CAR in H3K27M DMG, 14g2a-derived)
- Affinity: ~10⁻⁸ M (moderate). Lower affinity is in many ways *desirable* for a CAR: reduces on-target/off-tumor toxicity on peripheral nerve GD2, trogocytosis, and tonic-signaling exhaustion.
- Tonic signaling: well-documented (Long 2015). The 14g2a scFv self-aggregates on the CAR surface → antigen-independent CD3ζ phosphorylation → exhaustion. Rescued by **4-1BB co-stimulation** (vs CD28) and by framework mutations.

### hu3F8 (humanized 3F8 → naxitamab / Danyelza)

- Origin: humanized CDR-graft of murine 3F8 (Cheung lab, MSKCC). Approved as **naxitamab** (FDA, 2020) for relapsed/refractory high-risk neuroblastoma with bone/marrow disease.
- CAR usage: **limited clinical data.** Mostly preclinical Cheung-lab constructs and a few early-phase trials. No published intracranial CAR-T data.
- Affinity: ~10⁻⁹ M (5-10× higher than 14g2a in head-to-head assays).
- Epitope: binds a non-identical fine specificity vs 14g2a on the GD2 terminal sialic acid motif.
- Immunogenicity: humanized framework → much lower anti-CAR responses on re-infusion or in combination with soluble hu3F8 formats (BiTE, mAb boost).
- Tonic signaling: less systematically characterized, but humanized frameworks are reported to aggregate less than murine ones in CAR contexts.

### Recommendation for a DHG-H3G34 program

**Default = 14g2a scFv**, paired with **4-1BB co-stimulation + a safety switch** (iCasp9 or EGFRt). This piggybacks on Stanford's IND / CMC precedent for intracranial GD2-CAR in H3K27M DMG (Majzner 2022). hu3F8 is a credible second-generation candidate, particularly if combining CAR-T with a soluble hu3F8 BiTE or naked-mAb boost where its humanized framework matters most.

## 2. CAR-T engineering tradeoffs directly relevant to 14g2a

### Tonic signaling and 4-1BB co-stimulation (Long 2015, Nat Med)

- GD2-28z CARs (14g2a scFv + CD28 + CD3ζ) display **antigen-independent CD3ζ phosphorylation** driven by scFv aggregation.
- Phenotypic consequence: rapid exhaustion, expression of PD-1 / TIM-3 / LAG-3, reduced IFN-γ and IL-2, impaired in vivo persistence.
- Rescue: swapping CD28 for **4-1BB** restores function, persistence, and antitumor activity in xenograft models. The Mackall/Lynn group's subsequent constructs (including Majzner 2022) use 4-1BB.
- Practical: **use 4-1BB, not CD28, for 14g2a-based CARs**, unless there is a specific reason to need CD28's faster proliferation kinetics.

### Exhaustion resistance via c-Jun overexpression (Lynn 2019, Nature)

- Lynn et al. mapped exhaustion to an **AP-1 imbalance** (excess of inhibitory AP-1 family members vs c-Jun) in chronically stimulated CAR-T cells.
- **c-Jun overexpression** in CAR-T cells (including GD2-CARs) restores effector function, prevents terminal differentiation, and dramatically improves in vivo efficacy at low CAR doses.
- This is the most direct exhaustion-mitigation strategy for 14g2a-based programs and has been incorporated into multiple academic INDs.

### Co-stimulation / activation domain summary

| Component | Function | Choice for 14g2a GD2-CAR | Justification |
|---|---|---|---|
| scFv | Antigen recognition | 14g2a | Clinical precedent in CNS (Majzner 2022) |
| Hinge | Spacer | CD8α (short) | Standard for short-distance ganglioside binding |
| Transmembrane | Membrane anchor | CD28 or CD8α | Either acceptable |
| Co-stimulation | Activation domain | **4-1BB** | Long 2015 — reduces tonic-signaling exhaustion |
| Signaling | Activation | CD3ζ | Standard |
| Exhaustion rescue | Modulator | c-Jun overexpression (optional) | Lynn 2019 — direct GD2-CAR exhaustion rescue |
| Safety | Suicide gene | iCasp9 or EGFRt | Recommended for intracranial use |

## 3. Clinical priors from neuroblastoma GD2-CAR trials

### Heczey et al. 2017 (Mol Ther)

- Combined first-generation GD2-CAR T cells with **lymphodepletion + PD-1 inhibition** (pembrolizumab) in r/r neuroblastoma.
- Established safety of GD2-CAR + checkpoint combination.
- Efficacy was modest with first-generation CAR design but informed subsequent multi-modal regimens.
- Relevance to DHG-H3G34: validates feasibility of GD2-CAR + immune checkpoint combination, which may be particularly important given Haase 2022's cGAS/STING activation in H3G34 tumors (suggesting baseline innate immune priming that checkpoint blockade could amplify).

### Del Bufalo et al. 2023 (NEJM, GD2-CART01)

- Retroviral 14g2a-based GD2-CAR with iCasp9 safety switch in pediatric r/r neuroblastoma.
- 63% overall response rate at 17-month median follow-up; manageable cytokine release syndrome and on-target neuropathic pain.
- Confirms that a modern 14g2a CAR with safety switch is clinically tractable in pediatric patients.
- Not in this corpus' PDF set (paywalled at NEJM), but documented in `index.tsv` of the parent literature search.

## 4. Translational priors specific to DHG-H3G34

These come from the parallel H3G34 corpus (`papers/h3g34-diffuse-hemispheric-glioma/`):

- **Cell of origin**: GSX2/DLX+ fetal ventral-forebrain interneuron progenitors (Chen 2020, Liu 2024). GABAergic / migratory neuronal lineage. GD2 expression on this lineage is the empirical question.
- **DNA repair impairment + cGAS/STING activation** (Haase 2022): baseline innate immune priming. May synergize with CAR-T-induced inflammation and checkpoint blockade.
- **Immune microenvironment**: relatively cold compared to inflammatory adult GBM, but PDGFRA / MUC mutations correlate with distinct immune infiltrates (Hu 2022).
- **ALT phenotype** (Kfoury 2025): unrelated to GD2 but informs combination strategies (PARP inhibitors + immune therapy).

## 5. Recommended next experimental steps before a DHG-H3G34 GD2-CAR program

1. **GD2 IHC and flow cytometry on DHG-H3G34 PDX / primary samples.** Use 14g2a or hu3F8 as the staining antibody. Stratify by lineage state (GSX2/DLX+ vs GABAergic vs astroglial vs cycling).
2. **scRNA-seq projection of B4GALNT1 / ST8SIA1 (GD2 biosynthesis genes)** onto existing DHG-H3G34 cell-state atlases (Chen 2020, Liu 2024 datasets in `papers/h3g34-diffuse-hemispheric-glioma/`).
3. **Preclinical 14g2a-CAR efficacy** in DHG-H3G34 PDX models with intracranial delivery, paralleling the Mount 2018 design for H3K27M.
4. **Combination logic**: 14g2a-CAR + PD-1 inhibition (Heczey 2017) + cGAS/STING agonist (motivated by Haase 2022) is a reasonable triple-combination hypothesis.

## 6. Open questions and gaps

- **No DHG-H3G34 GD2-CAR paper exists yet.** This corpus assembles the building blocks; the synthesis is forward-looking.
- **Affinity tuning** for CNS use — both 14g2a (lower affinity) and hu3F8 (higher) deserve direct preclinical comparison in DHG-H3G34 models.
- **Re-dosing strategy** — currently CAR-T is one-shot. If hu3F8 scFv allows immunogenicity-safe re-infusion, that may matter more in slowly-progressing CNS disease than in fast NB relapse.

## References

See `index.tsv` for the curated paper list and links. Key references for this synthesis:

- Long et al. 2015, Nat Med — 4-1BB rescues tonic-signaling exhaustion in 14g2a CAR
- Mount et al. 2018, Nat Med — GD2 + H3K27M DMG preclinical CAR-T
- Heczey et al. 2017, Mol Ther — GD2-CAR + PD-1 inhibition in neuroblastoma
- Lynn et al. 2019, Nature — c-Jun overexpression for CAR-T exhaustion resistance
- Majzner et al. 2022, Nature — first-in-human GD2-CAR in H3K27M DMG
- Cheung et al. 2012, OncoImmunology — humanization of m3F8 → hu3F8
- Mujoo et al. 1987, Cancer Res — original 14G2a anti-GD2 antibody
- Chen et al. 2020, Cell — H3G34 interneuron-progenitor origin (in H3G34 corpus)
- Liu et al. 2024, Cancer Cell — DHG-H3G34 GABAergic lineage hierarchy (in H3G34 corpus)
- Haase et al. 2022, JCI — cGAS/STING activation in H3G34 (in H3G34 corpus)
