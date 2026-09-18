# Case comparison: NKGen SNK01 (troculeucel) vs ImmunityBio M-ceNK

Two autologous, non-gene-modified peripheral-blood NK products that make **opposite process bets**. Both avoid
allogeneic rejection and donor-matching entirely; both refuse genetic engineering. They diverge on the one
question section 02 poses: do you buy potency with *expansion and activation*, or with *cytokine programming*?

- **SNK01** buys dose and receptor density: feeder-driven 17–18 day expansion to ~10⁴-fold, ≥95% purity,
  multi-billion-cell doses, activating-receptor expression as the declared product attribute.
- **M-ceNK** buys a differentiation state: ~12 days of feeder-free cytokine culture (IL-12/IL-18 plus the
  IL-15 superagonist N-803) to a memory-like CD3⁻CD56^high population, sub-billion doses, and persistence
  outsourced to systemic N-803 (ANKTIVA) after infusion.

**Evidence asymmetry to keep in mind.** SNK01's process, release specification and clinical results are in
peer-reviewed papers (PMID 38538093 and the phase I/IIa pembrolizumab trial, PMID 34856706). The M-ceNK
process is disclosed in patents, conference abstracts, a trial registration (NCT04898543) and company
releases — no peer-reviewed process paper. Statements below are labelled accordingly, and company-reported
numbers are claims, not independently verified data.

## Side by side

| | SNK01 / troculeucel (NKGen, NKMAX) | M-ceNK (ImmunityBio) |
| --- | --- | --- |
| Starting material | Leukapheresis or whole blood; **CD56⁺ positive selection** (CliniMACS CD56 microbeads) | Non-mobilized large-volume leukapheresis MNC; **no NK positive selection** (one patent family depletes CD3⁺/CD14⁺ instead) |
| Stimulation | Two γ-irradiated (100 Gy) feeder lines — **KL-1** (HLA class-I-low Jurkat subline) and **LCL** B cells — plus **IL-2 500 IU/mL + IL-21 50 ng/mL** | **Feeder-free cytokine programming**: N-803 (IL-15 superagonist) with IL-12 and IL-18; patent claims hydrocortisone + N-803 + human AB serum, then a short IL-12/IL-18-TxM induction (12–16 h) |
| Medium | RPMI-1640 + 10% FBS + gentamicin, subculture every 3–4 days | Serum-containing (human AB serum per patent); automated bioreactor contemplated |
| Duration | 17–18 days culture; ~30 days collection-to-release for the cryopreserved process | ~12 days apheresis-to-finished dosage form (company) |
| Yield | ~10⁴-fold (company); ≈4.5 × 10⁶-fold cumulative across the manufacturing campaign in the NSCLC trial; ~20 doses per batch from one leukapheresis | Up to 5 × 10⁹ cells per apheresis = **8–10 doses** (company); earlier release claimed 10–20 doses |
| Dose | **4–6 × 10⁹ cells/dose** weekly (NSCLC); 2–4 × 10⁹ with pembrolizumab; 6 × 10⁹ Q3W in the Alzheimer's programme | **0.25–0.75 × 10⁹ cells/dose** weekly, up to 10 doses (NCT04898543) |
| Product form | Originally **fresh**, formulated in Hartmann's solution + 1% HSA **with IL-2 500 IU/mL**, shipped at 2–8 °C; newer process cryopreserved (~2-year storage) | **Cryopreserved** from the outset; cryo-banked doses thawed per cycle |
| In vivo support | None systemic — IL-2 travels in the infusion bag; combinations are with checkpoint blockade (pembrolizumab) or chemo/cetuximab | **Systemic N-803 subcutaneously** every 2 weeks, designed to sustain proliferation and persistence after transfer |
| Lymphodepletion | None | None |
| Genetic modification | None | None |

## SNK01: what the published protocol actually specifies

Source: supplementary methods of PMID 34856706, with the same process used in PMID 38538093.

1. CD56⁺ cells selected from patient PBMC (starting CD3⁻CD56⁺ purity is donor-variable, 77.8 ± 12.6%).
2. Co-culture with irradiated KL-1 and LCL feeders in IL-2 (500 IU/mL) plus IL-21 (50 ng/mL); subculture
   every 3–4 days. KL-1 is the class-I-low Jurkat subline identified for selective NK outgrowth; the LCL
   partner supplies CD16-engaging B-cell ligands — feeder-driven CD16 triggering is intrinsic to this platform.
3. Harvest day 17–18, wash, formulate in Hartmann's solution with 1% human serum albumin and IL-2.
4. Final product: **CD3⁻CD56⁺ 99.81 ± 0.22%**, CD3⁺ 0.15%, CD14⁺ 0.32%, CD20⁺ 0.01%, viability 98 ± 1%.

**Release specification (published):** sterility (bacteria, fungi, virus, mycoplasma); viability ≥80%;
**cytotoxicity ≥50% against K562 at E:T 10:1**; endotoxin ≤0.5 EU/mL; CD3⁻CD56⁺ ≥80% with CD3, CD14, CD20
each ≤5%. Note what is *and is not* there: a 4-hour 2-D K562 assay is the potency gate — exactly the assay
section 05 argues does not predict tissue-relevant function, and the assay that cryopreservation passes while
3-D migration and killing are lost (PMID 33067467).

