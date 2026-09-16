# Cytokine support and armouring

Cytokines act at three separate points — ex vivo expansion, ex vivo differentiation (state programming), and
in vivo support after infusion — and the literature is clearest when those are kept apart.

## IL-2 versus IL-15

- IL-15 activates human NK cells through IL-2R components (Carson 1994, PMID 7523571) and IL-15
  trans-presentation drives NK development and differentiation in vivo (PMID 19103877).
- Clinically, systemic IL-2 supports infused NK expansion (Miller 2005, PMID 15632206) but also expands
  regulatory T cells; depleting Tregs with an IL-2-diphtheria-toxin fusion raised the in vivo NK expansion rate
  from 10% to 27% of patients and improved AML clearance (Bachanova 2014, PMID 24719405).
- The field has therefore moved to **IL-15-based support** (IL-15 super-agonist N-803, IL-15/IL-15Rα-Fc) or to
  **cell-intrinsic IL-15** so no systemic cytokine is needed.

## Preactivation: IL-12 + IL-15 + IL-18 (CIML)

Covered in detail in `01_phenotypes_and_cell_states.md`. Manufacturing-relevant points:

- The stimulus is **brief** (12–16 h) and therefore easy to insert at the end of an existing process
  (Romee 2012, PMID 22983442; 2016, PMID 27655849).
- It is compatible with feeder expansion (PM21 particles + cytokines, PMID 38711506), with engager
  pre-complexing (PMID 33986022) and with CAR transduction (PMID 38996027).
- IL-27 augments IL-15/IL-18-mediated activation (PMID 31277710), and DNMT1 inhibition further improves CIML
  activity (PMID 39704855) — both examples of tuning the priming cocktail rather than replacing it.

## IL-21: the expansion cytokine

IL-21 is used less for effector programming than for **proliferative capacity**, almost always as a
membrane-bound feeder ligand (see `07_expansion_and_gmp_manufacturing.md`):

- Membrane-bound IL-21 aAPCs support >10,000-fold expansion over 5 weeks with retained cytotoxicity and
  increased metabolic activation (PMID 31624330; PMID 21339714).
- Short soluble IL-21 exposure combined with K562-OX40L feeders is an alternative (PMID 31105701).
- IL-21 with autologous feeder cells in a CliniMACS Prodigy workflow supports clinical-grade CAR-NK generation
  (PMID 28810809).

## Cytokine armouring of the product

The dominant strategy for persistence without systemic cytokine toxicity:

| Design | Evidence |
|---|---|
| Membrane-bound / intracellular IL-15 in NK-92 | PMID 22310931 — IL-15 transduction enriches gene-modified effectors and removes IL-2 dependence |
| Secreted IL-15 + CD19 CAR in cord-blood NK | Liu 2018, PMID 28725044 → clinical (PMID 32023374, PMID 38238616) |
| IL-15/IL-15Rα fusion in iPSC-NK (FT596) | PMID 39798981 |
| Soluble IL-15 in cord-blood TRACK NK | PMID 38572955; interim clinical report PMID 39903538 |
| IL-15 + *CISH* knockout | PMID 32902645, PMID 32531207 |
| Neoleukin-2/15 mutein secretion (c-Myc/NRF1) | PMID 40025022 |
| Rimiducid-inducible MyD88/CD40 + IL-15 | PMID 32384544 |
| IL-15 in the engager rather than the cell (TriKE) | PMID 26847056, PMID 40694640 |
| Decoy-resistant IL-18 delivered in trans | PMID 39367093 |
| IL-15/IL-15Rα from an oncolytic virus + CAR-NK | OV-IL15C + EGFR-CAR NK |
| IL-15/4-1BBL ex vivo activation before infusion | PMID 25452614 — note: associated with acute GvHD after T-cell-depleted HSCT |

Two cautions run through this table:

1. **IL-15 armouring is not free.** The IL-15/4-1BBL-activated NK trial reported acute GvHD after T-cell
   depleted transplant (PMID 25452614), and unregulated IL-15 raises theoretical risks of NK-cell autonomy;
   inducible or membrane-restricted designs exist for that reason.
2. **Armouring compensates for, but does not replace, metabolic fitness.** CAR-NK relapse was driven by
   metabolic collapse and was rescued *by cytokine engineering* (PMID 37494448) — the two axes are coupled
   (see `08_metabolism_persistence_trafficking.md`).

## Practical schedule for a modern process

1. **Expansion phase:** IL-2 or IL-15 with membrane-bound IL-21/4-1BBL feeder or particle stimulation.
2. **Programming phase (final 12–16 h):** IL-12 + IL-15 + IL-18 to install the memory-like state.
3. **In vivo support:** cell-intrinsic IL-15 (secreted, membrane-bound or fusion) and/or an IL-15-containing
   engager; if systemic cytokine is used, prefer IL-15 super-agonist over IL-2 and consider Treg depletion.
