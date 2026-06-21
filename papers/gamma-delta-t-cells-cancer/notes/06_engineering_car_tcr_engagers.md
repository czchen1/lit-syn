# Engineering γδ T cells: CARs, TCR transfer, and engagers

The 2018→present surge is dominated by **redirecting** γδ T cells with a defined tumor specificity while keeping their innate killing. Four engineering modalities recur. The clinical‑grade automation of these processes is itself now a topic (e.g. automated CAR‑γδ manufacturing, PMID 42253960; CAR‑engineering of innate/innate‑like cells review, PMID 42082268).

## 1. CAR‑γδ T cells

A chimeric antigen receptor (scFv–hinge–TM–costim–CD3ζ) is expressed in γδ rather than αβ cells. Rationale:
- **Dual targeting:** the CAR provides antigen‑specific killing *and* the cell retains NKG2D/phosphoantigen/ADCC channels → harder antigen‑escape.
- **Allogeneic‑ready:** HLA‑independent → off‑the‑shelf with low GvHD.
- **Tissue homing / innate APC** functions as a bonus.

Representative work in the corpus:
- **GD2‑CAR Vγ9Vδ2** for neuroblastoma — early proof that CAR‑γδ cells expand, kill, and cross‑present (Capsomidis 2018; Caforio 2021).
- **CD20‑CAR allogeneic Vδ1** — the basis of **ADI‑001** (PMID 35136603, "Allogeneic CD20‑targeted γδ T cells exhibit innate and adaptive antitumor activities").
- **CD155/PVR‑oriented and B7‑H3 CAR‑γδ** for solid/CNS tumors, including **intrathecal allogeneic B7‑H3 CAR‑γδ for leptomeningeal metastasis** (PMID, recent clinical, see index).
- **γδ‑enriched CAR‑T for bone‑metastatic castrate‑resistant prostate cancer** (PMID 37134157).
- **CAR‑Vγ9Vδ2 propagated with a bisphosphonate prodrug** for allogeneic use (PMID, "CAR‑Modified Vγ9Vδ2 T Cells Propagated Using a Novel Bisphosphonate Prodrug").
- **Baboon‑envelope pseudotyped lentivirus** to transduce γδ cells efficiently (PMID, 2025).
- **Non‑viral / "super Vδ2"** CAR‑γδ via transposon/CRISPR knock‑in for r/r AML (PMID 42284763).

Engineering nuances specific to γδ: transduction can be harder than αβ; vector/promoter and costimulatory choice (CD28 vs 4‑1BB) interact with γδ metabolism; and tonic‑signaling/exhaustion concerns carry over from the CAR‑αβ field.

## 2. Defined γδ‑TCR transfer — TEGs

Instead of putting a CAR into γδ cells, **TEGs (T cells Engineered to express a defined γδ TCR)** put a tumor‑reactive **Vγ9Vδ2 TCR into αβ T cells** (Sebestyen, Kuball et al.). This combines:
- the **broad, HLA‑independent, metabolic‑stress recognition** of a high‑avidity γδ TCR (sensing the BTN2A1/BTN3A1 "phosphoantigen/dysregulated mevalonate" signature), with
- the **manufacturability and persistence** of αβ T cells.

**TEG001** (a high‑affinity Vγ9Vδ2 TCR in αβ cells) entered clinical testing for hematologic malignancies. The approach reframes the γδ TCR itself as the therapeutic "drug."

## 3. Antibody–TCR fusions and γ/δ‑TCR‑T

A hybrid modality couples antibody specificity to TCR/CD3 signaling:
- **AbTCR** (antibody‑TCR) T‑cell therapy — CD19‑directed, reported safe/effective in r/r B‑cell malignancies (PMID, "A novel antibody‑TCR (AbTCR) T‑cell therapy…").
- **CD19‑specific γ/δ TCR‑T** for r/r DLBCL (PMID, 2023).
- **Antibody‑γ/δ TCR** targeting **GPC2** to regress neuroblastoma at **low antigen density** (PMID 41027430) — exploiting γδ‑TCR signaling sensitivity for low‑density antigens where conventional CARs fail.

## 4. Bispecific γδ‑T‑cell engagers (γδ‑bsTCEs)

Rather than transferring cells, **bispecific antibodies** recruit endogenous (or co‑administered) γδ cells to tumor:
- **(tumor antigen) × Vγ9** or **× Vδ2** engagers crosslink Vγ9Vδ2 cells to HER2, CD123, EGFR, PSMA, etc.
- **CD1d × Vδ2** bispecifics (e.g. the LAVA platform) engage Vδ2 cells against CD1d⁺ tumors (myeloma/leukemia).
- Combination with αβ‑directed bispecifics: mosunetuzumab (CD20×CD3) was reported to also improve **Vγ9Vδ2** responses (PMID 40558... "Two Are Better than One"), showing engager strategies can co‑opt γδ cells.

Engager appeal: **off‑the‑shelf biologic** (no cell manufacturing), dosable/titratable; limitation: depends on the patient's endogenous γδ pool and fitness.

## 5. Armoring and gene edits
As in CAR‑αβ, γδ products are being **armored** (membrane/secreted **IL‑15**, IL‑18, checkpoint‑resistant designs, anti‑PD‑1 secretion — e.g. PMID 37... "Anti‑PD1 antibody armored γδ T cells" in ovarian cancer) and **edited** (knock‑out of inhibitory receptors/checkpoints, safety switches, αβTCR/HLA knockouts for allogeneic safety).

## Modality comparison
| Modality | What's engineered | Off‑the‑shelf? | Key strength | Key limitation |
| --- | --- | --- | --- | --- |
| CAR‑γδ | CAR into γδ cell | Yes (allog.) | Dual (CAR + innate) killing | Transduction; exhaustion |
| TEG | γδ TCR into αβ cell | No (autologous‑like) | Broad stress recognition + αβ manufacturability | Mixed‑dimer/MHC concerns |
| AbTCR / γδ‑TCR‑T | Ab or γδTCR signaling module | Varies | Low‑antigen‑density sensitivity | Newer, less clinical data |
| γδ bsTCE | Bispecific antibody | Yes (biologic) | No cell manufacturing | Relies on endogenous γδ fitness |
