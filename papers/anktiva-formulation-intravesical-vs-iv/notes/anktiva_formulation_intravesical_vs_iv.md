# ANKTIVA (nogapendekin alfa inbakicept-pmln, N-803): formulation and route evaluation — intravesical vs intravenous, with dilution arithmetic

Scope: why the approved bladder-cancer product is a 0.4 mL protein concentrate diluted into a
50 mL BCG instillation rather than a parenteral dose, what the dilution step actually does to
concentration and exposure, and what the IV/SC literature on the same molecule says about the
route that was not chosen. Sources are the FDA (US) and EMA product information for ANKTIVA,
the FDA approval summary, and the curated literature in `../index.tsv`.

**Regulatory boundary, stated once and applied throughout.** The marketed product is labelled
*For Intravesical Use Only*; the US label directs that it must **not** be given by the
subcutaneous, intravenous or intramuscular route. Nothing below is an IV regimen for ANKTIVA.
The IV/SC material is the investigational ALT-803/N-803 record, used as the comparator that
explains what route selection buys and costs.

---

## 1. What is in the vial

| Attribute | Value |
| --- | --- |
| Active moiety | Nogapendekin alfa inbakicept-pmln (N-803, formerly ALT-803) |
| Architecture | 2 × IL-15N72D superagonist bound to one inbakicept dimer (IL-15Rα sushi domain fused to human IgG1 Fc) |
| Deglycosylated MW | 92,106.5 Da |
| Presentation | Single-dose vial, 400 mcg in 0.4 mL solution → **1,000 mcg/mL concentrate** |
| Excipients | Dibasic sodium phosphate, monobasic potassium phosphate, sodium chloride, water for injection; HCl/NaOH for pH adjustment |
| pH | ~7.4 |
| Appearance | Clear to slightly opalescent, colourless to slightly yellow |
| Storage | 2–8 °C, protect from light, do not freeze, do not shake |

Three formulation facts drive the whole route argument:

1. **It is a large Fc-fusion protein (~92 kDa), not a small molecule.** Passive permeation across
   intact urothelium is size-limited, so a local instillation is an exposure strategy for the
   luminal surface and tumour/CIS lesions rather than a strategy for deep transmural delivery.
2. **It is an unbuffered-for-dilution, shear-sensitive protein in a phosphate/saline vehicle at
   physiologic pH.** Hence the "mix gently, do not shake" instruction, the short in-use window
   and the absence of any filtration step in the preparation directions.
3. **The IgG1 Fc exists to extend systemic half-life** — a property engineered for parenteral
   dosing that, in the intravesical setting, mostly serves molecular stability and receptor
   avidity, since the drug is voided after two hours.

## 2. The approved dilution, worked through

Preparation per the US/EU product information: prepare the BCG suspension in preservative-free
0.9 % sodium chloride according to that BCG product's instructions, add the entire 0.4 mL
ANKTIVA vial, and bring the admixture to **50 mL total volume**; mix gently; instil via urinary
catheter; retain for **2 hours**; void.

| Step | Arithmetic | Result |
| --- | --- | --- |
| Vial concentrate | 400 mcg ÷ 0.4 mL | 1,000 mcg/mL |
| Volumetric dilution | 0.4 mL → 50 mL | **125-fold (≈1:125 v/v)** |
| Nominal instilled concentration | 400 mcg ÷ 50 mL | **8 mcg/mL** |
| Molar equivalent | 8 mg/L ÷ 92,106.5 g/mol | **≈87 nmol/L** |
| Dose per instillation | fixed, not body-weight scaled | 400 mcg + 50 mg TICE BCG |

Two consequences worth stating plainly:

- **The 50 mL is a bladder-filling volume, not an infusion volume.** It is chosen to wet the
  whole urothelial surface at a volume patients can retain for two hours (intravesical practice
  converges on 40–60 mL; tolerability falls off above ~75 mL), not to make a protein solution
  isotonic or slow-infusible. The dilution factor is therefore set by bladder physiology, and
  the resulting 8 mcg/mL is a *consequence* of that choice rather than a targeted concentration.
- **87 nmol/L in the lumen is one to two orders of magnitude above the serum peaks parenteral
  dosing achieves.** Reported systemic references for the same molecule: serum Cmax ≈1 nmol/L
  after 5 mcg/kg, and ≈6 nmol/L after 0.03 mg/kg in preclinical work. The instillation therefore
  delivers a *higher local concentration than the systemic route can safely reach*, using
  1/100th of the molar amount a weight-based parenteral dose would require — the core
  pharmaceutical argument for the intravesical formulation.

