# Overview — Pemetrexed + CDK4/6 inhibitor combinations

## The central paradox: G1 arrest vs. S-phase cytotoxicity

Pemetrexed is a multitargeted antifolate that inhibits thymidylate synthase (TS), dihydrofolate reductase, and GARFT, depleting the dTTP/purine pools needed for DNA replication. Its cytotoxicity is **S-phase dependent** — cells must be cycling through DNA synthesis for the drug to kill them. CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) do the opposite: they block CDK4/6-mediated phosphorylation of RB, holding RB-proficient cells in **G1 arrest** before they ever enter S phase.

This creates a fundamental, schedule-dependent tension that runs through the entire collection:

- **Antagonism risk:** A cell arrested in G1 by a CDK4/6i is *not* in S phase and is therefore partially shielded from an S-phase-dependent antimetabolite given at the same time. Kumarasamy et al. 2020 (PMID 31745297) show this directly — concurrent gemcitabine "largely ablates the function of CDK4/6 inhibition in S-phase arrested cells," and the interaction depends entirely on the chemotherapy's mechanism and the schedule.
- **Synergy opportunity:** When the two agents hit complementary compartments (pemetrexed killing S-phase cells while the CDK4/6i arrests the escapees in G1 and lowers the apoptotic threshold), the net effect is additive-to-synergistic. Ke et al. 2022 (PMID 35686110) show exactly this for ribociclib + pemetrexed in lung adenocarcinoma — "pemetrexed blocked cells in the S phase, whereas ribociclib arrested cells in the G1 phase," and the combination enhanced apoptosis via caspase/Bcl-2 signaling.
- **A biochemical rationale beyond cell-cycle position:** Castellví et al. 2020 (PMID 32197329) show CDK4/6 inhibitors are pharmacological **activators of SAMHD1** (they block its inactivating phosphorylation). Active SAMHD1 depletes dNTPs — an effect that can *potentiate* both nucleoside analogues and **antifolate drugs**, producing highly synergistic combinations (CI < 0.04). This provides a positive mechanistic basis for pairing CDK4/6i with pemetrexed that does not depend on simultaneous S-phase occupancy.

The practical corollary, repeated across preclinical papers, is that **sequencing and schedule matter more than for most combinations**: chemotherapy-then-CDK4/6i (or transient/pulsed CDK4/6i) tends to preserve or enhance activity, whereas naive concurrent dosing of a continuous CDK4/6i with an S-phase antimetabolite risks mutual blunting.

## Collection taxonomy

| Category | n | Core content |
|---|---|---|
| **trilaciclib_myeloprotection** | 63 | Trilaciclib given transiently before chemotherapy to protect HSPCs/immune cells (SCLC, TNBC, CRC, solid tumors) |
| **cdk46_antimetabolite_mechanism** | 21 | Preclinical CDK4/6i × antimetabolite interaction biology (5-FU, cytarabine, gemcitabine, MTX, SAMHD1, sequencing) |
| **cdk46_chemo_lung_meso** | 20 | CDK4/6i + chemotherapy in NSCLC and pleural mesothelioma (pemetrexed disease contexts) |
| **pemetrexed_cdk46_direct** | 4 | Studies directly combining pemetrexed with a CDK4/6 inhibitor |

108 papers, 2012–2026 (86 from 2020 onward; 21 clinical trials / randomized studies; 53 with open-access full text).

## What the evidence actually supports (top-line)

1. **Direct pemetrexed + CDK4/6i clinical data are limited to early-phase work.** The only dedicated clinical combination is Kim et al. 2018 (PMID 30082474), a Phase Ib in metastatic NSCLC: abemaciclib + pemetrexed had no MTD reached and a disease-control rate of 57%, establishing feasibility but not efficacy. Abemaciclib brain-metastasis trials (Sahebjam et al. 2026, PMID 41768125) allowed concurrent pemetrexed but were not designed to isolate a combination effect and showed no confirmed intracranial responses.
2. **Preclinical pemetrexed + CDK4/6i is consistently synergistic** in lung adenocarcinoma (Ke 2022, ribociclib) and pleural mesothelioma (Terenziani 2022, abemaciclib + cisplatin/pemetrexed; PMID 36497412), the latter aligning with the positive abemaciclib MiST2 mesothelioma signal.
3. **Mesothelioma is the most promising disease context** — CDKN2A/p16 loss (≈70% of pleural mesothelioma) is a strong biomarker of CDK4/6 dependence, and pemetrexed/cisplatin is the chemotherapy backbone, making the combination biologically rational.
4. **Trilaciclib reframes "CDK4/6i + chemo"** as a supportive-care strategy: transient CDK4/6 inhibition before cytotoxic chemotherapy protects marrow and immune function without compromising (and sometimes enhancing, via immune activation) antitumor efficacy — approved in ES-SCLC and studied with gemcitabine/carboplatin and other regimens.
5. **The dominant translational message is schedule dependence** — the same two drugs can antagonize or synergize depending on order and continuity of dosing.

## How to read this collection

- Start with `01_direct_pemetrexed_cdk46.md` for the papers that answer the literal question.
- `02_cdk46_chemo_nsclc_mesothelioma.md` covers the disease settings where a pemetrexed combination is most plausible.
- `03_trilaciclib_myeloprotection.md` covers the myeloprotective use of a CDK4/6i alongside chemotherapy.
- `04_mechanism_antimetabolite_interactions.md` explains the synergy/antagonism biology that should guide any pemetrexed + CDK4/6i design.
