# The expansion protocol, step by step, with direct quotes

Two protocols exist and they are **not the same protocol**. Everything below is quoted verbatim;
`[00xx]` are paragraph numbers in WO2025123022A1, quotes attributed to "Portillo" are from the
Methods/Results of Portillo et al., *OncoImmunology* 2025;14(1):2562210 (PMC12477882), and quotes
attributed to "CRM 2022" are from the STAR Methods of Naeimi Kararoudi et al., *Cell Rep Methods*
2022;2(6):100236 — the NK protocol both γδ protocols are derived from.

Note on transcription: Google Patents renders `γδ` as `⁇` in the Examples section of
WO2025123022A1. Where that occurs I have written `[γδ]` in brackets. Nothing else is altered.

---

## PROTOCOL B — the patent (WO2025123022A1). This is the one that matches what he said.

### Step 1 — PBMC isolation

> "PBMCs are isolated from buffy coat purchased from RedCross using a density gradient
> centrifugation… Each aliquot was diluted with 15ml PBS1x. The solution was carefully layered on
> top of 15mL of Ficol… centrifuged at 500g for 30min (ACC-5; DEC-0)… washed with PBS1x (400g for
> 10min ACC-9 DEC-5). The cells were counted, and a single cell suspension was prepared in
> supplemented cell culture medium at a concentration of 5 x 10^7 cells/mL." — Examples

Same buffy-coat/Ficoll front end as the NK program (CRM 2022 lists "Buffy coat  RedCross" and
"Ficoll-Paque PLUS  Cytiva  Cat# 17144003" in its key resources table). Nothing unusual.

### Step 2 — γδ isolation by **negative** selection, and the stated reason

> "StemCells EasySep™ Human Gamma/Delta T Cell Isolation Kit (cat# 19255) was used to isolate
> [γδ] T-Cells based on an immunomagnetic negative selection… 50 ul/ml of Isolation Cocktail was
> added… incubated at room temperature for 15 min. The Magnetic Particles were vortexed for 30
> seconds and then 50ul/ml was added… incubated for 10 min… The polystyrene tube (without lid) was
> placed into the magnet and incubated for 5min." — Examples

The rationale is stated explicitly and it is the same logic as his verbal rule, applied to the
isolation step:

> "Negative immunomagnetic selection has been the method of choice for isolating immune cells for
> functional studies due to concerns that **binding antibodies to the cell surface may induce
> cellular activation, block ligand-receptor interactions or result in immune clearance**." — [0075]

