# Rituximab around solid-tumour CAR-T

*B-cell depletion to limit anti-CAR (anti-idiotype) antibodies and permit repeat dosing: schedules, evidence class, and administration*

*Literature synthesis of 252 curated records (1988–2026)*

> No published solid-tumour CAR-T trial has shown that rituximab prevents anti-CAR antibodies or improves CAR-T persistence. The two CAR-T-specific schedules quoted here are investigational trial protocols, not standards of care, and the administration guidance is transferred from the prescribing information and from other indications. Nothing here is a treatment recommendation for an individual patient.

---

# Rituximab / B-cell-depletion dosing to avoid anti-CAR antibodies in solid-tumour CAR-T

Scope: humoral anti-CAR immunogenicity (anti-idiotype / anti-drug antibodies, ADA) in CAR-T therapy of
**solid tumours**. Lymphoma, leukaemia and myeloma CAR-T are used only where they supply mechanism or
assay methodology, and are explicitly flagged as such. Rituximab used as a CAR **kill switch** or as
anti-tumour/target-sensitising therapy is catalogued separately as a confusable, not as evidence.

---

## 1. Bottom line

1. **No rituximab schedule for this indication has been *published*, but two active trials specify one and
   their results are not out yet.** Targeted PubMed searching (~3,100 records, `notes/search_strategy.md`)
   found no *publication*; ClinicalTrials.gov does (full quotes and URLs in
   `notes/registry_and_unpublished_evidence.md`):
   - **Stanford, GD2-CAR T, H3K27M+ diffuse midline glioma, NCT04196413 Arm D** (recruiting): rituximab
     **750 mg/m²/day IV on days −6 and −5 for the first round, then 750 mg/m² on day −5 for subsequent
     rounds**; cyclophosphamide 500 mg/m² + fludarabine 30 mg/m² on days −4/−3/−2; GD2-CAR T ICV
     10–50 × 10⁶ cells on day 0, repeated with re-lymphodepletion. Note this is **2× the conventional
     375 mg/m² dose**, and it is repeated per cycle rather than given as a one-off induction. Arms A–C use
     no rituximab.
   - **Penn, CART-EGFR-IL13Rα2 (murine EGFR806 scFv + humanised IL13Rα2 scFv), newly diagnosed GBM,
     NCT06973096 Cohort B**: rituximab **375 mg/m²/day × 1 day** with fludarabine 30 mg/m² and
     cyclophosphamide 300 mg/m² × 3 days, before each **q6-week** repeat ICV cycle. Cohort A (single dose,
     no repeat) gets no lymphodepletion and no rituximab.
   Neither has reported immunogenicity or efficacy data. Any *efficacy* claim for rituximab in this setting
   is still extrapolation.
2. **The rationale is now documented, in the same trial that added rituximab.** Chen et al. (medRxiv 2026,
   PMID 42465905, `fulltext/chen_2026_medrxiv_anticar_dmg.pdf`) show in NCT04196413 that GD2-CAR T therapy
   induces CD4+/CD8+ anti-CAR T-cell reactivity against murine scFv and junctional epitopes plus circulating
   **human anti-CAR antibodies (HACAs)** that bind CAR-expressing cells and inhibit CAR-mediated killing;
   HACA appearance tracked with progression, and HACA level correlated inversely with CAR-T persistence.
   They state Arm-A outcomes will be compared with "patients currently being enrolled on arms delivering an
   intensified lymphodepletion regimen designed to reduce or eliminate anti-CAR immune responses" — Arm D.
   The January 2026 CIRM board presentation (`fulltext/mackall_2026_cirm_board_gd2cart.pdf`) tabulates the
   arms — anti-CAR immunity in **all** Arm-B patients (no lymphodepletion) and early, versus **many but
   late** in Arm A, with Arm C (sequential lymphodepletion) showing "lower levels but still present" — and
   concludes the target product profile "requires sequential intracerebral infusions and sequential
   lymphodepleting chemotherapy, **likely with rituximab (mirror Arm D)**".
3. **Same preprint gives the reason B-cell-malignancy CAR-T tells you nothing here**: those patients are
   already immunosuppressed and CD19/BCMA products self-deplete B and plasma cells, "limiting induction of
   anti-CAR antibody responses". Solid-tumour patients have intact humoral immunity — e.g. **95% of
   recipients** of the CLDN18.2 CAR satri-cel in gastric/GEJ cancer developed anti-CAR antibodies
   (Lancet 2025, PMID 40460847).
4. **The one in-vivo test of anti-CD20 before a CAR-T product failed to prevent anti-CAR antibodies.**
   Pampusch 2023 (PMID 36825014, non-human primate, SIV — not a tumour) gave **anti-CD20 7 mg/kg IV as a
   single dose 7 days before CAR-T infusion**. B cells were fully depleted in blood but only partially in
   lymph nodes, and **all three CAR-T-treated animals still had anti-CAR IgG at day 56**; the authors
   attribute the failure to incomplete depletion of lymphoid follicles. Pre-treatment was also associated
   with prolonged IL-6 elevation and *faster* CAR-T disappearance. This is the closest thing to direct
   evidence and it is negative for a single low pre-dose.
5. **The problem being solved is real and solid-tumour-specific.** Anti-idiotype/anti-CAR humoral responses
   have neutralised or curtailed solid-tumour CAR-T in: CAIX CAR-T in renal cell carcinoma (PMID 20889925,
   23423337), FRα CAR-T in ovarian cancer (17062687), TAG-72 CAR-T in colorectal cancer (28344808),
   mesothelin CAR-T where human anti-chimeric antibodies appeared in 8/14 patients (31420241), and most
   severely mRNA mesothelin CAR-T, where intermittent repeat dosing of a murine scFv produced **anaphylaxis
   and cardiac arrest** via IgE (24777247).
6. **The field's own B-cell-depletion attempt in a solid tumour used a CAR, not rituximab — and was
   negative**: in metastatic pancreatic cancer a CD19 CAR was co-infused with a mesothelin CAR to deplete
   B cells; B cells became undetectable by 7–10 days and stayed so for ≥28 days, but CART-Meso persistence
   did not improve at the dose tested (n = 3, PMID 32730744).
7. **If a rituximab-containing regimen is to be designed, the transferable schedules come from immune
   tolerance induction (ITI) in enzyme replacement therapy, AAV gene therapy and haemophilia** (§3), and
   from one solid-tumour precedent using cyclophosphamide rather than rituximab (§4). All are indirect.
8. **Design-side mitigation is better evidenced than immunosuppression**: humanised/fully human binders,
   linker choice, and ADA monitoring before redosing (§6).

---

## 2. Direct evidence table (solid tumour / CAR product)

| Setting | Product & dosing | ADA finding | B-cell-directed prophylaxis? | PMID |
|---|---|---|---|---|
| mRCC | CAIX CAR-T, repeated IV infusions ± IL-2 | anti-idiotype antibodies **neutralising CAR function** in most patients; also anti-vector immunity | none | 20889925, 23423337, 16648493 |
| Ovarian | FRα CAR-T, IV ± IL-2 | inhibitory serum factor in **3/6 patients tested**, blocking T-cell responses to FR+ tumour; no persistence | none | 17062687 |
| Colorectal | first-generation TAG-72 CAR-T (humanised CC49), IV or hepatic artery, up to 1e10 cells | induced **interfering antibody to the CC49 binding domain** (seen as an artefactual fall in serum TAG-72); persistence ≤14 weeks; authors recommend fully human constructs | none | 28344808 |
| Mesothelioma / pancreas / ovary | **mRNA** mesothelin CAR-T, intermittent repeat infusions | IgE anti-murine-scFv → **anaphylaxis, cardiac arrest on 3rd infusion** | none | 24777247, 24579088 |
| Mesothelioma / ovarian / pancreas | lentiviral SS1 (murine scFv) mesothelin CAR-T, single infusion ± Cy | **HACA in 8/14 patients**; fully human CAR taken forward | none | 31420241 |
| Pancreas (n = 3) | mesothelin CAR-T **co-infused with CD19 CAR-T** | B cells undetectable 7–10 d and ≥28 d, but **CART-Meso persistence not improved** | yes — CAR-mediated, not rituximab; **negative** | 32730744 |
| NHP, SIV (not tumour) | CD4-MBL-CAR/CXCR5 T cells | anti-CAR IgG in **all** animals, ADCC-competent | — | 36582226 |
| NHP, SIV (not tumour) | same CAR + **anti-CD20 7 mg/kg IV, day −7, single dose** | **anti-CAR IgG still developed in all animals**; partial LN depletion only | yes — **failed** | 36825014 |
| Gastric / GEJ | satri-cel (CLDN18.2) CAR-T, up to 3 infusions, phase 2 randomised | **anti-CAR antibodies in 95% of recipients** | none | 40460847 |
| H3K27M+ DMG | GD2-CAR T (murine 14g2a scFv), IV then sequential ICV, NCT04196413 | anti-CAR CD4/CD8 responses + **HACAs that inhibit CAR killing**; HACA inversely correlated with persistence, temporally linked to progression | **Arm D adds rituximab 750 mg/m² d−6/−5 then d−5 per round**; no results yet | 42465905 (preprint) |
| Newly diagnosed GBM | CART-EGFR-IL13Rα2 (murine EGFR806 scFv), q6-week repeat ICV cycles | not yet reported | **rituximab 375 mg/m² ×1 + Flu/Cy per cycle**, Cohort B only; no results yet | NCT06973096 |

Solid-tumour trials that depend on repeat dosing — and therefore carry the ADA risk this question is about —
are indexed under `C_solid_redosing_trials` (HER2 sarcoma up to 12 infusions, 25800760; repeated
intracerebroventricular GD2 / HER2 / B7-H3 dosing, 35130560, 39537919, 34253928, 39775044; repeated
intracavitary IL13Rα2, 28029927; hepatic-artery and intraperitoneal CEA CAR-T, 32843493, 31155611, 41760800).

---

## 3. Dosing schedules that do exist, and what they were given for

All extracted verbatim from the sources in `fulltext/` (see `notes/dosing_schedules_extracted.md`).
**Evidence class**: none of these were given to prevent anti-CAR antibodies.

| Regimen | Timing relative to antigen | Outcome | Setting (evidence class) | PMID |
|---|---|---|---|---|
| Rituximab **375 mg/m² IV weekly × 4** + methotrexate **0.4 mg/kg × 3 cycles** (with first 3 doses of antigen) + IVIG **500 mg/kg monthly** — "5-week short-course ITI" | started **at or before the first antigen exposure** | prevented/blunted anti-drug antibody; sustained tolerance | CRIM-negative infantile Pompe ERT (prophylactic ITI in humans) | 32849613, 22237443, 28814660, 23825616, 26167453 |
| Rituximab **375 mg/m² IV weekly × 3** + methylprednisolone 10 mg/kg, then **sirolimus daily**, **rituximab every 12 weeks**, IVIG monthly (IgG trough 700–1000 mg/dL) | rituximab started **~20 days before** first antigen exposure | **non-responsiveness to both capsid and transgene**, redosing possible | AAV1-GAA gene therapy, single human subject | 25541616 |
| Rituximab **20 mg/kg IV (≈375 mg/m²)** + cyclosporine A | after antibody had formed (rescue) | eradicated anti-FIX inhibitors in some animals | NHP AAV8-FIX | 22565846 |
| Anti-CD20 mAb **before vector**, ± rapamycin / anti-BAFF / anti-CD19+CD22 | **before** first exposure | prevented neutralising antibody, permitted re-administration | mouse/NHP AAV | 40057826, 38440160, 36994804, 32670285 |
| Anti-CD20 **+ rapamycin** (4 mg/kg 3×/week) with antigen | concurrent | tolerance where anti-CD20 alone was insufficient | haemophilia A inhibitors (human 2-patient + preclinical) | 31985872, 27683758, 32670285 |
| Rituximab 375 mg/m² weekly × 4 **+ bortezomib** 1.3 mg/m² days 1/4/8/11 ± MTX ± IVIG | after high titres established (rescue) | titres fell only when the **plasma-cell arm** was added | Pompe with entrenched ADA | 23060045, 27493997 |
| **Cyclophosphamide ≥ 4,000 mg/m²** | before, and murine protein started **< 90 days after** | HAMA-positivity reduced to 2/76 vs 17/27 if started > 120 days | **neuroblastoma (solid tumour), murine 3F8 antibody** | 16421906 |
| Cyclosporin A; deoxyspergualin | around repeated murine antibody dosing | suppressed HAMA, permitted repeat dosing | solid-tumour radioimmunotherapy (historical) | 3265333, 8306252, 7606728, 9815950 |
| Standard rituximab **375 mg/m² weekly × 4**; also 1 × 375 mg/m², 2 × 375 mg/m² d0/d7, 1000 mg d0/d14, 500 mg, 100 mg | — | dose determines **duration** of depletion (median B-cell return 2.5 vs 5.0 vs 6.6 months for 100 mg/m², 375 mg/m², 2 × 375 mg/m²) | pharmacology/autoimmunity | 9310469, 30109447, 24609057, 40374120, 38247568, 38595918 |

---

## 4. Timing and depth principles that any schedule must respect

- **Prophylaxis works, rescue mostly does not.** Anti-CD20 ablates a *de novo* antibody response but spares
  pre-established immunity (35015688); it blunts primary *and* secondary responses to a true neoantigen
  (bacteriophage φX174 in humans, 15636611; hapten in primates, 11161973). So rituximab must precede the
  **first** CAR-T infusion — HAMA-type primary responses appear ~2 weeks after exposure (1711007).
- **An established anti-CAR titre is made by CD20-negative long-lived plasma cells** and will not be
  reversed by rituximab: plasma cells and their antibody survive years of complete B-cell aplasia after
  CD19 CAR-T (27166358), and bortezomib only *delays* rather than eradicates inhibitor-producing cells
  (21251202). Rescue requires a plasma-cell agent (bortezomib), IgG cleavage (imlifidase, 32483358), or
  plasmapheresis (38327805, 40705999).
- **Blood depletion ≠ follicular depletion.** This is why the one CAR-T experiment failed (36825014):
  lymph-node and germinal-centre B cells persist after standard dosing (30649469, 14551029, 15838377,
  33384685, 42162633), and higher NHP doses (20–50 mg/kg, often ×3 weekly) are needed for nodal depletion.
  Type-2 anti-CD20 (obinutuzumab) depletes tissue compartments more deeply (31257724).
- **Inflammation confers resistance to anti-CD20-mediated depletion** (27265023) — directly relevant to a
  patient with bulky tumour, CRS, or IL-6 elevation.
- **Anti-CD20 alone leaves T-cell help intact**; the regimens that actually induced tolerance paired B-cell
  depletion with an mTOR inhibitor or methotrexate (32670285, 31985872, 33205401, 28562666).
- **IVIG timing matters**: IVIG given too close to rituximab can block B-cell depletion and abolish ITI
  efficacy (32681978).

---

## 5. CAR-T-specific hazards of adding rituximab

- **Do not give rituximab to a patient whose CAR-T product carries a CD20/RQR8 safety switch** — rituximab
  is the agent used to *delete* those cells (24970931, 19734426, 37086278, 33526841). This is the single most
  common source of confusion in this literature and is catalogued in `I_confusables_do_not_confuse`.
- Cy/Flu lymphodepletion already reduces B cells; regimen intensity varies (41183747), so the marginal
  benefit and the marginal toxicity of rituximab must be judged against that baseline.
- Rituximab plus corticosteroids around CAR-T is associated with **late cytopenias** (35842124).
- Prolonged B-cell depletion causes hypogammaglobulinaemia and impaired vaccine responses, requiring IgG
  monitoring/replacement (36372267, 41942445, 36906276, 34702753).
- B-cell depletion can impair vaccine-induced **CD8 T-cell** responses in a type-I-interferon-dependent
  manner (34226189) — a theoretical risk of blunting the CAR-T response itself.

---

## 6. Better-evidenced alternatives to immunosuppression

1. **Remove the immunogen**: humanised or fully human binders eliminated the ADA barrier to retreatment in
   the settings where it was formally studied (33512480, 26101914, 22127019, 41881100); framework
   engineering did the same for murine antibodies (14522015). The scFv **linker** itself is a dominant
   epitope (41253492) — a cheap design fix.
2. **Monitor before redosing.** Validated flow-cytometric and cell-based anti-CAR ADA assays exist
   (42033387, 31678267, 37983584, 41518483); the OKT3-era paradigm of screening before re-exposure
   prevented anaphylaxis (8497882, 8090628).
3. **Regional/locoregional repeat dosing** (intracerebroventricular, intrapleural, intraperitoneal,
   intra-arterial) is the delivery strategy actually being used to redose solid-tumour CAR-T
   (35130560, 39537919, 34253928, 39775044, 34266984, 32843493) — how much systemic humoral immunity
   constrains it is, to our reading, not yet reported.
4. **Cyclophosphamide** is the only agent with solid-tumour human data for suppressing an anti-murine-protein
   humoral response (16421906), and it is already part of standard lymphodepletion.

---

## 7. If a schedule must be proposed

**Preferred: copy a schedule that is actually being tested in a solid-tumour CAR-T protocol** rather than
porting one from ERT/AAV. The two options, with no outcome data yet
(`notes/registry_and_unpublished_evidence.md`):

| | Stanford NCT04196413 Arm D | Penn NCT06973096 Cohort B |
|---|---|---|
| Rituximab | 750 mg/m²/day IV, days −6 **and** −5 first round; 750 mg/m² day −5 each later round | 375 mg/m²/day × 1 day, each cycle |
| Chemo | Cy 500 + Flu 30 mg/m², days −4/−3/−2 | Cy 300 + Flu 30 mg/m² × 3 days |
| CAR-T | ICV 10–50 × 10⁶, day 0, repeated | ICV, q6 weeks |
| Logic | double the standard dose, before **every** round | standard dose, before **every** round |

Both re-dose rituximab with each CAR-T cycle rather than giving a single induction — consistent with §4:
blood depletion is easy, follicular/germinal-centre depletion is not, and repeat CAR-T exposure keeps
re-priming the response.

The generic ITI-derived design below is **hypothesis-generating** and pre-dates the trial schedules above;
it has never been tested with a CAR-T product, and the only in-vivo attempt with a single low pre-dose
failed (36825014):

