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
next step. Contrast Portillo, whose *expansion* cultures start from bulk PBMC or from cells taken
with **positive** selection ("EasySep™ Human CD3 Positive Selection Kit II") — i.e. anti-CD3 beads
on the cells — which is the incidental ligation [0075] warns about. Fair qualifier: Portillo *does*
use negative selection where it matters most to them — their **fresh, unexpanded** comparator γδ
cells were isolated "using a TCRγ/δ+ T cell isolation kit (Miltenyi Biotec) or a EasySep™ Human
Gamma/Delta T Cell Isolation Kit (STEMCELL Technologies) and were used immediately in functional
assays." So the difference is a choice made for the expansion arm, not a lab-wide difference in
practice.

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

> "20. The method of claims 7-19, wherein, **at least 21 days after isolation of γδ T cells**, at
> least 3 million γδ T cells /condition were electroporated with Cas/RNP complexes targeting AAVS1
> safe harbor site."

The 21-day figure is not merely a description — it is **in the claims**, which settles the point.

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

- **AAV 20 min after electroporation**, both times. Near-identical to NK: *"Electroporation of the
  NK cells with Cas9/RNP targeting AAVS1 followed **30 min later** by AAV transduction"* (CRM 2022).
  The window is when the double-strand break is fresh and HDR template needs to be present.
- **The Nucleofector program differs by cell type and was re-optimized.** NK used *program EN-138*
  (CRM 2022); γδ screened EO-115 / CM-137 / EH-115 and picked **CM-137**. So the port from NK to γδ
  was not blind — at least the electroporation parameters were empirically re-derived.
- **MOI 75K for γδ vs 300K for NK.** CRM 2022: *"we transduced 3 × 10^5 electroporated cells with
  **300K MOI** (10-500K MOI if needed)"*, and Portillo used *"an MOI of 300 K"*. The patent's γδ
  process gets away with **4× less AAV**. Whether that reflects better transducibility of
  anti-CD3-primed γδ blasts or just an untitrated convenience number is not stated — worth asking.
- **The AAVS1 gRNA is literally the same sequence** in the γδ patent (`GGGGCCACTAGGGACAGGAT`) as in
  the NK paper (*"AAVS1 was targeted using gRNA (crRNA: 5′GGGGCCACTAGGGACAGGAT)"*, CRM 2022).
  The γδ program is a direct port of the NK toolkit, not a parallel invention.
- **"CD70CAR in both Vδ1 and Vδ2 subsets"** is the payoff of the anti-CD3 step. Compare Portillo,
  where Vδ2 is gone (below). Caveat: the patent shows CAR *in* both subsets by flow; it does not
  report what fraction of the culture each subset represents, so "polyclonal" is supported for the
  edited cells but the Vδ1:Vδ2 composition of the product is not quantified anywhere.
- **Post-edit feeder re-stimulation matches NK almost exactly.** Patent: "24 hours post transduction
  1 mL of 10% RPMI… + 100IU IL2 was added". CRM 2022: "The day after electroporation and
  transduction, we added 300ul of fresh media containing 50 IU of IL2… The cells were kept in
  culture for **48 h after electroporation and were then re-stimulated with 2 × 10^6 feeder
  cells**". Portillo: "The transduced cells were replenished with irradiated K562 mb-IL-21 cells
  **48 h after electroporation** and cryopreserved after 7 days." All three: feed at 24 h,
  re-feeder at 48 h.

### Step 7 — what the protocol yields

> "Figure 1a illustrates the proliferation of [γδ] T-cells **2 weeks post-isolation**… **98.8% of
> the expanded cells are CD3+ T cells and 98.4% are TCRγδ+.**" — Examples

**RETRACTED CAVEAT — the expansion protocol *is* exemplified.** Earlier versions of this note said
the Examples never narrate the anti-CD3 priming or feeder addition. That was wrong: **[0095], headed
"γδ T-Cells Expansion", is a complete worked expansion protocol.** See
`protocol_B_patent_verified.md` §Step 3A for the full quote. In brief: 350,000 cells seeded in
complete RPMI (10% FBS / 1% P-S / 1% GlutaMax / 1% HEPES) **+ 100 IU IL-2** on an **anti-CD3 (Tonbo
40-0038-U100) and anti-CD28 (Tonbo 40-0289-U100) coated plate**; **two days post-stimulation**
transferred to a **2:1 ratio with mbIL21 K562 feeder cells (CSTX002)**; 100 IU IL-2 **every other
day**; "**Cells were expanded every 7 days.**"

