# The six design decisions, and the case for each option

Each decision below has more than one defensible answer. What the literature supports is a clear statement of
what you gain, what you accept, and which conditions tip the choice.

## 1. Cell source

| Option | Strongest case | What you accept | Tips toward it |
|---|---|---|---|
| **Cord blood** | Banked, HLA-typed, expands ~1,800–2,400-fold with aAPC feeders (PMID 24204673); substrate for the IL-15-armoured CD19 CAR-NK clinical programme (PMID 28725044 → PMID 32023374, PMID 38238616) and TRACK NK (PMID 38572955) | Immature phenotype (CD56bright-skewed, low KIR) needing priming; still a per-lot process | 1–2 modifications, fastest credible route to clinic |
| **iPSC** | Clonal bank makes multiplex editing economic; clinical proof with FT596 (CD19 CAR + hnCD16 + IL-15/IL-15Rα, PMID 39798981); feeder-free clinical-scale differentiation (PMID 31396935, PMID 23515118) | Differentiation protocol is a critical process parameter that changes phenotype and cytotoxicity (PMID 39445004); tumourigenicity and genomic characterisation burden | ≥3 edits, off-the-shelf economics, uniformity as a selling point |
| **Peripheral blood** | Mature, educated, immediately cytotoxic; enables KIR/HLA donor selection (PMID 20581313, PMID 30647027); the historical clinical base (PMID 15632206, PMID 21791425) | Donor variability, low starting frequency, T-cell depletion required | Donor-selection-driven strategies, transplant settings, academic trials |
| **NK-92 / cell lines** | Unlimited, consistent, cheap; safe at high doses (PMID 18836917, PMID 24094496); CAR versions clinically dosed intracranially (PMID 25373520 → PMID 37148198) | Irradiation before infusion removes persistence entirely | Locoregional dosing, frequent redosing, CMC and preclinical development |

Autologous products are the weakest option in most indications: patient NK cells are functionally impaired
(PMID 20849361, PMID 40019438).

## 2. Where specificity comes from: engager, CAR, or both

