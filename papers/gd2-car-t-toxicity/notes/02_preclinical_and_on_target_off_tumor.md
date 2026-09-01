# 02 — Preclinical toxicity and on-target / off-tumour GD2 biology

## The affinity trap

**Richman 2018 (PMID 29180536)** [preclinical] is the reference hazard for this antigen. Variants of
the 14G2a scFv engineered for improved stability/affinity, including **E101K**, gave better
antitumour activity against GD2⁺ neuroblastoma xenografts **and lethal CNS toxicity**: extensive CAR
T-cell infiltration and proliferation in brain with neuronal destruction, an encephalitis localised
to **cerebellum and basal brain regions that express only low amounts of GD2**.

Three conclusions that constrain every subsequent GD2 CAR design:

1. Toxicity was not driven by high-antigen tissue — it appeared where GD2 is *low*, i.e. affinity
   raised the CAR above the antigen-density threshold that normally protects normal tissue.
2. Antibody safety does not transfer to CAR safety at the same epitope: dinutuximab is approved,
   yet the same binder in a high-affinity CAR was fatal in mice.
3. The clinically used GD2 CARs deliberately keep **standard 14g2a affinity**, which is why the
   density-discrimination argument (Majzner 2022 autopsy: tumour GD2 ≫ normal brain GD2) is load
   bearing rather than rhetorical. Affinity-tuning literature in the collection
   (PMID 34966954) makes the same point generically.

## Brainstem inflammation predicted the clinical problem

Preclinical H3K27M DMG models with GD2-CAR T cells (Mount 2018, PMID 29662203) [preclinical] showed
clearance of tumour **and** brainstem oedema in a fraction of mice, progressing to obstructive
hydrocephalus because of the neuroanatomy. This is the direct ancestor of the clinical TIAN
management algorithm: the Stanford protocol excluded bulky thalamic and cerebellar tumours,
mandated an Ommaya for ICP monitoring in DIPG, and pre-specified CSF removal, hypertonic saline,
anti-cytokine agents and corticosteroids (Majzner 2022, PMID 35130560).

So the preclinical signal that mattered was **not** on-target off-tumour neurotoxicity — it was
*on-tumour* inflammation in a space-limited compartment.

## What normal-tissue GD2 does with antibodies

[GD2-antibody] evidence sets the expectation for target engagement in normal nerve:

- Anti-GD2 antibodies cause **dose-limiting on-target/off-tumour neuropathic pain** in most children
  (ACCELERATE Paediatric Strategy Forum, PMID 41240535; mechanism review PMID 34884452).
- Rat models reproduce anti-GD2-induced allodynia and it is reducible by pretreatment (DFMO,
  PMID 32697811); dinutuximab variants engineered for reduced neuropathy induction exist
  (PMID 35792784); complement/Fc engineering and IgA formats are being used to dissociate efficacy
  from pain (PMID 37479484).
- FAERS disproportionality analysis of dinutuximab/dinutuximab β/naxitamab (PMID 38153627) confirms a
  broad real-world toxicity spectrum including signals absent from labels.

The clinical GD2 CAR-T experience does **not** reproduce this: no painful neuropathy in the Stanford
DMG cohort (Monje 2025), none attributed in Straathof 2020, only transient grade 1–2 neuropathic pain
in 4SCAR-GD2 (PMID 34724115). Plausible reasons — different effector mechanism (no complement
activation on nerve), lower and non-repeated peak target occupancy on nerve, and antigen-density
thresholding — but this is inference, not a demonstrated mechanism.

## Preclinical work on making it safer

- **iCasp9/AP1903** eliminates activated CAR T cells preferentially and is built into GD2-CART01,
  4SCAR-GD2 and the Stanford construct (PMID 25389405; medulloblastoma model PMID 38551501 showing
  CAR⁺ fraction 76.3% → 9.4% after AP1903).
- **Costimulation-only / logic-gated designs** to avoid activation on normal tissue
  (PMID 28341563, ALK AND-gate PMID 36396552).
- **Microenvironment-actuated and density-dependent ("velcro-like") CARs** claiming efficacy without
  toxicity (PMID 39841845, PMID 41005308); sonogenetic spatial control (PMID 40179881).
- Murine **neurofilament light chain** as a circulating neuroaxonal injury biomarker in CAR-T models
  (PMID 38551501) — the obvious translational readout for a "did we injure nerve?" question that
  clinical GD2 trials currently answer only by examination.

## Transfer caveat

Xenograft models are lymphodepleted, immunodeficient and small; they cannot model human CRS
(no functional myeloid compartment), and the mouse brainstem has different compliance and CSF
dynamics. They have proven predictive for **spatial** risk (where inflammation is dangerous) and for
**affinity/architecture** risk, and predictive for nothing about hepatic, renal or drug-interaction
behaviour.
