# Naeimi Kararoudi lab: NK and γδ T cell expansion / culture conditions — synthesis

Scope: what Meisam Naeimi Kararoudi (DVM, PhD) has actually published and patented on NK and γδ T
cell **expansion and culture conditions**, and how his verbally-stated design rule for γδ T cells
("short TCR expansion, then feeder cells that do JAK/STAT stimulation") maps onto that body of work
and onto the wider γδ T cell literature.

---

## 0. TL;DR — decoding the verbal statement

The reported statement was:

> - short TCR expansion period. too long = exhausted cells
> - instead have feeder cells that do JAK/STAT stimulation

This is not a vague heuristic. It is a fairly literal description of the manufacturing process
claimed in his γδ T patent application **WO2025123022A1, "Compositions and methods of making a
modified gamma-delta T-cell"** (Research Institute at Nationwide Children's Hospital; priority
US 63/608,159, 8 Dec 2023):

| His phrase | What it means concretely | Where it appears |
|---|---|---|
| "short TCR expansion period" | γδ T cells isolated by immunomagnetic **negative** selection, then seeded on **plate-bound anti-CD3 (± anti-CD28)** for a *priming* window only — "**at least 6 hours**", "1, 2, 3, 4, 5, 6, 7 days", claimed as "**at least 2 days**" | WO2025123022A1 [0076], claims 10–11 |
| "too long = exhausted cells" | The TCR-agonist phase is deliberately terminated; prolonged TCR crosslinking is the exhaustion/AICD driver, not culture *per se* | Rationale; not itself claimed. See §4 for the evidence |
| "feeder cells that do JAK/STAT stimulation" | After priming, switch to irradiated **K562.mbIL21.4-1BBL** feeders (the Lee-lab FC21 line; clinical-grade equivalent **CStX-002**) at ≥2:1 feeder:cell, with **100 IU/mL IL-2** replenished ~every 48 h. mbIL-21 → IL-21R → **JAK1/JAK3 → STAT3** (+STAT1); 4-1BBL → 4-1BB → TRAF/NF-κB | WO2025123022A1 [0077]–[0078], claims 12–18, 39–46 |