**In-use handling.** The US label directs that if the admixture is not used immediately it be
refrigerated at 2–8 °C and used within two hours, discarding unused material. EMA product
information reports studied admixture stability of up to 2 hours at 2–8 °C with OncoTICE and up
to 24 hours at 2–8 °C, protected from light, with BCG-medac; these windows are
BCG-product-specific and should not be generalised across BCG strains. BCG viability, not the
protein, is the fragile partner in the admixture, which is also why the drug is added to a
prepared BCG suspension rather than the reverse.

## 3. Dilution does not stop at the syringe: intravesical dilution kinetics

The label's 8 mcg/mL is the concentration at t = 0. Inside the bladder, two further dilution
processes act during the 2-hour dwell:

- **Residual urine** left at instillation adds volume immediately. This is why intravesical
  protocols require pre-procedure fluid restriction (typically 4–6 h) and complete catheter
  drainage before instillation.
- **Continuous urine production** dilutes progressively over the dwell. Canine intravesical PK
  of mitomycin C and suramin showed exactly this: drug levels fell over the dwell period "due to
  continued urine production", while plasma concentrations stayed minimal (undetectable at low
  dose, or ~6,000× below urine concentrations).

That this matters clinically is not an inference. The randomised phase III trial of
pharmacologically optimised intravesical mitomycin C — higher dose, urine-volume reduction to
raise concentration, and urine alkalinisation for stability — improved 5-year recurrence-free
fraction to 41.0 % (95 % CI 30.9–51.1) vs 24.6 % (14.9–34.3) and median time to recurrence to
29.1 vs 11.8 months (P = .005) against standard instillation. Concentration, not just dose,
carried the effect.

Applied to ANKTIVA, with the caveat that no equivalent optimisation trial exists for this
product:

- The two-hour dwell is the label-specified exposure window; if the patient voids before two
  hours, the dose is **not** repeated. Dwell time beyond 1–2 hours has shown diminishing
  incremental benefit for intravesical agents generally.
- Post-instillation patient rotation is not supported by evidence and is not recommended by
  major urology guidelines; it is not part of the ANKTIVA directions either.
- Because the product is a fixed 400 mcg dose in a fixed 50 mL vehicle, the only levers on
  achieved luminal concentration are bladder emptying and fluid restriction before instillation
  — i.e. clinical technique, not formulation.

## 4. Intravesical vs IV: exposure and toxicity

**Intravesical (approved).** Systemic exposure after the approved 400 mcg intravesical dose was
**below the limit of quantitation**; EMA reports concentrations below 100 pg/mL and below the
LLOQ in all patients. Efficacy support is Cohort A of QUILT-3.032 (N-803 400 mcg + 50 mg TICE
BCG weekly ×6 induction, second induction if no CR at month 3, then maintenance), with the dose
itself derived from a 100/200/400 mcg escalation in QUILT-2005. In that construction, the
100-fold-plus concentration advantage in the lumen is obtained with essentially no measurable
systemic drug.

**IV/SC (investigational, same molecule).** The route that was not chosen is well characterised:

| Setting | Route/dose | Key finding |
| --- | --- | --- |
| Phase I, advanced solid tumours | IV 0.3–6 mcg/kg vs SC 6–20 mcg/kg weekly | IV serum Cmax **>100-fold** higher than SC, Tmax 30 min (SC 8–24 h). IV toxicity was cytokine-typical: fatigue, nausea, vomiting, chills, fever. SC instead produced injection-site wheals in 11/13. No MTD defined either route |
| Phase I, post-allo-HCT relapse | IV or SC 1–10 mcg/kg weekly ×4 | IV: constitutional symptoms temporally tracking rises in serum IL-6 and IFN-γ. SC: self-limited lymphocyte-infiltrated injection-site rash, serum levels sustained >96 h; no DLTs |
| Phase I, healthy volunteers | SC | Serum peak ≈4 h, ≈20 h half-life; injection-site reactions, chills, pyrexia; no grade ≥3 events |
| Nonclinical toxicology | IV, cynomolgus monkey | Expected immune stimulation: raised WBC/lymphocyte counts, multi-organ lymphocytic and myeloid infiltration — the dataset FDA cites for *unexpected systemic exposure* in patients |