- **Precondition, do not react**: rituximab **375 mg/m² IV weekly, starting ≥ 2–4 weeks before the first CAR-T
  infusion**, for ≥ 2–4 doses (the ITI/AAV templates: 32849613, 25541616) — with the explicit caveat that
  standard dosing did not clear nodal/follicular B cells in the CAR-T primate experiment.
- **Verify depth, not just blood counts**: high-sensitivity flow for residual B cells (33384685); consider
  type-2 anti-CD20 for deeper tissue depletion (31257724).
- **Add a T-help arm** (sirolimus or low-dose methotrexate) rather than relying on B-cell depletion alone
  (32670285, 31985872, 32849613).
- **Do not expect rescue**: once anti-CAR titres exist, add a plasma-cell-directed or IgG-cleaving strategy
  (23060045, 32483358) rather than more rituximab.
- **Support IgG** with monthly IVIG, timed away from rituximab dosing (32681978, 36372267).
- **Absolute contraindication**: any CD20-based safety/selection switch in the CAR construct (24970931).
- **Monitor** ADA and CAR-T persistence with a validated assay at each redose (42033387, 31678267).

---

## 7b. How the drug is given, once a protocol calls for it

Full detail in `notes/administration_protocol.md` (every block labelled LABEL / REGISTRY / LIT /
INFERENCE). The points that change what gets written on an order sheet:

- **Timing within the round**: both trial schedules put rituximab **immediately before lymphodepletion**
  (day −6/−5 or day −5) and repeat it **every** CAR-T round. Neither registry record specifies premedication,
  infusion rate, or monitoring.
- **Infusion**: IV only, never push/bolus; dilute to 1–4 mg/mL in NaCl 0.9% or D5W. First infusion 50 mg/h
  (paediatric 0.5 mg/kg/h, max 50 mg/h), +50 mg/h every 30 min to max 400 mg/h; subsequent infusions start
  at 100 mg/h. The 90-minute rapid schedule is label-sanctioned only from cycle 2, with a steroid-containing
  regimen, and not if lymphocytes ≥5,000/mm³ (17244675, 16856919).
- **Premedication**: acetaminophen + H1 antihistamine before every infusion (paediatric label: 30–60 min
  before). Adding an H2 antagonist does not help (42530421). A second-generation H1 avoids sedation
  (41989666). **The steroid question is the CAR-T-specific one**: steroids reduce IRR (37205922) but inhibit
  ADCC (38270799) and blunt CAR-T; give one only if the CAR-T protocol says so.
- **Screening**: HBsAg + anti-HBc mandatory — anti-CD20 is high-risk for HBV reactivation (25% with R-CHOP
  in HBsAg−/anti-HBc+ patients, 19075267), so past *or* chronic HBV needs antivirals during and ≥12 months
  after (32716741, 23775967). Baseline CBC and **baseline quantitative IgG** (omitted in 85% of a
  4,479-patient cohort, 30646343).
- **Reactions**: stop or slow, treat by severity, resume at ≥50% rate reduction, discontinue for grade 3–4
  (label). Anaphylaxis is rechallengeable by desensitisation, serum sickness is not (42073020) — which
  matters when the drug is needed again next round.
- **Late effects that overlap the CAR-T window**: late-onset neutropenia at median 77–102 days
  (20827108, 21560117), hypogammaglobulinaemia (23276889), PML at median 5.5 months (19264918). Fold
  prophylaxis and IgG replacement into the CAR-T programme's plan (42274870, 34923107).
- **Fasting**: **not required for the rituximab infusion** — the label imposes no NPO status, and high-TLS-risk
  patients are supposed to be aggressively hydrated. Fasting rules belong to any sedation/anaesthesia for
  reservoir placement or ICV access, per the local anaesthesia policy (28045707, 36629465, 34857683).

---

## 8. What is not known

- No solid-tumour CAR-T trial has reported an ADA-prophylaxis intervention arm; there is no dose-response,
  no timing comparison, and no persistence or efficacy endpoint for rituximab in this setting.
- Whether locoregional redosing (ICV, intrapleural) is materially affected by systemic anti-CAR antibodies.
- Whether B-cell depletion impairs CAR-T expansion or antitumour function in humans.
- Whether anti-CAR ADA in solid tumours is predominantly IgG (neutralising/ADCC) or IgE (anaphylaxis), which
  determines whether prophylaxis is a persistence question or a safety question (24777247 vs 20889925).

---

# Extracted dosing schedules (verbatim from the primary sources)

Quotations are from the full texts in `../fulltext/` unless the source is marked *(abstract only)*.
Nothing here was given to prevent anti-CAR antibodies in a solid tumour; the indication is stated for each.

---

## 1. The only anti-CD20 dosing given before a CAR-T product

**PMID 36825014** — Pampusch 2023, *Front Immunol*, SIV-infected ART-suppressed rhesus macaques,
CD4-MBL-CAR/CXCR5 T cells. Not a tumour.

> "Seven days prior to infusion of CAR-T cells, the CD20-depleted animals were treated intravenously with a
> dose of 7 mg/kg of a rhesus IgG1 recombinant Anti-CD20 (2B8R1) monoclonal antibody"

> "We chose to similarly administer a single low dose (7 mg/kg) of anti-CD20 7 days prior to CAR-T cell
> infusion in order to facilitate a temporary depletion of the B cell follicles."

Outcome — **prophylaxis failed**:

> "In the CD20-depleted animals, at 56 DPT, all three of the CAR/CXCR5-treated animals also had detectable
> levels of anti-CAR IgG antibodies in their serum … This finding suggests that the ability of the animals to
> develop antibodies to the CAR was not impeded by anti-CD20 treatment, perhaps due to the limited depletion
> of the lymphoid follicles."

Depletion depth achieved, and the doses the authors say are actually needed in primates:

> "In CD20 depleted animals, complete depletion was observed in the blood and partial depletion was observed
> in the lymph nodes nine days after administration of 7 mg/kg anti-CD20."

> "Previous primate studies used anti-CD20 antibody doses of 20-50 mg/kg, usually with multiple
> administrations, which had prolonged impacts on CD20+ cells in blood and lymphoid tissues."

> "Infusion of 1.6 or 6.4 mg/kg rituximab … resulted in over 95% depletion of B cells in peripheral blood for
> 8 days and variable CD20 depletion in lymph nodes, resulting in 34-77% depletion of lymph node B cells seen
> 2 and 4 weeks after treatment." / "Three weekly doses of 20 mg/kg rituximab were shown to significantly
> deplete B cells in the peripheral blood and lymph nodes of rhesus macaques, also resulting in decreased
> Ki67+ B cells in GCs".

Additional CAR-T-relevant harms: "The potential for an inflammatory cytokine response appears to be enhanced
with anti-CD20 antibody treatment and future studies may require CRS control strategies", and the CAR-T cells
in depleted animals "abruptly disappeared" after an early proliferative burst.

Companion paper **PMID 36582226** (same CAR, no depletion) established the ADA baseline: "All of the treated
animals developed antibodies in their serum that bound to CD4-MBL CAR/CXCR5 T cells and the majority were
capable of inducing an ADCC response", with the dominant epitopes in the CD4 domains and the CD28
transmembrane/linker region — i.e. **ADA occurs even with self-protein-based CARs**.

---

## 2. Prophylactic ITI with rituximab, given *before* first antigen exposure (Pompe ERT)

**PMID 32849613** — Desai 2020, *Front Immunol*, CRIM-negative infantile Pompe, prophylactic short-course ITI:

> "The 5-week short-course immune tolerance induction approach included four doses of weekly rituximab
> (375 mg/m², intravenously), and three cycles of low-dose methotrexate (0.4 mg/kg …)"

> "To provide passive immunity during B cell suppression, monthly IVIG at 500 mg/kg was added to the
> combination therapy during the time of B cell suppression."

> "ITI with rituximab (4 weekly doses), methotrexate (3 cycles with first 3 ERT infusions …)" — i.e. the MTX
> cycles are timed to the **first three antigen exposures**.

**PMID 22237443** (Messinger 2012, *Genet Med*) and **PMID 23825616** (Banugaria 2013) give the same protocol:
"a regimen of rituximab (four weekly doses intravenously) and methotrexate (three doses per week for three
weeks subcutaneously), with or without monthly IVIG".

**PMID 26167453** (Stenger 2015) — sibling comparison showing timing is the variable that matters:
"prophylactic ITI with rituximab, methotrexate, and IVIG was initiated at the time of first alglucosidase alfa
dose (20 mg/kg every 2 weeks)" and "Patient 2 received a five week course of prophylactic ITI with rituximab,
IVIG and methotrexate which was initiated **prior to** first dose of alglucosidase alfa".

**PMID 32681978** *(abstract only)* — IVIG given too close to rituximab can block depletion and abolish ITI
efficacy; IVIG must be timed away from the rituximab doses.

---

## 3. Rituximab before AAV exposure — the closest human template for pre-CAR prophylaxis

**PMID 25541616** — Corti 2014, *Mol Ther Methods Clin Dev*, single human subject, rAAV1-CMV-hGAA:

> "At 5.5 months of age, about 20 days before starting ERT, the patient received 375 mg/m² of rituximab and
> 10 mg/kg of methylprednisolone intravenously (premedication) weekly for 3 weeks."

> "After the Rituximab induction doses, the patient received daily oral Sirolimus (0.06–1 mg/m²/day)."

> "Once the induction dose of Rituximab was completed, the patient started receiving a monthly dose of
> 500–1,000 mg/kg of IV immunoglobulin (IVIG) … adjusted in order to maintain a trough serum IgG level of
> 700–1,000 mg/dl."

> "A 3.5 year-old Pompe disease subject … received weekly administration of 375 mg/m² of rituximab along with
> 10 mg/kg of methylprednisolone for 3 weeks prior to dosing with 5 × 10¹² vg/kg of rAAV1-CMV-hGAA. The patient
> then received daily oral administration of 0.06–1 mg/m² of Sirolimus through the study and continued B-cell
> depletion with **Rituximab every 12 weeks**."

Result: "B-cell ablation with rituximab **prior to** AAV vector exposure results in non-responsiveness to both
capsid and transgene, therefore allowing the possibility of repeat administration in the future."

**PMID 22565846** — Mingozzi 2012, NHP, anti-FIX inhibitor eradication (rescue, not prophylaxis):
"Rituximab … was given intravenously at a dose of **20 mg/kg (equivalent to ~375 mg/m²)**" combined with
cyclosporine A.

**PMID 40057826** — Doshi 2025, mouse AAV8: "anti-CD20 initiated **before** AAV8 exposure with or without
concurrent immunosuppression prevented AAV8 NAb development and permitted transgene expression with systemic
AAV8 vector re-administration"; regimen "anti-CD19 (150 μg weekly) and anti-CD22 (150 μg weekly) with either
anti-B220 (150 μg weekly) or **anti-CD20 (250 μg every 21 days)**".

**PMID 38440160** — Rana 2024: transient protocol combining **anti-CD20 (B-cell depletion) + anti-BAFF**
(to slow repopulation) ± rapamycin "100 μg (~4 mg/kg) … by oral gavage 3×/week for 5 weeks"; "A single α-CD20
treatment depleted >99% of circulating B cells by day 2", and the combination "allows for efficient
re-administration following immune cell repopulation" at 12 weeks.

**PMID 22704060** *(negative control)* — transient intensive immunosuppression (MMF-based) failed to improve
repeat AAV5 liver gene transfer in macaques.

**PMID 40705999** *(abstract only)* — clinical de-titring before AAV9 gene therapy: "11 plasma exchanges and
2 doses of rituximab" lowered anti-AAV9 titres from 1:800 into the eligibility range; both twins still had
acute hypersensitivity reactions during infusion.

---

## 4. Pairing anti-CD20 with an mTOR inhibitor (haemophilia inhibitors)

**PMID 31985872** — Doshi 2020, *J Thromb Haemost*, two paediatric patients with refractory inhibitors:

> "treated with 100 units/kg/d of recombinant FVIII, rapamycin to target trough values of 5–15 ng/mL, and
> **four weekly doses of 375 mg/m² rituximab**"

**PMID 32670285** — Biswas 2020, AAV8-coF8 mice: "anti-mCD20 (250 μg) on weeks 0 and 3 or oral rapamycin
(4 mg/kg) 3 times per week from weeks 2 through 5 post-vector administration"; the combination gave a
consistently larger reduction in inhibitor titres (3.8–8.2-fold) than anti-CD20 alone (0.43–2.2-fold).

**PMID 27683758** — Biswas 2017: "Naïve BALB/c mice were injected IV with two doses of 250 µg anti-CD20 …
three weeks apart", followed by "rapamycin (4 mg/kg, 3×/week for 4 weeks)".

---

## 5. Rescue of an *established* titre needs a plasma-cell arm

**PMID 23060045** — Banugaria 2013, *Genet Med*, Pompe with titres up to 1:204,800:

> "Cyclophosphamide (250 mg/m² i.v.) monotherapy was administered at weeks 86 and 92 of ERT, followed by
> rituximab (375 mg/m² i.v.) every week from week 92 to week 95"

> "an ITI protocol … included rituximab (375 mg/m² i.v., every week for 4 weeks) and methotrexate
> (15 mg/m² s.c.) every other week." → "Even after his B-lymphocyte CD19 count dropped from 17.9% … to 0.1%,
> antibody titers did not drop to <1:102,400."

> "Bortezomib was administered twice weekly (1.3 mg/m² i.v.) according to a standard dosing regimen
> (days 1, 4, 8, and 11; equivalent to one cycle)" → titres fell from 1:204,800 to 1:51,200 and eventually
> 1:3,200.

Consistent with **PMID 27166358** (plasma cells and their antibody survive years of complete B-cell aplasia
after CD19 CAR-T) and **PMID 21251202** (bortezomib delays but does not eradicate inhibitor-producing cells).

---

## 6. The solid-tumour precedent: cyclophosphamide, not rituximab

**PMID 16421906** *(abstract only)* — Kushner 2007, neuroblastoma, murine antibody 3F8:

> "the incidence of HAMA-positivity was significantly lower if patients received **high-dose cyclophosphamide
> (HD-Cy, ≥ 4,000 mg/m²)** before 3F8 treatment (P < 0.001). In addition, HAMA-positivity was least likely if
> 3F8 treatment was initiated **< 90 days post-HD-Cy** (2/76 compared to 3/19 first treated at 90–120 days, and
> 17/27 first treated at > 120 days)"

> "HD-Cy reliably blocks humoral responses to a murine antibody. This capacity to prevent host rejection of
> foreign or not fully humanized proteins raises the possibility of a broad role for HD-Cy in immunotherapeutic
> strategies."

Historical companions: cyclosporin A (PMID 3265333, 8306252, 10541370) and deoxyspergualin (PMID 7606728,
9815950) suppressed HAMA to permit repeated murine-protein dosing in solid tumours.

---

## 7. Timing principle: prophylaxis, never rescue

**PMID 35015688** *(abstract only)* — "None of 31 patients who had received anti-CD20 treatment within 6 months
prior to vaccination developed blocking antibodies. In contrast, patients who initiated anti-CD20 treatment
shortly after achieving a vaccine-induced antibody response tended to retain that response during treatment,
suggesting a policy of immunizing prior to treatment whenever possible." (Cohort is lymphoma; used for the
**timing principle only**.)

**PMID 15636611** *(abstract only)* — rituximab significantly decreased the primary *and* secondary human
antibody response to the neoantigen bacteriophage φX174.

**PMID 11161973** *(abstract only)* — anti-CD20 infusion inhibited hapten-induced primary **and** memory
humoral responses in primates.

**PMID 1711007** *(abstract only)* — kinetics of primary HAMA responses; the window that prophylaxis must
precede is roughly the first two weeks after exposure.

---

## 8. Dose → depth → duration of depletion (what a schedule buys you)

- **PMID 9310469** — the original IDEC-C2B8 schedule: 375 mg/m² weekly × 4.
- **PMID 30109447** — children, one dose 100 mg/m² vs one dose 375 mg/m² vs two doses 375 mg/m² (d0, d7):
  median time to B-cell reconstitution **2.5 vs 5.0 vs 6.6 months**.
- **PMID 24609057** — a single 375 mg/m² dose achieved B-cell depletion < 0.005 cells/µl in 89% by a median of
  13 days, with median time to repopulation 9.2 months.
- **PMID 40374120** — 100 mg vs 500 mg vs 1000 mg at weeks 0 and 2: "CD20+ B-cell depletion occurred
  universally by week 2, with faster reconstitution in [ultralow dose] by 26 weeks".
- **Tissue vs blood**: PMID 30649469 (incomplete lymph-node depletion after standard dosing), 14551029 and
  15838377 (NHP blood vs lymphoid tissue dose-dependence), 33384685 (high-sensitivity detection of residual
  B cells), 42162633 (depth-of-depletion paradox), **27265023 (inflammation causes resistance to
  anti-CD20-mediated depletion)**.
- **Type-2 anti-CD20**: PMID 31257724 — obinutuzumab achieves deeper tissue depletion than rituximab.
- **Cost**: PMID 36372267 (acquired B-cell deficiency / hypogammaglobulinaemia), 41942445, 36906276, 34702753
  (vaccine responses), 35842124 (late cytopenias when rituximab is used around CAR-T), 34226189 (B-cell
  depletion impairs vaccine-induced CD8 T-cell responses).

---

## 9. Hard contraindication

**PMID 24970931 / 19734426 / 37086278 / 33526841** — CD20 and RQR8 are used as **selection/suicide markers**
in engineered T cells; rituximab is the agent that *deletes* the product. Rituximab must never be given as
ADA prophylaxis to a patient whose CAR construct contains a CD20-based switch.

---

# Rituximab in solid-tumour CAR-T: trial-registry and not-yet-published evidence

Added after the PubMed-only round. PubMed indexes no *published* rituximab schedule for preventing
anti-CAR antibodies in solid-tumour CAR-T — but two active trials now build rituximab into the
conditioning regimen, and one of them has a public dose and timing. Results are unpublished
(one preprint, one funder board presentation).

Retrieved 2026-08-06. All quotes verbatim.

---