**Engager (IL-15-containing).** Specificity and persistence in one reagent (161533 TriKE, PMID 26847056);
retargeting means a new reagent, not a new product; no transduction step, so no VCN/clonality burden; clinical
responses in double-refractory CD30+ lymphoma with AFM13-precomplexed cord-blood NK cells (PMID 40186077);
NKp46-directed constructs escape CD16 dependence and CD64-mediated resistance (PMID 36635380, PMID 40694640).
Accept: CD16 dependence (failure mode #3) and a second agent to dose.

**CAR.** Direct control of antigen-density thresholds and signal strength, and the only route to targets with no
Fc-engager equivalent. Use NK-native architecture (NKG2D-TM + 2B4 + CD3ζ, PMID 30082067) but screen costimulation
empirically — CD28 works in NK cells despite not being expressed there (PMID 38900051), and CD3ζ-locus knock-in is
a viable alternative topology (PMID 38493479). Accept: transduction step, trogocytosis/fratricide risk
(PMID 36175679), one target per product.

**Both.** CAR plus a cytokine-activated/memory-like backbone is already clinical (CAR-CIML NK against mesothelin,
PMID 38996027), and CAR-T cells secreting BiKEs to recruit endogenous NK cells (PMID 40659834) show the field
expects effector classes to be combined rather than ranked.

## 3. How persistence is supplied

Three routes, and they are substitutes, not complements:

- **In the cell** — secreted IL-15 (PMID 28725044), IL-15/IL-15Rα fusion (PMID 39798981), membrane/intracellular
  IL-15 (PMID 22310931), or inducible MyD88/CD40 + IL-15 (PMID 32384544). Most persistence per dose; least
  regulatory control over exposure (GvHD signal, PMID 25452614).
- **In the engager** — IL-15 as a module of the TriKE (PMID 26847056). Exposure stops when dosing stops, which is
  the cleanest safety story; requires the engager to be part of the regimen forever.
- **In the host** — lymphodepletion plus Treg control (10% → 27% in vivo expansion, PMID 24719405), or IL-15
  super-agonist support (used with CIML NK plus CTLA-4 blockade in head and neck cancer, PMID 39948608). Cheapest,
  and it works on any product — but systemic IL-2 specifically should be avoided because it expands Tregs.

Pairing *CISH* knockout with any of these lowers the cytokine concentration needed (PMID 32531207,
PMID 32902645).

## 4. How many edits to take

This is an economics decision, not a biology decision: Cas9 RNP electroporation already reaches ~90% editing of
primary NK cells (PMID 31704085) and feeder activation improves it further (PMID 35222382). The constraint is
that multiplex editing raises translocation and clonality questions whose assessment frameworks are only now
being formalised (PMID 41425600).

Priority order if you can take *n* edits:

1. *CISH* — cytokine-signalling gain, persistence, IL-15 independence (PMID 32531207).
2. Protected CD16 — hnCD16 knock-in or *ADAM17* knockout (PMID 31856277, PMID 31704085); can be combined with a
   CD38 knockout in a single *CD38*-locus knock-in (PMID 35135865).
3. *KLRC1*/NKG2A — for HLA-E-high tumours (PMID 39349459, PMID 37675109).
4. TGF-β resistance — *SMAD4* knockout or dnTGFBR2, for solid tumours specifically (PMID 40119192,
   PMID 38986609).
5. Target-antigen knockout where the antigen is shared with NK cells (CD38 is the worked example,
   PMID 32603414).
6. Emerging, screen-derived: Regnase-1/*ZC3H12A* (PMID 38821052), *TIPE2* (PMID 36725083), Cbl-b
   (PMID 24553136), MED12/ARIH2-class hits (PMID 40845844, PMID 38918616).

For a per-donor product, 1–2 edits is the realistic ceiling; the 4–6 edit stack is what justifies a clonal iPSC
bank in the first place.

## 5. Expansion platform

| Option | Case | Accept |
|---|---|---|
| Engineered feeder cells (mbIL-21/4-1BBL) | Highest, best-replicated yields (PMID 19383914, PMID 24204673, PMID 31624330); also improves transduction (PMID 35222382, PMID 40325497) | GMP feeder bank, irradiation validation, residual-cell release testing |
| Cell-free particles (PM21) | Feeder-like expansion (~825-fold) without feeder cells, with in vivo data (PMID 27059202); with cytokines gives memory-like phenotype and better survival (PMID 38711506) | Particle manufacture and characterisation become your problem instead |
| Feeder-free media/ligands | Simplest CMC; closed automated feeder-free expansion is established (PMID 20795758) and integrates with non-viral editing of cryopreserved cells (PMID 33433623) | Generally lower yield; strategy landscape still consolidating (PMID 41089682) |

Vessel and automation are separable choices layered on top: gas-permeable static culture for absolute yield
(19 × 10⁹ cells, PMID 22900959), CliniMACS Prodigy for closure and integrated transduction (PMID 28810809,
PMID 38253870), stirred bioreactors for true scale-up (PMID 40808775) — the last being the least
evidence-backed for edited or CAR-transduced cells. Media/supplement choice is a potency variable in its own
right (PMID 39570247).

## 6. Cryopreservation strategy

Standard DMSO is the default and it demonstrably damages tissue-relevant function (PMID 33067467,
PMID 32536506). The options are not "freeze or not" — an off-the-shelf product must freeze — but:

- **DMSO-minimised / DMSO-free formulations**, benchmarked against CryoStor 10 and FBS+DMSO
  (PMID 41208818, PMID 42098076, PMID 42564981).
- **Intracellular nanoparticle protection**, which changes the cell rather than the buffer (PMID 32382476).
- **Post-thaw rescue** — brief co-culture restoring motility and killing after thaw (PMID 40966444).
- **Freeze the complex** where relevant: engager-precomplexed NK cells retain activity and specificity
  (PMID 35225870), which is what makes engager-based off-the-shelf logistics viable.

Whichever you choose, the decision is only meaningful if the potency assay can detect the damage — which is the
subject of `05_potency_and_release.md`.

## Two configurations these decisions produce

Not prescriptions — worked examples of coherent decision sets:

- **Fast, low-risk:** cord-blood NK, feeder- or PM21-expanded, terminal IL-12/15/18 programming, no edits,
  cryopreserved DMSO-minimised, dosed repeatedly with an IL-15-containing engager after Treg-depleting
  lymphodepletion. Every element has clinical support; specificity risk sits in a reagent, not the cell.
- **Platform play:** iPSC-derived NK, NK-native CAR + IL-15/IL-15Rα + hnCD16, *CISH*/*KLRC1*/TGF-β-resistance
  edits, feeder-free clinical-scale differentiation, terminal memory-like programming, released on a 3-D post-thaw
  potency assay. Higher characterisation burden, and the only configuration that plausibly addresses solid
  tumours.
