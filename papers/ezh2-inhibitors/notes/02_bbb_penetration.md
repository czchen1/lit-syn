# Blood-brain-barrier (BBB) penetration & CNS exposure

This is the decisive property for brain-tumor use (DMG/DIPG, H3G34, ATRT/rhabdoid,
medulloblastoma, glioblastoma) and the weakest, least-reported axis across the
class. Two failure modes dominate: **active efflux at the BBB (P-gp/ABCB1 and
BCRP/ABCG2)** and generally **modest passive permeability / high protein binding**,
so that *total* brain levels overstate the pharmacologically relevant **free**
(unbound) brain concentration (Kp,uu).

## Per-agent CNS profile

- **Tazemetostat (EPZ-6438) — poor and variable CNS penetration.** Repeatedly
  described as a **substrate of P-glycoprotein (ABCB1) and BCRP (ABCG2)**, which
  actively pump it out of brain, giving low brain-to-plasma ratios and sub-target
  free-brain exposure at tolerated systemic doses. This is the mechanistic reason
  single-agent CNS activity in pediatric brain tumors (ATRT, INI1-negative tumors)
  has been **modest despite clear extracranial efficacy**, and it motivated
  explicit medicinal-chemistry programs to build brain-penetrant analogs (see the
  in-corpus 2021 "**A chemical strategy toward novel brain-penetrant EZH2
  inhibitors**"). Practical implication: expect efflux-limited CNS delivery unless
  combined with efflux considerations, higher local exposure, or a different
  chemotype.

- **EPZ011989 — early proof that the chemotype can be made brain-exposed.**
  Campbell 2015 reported an orally bioavailable EZH2i with **measurable brain
  exposure in mice** and antitumor activity — an existence proof that CNS
  penetration is achievable within the SAM-competitive series, though it was not
  advanced clinically.

- **Valemetostat (DS-3201) — reported to be more brain-penetrant.** Its dual
  EZH1/2 mechanism plus a PK profile described as more CNS-favorable make it the
  clinical-stage agent most often cited for CNS-adjacent potential; it has CNS
  disease exposure in ATL (which involves CNS relapse). Public **quantitative
  free-brain PK (Kp,uu) in humans remains sparse**, so treat "brain-penetrant" as
  directional, not established for brain tumors.

- **Mevrometostat (PF-06821497) / tulmimetostat (CPI-0209) / SHR2554.** Designed
  for improved drug-like PK and (mevrometostat, CPI-0209) longer target residence,
  but their development is in **extracranial** disease (mCRPC, solid tumors,
  lymphoma); **CNS penetration data are limited/not the development focus.**

- **GSK126 (GSK2816126).** Not CNS-optimized; its clinical program was limited by
  poor solubility/exposure generally (trial terminated), so it is not a CNS
  candidate. GSK343/GSK503 are tool compounds.

- **UNC1999 (dual EZH1/2).** Orally bioavailable tool; used in CNS mechanism studies
  but not characterized as a validated brain-penetrant drug.

- **EED inhibitors (EED226, MAK683, A-395).** Attractive because they bypass
  SAM-site resistance and, as a distinct chemotype, offer a fresh scaffold to
  engineer BBB penetration — but again, brain PK is not well documented publicly.

- **DZNep (3-deazaneplanocin A).** Historically noted to cross the BBB, but it is a
  **non-selective, cytotoxic SAH-hydrolase inhibitor**, unsuitable as a targeted
  CNS drug; useful only as a mechanistic depletor of PRC2.

## What the CNS/brain-tumor papers in this corpus actually show
CNS activity in the literature is mostly **preclinical and combination-driven**,
consistent with exposure being limiting for single agents:
- **DIPG/H3K27M:** EZH2i (EPZ-6438) synergizes with **HDAC inhibition** and with
  **ONC201/imipridones** (DR5/integrated stress response; Zhang 2021, and an
  imipridone×EZH1/2/HDAC synergy paper in-corpus) rather than curing as monotherapy.
- **ATRT/rhabdoid (SMARCB1/INI1-loss):** the strongest synthetic-lethal rationale;
  tazemetostat is active in models and pediatric rhabdoid tumors (Vejmelkova 2023),
  but CNS delivery caveats persist.
- **Group 3 medulloblastoma:** EZH2 inhibition downregulates **B7-H3** in
  MYC-driven tumors (2023, in-corpus) — an immuno-epigenetic combination angle.
- **Glioblastoma:** EZH2 inhibition triggers **ferroptosis** in resistant GBM stem
  cells (2026), enhances **radiation** response (miR-217 nanomiR, 2024), and with
  **5-azacytidine** activates viral-mimicry immunity in PTEN-deficient GBM (2025).

## Practical read for CNS programs
1. **Do not assume brain exposure.** For tazemetostat specifically, plan around
   **P-gp/BCRP efflux**; measure free-brain PK, not just plasma or total brain.
2. **Prefer agents/strategies with CNS intent:** dual EZH1/2 (valemetostat),
   purpose-built brain-penetrant analogs, or EED-allosteric scaffolds — but demand
   **Kp,uu data**, which is the field's key missing number.
3. **Expect combinations, not monotherapy, in brain tumors** (HDACi, ONC201,
   DNMTi, radiation), which also lowers the exposure needed for effect.
4. **Confirm target engagement in tumor** (H3K27me3 by IHC on-treatment biopsy),
   since the stable mark means PD, not plasma Cmax, defines efficacy.
