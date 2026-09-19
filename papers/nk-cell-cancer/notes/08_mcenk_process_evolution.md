# Deep dive: how the M-ceNK process evolved, and why each decision was made

M-ceNK is the clearest public example of a company converting an academic *assay* — 12–16 h cytokine priming of NK
cells — into a manufacturable autologous product. The interesting part is not the final recipe but the sequence of
substitutions: every generation removes a reagent or a step that blocked scale, and each removal is documented in
ImmunityBio's own patent prose as a fix for a named deficiency of the previous generation.

**Source discipline.** There is no peer-reviewed M-ceNK process paper. The reconstruction below uses patent claims
and specifications (dated by priority), the trial record (NCT04898543), conference abstracts and company releases.
Patent claims describe what was *claimed*, not necessarily what is run in the clinic; company releases are claims,
not verified data. Mechanistic explanations that the sources do not state are labelled as inference.

## Generation 0 — the academic method they started from (2012–2016)

Brief co-exposure of purified NK cells to IL-12 + IL-15 + IL-18 for 12–16 h produces cytokine-induced memory-like
(CIML) NK cells: a differentiation state, not an expansion, with enhanced IFN-γ recall and killing weeks later
(PMID 22983442), clinically active in relapsed/refractory AML (PMID 27655849) and durable after transfer
(PMID 35349491, PMID 39948608).

Three properties of that method make it a poor product, and every later decision traces back to one of them:

- **Dose is capped by the collection.** No expansion step, so one apheresis ≈ one infusion. ImmunityBio's patent
  states this plainly: CIML NK "is typically limited in usage due to the relatively limited number of cells that
  can be produced… multiple samples must be taken multiple times from a patient."
- **Three separate research-grade cytokines.** GMP supply of rhIL-12/15/18 at scale is a genuine bottleneck — the
  problem that also drove the academic field to single fusion reagents (HCW9201; Cancer Immunol Res 2021).
- **Fresh product, allogeneic donors, lymphodepletion.** Fits a transplant centre, not a distributed outpatient
  product.

## Generation 1 (priority Jul 2019, NantKwest) — make NK cells from unselected MNC, feeder-free

Two sibling filings from the same day: **WO2021/006875** (MNC-derived NK) and **WO2021/006876 / US20210008112**
(CIML NK, the two-step version).

What was claimed: mononuclear cells from whole or cord blood, **no CD34 isolation, no NK selection, no feeder
layer**; activation with an **anti-CD16 agonist antibody (0.05–0.5 µg/mL) + N-803 (0.1–1.0 nM)**, optionally
anti-CD3 (0.1–1.0 ng/mL); sequential feeding **every ~72 h** with N-803 medium (NK MACS + human AB serum +
**hydrocortisone 0.1–5 µM**), in a **single container**, to ≥100-fold expansion, **NK ≥80–90% of live cells** and
0.5–5 × 10⁹ total cells; explicitly contemplated in an **automated bioreactor** that measures growth and feeds on
schedule. The sibling adds the architecture that defines the product: **expand first, then induce memory** with
IL-12/IL-15/IL-18 or an IL-18/IL-12-TxM fusion.

Why these choices, per the patents' own background: feeder layers are "problematic from a technical and a
regulatory perspective"; bead-based NK selection and multi-step manipulation "add significant costs"; prior
bioreactor-friendly methods gave low NK yield. The single-container, scheduled-feed design is not a lab
convenience — it is the shape a process must have to run in the NANT 001 "GMP-in-a-box" bioreactor the company
was building in parallel.

## Generation 2 (priority Mar/Jun 2021) — the M-CENK claims: drop the antibody, add a corticosteroid, use one fusion protein

**US20240228964A9 / EP4301846** claims, in order: obtain MNC → contact with **a corticosteroid + IL-15 or agonist**
(preferred: **hydrocortisone + N-803**) → incubate **14–21 days**, or until **NK ≥65% of live cells** → **induce
12–16 h with a cytokine composition having IL-12 + IL-15 + IL-18 activity**, preferably a single **TxM fusion
protein** → harvest, formulate at **0.5–1.5 × 10⁷ cells/mL**, cryopreserve. Dependent claims allow the **MNC to be
cryopreserved before culture**, then thawed and cultured.

Each delta from generation 1, and what it buys:

| Change | Stated or evident rationale | Benefit | Cost / risk |
| --- | --- | --- | --- |
| **Anti-CD16 agonist removed** | The patent names its own predecessor and its defect: in WO2021/006876, MNC "are activated with anti-CD16 antibodies and N-803, and then expanded using a cytokine mix. While conceptually simplified, various difficulties nevertheless remain, including presence of CD3+ cells and sub-optimal cytotoxicity against at least some target cells." It separately faults antibody-based stimulation for "significant costs due to the specific reagent required" | One less GMP antibody; cleaner cost of goods; avoids sustained CD16 crosslinking, which drives ADAM17-mediated CD16 shedding and activation-induced death *(mechanism is inference, not stated)* | Loses a strong, NK-selective activation signal; enrichment now depends entirely on cytokine + steroid |
| **Hydrocortisone promoted from feed additive to enrichment driver** | Claimed as the enrichment condition itself: corticosteroid + IL-15/N-803, with hydrocortisone the preferred steroid | Purity without beads: glucocorticoid suppresses T/NKT outgrowth while IL-15 signalling sustains NK survival *(mechanism inference)*; a cheap, well-characterised small molecule replaces an antibody | Glucocorticoids blunt IFN-γ and NK effector output; the process is dosing a functional inhibitor during the expansion phase and relying on the later induction step to restore the program |
| **Purity bar lowered 80–90% → ≥65% NK of live cells** | Not stated | Realistic for heavily pre-treated patient apheresis; keeps batches releasable | Product identity is more donor-dependent than a bead-selected product; final purity claims rest on the memory-induction step and downstream washing |
| **Expand (14–21 d), then induce (12–16 h)** | Patent: CIML produced in the lab is dose-limited, requiring repeat collections | Breaks the one-collection-one-dose ceiling; the memory program is imprinted *last*, so it is fresh at cryopreservation | Two weeks of IL-15-driven proliferation before the memory step — the state that is cryopreserved is expansion-experienced, not resting-donor, NK |
| **Three cytokines → one TxM fusion** | Patent prefers "induction of the M-CENK phenotype… with a single protein complex" | One GMP reagent instead of three; fixed stoichiometry; IL-15 delivered as physiological trans-presentation on the N-803 scaffold. 18/12/TxM matches individual-cytokine priming transcriptionally and functionally (PMID 35284622) | Ties the product to a proprietary biologic; potency now depends on a fusion protein's lot-to-lot behaviour |
| **MNC cryopreserved upstream** | Claims 2–3 | Decouples collection from manufacture: patients can be apheresed while fit, before or between therapy lines, and doses made later — this directly attacks the autologous failure mode (poor starting material from pre-treated patients) | Adds a freeze–thaw before culture; starting-material quality now also depends on cryo performance |
| **Cryopreserved drug product** | Consistent across all generations | Multiple doses banked per collection; outpatient weekly dosing; shipping | Post-thaw function is the known weak point of NK products (section 05), and no post-thaw release criterion is public |

One line in the background explains the product's declared phenotype. Criticising prior TxM priming of freshly
isolated NK cells, the patent attributes its sub-optimal killing to "lack or low expression of specific activating
receptors and/or expression of specific inhibitory receptors." That is exactly the axis on which M-ceNK is now
characterised — NKp30/NKp44/NKp46 high, KLRG1/TIGIT low — so the receptor panel is not descriptive marketing; it is
the company's own stated theory of why its process beats short priming alone.

## Generation 3 (2021 → 2026) — what changed once it met patients

Public claims over time, all company-sourced except the registry row:

| | 2021 (IND authorisation) | 2022 (scale announcement) | 2021→2025 registry (NCT04898543) | 2026 (NK2022/NK2023 completion) |
| --- | --- | --- | --- | --- |
| Culture | MNC + N-803 enrichment, **2–3 log expansion by week 3**, then brief cytokine cocktail + rest | same architecture | not disclosed | **finished dosage form in 12 days** |
| Yield | ">3,000% expansion" | **>20 × 10⁹ cells** per collection | — | **up to 5 × 10⁹ cells** |
| Doses | 10–20 × **0.5 × 10⁹** | 10–20 × **1 × 10⁹** | up to **10 weekly**, **0.25–0.75 × 10⁹** per 100 mL bag | **8–10 doses** |
| Schedule | — | 4 doses (d1, 8, 15, 22), N-803 d1/d15 | up to 10 weekly M-CENK; **N-803 15 µg/kg SC** q2w before odd-numbered doses, ×5 | **23 doses across 10 treated patients — 2 to 5 bags each**, all outpatient |
| Automation | NANT 001 "GMP-in-a-box" | NANT 001 | — | ready for **NANT Leonardo** robotics |