## 1. Stanford GD2-CAR T for H3K27M+ diffuse midline glioma — NCT04196413, Arm D

The only registry record giving an explicit rituximab dose/schedule around a solid-tumour CAR-T.

Source: https://clinicaltrials.gov/study/NCT04196413 (record last updated 2026-01-23; status recruiting)

Arm D description:

> "GD2CART will be administered in escalating doses on Day 0 in hospitalized subjects with either DIPG,
> spinal DMG, or high risk features. Intracerebroventricularly after administration of conditioning
> lymphodepletion chemotherapy regimen with rituximab, cyclophosphamide and fludarabine"

Intervention descriptions (Arm D):

> Rituximab — "First round: 750 mg/m2 per day IV for days -6 and -5. Subsequent rounds: 750 mg/m2 per day
> IV for day -5."
> Cyclophosphamide — "Cyclophosphamide 500 mg/m2 per day IV for days -4, -3, -2"
> Fludarabine — "Fludarabine 30 mg/m2 per day IV for days -4, -3, -2"

So, per cycle:

| Day | Arm D |
|---|---|
| −6 | rituximab 750 mg/m² IV (**first round only**) |
| −5 | rituximab 750 mg/m² IV (every round) |
| −4, −3, −2 | cyclophosphamide 500 mg/m² + fludarabine 30 mg/m² IV daily |
| 0 | GD2-CAR T ICV, 10–50 × 10⁶ cells |
| — | repeated with re-lymphodepletion each round |

Note the dose: **750 mg/m², i.e. 2× the conventional 375 mg/m² lymphoma/autoimmune dose**, given
5–6 days pre-infusion, and repeated with each dosing cycle rather than as a one-off induction.
Arms A–C of the same trial use no rituximab (Arm A single lymphodepletion + IV then ICV; Arm B ICV with
no lymphodepletion; Arm C sequential lymphodepletion + sequential ICV).

## 2. Why Arm D exists: anti-CAR immunity as the resistance mechanism (preprint, not peer reviewed)

Chen Y, Reynolds K, … Ramakrishna S, Mackall CL. *Anti-CAR Immunity Drives Acquired Therapeutic
Resistance to GD2-CAR T Cell Therapy in Diffuse Midline Glioma.* medRxiv, posted 2026-07-09.
PMID 42465905 · PMC13370534 · doi 10.64898/2026.06.25.26356492 ·
https://www.medrxiv.org/content/10.64898/2026.06.25.26356492v1
Local copy: `fulltext/chen_2026_medrxiv_anticar_dmg.pdf`

Abstract:

> "peripheral blood CD4+ and CD8+ T cells manifested anti-CAR immune reactivity targeting epitopes
> enriched within murine-derived and engineered junctional regions of the CAR construct. This was
> associated with appearance of circulating Human Anti-CAR Antibodies (HACAs) that bound cells expressing
> the GD2-CAR, as well as clonal expansion of CSF B cells which produced HACA which impeded the cytotoxic
> activity of GD2-CAR T cells. In several cases, appearance of circulating HACA temporally correlated with
> disease progression … levels of circulating HACA inversely correlated with circulating CAR T cell
> persistence."

Discussion — the forward-looking statement that Arm D is the test of the hypothesis:

> "We anticipate that additional evidence to confirm the role of anti-CAR responses in therapeutic
> resistance will be gleaned by comparing outcomes from patients treated on Arm A to patients currently
> being enrolled on arms delivering an intensified lymphodepletion regimen designed to reduce or eliminate
> anti-CAR immune responses."

The preprint does not itself name rituximab; the drug and schedule come from the registry record (§1)
and the funder presentation (§3).

Why solid tumours specifically (same discussion):

> "Most patients who have received investigational and commercial CAR T cells to date have been treated for
> refractory B cell and plasma cell malignancies and therefore were highly immunosuppressed at the time CAR
> T cells were administered. Further, all commercial CAR T cells today target CD19 or BCMA and thus
> eradicate B and plasma cells respectively, limiting induction of anti-CAR antibody responses."

i.e. the reason lymphoma/leukaemia/myeloma CAR-T experience is *not* transferable is that those products
are self-B-cell-depleting. This is the mechanistic justification for the scope exclusion used in this
collection.

Corroborating solid-tumour datapoint cited there: in the satri-cel (CLDN18.2) gastric/GEJ phase 2
(CT041-ST-01, Lancet 2025;405:2049–60, PMID 40460847), **95% of CAR-T recipients developed anti-CAR
antibodies**.

## 3. Interim arm-by-arm comparison, including Arm D — CIRM board presentation, January 2026

Mackall CL. *GD2-CAR T Cells for Diffuse Midline Gliomas*, CIRM Board Meeting, January 2026 (CLIN2-12595).
https://www.cirm.ca.gov/wp-content/uploads/2026/01/7b.-20290129-Closer-to-Cures-Presentation.pdf
Local copy: `fulltext/mackall_2026_cirm_board_gd2cart.pdf`

Slide table (transcribed):

| Arm | Regimen | Outcome | CAR persistence | Anti-CAR immunity |
|---|---|---|---|---|
| A (n=13) | lymphodepletion ×1, IV ×1, sequential ICV | median OS 20.6 mo, sustained benefit; dose-limiting CRS | greater persistence correlates with better outcomes | "Many patients, occur late" |
| B (n=18) | no lymphodepletion, sequential ICV | median OS 14.8 mo, transient benefit | "Very poor CAR persistence" | "All patients, occur early" |
| C (n=11) | sequential lymphodepletion, sequential ICV | median OS not reached | "Better CAR persistence" | "Preliminary data shows lower levels but still present" |
| D (now enrolling) | **sequential lymphodepletion + rituximab**, sequential ICV | too early | pending | pending |

Conclusion slide:

> "We have learned that the target product profile requires sequential intracerebral infusions and
> sequential lymphodepleting chemotherapy, likely with rituximab (mirror Arm D)."

This is the strongest statement available that a rituximab-containing regimen is the intended
solid-tumour CAR-T schedule — but note it is a funder board slide, arms are non-randomised and
sequentially enrolled, and no Arm D immunogenicity or efficacy data exist yet.

Related conference record (data overlapping the preprint): Chen Y et al., *Longitudinal single-cell atlas
of GD2-CAR T cell therapy in H3K27M-mutant diffuse midline glioma identifies humoral and cellular anti-CAR
immunity*, AACR 2026.

## 4. Penn CART-EGFR-IL13Rα2 in newly diagnosed GBM — NCT06973096, Cohort B

Source: https://clinicaltrials.gov/study/NCT06973096 (phase 1, started 2025-07-18, active not recruiting)

> Cohort B (Repeat Cycles Following Lymphodepletion): "CART-EGFR-IL13Ra2 cells will be administered via
> intracerebroventricular delivery in q6 week cycles of treatment, following lymphodepletion with
> fludarabine, cyclophosphamide, and rituximab."

Interventions:

> "Rituximab or Rituximab biosimilar — 375 mg/m2/day x 1 day"
> "Fludarabine: 30mg/m2/day x 3 days; Cyclophosphamide: 300mg/m2/day x 3 days"

Product (relevant to why ADA is expected):

> "autologous T cells transduced with a bicistronic lentiviral vector containing a murine scFv targeting
> EGFR epitope 806 and a humanized scFv targeting IL13Ra2"

So Penn's schedule is **rituximab 375 mg/m² × 1 dose per cycle**, with Flu 30 / Cy 300 mg/m² × 3 days,
before each q6-week ICV redose — half the Stanford dose, single administration, but repeated per cycle.
Cohort A (single fixed dose, no repeat) receives no lymphodepletion and no rituximab, so the rituximab is
tied specifically to the repeat-dosing cohort. The registry record does not state the rationale in words.

Predecessor trials, for contrast — no rituximab, single ICV dose, no lymphodepletion:
- NCT05168423 (recurrent GBM, phase 1; published Bagley et al., Nat Med 2025, doi 10.1038/s41591-025-03745-0;
  ASCO 2025 abstract JCO 43:16_suppl 102; ASCO 2026 OS update JCO 44:16_suppl 2013).
- NCT07209241 (phase 1b, recurrent GBM, three dosing approaches incl. repeat dosing) — registry record
  lists no rituximab as of retrieval.

## 5. What is *not* there

- **No B7-H3 CAR-T trial at the University of Pennsylvania.** Searched ClinicalTrials.gov by lead sponsor
  (53 Penn CAR-T studies, none B7-H3/CD276), by intervention (20 B7-H3 CAR-T studies: St. Jude, Stanford,
  Seattle Children's, MacroGenics, PersonGen, Zhejiang, Tiantan, Children's National, Tcelltech,
  BrainChild Bio), and by Philadelphia location. The only B7-H3 CAR-T with a Philadelphia site is
  **BrainChild Bio's BCB-276 (NCT07680439, "Illuminate")**, a phase 2 DIPG study with CHOP as a site:
  up to 15 intraventricular doses q14 days, **no lymphodepletion and no rituximab** in the record.
  Majzner's B7-H3.CD28Z.CART trials (NCT07358260, NCT07390539) are Dana-Farber/Boston Children's, Flu/Cy
  only. Seattle's BrainChild-03 (NCT04185038; PMID 39775044, 36259971) gives repeated ICV B7-H3 CAR-T
  **without** lymphodepletion and reports no rituximab.
- **No published Arm D or Cohort B results** for either rituximab-containing regimen.
- No randomised comparison of rituximab vs no rituximab in any CAR-T setting for ADA prevention.

---

# Giving rituximab around CAR-T: dose, timing, premedication, monitoring, and bedside practicalities

Companion to `REPORT.md`. `REPORT.md` answers *whether* to give rituximab for anti-CAR immunity (answer:
unproven, two trials are testing it). This note answers *how the drug is actually given* once a protocol
calls for it.

**Evidence status of each block below is labelled.** Nothing here is a substitute for the treating
protocol: the two solid-tumour CAR-T regimens are investigational, and no anti-CAR-prophylaxis outcome
data exist for either.

| Label | Meaning |
|---|---|
| **[LABEL]** | US prescribing information, Rituxan IV, label effective 2025-01-06 (openFDA `drug/label`). Established. |
| **[REGISTRY]** | Verbatim from the ClinicalTrials.gov record. Investigational, no outcome data. |
| **[LIT]** | Peer-reviewed evidence, cited by PMID; strength varies and is stated. |
| **[INFERENCE]** | Our reasoning, not a sourced recommendation. |

---

## 1. Dose and timing

### 1.1 The two solid-tumour CAR-T schedules **[REGISTRY]**

|  | Stanford NCT04196413 Arm D (GD2 CAR-T, H3K27M+ DMG) | Penn NCT06973096 Cohort B (CART-EGFR-IL13Rα2, ndGBM) |
|---|---|---|
| Rituximab | **750 mg/m²/day IV on day −6 *and* day −5** for the first round; **750 mg/m²/day IV on day −5** for each subsequent round | **375 mg/m²/day IV × 1 day** (rituximab or biosimilar), before each cycle |
| Lymphodepletion | cyclophosphamide 500 + fludarabine 30 mg/m²/day, days −4, −3, −2 | cyclophosphamide 300 + fludarabine 30 mg/m²/day × 3 days |
| CAR-T | intracerebroventricular, day 0, repeated rounds | intracerebroventricular, q6-week cycles |
| Design logic | ~2× the standard single dose, split over 2 days, **1 day before lymphodepletion starts**, repeated every round | standard single dose, repeated every cycle |

Both put rituximab **immediately before lymphodepletion, i.e. 5–6 days before the CAR-T infusion**, and
repeat it with every CAR-T round rather than giving a one-off induction. Neither registry record specifies
premedication, infusion rate, or monitoring — those come from the treating protocol and the label.

### 1.2 Reference doses that anchor those numbers **[LABEL]** / **[LIT]**

- 375 mg/m² IV is the label dose for B-cell NHL (adult and paediatric ≥6 months) and the GPA/MPA induction
  dose; it comes from the pivotal 375 mg/m² weekly × 4 trial (9310469) **[LABEL]**.
- CLL uses 375 mg/m² cycle 1 then **500 mg/m² cycles 2–6**; RA and PV use **flat 1,000 mg × 2, 2 weeks
  apart** — so a >375 mg/m² dose is not itself unusual **[LABEL]**.
- Dose sets the **duration** of depletion more than the depth of blood depletion: median B-cell return
  ~2.5 / 5.0 / 6.6 months after 100 mg/m², 375 mg/m², and 2 × 375 mg/m² (see `REPORT.md` §3).
- Exposure is not fixed by BSA: clearance rises with proteinuria and with anti-rituximab antibodies
  (36420256), and anti-drug antibodies shorten depletion (58.5 vs 163 days in children, 42481732; 42340364)
  **[LIT]**.
- Subcutaneous rituximab (1,400 mg with rHuPH20) is bioequivalent-by-design in lymphoma (24002601, 30744432)
  but **is label-restricted to patients who have already tolerated a full IV dose**, and neither CAR-T
  protocol uses it **[LABEL]**.
- Biosimilars are explicitly permitted in NCT06973096; switching studies show no consistent immunogenicity
  or efficacy penalty (29500555) **[LIT]**.

### 1.3 Interaction with the CAR-T timeline **[INFERENCE]**

- Rituximab is given **before** Cy/Flu in both protocols. Cy/Flu itself depletes B cells, so the marginal
  benefit and marginal toxicity of rituximab is judged against that baseline (see `REPORT.md` §5).
- Fludarabine exposure drives CAR-T expansion and outcome, and is under-dosed in young children by fixed
  mg/m² dosing (40148484, 38191740, 41471106, 40609087) — adding rituximab does not change that, but it
  does add a day to the pre-infusion window in which the lymphodepletion schedule must not slip.
- The prophylaxis→rescue asymmetry (`REPORT.md` §4) means a **missed or delayed** pre-round rituximab dose
  cannot be made up after the CAR-T infusion.

---

## 2. Preparation and infusion **[LABEL]**

- **IV infusion only. Never IV push or bolus.** Administer only where severe infusion reactions can be
  managed.
- Dilute to **1–4 mg/mL** in 0.9% NaCl or 5% dextrose. Do not mix with other drugs. Diluted solution:
  24 h at 2–8 °C (plus a further 24 h at room temperature shown stable; refrigerate because there is no
  preservative). Inspect — should be clear and colourless.
- **First infusion (adult):** start **50 mg/h**; if no toxicity, increase by 50 mg/h every 30 min to a
  maximum of **400 mg/h**.
- **First infusion (paediatric mature B-cell NHL/B-AL):** start **0.5 mg/kg/h (max 50 mg/h)**; increase by
  0.5 mg/kg/h every 30 min to max 400 mg/h.
- **Subsequent infusions (adult):** start **100 mg/h**; increase by 100 mg/h every 30 min to max 400 mg/h.
  Paediatric: start 1 mg/kg/h (max 50 mg/h), increase by 1 mg/kg/h every 30 min.
- **90-minute rapid infusion** (20% of the dose in the first 30 min, remaining 80% over 60 min) is a label
  option **from cycle 2 onward**, only if no grade 3–4 infusion reaction in cycle 1 and only with a
  glucocorticoid-containing regimen. **Excluded:** clinically significant cardiovascular disease, or
  circulating lymphocytes ≥5,000/mm³.
- Rapid-infusion safety data: 90 min in 206 patients with no grade 3–4 reactions (17244675), 319 infusions
  with *and without* steroids with no grade 3–4 events (16856919), and 60-min infusions in 105 second-and-later
  doses (19220420) **[LIT]**.
- **[INFERENCE]** In a repeat-cycle CAR-T protocol, every rituximab dose after the first is a "subsequent
  infusion", so the faster start rate applies — but the 90-minute option assumes concurrent steroids, which
  is exactly what §3 says to think twice about here.

---

## 3. Premedication

**[LABEL]** Premedicate with **acetaminophen/paracetamol and an antihistamine before *every* infusion**.
For paediatric mature B-cell NHL/B-AL the label specifies acetaminophen + an H1 antihistamine
(diphenhydramine or equivalent) **30–60 min before** each infusion. A glucocorticoid is label-recommended
only for the autoimmune indications (methylprednisolone 100 mg IV or equivalent 30 min pre-dose for
RA/GPA/MPA/PV) and, for lymphoma, as the chemotherapy's own steroid when using the 90-minute rate.

**[LIT]** What the premedication evidence supports:

| Component | Evidence |
|---|---|
| Acetaminophen + H1 antihistamine | Standard of care; label-mandated. Most reactions occur 30–120 min into the first infusion (label; 42530421 observed most IRR at 30–60 min). |
| Second-generation H1 (e.g. bepotastine) instead of diphenhydramine/hydroxyzine | Randomised phase II: grade ≥2 IRR 32% vs 52% and less drowsiness, not significant at n=40 (41989666). Reasonable when sedation is undesirable. |
| Adding an **H2** antagonist | No benefit: IRR 38% vs 36.5%, no difference in grade 3–4 (42530421, n=299). |
| Corticosteroid premedication | Reduces IRR (prednisone pretreatment 15.9% vs 43.2% in DLBCL, 37205922); oral prednisolone 50 mg ≈ IV methylprednisolone 50 mg (41572843, 2,253 infusions). But rapid infusion is safe *without* steroids (16856919) and steroid necessity is being re-examined (41789935). |

**Corticosteroids are the one premedication decision that is CAR-T-specific.** Steroids inhibit ADCC and are
argued to belong at the first dose only for ADCC-dependent mAbs (38270799) **[LIT]**; separately, steroids
blunt CAR-T expansion and function and are the treatment for CRS/ICANS rather than a routine co-medication
(42274870, `REPORT.md` §5, where rituximab + steroids around CAR-T is linked to late cytopenias). Rituximab
here is given days **before** the CAR-T infusion, so a single pre-infusion steroid dose is
pharmacodynamically distant from the cells — but this is **[INFERENCE]**, and the decision belongs to the
CAR-T protocol, not to the infusion nurse's standing premedication order.

---

## 4. Before the first dose: screening and baseline labs **[LABEL]** + **[LIT]**

