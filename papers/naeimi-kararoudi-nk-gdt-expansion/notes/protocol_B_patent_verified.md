# Protocol B — WO2025123022A1, verified line by line

Every step below was re-checked against the full patent text. This file supersedes the Protocol B
sections of `expansion_protocol_walkthrough.md` where they disagree.

**Bibliographic facts.** WO2025123022A1, "Compositions and methods of making a modified gamma-delta
t-cell". PCT/US2024/059195. Priority **US 63/608,159, 8 Dec 2023**; PCT filed **9 Dec 2024**;
published **12 Jun 2025**; status **Pending**. Inventors: **Meisam Naeimi Kararoudi, Noushin
Saljoughian, Genesis Snyder, Dean Lee**. Assignee: Nationwide Children's Hospital Inc. Cited art is
one patent (WO2023178292A1) and two NPL references — i.e. no substantive search report yet.

Notation: `[00xx]` = description paragraph. "Claim n" = the claims as filed. "Example" = the worked
examples section. **These three tiers are not equivalent and are kept separate throughout.**

---

## Corrections to my earlier write-ups

0. **⚠️ BIGGEST CORRECTION: "the expansion protocol is never exemplified" was WRONG.** I missed
   paragraph **[0095], headed "γδ T-Cells Expansion"** — a complete worked expansion protocol with
   catalog numbers, cell numbers, and timings. It is quoted in full in Step 3A below. Everything I
   previously said about the expansion half being "claims and description only" must be discarded.
   What is genuinely missing is narrower and is itemized at the end of Step 3A.
1. **"No growth curve" was wrong.** FIG. 1A is "**γδ T-Cell growth curve from day one till 2 weeks
   after isolation**". The figure exists; what is absent is any *numeric* fold-expansion in the text.
2. **"No Vδ1:Vδ2 data" was too strong.** FIG. 1B is flow "for anti-CD3, anti-TCRγδ, TCR Vδ1, and
   TCR Vδ2". Subsets *were* measured at 2 weeks. What is absent is (a) the subset percentages in the
   text — only "98.8%… CD3+ … 98.4%… TCRγδ+" is given — and (b) any *timecourse*.
3. **"The stimulation step is never mentioned in the Examples" was wrong twice over.** The figure
   title is "γδ T Cell **Isolation, Stimulation**, and Proliferation", *and* [0095] states the
   conditions: Tonbo anti-CD3 + anti-CD28 coated plate, 2 days. Only the coating concentration and
   plate format are missing.
4. **I conflated two different examples' post-transduction feeds.** The "1 mL of 10% RPMI … + 100IU
   IL2 at 24 h" belongs to the **mCherry electroporation-optimization** example. The **CD70-CAR**
   example says "**24 hours post transduction 500uL of media was added**". Different volumes,
   different experiments.
5. **MOI 75K is the example, not the claim.** Claim 26 claims "**a Multiplicity of Infection (MOI)
   of at least 1k**"; [0079] describes "about 1 to about 1000K MOI (e.g., about 5 to 500K MOI)".
   75K is one worked value inside a very broad claim.
6. **"The patent says expansion takes at least 21 days" is only half of what [0079] says.** See §8.

---

## Step 1 — PBMC isolation *(Example — fully exemplified)*

> "PBMCs are isolated from **buffy coat purchased from RedCross** using a density gradient
> centrifugation. Each buffy coat that was separated into **15mL aliquots**… diluted with **15ml
> PBS1x**… layered on top of **15mL of Ficol**… centrifuged at **500g for 30min (ACC-5; DEC-0)**…
> washed with PBS1x (**400g for 10min ACC-9 DEC-5**)… a single cell suspension was prepared in
> supplemented cell culture medium at a concentration of **5 x 10^7 cells/mL**."

Healthy-donor buffy coat, standard Ficoll. Nothing unusual. **Verified.**

## Step 2 — γδ negative selection *(Example — fully exemplified, with kit-level detail)*

> "**StemCells EasySep™ Human Gamma/Delta T Cell Isolation Kit (cat# 19255)** was used to isolate γδ
> T-Cells based on an **immunomagnetic negative selection**… **50 ul/ml of Isolation Cocktail**…
> incubated at room temperature for **15 min**. The Magnetic Particles were vortexed for 30 seconds
> and then **50ul/ml** was added… incubated for **10 min**… **2.5mL** of supplemented media was
> added… placed into the magnet and incubated for **5min**… inverted so the enriched cell suspension
> was transferred into a new 5 ml tube."

