# Surgical access, imaging guidance, dosimetry and modelling

Delivery to the pons is executed by a trajectory. This note collects the literature that
determines whether a catheter, needle or acoustic focus can be placed where the drug is
needed, and whether the resulting distribution can be measured.

## Biopsy as the enabling procedure

Molecular diagnosis (H3K27M/H3K27-altered status) made brainstem biopsy routine, and the
same trajectory logic now supports therapeutic infusion.

- Role: Sheikh 2024 (PMID 39763605) on brainstem biopsy and targeted therapy in
  DMG/DIPG; Samadani 2003 (PMID 14742957) for the broader diagnostic indication.
- Safety and yield: Dalmage 2023 (PMID 37724839) on survival and neurological outcomes
  after DIPG stereotactic biopsy; Dawes 2019 (PMID 30523502) prospective robot-assisted
  brainstem biopsy in children; Junior 2026 on microsurgical biopsy through safe entry
  zones; transfrontal transventricular and extraventricular trajectory descriptions
  (Pereira 2008, PMID 18686061; Amundson 2005, PMID 15796398).
- Biopsy also has a differential-diagnosis function that protects against delivering
  cytotoxics into a non-neoplastic pontine mass (inflammatory and demyelinating lesions
  can mimic DIPG radiologically).

## Trajectories, safe entry zones and neuronavigation

- Safe entry zones are the best-characterised part of pontine access: high-resolution
  diffusion-tensor mapping (Mukherjee 2020, PMID 30136133), microsurgical and morphometric
  atlases (Cavalcanti 2016, PMID 26452114; Yagmurlu 2014, PMID 24983443;
  ultrahigh-resolution 7T anatomy in Hanalioglu 2024, PMID 39664682; Guberinic 2022,
  PMID 35395628; Serrato-Avila 2022, PMID 34715371), virtual/3-D exploration
  (Tayebi Meybodi 2020, PMID 32474103) and outcome comparisons between zones
  (Catapano 2023, PMID 36681989).
- Approach selection for lateral/central pons — trans-middle cerebellar peduncle
  (Graffeo 2024, PMID 37976511), lateral pontine zone (Cavalcanti 2020, PMID 32442280),
  peritrigeminal presigmoid retrolabyrinthine (Hoz 2023, PMID 37578224), endoscopic
  endonasal transclival (Weiss 2019, PMID 29750275) — comes largely from the cavernous
  malformation literature but defines the corridors available to a catheter.
- Neuronavigation in brainstem glioma surgery (Zhang 2023, PMID 37205194) shows the
  practical toolchain; FUS is now neuronavigation-guided as well (Wu 2025,
  PMID 41223245).

## Seeing the delivered agent

- **CED**: MR-visible surrogates — gadoteridol-loaded liposomes visualised in real time in
  the monkey brain including brainstem (Krauze 2005, PMID 16181805; Saito 2005,
  PMID 16197944) — plus DIPG-specific imaging protocols for assessing infusate
  distribution and tumour coverage (DIPG-18 2022 abstract, Szychot/GOSH programme).
- **Radiolabelled agents**: ¹²⁴I-8H9 theragnostic CED (Luther 2014, PMID 24526309) and
  ¹⁸F-panobinostat PET (Kommidi 2018, PMID 29456798) allow dosimetry rather than
  assumption.
- **Cells**: dual-modality longitudinal biodistribution imaging of ICV CAR-T
  (Li 2026, PMID 42068336).
- **CSF routes**: phase-contrast CSF flow MRI to confirm pathway patency before intra-CSF
  therapy (Patel 2018, PMID 29170836) and human CSF tracer distribution in brainstem and
  upper cord (Melin 2023, PMID 38063195).

## Modelling and dosimetry

- Infusate-parameter studies (Rechberger 2020, PMID 31896090) and mannitol/CED
  interaction (Sandberg 2002, PMID 12187954) are effectively experimental versions of the
  transport model.
- Deformation measurement after pontine CED (Bander 2020, PMID 31896089) provides the
  mechanical constraint that any patient-specific simulation must reproduce.
- Radiotherapy-side dosimetry appears where it interacts with delivery: FUS plus
  hypofractionated RT (Tazhibi 2024, PMID 38555449), brachytherapy-style permanent
  implants (GammaTile dosimetry, Zhang 2024), and radiation-volume implications of
  extrapontine progression (DIPG-52 2023 abstract).

## Gap

Patient-specific, prospectively validated pontine infusion planning (tract-aware,
deformation-aware, with measured Vd/Vi and reflux) is not established in this
literature: modelling records are the smallest category in the index, and most
distribution knowledge is empirical and centre-specific.