| Test | Why |
|---|---|
| **HBsAg + anti-HBc (add anti-HBs)** | Label-mandated before any rituximab dose. Anti-CD20 is a **high-risk** therapy for HBV reactivation: 25% reactivation with R-CHOP in HBsAg−/anti-HBc+ DLBCL vs 0% with CHOP, including a hepatic death (19075267). ASCO: chronic **or past** HBV + anti-CD20 → antiviral prophylaxis during and for **≥12 months after** therapy, with HBV-expert co-management (32716741, 25964247, 28219691). Entecavir prophylaxis cut reactivation 17.9%→2.4% in resolved HBV, and an undetectable baseline HBV DNA is **not** protective (23775967). Reactivation has been reported up to 24 months after therapy. |
| **CBC with differential and platelets** | Label-mandated pre-first-dose; then before each course (monotherapy) or weekly-to-monthly with chemotherapy, more often if cytopenic. Continue after the last dose until cytopenias resolve. |
| **Baseline quantitative IgG (± IgA/IgM) and B-cell flow** | 85% of a 4,479-patient cohort had **no** pre-rituximab immunoglobulin measurement, and severe infections rose 17.2%→21.7% (30646343); baseline + serial IgG and B-cell counts are the recommended monitoring (36706910). Also the only way to interpret post-CAR-T hypogammaglobulinaemia (34757064). |
| **Renal function, electrolytes, phosphate, uric acid, LDH; hepatitis C and HIV per CAR-T program** | TLS and renal toxicity are label warnings; CAR-T best-practice screening panels (34923107, 31753925). |
| **Anti-CAR ADA baseline, and confirmation of the CAR construct** | see §7. |

---

## 5. During and immediately after the infusion

**[LABEL]** Infusion-related reactions are the boxed warning: fatal reactions have occurred within 24 h,
**~80% with the first infusion**, severe reactions typically **30–120 min** into it. Manifestations include
urticaria, hypotension, angioedema, hypoxia, bronchospasm, pulmonary infiltrates, ARDS, MI, ventricular
fibrillation, cardiogenic shock, anaphylactoid events, death.

Management, per label:

1. **Interrupt or slow the infusion** for any infusion-related reaction.
2. Institute medical management as needed — **glucocorticoids, epinephrine, bronchodilators, oxygen**.
3. On symptom resolution, **resume at ≥50% rate reduction** (label also phrases this as one-half the
   previous rate).
4. **Temporarily or permanently discontinue** depending on severity and interventions required; discontinue
   for severe (grade 3–4) reactions and for serious/life-threatening arrhythmias.
5. Monitor closely, with cardiac monitoring during and after infusion, in: pre-existing cardiac or pulmonary
   disease, prior cardiopulmonary reactions, history of arrhythmia/angina, and circulating malignant cells
   ≥25,000/mm³.

**[LIT]** Practical additions:

- **Cytokine-release-type reactions and true (IgE) hypersensitivity are clinically indistinguishable at the
  bedside** but differ in mechanism and in whether rechallenge is safe (20350882, 31447561, 38452439); the
  distinction is made retrospectively, so treat by severity in the moment.
- **Anaphylaxis is rechallengeable via desensitisation; serum sickness is not.** In 1,534 paediatric
  infusions: 7 rituximab-induced serum sickness (fever + rash + arthralgia 1–30 days later, raised CRP/ESR,
  low complement) and 7 anaphylaxis; 5/7 anaphylaxis patients were successfully re-dosed under
  desensitisation, whereas RISS recurred severely (42073020). Adult desensitisation protocols: 46 procedures
  in 11 patients without anaphylaxis (42279029); paediatric workup framework in 41937341.
- **[INFERENCE]** In a repeat-cycle CAR-T protocol this matters more than usual: a reaction that closes the
  door on rituximab closes it on **every future round**, so grade the event carefully and involve
  allergy/immunology early rather than abandoning the drug.

**[LABEL]** Also mid-to-late: severe mucocutaneous reactions (including SJS/TEN, onset as early as day 1 →
discontinue permanently), TLS within **12–24 h** of the first infusion in high-burden disease (give
aggressive IV hydration + anti-hyperuricaemic therapy, correct electrolytes, monitor renal function and
fluid balance, dialyse if needed; 21561350), renal toxicity (discontinue for rising creatinine or oliguria),
and bowel obstruction/perforation with chemotherapy (evaluate abdominal pain or repeated vomiting).

---

## 6. After the dose: infection prophylaxis, immune reconstitution, vaccines

**[LABEL]**

- PJP (Pneumocystis) **and herpesvirus** prophylaxis is label-recommended in CLL during treatment and for up
  to 12 months after; PJP prophylaxis for GPA/MPA during and for ≥6 months after the last dose.
- Serious bacterial, fungal, and new or reactivated viral infection (CMV, HSV, VZV, parvovirus B19, WNV,
  HBV, HCV) can occur during and after therapy; infections have been reported with hypogammaglobulinaemia
  persisting >11 months. Withhold rituximab for serious infection; avoid in severe active infection.
- **Live viral vaccines are not recommended before or during treatment**; bring immunisations up to date
  beforehand where possible.

**[LIT]**

- Post-CAR-T infection prevention is a structured, risk-adapted programme in its own right — antiviral and
  PJP prophylaxis, selective antibacterial/antifungal cover during prolonged cytopenia, IgG replacement,
  and vaccination timed to immune recovery (42274870, 34923107, 31753925). Rituximab should be layered into
  **that** programme, not prescribed with a separate ad-hoc prophylaxis plan.
- **Hypogammaglobulinaemia:** 39% developed low IgG after rituximab and 6.6% needed IVIG for recurrent
  sinopulmonary infection, worse with maintenance dosing (23276889, 30646343). CAR-T-specific thresholds and
  duration in 34757064; IgG-replacement practice is extrapolated from primary immunodeficiency, not
  CAR-T-derived (31416717). IVIG timing must be kept away from rituximab dosing (`REPORT.md` §4).
- **Late-onset neutropenia:** grade 3–4 neutropenia weeks to months later — incidence 3–27%, median onset
  77 days (range 42–153) with infection in most (20827108); median 102 days in rheumatic disease, coinciding
  with the depletion window, 7/11 hospitalised with infection (21560117). Review 36706910. **[INFERENCE]**
  This overlaps exactly with the post-CAR-T cytopenia window, so a late neutropenia will be attributable to
  either agent; keeping counts is the only way to tell.
- **PML:** 57 rituximab-associated cases, median 5.5 months after the last dose, 90% fatal (19264918).
  New neurological signs in a CNS CAR-T patient have many likelier causes (§7), but PML belongs on the list.
- **Vaccines:** anti-CD20 blunts responses to tetanus, pneumococcal, neoantigen (KLH) and mRNA vaccines
  (32727835, 34514436); revaccinate after CAR-T or B-cell-depleting therapy per ASCO (38498792); CAR-T
  recipients lose seroprotection for specific pathogens (33914708). Vaccinate **before** depletion where the
  schedule allows.

---

## 7. CAR-T-specific cautions

- **Absolute contraindication: a CD20 or RQR8 safety/selection switch in the CAR construct.** Rituximab is
  the agent used to *delete* those cells. Confirm the construct before writing the order
  (`REPORT.md` §5, `I_confusables_do_not_confuse`).
- Anti-CAR ADA prophylaxis with rituximab has **no** outcome data in solid-tumour CAR-T; the one in-vivo
  attempt (single 7 mg/kg dose 7 days pre-infusion in macaques) failed to prevent anti-CAR IgG
  (`REPORT.md` §2).
- Rituximab does not reverse an established titre — that is plasma-cell-mediated (`REPORT.md` §4).
- B-cell depletion could in principle blunt the CAR-T response itself (type-I-IFN-dependent effects on CD8
  priming, `REPORT.md` §5); unresolved in humans.
- **New neurology after an ICV round is usually not rituximab.** TIAN (tumour inflammation-associated
  neurotoxicity) occurred in 16/21 children and 32% of infusions after intraventricular B7-H3 CAR-T, mostly
  grade 1–2, median resolution <24 h, one requiring CSF diversion (41798119); ICANS-type toxicity managed
  with dexamethasone and anakinra was seen with the intrathecal CART-EGFR-IL13Rα2 product used in
  NCT06973096 (38480922). Grade CRS/ICANS by ASTCT consensus (30592986).
- Locoregional delivery had ~61% fewer grade ≥3 adverse events than IV delivery in high-grade glioma
  (41895715); ICV-specific procedural AEs are mainly headache, nausea, vomiting (40282439).
- **[INFERENCE]** Rituximab does not meaningfully enter the CSF, and the CNS behaves as a B-cell sanctuary
  even during full peripheral depletion (42211720). A systemic dose given for systemic anti-CAR antibody
  prophylaxis should not be expected to deplete intrathecal B cells.

---

## 8. Fasting, hydration, and other bedside practicalities

- **Rituximab itself does not require fasting.** The label specifies no NPO status, no food-effect
  restriction, and no dietary requirement — it is an IV monoclonal antibody. Patients can eat and drink
  before and during the infusion **[LABEL]**. Nausea/vomiting risk around the dose comes from the
  co-administered cyclophosphamide/fludarabine, not from rituximab.
- **Fasting belongs to the procedure, not the drug.** If a round involves sedation or general anaesthesia —
  Ommaya/reservoir placement, some ICV infusions, imaging under anaesthesia — the anaesthesia service's
  fasting rule applies on that day. Published guidance for orientation only, **the institutional
  anaesthesia policy governs**: ASA 2017 (2 h clear liquids, 4 h breast milk, 6 h light meal, 8 h
  fried/fatty meal or solids; 28045707) with the 2023 modular update on carbohydrate-containing clear
  liquids, chewing gum, and paediatric clear-liquid duration (36629465); ESAIC 2022 paediatric (clear fluids
  to **1 h**, breast milk to 3 h, gastric ultrasound as an adjunct; 34857683); ESA 2011 (21712716)
  **[LIT]**. Do not translate these into a fasting order for the rituximab infusion itself **[INFERENCE]**.
- **Hydration is the opposite requirement:** the label calls for *aggressive* IV hydration plus
  anti-hyperuricaemic therapy in patients at high TLS risk — which argues against casual NPO orders on
  rituximab day **[LABEL]** **[INFERENCE]**.
- **Sedating premedication:** diphenhydramine/hydroxyzine cause drowsiness; a second-generation H1 avoids
  it (41989666). Relevant if the same day includes a neurological examination or a procedure.
- **Time budget:** a first 375 mg/m² infusion escalating from 50 mg/h takes roughly 4–6 h plus premedication
  and observation; the 90-minute schedule (cycle 2 onward, steroid-containing regimens, no prior grade 3–4
  IRR) is the label-sanctioned way to shorten it **[LABEL]** **[INFERENCE]**. Schedule accordingly on a day
  that also includes lymphodepletion or a procedure.
- **Chair/observation:** most reactions occur 30–120 min into the first infusion (label; 42530421), so the
  first dose of a course is the one requiring full monitoring capability, not the repeats.

---

## 9. Round checklist

**Before the round**
1. Confirm the CAR construct has **no CD20/RQR8 switch**.
2. HBsAg, anti-HBc, anti-HBs; start antivirals and involve hepatology if either is positive (continue ≥12
   months after the last dose).
3. CBC + differential + platelets, renal/liver panel, electrolytes, phosphate, uric acid, LDH; baseline
   quantitative IgG and B-cell flow.
4. Vaccinations up to date; no live vaccines.
5. TLS risk assessed; hydration and urate-lowering therapy ordered if high risk.
6. Baseline anti-CAR ADA sample per protocol.
7. Confirm rituximab day relative to Cy/Flu day −4 and CAR-T day 0 (day −6/−5 or day −5 per protocol),
   and that no procedure/anaesthesia conflicts with the infusion window.

**Day of infusion**
8. Acetaminophen + H1 antihistamine 30–60 min before; steroid **only** if the CAR-T protocol says so.
9. Dilute to 1–4 mg/mL in NaCl 0.9% or D5W; IV infusion only, no push/bolus.
10. First infusion 50 mg/h (paediatric 0.5 mg/kg/h, max 50 mg/h), escalate every 30 min to max 400 mg/h;
    subsequent infusions start 100 mg/h (paediatric 1 mg/kg/h).
11. No fasting for the infusion; encourage oral intake unless a procedure requires NPO.
12. For any reaction: stop or slow, treat by severity (steroid/epinephrine/bronchodilator/O₂), resume at
    ≤50% of the previous rate after resolution, discontinue for grade 3–4.

**After**
13. Serial CBC through the cytopenia window; consider late-onset neutropenia at 6 weeks–5 months.
14. Serial IgG; IVIG per protocol, timed away from rituximab.
15. PJP/antiviral prophylaxis integrated with the CAR-T program's plan, not a parallel one.
16. Monitor HBV, and keep PML on the differential for new neurology alongside TIAN/ICANS and progression.
17. Anti-CAR ADA and CAR-T persistence at each redose.

---

## 10. Sources

Label: openFDA `drug/label`, Rituxan (rituximab) IV, effective 2025-01-06 — sections 2.1 (important dosing
information, infusion rates), 2.2–2.7 (indication doses), 2.8 (premedication and prophylaxis), 2.9
(administration and storage), boxed warning, 5.1–5.11.

Registry: ClinicalTrials.gov NCT04196413 (Arm D) and NCT06973096 (Cohort B), quoted in
`notes/registry_and_unpublished_evidence.md`.

Literature: `index.tsv` categories `J_admin_premedication_infusion_reactions`,
`K_admin_screening_prophylaxis`, `L_admin_dose_route_pk`, `M_admin_cart_context`,
`N_admin_fasting_procedure`.

---

# Search strategy, screening, and inclusion rules

Database: PubMed/Europe PMC via NCBI E-utilities (esearch/esummary/efetch), searched 2026-08-06.
**3,107 unique records** were retrieved across 49 queries in 5 rounds and screened on title/abstract;
185 were curated into `../index.tsv`; 101 open-access full texts were downloaded into `../fulltext/`.

## Inclusion rules

Included as **direct evidence** only if the record reports humoral anti-CAR / anti-idiotype / anti-drug
antibodies (or an intervention against them) in engineered T cells used **outside** B-cell malignancy —
solid tumours preferentially, plus the SIV/HIV CAR-T primate work because it is the only setting where
anti-CD20 was actually given before a CAR product.

Included as **indirect/contextual**, always labelled: AAV and other gene-therapy prophylaxis; enzyme
replacement and haemophilia immune tolerance induction; rituximab pharmacology; historical HAMA suppression
in solid tumours; ADA assays and regulatory guidance.

Retained with an explicit `MECHANISM ONLY` flag: a small number of lymphoma/leukaemia/myeloma CAR-T papers
that supply transferable biology unavailable elsewhere (first human demonstration of anti-transgene
rejection; plasma-cell survival during B-cell aplasia; ADA assay validation; fully human binder redesign
motivated by ADA-blocked retreatment).

## Explicit exclusions

- CAR-T for lymphoma, leukaemia, myeloma, or other B-cell malignancies as a source of *conclusions*.
- Rituximab as anti-tumour therapy, or to sensitise/upregulate a target on tumour cells.
- Rituximab as a CAR **safety/suicide switch** (CD20, RQR8, QBEnd10) — collected separately in
  `I_confusables_do_not_confuse` because it is the dominant false-positive in every query combining
  "rituximab" with "chimeric antigen receptor", and because it is a contraindication rather than a therapy.
- Autoimmune-disease CD19 CAR-T, anti-CD20 vaccine-response studies, and generic HAMA literature, except
  where used purely for B-cell-depletion timing/depth principles.

## Notable zero-hit queries (evidence of absence, within PubMed indexing)

- `t7_rituximab_prior_cellular_therapy` — rituximab given *prior to* adoptive cell therapy for
  immunogenicity/anti-CAR/anti-drug-antibody purposes: **0 records**.
- `t10_second_infusion_solid_tumor_outcome` — loss of expansion after a second/subsequent infusion in solid
  tumours, as an indexed phrase: **0 records**.

These are the two searches that would have surfaced a rituximab-plus-solid-tumour-CAR-T prophylaxis protocol
if one were indexed. Absence in PubMed does not exclude unindexed trial protocols, conference abstracts, or
ClinicalTrials.gov records, which were not exhaustively searched.

## Screening notes

Automated keyword scoring was used for triage only; it over-ranked records where "CAR", "antibody" and
"rituximab" co-occur incidentally (autoimmunity, vasculitis, vaccine, and lymphoma literature), so every
curated record was confirmed by reading its title and abstract, and dose/schedule claims were taken from
full text where available (`dosing_schedules_extracted.md`).

## Queries

### Round 1

- `q1_car_immunogenicity`
  ```
  ("chimeric antigen receptor" OR "CAR-T" OR "CAR T") AND (immunogenicity OR "anti-drug antibod*" OR "anti-CAR antibod*" OR "anti-idiotype" OR "anti-idiotypic" OR "neutralizing antibod*" OR "humoral immune response" OR HAMA)
  ```
- `q2_car_rituximab_prevent`
  ```
  ("chimeric antigen receptor" OR "CAR-T") AND rituximab AND (immunogenicity OR "anti-drug antibod*" OR "anti-CAR" OR "B cell depletion" OR prophyla* OR tolerance)
  ```
- `q3_car_redosing_solid`
  ```
  ("chimeric antigen receptor") AND ("solid tumor" OR "solid tumour") AND (redosing OR "repeat infusion" OR "repeated infusions" OR reinfusion OR "multiple doses")
  ```
- `q4_immune_tolerance_induction_rituximab`
  ```
  rituximab AND ("immune tolerance induction" OR "antibody formation" OR "inhibitor development" OR "anti-drug antibod*") AND (methotrexate OR IVIG OR "intravenous immunoglobulin" OR sirolimus OR bortezomib OR cyclophosphamide)
  ```
- `q5_aav_gene_therapy_rituximab`
  ```
  ("gene therapy" OR "AAV" OR "adeno-associated virus") AND rituximab AND ("neutralizing antibod*" OR immunosuppress* OR "antibody response" OR prophylaxis)
  ```
- `q6_cd20_safety_switch`
  ```
  ("chimeric antigen receptor") AND (rituximab OR CD20) AND ("safety switch" OR "suicide gene" OR RQR8 OR "elimination marker")
  ```
