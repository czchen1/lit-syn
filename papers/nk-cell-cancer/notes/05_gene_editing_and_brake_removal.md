# Gene editing: removing the brakes

Adding a receptor gives specificity; deleting a brake gives fitness. The 2020–2026 literature has converged on
a fairly short, well-replicated edit list, and unbiased screens are now expanding it.

## The cytokine-signalling brake: CISH

- **Zhu et al. (2020, PMID 32531207)** deleted *CISH* in iPSC-NK cells: increased IL-15-driven JAK/STAT
  signalling, better expansion, greater cytotoxicity at low cytokine concentrations and improved in vivo
  persistence — i.e. the edit reduces the product's dependence on exogenous IL-15.
- **Daher et al. (2021, PMID 32902645)** combined *CISH* knockout with IL-15-armoured ("fourth-generation")
  CAR engineering of cord-blood NK cells, boosting effector function through the Akt/mTORC1 axis.
- A conditional *Cish*-deficient mouse model confirmed enhanced natural-cytotoxicity-receptor signalling and
  reduced NK exhaustion in solid tumours (PMID 35589278).

## The HLA-E brake: NKG2A / KLRC1

- Anti-NKG2A antibody (monalizumab) unleashes both NK and CD8 T cells (André 2018, PMID 30503213), and NKG2A
  is a therapeutic vulnerability in MHC-I-heterogeneous triple-negative breast cancer (PMID 37791898).
- Genetic deletion is more attractive for a cell product: *KLRC1* knockout improves NK activity against solid
  tumours (PMID 37675109); CRISPR editing of NKG2A improves primary **CD33-CAR NK** efficacy against AML
  (PMID 39349459); NKG2A knockout enhances cytotoxicity against myeloma (PMID 35694192).
- Tumours actively exploit this axis — HLA-E:NKG2A mediates escape of circulating tumour cells from NK
  surveillance (PMID 36706761).

## The TGF-β / activin brake

- TGF-β represses mTOR in NK cells (PMID 26884601), drives metabolic dysfunction in human metastatic breast
  cancer (PMID 33568351), drives NK→ILC1 conversion (PMID 28759001) and acts through SMAD3 to suppress NK
  development via E4BP4/NFIL3 (PMID 28262747).
- Edits: **SMAD4 knockout** makes human NK cells resistant to both TGF-β and activin A while retaining
  cytotoxicity and IL-2/IL-15-driven proliferation, with better tumour penetration (PMID 40119192);
  TGF-β-pathway disruption is *required* for iPSC-NK efficacy against hepatocellular carcinoma
  (PMID 38986609); dominant-negative TGFBR2 and αv-integrin/TGF-β axis targeting improve activity against
  glioblastoma stem cells (PMID 34138753).

## Fratricide and antibody-combination edits

- **CD38 knockout** removes daratumumab-induced fratricide and boosts effector activity (PMID 32603414),
  enables CD38-CAR NK cells (PMID 33375774), and its locus can host a high-affinity CD16 knock-in
  (PMID 35135865).
- **ADAM17 knockout** prevents CD16 shedding (PMID 31704085).
- **HLA class I knockout** makes allogeneic primary NK cells universal donors (PMID 33584651).

## Newer intracellular targets

- **Regnase-1 / ZC3H12A** deletion increases IFN-γ via OCT2-dependent transcription and intratumoral
  accumulation (PMID 38821052).
- **Cbl-b** inactivation licenses NK cells to reject metastases, with TAM receptors as the upstream axis
  (Paolino 2014, PMID 24553136).
- **TIPE2** deletion improves adoptively transferred NK cells against solid tumours (PMID 36725083).
- **TIM-3** knockout enhances activity against glioma (PMID 33800561); TIM-3 ligand context determines whether
  this helps (PMID 39773563).
- **PD-1 (PDCD1)** knockout is feasible in primary NK cells (PMID 31704085); TIGIT blockade prevents NK
  exhaustion (Zhang 2018, PMID 29915296).

## Unbiased screens are now the source of new targets

- **Genome-wide CRISPR screens in primary human NK cells** identified MED12, ARIH2 and other checkpoints whose
  ablation increases CAR-NK potency under immunosuppressive pressure (PMID 40845844).
- **In vivo AAV-SB-CRISPR screens of tumour-infiltrating NK cells** across four solid-tumour models identified
  genetic checkpoints of CAR-NK therapy alongside single-cell characterisation of TINK subpopulations
  (PMID 38918616).
- **Two-cell-type screens** shift the question to the target cell: *CHMP2A* loss in glioblastoma stem cells
  and HNSCC increases sensitivity to NK killing (PMID 35393416) — a druggable-sensitiser axis rather than an
  effector edit.
- Epigenetic regulators recur: EZH2 in NK differentiation (PMID 26668377), BATF in AML-driven NK dysfunction
  (PMID 39259809), DNMT1 inhibition improving CIML NK activity via autophagy (PMID 39704855), m6A methylation
  downstream of mTOR (PMID 38640466).

## Editing platform and safety

- Cas9 RNP electroporation is the workhorse: up to ~90% editing of primary peripheral-blood NK cells
  (PMID 31704085), integrated with feeder-free expansion of cryopreserved NK cells (PMID 33433623), and
  applied to NK-92 (PMID 32528479).
- Feeder-based activation improves both expansion and editability (PMID 35222382).
- Multiplex editing raises translocation, off-target and clonality questions; **safety-assessment platforms for
  CRISPR-modified NK cells** are being formalised (PMID 41425600), and this — not editing efficiency — is now
  the rate-limiting step for products carrying 3+ edits.

## Consensus edit stack for a solid-tumour product

1. *CISH* (cytokine-signalling brake) — persistence and IL-15 independence.
2. *KLRC1*/NKG2A — resist HLA-E-mediated inhibition.
3. TGF-β resistance (*SMAD4* knockout or dnTGFBR2) — resist TME reprogramming.
4. *ADAM17* knockout or hnCD16 knock-in — preserve ADCC.
5. Target-antigen knockout when the antigen is shared with NK cells (e.g. CD38).
6. Optional/emerging: Regnase-1, TIPE2, Cbl-b, MED12/ARIH2 from screens.
