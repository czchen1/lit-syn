# The scientific advances that change a design decision — and the ones that don't yet

Criterion for inclusion: **does this change a choice you would make when designing a product?** Papers that
describe biology without a design consequence are in `REPORT.md`, not here.

## Tier 1 — change the decision, with clinical support

### 1. Cell-intrinsic IL-15 (the highest-value single module)

IL-15 armouring converts a transient infusion into a product with measurable persistence. Secreted IL-15 +
CD19 CAR in cord-blood NK cells (Liu 2018, PMID 28725044) became the clinical CAR19/IL-15 product
(PMID 32023374; 37 patients with response determinants, PMID 38238616); an IL-15/IL-15Rα **fusion** is a core
module of iPSC-derived FT596 (PMID 39798981); soluble IL-15 defines cord-blood TRACK NK now in NSCLC
(PMID 38572955, PMID 39903538).

**Design consequence:** the cytokine goes *in the product*, not in the patient. Tether it, fuse it or make it
inducible (rimiducid-controlled MyD88/CD40 + IL-15, PMID 32384544) — the GvHD signal seen with IL-15/4-1BBL-
activated NK cells after T-depleted HSCT (PMID 25452614) is the reason not to leave IL-15 unregulated.

### 2. Cytokine-induced memory-like programming (IL-12 + IL-15 + IL-18)

Romee 2012 (PMID 22983442) showed a 12–16 h preactivation produces weeks-long enhanced responsiveness;
Romee 2016 (PMID 27655849) showed remissions in r/r AML; Berrien-Elliott 2022 (PMID 35349491) characterised
expansion and persistence for post-transplant relapse. The state is **epigenetically encoded**, not a transient
activation (PMID 38941480), which is why it survives manufacturing and infusion.

**Design consequence:** append it as the terminal step of any process. It costs one day, requires no genetic
modification, and stacks with engagers (PMID 33986022), CARs (PMID 38996027), particle expansion
(PMID 38711506) and checkpoint blockade (PMID 39948608).

### 3. Protected, high-affinity CD16

CD16A is shed by ADAM17 on activation — a negative-feedback loop that directly limits **serial killing**
(PMID 41116262) and blunts engager and antibody combinations. Fixes: high-affinity non-cleavable CD16a in
iPSC-NK (PMID 31856277, used in FT596), CD16-158V knocked into the *CD38* locus so one edit both deletes CD38
and installs better CD16 (PMID 35135865), ADAM17 knockout (PMID 31704085), or pharmacological ADAM17 blockade
which also enhances IL-15-driven activation and proliferation (PMID 39053944). The FcγRIIIA L48-H/R
polymorphism enhancing ADCC via serial killing (PMID 39666369) tells you which variant to install.

### 4. IL-15-containing engagers (specificity without gene transfer)

The BiKE → TriKE progression is the field's most underrated result: CD16×CD33 BiKE established redirection
(PMID 24652987), and adding IL-15 to make the 161533 TriKE added **expansion, persistence and survival**
(PMID 26847056) — one reagent supplying both specificity and the Tier-1 lever above. Extended to CD19 in CLL
(PMID 30890546), CLEC12A for AML stem cells (PMID 33097838), and NKp30×HER2 to bypass CD16 entirely
(PMID 40694640). Trifunctional NKp46×CD16a×CD123 NKCE controlled AML *and* overcame CD64-mediated resistance
to anti-CD123 ADCC (PMID 36635380).

AFM13 (CD30×CD16A) pre-complexed with cytokine-activated cord-blood NK cells gave "CAR-like" activity without
gene transfer (PMID 33986022) and produced clinical responses in lymphoma refractory to both brentuximab and
checkpoint inhibitors (PMID 40186077).

**Design consequence:** an engager moves specificity risk out of the cell product entirely — cheaper and
retargetable — at the cost of depending on CD16 and on repeat dosing of a second agent.

### 5. Host conditioning is part of the product's efficacy

Miller 2005 (PMID 15632206) established that in vivo expansion requires lymphodepletion; Bachanova 2014
(PMID 24719405) showed IL-2-diphtheria-toxin Treg depletion raised the expansion rate from 10% to 27% of
patients with better AML clearance. Donor selection is the other free lever: KIR B-haplotype donors improve
survival after unrelated transplant for AML (PMID 20581313) and the HLA-B −21 M/T dimorphism shapes NK education
and immunotherapy outcome (PMID 30647027).

## Tier 2 — change the decision on preclinical strength, clinical readout pending

### 6. NK-native CAR architecture

Li 2018 (PMID 30082067) screened CARs in iPSC-NK cells: **NKG2D transmembrane + 2B4 + CD3ζ** outperformed the
CD28-CD3ζ CAR-T design ported into NK cells. DAP10/DAP12-based receptors exploit native adaptors, and a
KIRS2/DAP12 CAR reached the clinic in r/r B-ALL (PMID 34703879). But the design rule is *screen, don't assume*:
CD28 — which mature NK cells do not express — augments a CD70-CAR via LCK/CD3ζ/ZAP70 (PMID 38900051), and
knocking a ζ-less CAR into the endogenous *CD3ζ* locus gives potent cytotoxicity (PMID 38493479).