- `q7_scfv_humanization_car`
  ```
  ("chimeric antigen receptor") AND ("murine scFv" OR humanized OR humanization OR "fully human") AND (immunogenicity OR "anti-CAR" OR rejection OR "transgene product")
  ```

### Round 2

- `a_anticar_humoral`
  ```
  (("chimeric antigen receptor" OR "CAR T" OR "CAR-T" OR "engineered T cell*" OR "TCR-T" OR "transgenic TCR") AND ("anti-CAR antibod*" OR "anti-CAR immune" OR "anti-idiotyp*" OR "human anti-mouse antibod*" OR HAMA OR "antibody against the CAR" OR "antibodies against the transgene" OR "transgene immunogenicity" OR "anti-transgene immune response" OR "host immune response against" OR "immune-mediated rejection of"))
  ```
- `b_car_ada`
  ```
  (("chimeric antigen receptor" OR "CAR-T" OR "CAR T cell*") AND ("anti-drug antibody" OR "anti-drug antibodies" OR "antidrug antibod*" OR immunogenicity[Title]))
  ```
- `c_rituximab_car_any`
  ```
  rituximab AND ("chimeric antigen receptor" OR "CAR-T" OR "CAR T cell*") AND ("solid tumor*" OR "solid tumour*" OR glioma OR neuroblastoma OR sarcoma OR mesothelioma OR "renal cell" OR prostate OR ovarian OR pancrea*)
  ```
- `d_bcell_depletion_prevent_ada`
  ```
  (rituximab OR "anti-CD20" OR obinutuzumab OR ocrelizumab OR "B-cell depletion" OR "B cell depletion") AND ("prevent* the formation of" OR "prevent antibody" OR "prevention of antibody" OR "prevent* anti-drug antibod*" OR "immune tolerance induction" OR "immunosuppressive prophylaxis" OR "prophylactic immunomodulation") 
  ```
- `e_repeat_dosing_solid_car`
  ```
  ("chimeric antigen receptor") AND ("repeat dosing" OR "repeated dosing" OR "redosing" OR "re-dosing" OR "multiple infusions" OR "repeat infusions" OR "second infusion" OR reinfusion OR "re-infusion")
  ```
- `f_lamers_kershaw_maus`
  ```
  ("carboxy-anhydrase-IX" OR "CAIX" OR "folate receptor alpha" OR mesothelin OR "HER2" OR "GD2" OR "IL13Ralpha2" OR "IL13Ra2" OR "EGFRvIII") AND ("chimeric antigen receptor") AND (immunogenic* OR "antibody response" OR anaphylax* OR "anti-idiotyp*" OR "cellular immune response against")
  ```
- `g_aav_bcell_ritux`
  ```
  ("adeno-associated viral" OR "adeno-associated virus vector*" OR "AAV vector*" OR "gene transfer") AND rituximab AND (sirolimus OR "neutralizing antibod*" OR "antibody formation" OR redosing OR "immune modulation")
  ```
- `h_ert_iti_ritux`
  ```
  ("enzyme replacement therapy" OR "Pompe disease" OR alglucosidase OR "hemophilia" OR "factor VIII inhibitor*") AND rituximab AND ("immune tolerance induction" OR "antibody titer*" OR prophyla*)
  ```
- `i_ritux_dosing_pk`
  ```
  rituximab AND ("dosing schedule" OR "dose schedule" OR "375 mg/m2" OR "pharmacokinetic*" AND "B cell recovery") AND ("B-cell depletion" OR "B cell depletion" OR repopulation)
  ```
- `j_car_solid_tumor_immunosuppression`
  ```
  ("chimeric antigen receptor") AND ("solid tumor*" OR "solid tumour*") AND ("host immunity" OR "host immune response" OR "immune rejection" OR "anti-CAR" OR "limited persistence" OR "transgene-specific")
  ```
- `k_mska_hama_compartmental`
  ```
  (HAMA OR "human anti-mouse antibody") AND (rituximab OR immunosuppress*) AND ("radioimmunotherapy" OR "monoclonal antibody therapy" OR omburtamab OR 8H9 OR 3F8)
  ```
- `l_car_autoimmune_ritux`
  ```
  ("chimeric antigen receptor") AND ("anti-CD20" OR rituximab) AND ("pretreatment" OR "pre-treatment" OR conditioning OR lymphodepletion) AND (antibod* )
  ```

### Round 3

- `s1_anticar_specific`
  ```
  ("anti-CAR antibod*"[tw] OR "anti-CAR immune response*"[tw] OR "anti-idiotype antibod*"[tw] AND "chimeric antigen receptor"[tw])
  ```
- `s2_immunogenicity_cart_review`
  ```
  ("chimeric antigen receptor"[tw] OR "CAR T"[tw]) AND immunogenic*[ti]
  ```
- `s3_transgene_rejection`
  ```
  ("chimeric antigen receptor"[tw] OR "gene-modified T cell*"[tw] OR "engineered T cell*"[tw]) AND ("transgene product"[tw] OR "transgene-specific"[tw] OR "anti-transgene"[tw] OR "immune rejection"[tw] OR "immunological rejection"[tw] OR "host-mediated rejection"[tw] OR "cellular immune response against the"[tw])
  ```
- `s4_scfv_ada_assay`
  ```
  ("chimeric antigen receptor"[tw] OR "CAR T"[tw] OR "TCR-T"[tw]) AND ("anti-drug antibod*"[tw] OR "antidrug antibod*"[tw] OR "ADA assay"[tw] OR "immunogenicity assessment"[tw] OR "immunogenicity assay*"[tw])
  ```
- `s5_solid_car_trials_repeat`
  ```
  ("chimeric antigen receptor"[tw]) AND ("clinical trial"[pt] OR "phase 1"[tw] OR "phase I"[ti]) AND ("solid tumor*"[tw] OR sarcoma[tw] OR glioma[tw] OR glioblastoma[tw] OR neuroblastoma[tw] OR mesothelioma[tw] OR "renal cell carcinoma"[tw] OR "prostate cancer"[tw] OR "ovarian cancer"[tw] OR "pancreatic cancer"[tw] OR "colorectal"[tw] OR "pontine glioma"[tw] OR "midline glioma"[tw]) AND ("repeat"[tw] OR "repeated"[tw] OR "multiple infusions"[tw] OR "second infusion"[tw] OR redos*[tw] OR reinfus*[tw] OR "re-infusion"[tw] OR "intracranial"[tw] OR "intraperitoneal"[tw] OR "intrapleural"[tw] OR "hepatic artery"[tw])
  ```
- `s6_ritux_prophylaxis_gt`
  ```
  rituximab[tw] AND ("gene therapy"[tw] OR "gene transfer"[tw] OR "adeno-associated"[tw] OR "AAV vector"[tw] OR "enzyme replacement"[tw] OR "factor VIII"[tw] OR "factor IX"[tw] OR "asparaginase"[tw] OR "immune tolerance induction"[tw]) AND (prophyla*[tw] OR prevent*[tw] OR "antibody formation"[tw] OR "antibody titer*"[tw] OR "anti-drug antibod*"[tw] OR "neutralizing antibod*"[tw] OR "inhibitor development"[tw])
  ```
- `s7_ritux_bcell_kinetics`
  ```
  rituximab[tw] AND ("B-cell depletion"[tw] OR "B cell depletion"[tw] OR repopulation[tw] OR reconstitution[tw]) AND (pharmacokinetic*[tw] OR "dose"[ti] OR dosing[tw] OR "375 mg"[tw] OR "1000 mg"[tw] OR schedule*[tw]) AND ("plasma cell*"[tw] OR "memory B cell*"[tw] OR "antibody response"[tw] OR "serum immunoglobulin"[tw] OR "vaccine response"[tw] OR duration[tw])
  ```
- `s8_ritux_kill_switch`
  ```
  (rituximab[tw] OR "CD20"[tw]) AND ("safety switch"[tw] OR "suicide switch"[tw] OR "elimination marker"[tw] OR RQR8[tw] OR "QBEnd10"[tw]) AND ("chimeric antigen receptor"[tw] OR "T cell*"[tw])
  ```
- `s9_hama_solid_mab`
  ```
  ("human anti-mouse antibod*"[tw] OR HAMA[tw] OR "human anti-chimeric antibod*"[tw]) AND (neuroblastoma[tw] OR glioma[tw] OR "solid tumor*"[tw] OR "radioimmunotherapy"[tw] OR "3F8"[tw] OR "8H9"[tw] OR omburtamab[tw] OR dinutuximab[tw] OR "ch14.18"[tw])
  ```
- `s10_bcell_depletion_before_immunogen`
  ```
  (rituximab[tw] OR "anti-CD20"[tw]) AND ("prior to"[tw] OR pretreat*[tw] OR "pre-treatment"[tw] OR preconditioning[tw] OR "before administration"[tw]) AND ("prevent* antibod*"[tw] OR "blunt* the antibody"[tw] OR "abrogat* antibod*"[tw] OR "suppress* antibody"[tw] OR "humoral response"[tw] OR "primary antibody response"[tw])
  ```
- `s11_car_solid_persistence_host`
  ```
  ("chimeric antigen receptor"[tw]) AND ("solid tumor*"[tw] OR "solid tumour*"[tw]) AND ("limited persistence"[tw] OR "lack of persistence"[tw] OR "poor persistence"[tw] OR "host immune response*"[tw] OR "immunogenicity"[tw])
  ```
- `s12_ivig_plasma_cell_ada`
  ```
  ("anti-drug antibod*"[tw] OR "neutralizing antibod*"[tw] OR "inhibitor*"[tw]) AND (bortezomib[tw] OR daratumumab[tw] OR "anti-CD38"[tw] OR "plasma cell depletion"[tw] OR "IdeS"[tw] OR imlifidase[tw] OR "anti-CD20"[tw] OR rituximab[tw]) AND ("gene therapy"[tw] OR "AAV"[tw] OR "enzyme replacement"[tw] OR "cell therapy"[tw] OR "redos*"[tw] OR "re-administration"[tw] OR readministration[tw])
  ```

### Round 4

- `t1_lamers`
  ```
  Lamers CH[au] AND ("chimeric"[tw] OR CAIX[tw] OR "carboxy-anhydrase"[tw] OR "renal cell"[tw])
  ```
- `t2_kershaw_frα`
  ```
  ("folate receptor"[tw]) AND ("chimeric receptor"[tw] OR "chimeric antigen receptor"[tw]) AND (ovarian[tw] OR "phase I"[tw] OR "clinical trial"[pt])
  ```
- `t3_anticd20_prevent_anticar_preclin`
  ```
  ("anti-CD20"[tw] OR rituximab[tw] OR "B cell depletion"[tw] OR "B-cell depletion"[tw] OR "BAFF"[tw] OR "anti-CD38"[tw] OR daratumumab[tw]) AND ("adoptive transfer"[tw] OR "adoptive cell"[tw] OR "CAR T"[tw] OR "chimeric antigen receptor"[tw] OR "gene-modified T cell*"[tw]) AND ("anti-CAR"[tw] OR "anti-transgene"[tw] OR "antibody response"[tw] OR "humoral response"[tw] OR "repeat dosing"[tw] OR readministration[tw] OR "re-administration"[tw] OR persistence[tw])
  ```
- `t4_hama_prevent_immunosuppression`
  ```
  (HAMA[tw] OR "human anti-mouse antibod*"[tw] OR "human antimouse antibod*"[tw]) AND (prevent*[tw] OR abrogat*[tw] OR suppress*[tw] OR rituximab[tw] OR cyclosporin*[tw] OR "immunosuppress*"[tw] OR methotrexate[tw] OR "deoxyspergualin"[tw]) AND ("repeat*"[tw] OR "retreatment"[tw] OR "multiple cycles"[tw] OR "subsequent"[tw] OR "murine antibod*"[tw])
  ```
- `t5_aav_readmin_immunomod`
  ```
  ("adeno-associated"[tw] OR "AAV"[ti]) AND (readministration[tw] OR "re-administration"[tw] OR redosing[tw] OR "repeat administration"[tw] OR "second dose"[tw]) AND (rituximab[tw] OR "B cell depletion"[tw] OR imlifidase[tw] OR IdeS[tw] OR plasmapheresis[tw] OR bortezomib[tw] OR "immune modulation"[tw] OR sirolimus[tw] OR rapamycin[tw])
  ```
- `t6_solid_car_trials_immunogenicity_named`
  ```
  ("chimeric antigen receptor"[tw]) AND ("HER2"[tw] OR "GD2"[tw] OR "B7-H3"[tw] OR "IL13Ralpha2"[tw] OR "IL13Ra2"[tw] OR "EGFRvIII"[tw] OR mesothelin[tw] OR "CEA"[tw] OR "PSCA"[tw] OR "PSMA"[tw] OR CLDN6[tw] OR "claudin 18.2"[tw] OR GPC3[tw] OR "CAIX"[tw] OR "MUC1"[tw] OR "CD70"[tw]) AND ("phase 1"[tw] OR "phase I"[ti] OR "first-in-human"[tw] OR "clinical trial"[pt]) AND ("solid"[tw] OR glioma[tw] OR sarcoma[tw] OR neuroblastoma[tw] OR carcinoma[tw] OR glioblastoma[tw] OR mesothelioma[tw])
  ```
- `t7_rituximab_prior_cellular_therapy`
  ```
  rituximab[tw] AND ("adoptive cell therapy"[tw] OR "adoptive immunotherapy"[tw] OR "cell therapy"[tw] OR "CAR T"[tw]) AND ("prior to"[tw] OR before[tw] OR prophylactic[tw] OR preemptive[tw]) AND ("antibody formation"[tw] OR "anti-drug antibod*"[tw] OR "immunogenicity"[tw] OR "anti-CAR"[tw] OR "neutralizing"[tw])
  ```
- `t8_ritux_pk_dose_response`
  ```
  rituximab[tw] AND ("low dose"[tw] OR "single dose"[tw] OR "100 mg"[tw] OR "375 mg/m2"[tw] OR "1000 mg"[tw] OR "dose-finding"[tw]) AND ("B cell depletion"[tw] OR "B-cell depletion"[tw]) AND ("kinetics"[tw] OR duration[tw] OR "time to"[tw] OR onset[tw] OR "lymph node"[tw] OR "germinal cent*"[tw] OR "tissue"[tw])
  ```
- `t9_regulatory_guidance_immunogenicity`
  ```
  ("immunogenicity"[ti] OR "anti-drug antibod*"[ti]) AND (guidance[tw] OR "regulatory"[tw] OR "FDA"[tw] OR "EMA"[tw] OR "risk assessment"[tw]) AND ("cell therapy"[tw] OR "gene therapy"[tw] OR "CAR-T"[tw] OR "CAR T"[tw])
  ```
- `t10_second_infusion_solid_tumor_outcome`
  ```
  ("chimeric antigen receptor"[tw] OR "CAR-T"[tw]) AND ("solid"[tw] OR glioma[tw] OR sarcoma[tw] OR neuroblastoma[tw] OR mesothelioma[tw] OR carcinoma[tw]) AND ("loss of"[tw] OR "decreased"[tw] OR "diminished"[tw] OR "absent"[tw]) AND ("expansion after the second"[tw] OR "subsequent infusions"[tw] OR "second infusion"[tw] OR "later infusions"[tw] OR "repeat infusions"[tw])
  ```

### Round 5

- `u1`
  ```
  Kershaw MH[au] AND ("folate receptor"[tw] OR "phase I"[tw] OR ovarian[tw])
  ```
- `u2`
  ```
  Ahmed N[au] AND "HER2"[tw] AND (sarcoma[tw] OR glioblastoma[tw]) AND ("chimeric antigen receptor"[tw] OR "virus-specific"[tw])
  ```
- `u3`
  ```
  Beatty GL[au] AND mesothelin[tw] AND (mRNA[tw] OR "chimeric antigen receptor"[tw])
  ```
- `u4`
  ```
  ("PSCA"[tw] OR "prostate stem cell antigen"[tw]) AND "chimeric antigen receptor"[tw] AND ("phase 1"[tw] OR trial[tw])
  ```
- `u5`
  ```
  Thistlethwaite FC[au] OR ("CEA"[tw] AND "chimeric antigen receptor"[tw] AND ("phase I"[tw] OR "first-in-man"[tw]) AND (colorectal[tw] OR "carcinoembryonic"[tw]))
  ```
- `u6`
  ```
  ("anti-CD20"[tw] OR rituximab[tw]) AND ("KLH"[tw] OR "keyhole limpet"[tw] OR "neoantigen challenge"[tw] OR "primary immunization"[tw] OR "de novo antibody"[tw] OR "T-dependent antigen"[tw])
  ```
- `u7`
  ```
  ("germinal center"[tw] OR "lymph node"[tw] OR "tissue-resident"[tw] OR spleen[tw]) AND (rituximab[tw] OR "anti-CD20"[tw]) AND ("incomplete depletion"[tw] OR "residual B cells"[tw] OR "depletion of B cells"[tw] OR "resistance to depletion"[tw])
  ```
- `u8`
  ```
  ("chimeric antigen receptor"[tw] OR "CAR T"[tw]) AND ("cyclophosphamide"[tw] AND "fludarabine"[tw]) AND ("lymphodepletion"[tw]) AND ("B cell"[tw] OR "humoral"[tw] OR "antibody"[tw] OR "immunogenicity"[tw])
  ```
- `u9`
  ```
  ("mycophenolate"[tw] OR "tacrolimus"[tw] OR "sirolimus"[tw] OR "rapamycin"[tw] OR "belatacept"[tw] OR "abatacept"[tw] OR "CTLA4-Ig"[tw]) AND ("anti-drug antibod*"[tw] OR "antibody formation"[tw] OR "immune tolerance"[tw]) AND ("gene therapy"[tw] OR "cell therapy"[tw] OR "transgene"[tw] OR "biologic*"[tw])
  ```
- `u10`
  ```
  ("humanized"[tw] OR "fully human"[tw]) AND "chimeric antigen receptor"[tw] AND (retreatment[tw] OR "second infusion"[tw] OR "anti-CAR"[tw] OR "anti-murine"[tw] OR immunogenic*[tw]) AND ("solid"[tw] OR glioma[tw] OR sarcoma[tw] OR neuroblastoma[tw] OR myeloma[tw])
  ```