What remains genuinely absent: **no numeric fold expansion in the text** (FIG. 1A is a growth curve
but carries no value in the narrative), **no Vδ1:Vδ2 percentages in the text** (FIG. 1B stains them),
no donor number, **no irradiation of the feeders stated anywhere**, and **no head-to-head against a
longer or absent anti-CD3 window.**

---

## PROTOCOL A — Portillo et al. 2025. Published, peer-reviewed, and **has no TCR step at all**.

### A1 — Feeder line (same line as the patent, despite the shorthand)

> "**K562 feeder cells expressing membrane-bound IL-21 and 4-1BBL (K562-mb-IL-21)** have been used
> for the large-scale expansion of highly potent anti-tumor human NK cells for clinical use"
> — Portillo, Introduction

> "The suspension K562 feeder cells engineered to express **mb-IL-21 or mb-IL-15** as previously
> described were **kindly obtained from Dr. Dean A. Lee (Nationwide Children's Hospital)**"
> — Portillo, Methods

So "K562 mb-IL-21" throughout their Methods means **mbIL-21 + 4-1BBL K562**, i.e. the FC21/clone-9
line — the same feeder the patent calls K562.mbIL21.4-1BBL / CStX-002. **The feeder is not a
variable between Protocol A and Protocol B.**

### A2 — Starting material and seeding

> "To expand γδ T cells, either **bulk PBMCs or CD3+ T cells isolated from PBMCs using the EasySep™
> Human CD3 Positive Selection Kit II** (STEMCELL Technologies) were **co-cultured with K562 mb-IL-21
> cells at a 1:2 ratio**." — Portillo, Methods

`1:2` here is **cells : feeder** — i.e. 2 feeders per target cell, the same feeder excess as the
patent's "at least a 2:1 ratio *with* mbIL21-expressing feeder cells" (feeder:cell) and the NK
protocol's "2:1 (feeder:NK)". No TCR agonist, no mitogen, no phosphoantigen is added at any point.

### A3 — Maintenance

> "All expanded γδ T cell and NK cell cultures were maintained in **complete RPMI 1640 media
> supplemented with human IL-2 (100 U/mL)** and cultured at 37°C and 5% CO2. **All cultures were
> replenished with irradiated feeder cells on a weekly basis and media and IL-2 was replaced every
> two to three days.**" — Portillo, Methods

> "We first co-cultured the irradiated feeder cells with bulk PBMCs or isolated CD3+ T cells
> **every seven days** with 100 U/mL of IL-2 and tracked the proportion and fold expansion of NK,
> αβ T, and γδ T cells in the cultures weekly." — Portillo, Results

### A4 — Mid-culture re-isolation (easy to miss, and it changes what the product is)

> "**Hence, expanded γδ T cells were isolated from bulk PBMC expanded co-cultures using a CD3+
> immunomagnetic positive selection kit before further expansion prior to use in functional
> experiments.**" — Portillo, Results

Their reasoning, quoted: fold expansion was higher from CD3⁺-isolated cultures, but "majority of
expanded live cells in the bulk PBMC co-cultures were **NK cells**", while bulk PBMC cultures gave a
higher *proportion* of γδ within CD3⁺. So they take the purity of the bulk route and rescue the
yield by CD3-selecting mid-culture and re-expanding:

> "CD3+ isolated cells were **re-expanded** with K562 mb-IL-21 cells and **γδ T cells were expanded
> for a minimum of 5 weeks prior to use in functional assays**." — Portillo, Methods

### A5 — Cryopreservation

> "Cells were cryopreserved in **10% DMSO, 20% FBS, and 70% complete RPMI 1640** media." — Methods

> "We did not detect a decrease in the viability or change in the proportion of cell subsets
> post-thaw (Figs. S1A-D)." — Results

### A6 — CAR arming (adapted from his NK method, ref. 27 = CRM 2022)

> "expanded Vδ1 T cells were electroporated with **HiFi CRISPR/Cas9 Nuclease V3** (IDT) and guide
> RNA targeting the **AAVS1** safe harbor locus. After electroporation, cells were transduced with
> **ssAAV6 encoding the HER2 CAR construct at a 300K multiplicity of infection (MOI)**… The
> transduced cells were **replenished with irradiated K562 mb-IL-21 cells 48 h after
> electroporation and cryopreserved after 7 days**. Cells were replenished with irradiated K562
> mb-IL-21 cells **weekly post-thaw**." — Portillo, Methods

CAR construct: "a HER2-specific **DARPin28z** binding domain, a **CD28** co-stimulation domain, and
the cytoplasmic domain of **CD3ξ** [sic — CD3ζ]… with the modification of an **IgG heavy chain for
the hinge**".
CAR expression tracked "every seven days… **over 21-days of expansion**".

### A7 — What comes out (and the donor variability, which the headline number hides)

> "The percentage of **Vδ1** T cells significantly increased from mean **6.14 ± 3.99%** at
> pre-expansion to mean **70.20 ± 11.37%** after eight weeks. The **Vδ2** T cells became **almost
> completely absent**… from mean **81.50 ± 7.60%** to mean **3.79 ± 2.91%**." — Results

> "we observed an over **500-fold and 26,000-fold expansion** of γδ T cells from bulk PBMCs or
> isolated CD3+ T cells starting cell populations, respectively." — Results

But Table 1 (the 7 donors actually used in functional assays) is more heterogeneous than
"Vδ1-dominant" suggests:

| Donor | %CD3⁺ | %CD3⁻CD56⁺ | %αβTCR⁺ | %γδTCR⁺ | **%Vδ1** | %Vδ2 | **%Vδ1⁻Vδ2⁻** |
|---|---|---|---|---|---|---|---|
| 1 | 98.7 | 1.1 | 0 | 99.4 | 97.3 | 0 | 2.72 |
| 2 | 99.4 | 0.31 | 5.33 | 91.7 | 99.0 | 0 | 1.0 |
| 3 | 96.5 | 2.51 | 0.15 | 97.7 | **22.5** | 0 | **77.4** |
| 4 | 98.1 | 0.82 | 1.87 | 97.7 | 99.2 | 0 | 0.68 |
| 5 | 98.8 | 0.72 | 0.24 | 93.6 | 99.3 | 0 | 0.24 |
| 6 | 99.4 | 0.3 | **11.5** | 87.3 | **40.8** | 0 | **59.1** |
| 7 | 97.9 | 1.71 | 1.59 | 95.9 | 85.2 | 0.4 | 14.3 |

Three things this table says that the abstract does not:
- **Vδ2 is not reduced — it is eliminated.** 0.0% in six of seven donors. There is no dose of this
  protocol that gives you a Vδ2-containing product.
- **Two of seven donors are actually Vδ1⁻Vδ2⁻-dominant** (77.4% and 59.1%). Those are Vδ3/Vδ5/etc.,
  an uncharacterized population that was never functionally separated in the paper. "Vδ1 T cells"
  as the product label is an approximation for 5/7 donors.
- **αβ carryover reaches 11.5%.** For an allogeneic product that is the GvHD-relevant number, and
  it is not depleted anywhere in Protocol A. (Their own Vδ2 comparator arm *does* get αβ-depleted
  with CD4/CD8 microbeads at harvest; the mbIL-21 arm does not.)

### A8 — The Vδ2 comparator arm in the same paper, quoted in full

> "Vγ9 Vδ2 T cells were activated with **10 mM Zoledronic acid** (Sigma-Aldrich) and **4 ng/mL
> IL-2** (Cellgenix) from bulk PBMCs. PBMCs were seeded at **2x10^6 cells/cm^2 in a 24-well G-Rex
> plate**. Cells were maintained in complete RPMI 1640 supplemented with 1 mM sodium pyruvate,
> 1 mM non-essential amino acids, and 55 μM β-mercaptoethanol for the **first 4 days**. On **day 4**
> cells were… resuspended in **CTS OpTmizer T cell Expansion SFM** + 1X Glutamax + **5% CTS Immune
> Cell Serum Replacement**. A **75% media replacement every 3–4 days** with **4 ng/mL IL-2 every
> 2–3 days** and **5 ng/mL IL-15 every 2–3 days starting on day 7**. Cells were harvested on
> **day 14**, **depleted of αβ T cells using CD4 and CD8 Microbeads**… cryopreserved in CryoStor
> CS10, thawed, and **rested in IL-2 (1.5 ng/mL) and IL-15 (5 ng/mL) for 24 h** prior to use."
> — Portillo, Methods

⚠️ **"10 mM zoledronic acid" is almost certainly an error in the published paper** — standard γδ
expansion uses **1–5 µM**, so this is ~2,000–10,000× high. Two consequences: (a) don't reproduce
the number; (b) if it were literally 10 mM the comparator arm would be a toxicity condition, which
would materially weaken the "ZA-expanded Vδ2 cells are metabolically fragile" comparison that this
paper leans on. Worth confirming with the authors before citing that comparison as evidence.

Differences from Protocol B that actually change the product:

| | Protocol A (Portillo) | Protocol B (patent) |
|---|---|---|
| Selection (expansion arm) | bulk PBMC, or CD3 **positive** | γδ **negative** |
| TCR agonist | **none** | plate-bound anti-CD3, ≥6 h–7 d |
| Feeder:cell | 1:2 cells:feeder = **2 feeders per cell** | "at least a 2:1 ratio" feeder:cell = **≥2 feeders per cell** |
| 4-1BBL on feeder | **yes** — see correction below | mbIL21 **+ 4-1BBL** explicitly |
| IL-2 | 100 U/mL, q2–3 d | 100 IU, q48h |
| Duration | **≥5 weeks**, weekly restim | edit at d14–21 |

**Two corrections worth stating plainly, because the obvious reading of the wording is wrong.**

*Feeder ratio.* Portillo writes "at a **1:2** ratio" and the patent writes "at least a **2:1**
ratio" — but they are written in opposite orders. Portillo's is cells:feeder; the patent's is
explicitly "2:1 ratio **with** mbIL21-expressing feeder cells" following the NK convention
(feeder:cell). Both therefore mean **~2 feeder cells per γδ cell**, matching the NK protocol
("stimulated with irradiated feeder cells (FC21)… at a **ratio of 2:1 (feeder:NK)**", CRM 2022).
The apparent 4× discrepancy is an artifact of notation; the patent's "at least" only makes it a
floor rather than a fixed value. **This is not a real difference between the two protocols.**

*4-1BBL.* Portillo's shorthand "K562 mb-IL-21" hides the costimulatory ligand, but the paper's
introduction spells it out: "K562 feeder cells expressing **membrane-bound IL-21 and 4-1BBL**
(K562-mb-IL-21) have been used for the large-scale expansion of highly potent anti-tumor human NK
cells for clinical use". So **both protocols use the same mbIL-21 + 4-1BBL feeder**; the feeder is
not a variable between them. (Portillo also notes the feeders "were kindly obtained from Dr." —
Lee — confirming they are the same FC21-lineage line.)

What that leaves as the *actual* differences: **the TCR-priming step, the starting selection, and
the timepoint at which the product is taken.** Nothing else.

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

> "Vδ2 T cell expansion — **Vγ9 Vδ2 T cells were activated with 10 mM Zoledronic acid**
> (Sigma-Aldrich) **and 4 ng/mL IL-2** (Cellgenix) from bulk PBMCs. **PBMCs were seeded at 2x10^6
> cells/cm^2 in a 24-well G-Rex plate** (Wilson Wolf). Cells were maintained in complete RPMI 1640
> supplemented with 1 mM sodium pyruvate, 1 mM non-essential [amino acids]…" — Portillo, Methods

(Flagging a probable error **in the published paper**, not in my transcription: "10 mM zoledronic
acid" is ~1,000–10,000× the standard γδ-expansion concentration, which is 1–5 µM. The paper says
mM; almost certainly µM was intended. Don't propagate the number without checking with the authors.)

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
3. **4-1BBL vs mbIL-21 is unresolved for γδ.** Deniger's data say γδ proliferation "was dependent
   upon **CD137L** expression on aAPC and addition of exogenous IL2 and IL21", i.e. the
   costimulatory ligand was the non-negotiable component, whereas the whole STAT3 narrative is about
   IL-21. Both protocols here use a feeder carrying **both**, and neither drops one to see which is
   load-bearing in γδ cells. The mbIL-21-vs-mbIL-15 comparisons (Denman in NK, Portillo Fig. S2 in
   γδ) hold 4-1BBL constant and vary the cytokine — they cannot answer this.
4. **Nothing verifies the STAT3 mechanism in γδ cells.** No pSTAT3 measurement and no telomere/hTERT
   data in either document. "Feeders that do JAK/STAT stimulation" is a mechanistic claim carried
   entirely by NK data (Denman 2012) and inference from IL-21R biology.

   ⚠️ **A JAK inhibitor is the wrong experiment** (an earlier version of this note proposed
   tofacitinib/ruxolitinib — retracted). IL-2, IL-15 and IL-21 are all γc cytokines signalling
   through the **same JAK1 + JAK3 pair**; the divergence is at the STAT docking step, set by the
   private receptor chain (IL-2Rβ → STAT5A/B; IL-21R → STAT3/STAT1). A JAK inhibitor would block
   both arms equally and discriminate nothing. **The correct term is "STAT3-biased", not
   "JAK/STAT3-biased"** — the JAK layer is identical across these cytokines. The discriminating
   experiments are **pSTAT3 vs pSTAT5 flow during feeder co-culture**, and STAT3 KO or a selective
   STAT3 inhibitor with the rest of the culture held constant.

   Note also that only *half* the feeder is JAK/STAT: mbIL-21 → JAK1/JAK3 → STAT3, but
   **4-1BBL → 4-1BB → TRAF1/2 → NF-κB**, no JAKs or STATs involved. Deniger's γδ data point at
   the latter ("dependent upon CD137L").
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