**This is the most self-consistent part of the design.** He refuses to let an antibody touch the
TCR incidentally during isolation, and then applies a TCR stimulus deliberately, on a clock, in the
next step. Contrast Portillo, which uses **positive** selection ("EasySep™ Human CD3 Positive
Selection Kit II") — i.e. anti-CD3 beads on the cells — which is exactly the incidental ligation
[0075] warns about.

### Step 3 — the **short TCR priming window**

> "the isolated γδ T cells are seeded on to culture plates coated with an anti-CD3 antibody or
> equivalent and/or anti-CD28 antibody or equivalent, in complete growth medium. In some
> embodiments, anti-CD3 activates all T cells regardless of their antigen specificity by
> **crosslinking the TCR-CD3 signaling machinery**. In some embodiments, T cell activation triggers
> proliferation and expansion of the γδ T cells. **In some embodiments the stimulation time is at
> least 6 hours. In some embodiments, the stimulation time is 1, 2, 3, 4, 5, 6, 7 days. In some
> embodiments, the stimulation time is at least 2 days.**" — [0076]

and as claims:

> "10. The method of claims 7-9, wherein the γδ T cells were seeded on to culture plates coated with
> an anti-CD3 antibody or equivalent and/or anti-CD28 antibody or equivalent, in complete growth
> medium.
> **11. The method of claims 7-10, wherein stimulation time is at least 2 days.**"

Four things to notice:

1. **Plate-bound, not soluble.** Plate-bound anti-CD3 gives sustained, high-avidity crosslinking;
   the stimulus stops the moment you move the cells off the plate. That is what makes the window
   *controllable* — it is a switch, not a soluble agonist you have to wash out or wait to decay.
   The phrase "seeded on to culture plates coated with" is doing real work here.
2. **The ceiling is 7 days and the floor is 6 hours.** A 6-hour anti-CD3 pulse is not an expansion
   step — it cannot be. It is a *licensing* step: push cells out of G0 into cycle. This is the
   textual evidence that he treats TCR signal as a **starter, not an engine**.
3. **"and/or anti-CD28".** CD28 costimulation is optional. In αβ T cells CD3 without CD28 is the
   classic anergy/AICD-inducing signal-1-alone condition; here it is left optional, presumably
   because 4-1BBL on the feeder supplies costimulation in step 4 instead.
4. **Anti-CD3, not an anti-γδTCR or phosphoantigen.** He deliberately picked the *pan*-T agonist —
   "activates all T cells regardless of their antigen specificity" — which is how you keep both Vδ1
   and Vδ2 in the product rather than selecting a subset (see the payoff in step 6).

Note what the patent does **not** say: nowhere does it state a mechanism or a datum for why longer
is worse. The word "exhaustion" does not appear in the document. "Too long = exhausted cells" is
his verbal rationale for the claimed range; the range is claimed, the rationale is not.

### Step 4 — handoff to the mbIL-21 feeder ("JAK/STAT stimulation")

> "T cells can be further activated and proliferated by two established clinical-grade feeder
> systems… such as, for example, Epstein-Barr virus transformed lymphoblastoid cell lines and
> genetically engineered **K562.mbIL21.4-1BBL feeder cells including, but not limited to CStX-002
> cells**." — [0076]

> "the γδ T cells are expanded with feeder cells that comprise **membrane bound (mb) IL21 on the
> cell surface**. In some embodiments, the mbIL21 feeder cells further comprise **membrane bound
> 4-1BBL**… In some embodiments, the γδ T cells are expanded with **at least a 2:1 ratio** with
> mbIL21-expressing feeder cells. In some embodiments… during expansion, γδ T cells are
> supplemented with **100IU IL2**… **at least every** 1, 2, 3… **48 hours**." — [0078]

The broad fallback list (what he'd accept if the preferred feeder isn't available):

> "T cell stimulating feeder cells… can be either irradiated autologous or allogeneic peripheral
> blood mononuclear cells (PBMCs) or nonirradiated autologous or PBMCs; RPMI8866; HFWT, K562; K562
> cells transfected with membrane bound IL-15, and 41BBL, or IL-21 or any combination thereof; or
> EBV-LCL… Feeder cells can be seeded in the culture of cells at a 1:2, 1:1, or 2:1 ratio." — [0077]

Reading the two paragraphs together tells you what is real and what is patent-lawyer breadth:
[0077] is the "any feeder, any ratio" fallback; **[0078] is the preferred embodiment** —
mbIL-21 **+** 4-1BBL **on K562** at **≥2:1 feeder-excess** with **100 IU IL-2 q48h**. The ratio
matters: ≥2:1 is *feeder in excess of γδ cells*, matching the NK protocol exactly:

> "Purified NK cells were stimulated with irradiated feeder cells (FC21) comprised of K562
> transduced with 4-1BBL and membrane-bound IL-21 (mbIL21) at a **ratio of 2:1 (feeder:NK)**"
> — CRM 2022

The two-signal logic of this step, made explicit:

- **mbIL-21 → IL-21R → JAK1/JAK3 → STAT3** — the "JAK/STAT stimulation" of his verbal comment.
  Membrane-bound rather than soluble means the signal is **contact-dependent, non-diffusible, and
  terminated when the irradiated feeder dies** — so it is re-dosed weekly rather than applied
  continuously. That is a fundamentally different signalling regime from soluble IL-21.
- **4-1BBL → 4-1BB → TRAF1/2 → NF-κB** — the costimulation that replaces the anti-CD28 made
  optional in step 3. Deniger's MD Anderson aAPC paper found γδ proliferation "was dependent upon
  **CD137L** expression on aAPC and addition of exogenous IL2 and IL21" — i.e. 4-1BBL is not
  decorative on this feeder, it is load-bearing for γδ specifically.
- **IL-2 at 100 IU/mL, q48h** — deliberately low and frequently refreshed. 100 IU is a survival/
  tonic STAT5 dose, an order of magnitude below the 500–1000 IU used in classic pAg protocols. The
  design is STAT3-**biased**, not STAT3-only.

### Step 5 — expansion duration, and the editing window

> "γδ T cell expansion can take between 1 to 21 days… **In some embodiments γδ T cell expansion
> takes at least 21 days after isolation** of γδ T cells." — [0079]

> "**19. The method of claims 7-18, wherein the γδ T cells were expanded for at least 7 days.**"

So: TCR phase ≤7 d, feeder phase ≥7 d and typically to ~21 d. **The "short" is the TCR phase. The
overall culture is not short.** Anyone reading his verbal comment as "short culture" has it wrong.

The second, easily-missed purpose of the feeder phase is claimed as an **independent invention**:

> "**39. A method of making gamma delta T cells susceptible to gene editing comprising culturing the
> γδ T cells with feeder cells that comprise membrane bound (mb) IL21 on the cell surface.**"
> (claims 39–46 then recite 4-1BBL, K562, CStX-002, ≥2:1, 100 IU IL-2, q48h — the same conditions
> as claims 12–18, re-claimed for the editing purpose)

That is the NK finding transplanted. In CRM 2022 he showed that FC21 expansion is what makes the
DNA-repair machinery available:

> "we show that the expression level of genes regulating HDR and NHEJ pathways in human NK cells
> generally increase during expansion, with **FC21 resulting in improved conditions for
> site-directed gene insertion**." — CRM 2022

The feeder phase is therefore doing three jobs at once: numbers, phenotype, **and** editability.
This is why he cannot simply shorten the whole culture — he needs the cells in the mbIL-21-driven
proliferative state on the day he electroporates.

### Step 6 — editing (the readout that the protocol worked)

> "**21 days after isolation** gamma delta cells, **3e6 cells/condition were electroporated with
> Cas9RNP complexes** targeting AAVS1 safe harbor site. Cells were resuspended in **P3 buffer** and
> electroporated with one of the following programs: **EO-115, CM-137, and EH-115** in the
> 4D-Nucleofector™ System… **20 minutes post electroporation** the cells were counted and **2
> million cells per condition** were obtained to transduce with TT954-2 mCherry-600bp-AAVS1-AAV6
> with the **MOI of 75k**. **24 hours post transduction, 1 mL of 10% RPMI (1%p/s+1%Glutamax+1%HEPES)
> + 100IU IL2** was added to the transduced cells. 72 hours after transduction cells were stained
> for viability… **the CM-137 program has both the highest percent live and mCherry positive gamma
> delta T cells.**" — Examples

> "CD70 CAR [γδ] T cells were generated **14 days after isolation and expansion**. Flow staining
> prior to CAR generation showed a **97.1% expression of CD70** on the surface of [γδ] T cells…
> **To prevent fratricide, CD70 was knocked-out simultaneously with the integration of the CD70 CAR
> construct into the AAVS1 safe-harbor site**… Virus was added **20 minutes following the
> electroporation** of cas9/RNP containing **200uM of CD70 (AGCGTGGATGCACACCACG) and AAVS1
> (GGGGCCACTAGGGACAGGAT) targeting gRNAs plus 6.2uM of ALT-R® S.p. HiFi Cas9 Nuclease V3**… at an
> **MOI of 75k**… **we were able to generate CD70CAR in both Vδ1 and Vδ2 subsets of [γδ] T
> cells.**" — Examples

Three protocol details worth calling out:

- **AAV 20 min after electroporation**, both times. Identical to NK: *"Electroporation of the NK
  cells with Cas9/RNP targeting AAVS1 followed **30 min later** by AAV transduction"* (CRM 2022).
  The window is when the double-strand break is fresh and HDR template needs to be present.
- **MOI 75K for γδ vs 300K for NK.** CRM 2022: *"we transduced 3 × 10^5 electroporated cells with
  **300K MOI** (10-500K MOI if needed)"*, and Portillo used *"an MOI of 300 K"*. The patent's γδ
  process gets away with **4× less AAV**. Whether that reflects better transducibility of
  anti-CD3-primed γδ blasts or just an untitrated convenience number is not stated — worth asking.
- **The AAVS1 gRNA is literally the same sequence** in the γδ patent (`GGGGCCACTAGGGACAGGAT`) as in
  the NK paper (*"AAVS1 was targeted using gRNA (crRNA: 5′GGGGCCACTAGGGACAGGAT)"*, CRM 2022).
  The γδ program is a direct port of the NK toolkit, not a parallel invention.
- **"CD70CAR in both Vδ1 and Vδ2 subsets"** is the payoff of the anti-CD3 step. Compare Portillo,
  where Vδ2 is gone (below).

### Step 7 — what the protocol yields

> "Figure 1a illustrates the proliferation of [γδ] T-cells **2 weeks post-isolation**… **98.8% of
> the expanded cells are CD3+ T cells and 98.4% are TCRγδ+.**" — Examples

**Caveat you should know about before quoting this protocol as validated:** the patent's *Examples*
section never actually narrates the anti-CD3 priming step or the feeder addition. It goes straight
from the EasySep negative selection to "proliferation of [γδ] T-cells 2 weeks post-isolation."
The anti-CD3 window, the K562.mbIL21.4-1BBL feeders, the ≥2:1 ratio and the 100 IU q48h all appear
in the **description ([0076]–[0078]) and the claims (10–19, 39–46)** — never in a worked example
with a figure. There is **no expansion-fold number, no growth curve, no Vδ1:Vδ2 ratio over time,
and no head-to-head against a longer or absent anti-CD3 window anywhere in the document.** The
process is claimed and described; only the *editing* half is exemplified with data.

---

## PROTOCOL A — Portillo et al. 2025. Published, peer-reviewed, and **has no TCR step at all**.

> "To expand γδ T cells, either bulk PBMCs or CD3+ T cells isolated from PBMCs using the EasySep™
> Human CD3 Positive Selection Kit II (STEMCELL Technologies) were **co-cultured with K562 mb-IL-21
> cells at a 1:2 ratio**… CD3+ isolated cells were re-expanded with K562 mb-IL-21 cells and **γδ T
> cells were expanded for a minimum of 5 weeks prior to use in functional assays**… All expanded
> γδ T cell and NK cell cultures were maintained in **complete RPMI 1640 media supplemented with
> human IL-2 (100 U/mL)** and cultured at 37°C and 5% CO2. **All cultures were replenished with
> irradiated feeder cells on a weekly basis and media and IL-2 was replaced every two to three
> days.**" — Portillo, Methods

> "We first co-cultured the irradiated feeder cells with bulk PBMCs or isolated CD3+ T cells
> **every seven days** with 100 U/mL of IL-2 and tracked the proportion and fold expansion of NK,
> αβ T, and γδ T cells in the cultures weekly." — Portillo, Results

Differences from Protocol B that actually change the product:

| | Protocol A (Portillo) | Protocol B (patent) |
|---|---|---|
| Selection | CD3 **positive** (anti-CD3 beads) | γδ **negative** |
| TCR agonist | **none** | plate-bound anti-CD3, ≥6 h–7 d |
| Feeder:cell | **1:2** (feeder is the *minority*) | **≥2:1** (feeder in excess) |
| 4-1BBL on feeder | "K562 mb-IL-21" — 4-1BBL not stated | mbIL21 **+ 4-1BBL** explicitly |
| IL-2 | 100 U/mL, q2–3 d | 100 IU, q48h |
| Duration | **≥5 weeks**, weekly restim | edit at d14–21 |

The 1:2 vs ≥2:1 inversion is not a typo on either side — Portillo writes "at a 1:2 ratio" for
cells:feeder and the patent writes "at least a 2:1 ratio" for feeder:cells, so they are actually
**within 4× of each other and both feeder-rich**, but the patent demands more feeder per cell.

### The outputs, quoted

> "The percentage of **Vδ1** T cells significantly increased from mean **6.14 ± 3.99%** at
> pre-expansion to mean **70.20 ± 11.37%** after eight weeks. The **Vδ2** T cells became **almost
> completely absent** after the expansion, significantly de[c]reasing from mean **81.50 ± 7.60%** to
> mean **3.79 ± 2.91%**." — Portillo, Results

> "we observed an over **500-fold and 26,000-fold expansion** of γδ T cells from bulk PBMCs or
> isolated CD3+ T cells starting cell populations, respectively." — Portillo

> "there was a trend toward a lower proportion of γδ T cells within the CD3+ population (mean
> 58.02 ± 30.30) after five weeks compared to cultures expanded with **K562-mb-IL-21** cells (mean
> 76.85 ± 15.13)" [vs **K562-mb-IL-15**] "… there was also a lower proportion of Vδ1 T cells five
> weeks post-expansion" — Portillo (Fig. S2)