**Preclinical head-to-head in bladder cancer.** In the carcinogen-induced (BBN) orthotopic NMIBC
model, SC ALT-803 reduced tumour burden by 37 % vs 28 % for intravesical ALT-803 and 28 % for
intravesical BCG — i.e. the systemic route was not inferior on tumour burden. The distinguishing
result was the exposure signature: SC dosing expanded peripheral CD8⁺ T, NK and NKT populations
and raised serum IL-5/IL-6, whereas intravesical ALT-803 (alone or with BCG) had little to no
systemic effect. Route selection here is a decision about *where the pharmacology happens*, not
a claim that only local delivery can shrink tumours. Murine serum half-life was similar between
routes (7.50 h IV vs 7.71 h SC).

**Read-across from another intravesical cytokine.** Intravesical chitosan/IL-12 in mice produced
significantly lower cytokine dissemination and systemic exposure than SC injection, without
significant local or systemic toxicity — the same local-containment logic that justified taking
a cytokine with a known systemic-toxicity history into the bladder rather than the vein.

## 5. Formulation trade-offs of the intravesical choice

What the 50 mL instillation buys:

- High luminal concentration (≈87 nmol/L) at 1/100th of the parenteral molar dose.
- Systemic exposure below quantitation, hence no cytokine-release-type constitutional syndrome
  of the kind IV dosing of this class produces.
- Co-formulation with BCG in a single instillation: one catheterisation, one dwell, and IL-15
  agonism delivered into the same compartment and time window as the BCG stimulus.
- No weight-based dosing, no reconstitution of a lyophilisate, no infusion set — a
  pharmacy-simple admixture step.

What it costs, and where the evidence is thin:

- **Barrier-limited depth.** A ~92 kDa protein instilled into the lumen faces the mucus/GAG
  layer, umbrella cells and tight junctions. Other intravesical biologics engineer around this
  (e.g. the Syn3 excipient enabling adenoviral transduction for nadofaragene firadenovec;
  mucoadhesive, hydrogel and nanoparticle platforms in development). ANKTIVA carries no
  permeation enhancer, mucoadhesive or sustained-release element — a plain solution voided at
  two hours. Bladder-wall penetration depth for this molecule is not established in the
  published record reviewed here.
- **Uncontrolled in-vivo dilution.** Achieved concentration depends on residual urine and
  diuresis, neither of which the formulation controls; there is no ANKTIVA analogue of the
  optimised-mitomycin trial to quantify how much this costs.
- **Exposure limited to two hours per week-level interval**, versus the multi-day pharmacodynamic
  tail that Fc-extended half-life gives parenterally.
- **No systemic component.** For patients whose risk is occult extravesical disease, a
  local-only exposure is a deliberate ceiling; the systemic arm of that trade-off is a different
  product decision (e.g. systemic checkpoint inhibition), not a dilution or dose change.
- **Admixture constraints.** In-use window depends on the BCG partner product, and the "do not
  shake" instruction reflects a protein that is not formulated for agitation, transport or
  filtration.

## 6. Limits of this comparison

- The IV/SC data are for ALT-803/N-803 in solid tumours, post-transplant relapse and healthy
  volunteers — different populations, weight-based doses and endpoints. They characterise the
  molecule's systemic behaviour; they do not describe an ANKTIVA IV regimen, which does not
  exist and is contraindicated by the label.
- "Below the limit of quantitation" is an assay statement about serum, not proof of zero
  systemic biological effect; FDA still applies reproductive-risk precautions on mechanistic
  grounds in case of systemic exposure.
- The 8 mcg/mL and 87 nmol/L figures are nominal at t = 0 in a 50 mL admixture and are not
  measured intravesical concentrations.
- Cross-route potency comparison at the molar level assumes the receptor pharmacology is the
  same in the bladder lumen as in serum; local binding, urine composition and protein
  adsorption effects were not quantified in the reviewed literature.

---

## Key numbers

| Quantity | Value |
| --- | --- |
| Vial | 400 mcg / 0.4 mL (1,000 mcg/mL) |
| Final admixture volume | 50 mL (with 50 mg TICE BCG in preservative-free 0.9 % NaCl) |
| Dilution factor | ~125-fold |
| Nominal instilled concentration | 8 mcg/mL ≈ 87 nmol/L |
| Dwell | 2 hours, then void; no repeat if voided early |
| Systemic exposure, intravesical | < LLOQ (< 100 pg/mL) |
| IV vs SC Cmax, parenteral ALT-803 | IV > 100-fold higher, Tmax 30 min vs 8–24 h |
| Route restriction | Intravesical only; not IV/SC/IM |