---

## Administration-level supplementary search (categories J–N)

Second pass, run to answer the follow-up question "how is the drug actually given" rather than "does it
work". Source: Europe PMC REST (`/search`, `resultType=core`), no API key; script
`harvest_administration.py`, 1,365 unique records across seven query groups, then hand-screened down to the
59 records now in `index.tsv` categories `J`–`N`. Metadata and abstracts refetched by PMID with
`curate_administration.py`; rows appended and PMC open-access XML fetched by `index_administration.py`.

Query groups (full strings in `harvest_administration.py`):

| Group | Intent |
|---|---|
| `premedication_infusion_reactions` | premedication components, rapid/shortened infusion schedules, IRR incidence and management, desensitisation, anti-rituximab antibodies |
| `pediatric_administration` | paediatric infusion rates, PK/BSA dosing, hypogammaglobulinaemia in children |
| `screening_and_prophylaxis` | HBV, PJP, IgG replacement, vaccination, late-onset neutropenia, TLS, PML |
| `cns_and_route` | CSF penetration, intrathecal/intraventricular routes, subcutaneous and biosimilar formulations |
| `dose_depth_duration` | dose–depletion–duration, high-dose (500–750 mg/m²) exposure and safety |
| `cart_context` | steroids and CAR-T function, Cy/Flu lymphodepletion dosing, ICV procedure, infection prophylaxis guidelines |
| `fasting_npo_sedation` | preoperative/procedural fasting guidelines, whether any infusion requires fasting |

Non-literature sources used for the same note: openFDA `drug/label` (Rituxan IV, label effective
2025-01-06) for all label-derived statements, and the two ClinicalTrials.gov records already quoted in
`notes/registry_and_unpublished_evidence.md`. The searches returned **no** publication specifying
premedication, infusion rate, or fasting requirements for rituximab given for anti-CAR prophylaxis in
solid-tumour CAR-T; every administration statement in `notes/administration_protocol.md` is therefore
label-derived, indication-transferred, or explicitly labelled INFERENCE.

---

# Appendix: full reference list

All 252 curated records, grouped by category and ordered by year (descending). Records without a PMID are trial-registry entries, preprints, or presentations.

## A — Anti-CAR antibody evidence in solid tumours (18)

- Tebas P et al. Clinical trial results provide the rationale to protect dual HIV-specific T cells with a signaling-defective HIV fusion inhibitor. *Mol Ther* 2026. PMID 41520175.
- Chen Y et al. Anti-CAR Immunity Drives Acquired Therapeutic Resistance to GD2-CAR T Cell Therapy in Diffuse Midline Glioma. *medRxiv (preprint)* 2026. PMID 42465905.
- Kimble EL et al. Novel antibodies for identification, selection, and manipulation of T cells expressing Whitlow linker-containing CARs. *J Immunother Cancer* 2025. PMID 41253492.
- Qi C et al. Claudin-18 isoform 2-specific CAR T-cell therapy (satri-cel) versus treatment of physician's choice for previously treated advanced gastric or gastro-oesophageal junction cancer (CT041-ST-01): a randomised, open-label, phase 2 trial. *Lancet* 2025. PMID 40460847.
- Pampusch MS et al. Assessment of anti-CD20 antibody pre-treatment for augmentation of CAR-T cell therapy in SIV-infected rhesus macaques. *Front Immunol* 2023. PMID 36825014.
- Davey BC et al. Development of an anti-CAR antibody response in SIV-infected rhesus macaques treated with CD4-MBL CAR/CXCR5 T cells. *Front Immunol* 2022. PMID 36582226.
- Ko AH et al. Dual Targeting of Mesothelin and CD19 with Chimeric Antigen Receptor-Modified T Cells in Patients with Metastatic Pancreatic Cancer. *Mol Ther* 2020. PMID 32730744.
- Haas AR et al. Phase I Study of Lentiviral-Transduced Chimeric Antigen Receptor-Modified T Cells Recognizing Mesothelin in Advanced Solid Cancers. *Mol Ther* 2019. PMID 31420241.
- Hege KM et al. Safety, tumor trafficking and immunogenicity of chimeric antigen receptor (CAR)-T cells specific for TAG-72 in colorectal cancer. *J Immunother Cancer* 2017. PMID 28344808.
- Lamers CH et al. Treatment of metastatic renal cell carcinoma (mRCC) with CAIX CAR-engineered T-cells-a completed study overview. *Biochem Soc Trans* 2016. PMID 27284065.
- Junghans RP et al. Phase I Trial of Anti-PSMA Designer CAR-T Cells in Prostate Cancer: Possible Role for Interacting Interleukin 2-T Cell Pharmacodynamics as a Determinant of Clinical Response. *Prostate* 2016. PMID 27324746.
- Beatty GL et al. Mesothelin-specific chimeric antigen receptor mRNA-engineered T cells induce anti-tumor activity in solid malignancies. *Cancer Immunol Res* 2014. PMID 24579088.
- Lamers CH et al. Treatment of metastatic renal cell carcinoma with CAIX CAR-engineered T cells: clinical evaluation and management of on-target toxicity. *Mol Ther* 2013. PMID 23423337.
- Maus MV et al. T cells expressing chimeric antigen receptors can cause anaphylaxis in humans. *Cancer Immunol Res* 2013. PMID 24777247.
- Lamers CH et al. Immune responses to transgene and retroviral vector in patients treated with ex vivo-engineered T cells. *Blood* 2011. PMID 20889925.
- Lamers CH et al. Gene-modified T cells for adoptive immunotherapy of renal cell cancer maintain transgene-specific immune functions in vivo. *Cancer Immunol Immunother* 2007. PMID 17479266.
- Lamers CH et al. Treatment of metastatic renal cell carcinoma with autologous T-lymphocytes genetically retargeted against carbonic anhydrase IX: first clinical experience. *J Clin Oncol* 2006. PMID 16648493.
- Kershaw MH et al. A phase I study on adoptive immunotherapy using gene-modified T cells for ovarian cancer. *Clin Cancer Res* 2006. PMID 17062687.

## B — Mechanism, ADA assays, regulatory guidance (28)

- Hofman K et al. Immunogenicity of Gene and Cell Therapies. *BioDrugs* 2026. PMID 41518483.
- Day G et al. Development of a flow cytometry method to measure antidrug antibodies against CAR T cells. *Immunohorizons* 2026. PMID 42033387.
- Liu X et al. Epitope mapping of humoral immunogenicity of orvacabtagene autoleucel shows an IgM response with minimal impact on CAR T cellular kinetics. *Mol Ther Adv* 2026. PMID 42375474.
- Fernández N et al. A roadmap for systematic humanization of a chimeric antigen receptor: preclinical validation of a humanized CD22 scFv as a model. *Exp Hematol* 2026. PMID 41881100.
- Alfar HR et al. Clinical evidence of immunogenicity of CAR-T cell therapies and its implication in the clinical development of CAR-T drug products. *Front Immunol* 2025. PMID 40061940.
- Masilamani M et al. Cellular Immunogenicity Assessments in CAR-T Cell Therapies: Current Insights and Future Directions. *AAPS J* 2025. PMID 40908464.
- Gokemeijer J et al. An IQ Consortium Perspective on Best Practices for Bioanalytical and Immunogenicity Assessment Aspects of CAR-T and TCR-T Cellular Therapies Development. *Clin Pharmacol Ther* 2024. PMID 37983584.
- Mattei AE et al. In silico methods for immunogenicity risk assessment and human homology screening for therapeutic antibodies. *MAbs* 2024. PMID 38536724.
- Sauna ZE et al. Understanding preclinical and clinical immunogenicity risks in novel biotherapeutics development. *Front Immunol* 2023. PMID 37251396.
- Khan AN et al. Immunogenicity of CAR-T Cell Therapeutics: Evidence, Mechanism and Mitigation. *Front Immunol* 2022. PMID 35677038.
- Wagner DL et al. Immunogenicity of CAR T cells in cancer therapy. *Nat Rev Clin Oncol* 2021. PMID 33633361.
- Zinsli LV et al. Deimmunization of protein therapeutics - Recent advances in experimental and computational epitope prediction and deletion. *Comput Struct Biotechnol J* 2021. PMID 33425259.
- Thudium Mueller K et al. Tisagenlecleucel immunogenicity in relapsed/refractory acute lymphoblastic leukemia and diffuse large B-cell lymphoma. *Blood Adv* 2021. PMID 34432863.
- Gazeau N et al. Effective anti-BCMA retreatment in multiple myeloma. *Blood Adv* 2021. PMID 34351389.
- Wang D et al. A phase 1 study of a novel fully human BCMA-targeting CAR (CT103A) in patients with relapsed/refractory multiple myeloma. *Blood* 2021. PMID 33512480.
- Potthoff B et al. A cell-based immunogenicity assay to detect antibodies against chimeric antigen receptor expressed by tisagenlecleucel. *J Immunol Methods* 2020. PMID 31678267.
- Awasthi R et al. Tisagenlecleucel cellular kinetics, dose, and immunogenicity in relation to clinical factors in relapsed/refractory DLBCL. *Blood Adv* 2020. PMID 32045475.
- Gorovits B et al. Immunogenicity of Chimeric Antigen Receptor T-Cell Therapeutics. *BioDrugs* 2019. PMID 31069709.
- Davda J et al. Immunogenicity of immunomodulatory, antibody-based, oncology therapeutics. *J Immunother Cancer* 2019. PMID 30992085.
- Xu J et al. Exploratory trial of a biepitopic CAR T-targeting B cell maturation antigen in relapsed/refractory multiple myeloma. *Proc Natl Acad Sci U S A* 2019. PMID 30988175.
- Salazar-Fontana LI et al. Approaches to Mitigate the Unwanted Immunogenicity of Therapeutic Proteins during Drug Development. *AAPS J* 2017. PMID 28083796.
- Turtle CJ et al. CD19 CAR-T cells of defined CD4+:CD8+ composition in adult B cell ALL patients. *J Clin Invest* 2016. PMID 27111235.
- Song DG et al. A fully human chimeric antigen receptor with potent activity against cancer cells but reduced risk for off-tumor toxicity. *Oncotarget* 2015. PMID 26101914.
- Lanitis E et al. Redirected antitumor activity of primary human lymphocytes transduced with a fully human anti-mesothelin chimeric receptor. *Mol Ther* 2012. PMID 22127019.
- Jensen MC et al. Antitransgene rejection responses contribute to attenuated persistence of adoptively transferred CD20/CD19-specific chimeric antigen receptor redirected T cells in humans. *Biol Blood Marrow Transplant* 2010. PMID 20304086.
- Piasecki JC et al. Induction of transgene-specific cytotoxic T lymphocyte responses after transplantation of gene-modified CD34+ cells despite nonablative immunosuppressive conditioning. *Hum Gene Ther* 2008. PMID 18092920.
- Berger C et al. Analysis of transgene-specific immune responses that limit the in vivo persistence of adoptively transferred HSV-TK-modified donor T cells after allogeneic hematopoietic cell transplantation. *Blood* 2006. PMID 16282341.
- Berger C et al. Nonmyeloablative immunosuppressive regimen prolongs In vivo persistence of gene-modified autologous T cells in a nonhuman primate model. *J Virol* 2001. PMID 11134293.

## C — Solid-tumour CAR-T trials that redose (40)

- Shan Y et al. T-cell receptor-like chimeric antigen receptor T cells targeting mesothelin: A first-in-human dose-escalation trial for platinum-resistant advanced ovarian cancer. *Cancer* 2026. PMID 41575866.
- Ronsley R et al. Intracerebroventricular B7-H3-targeting CAR T cells for non-pontine DMG and recurrent/refractory pediatric CNS tumors: a phase 1 trial. *Neuro Oncol* 2026. PMID 42503899.
- Gao Y et al. Hypoxia-responsive CEA-targeted CAR T cells in CEA-positive solid tumors through intraperitoneal or intravenous infusion: a phase 1 trial. *Nat Cancer* 2026. PMID 41760800.
- Liu C et al. Allogeneic B7-H3-Targeted CAR Vδ1T-cell Therapy in Advanced Solid Tumors: A Phase I Study. *Clin Cancer Res* 2026. PMID 41779003.
- Srour SA et al. Allogeneic CD70-Targeted Chimeric Antigen Receptor T-Cell Therapy for Advanced Renal Cell Carcinoma: Results From the Phase I TRAVERSE Trial. *J Clin Oncol* 2026. PMID 42447427.
- Mackall CL. GD2-CAR T Cells for Diffuse Midline Gliomas (CLIN2-12595), CIRM Board Meeting presentation, January 2026. *CIRM Board Meeting (presentation)* 2026. https://www.cirm.ca.gov/wp-content/uploads/2026/01/7b.-20290129-Closer-to-Cures-Presentation.pdf.
- Stanford University (sponsor). GD2 CAR T Cells in Diffuse Intrinsic Pontine Gliomas (DIPG) & Spinal Diffuse Midline Glioma (DMG) - NCT04196413, Arm D. *ClinicalTrials.gov* 2026. https://clinicaltrials.gov/study/NCT04196413.
- Freeburg NF et al. The critical role of the endogenous immune compartment after CAR T cell therapy in recurrent GBM. *Cell* 2026. PMID 42296961.
- Monje M et al. Intravenous and intracranial GD2-CAR T cells for H3K27M+ diffuse midline gliomas. *Nature* 2025. PMID 39537919.
- Vitanza NA et al. Intracerebroventricular B7-H3-targeting CAR T cells for diffuse intrinsic pontine glioma: a phase 1 trial. *Nat Med* 2025. PMID 39775044.
- Barish ME et al. Chlorotoxin-directed CAR T cell therapy for recurrent glioblastoma: Interim clinical experience demonstrating feasibility and safety. *Cell Rep Med* 2025. PMID 40818458.
- Li B et al. Intraperitoneal infusion of NKG2D CAR-NK cells induces endogenous CD8+ T cell activation in patients with advanced colorectal cancer. *Mol Ther* 2025. PMID 40437757.
- Begley SL et al. CAR T cell therapy for glioblastoma: A review of the first decade of clinical trials. *Mol Ther* 2025. PMID 40057825.
- Silbert S et al. Have CARs stalled for non-B-cell malignancies? Where are we, and where are we going? *Hematology Am Soc Hematol Educ Program* 2025. PMID 41347986.
- University of Pennsylvania (sponsor). CART-EGFR-IL13Ra2 in Newly Diagnosed GBM Following Initial Radiotherapy - NCT06973096, Cohort B. *ClinicalTrials.gov* 2025. https://clinicaltrials.gov/study/NCT06973096.
- Bagley SJ et al. Intracerebroventricular bivalent CAR T cells targeting EGFR and IL-13Ralpha2 in recurrent glioblastoma: a phase 1 trial. *Nat Med* 2025. PMID 40451950.
- Dorff TB et al. PSCA-CAR T cell therapy in metastatic castration-resistant prostate cancer: a phase 1 trial. *Nat Med* 2024. PMID 38867077.
- Stein MN et al. PSCA-targeted BPX-601 CAR T cells with pharmacological activation by rimiducid in metastatic pancreatic and prostate cancer: a phase 1 dose escalation trial. *Nat Commun* 2024. PMID 39737899.
- Hegde M et al. Autologous HER2-specific CAR T cells after lymphodepletion for advanced sarcoma: a phase 1 trial. *Nat Cancer* 2024. PMID 38658775.
- Bagley SJ et al. Repeated peripheral infusions of anti-EGFRvIII CAR T cells in combination with pembrolizumab show no efficacy in glioblastoma: a phase 1 trial. *Nat Cancer* 2024. PMID 38216766.
- Pinto N et al. STRIvE-02: A First-in-Human Phase I Study of Systemically Administered B7-H3 Chimeric Antigen Receptor T Cells for Patients With Relapsed/Refractory Solid Tumors. *J Clin Oncol* 2024. PMID 39255444.
- Mackensen A et al. CLDN6-specific CAR-T cells plus amplifying RNA vaccine in relapsed or refractory solid tumors: the phase 1 BNT211-01 trial. *Nat Med* 2023. PMID 37872225.
- Majzner RG et al. GD2-CAR T cell therapy for H3K27M-mutated diffuse midline gliomas. *Nature* 2022. PMID 35130560.
- Brown CE et al. Off-the-shelf, steroid-resistant, IL13Rα2-specific CAR T cells for treatment of glioblastoma. *Neuro Oncol* 2022. PMID 35100373.
- Ghosn M et al. Image-guided interventional radiological delivery of chimeric antigen receptor (CAR) T cells for pleural malignancies in a phase I/II clinical trial. *Lung Cancer* 2022. PMID 35045358.
- Vitanza NA et al. Locoregional infusion of HER2-specific CAR T cells in children and young adults with recurrent or refractory CNS tumors: an interim analysis. *Nat Med* 2021. PMID 34253928.
- Adusumilli PS et al. A Phase I Trial of Regional Mesothelin-Targeted CAR T-cell Therapy in Patients with Malignant Pleural Disease, in Combination with the Anti-PD-1 Agent Pembrolizumab. *Cancer Discov* 2021. PMID 34266984.
- Katz SC et al. HITM-SURE: Hepatic immunotherapy for metastases phase Ib anti-CEA CAR-T study utilizing pressure enabled drug delivery. *J Immunother Cancer* 2020. PMID 32843493.
- Katz SC et al. HITM-SIR: phase Ib trial of intraarterial chimeric antigen receptor T-cell therapy and selective internal radiation therapy for CEA+ liver metastases. *Cancer Gene Ther* 2020. PMID 31155611.
- Beatty GL et al. Activity of Mesothelin-Specific Chimeric Antigen Receptor T Cells Against Pancreatic Carcinoma Metastases in a Phase 1 Trial. *Gastroenterology* 2018. PMID 29567081.
- Wang Y et al. CD133-directed CAR T cells for advanced metastasis malignancies: A phase I trial. *Oncoimmunology* 2018. PMID 29900044.
- Thistlethwaite FC et al. The clinical efficacy of first-generation carcinoembryonic antigen (CEACAM5)-specific CAR T cells is limited by poor persistence and transient pre-conditioning-dependent respiratory toxicity. *Cancer Immunol Immunother* 2017. PMID 28660319.
- Zhang C et al. Phase I Escalating-Dose Trial of CAR-T Therapy Targeting CEA+ Metastatic Colorectal Cancers. *Mol Ther* 2017. PMID 28366766.
- Ahmed N et al. HER2-Specific Chimeric Antigen Receptor-Modified Virus-Specific T Cells for Progressive Glioblastoma: A Phase 1 Dose-Escalation Trial. *JAMA Oncol* 2017. PMID 28426845.
- Brown CE et al. Regression of Glioblastoma after Chimeric Antigen Receptor T-Cell Therapy. *N Engl J Med* 2016. PMID 28029927.
- Katz SC et al. Regional CAR-T cell infusions for peritoneal carcinomatosis are superior to systemic delivery. *Cancer Gene Ther* 2016. PMID 27080226.
- Ahmed N et al. Human Epidermal Growth Factor Receptor 2 (HER2) -Specific Chimeric Antigen Receptor-Modified T Cells for the Immunotherapy of HER2-Positive Sarcoma. *J Clin Oncol* 2015. PMID 25800760.
- Brown CE et al. Bioactivity and Safety of IL13Rα2-Redirected Chimeric Antigen Receptor CD8+ T Cells in Patients with Recurrent Glioblastoma. *Clin Cancer Res* 2015. PMID 26059190.
- Adusumilli PS et al. Regional delivery of mesothelin-targeted CAR T cell therapy generates potent and long-lasting CD4-dependent tumor immunity. *Sci Transl Med* 2014. PMID 25378643.
- Saied A et al. Neutrophil:lymphocyte ratios and serum cytokine changes after hepatic artery chimeric antigen receptor-modified T-cell infusions for liver metastases. *Cancer Gene Ther* 2014. PMID 25277132.