That last quote is the direct **mbIL-21 vs mbIL-15 head-to-head in γδ cells** — the γδ counterpart
of Denman's NK result, and the closest thing to evidence that the "IL-21 not IL-15" choice is
γδ-specific rather than borrowed. It is a *trend* in supplementary data, not a powered comparison.

### The comparator arm, i.e. what a TCR-driven protocol looks like in the same hands

> "**Vγ9 Vδ2 T cells were activated with 10 mM Zoledronic acid** … **and 4 ng/mL IL-2** … Cells were
> harvested on **day 14** of culture" — Portillo, Methods

and the functional consequence they report: ZA-expanded Vδ2 cells lost CD71 (transferrin receptor /
nutrient uptake) and metabolic competence in patient ovarian ascites, where the mbIL-21-expanded
Vδ1 cells did not. **That is the single best in-house datum behind "too long TCR = bad cells"** —
but note it compares *phosphoantigen* stimulation to *no TCR stimulation*, at different durations,
in different subsets. It is not a titration of anti-CD3 duration.

### And the sentence that complicates the whole story

> "**Decreasing the length of the expansion process may be advantageous as long-term expansion
> could lead to γδ T cell exhaustion and potentially impair the expansion capacity of γδ T cells
> after adoptive transfer.**" — Portillo, Discussion

