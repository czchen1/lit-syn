# Logic gates, switchable, and bispecific GD2 CARs

A growing subset of papers in this collection (mostly 2020–2026) re-engineers the GD2 CAR signaling architecture to gain spatial selectivity, off-switches, or multi-antigen coverage.

## 1. AND-gates: synNotch

- **Moghimi 2021** (J Clin Invest / Nat Commun, cited in `index.tsv`) and related synNotch papers in the collection describe a two-receptor system:
  - **Sensor**: anti-B7-H3 synNotch receptor releases a transcription factor (e.g., tTA, Gal4-VP16) upon binding B7-H3 on tumor cells.
  - **Effector**: the released TF drives transcription of a 14g2a-CD8-4-1BB-CD3ζ GD2 CAR.
- Cells therefore express the GD2 CAR only after encountering B7-H3+ tumor, sparing B7-H3− healthy GD2+ tissues (peripheral nerves, dorsal root ganglia, normal cerebellum).
- Limitations noted in papers: (a) leaky basal CAR expression, (b) loss of synNotch signal after sustained exposure, (c) need to maintain the inducible CAR transgene below tonic-signaling thresholds.

## 2. OR-gates and bispecific (tandem) CARs

- Bispecific CARs are constructs where a single polypeptide carries two scFvs in tandem (or a single scFv plus a second binder), each able to drive activation. Papers in the collection target combinations such as:
  - GD2 + B7-H3
  - GD2 + L1CAM
  - GD2 + EGFR variants (in glioma)
  - GD2 + HER2
- The motivation is to cover antigen escape: GD2-loss variants are common after CAR-T pressure (Heczey 2020/2023; Majzner 2022). Bispecific CARs can also reach lower-density antigen by avidity effects.

## 3. NOT-gates (inhibitory CARs)

- Less common in the GD2 field but represented by a handful of preclinical papers using CD22-, MHC-I-, or HLA-DR-specific inhibitory CARs to spare healthy tissues. The inhibitory CAR uses an scFv against a healthy-tissue antigen fused to an inhibitory cytoplasmic tail (e.g., PD-1 or TIGIT ITIMs).

## 4. SUPRA / split universal CARs

- A subset of 2022–2026 papers tests SUPRA architectures: T cells express a "zipCAR" (leucine-zipper extracellular + signaling cytoplasmic), and a soluble "zipFv" — anti-GD2 scFv fused to the cognate leucine zipper — is delivered separately as a drug. Switching adapters tunes specificity; withholding the adapter is an OFF switch.
- DARPin-based universal CARs use DARPin-tagged scFvs against GD2 with a anti-DARPin-tag CAR T cell.

## 5. Antigen-density-gated and tuned CARs

- 2024–2026 papers tune GD2 CAR signaling thresholds via:
  - Hinge length: longer hinges (IgG1 CH2CH3) lower trigger threshold; shorter (CD8α) raise it.
  - ITAM number: full 3-ITAM CD3ζ vs ITAM1-only.
  - Costimulation strength: 4-1BB vs CD28 vs costimulation-only.
- Goal: drive activation only when GD2 surface density exceeds an empirically chosen threshold matching tumor expression but exceeding peripheral-nerve expression.

## 6. Chemokine-armored gated activation

- A handful of 2024–2026 papers combine GD2 CARs with hypoxia-responsive promoters (HIF-binding sites in the CAR promoter) to restrict activation to hypoxic tumor cores.

## 7. Trans-signaling and modular receptors

- **Vogt 2025** and related — hypoxia-actuated GD2 CARs designed to express CAR only in tumor hypoxic niches.
- **Foster 2025** — TRAC knock-in GD2 CAR with additional logic modules for spatial control.

## 8. Bispecific CAR examples documented in the collection

| Paper | Combination | Format | Notes |
| --- | --- | --- | --- |
| Synthetic biology subset 2024–2026 | GD2 + B7-H3 | tandem scFv-CAR | Reduces escape via single-antigen loss |
| Synthetic biology subset 2024–2026 | GD2 + L1CAM | dual-CAR (two independent cassettes) | L1CAM compensates GD2 loss; co-expression often via 2A peptide |
| Synthetic biology subset 2024–2026 | GD2 + EGFR | tandem scFv-CAR | For HGG / DIPG indications |

## 9. Combination with bispecific T-cell engagers (BiTEs)

- Some 2024–2026 GD2 CAR papers in collection co-express a secreted BiTE (e.g., EGFRvIII × CD3 or B7-H3 × CD3) to recruit bystander T cells without re-engineering them. Acts as a paracrine amplification of CAR activity.

## 10. Practical lessons from the logic-gate literature

- Leaky basal CAR expression remains the dominant failure mode of synNotch and SUPRA designs.
- Tonic 14g2a clustering (Long 2015 PMID 25939063) makes 14g2a a particularly hard scFv to put in a "must-be-quiet" inducible system; some logic-gate papers switch to less-aggregating scFvs (humanized 14.18 or 3F8 with engineered framework).
- Bispecific tandem CARs gain dual-antigen coverage but may sacrifice antigen sensitivity to either one alone; affinity-tuning per arm is necessary.
