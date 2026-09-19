# What actually makes an NK product good: the decisions that matter

This collection (313 papers, 1993–2026) is read from a product point of view: **which advances change a design
decision, which failure modes destroy products, and where the evidence genuinely supports a choice versus where
it only supports an option.** Papers that describe biology without a design consequence stay in `REPORT.md`.

There is no single best NK product — the right design depends on target tissue, whether the antigen is shared
with NK cells, how many modifications you can afford to characterise, and whether you are optimising for speed
to clinic or for platform economics. What *is* well supported is a short list of levers, a shorter list of
failure modes, and a set of trade-offs that are now well enough characterised to be made deliberately rather
than by default.

## The central claim

**NK therapy's unsolved problem is potency-duration, not target recognition.** Safety is settled: no GvHD and
essentially no CRS/ICANS across allogeneic, cord-blood, iPSC-derived and cell-line products (PMID 32023374,
PMID 38238616, PMID 39798981, PMID 40251398, PMID 37148198). But infused NK cells kill well for days and then
stop mattering.

Two lines of evidence make this concrete rather than rhetorical:

- Preclinical CAR-NK relapse was driven by **loss of metabolic fitness, not antigen escape**, and was rescued by
  cytokine engineering (PMID 37494448).
- Cryopreserved NK cells pass conventional degranulation and release assays while losing **3-D migration and
  killing** (PMID 33067467) — so a product can meet specification and still be functionally inert in tissue.

Everything that has moved a clinical needle addresses potency-duration (cell-intrinsic IL-15, memory-like
programming, lymphodepletion with Treg control, protected CD16); most of what limits products is a
manufacturing-coupled fitness problem (metabolic collapse, TME reprogramming, CD16 shedding,
trogocytosis-driven fratricide, cryo damage). That is the lens for the rest of these notes.

## The levers, ranked by evidence per unit of engineering cost

1. **Cell-intrinsic IL-15, or IL-15 built into the engager.** Present in essentially every NK product with a
   clear clinical response signal (PMID 28725044 → PMID 32023374, PMID 38238616; PMID 39798981; PMID 26847056).
   Known risk: unregulated IL-15 was associated with acute GvHD after T-depleted HSCT (PMID 25452614), so
   tethered, fused or inducible designs exist for a reason (PMID 32384544).
2. **Host conditioning.** Free — a regimen, not a product change. Lymphodepletion enables expansion at all
   (PMID 15632206); adding Treg depletion moved in vivo NK expansion from 10% to 27% of patients with improved
   AML clearance (PMID 24719405).
3. **Memory-like (IL-12+IL-15+IL-18) programming.** 12–16 h appended to an existing process, epigenetically
   encoded rather than transient (PMID 22983442, PMID 38941480), with clinical expansion and persistence data in
   two settings (PMID 27655849, PMID 35349491).
4. **Protected CD16 (hnCD16 or ADAM17 blockade).** One module that converts single-round killers into serial
   killers (PMID 41116262, PMID 39666369) and strengthens every antibody or engager combination
   (PMID 31856277, PMID 39053944).
5. **Brake knockouts, in order of evidence: *CISH* → *KLRC1*/NKG2A → TGF-β resistance.** The strongest
   preclinical case for solid tumours; clinical readouts immature; each edit adds safety-characterisation
   burden (PMID 41425600), which is why edit count is an economic decision as much as a biological one.

## The six decisions worth arguing about

Each is treated properly in `04_design_decisions.md`; in short:

| Decision | Options that survive scrutiny | What tips it |
|---|---|---|
| **Cell source** | cord blood; iPSC; peripheral blood; NK-92 for locoregional | number of modifications you must characterise, and doses per lot |
| **Specificity** | IL-15-containing engager vs CAR vs both | retargeting flexibility and transduction burden vs antigen-density control |
| **Persistence** | armour the cell vs put IL-15 in the engager vs support the host | how much regulatory control you want over IL-15 exposure |
| **Edit count** | 0–2 (per-donor products) vs 4–6 (clonal bank) | translocation/clonality characterisation cost, not editing efficiency |
| **Expansion** | feeder cells vs cell-free particles vs feeder-free media | yield versus residual-cell testing and GMP feeder-bank burden |
| **Cryopreservation** | DMSO standard vs DMSO-minimised vs post-thaw rescue | whether your potency assay can even detect the damage |

## Where I would not spend the next dollar

- **Novel CAR targets as the primary research investment.** Two independent solid-tumour CAR-NK reviews converge
  on trafficking, persistence and TME suppression as the limiting factors (PMID 38245520, PMID 39134804), and
  in vivo relapse was metabolic rather than antigenic (PMID 37494448).
- **Systemic IL-2 support**, which expands Tregs — IL-15 super-agonist or cell-intrinsic IL-15 dominates it.
- **Elaborate logic gates before fitness is solved.** synNotch conversion of TIGIT/CD73 into activating inputs
  (PMID 38429294) is excellent science, but a logic-gated cell that dies in 72 hours still dies in 72 hours.
- **Fresh-only products.** The right response to cryo damage is a better formulation and a better potency assay
  (`03_failure_modes.md`, `05_potency_and_release.md`), not avoiding the freeze that off-the-shelf logistics
  require.
- **Autologous NK products** for most indications: patient NK cells are functionally impaired (PMID 20849361,
  PMID 40019438), forfeiting the platform's main advantage.

## Reading order

- `01_scientific_advances.md` — advances tiered by whether they change a decision.
- `02_manufacturing_advances.md` — process advances with numbers, and the platform comparison nobody has run.
- `03_failure_modes.md` — ranked failure modes, mechanisms, and the mitigation each implies.
- `04_design_decisions.md` — the six decisions, with the case for each option and when it wins.
- `05_potency_and_release.md` — why standard release testing misses the thing that matters, and what to measure.
- `06_clinical_evidence_and_open_questions.md` — trial-by-trial anchors, and what would change this thesis.