> "worth examining whether **addition of Vδ1 TCR stimulation** may increase the yield and purity"
> — Portillo, Discussion

Read those two together and the published position is: *we ran 5+ weeks with no TCR signal, we
suspect that's too long, and we're not sure whether adding TCR stimulation back would help.* The
patent is the answer to the second sentence — add TCR stimulation back, but bound it.

---

## What I'd push on

1. **The titration doesn't exist in either document.** 6 h vs 2 d vs 7 d anti-CD3, feeder phase held
   constant, reading out fold expansion, Vδ1:Vδ2, TOX/TCF7, and re-expansion after transfer. The
   claim range (6 h → 7 d) spans a 28× difference in stimulus duration with no data distinguishing
   the ends. "At least 2 days" in claim 11 looks like a claim-drafting floor, not an optimum.
2. **Feeder:cell ratio is asserted, never optimized.** ≥2:1 is inherited from the NK protocol
   verbatim. γδ cells are not NK cells; 4-1BB expression kinetics after anti-CD3 priming differ.
3. **4-1BBL vs mbIL-21 is unresolved for γδ.** Deniger's data say proliferation "was dependent upon
   CD137L", i.e. the costim, whereas the whole STAT3 story is about IL-21. Portillo's feeder is
   written as "K562 mb-IL-21" without stating 4-1BBL. Which signal is actually carrying the γδ
   expansion has not been dissected in his own work.