## D — Rituximab pharmacology and what sets a schedule (26)

- Chen C et al. The rituximab paradox in rheumatoid arthritis: Re-evaluating B-cell depletion depth and the synovial microenvironment. *Autoimmun Rev* 2026. PMID 42162633.
- Yuan M et al. Translating B-Cell and Plasma-Cell Targeting from Oncology to Autoimmunity: Modalities, Quantitative Bridging, and a Development Roadmap. *Clin Pharmacol Ther* 2026. PMID 42244451.
- Cao S et al. Efficacy, safety, and B-cell depletion capacity of 3 rituximab dosing regimens in the treatment of moderate-to-severe pemphigus vulgaris and pemphigus foliaceus: A 52-week clinical trial. *J Am Acad Dermatol* 2025. PMID 40374120.
- Liang H et al. Dosing optimization of rituximab for primary membranous nephropathy by population pharmacokinetic and pharmacodynamic study. *Front Pharmacol* 2024. PMID 38595918.
- Ciolfi C et al. Is It Time to Reconsider Rituximab Dosing Regimens for Pemphigus Vulgaris? *Antibodies (Basel)* 2024. PMID 38247568.
- Hamaya T et al. Humoral response to SARS-CoV-2 mRNA vaccine on in ABO blood type incompatible kidney transplant recipients treated with low-dose rituximab. *Sci Rep* 2023. PMID 37699969.
- Shree T et al. CD20-Targeted Therapy Ablates De Novo Antibody Response to Vaccination but Spares Preestablished Immunity. *Blood Cancer Discov* 2022. PMID 35015688.
- Blincoe A et al. Acquired B-cell deficiency secondary to B-cell-depleting therapies. *J Immunol Methods* 2022. PMID 36372267.
- van Dam LS et al. Highly Sensitive Flow Cytometric Detection of Residual B-Cells After Rituximab in Anti-Neutrophil Cytoplasmic Antibodies-Associated Vasculitis Patients. *Front Immunol* 2020. PMID 33384685.
- Ramwadhdoebe TH et al. Effect of rituximab treatment on T and B cell subsets in lymph node biopsies of patients with rheumatoid arthritis. *Rheumatology (Oxford)* 2019. PMID 30649469.
- Hogan J et al. Effect of different rituximab regimens on B cell depletion and time to relapse in children with steroid-dependent nephrotic syndrome. *Pediatr Nephrol* 2019. PMID 30109447.
- Redfield RR et al. Safety, pharmacokinetics, and pharmacodynamic activity of obinutuzumab, a type 2 anti-CD20 monoclonal antibody for the desensitization of candidates for renal transplant. *Am J Transplant* 2019. PMID 31257724.
- Cornec D et al. Pharmacokinetics of rituximab and clinical outcomes in patients with anti-neutrophil cytoplasmic antibody associated vasculitis. *Rheumatology (Oxford)* 2018. PMID 29340623.
- Bhoj VG et al. Persistence of long-lived plasma cells and humoral immunity in individuals responding to CD19-directed CAR T-cell therapy. *Blood* 2016. PMID 27166358.
- Laws LH et al. Inflammation Causes Resistance to Anti-CD20-Mediated B Cell Depletion. *Am J Transplant* 2016. PMID 27265023.
- Rosenberg AS et al. A role for plasma cell targeting agents in immune tolerance induction in autoimmune disease and antibody responses to therapeutic proteins. *Clin Immunol* 2016. PMID 26928739.
- Turner-Stokes T et al. Induction treatment of ANCA-associated vasculitis with a single dose of rituximab. *Rheumatology (Oxford)* 2014. PMID 24609057.
- Vaidyanathan A et al. Developmental immunotoxicology assessment of rituximab in cynomolgus monkeys. *Toxicol Sci* 2011. PMID 20937725.
- Bingham CO et al. Immunization responses in rheumatoid arthritis patients treated with rituximab: results from a controlled clinical trial. *Arthritis Rheum* 2010. PMID 20039397.
- St Clair EW. Good and bad memories following rituximab therapy. *Arthritis Rheum* 2010. PMID 20039422.
- Bearden CM et al. Rituximab inhibits the in vivo primary and secondary antibody response to a neoantigen, bacteriophage phiX174. *Am J Transplant* 2005. PMID 15636611.
- Vugmeyster Y et al. Depletion of B cells by a humanized anti-CD20 antibody PRO70769 in Macaca fascicularis. *J Immunother* 2005. PMID 15838377.
- Schröder C et al. Anti-CD20 treatment depletes B-cells in blood and lymphatic tissue of cynomolgus monkeys. *Transpl Immunol* 2003. PMID 14551029.
- van der Kolk LE et al. Rituximab treatment results in impaired secondary humoral immune responsiveness. *Blood* 2002. PMID 12200395.
- Gonzalez-Stawinski GV et al. Hapten-induced primary and memory humoral responses are inhibited by the infusion of anti-CD20 monoclonal antibody (IDEC-C2B8, Rituximab). *Clin Immunol* 2001. PMID 11161973.
- Maloney DG et al. IDEC-C2B8 (Rituximab) anti-CD20 monoclonal antibody therapy in patients with relapsed low-grade non-Hodgkin's lymphoma. *Blood* 1997. PMID 9310469.

## E — Anti-CD20 prophylaxis in gene therapy (20)

- Vicidomini A et al. Rapamycin nanoparticles mitigate anti-AAV antibody formation in a mouse model of ornithine transcarbamylase deficiency. *Mol Ther Adv* 2026. PMID 42436852.
- Li L et al. Cholesterolated Rapamycin Prodrug Liposomes Induce Antigen-Specific Tolerance and Enable AAV Redosing. *Mol Pharm* 2026. PMID 41674289.
- Doshi BS et al. Use of CD19-targeted immune modulation to eradicate AAV-neutralizing antibodies. *Mol Ther* 2025. PMID 40057826.
- Nelson RW et al. Reduction of Preexisting AAV9 Antibody Titers Before Onasemnogene Abeparvovec Administration in Twins With Spinal Muscular Atrophy. *Neurology* 2025. PMID 40705999.
- Li X et al. Lipid-Rapamycin Nanovaccines Overcome the Antidrug Antibody Barrier in Biologic Therapies. *ACS Nano* 2025. PMID 39847793.
- Rana J et al. B cell focused transient immune suppression protocol for efficient AAV readministration to the liver. *Mol Ther Methods Clin Dev* 2024. PMID 38440160.
- Potter RA et al. Use of plasmapheresis to lower anti-AAV antibodies in nonhuman primates with pre-existing immunity to AAVrh74. *Mol Ther Methods Clin Dev* 2024. PMID 38327805.
- Salabarria SM et al. Thrombotic microangiopathy following systemic AAV administration is dependent on anti-capsid antibodies. *J Clin Invest* 2024. PMID 37988172.
- Choi SJ et al. Successful AAV8 readministration: Suppression of capsid-specific neutralizing antibodies by a combination treatment of bortezomib and CD20 mAb in a mouse model of Pompe disease. *J Gene Med* 2023. PMID 36994804.
- Ilyinskii PO et al. Readministration of high-dose adeno-associated virus gene therapy vectors enabled by ImmTOR nanoparticles combined with B cell-targeted agents. *PNAS Nexus* 2023. PMID 38024395.
- Li N et al. The Effect of Immunomodulatory Treatments on Anti-Dystrophin Immune Response After AAV Gene Therapy in Dystrophin Deficient mdx Mice. *J Neuromuscul Dis* 2021. PMID 34569971.
- Leborgne C et al. IgG-cleaving endopeptidase enables in vivo gene therapy in the presence of anti-AAV neutralizing antibodies. *Nat Med* 2020. PMID 32483358.
- Meliani A et al. Antigen-selective modulation of AAV immunogenicity with tolerogenic rapamycin nanoparticles enables successful vector re-administration. *Nat Commun* 2018. PMID 30291246.
- Corti M et al. Evaluation of Readministration of a Recombinant Adeno-Associated Virus Vector Expressing Acid Alpha-Glucosidase in Pompe Disease: Preclinical to Clinical Planning. *Hum Gene Ther Clin Dev* 2015. PMID 26390092.
- Unzu C et al. Helper-dependent adenovirus achieve more efficient and persistent liver transgene expression in non-human primates under immunosuppression. *Gene Ther* 2015. PMID 26125605.
- Corti M et al. B-Cell Depletion is Protective Against Anti-AAV Capsid Immune Response: A Human Subject Case Study. *Mol Ther Methods Clin Dev* 2014. PMID 25541616.
- Mingozzi F et al. Prevalence and pharmacological modulation of humoral immunity to AAV vectors in gene transfer to synovial tissue. *Gene Ther* 2013. PMID 22786533.
- Mingozzi F et al. Pharmacological modulation of humoral immunity in a nonhuman primate model of AAV gene transfer for hemophilia B. *Mol Ther* 2012. PMID 22565846.
- Unzu C et al. Transient and intensive pharmacological immunosuppression fails to improve AAV-based liver gene transfer in non-human primates. *J Transl Med* 2012. PMID 22704060.
- Fontanellas A et al. Intensive pharmacological immunosuppression allows for repetitive liver gene transfer with recombinant adenovirus in nonhuman primates. *Mol Ther* 2010. PMID 20087317.

## F — Immune tolerance induction regimens (30)

- Kishnani PS et al. Insights into immunogenicity and therapeutic strategies to mitigate the immune response in infantile-onset Pompe disease: a comprehensive systematic literature review. *Front Immunol* 2025. PMID 41583481.
- Chen HA et al. Optimizing treatment outcomes: immune tolerance induction in Pompe disease patients undergoing enzyme replacement therapy. *Front Immunol* 2024. PMID 38715621.
- Desai AK et al. An updated management approach of Pompe disease patients with high-sustained anti-rhGAA IgG antibody titers: experience with bortezomib-based immunomodulation. *Front Immunol* 2024. PMID 38524130.
- Li Z et al. Eradication of FIX inhibitor in haemophilia B children using low-dose immune tolerance induction with rituximab-based immunosuppressive agent(s) in China. *Haemophilia* 2022. PMID 35503087.
- Tran JQ et al. Expansion of immature, nucleated red blood cells by transient low-dose methotrexate immune tolerance induction in mice. *Clin Exp Immunol* 2021. PMID 33205401.
- Desai AK et al. Benefits of Prophylactic Short-Course Immune Tolerance Induction in Patients With Infantile Pompe Disease: Demonstration of Long-Term Safety and Efficacy in an Expanded Cohort. *Front Immunol* 2020. PMID 32849613.
- Desai AK et al. The potential impact of timing of IVIG administration on the efficacy of rituximab for immune tolerance induction for patients with Pompe disease. *Clin Immunol* 2020. PMID 32681978.
- Gupta P et al. A Race Against Time-Changing the Natural History of CRIM Negative Infantile Pompe Disease. *Front Immunol* 2020. PMID 33013846.
- Julien DC et al. Immune Modulation for Enzyme Replacement Therapy in A Female Patient With Hunter Syndrome. *Front Immunol* 2020. PMID 32508845.
- Poelman E et al. Effects of higher and more frequent dosing of alglucosidase alfa and immunomodulation on long-term clinical outcome of classic infantile Pompe patients. *J Inherit Metab Dis* 2020. PMID 32506446.
- Doshi BS et al. Combined anti-CD20 and mTOR inhibition with factor VIII for immune tolerance induction in hemophilia A patients with refractory inhibitors. *J Thromb Haemost* 2020. PMID 31985872.
- Biswas M et al. B Cell Depletion Eliminates FVIII Memory B Cells and Enhances AAV8-coF8 Immune Tolerance Induction When Combined With Rapamycin. *Front Immunol* 2020. PMID 32670285.
- De Groot AS et al. HLA- and genotype-based risk assessment model to identify infantile onset pompe disease patients at high-risk of developing significant anti-drug antibodies (ADA). *Clin Immunol* 2019. PMID 30711607.
- Poelman E et al. High Sustained Antibody Titers in Patients with Classic Infantile Pompe Disease Following Immunomodulation at Start of Enzyme Replacement Therapy. *J Pediatr* 2018. PMID 29428273.
- Hassan S et al. Preventing or Eradicating Factor VIII Antibody Formation in Patients with Hemophilia A: What Can We Learn from Other Disorders? *Semin Thromb Hemost* 2018. PMID 30045390.
- Kazi ZB et al. Sustained immune tolerance induction in enzyme replacement therapy-treated CRIM-negative patients with infantile Pompe disease. *JCI Insight* 2017. PMID 28814660.
- Rairikar M et al. High dose IVIG successfully reduces high rhGAA IgG antibody titers in a CRIM-negative infantile Pompe disease patient. *Mol Genet Metab* 2017. PMID 28648664.
- Biswas M et al. Combination therapy for inhibitor reversal in haemophilia A using monoclonal anti-CD20 and rapamycin. *Thromb Haemost* 2017. PMID 27683758.
- Schultz HS et al. Quantitative analysis of the CD4+ T cell response to therapeutic antibodies in healthy donors using a novel T cell:PBMC assay. *PLoS One* 2017. PMID 28562666.
- Kazi ZB et al. Durable and sustained immune tolerance to ERT in Pompe disease with entrenched immune responses. *JCI Insight* 2016. PMID 27493997.
- Stenger EO et al. Immune Tolerance Strategies in Siblings with Infantile Pompe Disease-Advantages for a Preemptive Approach to High-Sustained Antibody Titers. *Mol Genet Metab Rep* 2015. PMID 26167453.
- Debiec H et al. Allo-immune membranous nephropathy and recombinant aryl sulfatase replacement therapy: a need for tolerance induction therapy. *J Am Soc Nephrol* 2014. PMID 24262793.
- Leissinger C et al. Rituximab for treatment of inhibitors in haemophilia A. A Phase II study. *Thromb Haemost* 2014. PMID 24919980.
- Banugaria SG et al. Algorithm for the early diagnosis and treatment of patients with cross reactive immunologic material-negative classic infantile pompe disease: a step towards improving the efficacy of ERT. *PLoS One* 2013. PMID 23825616.
- Banugaria SG et al. Bortezomib in the rapid reduction of high sustained antibody titers in disorders treated with therapeutic protein: lessons learned from Pompe disease. *Genet Med* 2013. PMID 23060045.
- Messinger YH et al. Successful immune tolerance induction to enzyme replacement therapy in CRIM-negative infantile Pompe disease. *Genet Med* 2012. PMID 22237443.
- Meslier Y et al. Bortezomib delays the onset of factor VIII inhibitors in experimental hemophilia A, but fails to eliminate established anti-factor VIII IgG-producing cells. *J Thromb Haemost* 2011. PMID 21251202.
- Barnes C et al. Induction of immune tolerance using rituximab in a child with severe haemophilia B with inhibitors and anaphylaxis to factor IX. *Haemophilia* 2010. PMID 20546030.
- Kessel C et al. Humoral immune responsiveness to a defined epitope on factor VIII before and after B cell ablation with rituximab. *Mol Immunol* 2008. PMID 18715645.
- Hay C et al. Current and future approaches to inhibitor management and aversion. *Semin Thromb Hemost* 2006. PMID 16804831.

## G — Solid-tumour anti-murine-antibody precedent (14)

