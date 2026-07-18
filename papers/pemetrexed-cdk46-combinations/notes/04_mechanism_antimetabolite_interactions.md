# CDK4/6 inhibitor × antimetabolite interactions — mechanism and scheduling

Pemetrexed is an antifolate antimetabolite, so the broader preclinical literature on how CDK4/6 inhibition interacts with antimetabolites (5-FU, capecitabine, cytarabine, gemcitabine, methotrexate, and nucleoside/folate analogues) is the mechanistic foundation for designing — or avoiding — a pemetrexed + CDK4/6i regimen. Two opposing forces dominate, and their balance is set by **schedule**.

## Force 1 — Synergy: dNTP depletion and complementary arrest

- **Castellví et al. 2020 — SAMHD1 activation (PMID 32197329).** The most mechanistically important paper for antifolates. SAMHD1 is a dNTP triphosphohydrolase whose activity is switched off by cell-cycle CDK phosphorylation. CDK4/6 inhibitors **pharmacologically activate SAMHD1** by preventing that phosphorylation; active SAMHD1 drains the dNTP pool. Combining a CDK4/6i with **nucleoside *or* folate antimetabolites** was **highly synergistic (CI < 0.04)**. This gives pemetrexed (an antifolate) a positive, dNTP-based rationale for combination that does not require simultaneous S-phase occupancy, and SAMHD1 expression is proposed as a predictive biomarker.
- **Lin et al. 2020 — ribociclib + 5-FU, colorectal (PMID 33109564):** synergistic viability reduction with G1 arrest and reduced pRB/p53 — antimetabolite + CDK4/6i synergy in a GI model.
- **Yang et al. 2015 — palbociclib sensitizes AML to cytarabine (PMID 25744718):** CDK4/6 inhibition primes leukemic cells for a nucleoside analogue.
- **Gelbert et al. 2014 — abemaciclib (LY2835219) + gemcitabine (PMID 24919854):** foundational abemaciclib characterization; combination enhanced in-vivo antitumor activity, associated with **reduced ribonucleotide reductase** (i.e., a nucleotide-metabolism effect) rather than simple additive G1 arrest.
- **CDK4/6i potentiates chemotherapy via p73/DR5** (PMID 36721000, 35149588) and cooperates with cytotoxics in biliary tract (PMID 34407567) and medulloblastoma (ribociclib + gemcitabine, PMID 35709750) models.

## Force 2 — Antagonism: G1 arrest shields cells from S-phase drugs

- **Kumarasamy et al. 2020 — the definitive scheduling paper (PMID 31745297).** In pancreatic models, the interaction between CDK4/6i and chemotherapy is **mechanism- and schedule-specific**: concurrent **gemcitabine largely ablates CDK4/6i function in S-phase-arrested cells**, but cells recovering from S-phase block regain CDK4/6i sensitivity; by contrast, docetaxel + CDK4/6i is cooperative and blocks adaptive cell-cycle re-entry. Direct evidence that a continuous CDK4/6i given with an S-phase antimetabolite can be mutually blunting.
- **Chemotherapy impacts on CDK4/6i response** and cell-cycle-dependent drug sensitivity screens (PMID 34049239) reinforce that where a cell sits in the cycle when each drug arrives determines outcome.
- **Sequential Rb/DNA-synthesis targeting** in sarcoma (PMID 36603130) — an explicit demonstration that ordering matters when combining RB-pathway and DNA-synthesis-pathway drugs.

## Antifolate-resistance and CDK context
- **Georgiou et al. 2022 — ATR + CDK4/6 inhibition in methotrexate-resistant choriocarcinoma (PMID 35301407):** CDK4/6i (with ATR inhibition) targets antifolate (MTX)-resistant tumor growth — relevant to overcoming antifolate resistance, a mechanism shared with pemetrexed.
- **Vo et al. 2017 (PMID 28566433):** mTORC1 inhibition induces methotrexate resistance in B-ALL — a caution that upstream signaling context modulates antifolate sensitivity in combinations.

## Clinical sequencing analogue (breast capecitabine data)
Although breast-specific, the head-to-head/sequencing trials of the antimetabolite **capecitabine** vs./after CDK4/6i inform the same question of how antimetabolites and CDK4/6i are best ordered clinically:
- Palbociclib + endocrine therapy vs. capecitabine (PEARL and related, PMID 33385521, 31668850, 39978378, 40632974) and capecitabine efficacy **after** CDK4/6i progression (PMID 37390791) — collectively show antimetabolite chemotherapy retains activity after CDK4/6i and that these classes are typically used **sequentially** rather than concurrently in practice.

## Design implications for pemetrexed + CDK4/6i

1. **There is a genuine biochemical synergy rationale** (SAMHD1-mediated dNTP depletion potentiating an antifolate) — pemetrexed + CDK4/6i is not merely additive cell-cycle blockade.
2. **Naive concurrent dosing of a continuous CDK4/6i with pemetrexed risks antagonism** by removing tumor cells from the S phase where pemetrexed kills.
3. **Favorable schedules** are chemo-first / pemetrexed-then-CDK4/6i, or transient/pulsed CDK4/6i (the trilaciclib paradigm), preserving the antimetabolite's S-phase window.
4. **Candidate biomarkers:** RB proficiency (required for CDK4/6i activity), CDKN2A/p16 loss (dependence), and SAMHD1 expression (predicts antimetabolite potentiation).
