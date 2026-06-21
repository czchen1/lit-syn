# Gamma‑delta (γδ) T cells in cancer: a synthesis

A comprehensive synthesis of the published literature on **γδ T cells in cancer**, consolidating the topical notes in `notes/` into a single end‑to‑end reference. It is built from the **1,125‑paper corpus** indexed in `index.tsv` (552 open‑access PDFs in `pdfs/`), assembled from a PubMed search focused on the therapeutic/translational question: *can γδ T cells be turned into a cancer medicine, and how?*

It is organized as: **Part I — Biology & recognition** · **Part II — Effector function & the dual role** · **Part III — Manufacturing** · **Part IV — Engineering** · **Part V — Clinical** · **Part VI — Discussion**.

For topical deep‑dives see the numbered notes (`00_overview.md` … `10_per_paper_extractions.md`). For per‑paper capsules see `notes/10_per_paper_extractions.md`.

---

## Table of contents

- [Executive summary](#executive-summary)
- [Corpus and methods](#corpus-and-methods)
- [Glossary](#glossary)
- **Part I — Biology & recognition**
  - [I.1 What γδ T cells are](#i1-what-γδ-t-cells-are)
  - [I.2 The δ‑chain subset framework](#i2-the-δ-chain-subset-framework)
  - [I.3 How γδ cells recognize tumors](#i3-how-γδ-cells-recognize-tumors)
- **Part II — Effector function & the dual role**
  - [II.1 Antitumor effector mechanisms](#ii1-antitumor-effector-mechanisms)
  - [II.2 The double‑edged sword: protumor γδ cells](#ii2-the-double-edged-sword-protumor-γδ-cells)
  - [II.3 The prognosis debate](#ii3-the-prognosis-debate)
- **Part III — Manufacturing**
  - [III.1 Vγ9Vδ2 expansion](#iii1-vγ9vδ2-expansion)
  - [III.2 Vδ1 / DOT expansion](#iii2-vδ1--dot-expansion)
  - [III.3 Allogeneic, off‑the‑shelf logic](#iii3-allogeneic-off-the-shelf-logic)
- **Part IV — Engineering**
  - [IV.1 CAR‑γδ](#iv1-car-γδ)
  - [IV.2 Defined‑TCR transfer (TEGs)](#iv2-defined-tcr-transfer-tegs)
  - [IV.3 AbTCR and γδ‑TCR‑T](#iv3-abtcr-and-γδ-tcr-t)
  - [IV.4 Bispecific γδ‑engagers](#iv4-bispecific-γδ-engagers)
  - [IV.5 Armoring and edits](#iv5-armoring-and-edits)
- **Part V — Clinical**
  - [V.1 Generation 1: autologous/in‑vivo Vγ9Vδ2](#v1-generation-1-autologousin-vivo-vγ9vδ2)
  - [V.2 Generation 2: allogeneic & engineered](#v2-generation-2-allogeneic--engineered)
  - [V.3 Agonists and engagers](#v3-agonists-and-engagers)
  - [V.4 Combinations & resistance](#v4-combinations--resistance)
- **Part VI — Discussion**
  - [VI.1 What the field has learned](#vi1-what-the-field-has-learned)
  - [VI.2 Open questions](#vi2-open-questions)
  - [VI.3 Outlook](#vi3-outlook)

---

## Executive summary

γδ T cells are a small, conserved T‑lineage that recognizes tumors **without classical MHC restriction**, kills through multiple redundant pathways, and — critically for cell therapy — can be used **allogeneically with low graft‑versus‑host risk**. These properties have made them a perennial candidate for cancer immunotherapy for over two decades.

The field's history is a story of two corrections:
1. **From "γδ = good" to "it depends on subset/polarization."** A famous pan‑cancer analysis ranked a γδ signature as among the most favorable prognostic immune populations, but subsequent work showed γδ cells can be powerfully **protumor** — chiefly the IL‑17⁺ "γδ T17" cells that recruit immunosuppressive myeloid cells and promote metastasis and radioresistance.
2. **From autologous Vγ9Vδ2 to allogeneic, engineered products.** First‑generation autologous Vγ9Vδ2 therapy (aminobisphosphonate/IL‑2 expanded) was reproducibly **safe but only modestly effective**, limited by persistence, trafficking, and the immunosuppressive tumor microenvironment (TME). The modern field has pivoted to **banked allogeneic** cells, **Vδ1/DOT** platforms for solid tumors, and **engineered redirection** (CAR‑γδ, defined‑TCR transfer/TEGs, antibody‑TCR fusions, and bispecific γδ‑engagers).

The clearest clinical responses to date are in **hematologic malignancies** (allogeneic anti‑CD20 CAR‑Vδ1/ADI‑001, haploidentical γδ cells, CD19 AbTCR/γδ‑TCR‑T). **Solid tumors** remain the hard problem, driving today's emphasis on Vδ1 subsets, IL‑15 armoring, checkpoint and antigen‑release combinations, and improved trafficking. The unifying design goal across the corpus is to **lock γδ cells into the cytotoxic (IFN‑γ⁺) program, deliver them to the tumor, and keep them functional in the TME — while avoiding the protumor γδ17 state.**

## Corpus and methods

- **1,125 papers** indexed (1 of 1,126 PMIDs failed metadata fetch). Strong recency skew (~600 from 2020+), reflecting the engineering/clinical surge.
- **552** open‑access PDFs retrieved (Europe PMC OA subset); **206** PMC records not OA; **367** without PMCID.
- Two de‑duplicated PubMed queries (therapy‑core + CAR/engineering); see `README.md` for exact strings.
- Heuristic categories (navigation only): ~515 primary research, 376 reviews, 112 clinical/trial‑tagged, 104 engineering, 18 commentary.
- **A note on rigor:** category/topic tags are keyword‑assigned and approximate; a small tail of tangential papers is included by the keyword search. Landmark papers predating or outside the OA subset are cited by author/year/PMID without a local file.

## Glossary

- **Vγ9Vδ2 (Vγ2Vδ2):** blood‑dominant, phosphoantigen‑reactive γδ subset.
- **Vδ1:** tissue‑resident, "adaptive‑like" subset; basis of DOT/CAR‑Vδ1 products.
- **Phosphoantigen (pAg):** small pyrophosphates (HMBPP microbial; IPP host) that activate Vγ9Vδ2 via butyrophilins.
- **BTN3A1 / BTN2A1:** butyrophilins that sense/present pAg and engage the Vγ9Vδ2 TCR.
- **NKG2D / DNAM‑1 / NCRs / KIR:** germline‑encoded NK‑type receptors for stress‑ligand recognition.
- **γδ T17:** IL‑17‑producing, generally protumor γδ cells.
- **DOT cells:** Delta One T — clinical‑grade expanded Vδ1 product.
- **TEG:** αβ T cell engineered to express a defined γδ TCR.
- **AbTCR:** antibody–TCR fusion using TCR/CD3 signaling.
- **bsTCE / γδ‑engager:** bispecific antibody crosslinking γδ cells to tumor.
- **ADCC:** antibody‑dependent cellular cytotoxicity (CD16/FcγRIII).

---

# Part I — Biology & recognition

## I.1 What γδ T cells are

γδ T cells develop in the thymus alongside αβ cells but are exported as comparatively pre‑programmed effectors, seeding blood (1–10% of T cells) and, more heavily, epithelial/mucosal tissues, liver, and gut. They span an **innate‑like ↔ adaptive‑like** spectrum: rapid, NK‑receptor‑driven responses at one end; clonally focused, antigen‑experience‑shaped responses at the other. (Full detail: `notes/01_biology_and_subsets.md`.)

## I.2 The δ‑chain subset framework

- **Vγ9Vδ2** — blood‑dominant, innate‑like, **phosphoantigen‑reactive**, trivially expandable with aminobisphosphonates; the basis of essentially all first‑generation therapy.
- **Vδ1** — tissue‑resident, adaptive‑like, stress‑ligand‑driven (NKG2D/NCRs), enriched in solid tumors; harder to expand but **TME‑adapted** (lactate/hypoxia resistant; PMID 42106736) and **less γδ17‑prone** — the leading solid‑tumor and CAR platform (ADI‑001, DOT).
- **Vδ3 / Vδ1⁻Vδ2⁻** — minor, liver/leukemia‑enriched, less developed.

The recurring strategic fork — **Vγ9Vδ2 vs Vδ1** — propagates into every downstream design choice (expansion method, allogeneic strategy, target indication).

## I.3 How γδ cells recognize tumors

Two parallel channels (full detail: `notes/02_antigen_recognition.md`):

1. **γδ‑TCR / phosphoantigen (Vγ9Vδ2).** Intracellular pAg (host **IPP** from the mevalonate pathway; microbial **HMBPP**) is sensed by **BTN3A1** (B30.2 domain, "inside‑out") and presented together with **BTN2A1**, which binds the Vγ9 germline region directly. Aminobisphosphonates raise IPP and sensitize tumors; **anti‑BTN3A agonists (ICT01)** force activation; tumor butyrophilin dysregulation is an escape (and exhaustion) axis.
2. **NK‑receptor / stress‑ligand recognition (both subsets, esp. Vδ1).** **NKG2D**↔MICA/B/ULBPs, **DNAM‑1**↔CD155/CD112 (PMID 38437507), **NKp30/44/46**↔tumor ligands, and **KIR**‑defined programs (PMID 42044172). Some γδ TCRs also bind defined ligands directly (CD1d/lipid, EPCR, annexin A2, BTNL).

Native recognition is **broad but variable and TME‑suppressible**, which is exactly why the engineering era largely **redirects** γδ cells with a defined specificity while **retaining** these innate channels as a bonus.

---

# Part II — Effector function & the dual role

## II.1 Antitumor effector mechanisms

γδ killing is **multi‑modal and largely HLA‑independent** (full detail: `notes/03_antitumor_effector_mechanisms.md`):
1. **Perforin/granzyme** granule cytotoxicity (dominant in expanded products).
2. **Death‑receptor** killing via **TRAIL/FasL** (engages granule‑resistant tumors; mesothelioma dissection PMID 37006249).
3. **ADCC** via induced **CD16** — directly combinable with approved tumor mAbs.
4. **Cytokines** (IFN‑γ, TNF‑α) that inhibit tumor, upregulate MHC, and license αβ responses.
5. **Professional antigen presentation** ("γδ‑APC"; Brandes *Science* 2005) — bridging innate and adaptive immunity.
6. **NK‑receptor‑driven** cytotoxicity (NKG2D/DNAM‑1/NCRs/KIR).

Redundancy makes single‑pathway antigen escape harder than for CAR‑αβ — a core selling point. But effector output only matters if cells **survive and traffic** in the TME (lactate/hypoxia/TGF‑β/adenosine; CXCR3‑dependent homing, PMID 42208977).

## II.2 The double‑edged sword: protumor γδ cells

The single most important nuance (full detail: `notes/04_dual_role_and_protumor.md`): γδ cells are **not uniformly antitumor**. The **IL‑17⁺ γδ T17** program is reliably **protumor** — recruiting neutrophils/MDSCs (the *Nature* 2015 breast‑metastasis paradigm), driving angiogenesis (CRC/HCC), and promoting **radioresistance** (PMID 41055972). Additional suppressive states include regulatory (IL‑10/TGF‑β) and exhausted γδ cells, and tumor **BTN3A1‑driven Vγ9Vδ2 exhaustion**.

The antitumor↔protumor **fork** is controlled by subset, priming cytokines (IL‑12/18/IFN‑γ → cytotoxic; TGF‑β/IL‑1β/IL‑23/IL‑6 → γδ17), microbiome/chronic inflammation, and metabolic context. **Implication:** manufacturing and indication selection deliberately steer away from γδ17.

## II.3 The prognosis debate

The optimistic anchor (γδ signature favorable pan‑cancer; Gentles *Nat Med* 2015) was later argued to be **confounded** by signature deconvolution, and direct studies show **context dependence**: γδ infiltration is favorable in some tumors (Vδ1/IFN‑γ‑biased) and unfavorable in others (γδ17‑biased). The durable lesson: **subset and polarization predict outcome better than total γδ count** (e.g. CRC heterogeneity PMID 41953027; CD69⁺ Vδ1 as the HCC antitumor subset).

---

# Part III — Manufacturing

(Full detail: `notes/05_expansion_and_adoptive_platforms.md`.)

## III.1 Vγ9Vδ2 expansion

**Aminobisphosphonate (zoledronate) + IL‑2** (or synthetic pAg BrHPP) selectively expands Vγ9Vδ2 from PBMCs without sorting (PMID 19016372; pulse‑zoledronate PMID 28239463). **IL‑15** improves memory/persistence vs IL‑2 (PMID 42039157); IL‑18/IL‑12 push IFN‑γ. In‑vivo activation (zoledronate + low‑dose IL‑2, PMID 20491785) is simpler but limited. Main liability: **repeated‑stimulation senescence/exhaustion**.

## III.2 Vδ1 / DOT expansion

Vδ1 cells need non‑pAg mitogens: the **DOT (Delta One T)** protocol uses **OKT3 + a defined cytokine cocktail** to expand NCR‑high cytotoxic Vδ1 cells while depleting αβ cells; artificial APCs (K562‑based, membrane IL‑15/IL‑21) and humanized Vδ1‑TCR‑antibody protocols also exist (PMID 42106736). Vδ1's tissue tropism, **lactate resistance**, and lower γδ17 propensity favor solid tumors.

## III.3 Allogeneic, off‑the‑shelf logic

The strongest strategic argument for γδ over αβ: **HLA‑independent recognition → low GvHD → banked allogeneic products.** Requirements: **αβ‑TCR depletion**, scalable closed‑system GMP (feeders/aAPC/DOT), donor selection (CMV shapes Vδ1), cryopreservation, release testing. **Automated CAR‑γδ manufacturing platforms** are emerging (PMID 42253960). Haploidentical/αβ‑depleted grafts provide a transplant‑adjacent bridge (CRs in chemorefractory B‑NHL).

---

# Part IV — Engineering

(Full detail: `notes/06_engineering_car_tcr_engagers.md`.)

## IV.1 CAR‑γδ

A CAR in γδ cells provides **antigen‑specific killing + retained innate killing**, is **allogeneic‑ready**, and adds tissue‑homing/APC functions. Examples: GD2‑CAR Vγ9Vδ2 (Capsomidis 2018; Caforio 2021); **allogeneic anti‑CD20 CAR‑Vδ1 = ADI‑001** (PMID 35136603); B7‑H3 CAR‑γδ (intrathecal, leptomeningeal mets); PSCA γδ‑CAR + zoledronate for bone mCRPC (PMID 37134157); bisphosphonate‑prodrug‑propagated allogeneic CAR‑Vγ9Vδ2; baboon‑envelope LV transduction; non‑viral "super Vδ2" for AML (PMID 42284763). Nuances: harder transduction, costimulation–metabolism interactions, tonic‑signal/exhaustion carryover from CAR‑αβ.

## IV.2 Defined‑TCR transfer (TEGs)

**TEGs** put a high‑avidity **Vγ9Vδ2 TCR into αβ T cells**, combining broad HLA‑independent metabolic‑stress recognition with αβ manufacturability/persistence. **TEG001** entered clinical testing for hematologic malignancies. Reframes the γδ TCR itself as the "drug."

## IV.3 AbTCR and γδ‑TCR‑T

Antibody specificity coupled to TCR/CD3 signaling: **CD19 AbTCR** (safe/effective in r/r B‑cell disease), **CD19 γ/δ TCR‑T** for r/r DLBCL, and **antibody‑γ/δ‑TCR targeting GPC2** that regresses neuroblastoma at **low antigen density** (PMID 41027430) — exploiting γδ‑TCR signaling sensitivity where CARs fail.

## IV.4 Bispecific γδ‑engagers

Off‑the‑shelf biologics recruiting endogenous γδ cells: (tumor antigen)×Vγ9/Vδ2 engagers; **CD1d×Vδ2** (LAVA platform) for CD1d⁺ heme tumors; and αβ‑directed bispecifics that also co‑opt Vγ9Vδ2 (mosunetuzumab, "Two Are Better than One"). No cell manufacturing, but depends on endogenous γδ fitness.

## IV.5 Armoring and edits

Membrane/secreted **IL‑15**, IL‑18, **anti‑PD‑1‑secreting** ("armored") γδ cells (ovarian), checkpoint‑resistant designs, inhibitory‑receptor/checkpoint knockouts, safety switches, and αβTCR/HLA knockouts for allogeneic safety. "Dual modulation" of activating + inhibitory receptors tunes DOT efficacy (PMID 40240620).

---

# Part V — Clinical

(Full detail: `notes/07_clinical_trials.md` and `notes/08_combinations_and_resistance.md`.)

## V.1 Generation 1: autologous/in‑vivo Vγ9Vδ2

In‑vivo (zoledronate + low‑dose IL‑2) and adoptive (ex‑vivo expanded) autologous Vγ9Vδ2 across lymphoma/myeloma (Wilhelm 2003), prostate (Dieli 2007), renal, breast, lung (PMID NSCLC experience), CRC, HCC: **reproducibly safe**, with immune/PD responses but **low ORR and short persistence**. Failure modes: scarce/exhausted patient cells, senescence, IL‑2 toxicity, poor trafficking, suppressive TME.

## V.2 Generation 2: allogeneic & engineered

The pivot: **ADI‑001** (allogeneic anti‑CD20 CAR‑Vδ1; responses incl. CRs in r/r B‑NHL), **DOT cells** (Vδ1; AML/solid), **TEG001**, **haploidentical γδ** (CRs in chemorefractory B‑NHL), CD19 **AbTCR/γδ‑TCR‑T**, and CAR‑γδ for **solid/CNS** tumors (B7‑H3 intrathecal; intracranial MGMT‑modified γδ + temozolomide; bone mCRPC). Clearest responses are in **B‑cell malignancies and AML**.

## V.3 Agonists and engagers

**ICT01** (anti‑BTN3A agonist; EVICTION ± anti‑PD‑1), **γδ bispecific engagers** (CD1d×Vδ2 etc.), and **rIL‑15** support — "drug, not cell" approaches that recruit/sustain endogenous γδ cells.

## V.4 Combinations & resistance

Combinations: **ADCC mAbs**, **zoledronate sensitization**, **checkpoint blockade** (anti‑PD‑1‑armored γδ, ovarian; ICT01+pembro), **radiation/oncolytic virus/antigen‑release** (γδ‑TCR‑T + OV for DMG, PMID 40076788), **IL‑15** support. Resistance: NKG2D/CD155‑ligand loss‑or‑shedding, butyrophilin subversion (incl. BTN3A1‑driven exhaustion), metabolic hostility, γδ17 repolarization, checkpoint upregulation, poor trafficking, antigen‑density limits.

---

# Part VI — Discussion

## VI.1 What the field has learned

1. **Safety is solved; persistence/trafficking/TME are not.** γδ products are reliably well tolerated (including allogeneic, low GvHD) — the enabling fact for off‑the‑shelf development — but durable solid‑tumor efficacy remains elusive.
2. **Subset and polarization beat raw numbers.** Cytotoxic IFN‑γ⁺ Vδ1/Vγ9Vδ2 are therapeutic; γδ17 is a liability. Both manufacturing and indication selection must steer the fork.
3. **Allogeneic + engineered + combination is the consensus modern bet,** with Vδ1 favored for solid tumors and IL‑15/armoring/checkpoint as fitness levers.
4. **Hematologic first.** The clinical signal is strongest in B‑cell malignancies and AML; solid tumors lag.

## VI.2 Open questions

- **Which subset wins where?** Vγ9Vδ2 vs Vδ1 vs pan‑γδ remains unsettled and likely indication‑specific.
- **Can γδ17 be reliably suppressed in vivo,** especially when stimulating endogenous cells (bisphosphonates, agonists) in protumor‑prone tumors (CRC, HCC, breast, pancreas)?
- **Persistence vs exhaustion:** how to expand to clinical doses without senescing Vγ9Vδ2 or losing Vδ1 fitness.
- **Trafficking into solid tumors** (chemokine engineering, e.g. CXCR3) — still early.
- **CAR vs TCR vs AbTCR vs engager:** which redirection modality, and does retained innate killing measurably reduce antigen escape in patients?
- **Biomarkers:** can butyrophilin status, subset composition, or γδ‑TIL transcriptomes predict response and stratify patients?

## VI.3 Outlook

The most likely near‑term wins are **allogeneic, engineered B‑cell‑malignancy products** (CAR‑Vδ1/ADI‑001‑class, AbTCR/γδ‑TCR‑T) and **agonist/engager biologics**. Solid‑tumor success will hinge on combining a **TME‑adapted subset (Vδ1)** with **armoring (IL‑15), trafficking engineering, and TME‑reprogramming partners**, while explicitly avoiding the protumor γδ17 program. The defining advantage of the lineage — **MHC‑independent, low‑GvHD, multi‑modal killing** — keeps γδ T cells one of the most compelling chassis for the next generation of off‑the‑shelf cell therapy.

---

*This document synthesizes published literature for research purposes and is **not medical advice**. Specific trial names, sponsors, and outcomes are summarized from the corpus and standard public references; consult primary sources and registries for authoritative detail.*