So "JAK/STAT stimulation" = **membrane-bound IL-21 signalling through STAT3**, delivered as a
*contact-dependent, repeatable* stimulus by an irradiated engineered K562 feeder, deliberately
substituted for continued antigen-receptor stimulation. The separate claim set 39–46 ("A method of
making gamma delta T cells **susceptible to gene editing** comprising culturing the γδ T cells with
feeder cells that comprise mbIL21") shows the second purpose of the feeder phase: the mbIL21-driven
proliferative state is also the state in which CRISPR/AAV6 editing works.

**Important nuance / internal tension.** In the one peer-reviewed γδ paper he co-authored
(Portillo et al., *OncoImmunology* 2025), the protocol uses **no TCR agonist at all** and runs
**≥5 weeks** of weekly mbIL21 feeder restimulation. That paper's own discussion says
"*Decreasing the length of the expansion process may be advantageous as long-term expansion could
lead to γδ T cell exhaustion*". So the "short" in his verbal rule is best read as **short
TCR-agonist phase**, with total culture length still an open, actively-debated variable in his own
work. See §3.3 for the two distinct process designs that coexist across his patent and his paper.

---

## 1. Who / where (context for the IP landscape)

- DVM (Iran) → PhD-track work in Sweden (Gothenburg, xenotransplantation/CRISPR) → postdoc with
  **Dean A. Lee** (Cellular Therapy & Cancer Immunology, Nationwide Children's Hospital, NCH),
  where he solved efficient Cas9/RNP editing of primary and expanded human NK cells.
- Then Director, **CRISPR/Gene Editing Core**, and PI, Center for Childhood Cancer Research, NCH;
  Assistant Professor of Pediatrics, Ohio State.
- Now **Director of Innovation in Cell and Gene Therapies, Cincinnati Children's** (Associate
  Professor, UC Dept. of Pediatrics).
- Founder/affiliate of **CARTx Therapeutics** — stated mission: affordable off-the-shelf CAR-T made
  from **γδ T cells** using **CRISPR/AAV**, targeted at low- and middle-income countries.

Practical consequence: almost all of his expansion-platform IP is **assigned to Research Institute
at Nationwide Children's Hospital**, and much of it names **Dean Lee** as co-inventor, because the
underlying feeder platform (K562 clone9.mbIL21.4-1BBL) is Lee-lineage technology
(MD Anderson → NCH). The γδ work is the newest branch and the one where he is lead inventor.

---

## 2. The NK platform he inherited and optimized (the foundation for everything γδ)

### 2.1 The feeder line

- **FC21 / K562 clone 9.mbIL21.4-1BBL** — K562 (HLA-I-null CML line) engineered with CD19, CD64,
  CD86, **4-1BBL (CD137L)**, and **membrane-bound IL-21**; γ-irradiated before use.
  Clinical-grade descendant referenced in his patent: **CStX-002**.
- Culture parameters, stated per source rather than merged (they differ):
  - *Cell Rep Methods* 2022 (NK): feeders **2:1 (feeder:NK)**, serum-free **AIM-V/ICSR** medium,
    **50 IU/mL IL-2**, 7-day stimulation before editing; after electroporation, feed at 24 h and
    **re-stimulate with 2×10⁶ feeder cells at 48 h**.
  - *OncoImmunology* 2025 (γδ/NK): feeders **1:2 (cells:feeder)** = 2 feeders per cell, complete
    **RPMI-1640**, **IL-2 100 U/mL**, feeders replenished **weekly**, media + IL-2 **q2–3 days**.
  - WO2025123022A1 (γδ): feeders **≥2:1 (feeder:cell)**, **100 IU IL-2 q48h**.
  The three feeder ratios are the same number written in different orders (~2 feeders per target
  cell); the IL-2 dose genuinely differs (50 IU in the NK paper vs 100 in the γδ work).

### 2.2 Why mbIL-21 rather than mbIL-15 — the STAT3 argument

The founding dataset is **Denman et al., PLoS ONE 2012** (Lee lab, MD Anderson), which is the
citation behind every subsequent "mbIL21 feeder" claim:

| Feeder | Day-21 fold expansion (mean, 22 donors) | Telomeres | Proliferative lifespan |
|---|---|---|---|
| K562.4-1BBL.**mbIL15** | ~825-fold (median 325) | **shortened** vs fresh NK | senescence, proliferation lost at weeks 4–6 |
| K562.4-1BBL.**mbIL21** | ~**47,967-fold** (median 31,747) | **increased** vs fresh NK | log-phase growth ≥6 weeks, no senescence |

Mechanistic rationale, stated explicitly in the original 2009 ASH abstract: *IL-21 signals via
STAT3, and STAT3 is a known activator of telomerase (hTERT) transcription.* Downstream work adds:

- **mbIL-21 → STAT3/cMyc → metabolic reprogramming** of NK cells; expanded cells retain glycolytic
  and OXPHOS capacity in hostile TMEs (Poznanski et al., *Cell Metab* 2021; reviewed in
  Gurney et al., *Front Immunol* 2022, PMC8873083).
- **IL-15-expanded NK cells overexpress GSK3β** and are functionally/metabolically impaired,
  whereas **mbIL-21 expansion maintains normal GSK3β levels** — this was the enabling observation
  that let his group study GSK3B by CRISPR KO at all (Pereira, …, Naeimi Kararoudi, *Cancers* 2023).

This is the mechanistic core of "feeder cells that do JAK/STAT stimulation": a *STAT3-biased*
γc-cytokine signal delivered in trans, rather than a STAT5-dominant (IL-2/IL-15) or
TCR/ITAM-dominant signal.

### 2.3 The editing window — why expansion state matters, not just cell number

*Cell Rep Methods* 2022 (Naeimi Kararoudi et al.) showed that FC21 expansion **broadly upregulates
HDR and NHEJ machinery** (BRCA1, BRCA2, RAD51, LIG4 all up; only ATM modestly down) relative to
freshly isolated NK cells — i.e. expansion creates a *permissive editing window*. Their canonical
schedule:

- **Day 0** isolate (RosetteSep negative selection), start FC21 co-culture, 50 IU/mL IL-2
- **Day 7** electroporate Cas9/RNP (Alt-R HiFi Cas9 V3 + sgRNA; AAVS1 or gene-specific gRNA)
- **+20–30 min** transduce ssAAV6/scAAV6 donor (typically **300K MOI**, range 10K–500K)
- **+24 h** feed with fresh media + 50 IU IL-2 (old media not changed); **+48 h** re-stimulate with
  **2×10⁶ feeder cells**; 48 h after that, add 8 mL fresh IL-2-supplemented media
- Read out CAR at day 7 and day 14 post-electroporation; CAR expression is **stable through
  further expansion** — the historical failure mode this method solved. (Electroporation program
  for NK was **EN-138**; the γδ patent re-optimized to **CM-137**.)

The same logic is transplanted verbatim into the γδ program (see §3).

### 2.4 NK-side IP and edits (all built on this culture platform)

| Technology | Content | Reference |
|---|---|---|
| CD38 KO NK | Eliminates daratumumab-induced fratricide, boosts effector activity | *Blood* 2020; WO/CA3156509A1; NCH TS listing |
| **ADAM17 KO** | Preserves CD16 after cryopreservation → higher ADCC post-thaw | NCH TS-003705 (Lee, Naeimi Kararoudi, Sorathia) |
| **TIGIT locus as CAR integration site** | Removes inhibitory checkpoint *and* provides the CAR knock-in site | NCH TS-004607; WO2026085461A1 |
| **CD70 KO + CD70 locus as CAR site** | Avoids CD70-CAR fratricide | NCH TS-003681; WO2024124244A1 (CD38 analogue) |
| CD33-CAR / CD38-CAR NK | CRISPR/AAV6 knock-in at AAVS1 or at the target locus | *Cell Rep Methods* 2022; *Blood Neoplasia* 2024 |
| GSK3B KO NK | Metabolic reprogramming | *Cancers* 2023; WO2024155711A1 |
| **HLA-I downregulation via integrated shRNA** | Allogeneic persistence while preserving NK "missing-self" inhibition | NCH TS-005768 (sole inventor) |
| **CD8+γδNKT CAR cell generation *and expansion*** | Explicitly an expansion + CAR technology for an off-the-shelf CAR-T | NCH **TS-005689** (Naeimi Kararoudi, Martin, Sezgin, Snyder) |

---

## 3. The γδ T program

### 3.1 Patent: WO2025123022A1 (lead inventor Naeimi Kararoudi)

**Process, as claimed:**

1. PBMC from buffy coat, Ficoll density gradient, resuspend at 5×10⁷/mL.
2. **γδ T isolation by immunomagnetic negative selection** (StemCell EasySep Human Gamma/Delta
   T Cell Isolation Kit, #19255) — the spec explicitly justifies negative selection because
   *antibody binding to the cell surface may induce activation or block ligand–receptor
   interactions*. (Note the internal consistency: they avoid incidental TCR ligation during
   isolation, then apply a *controlled, time-limited* TCR stimulus.)
3. **Short TCR priming**: plate-bound anti-CD3 (± anti-CD28), "at least 6 hours", 1–7 days,
   claimed at **≥2 days**.
4. **Feeder phase**: irradiated **K562.mbIL21.4-1BBL / CStX-002** at ≥**2:1**, **100 IU IL-2**
   every ~48 h, ≥7 days (claim 19). Alternatives recited: EBV-LCL, RPMI8866, HFWT, irradiated
   PBMC, K562-mbIL15/4-1BBL.
5. **Editing at ~day 14–21**: 3×10⁶ cells/condition electroporated with Cas9/RNP
   (4D-Nucleofector, **P3 buffer**, program **CM-137** was optimal vs EO-115 and EH-115 for
   viability × mCherry⁺), then 2×10⁶ cells transduced with **AAV6** donor at **MOI 75K**
   (vs 300K used for NK), 24 h later fed with RPMI +10% FBS/P-S/GlutaMAX/HEPES **+100 IU IL-2**.
6. Product: **CD70 KO + CD70-CAR knocked into AAVS1 simultaneously** (fratricide avoidance —
   97.1% of expanded γδ T cells were CD70⁺ before editing). CAR obtained in **both Vδ1 and Vδ2**
   subsets. Also claimed: CD38, CD33, **TGFβRII** KO/CAR pairs.
7. Reported purity after 2 weeks: **98.8% CD3⁺, 98.4% TCRγδ⁺**.
8. Indication framing: allogeneic cancer therapy **without GvHD**.

### 3.2 Peer-reviewed: Portillo, …, Lee, Naeimi Kararoudi, Ashkar. *OncoImmunology* 2025;14(1):2562210 (PMC12477882)

"IL-21-reprogrammed Vδ1 T cells exert killing against solid tumors which is enhanced by CAR arming
for off-the-shelf immunotherapy" — McMaster (Ashkar) × NCH collaboration; the feeders came from
Dean Lee.

**Expansion method (Methods, verbatim details):**
- Bulk PBMC **or** EasySep-positively-selected CD3⁺ T cells co-cultured with **K562-mbIL-21 at 1:2
  (cells:feeder)**; complete RPMI-1640 + **100 U/mL IL-2**; **irradiated feeders replenished
  weekly**; media/IL-2 every 2–3 days; **≥5 weeks** before functional assays.
- **No TCR agonist, no mitogen, no zoledronate** — this is stated as a deliberate design choice
  and as the novelty vs prior Vδ1 protocols.
- Comparator arms in the same paper: **K562-mbIL-15** feeders (same 1:2), and classic
  **Vγ9Vδ2** expansion = **"10 mM" zoledronic acid + 4 ng/mL IL-2** in a 24-well G-Rex at
  2×10⁶ cells/cm², harvested day 14. (The "10 mM" is as printed in the paper and is almost
  certainly a µM/mM error — standard is 1–5 µM. Don't reuse the number unchecked.)
- CAR arming: adapted from the NK CRISPR/AAV method (ref. 27 = his own *Cell Rep Methods* 2022):
  HiFi Cas9/RNP + AAVS1 gRNA, then **ssAAV6-HER2-CAR at 300K MOI**.

**Key results relevant to the culture question:**
- mbIL-21 feeders **preferentially expand Vδ1** (Vδ2 essentially disappears; Table 1 donors are
  ~22–99% Vδ1, 0–0.4% Vδ2). **>500-fold** γδ expansion from bulk PBMC and **>26,000-fold** from
  isolated CD3⁺ over the culture period.
- Expanded γδ T cells acquire an **NK-like activation program**: ↑NKG2D, NKp30, NKp44, CD69, CD56;
  unchanged NKG2A/KIRs.
- They also **upregulate TIGIT and TIM3** — the authors flag these as ambiguous in this context
  (also high on highly functional mbIL-21-expanded NK cells).
- They retain **CD71/nutrient transporter expression, glycolysis, OXPHOS and killing in
  patient-derived ovarian ascites**, whereas fresh γδ T cells and **zoledronate-activated Vδ2 cells
  lost nearly all CD71** — i.e. a direct head-to-head showing the TCR-agonist-expanded product is
  the metabolically fragile one.
- Discussion, verbatim: *"Decreasing the length of the expansion process may be advantageous as
  long-term expansion could lead to γδ T cell exhaustion and potentially impair the expansion
  capacity of γδ T cells after adoptive transfer."* And separately: it is *"worth examining whether
  addition of Vδ1 TCR stimulation may increase the yield and purity"*.
- Odd/unexplained finding to keep in mind: near-absent CD107a and IFN-γ on tumor contact despite
  potent killing; IFN-γ/TNF-α recoverable with IL-12/15/18 or PMA/ionomycin.

### 3.3 The two coexisting process designs — this is the actual "make sense of it" point

| | **Design A — Portillo/Ashkar 2025 (published)** | **Design B — WO2025123022A1 (patent) / CARTx** |
|---|---|---|
| TCR agonist | **none** | plate-bound anti-CD3, **≥6 h to ~2–7 days only** |
| Feeder | K562-mbIL21 **+ 4-1BBL**, 2 feeders/cell, weekly | K562.mbIL21.4-1BBL / CStX-002, ≥2 feeders/cell |
| IL-2 | 100 U/mL | 100 IU, ~q48h |
| Duration to product | **≥5 weeks** | edit at ~d14–21; CAR product ~14 d post-transduction |
| Subset output | **Vδ1-dominant** (Vδ2 lost) | **polyclonal — CAR obtained in both Vδ1 and Vδ2** |
| Starting purity step | CD3⁺ positive selection or bulk PBMC | γδ **negative** selection |

Reading them together, the coherent design logic is:

1. **TCR signal is a starter, not an engine.** A brief anti-CD3 pulse recruits the whole γδ
   repertoire (including Vδ2, which is otherwise outcompeted) into cycle and shortens time to a
   gene-editable blast state. Leaving it on is what costs you.
2. **The engine is mbIL-21/STAT3 + 4-1BB/NF-κB, delivered by cells.** Repeatable weekly, contact
   dependent, telomere/hTERT-supporting, metabolically favourable, and — critically for his
   program — the state in which Cas9/RNP + AAV6 knock-in works (patent claims 39–46 make this an
   independent invention).
3. **Skip the TCR pulse and you get a purer but narrower product.** Design A's Vδ1 selectivity is a
   *consequence* of removing TCR agonism, not an independent trick. His patent's choice to keep a
   short pulse is what preserves Vδ2 and polyclonality.
4. **Total culture length remains unresolved** and is explicitly named as the next thing to shorten.

---

## 4. Is "too long TCR stimulation = exhausted cells" supported by the γδ literature?

**Directionally yes, with caveats. The strongest evidence is about TCR-agonist *dose/repetition*,
not simply days in culture.**

Supporting:

- **Zoledronate dose-dependently drives an inhibitory-receptor phenotype in Vδ2 cells.**
  ZA-expanded Vδ2⁺ cells upregulate **PD-1, TIM-3, TIGIT, LAG-3 and CD57** in a dose-dependent
  manner and kill THP-1 targets **worse** at higher ZA; heat-killed BCG expansion of the same cells
  does not raise PD-1 (St George's/Open Access study of BCG vs ZA, *Clin Exp Immunol* 2022).
- **Repeated in vivo phosphoantigen stimulation depletes and desensitizes the compartment.**
  In early-stage breast cancer patients, ZA treatment alone **decreased Vγ2Vδ2 numbers and reduced
  their ex vivo responsiveness**; patients with low baseline frequencies were poorly responsive
  (Kobayashi/Tanaka-type studies, PMC3639312). This is the clinical correlate of "burning out the
  TCR arm", and it is a large part of why >20 years of ZA/pAg + IL-2 γδ trials produced modest
  clinical results despite excellent in vitro killing.
- **Generic T-cell exhaustion biology.** Chronic/repetitive TCR–ITAM signalling drives the
  NR4A/TOX-dependent exhaustion program and activation-induced cell death; γδ T cells are not
  exempt. A dedicated 2025 *Front Immunol* review now specifically models **exhausted Vγ9Vδ2 cells**
  as an entity worth targeting with checkpoint blockade.
- **γδ T cells can be driven to potent function with no TCR signal at all.** Schilbach et al.
  (*Cancers* 2020) showed IL-2/IL-12/IL-18-stimulated γδ T cells kill and induce senescence in
  tumor cells **in the absence of a TCR signal**. Deniger et al. (*Clin Cancer Res* 2014, the
  MD Anderson aAPC paper) found polyclonal γδ proliferation depended on **CD137L on the aAPC plus
  exogenous IL-2 and IL-21**, not on TCR agonism.
- **Portillo's own head-to-head**: zoledronate-activated Vδ2 cells lost CD71 and metabolic
  competence in ascites; mbIL-21-expanded Vδ1 cells did not.

Caveats / where the statement is loose:

- **"Exhaustion" is being used phenotypically.** The mbIL-21 route also produces **TIGIT-high,
  TIM3-high** γδ T cells (Portillo Fig. 2), and those cells kill well. Inhibitory-receptor
  expression after strong expansion is not by itself exhaustion; no one has yet shown TOX/TCF7/
  epigenetic exhaustion signatures, serial-killing decay, or post-transfer re-expansion failure
  comparing short-vs-long TCR priming in γδ cells. That experiment appears not to exist.
- **Long culture without TCR agonist is still long culture.** 5+ weeks of weekly restimulation is
  not obviously "short" — the protective claim rests on the STAT3/telomere argument imported from
  NK biology (Denman 2012), which has **not** been directly validated for telomere length/hTERT in
  γδ T cells.
- **Some leading Vδ1 platforms use sustained TCR agonism and work fine.** The **DOT (Delta One T)**
  protocol (Almeida et al., *Clin Cancer Res* 2016; Silva-Santos lab; feeder-free, clinical-grade,
  NCT05001451) runs a **two-step, 2–3 week** process using an anti-CD3 agonist with IL-4/IL-15/
  IFN-γ/IL-21 followed by IL-15-driven differentiation, reaching ~2,000-fold expansion and
  producing NKp30/NKp44⁺ Vδ1 cells that persisted in vivo **"without showing signs of loss of
  function"**. **Ferry et al. (*Front Immunol* 2022, GammaDelta Therapeutics)** expand and transduce
  Vδ1 in **one step with OKT-3 + IL-15 alone**. So the field's counter-position is that TCR agonism
  is tolerable if the cytokine milieu drives differentiation correctly — the exhaustion risk is
  contingent, not absolute.
- **IL-2 is still in the medium.** 100 IU/mL IL-2 is a STAT5 signal; the design is
  STAT3-*biased*, not STAT3-only.

Mechanistic backing for preferring the STAT3 arm (imported from αβ/NK biology, plausible but not
γδ-proven):

- **IL-2 and IL-21 confer opposing differentiation programs** on CD8 T cells: IL-2 → Eomes,
  granzyme B, terminal effector, *worse* after adoptive transfer; IL-21 → L-selectin-high, less
  differentiated, *better* tumor regression (Hinrichs et al., *Blood* 2008).
- γc-cytokine/STAT mapping: **IL-2/IL-15 → STAT5** (terminal differentiation at high strength),
  **IL-21 → STAT1/STAT3 → TCF1, CD62L, CD95** (T-stem-cell-memory-like). Reviewed in
  *Cell Commun Signal* 2023, doi:10.1186/s12964-023-01354-3.
- STAT3 → hTERT transcription → telomere maintenance → the 6-week non-senescent proliferation seen
  with mbIL-21 vs mbIL-15 (Denman 2012).

---

## 5. Where his γδ approach sits among γδ manufacturing platforms

| Platform | Stimulus | Cytokines | Duration | Output | Notes |
|---|---|---|---|---|---|
| Classic pAg/ZA | zoledronate or BrHPP (**sustained TCR/pAg**) | IL-2 (± IL-15) | ~14 d | Vγ9**Vδ2** | Dose-dependent PD-1/TIM3/TIGIT/LAG3/CD57; poor metabolic fitness in TME; modest clinical results |
| **DOT** (Almeida 2016, Silva-Santos / Lymphact-Takeda) | anti-CD3 agonist, **feeder-free** | IL-4 + IL-15 + IFN-γ + IL-21 → IL-15 | 2–3 wk, 2 steps | **Vδ1**, NKp30/NKp44⁺ | ~2,000-fold; GMP bags; persists in vivo; NCT05001451 |
| **One-step CAR-Vδ1** (Ferry 2022, GammaDelta Tx) | OKT-3, αβ/CD56-depleted PBMC | **IL-15 only** | single step | Vδ1 + CAR | Standard viral transduction; no alloreactivity |
| **aAPC polyclonal** (Deniger 2014, MD Anderson) | K562 aAPC clone 4 (CD19/CD64/CD86/**4-1BBL**/mbIL15) | IL-2 **+ IL-21** (soluble) | ~3–4 wk | **polyclonal** Vδ1/Vδ2/Vδ1negVδ2neg | Proliferation required **CD137L**; in vivo potency polyclonal > Vδ1 > Vδ1negVδ2neg > Vδ2 |
| **Naeimi Kararoudi — Design A** (Portillo 2025) | **none** | **K562-mbIL21 + 4-1BBL** feeder + IL-2 | ≥5 wk | **Vδ1**-dominant | 500–26,000-fold; metabolically fit in ascites; HER2-CAR via CRISPR/AAV6 |
| **Naeimi Kararoudi — Design B** (WO2025123022A1) | **anti-CD3, ≥2 d only** | **K562.mbIL21.4-1BBL (CStX-002)** + 100 IU IL-2 | edit d14–21 | **polyclonal (Vδ1 + Vδ2)** | CD70 KO + CD70-CAR into AAVS1; Nucleofector CM-137; AAV6 MOI 75K |

His differentiator vs the field is not the CAR and not the subset — it is **replacing the
antigen-receptor engine with an mbIL-21/4-1BBL feeder engine**, imported wholesale from the NK
platform he spent years optimizing, and then exploiting that state as the **gene-editing window**.

---

## 6. Open questions worth putting to him / worth testing

1. **Is there a titration?** Anti-CD3 priming of 6 h vs 2 d vs 7 d, holding the mbIL-21 phase
   constant — fold expansion, Vδ1:Vδ2 ratio, TOX/TCF7, and *post-transfer re-expansion*. This is the
   experiment that would convert the verbal rule into data; nothing published does it.
2. **Telomere/hTERT in γδ, not NK.** Does mbIL-21 raise telomere length in expanded Vδ1/Vδ2 cells
   the way it does in NK cells? The whole "long culture is safe if STAT3-driven" argument rests on
   an NK dataset.
3. **Is TIGIT/TIM3-high after mbIL-21 exhaustion or activation?** He already owns **TIGIT-locus
   CAR knock-in** IP (TS-004607 / WO2026085461A1) on the NK side — combining TIGIT KO with the CAR
   insertion in γδ T cells is the obvious next product and would also settle the question.
4. **Vδ2 rescue.** mbIL-21 alone loses Vδ2 entirely. Is the short anti-CD3 pulse the *only* way he
   keeps polyclonality, or is there a Vδ1-TCR/Vδ2-specific agonist step?
5. **CStX-002 vs research FC21** — clinical-grade feeder supply is the practical bottleneck
   (note: the older K562-mbIL21 line has had inter-institutional licensing problems, explicitly
   cited as a motivation for competitor feeder lines such as OCI-AML3-derived "NKF",
   US 12,060,577).
6. **CD8⁺γδNKT (TS-005689)** — the NCH listing pairs "**Generation and Expansion**" in the title,
   implying a distinct culture protocol for a CD8⁺ γδ/NKT-like product. No public method yet; worth
   requesting the non-confidential summary from NCH tech transfer (licensing officer: Andrew Corris).
7. **αβ contamination / GvHD.** Portillo reports persistent low-level αβ T cells and recommends an
   αβ-depletion step; the patent relies on negative γδ selection up front. For a clinical
   allogeneic product these are not equivalent.

---

## 7. Provenance / confidence

- **Directly evidenced** (read from primary sources): all patent claim language and examples in
  §3.1; all protocol parameters in §2.1, §2.3, §3.2; the Denman 2012 numbers; the GSK3β/IL-15
  observation; the ZA-exhaustion phenotypes; the DOT/Ferry/Deniger comparators.
- **Inference (mine, flagged as such)**: the §3.3 reconciliation of Designs A and B, and the claim
  that Vδ1-dominance in Design A is a *consequence* of removing TCR agonism. Portillo et al. offer
  two alternative explanations (differential resistance to AICD/exhaustion between Vδ1 and Vδ2, or
  differential 4-1BB expression) and explicitly say follow-up is needed.
- **Not verified**: the verbal statement itself is second-hand and I found no publication or patent
  in which he states a numeric maximum TCR-stimulation duration beyond the patent's "1–7 days /
  at least 2 days" range. Treat "too long = exhausted" as his working rationale, currently
  supported by analogy (NK STAT3 data + Vδ2/ZA data) rather than by a published γδ time-course.