Also claimed — claim 9: "wherein the γδ T cells are isolated from human PBMCs using **immunomagnetic
negative selection**."

Rationale, [0075]:

> "Negative immunomagnetic selection has been the method of choice for isolating immune cells for
> functional studies due to concerns that **binding antibodies to the cell surface may induce
> cellular activation, block ligand-receptor interactions or result in immune clearance**."

⚠️ **But the worked example [0075] gives is myeloid, not γδ:** "T cell selection from PBMCs comprises
using antibodies against **CD33, CD34, CD123, CD11c and CD36** markers to deplete myeloblasts."
The patent never states the actual depletion cocktail of kit #19255. Any claim about which markers
(e.g. TCRαβ) that kit depletes must come from StemCell's product documentation, **not from this
patent.** Flagged as unverified here.

Background numbers, [0074]: γδ are "**1–5% of all CD3+ cells**"; Vγ9Vδ2 "can account for up 95% of
γδ T-cells"; "**Vδ1 T-cells represent only 10–30% of γδ T-cells** in peripheral blood". *(Note the
last figure sits above Portillo's measured 6.14 ± 3.99% Vδ1 pre-expansion — a background-literature
value, not a measurement in this document.)*

## Step 3 — anti-CD3 priming *(description + claims; worked conditions in Step 3A)*

[0076], in full:

> "the isolated γδ T cells are **seeded on to culture plates coated with an anti-CD3 antibody or
> equivalent and/or anti-CD28 antibody or equivalent**, in complete growth medium. In some
> embodiments, **anti-CD3 activates all T cells regardless of their antigen specificity by
> crosslinking the TCR-CD3 signaling machinery**. In some embodiments, T cell activation triggers
> proliferation and expansion of the γδ T cells. In some embodiments **the stimulation time is at
> least 6 hours**. In some embodiments, the stimulation time is **1, 2, 3, 4, 5, 6, 7 days**. In some
> embodiments, the stimulation time is **at least 2 days**."

Claim 10 recites the plate-bound anti-CD3/anti-CD28 seeding; **claim 11: "wherein stimulation time
is at least 2 days."**

