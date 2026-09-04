# ANKTIVA (N-803) formulation for bladder cancer: intravesical vs IV, including dilution

Literature collection assembled to evaluate why the approved bladder-cancer presentation of
nogapendekin alfa inbakicept-pmln (ANKTIVA, N-803/ALT-803) is a 0.4 mL protein concentrate
diluted into a 50 mL BCG instillation rather than a parenteral dose — what the dilution step
does to concentration and exposure, and what the IV/SC record on the same molecule says about
the route that was not chosen.

ANKTIVA is labelled for intravesical use only and must not be given IV, SC or IM. The IV/SC
literature here is the investigational ALT-803/N-803 comparator record, not an IV regimen for
the marketed product.

## Read this first

`notes/anktiva_formulation_intravesical_vs_iv.md` — the evaluation: vial composition and what
the ~92 kDa Fc-fusion architecture implies for local delivery, the 125-fold dilution worked
through to 8 mcg/mL ≈ 87 nmol/L, further in-vivo dilution by residual urine and diuresis during
the 2-hour dwell, intravesical (< LLOQ systemic) vs IV/SC exposure and toxicity for the same
molecule, formulation trade-offs of the local route, and the limits of the cross-route
comparison.

## Directory structure

- `harvest.py` → `raw_harvest.json` — Europe PMC search across 6 query domains (N-803/ALT-803
  molecule and intravesical use; systemic IL-15 agonist PK/toxicity; intravesical PK, dilution
  and dwell time; urothelial permeability to macromolecules; intravesical formulation and
  delivery devices; local-vs-systemic route comparisons). 8,333 unique records.
- `curate.py` → `index.tsv`, `curated.json` — regex scoring for agent identity (N-803 vs other
  IL-15 agonists vs intravesical agents generally) crossed with route, pharmacokinetic,
  dilution/dwell, formulation, barrier-penetration and systemic-toxicity signal; non-oncologic
  bladder and immune-disease records are filtered out. 393 records kept.
- `fetch_fulltext.py` → `fulltext/` — open-access full-text XML from Europe PMC, falling back to
  NCBI E-utilities for records Europe PMC serves empty. 236 of 393 indexed records have a
  PMCID and all 236 downloaded; the remaining 157 are metadata-only (no OA full text).

`raw_harvest.json`, `harvest.log`, `fetch.log` and `fulltext/` are gitignored; regenerate with
`python3 harvest.py && python3 curate.py && python3 fetch_fulltext.py`.

## Categories in `index.tsv`

- `n803_anktiva_bladder` — the molecule in bladder cancer/intravesical settings.
- `n803_systemic_other_indications` — the same molecule dosed IV/SC elsewhere, kept where it
  carries route, PK, formulation or systemic-toxicity data.
- `il15_systemic_route_pk` — other IL-15 agonists, for class-level systemic behaviour.
- `intravesical_pk_dilution` — instillation pharmacokinetics, dilution, urine chemistry, dwell.
- `intravesical_biologics_barrier` — urothelial barrier and delivery of proteins/gene therapy.
- `formulation_delivery_systems` — mucoadhesives, hydrogels, nanocarriers, devices.
- `local_vs_systemic_immunotherapy`, `bladder_cancer_context`, `reviews_guidelines`.

## Scope notes

Records run to 2026 and are weighted recent (290 records 2020+, 133 from 2025+). Curation keeps
distinctions that are easy to blur in a route argument:

- Approved intravesical ANKTIVA vs investigational IV/SC ALT-803/N-803.
- Nominal admixture concentration at t = 0 vs concentration achieved in the bladder after
  residual urine and diuresis.
- Measured systemic exposure (below limit of quantitation intravesically) vs mechanistic
  systemic risk.
- Formulated permeation enhancement (e.g. Syn3, mucoadhesives, hydrogels) vs plain solution
  instillation, which is what ANKTIVA is.
- Preclinical route head-to-heads in bladder models vs human dose-finding in other indications.

Regulatory and label facts in the note (composition, MW, dilution directions, in-use stability,
route restriction) come from the FDA and EMA product information and the FDA approval summary;
they are cited in the note rather than harvested into `index.tsv`.
