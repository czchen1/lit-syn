# The product thesis: what is the best NK product we can build, and why

This collection (313 papers, 1993–2026) is read for one purpose: **to specify the best NK-cell cancer product
that current evidence supports, and to say why each element is in it and what it displaces.** Everything that
does not change a design decision is background.

## The core argument in six sentences

NK-cell therapy's safety profile is settled — no GvHD, essentially no CRS/ICANS across allogeneic, cord-blood,
iPSC and cell-line products (PMID 32023374, PMID 38238616, PMID 39798981, PMID 40251398, PMID 37148198). What
is not settled is **potency-duration**: infused NK cells kill well for days and then stop mattering. Every
advancement that has actually moved a clinical needle addresses potency-duration rather than target
recognition — cell-intrinsic IL-15, memory-like programming, lymphodepletion with Treg control, protected
CD16. Conversely, the dominant failure modes are not antigen escape (the CAR-T failure mode) but **metabolic
collapse, TME reprogramming, CD16 shedding, trogocytosis-driven fratricide, and cryopreservation damage** —
all of which are product-manufacturing problems as much as biology problems. Therefore the best product is not
"the most sophisticated CAR" but **the most fitness-protected effector, manufactured in a process that does not
destroy the fitness it was engineered for**. The rest of this note is that spec.

## Recommendation: two products, not one

The evidence supports different answers for "build now" and "build for the platform".

### Product A — near-term, highest probability of clinical benefit

**Cord-blood-derived, feeder-expanded, memory-like-programmed NK cells, cryopreserved, dosed repeatedly with an
IL-15-containing engager, after lymphodepletion.**

No CAR. Specificity comes from the engager (TriKE/AFM13-class), which also supplies IL-15.

Why this and not a CAR product:
- Every element has **clinical** support: CB expansion (PMID 24204673), CIML programming (PMID 27655849,
  PMID 35349491), engager pre-complexing in patients refractory to both brentuximab and checkpoint blockade
  (PMID 40186077), IL-15-in-the-engager for persistence (PMID 26847056), repeat dosing (PMID 40251398),
  Treg-depleting lymphodepletion tripling in vivo expansion (PMID 24719405).
- It removes the three highest-risk failure modes of CAR-NK in one stroke: no transduction step (no VCN,
  clonality or vector-supply constraints), no CAR-driven trogocytosis/fratricide (PMID 36175679), and target
  swapping requires a new *reagent*, not a new *product*.
- Manufacturing is short and cheap: 10–14 days, one banked CB unit yields many doses, engager loaded at
  formulation, and the complex survives freezing (PMID 35225870).

Cost: it depends on CD16, so it inherits shedding (mitigated with an ADAM17 inhibitor, PMID 39053944) and it
will not solve solid tumours.

### Product B — the platform worth building, 3–5 year horizon

**iPSC-derived NK cells, clonal master bank, with:**

| Module | Purpose | Evidence |
|---|---|---|
| NK-native CAR (NKG2D-TM + 2B4 + CD3ζ), empirically costim-screened | antigen specificity that actually signals in NK cells | PMID 30082067; CD28/LCK surprise PMID 38900051 |
| IL-15/IL-15Rα fusion (membrane-tethered or inducible) | persistence without systemic cytokine | PMID 39798981, PMID 28725044, PMID 32384544 |
| hnCD16 (high-affinity, non-cleavable) | ADCC + serial killing + engager compatibility | PMID 31856277, PMID 41116262 |
| *CISH* KO | cytokine-signalling brake; IL-15 independence | PMID 32531207, PMID 32902645 |
| *KLRC1*/NKG2A KO | resist HLA-E inhibition | PMID 39349459, PMID 37675109 |
| TGF-β resistance (*SMAD4* KO or dnTGFBR2) | block TME reprogramming and NK→ILC1 conversion | PMID 40119192, PMID 38986609, PMID 28759001 |
| Target-antigen KO where shared with NK (e.g. CD38) | prevent fratricide | PMID 32603414, PMID 33375774 |
| Terminal IL-12/15/18 preactivation | memory-like state at the moment of infusion | PMID 22983442, PMID 27655849 |

Why iPSC rather than cord blood for the platform: **six or more edits plus a CAR is not a per-donor process.**
Clonal selection, sequencing verification and one-time safety characterisation are only economic on a master
bank, and multiplex-edited iNK products already exist clinically (PMID 39798981). Cord blood remains the better
substrate for one- or two-modification products.

Why *not* NK-92 for either: irradiation before infusion removes persistence, which is the exact variable that
determines efficacy. NK-92 remains a good vehicle for locoregional dosing (intracranial HER2-CAR NK-92,
PMID 37148198) and for cheap preclinical/CMC development.

## The five levers, ranked by evidence per unit of engineering cost

1. **Cell-intrinsic IL-15 (or IL-15 in the engager).** Present in essentially every NK product with a clear
   clinical response signal. Highest return, well-characterised risk (unregulated IL-15 → GvHD signal after
   T-depleted HSCT, PMID 25452614; use tethered/inducible designs).
2. **Host conditioning: lymphodepletion + Treg control.** Free — it is a regimen, not a product change — and it
   moved in vivo NK expansion from 10% to 27% of patients with improved AML clearance (PMID 24719405).
3. **Memory-like (IL-12/15/18) programming.** 12–16 hours appended to an existing process; epigenetically
   stable (PMID 38941480); clinical expansion/persistence data in two settings.
4. **Protected CD16 (hnCD16 or ADAM17 blockade).** One module; converts single-round killers into serial
   killers (PMID 41116262, PMID 39666369) and makes every antibody/engager combination stronger.
5. **Brake knockouts (CISH → NKG2A → TGF-β).** Strongest preclinical case for solid tumours, immature clinical
   readout, and each edit adds safety-characterisation burden (PMID 41425600). Worth it on a clonal bank, hard
   to justify per-donor.

## What I would cut

- **Novel CAR targets as the primary research investment.** Antigen choice is not the bottleneck; two
  independent solid-tumour CAR-NK reviews converge on trafficking, persistence and TME suppression instead
  (PMID 38245520, PMID 39134804), and CAR-NK relapse in vivo was metabolic, not antigenic (PMID 37494448).
- **Systemic IL-2 support.** It expands Tregs; IL-15 super-agonist or cell-intrinsic IL-15 dominates it.
- **Elaborate logic gates before fitness is solved.** synNotch-programmed TIGIT/CD73 conversion
  (PMID 38429294) is elegant, but a logic-gated cell that dies in 72 hours is still a cell that dies in 72
  hours.
- **Fresh-only products.** They cannot be a commercial off-the-shelf product; the correct response to
  cryopreservation damage is to fix the formulation and the potency assay (`03_failure_modes.md`), not to avoid
  freezing.
- **Autologous NK products for most indications.** Patient NK cells are functionally impaired (PMID 20849361,
  PMID 40019438), which forfeits the platform's main advantage.

## Reading order

- `01_scientific_advances.md` — the advances that earn a place in the spec, and the ones that don't yet.
- `02_manufacturing_advances.md` — the process advances, with numbers, and the unresolved platform comparison.
- `03_failure_modes.md` — ranked failure modes, mechanism, and the mitigation each implies.
- `04_product_spec_and_release.md` — the buildable spec, step by step, with the release panel.
- `05_evidence_base_and_open_questions.md` — clinical anchors, what is *not* established, and what would
  change this thesis.
- `REPORT.md` — the full 313-paper listing by axis (auto-generated).