What the wording establishes:
- **Plate-bound**, therefore terminable by removing the cells — a switch, not a decaying agonist.
- **Floor of 6 hours** — at 6 h this cannot be an expansion step; it is a licensing step.
- **"and/or anti-CD28"** — costim optional, consistent with 4-1BBL supplying it downstream.
- **anti-CD3, not anti-Vδ1 or phosphoantigen** — pan-T by design ("regardless of their antigen
  specificity"), which is the mechanistic basis for retaining Vδ2.

What this description alone does not establish — the clone, the duration used, whether CD28 is
included — **is supplied by the worked example in [0095]; see Step 3A.** What remains missing even
after [0095] is the coating concentration, the plate format, and **any comparison between
stimulation durations anywhere in the document.**

⚠️ **The word "exhaustion" appears zero times in the patent. "STAT", "JAK" and "telomere" appear zero
times as mechanism** (the only "JAK"/"zoledronic" hits are inside a boilerplate list of approved
oncology drugs). The verbal rationale he gave is nowhere in the filing.

## Step 3A — THE WORKED EXPANSION EXAMPLE, [0095] *(the paragraph I missed)*

Immediately before this, the end of the isolation example gives a **yield**:

> "The addition of magnetic particles was repeated in the enriched cell suspension with a volume of
> **37.5ul**, incubated for 5mins, placed into the magnet for 5min, and inverted to the new 5ml tube.
> The isolated cells were ready to use. Since γδ T-Cells account for less than 1% of circulating
> white blood cells, therefore **700,000 γδ T-Cells were isolated from 20,000,000 PBMCs**."

(3.5% of PBMC — above the "1–5% of CD3+" of [0074], and note the second magnetic round, which I had
also missed.)

Then [0095] in full:

> "**γδ T-Cells Expansion** [0095] **350,000 cells were seeded** in completed RPMI (Fisher Scientific
> cat# SH30096FS or equivalent) (**10% Fetal Bovine Serum** (GenClone cat# 25-514H), **1%
> Penicillin-Streptomycin** (Fisher cat# 15-140-122), **1% GlutaMax** (Fisher cat# 35-050-061), and
> **1% HEPES** (Fisher cat# MT25060CI)) and **supplemented with 100IU IL2** on an **anti CD3 (Tonbo
> Bioscience cat# 40-0038-U100 or equivalent) and anti CD28 (Tonbo Bioscience cat# 40-0289-U100 or
> equivalent) coated plate** for their stimulation. **Two days post-stimulation, cells were counted
> and expanded at a 2:1 ratio with mbIL21 K562 feeder cells (CSTX002).** During expansion, cells were
> counted and **supplemented with 100IU IL2 every other day**, media was added as necessary. **Cells
> were expanded every 7 days.**"

Everything the claims recite is here as an actual worked condition:

| Element | Claim/description | **[0095] worked value** |
|---|---|---|
| Anti-CD3 ± anti-CD28 | "and/or", no clone | **both**, Tonbo 40-0038-U100 + 40-0289-U100, plate-coated |
| Stimulation time | 6 h – 7 d; "at least 2 days" | **exactly 2 days** |
| Feeder | K562.mbIL21.4-1BBL / CStX-002 | **mbIL21 K562 (CSTX002)** |
| Ratio | "at least a 2:1 ratio" | **2:1**, and unambiguously **feeder:cell** ("expanded **at** a 2:1 ratio **with** … feeder cells") |
| IL-2 | 100 IU q≤48 h | **100 IU every other day** |
| Re-stimulation | not recited | **"Cells were expanded every 7 days"** — weekly, same as Portillo |
| Seeding | not recited | **350,000 cells** (half the 700,000 isolated) |
| Medium | "complete growth medium" | **cRPMI + 10% FBS + 1% P-S + 1% GlutaMax + 1% HEPES** |

Three substantive points that only this paragraph establishes:

1. **IL-2 is present from day 0, during the anti-CD3 phase** — 100 IU is in the seeding medium, not
   added later. So the TCR pulse is delivered *on top of* tonic γc signalling; it is not a pure
   TCR-only window.
2. **anti-CD28 is actually used**, not merely permitted. The "and/or" of [0076] is claim-breadth
   language; the real protocol gives CD3 + CD28 together, i.e. full two-signal priming.
3. **Weekly feeder re-stimulation** — "expanded every 7 days" — which makes the feeder cadence
   identical to Portillo's "replenished with irradiated feeder cells on a weekly basis". I had
   previously listed re-stimulation frequency as unspecified in the patent.

**What is still genuinely absent from [0095] and the rest of the Examples:** no numeric fold
expansion in the text (FIG. 1A plots it, the narrative gives no value); no Vδ1/Vδ2 percentages in the
text (FIG. 1B stains them); no donor number or replicates; no plate format or coating concentration;
**no statement that the CSTX002 feeders are irradiated**; and no comparison of a longer or shorter
anti-CD3 window — the 2-day value is used, never justified against alternatives.

## Step 4 — feeder cells *(description + claims; now also exemplified in [0095])*

[0076] names two "**established clinical-grade feeder systems**": "**Epstein-Barr virus transformed
lymphoblastoid cell lines** and genetically engineered **K562.mbIL21.4-1BBL feeder cells including,
but not limited to CStX-002 cells**."

[0078] is the operative embodiment:

> "the γδ T cells are expanded with feeder cells that comprise **membrane bound (mb) IL21** on the
> cell surface. In some embodiments, the mbIL21 feeder cells **further comprise membrane bound
> 4-1BBL**. In some embodiments the feeder cells are **K562** cells. In some embodiments the feeder
> cell line is **CSTX-002**. In some embodiments, the γδ T cells are expanded with **at least a 2:1
> ratio** with mbIL21-expressing feeder cells."

Claims 12–16 track this exactly. **Claim 12 depends on "claims 8-11"** — i.e. the feeder step is
claimed as occurring "**following stimulation**", which makes the two-phase architecture explicit in
the claims, not merely in the description.

⚠️ **[0077] is much broader than the ≥2:1 I previously reported:**

> "T cell stimulating feeder cells… can be either **irradiated autologous or allogeneic PBMCs or
> nonirradiated** autologous or PBMCs; **RPMI8866; HFWT, K562; K562 cells transfected with membrane
> bound IL-15, and 41BBL, or IL-21** or any combination thereof; or **EBV-LCL**… **Feeder cells can
> be seeded in the culture of cells at a 1:2, 1:1, or 2:1 ratio.** In some aspects, the media can
> comprise **IL-2, IL-7, IL-12, IL-15, IL-18, and/or IL-21**."

Two consequences. First, **1:2 is an explicitly described option**, so Portillo's ratio falls inside
the patent's disclosed range whichever orientation you read. The ≥2:1 of [0078]/claim 16 is the
*preferred and claimed* embodiment, not the only described one. Second, [0077] is standard
broad-coverage drafting (it even covers mbIL-15, the comparator this platform exists to beat) and
should not be read as the intended process.

⚠️ **The patent never states that the K562.mbIL21.4-1BBL feeders are irradiated.** "Irradiated"
appears exactly once, in the [0077] laundry list, applied to PBMC feeders — and that same sentence
also permits "**nonirradiated**". [0078], the operative paragraph, and claims 12–16 and 39–46 are
silent. By contrast Portillo says "irradiated feeder cells" throughout and CRM 2022 says "irradiated
feeder cells (FC21)". **For a therapeutic process this is a material omission as written** — an
unirradiated K562 is a proliferating CML line. Almost certainly irradiation is intended and simply
went unrecited; but it is not in the document.

## Step 5 — IL-2 *(description + claims)*

[0078]: "during expansion, γδ T cells are supplemented with **100IU IL2**… at least every 1, 2, 3 …
**48 hours**." Claims 17–18: 100 IU IL-2, "at least every 48 hours". **Verified.**

Note this is a *tonic* STAT5 dose ~10× below classic phosphoantigen protocols (500–1000 IU). The
design is STAT3-**biased**, not IL-2-free.

## Step 6 — what the Examples actually show

> "**Figure 1a** illustrates the proliferation of γδ T-cells **2 weeks post-isolation**. **Figure 1b**
> we performed flow cytometry for anti-CD3, anti-TCRγδ, TCR Vδ1, and TCR Vδ2… **98.8% of the
> expanded cells are CD3+ T cells and 98.4% are TCRγδ+.**"

Figure legends: "FIG. 1A and 1B show γδ T Cell **Isolation, Stimulation, and Proliferation**.
Figure 1A shows **γδ T-Cell growth curve from day one till 2 weeks after isolation**. Figure 1B shows
flow cytometry to identify the **purity and subsets** of expanded γδ T cells."

**So:** a growth curve and a subset panel both exist as figures. **What is missing from the text is
the fold-expansion value, the Vδ1/Vδ2 percentages, the donor number, and — critically — any
statement of the anti-CD3 conditions used to generate them.** The Examples narrative goes directly
from the EasySep magnet to "2 weeks post-isolation" with no process description in between. You
cannot reproduce the expansion from this document.

## Step 7 — electroporation optimization *(Example — this half is genuinely exemplified)*

> "**21 days after isolation** gamma delta cells, **3e6 cells/condition** were electroporated with
> Cas9RNP complexes targeting AAVS1 safe harbor site. Cells were resuspended in **P3 buffer** and
> electroporated with one of the following programs: **EO-115, CM-137, and EH-115** in the
> **4D-Nucleofector™ System**… **20 minutes post electroporation** the cells were counted and **2
> million cells per condition** were obtained to transduce with **TT954-2 mCherry-600bp-AAVS1-AAV6
> with the MOI of 75k**. **24 hours post transduction, 1 mL of 10% RPMI (1%p/s+1%Glutamax+1%HEPES) +
> 100IU IL2** was added… **72 hours after transduction** cells were stained for viability and flow
> was run… **the CM-137 program has both the highest percent live and mCherry positive** gamma delta
> T cells. Mean fluorescent intensity is the highest in CM-137."

Versus the NK parent (CRM 2022): program **EN-138**, AAV at **+30 min**, **300K MOI**. So the
γδ program was **empirically re-derived rather than inherited** — a real optimization — while the
AAV MOI dropped 4× to 75K with **no titration shown in γδ cells**. Claim 26 only requires "at least
1k". Whether 75K is optimized or operational is unanswerable from the document.

## Step 8 — duration to product: the editing timepoint is NOT the product timepoint

**This step was previously misframed.** d14–21 is when the cells are *edited*, not when the product
exists. The patent adds a post-transduction culture period on top:

> "It is understood and herein contemplated that **the period of culturing of the CD70 CAR-expressing
> γδ T cells can be between 1- and 14-days post AAV infection** (i.e., 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
> 11, 12, 13, or 14 days)." — [0079]

> "**29.** The method of claims 7-28, wherein generating expanded CD70 CAR-expressing γδ T cells,
> **post-transduction, occurs in at least 14 days**."

So **Protocol B to a CAR product = [2 d anti-CD3/CD28 priming + feeder expansion to d14–d21] +
1–14 d post-transduction ≈ 15–35 days**, i.e. up to five weeks — not the "2–3 weeks" previously
stated. ([0095] fixes the priming phase at exactly 2 days, so the feeder phase is d2→d14 or d2→d21,
i.e. **12–19 days of feeder co-culture, or 2–3 weekly re-stimulation cycles**.)

And Portillo's "≥5 weeks" is time to functional assay of *unedited* cells. Their **CAR** product runs
longer: ≥5 wk expansion → electroporation → feeders at 48 h → "**cryopreserved after 7 days**" →
"replenished with irradiated K562 mb-IL-21 cells **weekly post-thaw** to expand cells for functional
assessment", with CAR tracked "over **21-days** of expansion".

**Corrected comparison: B ≈ 2–5 weeks to CAR product; A ≈ 6+ weeks.** A real but modest difference of
roughly one to two weeks — not the large gap previously claimed. Consequences: (a) "duration to
product" is a weak differentiator between the two protocols; (b) the argument that B implements
Portillo's "decreasing the length of the expansion process may be advantageous" is weakened — B is
shorter, but not dramatically. What survives is that **B reaches an *editable* state at d14 vs
≥5 weeks in A**, and that **B's TCR-agonist phase is bounded at ≤7 days regardless of total culture
length**. "Short" holds for the TCR window, not for the process.

⚠️ **[0079] and claim 29 contradict each other**: the description caps the post-transduction period
at 14 days ("between 1- and 14-days"), the claim sets 14 days as a floor ("at least 14 days"). On
top of the anchor mismatch already noted (claim 29 counts from transduction; the Example counts
"14 days after isolation and expansion").

⚠️ **No data exist for this period.** The Examples confirm CAR only at **48 h post-transduction** by
Protein L flow. The 1–14 d post-transduction expansion the claim rests on is entirely unexemplified.

### Duration head-to-head, both sources verified

| Phase | **B (WO2025123022A1)** | **A (Portillo 2025)** |
|---|---|---|
| TCR priming | **2 days** anti-CD3+CD28 [0095] | **none** |
| Feeder co-culture before editing | **d2 → d14** (CD70-CAR) or **d2 → d21** (mCherry) | "γδ T cells were expanded for a **minimum of 5 weeks** prior to use in functional assays"; subsets tracked to **8 weeks** |
| Feeder cadence | "Cells were expanded **every 7 days**" [0095] | "replenished with irradiated feeder cells on a **weekly basis**" |
| IL-2 | 100 IU **every other day** | 100 U/mL, "replaced **every two to three days**" |
| Post-edit culture | **1–14 d** ([0079]) / "at least 14 days" (cl. 29) | feeders at **48 h**, "**cryopreserved after 7 days**"; CAR stability then tracked "over **21-days** of expansion" post-thaw |
| **Total to CAR product** | **≈15–35 days** | **≈6+ weeks** (≥5 wk expansion, then edit, then 7 d, then post-thaw re-expansion) |

Both cadences are weekly and both IL-2 schedules are q2–3 d — **the feeder engine runs identically.**
The entire duration difference sits in **how long the cells are grown before editing**: ~2–3 weeks in
B versus ≥5 weeks in A. B's 2-day TCR pulse is not what makes B shorter; **skipping three-plus weeks
of pre-editing feeder culture is.**

Note also that A's mid-culture CD3⁺ re-isolation and re-expansion (absent in B, unnecessary because
B starts γδ-pure) is part of why A takes ≥5 weeks — a purity step that costs weeks of calendar time.

### Expansion-phase duration: the patent also contradicts itself here

[0079], consecutive sentences:

> "γδ T cell expansion **can take between 1 to 21 days** (1, 2, 3, … or 21. In some embodiments γδ T
> cell expansion **takes at least 21 days after isolation** of γδ T cells."

Both. Plus claim 19 ("**expanded for at least 7 days**"), claim 46 (same), and claim 20 ("**at least
21 days after isolation** … at least 3 million γδ T cells/condition were electroporated"). The
Examples edit at **21 days** (mCherry) and **14 days** (CD70-CAR).

The defensible statement is: **the claimed floor is 7 days of feeder expansion; editing is performed
at 14–21 days after isolation in the worked examples; the description covers everything from 1 day
to ≥21 days; and the CAR product follows 1–14 days after that.** My earlier flat "at least 21 days"
over-read one sentence. What survives intact is the substantive point: **nothing here is a short
culture, so "short TCR expansion" cannot mean short total process.**

## Step 9 — CD70 CAR knock-in *(Example)*

> "CD70 CAR γδ T cells were generated **14 days after isolation and expansion**. Flow staining prior
> to CAR generation showed a **97.1% expression of CD70** on the surface of γδ T cells… To prevent
> fratricide, **CD70 was knocked-out simultaneously with the integration of the CD70 CAR construct
> into the AAVS1 safe-harbor site**… using AAV6 virus harboring CD70CAR containing homology arms for
> AAVS1 (**TT826-4 CD70CAR Gen2**). Virus was added **20 minutes following the electroporation** of
> cas9/RNP containing **200uM of CD70 (AGCGTGGATGCACACCACG)** and **AAVS1 (GGGGCCACTAGGGACAGGAT)**
> targeting gRNAs plus **6.2uM of ALT-R® S.p. HiFi Cas9 Nuclease V3 (cat# 1081061)** (incubated for
> **20 minutes**), at an **MOI of 75k**. **24 hours post transduction 500uL of media was added** and
> **48 hours after transduction** CD70CAR γδ T cell generation was confirmed by flow cytometry using
> **Biotinylated Recombinant Protein L**… we were able to generate **CD70CAR in both Vδ1 and Vδ2
> subsets**."

The AAVS1 gRNA `GGGGCCACTAGGGACAGGAT` is **the same sequence as the NK protocol**, as is the ~20–30
min AAV window — the editing toolkit is a direct port.

⚠️ **"200uM of CD70 [gRNA] plus 6.2uM of Cas9" is a ~32:1 molar excess of guide over enzyme.**
Standard RNP assembly is ~1.2–3:1. Either these are stock rather than final concentrations, or a
unit is wrong. Do not reproduce this stoichiometry without checking.

⚠️ **CAR-in-both-subsets is a qualitative flow observation.** The patent never reports the Vδ1:Vδ2
*ratio* of the product. "Polyclonal" is supported; the composition is unquantified.

---

## Internal inconsistencies and drafting defects found

| # | Location | Problem |
|---|---|---|
| 1 | [0079] | "expansion can take between **1 to 21 days**" vs "takes **at least 21 days**" — contradictory in adjacent sentences |
| 2 | [0079] | MOI given as "about 1 to about **1000K** MOI (e.g., about 5 to **500K**)" then enumerated "…450, or **500 MOI**" — the K is dropped mid-paragraph, a 1000× ambiguity |
| 3 | Claim 2, [0005] | "**γ1δ9 or a γ2δ9** T cell" — not valid nomenclature. Intended Vγ9Vδ1 / Vγ9Vδ2. This is in a *claim*, so it recites a cell type that does not exist |
| 4 | Claim 29 vs Example | Claim: CAR-expressing γδ cells generated "**post-transduction, occurs in at least 14 days**". Example: "generated **14 days after isolation and expansion**". Different anchors (transduction vs isolation) for the same number |
| 4b | Claim 29 vs [0079] | Description **caps** the post-transduction period at 14 d ("between 1- and 14-days post AAV infection"); claim 29 makes 14 d a **floor** ("at least 14 days"). Direct contradiction |
| 5 | [0078] / claims 12–16, 39–46 | **Irradiation of the K562 feeders is never recited** (only in the [0077] alternatives list, which also permits "nonirradiated") |
| 6 | [0079] | "electroporated **and transduced** with Cas/RNP complexes" — Cas9/RNP is electroporated, not transduced |
| 7 | Throughout | Feeder line spelled **CStX-002** in [0076] and **CSTX-002** in [0078]/claims 15, 42 |
| 8 | Claim 12 | Depends on "claims **8**-11", skipping claim 7 — the independent claim it ultimately needs |
| 9 | Claims 7–46 | Pervasive improper multiple dependency ("The method of claims 7-10"). Fine for PCT filing; will need amendment on US national-phase entry |
| 10 | Example (CD70) | gRNA 200 µM vs Cas9 6.2 µM — implausible ~32:1 molar ratio |
| 11 | [0075] | The negative-selection rationale is illustrated with a **myeloid** depletion cocktail (CD33/CD34/CD123/CD11c/CD36), which has nothing to do with the γδ kit actually used |

## What is exemplified vs claimed vs merely described

| Element | Example (data) | Claim | Description |
|---|---|---|---|
| Ficoll/PBMC prep | ✅ full detail | — | ✅ |
| γδ negative selection | ✅ full detail + yield (700k from 20M PBMC) | ✅ cl. 9 | ✅ [0074-75] |
| **anti-CD3 + anti-CD28 priming** | ✅ **[0095]: Tonbo clones, plate-coated, 2 days** | ✅ cl. 10–11 | ✅ [0076] |
| **mbIL21 K562 (CSTX002) feeder** | ✅ **[0095]** | ✅ cl. 12–15, 39–42 | ✅ [0076-78] |
| **2:1 ratio (feeder:cell)** | ✅ **[0095]** | ✅ cl. 16, 43 | ✅ [0078]; [0077] also allows 1:2 and 1:1 |
| **100 IU IL-2 every other day** | ✅ **[0095]** | ✅ cl. 17–18, 44–45 | ✅ [0078] |
| **Weekly feeder re-stimulation** | ✅ **[0095]** | ❌ not claimed | ❌ not described |
| Feeder **irradiation** | ❌ | ❌ | ❌ only in [0077] alternatives list |
| Growth curve to 2 wk | ✅ **FIG. 1A** (no numbers in text) | — | — |
| 98.8% CD3⁺ / 98.4% γδ⁺ | ✅ | — | — |
| Vδ1/Vδ2 subset staining | ✅ **FIG. 1B** (no percentages in text) | — | — |
| Electroporation program screen | ✅ EO-115/CM-137/EH-115 → CM-137 | ❌ not claimed | ❌ |
| AAV6 +20 min, MOI 75K | ✅ | ✅ cl. 26 as "**at least 1k**" | ✅ [0079] as 1–1000K |
| CD70 KO + CD70-CAR KI | ✅ (flow at 48 h only) | ✅ cl. 30 | ✅ [0080] |
| 1–14 d post-transduction expansion | ❌ **no data** | ✅ cl. 29 | ✅ [0079] |
| Fold expansion (number) | ❌ | ❌ | ❌ |
| Vδ1:Vδ2 of product | ❌ | ❌ | ❌ |
| Long vs short anti-CD3 | ❌ | ❌ | ❌ |
| Exhaustion / STAT / telomere | ❌ | ❌ | ❌ **(0 occurrences)** |

**Bottom line (revised after finding [0095]).** Both halves of Protocol B are exemplified. The
expansion protocol is reproducible at the bench from [0095] — catalog numbers, cell numbers, ratio,
cytokine cadence and weekly re-stimulation are all stated. Two real gaps remain: **feeder
irradiation is never mentioned**, and **no quantitative expansion outcome appears in the text**
(FIG. 1A/1B carry the data; the narrative reports only 98.8% CD3⁺ / 98.4% TCRγδ⁺).

What is missing is not the protocol but the *rationale*: **"exhaustion", "STAT", "JAK" and
"telomere" appear zero times.** The 2-day window is used, never justified; no duration comparison
exists. Claims 39–46 separately claim mbIL-21 feeder culture as a method of making γδ cells
"susceptible to gene editing" — the honest framing: the feeder phase is claimed for what the
document demonstrates it enables (editing), not for an exhaustion benefit it never attempts to show.