Two honest readings of that trajectory, both inference:

1. **The dose and yield claims came down by ~4-fold while the timeline halved.** The most likely explanation is that
   2021–22 figures were research-scale, healthy-donor-weighted, and the GMP-validated process traded total yield for
   speed, reproducibility across cancer-patient material, and post-thaw quality. A 12-day process cannot reach the
   same fold expansion as a 21-day one — this is a deliberate trade, not a failure, but it should be read as one.
2. **The programme spent five years de-risking starting material rather than biology.** Of 74 subjects enrolled
   across NK2022/NK2023 and the trial, 64 existed only to show that large-volume non-mobilised apheresis is safe and
   that downstream enrichment is reproducible in healthy donors *and* pre-treated cancer patients; only 10 were
   dosed. For an autologous product that is the correct place to spend the money, and it is the step most
   competitors skip. The headline manufacturing result is the one that matters most: NK cells from cancer patients,
   including those with prior systemic therapy, killed NK-resistant lines equivalently to healthy-donor cells
   (company-reported).

Two claims in the same release should not be carried forward uncritically. Patients actually received **2–5 doses**,
not the 8–10 the process supports or the 10 the protocol allows — the gap between manufacturable and administered
doses is unexplained. And the "World Bank of NK Cells" framing extends to NK cells "universally donated to any
patient without HLA matching", which is an allogeneic proposition; nothing in the autologous M-ceNK data supports it.
Safety so far is clean (no grade 4/5 treatment-related events, no cytokine storm, outpatient dosing), but a 10-patient
phase I with no reported response data says nothing about efficacy.

In vivo evidence arrived only in 2026 and is not the company's: an NCI group reported M-ceNK + N-803 shrinking two
SCLC xenografts with persistence of functional cells, plus upregulation of MHC class I on residual tumour — a
sensible niche, since 62% of the neuroendocrine tumours they surveyed lack MHC class I and are therefore T-cell-cold
but missing-self vulnerable (AACR IO 2026, conference-stage).

## What the design is betting on

- **Programming over payload.** No CAR, no IL-15 armouring, no knockouts. Potency comes from a differentiation state
  and from systemic N-803 — the same molecule used inside the process. The allogeneic warning that systemic IL-15
  accelerates rejection of infused NK cells (PMID 34797911, PMID 39948608) should not apply to an autologous product,
  which makes N-803 a more defensible pairing here than where it was first tested.
- **Purity by culture, not by selection.** Cheaper and automatable, but final identity depends on the patient's own
  NK compartment responding to hydrocortisone + N-803 — untestable from the public record, and precisely what the
  64-subject apheresis programme was built to answer.
- **A metabolic phenotype they have not yet defended.** M-ceNK is characterised as CD3⁻CD56^high, NKp30/44/46-high,
  KLRG1/TIGIT-low, IFN-γ/granzyme B-high, with **increased reliance on glycolysis** (AACR IO 2026 A018; median 69%
  lysis, range 35–89%, at E:T 5:1 against neuroendocrine lines). Glycolytic dependence is a liability in the hypoxic,
  glucose-poor tumours these cells are aimed at — the axis this review ranks as failure mode #1, and the one where
  metabolic programming determines whether infused NK cells function at all (PMID 39475618).

## Still undisclosed

Which patented variant is the clinical process; hydrocortisone and TxM concentrations actually used; the medium and
vessel; purity, viability and potency acceptance criteria; post-thaw recovery and function; the fraction of
pre-treated patients whose material yields a releasable batch; and any efficacy readout from QUILT-3.076.

## Sources outside the curated corpus

Patents: WO2021/006875 (CA3120695C, priority 2019-07-08, NantKwest); WO2021/006876 / US20210008112A1 (same
priority); US20240228964A9 / EP4301846A1 (priority 2021-03-03, ImmunityBio); WO2018/165208 (18/12-TxM).
Literature not in `index.tsv`: PMID 35284622 (18/12/TxM fusion scaffold); the HCW9201 heteromeric fusion platform
(Cancer Immunol Res 2021, PMC8416787). Trial: NCT04898543 (start 2021-06-21). Abstracts: AACR IO 2026 A018;
SITC 2023 ab358; ASCO 2025 trial-in-progress. Company releases: 17 May 2021, 2 Mar 2022, 13 Mar 2026; NCI Drug
Dictionary entry for autologous memory cytokine-enriched NK cells.
