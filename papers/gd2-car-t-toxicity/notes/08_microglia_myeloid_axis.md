# 08 — The myeloid/microglial axis: recruitment, states, and its relation to TIAN

The clinical toxicity of GD2 CAR-T in the CNS correlates better with **myeloid** readouts than with
T-cell readouts. This note collects what is actually measured, because it is the mechanistic bridge
between "CAR T cells engage tumour" and "the patient's brainstem swells".

## What is measured in GD2 CAR-T patients

**Tumour tissue (autopsy, DIPG-1; PMID 35130560)** [GD2-clinical]

- Prominent **microglial and other myeloid infiltration of tumour**: CD163⁺ myeloid cells throughout
  tumour tissue, and Iba1⁺ myeloid cells densely infiltrating H3K27M⁺ regions on confocal microscopy.
- In the **unaffected cortex** of the same patient, CD163 staining showed only microglia in their
  resting perivascular position — **no reactive microglia/macrophages**. Combined with CAR transcript
  and lymphocytic infiltrate confined to tumour, and tumour GD2 ≫ normal-brain GD2, this is the
  strongest single piece of human evidence that the inflammatory response is spatially restricted to
  tumour rather than provoked diffusely in normal brain.

**CSF single-cell RNA-seq across routes (PMID 35130560)** [GD2-clinical, ICV-clinical]

- CSF myeloid cells resolved into **seven clusters** — monocytes, microglia and macrophages with
  distinct functional signatures, plus a proliferating myeloid cluster (myeloid identity called on
  AIF1, CSF1R, CX3CR1, CD14, CD68, CD163).
- **Route-dependent myeloid states**:
  - after **ICV** administration, at peak inflammation, an **interferon-response myeloid population**
    dominates;
  - after **IV** administration and at late timepoints, myeloid cells instead express **phagocytosis
    and lipid-metabolism programmes** with a strongly **immune-suppressive** profile, aligning with
    **disease-associated microglia (DAM)**, **MDSC** and **axon-tract-associated microglia** signatures.
- The patient with the most severe intracranial events (DIPG-1) had **differentially increased
  interleukin, chemokine and neutrophil-degranulation pathways** in the CSF myeloid fraction relative
  to the other patients at peak inflammation.

So the ICV route does not merely relocate inflammation — it elicits a **different myeloid state**
(IFN-responsive/activating) than the IV route (suppressive/DAM-like). Whether the ICV state is
mechanistically responsible for the higher CSF cytokines with lower systemic toxicity is untested.

**Cytokine correlates of toxicity (PMID 39537919)** [GD2-clinical]

- Grade ≥2 **CRS** correlated with higher **plasma MCP-1/CCL2** — a monocyte-recruiting chemokine —
  plus a trend for IL-2.
- Grade ≥2 **TIAN** correlated with higher **CSF MCP-1/CCL2**, IL-10 and TNF-α.
- The authors' own reading: the association of severe TIAN with myeloid-response chemokines "raises the
  prospect that **myeloid cells may contribute to neurological symptoms** induced by CAR T cell therapy
  for CNS tumours, a hypothesis that requires testing in future studies."

That is the current state of the evidence: **correlative and explicitly hypothesis-generating**. No
GD2 CAR-T study has depleted or blocked myeloid recruitment and measured the effect on TIAN.

## Why a myeloid mechanism is plausible

[CART-general] mechanism, transferable because it is antigen-agnostic:

- CRS itself is **macrophage-mediated**: monocyte/macrophage IL-1 and IL-6 drive the syndrome, and
  **IL-1 blockade abates CRS while separating it from neurotoxicity** (Giavridis 2018, PMID 29808005;
  Norelli 2018, PMID 29808007). Monocyte depletion has been explored as a CRS intervention
  (PMID 34570442 review; monocyte-depletion preprint, DOI 10.1101/2020.11.22.20232801).
- In ICANS, **CD14⁺ myeloid cells are found in CSF**, and the proposed cascade is endothelial
  activation → BBB disruption → immunocyte infiltration → astrocyte injury and **microglial
  activation** → neuronal dysfunction (PMID 35871757). Autopsy in CAR-T cerebral oedema showed
  microglial activation, extensive in one case and perivascular in another (cited in PMID 35871757).
- Cytokine-level detail (PMID 33391257): **GM-CSF** secreted by CNS-infiltrating helper T cells
  activates microglia, and GM-CSF neutralisation reduced brain contrast enhancement in a CAR-T
  xenograft; **IFN-γ** drives microglial activation and antigen presentation; **IL-6** induces
  microglial proliferation; **IL-15** induces microglial cytokine production, and increased astrocytic
  IL-15 worsened cerebral oedema in mice — relevant because IL-15-armoured products exist in the GD2
  space (GD2-CAR.15 NKT). Microglia also retain **epigenetic memory** of inflammatory stimuli, a
  proposed substrate for prolonged neurologic sequelae.
- Preclinically in GD2/DMG models, tumour clearance produced **brainstem oedema and obstructive
  hydrocephalus** (PMID 29662203) — the mass-effect endpoint that TIAN type 1 describes.

## Is microglia a *target* or an *amplifier*?

An important distinction for the off-target question: nothing in this corpus shows GD2 CAR T cells
**targeting** microglia. GD2 in normal CNS is described on neurons, astrocytes and peripheral nerve
fibres, not as a microglial marker, and the only demonstrated GD2 CAR-mediated normal-CNS injury is
the high-affinity **E101K** encephalitis, where CAR T cells infiltrated and proliferated in low-GD2
cerebellar and basal brain regions with neuronal destruction (PMID 29180536) — a T-cell-driven lesion,
with myeloid involvement not separately characterised in that report.

Practical framing:

- **Amplifier (evidenced)**: myeloid recruitment and microglial activation downstream of CAR-T
  engagement, correlating with CRS (plasma CCL2) and TIAN (CSF CCL2/TNF/IL-10).
- **Target (no evidence)**: GD2 CAR-T killing microglia.
- **Consequence**: interventions aimed at the myeloid arm — anakinra (IL-1R), tocilizumab/siltuximab
  (IL-6), and in the hyperinflammatory extreme emapalumab (IFN-γ) or ruxolitinib — are the
  mechanistically-matched drugs for TIAN and CRS, whereas corticosteroids act broadly and also blunt
  the CAR. This is exactly the order the GD2 CNS protocols use.

## Open questions this would answer if measured

1. Does blocking **CCL2/CCR2** or GM-CSF (lenzilumab-type) reduce TIAN without reducing antitumour
   effect? Untested in GD2 CAR-T.
2. Do the **DAM/MDSC-like suppressive myeloid states** seen after IV dosing and at late timepoints act
   as a *resistance* mechanism as well as a toxicity mechanism?
3. Does the attenuation of TIAN over successive ICV infusions reflect **myeloid-state adaptation**
   (tolerisation) or simply less tumour left to inflame?
4. Is there measurable **microglial injury** (e.g. sTREM2, GFAP, NfL in CSF) after ICV GD2 CAR-T? No
   GD2 trial reports neuroglial-injury biomarkers, although CSF/serum **GFAP and NfL** track
   neurotoxicity and endothelial dysfunction after CD19 CAR-T (PMID 41553539) and murine NfL has been
   used preclinically (PMID 38551501).
