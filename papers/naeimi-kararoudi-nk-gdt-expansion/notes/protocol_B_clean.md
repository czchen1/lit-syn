# Protocol B (WO2025123022A1) — clean single-source version

Patent-only. Where a step is exemplified, the worked value is given and the claim range noted
alongside. **No values from Portillo et al. are imported into this document** — see the change log
for why that mattered.

Source tiers: **[E]** worked example · **[D]** description · **[C]** claim.

---

### 1. Starting material **[E]**

> "PBMCs are isolated from **buffy coat purchased from RedCross** using a density gradient
> centrifugation… layered on top of **15mL of Ficol**… **500g for 30min** (ACC-5; DEC-0)… washed with
> PBS1x (**400g for 10min**)… a single cell suspension was prepared… at **5 x 10^7 cells/mL**."

Healthy-donor buffy coat, standard Ficoll.

### 2. γδ isolation — immunomagnetic **negative** selection **[E]** + **[C9]**

> "**StemCells EasySep™ Human Gamma/Delta T Cell Isolation Kit (cat# 19255)** was used to isolate γδ
> T-Cells based on an **immunomagnetic negative selection**."

Worked procedure: **50 µL/mL** Isolation Cocktail, 15 min RT → **50 µL/mL** magnetic particles,
10 min → 2.5 mL medium → magnet 5 min → invert. **A second particle round follows** (37.5 µL, 5 min
incubation, 5 min magnet).

**Yield [E]:** "**700,000 γδ T-Cells were isolated from 20,000,000 PBMCs**" (3.5%).

Rationale **[D, 0075]**:

> "Negative immunomagnetic selection has been the method of choice… due to concerns that **binding
> antibodies to the cell surface may induce cellular activation, block ligand-receptor interactions
> or result in immune clearance**."

*Caveat: the patent never states kit #19255's depletion cocktail. The only cocktail it names
(CD33/CD34/CD123/CD11c/CD36, [0075]) is a myeloid example, unrelated to this kit.*

### 3. TCR priming — plate-bound anti-CD3 **+** anti-CD28, **2 days** **[E]** + **[D0076]** + **[C10–11]**

Worked conditions **[E, 0095]**:

> "**350,000 cells** were seeded in completed RPMI (**10% FBS, 1% Pen-Strep, 1% GlutaMax, 1% HEPES**)
> and **supplemented with 100IU IL2** on an **anti CD3 (Tonbo Bioscience cat# 40-0038-U100) and anti
> CD28 (Tonbo Bioscience cat# 40-0289-U100) coated plate** for their stimulation. **Two days
> post-stimulation**…"

Mechanism **[D, 0076]**:

> "**anti-CD3 activates all T cells regardless of their antigen specificity by crosslinking the
> TCR-CD3 signaling machinery**"

Claim scope **[C11]**: "at least 2 days". Description range **[D]**: "at least 6 hours… 1, 2, 3, 4,
5, 6, 7 days" — a nested drafting ladder, **not** three findings. The worked value is **2 days**.

Two consequences of *plate-bound*: (a) negative selection removed FcR⁺ accessory cells, so soluble
anti-CD3 would not crosslink — the coated plastic replaces them; (b) the stimulus terminates when
cells are lifted off, making duration a controlled variable.

**Note: IL-2 100 IU is present from day 0**, in the priming medium. The TCR window is not
cytokine-free.

### 4. Feeder cells — mbIL21 K562 (CSTX002) **[E]** + **[D0076/0078]** + **[C12–15, 39–42]**

> "genetically engineered **K562.mbIL21.4-1BBL** feeder cells including, but not limited to
> **CStX-002** cells" — [0076]

Worked **[E, 0095]**: "**mbIL21 K562 feeder cells (CSTX002)**".

⚠️ **The patent never states these feeders are irradiated** — not in [0078], not in [0095], not in
any claim. "Irradiated" appears once, in the [0077] alternatives list, which also permits
"nonirradiated". Certainly intended; not recited.

### 5. Feeder ratio — **2:1 feeder:cell** (= 2 feeders per γδ cell) **[E]** + **[C16, 43]**

> "cells were counted and **expanded at a 2:1 ratio with mbIL21 K562 feeder cells (CSTX002)**"
> — [0095]

Claim 16 / 43: "at least a **2:1** ratio with mbIL21-expressing feeder cells."

[0077] additionally describes "**1:2, 1:1, or 2:1**" as options, but that paragraph is
broad-coverage boilerplate (it also covers EBV-LCL, RPMI8866, HFWT and mbIL-15). **The operative,
claimed and exemplified value is 2:1 feeder:cell.**

*For cross-reading only: Portillo's "1:2" is written cells:feeder and is **the same density** —
2 feeders per γδ cell. The two protocols do not differ here.*

### 6. Cytokine + feeder schedule **[E]** + **[C17–18, 44–45]**

Worked **[E, 0095]**: complete RPMI (10% FBS / 1% P-S / 1% GlutaMax / 1% HEPES); "**supplemented
with 100IU IL2 every other day**, media was added as necessary"; "**Cells were expanded every 7
days**" (weekly feeder re-stimulation).

Claims 17–18 / 44–45: 100 IU IL-2, "at least every 48 hours".

### 7. Mid-expansion re-isolation — **not required**

Day-0 negative selection yields a γδ-pure culture, so there is no NK or αβ overgrowth to correct.
*(Contrast: Portillo must CD3⁺-re-isolate mid-culture because "the majority of expanded live cells
in the bulk PBMC co-cultures were NK cells".)*

### 8. Culture length **[E]** + **[D0079]** + **[C19–20, 29, 46]**

| Phase | Value | Tier |
|---|---|---|
| Priming | **2 days** | [E, 0095] |
| Feeder expansion before editing | to **day 14** (CD70-CAR) or **day 21** (mCherry) | [E] |
| Claimed feeder-expansion floor | "at least **7 days**" | [C19, C46] |
| Post-transduction culture | "**1- and 14-days** post AAV infection" | [D0079] |
| — same, as claimed | "post-transduction, occurs in **at least 14 days**" | [C29] |
| **Total to CAR product** | **≈15–35 days** | derived |

⚠️ Two internal contradictions: [0079] says expansion "can take between **1 to 21 days**" *and*
"takes **at least 21 days** after isolation"; and the post-transduction period is **capped** at 14 d
in [0079] but **floored** at 14 d in claim 29.

**Purity at 2 weeks [E]:** "**98.8% of the expanded cells are CD3+ T cells and 98.4% are TCRγδ+**."
FIG. 1A is a growth curve and FIG. 1B stains Vδ1/Vδ2, but **no fold-expansion value and no subset
percentages appear in the text.**

### 9. Gene editing — simultaneous KO + KI **[E]** + **[C20–30]**

Electroporation, optimized **[E, 0100]**: 3×10⁶ cells/condition, **P3 buffer**, 4D-Nucleofector;
**EO-115 / CM-137 / EH-115** screened — **CM-137 won** on percent-live, percent-mCherry⁺ and MFI.
*(NK parent uses EN-138, so this was genuinely re-derived for γδ.)*

**AAV6 added 20 minutes post-electroporation**, MOI **75K** [E]; claim 26 requires only "at least
1k"; [0079] describes 1–1000K. *(NK parent uses 300K — the 4× reduction is unexplained and
untitrated in γδ.)*

CD70-CAR **[E]**, at day 14:

> "**97.1% expression of CD70** on the surface of γδ T cells… To prevent fratricide, **CD70 was
> knocked-out simultaneously with the integration of the CD70 CAR construct into the AAVS1
> safe-harbor site**."

One electroporation, **two guides** — CD70 `AGCGTGGATGCACACCACG` and AAVS1
`GGGGCCACTAGGGACAGGAT` — plus one AAV6 (TT826-4 CD70CAR Gen2) carrying AAVS1 homology arms. Cas9
cuts identically at both loci; **the outcome differs only because a homologous template is supplied
at AAVS1 and not at CD70**: NHEJ → frameshift → knockout at *CD70*; HDR → knock-in at *AAVS1*.

Confirmed by Protein L flow **48 h post-transduction**, "in both **Vδ1 and Vδ2** subsets".

Claim 30 generalizes to "**CD70, CD38, CD33, or TGFβRII**" — the first three are fratricide logic,
TGFβRII is TME resistance, a different rationale.

**Why the feeder phase is the invention:** claims 39–46 separately claim mbIL-21 feeder culture as
"a method of making γδ T cells **susceptible to gene editing**". HDR requires S/G2 and an active
BRCA1/2–RAD51–LIG4 program; his NK work showed feeder expansion upregulates exactly that.

⚠️ Not demonstrated: KO efficiency, KI efficiency, any fratricide-rescue comparison, cytotoxicity,
or genomic-integrity assessment after two simultaneous DSBs (both loci are on chr19). And the
printed RNP stoichiometry — **200 µM guide vs 6.2 µM Cas9**, ~32:1 — is implausible against a
standard 1.2–3:1; likely stock, not final, concentrations.

---

## Change log against the prior draft

| # | Step | Change | Rationale |
|---|---|---|---|
| 1 | **5. Ratio** | Replaced Portillo's "1:2 cells:feeder" with the patent's own **[0095] "2:1 ratio with mbIL21 K562 feeder cells"** | The prior draft imported Protocol **A**'s number into a Protocol **B** document. The patent exemplifies its own ratio. Both happen to equal ~2 feeders/cell, so the biology is unchanged — but the sourcing was wrong |
| 2 | **5. Ratio** | Demoted "patent allows 2:1, 1:1, or 1:2" to a footnote | That list is [0077] broad-coverage boilerplate (it also covers mbIL-15, EBV-LCL, HFWT). Presenting it as the operative range implies the protocol is undecided; the claimed and worked value is a single number |
| 3 | **6. Schedule** | Replaced the Portillo RPMI/weekly-feeder quote with **[0095]**: cRPMI + 10% FBS/1% P-S/1% GlutaMax/1% HEPES, **100 IU IL-2 every other day**, "**expanded every 7 days**" | Same import problem. The patent states its own full medium composition and its own weekly cadence — nothing needs to be borrowed |
| 4 | **3. Stimulation** | Kept "**and**" (not "and/or") but re-sourced it to **[0095]**, not [0076] | [0076] genuinely says "and/or" — that's claim-breadth drafting. The *worked example* uses both antibodies, with catalog numbers. "and" is right; the citation had to move |
| 5 | **3. Stimulation** | "stimulation time is 2 days" re-sourced to **[0095]**; claim 11 = "at least 2 days" | 2 days is the exemplified value, not what [0076] says. [0076] gives a 6 h – 7 d ladder |
| 6 | **3. Stimulation** | Added that **100 IU IL-2 is in the priming medium from day 0** | Material: the TCR window is not cytokine-free, which weakens any clean "TCR-only phase" reading |
| 7 | **4. Feeders** | Added the **irradiation omission** flag | The patent never recites irradiation for the K562 feeders. For a therapeutic process this is a material gap as written |
| 8 | **8. Length** | Answered, with the editing/product distinction: **2 d + feeder to d14–21 + 1–14 d post-transduction ≈ 15–35 days** | The editing timepoint is not the product timepoint; conflating them understates the process by ~2 weeks |
| 9 | **2. Isolation** | Added the **yield** (700k from 20M PBMC) and the **second magnetic round** | Both are in the worked example and both matter for planning a run |
| 10 | **3. Stimulation** | Added **350,000 cells seeded** | Half the isolated yield; the only seeding density stated |
| 11 | **9. Editing** | Added the **CM-137 screen**, P3 buffer, 3×10⁶ cells, **MOI 75K** | The electroporation optimization is the patent's single strongest dataset and was missing |
| 12 | **9. Editing** | Explained *why* one Cas9 gives KO at one locus and KI at another (template present vs absent) | The prior line stated the strategy without the mechanism that makes it work |
| 13 | Throughout | Tagged every line **[E] / [D] / [C]** | The prior draft cited [0076] and "claims 10–11" for a value that comes from a worked example; the tiers were blurring |