**Target phenotype, as declared by the sponsor.** The product is characterised as CD56^bright CD16⁺ with
elevated activating and chemokine receptors rather than by a memory-like signature: per-batch QC values
reported from the Alzheimer's trial were NKG2D 98.8–99.4%, DNAM-1 98.6–100%, CXCR3 94.7–97.8%, NKp46
70.5–82.2% (company presentation). The phenotyping panel in the trial covers NKG2D, NKp30, NKp44, NKp46,
CD16, DNAM-1, CXCR3, CX3CR1, NKG2A, KIR (CD158a/b/e) and intracellular perforin/granzyme. CXCR3 is the
trafficking claim (CNS entry in the neurodegeneration programme); NKG2D/DNAM-1 carry the cytotoxicity claim.

## M-ceNK: what is disclosed

Sources: NCT04898543 and its ASCO 2025 trial-in-progress abstract, NCI-collaboration abstracts
(SITC 2023 ab358; AACR IO 2026 A018), ImmunityBio patents (US20240228964A9; CA3120695C) and the March 2026
manufacturing release.

1. Apheresis MNC exposed to a cytokine cocktail including **N-803, IL-12 and IL-18** until a highly purified
   CD3⁻CD56^high population results — enrichment by differential cytokine response, not by bead selection.
2. Patent-claimed variants: hydrocortisone + N-803 + human AB serum for 14–21 days (or until NK ≥65% of live
   cells) followed by 12–16 h induction with an IL-12/IL-18-TxM fusion complex; a separate family depletes
   CD3⁺/CD14⁺ first and uses IL-12/IL-15/IL-18 derivatives to stabilise **CD16** expression and shorten the
   process to 10–12 days. The patents explicitly position this as distinct from classical CIML protocols,
   which pre-activate briefly and do not expand.
3. Cryopreserved dosage form within ~12 days; company reports retained cytotoxicity post-thaw.

**Target phenotype, as reported.** CD3⁻CD56^high with **high natural cytotoxicity receptors (NKp30, NKp44,
NKp46), low inhibitory markers (KLRG1, TIGIT)**, elevated IFN-γ and granzyme B versus unmanipulated healthy-donor
NK cells, and **increased glycolytic dependence** — the only one of the two products whose declared phenotype
includes a metabolic attribute, which is the axis section 03 ranks as failure mode #1. No public release
specification (purity thresholds, potency assay, acceptance criteria) has been disclosed.

**Clinical status.** QUILT-3.076 dosed 10 relapsed/refractory solid-tumour patients (2–5 bags each) with
weekly M-ceNK plus subcutaneous N-803, all outpatient, no grade 4–5 treatment-related events and no cytokine
storm reported; 64 subjects completed apheresis across the NK2022/NK2023 process-engineering programmes. These
are safety and feasibility claims from company disclosure — no efficacy readout is published.

## What the comparison teaches

1. **Purity can come from selection or from selective culture.** SNK01 pays for CD56 beads and gets 99.8%
   purity independent of donor NK response; M-ceNK lets cytokines do the selecting, which removes a costly
   step but makes final purity a function of the patient's own NK compartment — the failure mode that matters
   most for autologous products in heavily pre-treated patients (section 03, #8).
2. **Dose and state are substitutable within limits.** The two products differ ~10-fold per dose in the same
   direction as their process philosophies. There is no head-to-head evidence that either substitution is
   correct, and no shared potency assay that would let the comparison be made — the gap section 02 flags.
3. **Persistence is either not addressed or outsourced.** Neither product is IL-15-armoured. SNK01 puts IL-2
   in the bag and relies on weekly redosing; M-ceNK relies on systemic N-803. The allogeneic trials warn that
   systemic IL-15 accelerates rejection of infused NK cells by recipient CD8 T cells (PMID 34797911, PMID
   39948608) — a penalty that should not apply to an autologous product, making N-803 support a more
   defensible pairing here than in the haploidentical setting where it was first tested.
4. **Feeders are a CMC liability that buys real expansion.** KL-1 + LCL feeders are what makes 10⁴-fold and
   6 × 10⁹-cell doses possible; they also import irradiated tumour-line and EBV-transformed B-cell residual
   testing into every batch. M-ceNK's feeder-free route avoids that file entirely and reaches a cryopreserved
   product in ~12 days, at roughly one-tenth the dose.
5. **Both release specifications are weaker than their biology.** SNK01's is public and gates on a 4-hour 2-D
   K562 assay; M-ceNK's is not public. Neither discloses a post-thaw migration or 3-D killing assay, which is
   where cryopreserved NK product most reliably fails (section 05).

## Open questions a data room would need to answer

- SNK01: what is the cryopreserved process's post-thaw potency and phenotype versus the fresh product that
  generated the clinical data, and is the release assay unchanged across that switch?
- M-ceNK: which of the patented variants is the clinical process, what are the purity/potency acceptance
  criteria, and what fraction of heavily pre-treated patients yield a releasable batch?
- Both: fold-expansion and receptor percentages are reported per batch, but neither discloses serial-killing
  capacity, CD16 shedding after activation, or function in a 3-D or organoid assay.

## Sources outside the curated corpus

PMIDs cited above are in `index.tsv` except **PMID 34856706** (Kim et al., *Cancer Res Treat* 2022, SNK01 +
pembrolizumab phase I/IIa) and **PMID 23580577** (Lim et al., *Cancer Res* 2013, the KL-1 + LCL feeder
expansion method the process derives from — ~100-fold with KL-1 alone, ~740-fold with EBV-transformed B cells
added, CD16-dependent). Non-literature sources: NCT04872634, NCT04898543, NCT06710288;
ImmunityBio patents US20240228964A9 and CA3120695C; ImmunityBio press release 13 Mar 2026; NKGen Biotech
WCN 2025 and AD/PD 2026 presentations.