### 7. Brake knockouts

Ranked by evidence and by what each protects against. Which subset is worth taking depends on the edit-count
decision in `04_design_decisions.md`, not on biology alone:

| Edit | Protects against | Key evidence |
|---|---|---|
| *CISH* | cytokine-signalling brake; IL-15 dependence | PMID 32531207; with IL-15-armoured CAR PMID 32902645; in vivo model PMID 35589278 |
| *KLRC1*/NKG2A | HLA-E-mediated inhibition, incl. CTC escape | PMID 39349459, PMID 37675109, PMID 35694192, PMID 36706761 |
| *SMAD4* / dnTGFBR2 | TGF-β + activin A reprogramming, NK→ILC1 conversion | PMID 40119192, PMID 38986609, PMID 34138753, PMID 28759001 |
| *CD38* (when using daratumumab or a CD38 CAR) | fratricide | PMID 32603414, PMID 33375774 |
| *ADAM17* | CD16 shedding | PMID 31704085 |
| *ZC3H12A* (Regnase-1), *TIPE2*, *Cbl-b* | intracellular restraint on IFN-γ / accumulation | PMID 38821052, PMID 36725083, PMID 24553136 |
| HLA class I | host T-cell rejection of allogeneic NK | PMID 33584651 |

Unbiased screens are now the target pipeline: genome-wide CRISPR screens in primary human NK cells found
MED12/ARIH2-class checkpoints whose ablation increases CAR-NK potency under immunosuppression (PMID 40845844),
and in vivo AAV-SB screens of tumour-infiltrating NK cells across four solid-tumour models found genetic
checkpoints of CAR-NK therapy (PMID 38918616). A different lever from the same technique: *CHMP2A* loss in
glioblastoma stem cells and HNSCC makes the **target** NK-sensitive (PMID 35393416).

### 8. Metabolic fitness as a designed attribute

The most consequential mechanistic result for product design: single-cell profiling of CAR-NK cells after
transfer showed relapse was driven by **loss of metabolic fitness, reversible by cytokine engineering**
(PMID 37494448). The supporting map: amino-acid-dependent cMyc as the checkpoint (PMID 29904050), TGF-β
repression of mTOR (PMID 26884601) and metabolic dysfunction in human metastatic breast cancer
(PMID 33568351), hypoxia via HIF-1α (PMID 32445619) and SHP-1/STAT3/ERK (PMID 33123602), obesity/PPAR-driven
lipid paralysis (PMID 30420624), lactate-driven lysine **lactylation** that can be targeted to restore killing
(PMID 40494934), vitamin B6 restriction by pancreatic cancer (PMID 37931287), myCAF-driven glutamine
deprivation (PMID 39696364), and mitochondrial apoptotic priming setting killing efficiency at physiological E:T
ratios (PMID 35447071).

**Design consequence:** treat metabolic fitness as a **release attribute** and a design target, not a research
topic (see `05_potency_and_release.md`).

## Tier 3 — real advances that do not yet change a design decision

- **High-dimensional phenotype maps.** scRNA-seq/CITE-seq resolution of human NK states (PMID 38956378),
  pan-cancer tumour-infiltrating NK maps (PMID 38956379, PMID 37607536) and tissue imprinting (PMID 32059780)
  prove CD56bright/dim is inadequate — but no map yet names a state you can select for and manufacture at
  scale. Their present use is **product characterisation**, and that is genuinely valuable: it is how you show
  your process makes the same cell twice.
- **Adaptive/NKG2C+ NK cells.** Associated with reduced leukaemia relapse (PMID 26416461) and now buildable
  into iPSC-NK products (PMID 34525347) — but it depends on CMV serostatus for primary products, so it is a
  donor-selection footnote until the engineered version has clinical data.
- **Synthetic-biology logic.** synNotch conversion of TIGIT/CD73 into activating signals (PMID 38429294) and
  KIR-based inhibitory CARs (PMID 36175679) are excellent science; the iCAR is worth its complexity mainly
  where trogocytosis is demonstrated (see `03_failure_modes.md`).
- **Checkpoint blockade of NK cells.** Monalizumab/anti-NKG2A unleashes NK and T cells (PMID 30503213) and
  TIGIT blockade prevents exhaustion (PMID 29915296) — but for a cell product, deleting the receptor beats
  co-administering an antibody.
- **Pharmacological sensitisation of the tumour.** Bortezomib lowering HLA-E and raising DR5 (PMID 30713790),
  BET inhibition via BRD4/SMAD3 (PMID 38519469), STING agonists with CAR-NK (PMID 35371622), radiotherapy via
  CXCL8 (PMID 35319989). These are combination-regimen decisions, not product decisions — but they are the
  cheapest way to improve a fixed product.
- **NK→DC→T-cell axis.** NK recruitment of cDC1 (PMID 29429633) and the NK–DC axis in checkpoint-responsive
  tumours (PMID 29942093) argue for positioning NK products *with* T-cell therapy rather than against it — a
  clinical-development choice.