- Eger C et al. Generation and Characterization of a Human/Mouse Chimeric GD2-Mimicking Anti-Idiotype Antibody Ganglidiximab for Active Immunotherapy against Neuroblastoma. *PLoS One* 2016. PMID 26967324.
- Kushner BH et al. Prolonged progression-free survival after consolidating second or later remissions of neuroblastoma with Anti-GD2 immunotherapy and isotretinoin: a prospective Phase II study. *Oncoimmunology* 2015. PMID 26140243.
- Kushner BH et al. High-dose cyclophosphamide inhibition of humoral immune response to murine monoclonal antibody 3F8 in neuroblastoma patients: broad implications for immunotherapy. *Pediatr Blood Cancer* 2007. PMID 16421906.
- Gonzales NR et al. Minimizing immunogenicity of the SDR-grafted humanized antibody CC49 by genetic manipulation of the framework residues. *Mol Immunol* 2003. PMID 14522015.
- Richman CM et al. Dosimetry-based therapy in metastatic breast cancer patients using 90Y monoclonal antibody 170H.82 with autologous stem cell support and cyclosporin A. *Clin Cancer Res* 1999. PMID 10541370.
- Albertini MR et al. Systemic interleukin-2 modulates the anti-idiotypic response to chimeric anti-GD2 antibody in patients with melanoma. *J Immunother Emphasis Tumor Immunol* 1996. PMID 8877722.
- Dhingra K et al. Phase I clinical and pharmacological study of suppression of human antimouse antibody response to monoclonal antibody L6 by deoxyspergualin. *Cancer Res* 1995. PMID 7606728.
- Divgi CR et al. Pilot radioimmunotherapy trial with 131I-labeled murine monoclonal antibody CC49 and deoxyspergualin in metastatic colon carcinoma. *Clin Cancer Res* 1995. PMID 9815950.
- Kimball JA et al. The OKT3 Antibody Response Study: a multicentre study of human anti-mouse antibody (HAMA) production following OKT3 use in solid organ transplantation. *Transpl Immunol* 1995. PMID 8581409.
- Weiden PL et al. Human anti-mouse antibody suppression with cyclosporin A. *Cancer* 1994. PMID 8306252.
- Rettenbacher L et al. [Anaphylactic shock after repeated injection of 99mTc-labeled CEA antibody]. *Nuklearmedizin* 1994. PMID 8090628.
- Hammond EA et al. Prevention of adverse clinical outcome by monitoring of cardiac transplant patients for murine monoclonal CD3 antibody (OKT3) sensitization. *Transplantation* 1993. PMID 8497882.
- Tjandra JJ et al. Development of human anti-murine antibody (HAMA) response in patients. *Immunol Cell Biol* 1990. PMID 1711007.
- Ledermann JA et al. Repeated antitumour antibody therapy in man with suppression of the host response by cyclosporin A. *Br J Cancer* 1988. PMID 3265333.

## H — Lymphodepletion and concomitant immunosuppression (8)

- Christodoulou I et al. Comparative Analysis of Lymphodepletion Regimens in CART-19 Treatment for Relapsed/Refractory Diffuse Large B Cell Lymphoma. *Transplant Cell Ther* 2026. PMID 41183747.
- Synnott D et al. Systematic Review of Immunosuppression After Chimeric Antigen Receptor T-Cell Therapy for Posttransplant Lymphoproliferative Disorder. *Kidney Int Rep* 2026. PMID 41907816.
- Ozog S et al. Influence of B cell-lineage targeted CAR-T cell therapy on humoral immunity and vaccine-induced antibody response. *Nat Commun* 2026. PMID 41942445.
- Roddie C et al. Matched donor allogeneic CAR-T for adult B-ALL: toxicity, efficacy, repeat dosing, and the importance of lymphodepletion. *Blood* 2025. PMID 40643148.
- Aleissa MM et al. Severe Acute Respiratory Syndrome Coronavirus 2 Vaccine Immunogenicity among Chimeric Antigen Receptor T Cell Therapy Recipients. *Transplant Cell Ther* 2023. PMID 36906276.
- Iqbal M et al. Impact of Rituximab and Corticosteroids on Late Cytopenias Post-Chimeric Antigen Receptor T Cell Therapy. *Transplant Cell Ther* 2022. PMID 35842124.
- Walti CS et al. Humoral immunogenicity of the seasonal influenza vaccine before and after CAR-T-cell therapy: a prospective observational study. *J Immunother Cancer* 2021. PMID 34702753.
- Graalmann T et al. B cell depletion impairs vaccination-induced CD8+ T cell responses in a type I interferon-dependent manner. *Ann Rheum Dis* 2021. PMID 34226189.

## I — Confusables (not evidence) (9)

- BrainChild Bio, Inc (sponsor). Illuminate: a phase 2 pivotal study of BCB-276, a B7-H3-specific CAR T cell locoregional immunotherapy for DIPG - NCT07680439. *ClinicalTrials.gov* 2026. https://clinicaltrials.gov/study/NCT07680439.
- Li Y et al. Rituximab potentially improves clinical outcomes of CAR-T therapy for r/r B-ALL via sensitizing leukemia cells to CAR-T-mediated cytotoxicity and reducing CAR-T exhaustion. *Cell Oncol (Dordr)* 2024. PMID 38662336.
- Xiong X et al. Functional Validation of the RQR8 Suicide /Marker Gene in CD19 CAR-T Cells and CLL1CAR-T Cells. *Ann Hematol* 2023. PMID 37086278.
- Mosti L et al. Targeted multi-epitope switching enables straightforward positive/negative selection of CAR T cells. *Gene Ther* 2021. PMID 33526841.
- Sang W et al. Phase II trial of co-administration of CD19- and CD20-targeted chimeric antigen receptor T cells for relapsed and refractory diffuse large B cell lymphoma. *Cancer Med* 2020. PMID 32608579.
- Viaud S et al. Switchable control over in vivo CAR T expansion, B cell depletion, and induction of memory. *Proc Natl Acad Sci U S A* 2018. PMID 30373813.
- Philip B et al. A highly compact epitope-based marker/suicide gene for easier and safer T-cell therapy. *Blood* 2014. PMID 24970931.
- van Loenen MM et al. Multi-cistronic vector encoding optimized safety switch for adoptive therapy with T-cell receptor-modified T cells. *Gene Ther* 2013. PMID 23364317.
- Griffioen M et al. Retroviral transfer of human CD20 as a suicide gene for adoptive T-cell therapy. *Haematologica* 2009. PMID 19734426.

## J — Premedication and infusion reactions (15)

- Nguyen NN et al. Comparison of H1 versus combined H1/H2 antagonist premedication on incidence of rituximab infusion-related reaction: A retrospective cohort study *Journal of oncology pharmacy practice : official publication of the International Society of Oncology Pharmacy Practitioners* 2026. PMID 42530421.
- El Shenawy Z et al. Reevaluating corticosteroid premedication for rituximab: a retrospective cohort study *Leukemia & lymphoma* 2026. PMID 41789935.
- Bovens P et al. Oral glucocorticoid premedication for preventing infusion-related reactions to rituximab in rheumatoid arthritis *Scandinavian journal of rheumatology* 2026. PMID 41572843.
- Kitahiro Y et al. Efficacy of bepotastine compared with hydroxyzine in preventing rituximab-induced infusion-related reactions in non-hodgkin lymphoma patients: a phase II, double-blind, multicenter, and randomized trial *International journal of clinical oncology* 2026. PMID 41989666.
- Candar Ö et al. Management of Rituximab-Associated Hypersensitivity Reactions with Successfully Applied Desensitization Protocols: A Clinical Experience of 46 Infusions in 11 Patients *Journal of clinical medicine* 2026. PMID 42279029.
- Feltesse C et al. Severe Reactions to Rituximab in Children: A Cohort Study of Rituximab-Induced Serum Sickness and Anaphylaxis *Children (Basel, Switzerland)* 2026. PMID 42073020.
- Mori F et al. Immediate and delayed hypersensitivity to biologicals in children-A practical approach: An EAACI task force report *Pediatric allergy and immunology : official publication of the European Society of Pediatric Allergy and Immunology* 2026. PMID 41937341.
- Barroso A et al. Management of infusion-related reactions in cancer therapy: strategies and challenges *ESMO open* 2024. PMID 38452439.
- Karlsen EA et al. Steroid Premedication and Monoclonal Antibody Therapy: Should We Reconsider? *Current treatment options in oncology* 2024. PMID 38270799.
- Ding J et al. A novel prednisone premedication protocol significantly decreases infusion‑related reactions of rituximab in newly diagnosed diffuse large B‑cell lymphoma *Oncology letters* 2023. PMID 37205922.
- Cáceres MC et al. The importance of early identification of infusion-related reactions to monoclonal antibodies *Therapeutics and clinical risk management* 2019. PMID 31447561.
- Vogel WH. Infusion reactions: diagnosis, assessment, and management *Clinical journal of oncology nursing* 2010. PMID 20350882.
- Tuthill M et al. Rapid infusion of rituximab over 60 min *European journal of haematology* 2009. PMID 19220420.
- Sehn LH et al. Rapid infusion rituximab in combination with corticosteroid-containing chemotherapy or as maintenance therapy is well tolerated and can safely be delivered in the community setting *Blood* 2007. PMID 17244675.
- Salar A et al. Rapid infusion of rituximab with or without steroid-containing chemotherapy: 1-yr experience in a single institution *European journal of haematology* 2006. PMID 16856919.

## K — Screening, prophylaxis, and late effects (21)

- Lee E et al. Infectious complications after CAR T-cell therapy: mechanisms, risk stratification, and prevention *Blood research* 2026. PMID 42274870.
- Kamboj M et al. Vaccination of Adults With Cancer: ASCO Guideline *Journal of clinical oncology : official journal of the American Society of Clinical Oncology* 2024. PMID 38498792.
- Athni TS et al. Hypogammaglobulinemia, late-onset neutropenia, and infections following rituximab *Annals of allergy, asthma & immunology : official publication of the American College of Allergy, Asthma, & Immunology* 2023. PMID 36706910.
- Wat J et al. Hypogammaglobulinemia After Chimeric Antigen Receptor (CAR) T-Cell Therapy: Characteristics, Management, and Future Directions *The journal of allergy and clinical immunology. In practice* 2022. PMID 34757064.
- Hayden PJ et al. Management of adults and children receiving CAR T-cell therapy: 2021 best practice recommendations of the European Society for Blood and Marrow Transplantation (EBMT) and the Joint Accreditation Committee of ISCT and EBMT (JACIE) and the European Haematology Association (EHA) *Annals of oncology : official journal of the European Society for Medical Oncology* 2022. PMID 34923107.
- Moor MB et al. Humoral and cellular responses to mRNA vaccines against SARS-CoV-2 in patients with a history of CD20 B-cell-depleting therapy (RituxiVac): an investigator-initiated, single-centre, open-label study *The Lancet. Rheumatology* 2021. PMID 34514436.
- Walti CS et al. Antibodies against vaccine-preventable infections after CAR-T cell therapy for B cell malignancies *JCI insight* 2021. PMID 33914708.
- Hwang JP et al. Hepatitis B Virus Screening and Management for Patients With Cancer Prior to Therapy: ASCO Provisional Clinical Opinion Update *Journal of clinical oncology : official journal of the American Society of Clinical Oncology* 2020. PMID 32716741.
- Bar-Or A et al. Effect of ocrelizumab on vaccine responses in patients with multiple sclerosis: The VELOCE study *Neurology* 2020. PMID 32727835.
- Yakoub-Agha I et al. Management of adults and children undergoing chimeric antigen receptor T-cell therapy: best practice recommendations of the European Society for Blood and Marrow Transplantation (EBMT) and the Joint Accreditation Committee of ISCT and EBMT (JACIE) *Haematologica* 2020. PMID 31753925.
- Hill JA et al. CAR-T - and a side order of IgG, to go? - Immunoglobulin replacement in patients receiving CAR-T cell therapy *Blood reviews* 2019. PMID 31416717.
- Barmettler S et al. Association of Immunoglobulin Levels, Infectious Risk, and Mortality With Rituximab and Hypogammaglobulinemia *JAMA network open* 2018. PMID 30646343.
- Loomba R et al. Hepatitis B Reactivation Associated With Immune Suppressive and Biological Modifier Therapies: Current Concepts, Management Strategies, and Future Directions *Gastroenterology* 2017. PMID 28219691.
- Hwang JP et al. Hepatitis B Virus Screening for Patients With Cancer Before Therapy: American Society of Clinical Oncology Provisional Clinical Opinion Update *Journal of clinical oncology : official journal of the American Society of Clinical Oncology* 2015. PMID 25964247.
- Huang YH et al. Randomized controlled trial of entecavir prophylaxis for rituximab-associated hepatitis B virus reactivation in patients with lymphoma and resolved hepatitis B *Journal of clinical oncology : official journal of the American Society of Clinical Oncology* 2013. PMID 23775967.
- Casulo C et al. Incidence of hypogammaglobulinemia in patients receiving rituximab and the use of intravenous immunoglobulin for recurrent infections *Clinical lymphoma, myeloma & leukemia* 2013. PMID 23276889.
- Tesfa D et al. Late-onset neutropenia following rituximab therapy in rheumatic diseases: association with B lymphocyte depletion and infections *Arthritis and rheumatism* 2011. PMID 21560117.
- Howard SC et al. The tumor lysis syndrome *The New England journal of medicine* 2011. PMID 21561350.
- Wolach O et al. Late-onset neutropenia after rituximab treatment: case series and comprehensive review of the literature *Medicine* 2010. PMID 20827108.
- Yeo W et al. Hepatitis B virus reactivation in lymphoma patients with prior resolved hepatitis B undergoing anticancer therapy with or without rituximab *Journal of clinical oncology : official journal of the American Society of Clinical Oncology* 2009. PMID 19075267.
- Carson KR et al. Progressive multifocal leukoencephalopathy after rituximab therapy in HIV-negative patients: a report of 57 cases from the Research on Adverse Drug Events and Reports project *Blood* 2009. PMID 19264918.

## L — Dose, route, and pharmacokinetics (9)

- Hartinger JM et al. Prevalence of anti-rituximab antibodies in autoimmune forms of glomerulonephritis and podocytopathies *Nephrology, dialysis, transplantation : official publication of the European Dialysis and Transplant Association - European Renal Association* 2026. PMID 42340364.
- Wang D et al. The impact of anti-rituximab antibodies on rituximab efficacy in children with frequently relapsing or steroid-dependent nephrotic syndrome *Pediatric nephrology (Berlin, Germany)* 2026. PMID 42481732.
- Harirchian MH et al. The Sanctuary Within: Development of CD20+ CNS Lymphoma Despite Peripheral B-Cell Depletion by Rituximab in a Multiple Sclerosis Patient *Case reports in neurological medicine* 2026. PMID 42211720.
- Lee GY et al. Retrospective Review of Intra-Cerebrospinal Fluid (CSF) Drug Delivery in CNS Malignancies: Safety, Clinical Efficacy and Pharmacokinetic Profiles of Intracerebroventricular (ICV), Lumbar Intrathecal (LIT), and Intra-Cisterna Magna (ICM) Injections *Cancers* 2025. PMID 40282439.
- Hartinger JM et al. Implications of rituximab pharmacokinetic and pharmacodynamic alterations in various immune-mediated glomerulopathies and potential anti-CD20 therapy alternatives *Frontiers in immunology* 2022. PMID 36420256.
- Locke KW et al. ENHANZE<sup>®</sup> drug delivery technology: a novel approach to subcutaneous administration using recombinant human hyaluronidase PH20 *Drug delivery* 2019. PMID 30744432.
- Cohen HP et al. Switching Reference Medicines to Biosimilars: A Systematic Literature Review of Clinical Outcomes *Drugs* 2018. PMID 29500555.
- Ryman JT et al. Pharmacokinetics of Monoclonal Antibodies *CPT: pharmacometrics & systems pharmacology* 2017. PMID 28653357.
- Shpilberg O et al. Subcutaneous administration of rituximab (MabThera) and trastuzumab (Herceptin) using hyaluronidase *British journal of cancer* 2013. PMID 24002601.

## M — CAR-T round context (10)

- Ronsley R et al. Tumor inflammation-associated neurotoxicity in children with diffuse intrinsic pontine glioma receiving B7-H3-targeting CAR T cells on BrainChild-03 *Neuro-oncology practice* 2026. PMID 41798119.
- Ramsoomair CK et al. Locoregional delivery of CAR T cells in high-grade gliomas: a systematic analysis of safety, efficacy, and emerging biomarkers of response *Journal for immunotherapy of cancer* 2026. PMID 41895715.
- Canelo-Vilaseca M et al. Lymphodepletion chemotherapy in chimeric antigen receptor-engineered T (CAR-T) cell therapy in lymphoma *Bone marrow transplantation* 2025. PMID 40148484.
- Varela-González-Aller J et al. Towards Personalized Lymphodepletion: A Population Pharmacokinetic Fludarabine Model in Patients Receiving CAR T-Cell Therapy *Pharmaceutics* 2025. PMID 41471106.
- Panetta JC et al. Age-adjusted dosing of fludarabine for lymphodepletion in CAR T-cell therapy: a clinical trial simulation study *Blood advances* 2025. PMID 40609087.
- Wicha SG et al. Chimeric antigen receptor T-cell therapy and fludarabine: precision dosing imperatives *Blood advances* 2024. PMID 38191740.
- Bagley SJ et al. Intrathecal bivalent CAR T cells targeting EGFR and IL13Rα2 in recurrent glioblastoma: phase 1 trial interim results *Nature medicine* 2024. PMID 38480922.
- Vitanza NA et al. Intraventricular B7-H3 CAR T Cells for Diffuse Intrinsic Pontine Glioma: Preliminary First-in-Human Bioactivity and Safety *Cancer discovery* 2023. PMID 36259971.
- Donovan LK et al. Locoregional delivery of CAR T cells to the cerebrospinal fluid for treatment of metastatic medulloblastoma and ependymoma *Nature medicine* 2020. PMID 32341580.
- Lee DW et al. ASTCT Consensus Grading for Cytokine Release Syndrome and Neurologic Toxicity Associated with Immune Effector Cells *Biology of blood and marrow transplantation : journal of the American Society for Blood and Marrow Transplantation* 2019. PMID 30592986.

## N — Procedural fasting guidelines (4)

- Joshi GP et al. 2023 American Society of Anesthesiologists Practice Guidelines for Preoperative Fasting: Carbohydrate-containing Clear Liquids with or without Protein, Chewing Gum, and Pediatric Fasting Duration-A Modular Update of the 2017 American Society of Anesthesiologists Practice Guidelines for Preoperative Fasting *Anesthesiology* 2023. PMID 36629465.
- Frykholm P et al. Pre-operative fasting in children: A guideline from the European Society of Anaesthesiology and Intensive Care *European journal of anaesthesiology* 2022. PMID 34857683.
- ASA Task Force on Preoperative Fasting. Practice Guidelines for Preoperative Fasting and the Use of Pharmacologic Agents to Reduce the Risk of Pulmonary Aspiration: Application to Healthy Patients Undergoing Elective Procedures: An Updated Report by the American Society of Anesthesiologists Task Force on Preoperative Fasting and the Use of Pharmacologic Agents to Reduce the Risk of Pulmonary Aspiration *Anesthesiology* 2017. PMID 28045707.
- Smith I et al. Perioperative fasting in adults and children: guidelines from the European Society of Anaesthesiology *European journal of anaesthesiology* 2011. PMID 21712716.
