# Potency, mechanism & selectivity

## Mechanism (shared)
EZH2 is the catalytic SET-domain subunit of **PRC2** (with EED, SUZ12, RBBP4/7);
it uses the cofactor **S-adenosyl-L-methionine (SAM)** to write H3K27me1/2/3.
Every clinical-stage inhibitor here is a **SAM-competitive** small molecule that
binds the cofactor pocket and blocks methyl transfer — they are *not* substrate
(H3-peptide) competitive. EED can also be blocked **allosterically** (EED226,
MAK683, A-395) by occupying the H3K27me3-binding aromatic cage that normally
allosterically activates PRC2; this bypasses the SAM site and can overcome
SAM-site resistance mutations.

Two consequences recur throughout the corpus:
- **Pharmacodynamics lag exposure.** Because H3K27me3 is a stable chromatin mark,
  target engagement (loss of global H3K27me3) and phenotype develop over **days**,
  and re-methylation after washout is slow. Dosing/PD readouts (H3K27me3 by WB/IHC)
  matter more than instantaneous plasma levels.
- **Gain-of-function (GOF) EZH2 mutants** (Y641F/N/S/H/C, A677G, A687V) shift
  substrate preference toward tri-methylation, elevating H3K27me3 and creating a
  dependency that inhibitors exploit (basis of the FL indication).

## Biochemical / cellular potency by agent
Canonical first-disclosure and characterization values (assay conditions vary —
biochemical Ki/IC50 on recombinant PRC2 vs cellular H3K27me3 EC50 are not directly
comparable):

- **Tazemetostat / EPZ-6438** (Knutson 2014, *Mol Cancer Ther*, in corpus): EZH2
  **Ki ≈ 2.5 nM**, ~**35-fold** selective over EZH1 and >100–4,500× over a panel
  of other HMTs; cellular H3K27me3 EC50 low-nM; oral, potent regression of
  EZH2-mutant NHL xenografts.
- **GSK126 / GSK2816126** (McCabe 2012, *Nature*): EZH2 **Ki ≈ 0.5–3 nM**,
  ~**150-fold** vs EZH1, >1,000× vs other methyltransferases; SAM-competitive.
  Clinically limited by poor solubility/exposure (trial terminated).
- **GSK343** (cellular EC50 ~ nM; tool), **GSK503**, **GSK926** — GSK tool series
  used widely in mechanism papers.
- **EPZ005687** (Knutson 2012, *Nat Chem Biol* — the field's first potent selective
  EZH2i): **Ki ≈ 24 nM**, ~50× vs EZH1, >500× other HMTs; selectively lowers
  H3K27me3 in Y641/A677 mutant lymphoma cells.
- **EI1** (Qi 2012, Novartis): EZH2 IC50 ~**15 nM**, SAM-competitive; early tool.
- **EPZ011989** (Campbell 2015): orally bioavailable EZH2i with **measurable brain
  exposure in mice** and antitumor activity — an early demonstration that the
  chemotype can be tuned for CNS (see `02_bbb_penetration.md`).
- **UNC1999** (Konze 2013): **dual EZH2/EZH1**, IC50 <**10 nM** (EZH2), ~**45 nM**
  (EZH1); first orally bioavailable dual probe; paired with inactive control
  **UNC2400**.
- **Valemetostat / DS-3201** (Honma 2017): **dual EZH1/2**, low-nM against both
  enzymes; dual inhibition gives deeper H3K27me3 suppression where EZH1
  compensates — mechanistic basis for activity in ATL/PTCL and interest in
  stem-like/CNS contexts.
- **Tulmimetostat / CPI-0209** (2nd-gen, from the **CPI-1205** series; Kung 2016
  described CPI-1205): designed for **prolonged target residence time**, low-nM
  potency, broader activity than first-gen in preclinical models.
- **Mevrometostat / PF-06821497** (Pfizer): potent selective EZH2i with improved
  drug-like PK; advanced to Phase 3 in mCRPC (with enzalutamide).
- **SHR2554** (Hengrui): potent selective oral EZH2i; low-nM class potency; Chinese
  Phase 1/2 in lymphoma.
- **EED226 / A-395 / MAK683** (allosteric EED): low-nM cellular potency; retain
  activity against EZH2 SET-domain mutant, EZH2i-resistant cells.
- **DZNep** (3-deazaneplanocin A): **not a direct EZH2 inhibitor** — an
  S-adenosylhomocysteine hydrolase inhibitor that indirectly depletes PRC2
  proteins; potent but **non-selective and cytotoxic**, so used mechanistically,
  not as a drug candidate.

## Selectivity axes that actually matter
1. **EZH2-selective vs dual EZH1/2.** EZH1 can partially compensate for EZH2
   inhibition (residual H3K27me3, especially in quiescent/stem-like cells). Dual
   inhibitors (**valemetostat, UNC1999**) achieve deeper, more durable H3K27me3
   loss — relevant where EZH1 is expressed, including some neural/CNS contexts.
2. **Catalytic-site vs EED-allosteric.** EED inhibitors (**EED226, MAK683**) bind a
   different pocket and **retain potency against acquired EZH2 SET-domain
   mutations** that confer resistance to SAM-competitive drugs (see
   `04_...resistance`).
3. **Off-target/DDI.** Tazemetostat is a **CYP3A** substrate (dose adjustment with
   strong 3A modulators) and clinically carries a **secondary-malignancy (T-LBL/MDS)**
   boxed concern in children — both are exposure/selectivity considerations beyond
   raw enzyme potency.

**Bottom line on potency:** potency is not the differentiator — all modern agents
are low-nanomolar and clean against non-PRC2 methyltransferases. The decisions are
**EZH2 vs EZH1/2 dual**, **catalytic vs allosteric**, and **PK/BBB** (next note).