4. **Nothing verifies the STAT3 mechanism in γδ cells.** No pSTAT3 blot, no telomere/hTERT
   measurement, no JAK inhibitor control in either document. "Feeders that do JAK/STAT stimulation"
   is a mechanistic claim carried entirely by NK data (Denman 2012) and inference from IL-21R
   biology. A tofacitinib/ruxolitinib add-back would settle it in a week.
5. **Two-week vs five-week product.** The patent edits at d14–21; Portillo assays at ≥5 weeks. If
   the short-culture rationale is real, the *published functional data* were generated on cells the
   rationale says are suboptimal. Worth asking which duration the CARTx clinical process uses.
6. **AAV MOI 75K (γδ) vs 300K (NK)** — was this titrated in γδ, or inherited/guessed?
7. **αβ carryover.** Protocol B's negative selection is the cleaner GvHD answer; Protocol A's
   CD3-positive selection retains αβ T cells and Portillo recommends a downstream αβ-depletion.
   For an allogeneic product these are not interchangeable.

---

### Source documents

- WO2025123022A1 — https://patents.google.com/patent/WO2025123022A1/en
- Portillo et al. 2025, *OncoImmunology* — https://pmc.ncbi.nlm.nih.gov/articles/PMC12477882/
- Naeimi Kararoudi et al. 2022, *Cell Rep Methods* — https://pmc.ncbi.nlm.nih.gov/articles/PMC9243630/
- Denman et al. 2012, *PLoS ONE* — https://doi.org/10.1371/journal.pone.0030264
- Deniger et al. 2014, *Clin Cancer Res* — https://pmc.ncbi.nlm.nih.gov/articles/PMC4233015/
