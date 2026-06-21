# Antigen recognition and stress surveillance

γδ T cells recognize tumors through (1) the γδ TCR sensing metabolic/stress signals and (2) a parallel set of germline‑encoded NK‑type receptors. Understanding these channels is essential because every therapeutic strategy either exploits one of them (agonist antibodies, bisphosphonates) or bypasses them entirely (CARs, defined‑TCR transfer, engagers).

## Phosphoantigen sensing by Vγ9Vδ2 (the BTN2A1/BTN3A1 axis)

The defining feature of the blood‑dominant Vγ9Vδ2 subset is its response to **phosphoantigens (pAg)** — small pyrophosphate metabolites:
- **HMBPP** (from the microbial non‑mevalonate isoprenoid pathway), an extremely potent agonist.
- **IPP** (isopentenyl pyrophosphate) from the host **mevalonate** pathway, which accumulates in stressed/transformed cells and after pharmacologic blockade of downstream farnesyl‑pyrophosphate synthase (FPPS) by **aminobisphosphonates** (zoledronate).

The presenting machinery, resolved over the last decade, is a **two‑butyrophilin** system:
- **BTN3A1 (CD277)** binds pAg in its intracellular **B30.2** domain ("inside‑out" sensing); this is the long‑sought essential pAg‑sensing molecule (Harly, Sandstrom, Vavassori, Sebestyen ~2012–2014).
- **BTN2A1** binds the **Vγ9** TCR germline region directly and cooperates with BTN3A1 to trigger the cell (Rigau et al. *Science* 2020; Karunakaran et al. *Nature* 2020). Recent structural work describes butyrophilin multimers acting via a "plier‑like" mechanism for Vγ9Vδ2 TCR engagement (PMID 40505658).

**Therapeutic consequences.**
- **Aminobisphosphonates** (zoledronate) raise intracellular IPP in tumor and accessory cells, sensitizing them to Vγ9Vδ2 killing and driving selective ex‑vivo expansion — the foundation of first‑generation therapy and many combination strategies (e.g. PMID 28239463 pulse zoledronate; PMID 20491785 in‑vivo zoledronate + low‑dose IL‑2).
- **Agonist anti‑BTN3A antibodies (ICT01, Imcheck)** force BTN3A1 into the activating conformation, activating Vγ9Vδ2 cells against tumors independent of the mevalonate state — now in clinical trials (EVICTION).
- **BTN2A1 as a target/biomarker.** BTN2A1 levels tune γδ killing capacity (PMID 39475356); tumor‑intrinsic regulation of butyrophilins is an escape axis — e.g. BTN3A1 can also drive Vγ9Vδ2 **exhaustion** in cervical cancer (PMID, see index "BTN3A1 expressed in cervical cancer…"), and EBV BRRF1 induces BTN2A1 in nasopharyngeal carcinoma (PMID 39769218).

## NK‑receptor / stress‑ligand recognition (both subsets, esp. Vδ1)

Independently of the TCR, γδ cells use germline‑encoded activating receptors to read "stressed/transformed" surfaces:
- **NKG2D** ↔ **MICA/MICB, ULBP1‑6** (stress‑induced; commonly upregulated on tumors). A dominant antitumor recognition channel, especially for Vδ1.
- **DNAM‑1 (CD226)** ↔ **CD155 (PVR)/CD112** — recently shown to determine AML targeting by Vδ1 DOT cells (PMID 38437507).
- **NKp30, NKp44, NKp46** (natural cytotoxicity receptors) ↔ tumor ligands (e.g. B7‑H6, PCNA‑associated, BAG6) — prominent on activated Vδ1.
- **KIRs** define a potent effector program in human γδ cells (PMID 42044172) and can be inhibitory checkpoints.

## TCR ligands beyond phosphoantigen

Some γδ TCRs recognize defined surface molecules directly, independent of MHC: **CD1d/lipid** (Vδ1, Vδ3), **EPCR** (endothelial protein C receptor), **annexin A2**, **MR1**, and the stress molecule **butyrophilin‑like (BTNL)** family in epithelia. These broaden the "stress surveillance" concept and inform defined‑TCR therapeutic transfer (TEGs) where a tumor‑reactive γδ TCR with known ligand specificity is moved into a more easily manufactured cell.

## Why engineering often *bypasses* native recognition

Native recognition is broad but (a) **variable across patients/tumors**, (b) **down‑modulated** by the tumor microenvironment (low pAg, butyrophilin dysregulation, NKG2D‑ligand shedding), and (c) **hard to control**. Hence the engineering era largely **redirects** γδ cells with a defined specificity (CAR, transferred TCR, or bispecific engager) while **retaining** their innate killing channels as a bonus — the explicit rationale for allogeneic CAR‑Vδ1 and CAR‑Vγ9Vδ2 products (see `06_engineering_car_tcr_engagers.md`).
