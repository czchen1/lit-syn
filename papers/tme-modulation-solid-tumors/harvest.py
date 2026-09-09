#!/usr/bin/env python3
"""Harvest tumour-microenvironment (TME) modulation literature for solid tumours and
immunotherapy-resistant tumours from Europe PMC.

Query construction. Broad TME vocabulary ("macrophage", "regulatory T cell", "hypoxia",
"resistance", ...) matches six-figure numbers of records when searched over the whole
abstract, so each theme is expressed as **title-anchored** term lists (`TITLE:"..."`)
conjoined with a cancer-context clause searched over the full record. Highly specific
vocabulary — drug names, programme codes, agent classes that only occur in this field —
is additionally searched over title+abstract, where precision does not depend on the
title. All boolean grouping is generated in Python so that AND/OR precedence is explicit.

Two sweeps per query:

* `modern` — `FIRST_PDATE:[2015-01-01 TO 2026-12-31]`, cursor-paginated to `MAX_PAGES`.
* `foundational` — no date restriction, one page sorted by citation count, so pre-2015
  landmark papers (vascular normalisation, immunoediting, CSF1R, IDO, STING, …) enter the
  corpus even though the modern window would exclude them.

Output: raw_harvest.json (consumed by curate.py) and harvest.log.
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "raw_harvest.json")
LOG = os.path.join(HERE, "harvest.log")

WINDOW = 'FIRST_PDATE:[2015-01-01 TO 2026-12-31] AND (SRC:MED OR SRC:PMC OR SRC:PPR)'
RECENT = 'FIRST_PDATE:[2024-01-01 TO 2026-12-31] AND (SRC:MED OR SRC:PMC OR SRC:PPR)'
NODATE = '(SRC:MED OR SRC:PMC)'


def phrase(term):
    return '"' + term.replace('"', "") + '"'


def concept(term):
    """Title-or-abstract match for one term; 'a & b' requires co-occurrence of both."""
    if " & " in term:
        return "(" + " AND ".join(concept(p.strip()) for p in term.split(" & ")) + ")"
    q = phrase(term)
    return f"(TITLE:{q} OR ABSTRACT:{q})"


def any_of(terms):
    """OR over title/abstract concepts. Europe PMC's default field includes full
    text of OA articles, so every clause is field-restricted to stay specific."""
    return "(" + " OR ".join(concept(t) for t in terms) + ")"


def title_any(terms):
    """OR over titles only."""
    return "(" + " OR ".join(f"TITLE:{phrase(t)}" for t in terms) + ")"


def journal_any(journals):
    return "(" + " OR ".join(f'JOURNAL:"{j}"' for j in journals) + ")"


CANCER = any_of([
    "cancer", "cancers", "tumor", "tumour", "tumors", "tumours", "carcinoma",
    "adenocarcinoma", "melanoma", "glioma", "glioblastoma", "sarcoma", "neoplasm",
    "neuroblastoma", "mesothelioma", "malignancy", "malignancies", "oncology",
])
SOLID = any_of([
    "solid tumor", "solid tumors", "solid tumour", "solid tumours", "carcinoma",
    "adenocarcinoma", "melanoma", "glioma", "glioblastoma", "sarcoma", "neuroblastoma",
    "mesothelioma", "breast cancer", "lung cancer", "non-small cell lung",
    "colorectal cancer", "pancreatic cancer", "pancreatic ductal", "ovarian cancer",
    "gastric cancer", "hepatocellular carcinoma", "renal cell carcinoma",
    "prostate cancer", "head and neck", "bladder cancer", "esophageal cancer",
    "cervical cancer", "endometrial cancer", "cholangiocarcinoma", "brain tumor",
    "brain tumour", "solid malignancy", "solid malignancies", "urothelial",
])
IMMUNO = any_of([
    "immune checkpoint", "immunotherapy", "checkpoint blockade", "checkpoint inhibitor",
    "anti-PD-1", "anti-PD-L1", "PD-1 blockade", "PD-L1", "anti-CTLA-4", "CTLA-4",
    "pembrolizumab", "nivolumab", "atezolizumab", "durvalumab", "ipilimumab",
    "CAR T", "CAR-T", "adoptive cell therapy", "tumor-infiltrating lymphocyte",
    "cancer vaccine", "T-cell engager", "antitumor immunity", "antitumour immunity",
    "anti-tumor immunity", "immune evasion", "immunosuppressive microenvironment",
    "T cell", "T-cell", "immune microenvironment",
])
TME_ANCHOR = any_of([
    "tumor microenvironment", "tumour microenvironment", "microenvironment",
    "immune microenvironment", "stroma", "stromal", "immune infiltrate",
    "immune infiltration", "immunosuppressive", "tumor immunity", "antitumor immunity",
    "antitumour immunity",
])
INVIVO = any_of([
    "mice", "mouse", "murine", "xenograft", "PDX", "syngeneic", "orthotopic", "in vivo",
    "mouse model", "organoid", "tumor-bearing", "tumour-bearing", "humanized mouse",
])
TRIAL = any_of([
    "phase 1", "phase I", "phase 2", "phase II", "phase 3", "phase III", "phase 1/2",
    "phase 1b", "randomized", "randomised", "first-in-human", "clinical trial",
    "single-arm", "open-label", "dose-escalation", "neoadjuvant", "real-world",
    "patients with", "cohort of patients",
])

RESISTANCE_TITLE = title_any([
    "immunotherapy resistance", "resistance to immunotherapy",
    "resistance to immune checkpoint", "checkpoint inhibitor resistance",
    "resistance to checkpoint", "anti-PD-1 resistance", "PD-1 resistance",
    "immune resistance", "immune escape", "immune evasion", "immunoresistance",
    "immunotherapy-resistant", "immunotherapy resistant", "ICI-resistant",
    "resistant to anti-PD-1", "resistant to immune checkpoint", "immunologically cold",
    "cold tumor", "cold tumors", "cold tumour", "cold tumours", "immune-cold",
    "immune desert", "immune-excluded", "immune exclusion", "T cell exclusion",
    "T-cell exclusion", "non-inflamed", "refractory to immunotherapy",
    "primary resistance", "acquired resistance", "hyperprogression",
])

QUERIES = {
    # ------------------------------------------------------------ macrophages / myeloid
    "myeloid_macrophage": [
        f'{title_any(["tumor-associated macrophage", "tumour-associated macrophage", "tumor associated macrophages", "tumor-associated macrophages", "TAMs", "macrophage polarization", "macrophage polarisation", "macrophage reprogramming", "macrophage repolarization", "M2 macrophage", "M2 macrophages", "M1 macrophage", "myeloid cells", "myeloid compartment", "myeloid checkpoint", "myeloid reprogramming", "monocyte", "monocytes", "microglia", "CAR macrophage", "CAR-M", "efferocytosis", "phagocytosis checkpoint"])} AND {CANCER} AND {TME_ANCHOR}',
        f'{any_of(["CSF1R inhibitor", "CSF-1R inhibitor", "anti-CSF1R", "pexidartinib", "emactuzumab", "cabiralizumab", "axatilimab", "anti-CSF-1", "CCR2 antagonist", "CCR2 inhibitor", "CCR5 antagonist", "maraviroc", "plozalizumab", "TREM2 antibody", "anti-TREM2", "PY314", "MARCO antibody", "anti-CD40 agonist", "CD40 agonist", "selicrelumab", "sotigalimab", "mitazalimab", "APX005M", "anti-CD47", "CD47 blockade", "magrolimab", "evorpacept", "ALX148", "lemzoparlimab", "SIRPalpha", "SIRP-alpha", "Siglec-10", "CD24 blockade", "LILRB1", "LILRB2", "ILT4 inhibitor", "MerTK inhibitor", "anti-phosphatidylserine", "bexmarilimab", "Clever-1", "PI3K-gamma inhibitor", "eganelisib", "IPI-549"])} AND {CANCER}',
        f'{title_any(["myeloid-derived suppressor", "myeloid derived suppressor", "MDSC", "MDSCs", "granulocytic MDSC", "monocytic MDSC", "PMN-MDSC", "tumor-associated neutrophil", "tumour-associated neutrophil", "tumor-associated neutrophils", "neutrophil extracellular trap", "neutrophil extracellular traps", "NETosis", "neutrophils", "N2 neutrophil", "mast cell", "eosinophil"])} AND {CANCER} AND {TME_ANCHOR}',
        f'{any_of(["CXCR2 inhibitor", "CXCR1/2 inhibitor", "navarixin", "SX-682", "AZD5069", "anti-IL-8", "BMS-986253", "IL-8 blockade", "S100A9 inhibitor", "tasquinimod", "PDE5 inhibitor & MDSC", "all-trans retinoic acid & MDSC", "MDSC depletion", "targeting & myeloid-derived suppressor"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ suppressive lymphoid cells
    "treg_suppressive_lymphoid": [
        f'{title_any(["regulatory T cell", "regulatory T cells", "Treg", "Tregs", "FOXP3", "Treg depletion", "intratumoral Treg", "tumor-infiltrating Treg", "regulatory B cell", "Bregs", "gamma delta T cells", "innate lymphoid cell", "NK cell dysfunction", "T cell exhaustion", "exhausted T cells", "T-cell exhaustion", "stem-like T cells", "progenitor exhausted", "TCF1", "TOX", "tumor-reactive T cells", "bystander T cells", "tissue-resident memory"])} AND {CANCER} AND {TME_ANCHOR}',
        f'{any_of(["anti-CCR8", "CCR8 antibody", "CCR8-targeting", "BAY 3375968", "LM-108", "S-531011", "GS-1811", "mogamulizumab", "CCR4 antibody", "anti-CD25", "RG6292", "Fc-optimized anti-CTLA-4", "Treg-depleting antibody", "botensilimab", "TNFR2 antibody", "anti-TNFR2", "OX40 agonist", "GITR agonist", "4-1BB agonist", "ICOS agonist"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ CAF / ECM / stroma
    "caf_stroma_ecm": [
        f'{title_any(["cancer-associated fibroblast", "cancer-associated fibroblasts", "cancer associated fibroblasts", "CAFs", "myofibroblast", "fibroblast activation protein", "FAP-targeted", "pancreatic stellate cell", "hepatic stellate cell", "desmoplasia", "desmoplastic", "stromal reprogramming", "stroma-targeting", "extracellular matrix", "matrix stiffness", "collagen", "hyaluronan", "hyaluronic acid", "lysyl oxidase", "LOXL2", "interstitial fluid pressure", "solid stress", "tumor stiffness", "matrix remodeling", "matrix metalloproteinase", "focal adhesion kinase", "integrin"])} AND {CANCER} AND {TME_ANCHOR}',
        f'{any_of(["PEGPH20", "pegvorhyaluronidase", "vismodegib", "sonidegib", "hedgehog inhibitor & stroma", "defactinib", "FAK inhibitor & tumor", "narnatumab", "FAP-CAR", "FAP & CAR T", "simlukafusp", "RO6874281", "anti-FAP", "nintedanib & tumor", "pirfenidone & tumor", "losartan & stroma", "angiotensin & stroma", "collagenase & intratumoral"])} AND {CANCER}',
        f'{any_of(["TGF-beta inhibitor", "TGF-β inhibitor", "TGF-beta blockade", "anti-TGF-beta", "TGF-beta trap", "bintrafusp alfa", "galunisertib", "vactosertib", "SRK-181", "NIS793", "TGF-beta receptor kinase", "TGFbeta signature", "TGF-beta signature", "dominant-negative TGF-beta receptor"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ vasculature / hypoxia
    "vasculature_hypoxia": [
        f'{title_any(["vascular normalization", "vascular normalisation", "vessel normalization", "tumor vasculature", "tumour vasculature", "tumor endothelium", "endothelial anergy", "high endothelial venule", "high endothelial venules", "angiogenesis", "anti-angiogenic", "antiangiogenic", "VEGF", "angiopoietin", "pericyte", "tumor perfusion"])} AND {CANCER} AND {IMMUNO}',
        f'{title_any(["tumor hypoxia", "tumour hypoxia", "hypoxic microenvironment", "hypoxia", "HIF-1alpha", "HIF-1α", "HIF-2alpha", "HIF-2α", "hypoxia-inducible factor", "reoxygenation", "oxygenation", "carbonic anhydrase IX", "hypoxia-activated prodrug"])} AND {CANCER} AND {TME_ANCHOR}',
        f'{any_of(["evofosfamide", "TH-302", "tarloxotinib", "belzutifan", "PT2977", "oxygen-generating nanoparticle", "perfluorocarbon & oxygen & tumor", "hyperbaric oxygen & tumor", "hypoxia-activated", "HIF-2 inhibitor", "ivonescimab", "PD-1/VEGF bispecific", "vanucizumab", "trebananib", "bevacizumab & atezolizumab", "lenvatinib & pembrolizumab", "cabozantinib & nivolumab"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ metabolism
    "metabolic_tme": [
        f'{any_of(["CD73 inhibitor", "anti-CD73", "oleclumab", "quemliclustat", "AB680", "CD39 antibody", "anti-CD39", "TTX-030", "A2A receptor antagonist", "A2AR antagonist", "ciforadenant", "etrumadenant", "inupadenant", "taminadenant", "adenosine axis", "adenosinergic", "adenosine pathway blockade"])} AND {CANCER}',
        f'{any_of(["IDO1 inhibitor", "indoleamine 2,3-dioxygenase inhibitor", "epacadostat", "linrodostat", "navoximod", "IDO/TDO", "TDO2 inhibitor", "kynurenine pathway", "kynureninase", "arginase inhibitor", "numidargistat", "CB-1158", "INCB001158", "arginine deprivation", "pegzilarginase", "glutaminase inhibitor", "telaglenastat", "CB-839", "glutamine antagonist", "JHU083", "sirpiglenastat", "DRP-104", "methionine restriction & tumor", "serine & deprivation & tumor"])} AND {CANCER}',
        f'{title_any(["metabolic reprogramming", "tumor metabolism", "immunometabolism", "lactate", "lactic acid", "acidosis", "tumor acidity", "acidic microenvironment", "glycolysis", "MCT1", "MCT4", "glucose competition", "fatty acid oxidation", "lipid metabolism", "cholesterol metabolism", "OXPHOS", "mitochondrial dysfunction", "nutrient competition", "amino acid metabolism", "nicotinamide", "NAD+"])} AND {CANCER} AND {TME_ANCHOR}',
        f'{any_of(["ketogenic diet & cancer", "fasting-mimicking diet", "caloric restriction & tumor", "high-fiber diet & immunotherapy", "obesity & immunotherapy", "exercise & tumor microenvironment", "metformin & immunotherapy", "statin & immunotherapy", "beta-blocker & immunotherapy", "propranolol & immunotherapy", "chronic stress & antitumor immunity", "circadian & immunotherapy"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ innate sensing agonists
    "innate_agonists": [
        f'{any_of(["STING agonist", "STING agonists", "cGAS-STING", "cGAS/STING", "STING activation", "ADU-S100", "MK-1454", "E7766", "exoSTING", "SNX281", "TAK-676", "non-nucleotide STING", "TLR agonist", "TLR7 agonist", "TLR7/8 agonist", "TLR9 agonist", "TLR3 agonist", "poly(I:C)", "poly-ICLC", "imiquimod", "resiquimod", "CpG oligodeoxynucleotide", "vidutolimod", "CMP-001", "tilsotolimod", "lefitolimod", "BO-112", "RIG-I agonist", "MDA5 agonist", "AIM2 inflammasome & tumor", "type I interferon & tumor microenvironment", "STAT6 antagonist", "stimulator of interferon genes"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ engineered cytokines
    "cytokine_engineering": [
        f'{any_of(["IL-12 & tumor", "interleukin-12 & tumor", "IL-2 variant", "IL-2 mutein", "not-alpha IL-2", "engineered IL-2", "bempegaldesleukin", "nemvaleukin", "PD1-IL2v", "IL-15 superagonist", "N-803", "nogapendekin", "decoy-resistant IL-18", "IL-18 & antitumor", "IL-21 & antitumor", "IL-10 & antitumor", "pegilodecakin", "efineptakin", "immunocytokine", "antibody-cytokine fusion", "cytokine prodrug", "masked cytokine", "tumor-targeted cytokine", "L19-IL2", "collagen-anchored cytokine", "intratumoral IL-12", "cytokine armoring", "anti-IL-6 & immunotherapy", "tocilizumab & immunotherapy", "canakinumab", "IL-1beta blockade", "LIF blockade", "anti-LIF"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ trafficking / TLS
    "trafficking_tls": [
        f'{title_any(["tertiary lymphoid structure", "tertiary lymphoid structures", "lymphoid neogenesis", "T cell infiltration", "T-cell infiltration", "immune cell infiltration", "lymphocyte infiltration", "T cell trafficking", "T-cell trafficking", "lymphocyte homing", "chemokine", "chemokines", "CXCL9", "CXCL10", "CXCL13", "CCL5", "CCL21", "CXCR3", "CXCR4", "CXCL12", "immune contexture"])} AND {CANCER} AND {TME_ANCHOR}',
        f'{any_of(["CXCR4 antagonist", "plerixafor", "motixafortide", "balixafortide", "BL-8040", "olaptesed", "NOX-A12", "CXCL12 blockade", "LIGHT & vascular & tumor", "TNFSF14 & tumor", "TLS induction", "induction of tertiary lymphoid"])} AND {CANCER}',
    ],
    # ------------------------------------------------------- antigen presentation / IFN resistance
    "antigen_presentation_ifn": [
        f'{title_any(["antigen presentation", "MHC class I", "MHC-I", "HLA loss", "beta-2 microglobulin", "B2M", "antigen presentation machinery", "TAP1", "NLRC5", "JAK1", "JAK2", "interferon-gamma signaling", "IFN-gamma signaling", "interferon signaling", "immunoediting", "antigen loss", "neoantigen", "neoantigens", "WNT/beta-catenin", "beta-catenin", "PTEN loss", "STK11", "LKB1", "KEAP1", "SERPINB9", "epigenetic silencing"])} AND {CANCER} AND {IMMUNO}',
    ],
    # ------------------------------------------------------------ clinical / translational resistance
    "clinical_resistance": [
        f'{RESISTANCE_TITLE} AND {CANCER} AND {SOLID}',
        f'{RESISTANCE_TITLE} AND {CANCER} AND {TRIAL}',
        f'{RESISTANCE_TITLE} AND {CANCER} AND {INVIVO}',
        f'{any_of(["overcoming resistance to immunotherapy", "reversing immunotherapy resistance", "resensitize to immunotherapy", "resensitizing & immunotherapy", "restore response to checkpoint", "salvage & after immunotherapy", "progression on immunotherapy", "checkpoint inhibitor rechallenge", "immunotherapy rechallenge", "secondary resistance & checkpoint"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ epigenetic priming
    "epigenetic_priming": [
        f'{any_of(["epigenetic therapy & immunotherapy", "DNMT inhibitor & immunotherapy", "azacitidine & immunotherapy", "decitabine & immunotherapy", "guadecitabine", "HDAC inhibitor & immunotherapy", "entinostat", "domatinostat", "mocetinostat", "EZH2 inhibitor & immunotherapy", "tazemetostat & immune", "LSD1 inhibitor & immune", "BET inhibitor & immune", "SETDB1", "KDM5 inhibitor", "viral mimicry", "endogenous retrovirus & tumor", "ERV activation", "epigenetic priming", "epigenetic reprogramming & tumor microenvironment"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ radiation / chemotherapy priming
    "radiation_chemo_priming": [
        f'{any_of(["abscopal", "radiotherapy & immune checkpoint", "radiation & checkpoint blockade", "stereotactic body radiotherapy & immunotherapy", "SBRT & immunotherapy", "low-dose radiotherapy & immune", "FLASH radiotherapy & immune", "radiation-induced immunogenic", "in situ vaccine & radiation", "immunogenic cell death", "chemotherapy-induced immunogenic", "metronomic chemotherapy & immune", "cyclophosphamide & Treg", "gemcitabine & MDSC", "oxaliplatin & immunogenic", "chemoimmunotherapy & microenvironment"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ intratumoral / oncolytic
    "intratumoral_oncolytic": [
        f'{any_of(["intratumoral immunotherapy", "intratumoural immunotherapy", "intratumoral injection", "intratumoral administration", "in situ vaccination", "oncolytic virus", "oncolytic virotherapy", "talimogene laherparepvec", "T-VEC", "RP1 oncolytic", "vusolimogene", "oncolytic adenovirus", "oncolytic herpes", "oncolytic vaccinia", "engineered bacteria & tumor", "bacterial cancer therapy", "Salmonella typhimurium & tumor", "Clostridium novyi", "attenuated Listeria & cancer"])} AND {CANCER} AND {TME_ANCHOR}',
    ],
    # ------------------------------------------------------------ microbiome
    "microbiome": [
        f'{any_of(["gut microbiome & immunotherapy", "gut microbiota & immunotherapy", "fecal microbiota transplantation & cancer", "faecal microbiota transplantation & cancer", "Akkermansia muciniphila & tumor", "live biotherapeutic & cancer", "CBM588", "MRx0518", "probiotic & immunotherapy", "intratumoral bacteria", "intratumour bacteria", "tumor microbiome", "tumour microbiome", "microbial metabolite & antitumor", "short-chain fatty acid & immunotherapy", "antibiotics & immune checkpoint", "microbiome & response to immunotherapy"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ TME-directed delivery
    "tme_directed_delivery": [
        f'{any_of(["tumor microenvironment-responsive", "TME-responsive", "microenvironment-responsive nanoparticle", "pH-responsive & nanoparticle & tumor", "ROS-responsive nanoparticle", "enzyme-responsive nanoparticle", "MMP-responsive", "protease-activated antibody", "masked antibody", "conditionally active biologic", "probody", "logic-gated & tumor microenvironment", "nanoparticle & macrophage repolarization", "nanoparticle & STING agonist", "nanoparticle & immunogenic cell death", "nanoparticle & remodeling the tumor microenvironment", "injectable hydrogel & immunotherapy", "intratumoral hydrogel", "lipid nanoparticle & tumor microenvironment", "in situ CAR", "ferroptosis & antitumor immunity", "pyroptosis & antitumor immunity", "cuproptosis & immune"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ cell therapy vs. the TME
    "cell_therapy_tme": [
        f'{title_any(["CAR T", "CAR-T", "chimeric antigen receptor", "CAR NK", "CAR-NK", "TCR-T", "TCR-engineered", "tumor-infiltrating lymphocyte", "TIL therapy", "adoptive cell therapy", "armored CAR", "armoured CAR"])} AND {CANCER} AND {TME_ANCHOR}',
        f'{any_of(["armored CAR", "armoured CAR", "CAR T & tumor microenvironment", "dominant-negative TGF-beta receptor", "switch receptor & CAR", "IL-18 & CAR T", "IL-12 & CAR T", "hypoxia-inducible CAR", "chemokine receptor & CAR T", "CCR2b", "CXCR2 & CAR T", "CAR T & exhaustion & solid tumor", "CAR macrophage & solid tumor", "TIL therapy & tumor microenvironment"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ physical modulation
    "physical_modulation": [
        f'{any_of(["focused ultrasound & immune", "histotripsy", "high-intensity focused ultrasound & immune", "microbubble & immunotherapy", "sonodynamic therapy & immune", "photodynamic therapy & antitumor immunity", "photothermal & immunotherapy", "photoimmunotherapy", "hyperthermia & immunotherapy", "cryoablation & immune", "radiofrequency ablation & immune", "irreversible electroporation & immune", "tumor treating fields & immune", "pressure-enabled drug delivery", "convection-enhanced delivery", "blood-brain barrier opening", "blood-tumor barrier"])} AND {CANCER}',
    ],
    # ------------------------------------------------------------ spatial / single-cell profiling
    "spatial_profiling": [
        f'{any_of(["single-cell RNA sequencing & tumor microenvironment", "scRNA-seq & tumor microenvironment", "spatial transcriptomics & tumor", "imaging mass cytometry & tumor", "multiplex immunofluorescence & tumor", "CODEX & tumor microenvironment", "spatial proteomics & tumor", "single-cell atlas & tumor", "spatial multi-omics & tumor", "immune atlas & tumor"])} AND {CANCER} AND {IMMUNO}',
    ],
    # ------------------------------------------------------------ disease-specific cold tumours
    "cold_tumor_pdac_gi": [
        f'{title_any(["pancreatic ductal adenocarcinoma", "pancreatic cancer", "microsatellite stable", "mismatch repair proficient", "MSS colorectal", "colorectal cancer", "hepatocellular carcinoma", "biliary tract cancer", "cholangiocarcinoma", "gastric cancer", "peritoneal metastasis", "esophageal cancer"])} AND {TME_ANCHOR} AND {IMMUNO} AND {CANCER}',
    ],
    "cold_tumor_cns": [
        f'{title_any(["glioblastoma", "glioma", "diffuse midline glioma", "brain metastases", "brain metastasis", "medulloblastoma", "CNS tumor", "meningioma", "leptomeningeal"])} AND {TME_ANCHOR} AND {IMMUNO} AND {CANCER}',
    ],
    "cold_tumor_other": [
        f'{title_any(["triple-negative breast cancer", "breast cancer", "prostate cancer", "castration-resistant prostate", "ovarian cancer", "uveal melanoma", "sarcoma", "osteosarcoma", "neuroblastoma", "mesothelioma", "thyroid cancer", "adenoid cystic carcinoma", "salivary gland carcinoma", "renal cell carcinoma", "bladder cancer", "head and neck squamous"])} AND {TME_ANCHOR} AND {IMMUNO} AND {CANCER}',
    ],
    # ------------------------------------------------------------ cross-cutting / general
    "general_tme_modulation": [
        f'{any_of(["tumor microenvironment modulation", "tumour microenvironment modulation", "modulating the tumor microenvironment", "remodeling the tumor microenvironment", "remodelling the tumour microenvironment", "reprogramming the tumor microenvironment", "reshaping the tumor microenvironment", "TME modulation", "turning cold tumors hot", "cold-to-hot", "converting cold tumors", "cold to hot tumor", "immunologically cold tumors", "normalize the tumor microenvironment", "microenvironment-targeted therapy", "stroma-targeted therapy"])} AND {CANCER}',
        f'{title_any(["tumor microenvironment", "tumour microenvironment", "immune microenvironment", "tumor immune microenvironment"])} AND {SOLID} AND {IMMUNO} AND {any_of(["therapy", "therapeutic", "treatment", "targeting", "combination", "inhibitor", "antibody", "overcome", "reverse", "modulate", "remodel", "reprogram"])}',
    ],
    # ------------------------------------------------------------ high-impact venue sweep
    "sweep_high_impact": [
        f'{journal_any(["Nature", "Science", "Cell", "Cancer Cell", "Nat Med", "Nat Cancer", "Immunity", "Nat Immunol", "Cancer Discov", "Sci Transl Med", "J Clin Invest", "J Exp Med", "Cancer Immunol Res", "J Immunother Cancer", "Clin Cancer Res", "Cancer Res", "Nat Rev Cancer", "Nat Rev Clin Oncol", "Nat Rev Immunol", "Cell Rep Med", "Sci Immunol", "Ann Oncol", "Lancet Oncol", "J Clin Oncol", "N Engl J Med", "Neuro Oncol", "Signal Transduct Target Ther", "Mol Cancer", "Cell Metab", "Nat Biotechnol", "Nat Nanotechnol"])} AND {title_any(["tumor microenvironment", "tumour microenvironment", "immune microenvironment", "macrophage", "macrophages", "fibroblast", "fibroblasts", "regulatory T", "myeloid", "immune evasion", "immunotherapy resistance", "resistance to immunotherapy", "checkpoint blockade", "immunotherapy", "antitumor immunity", "T cell exhaustion", "stroma", "hypoxia", "immune exclusion"])} AND {CANCER}',
    ],
}

# Every axis query matches thousands of records, so each sweep takes a
# citation-ranked slice instead of the whole hit list.
PAGE = 100
SWEEPS = [
    ("modern", WINDOW, 3),        # 2015-2026, most-cited
    ("recent", RECENT, 2),        # 2024-2026, most-cited (offsets citation lag)
    ("foundational", NODATE, 1),  # all years, most-cited landmarks
]


def request_json(url):
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "lit-syn/1.0"})
            with urllib.request.urlopen(req, timeout=180) as resp:
                return json.load(resp)
        except Exception as exc:
            sys.stderr.write(f"  retry {attempt}: {exc}\n")
            time.sleep(4 + 4 * attempt)
    return None


def epmc_top_cited(query, pages):
    """Most-cited records first. Europe PMC ignores `page` alongside `sort`, so
    paging has to go through cursorMark."""
    out, hits, cursor = [], 0, "*"
    for _ in range(pages):
        params = urllib.parse.urlencode({
            "query": query, "format": "json", "pageSize": PAGE,
            "resultType": "core", "sort": "CITED desc", "cursorMark": cursor,
        })
        data = request_json(f"{EPMC}?{params}")
        if data is None:
            break
        hits = hits or data.get("hitCount", 0)
        results = data.get("resultList", {}).get("result", [])
        out.extend(results)
        nxt = data.get("nextCursorMark")
        if len(results) < PAGE or not nxt or nxt == cursor:
            break
        cursor = nxt
        time.sleep(0.34)
    return out, hits


def clean(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text)).strip()


def venue_of(rec):
    ji = rec.get("journalInfo", {}) or {}
    return (ji.get("journal", {}).get("title", "")
            or ji.get("journal", {}).get("medlineAbbreviation", "")
            or rec.get("journalTitle", "")
            or (rec.get("bookOrReportDetails", {}) or {}).get("publisher", ""))


def ingest(seen, results, domain, sweep):
    new = 0
    for rec in results:
        key = rec.get("pmid") or rec.get("doi") or rec.get("id")
        if not key:
            continue
        if key in seen:
            seen[key]["also_domains"].add(domain)
            continue
        new += 1
        seen[key] = {
            "domain": domain,
            "also_domains": set(),
            "sweep": sweep,
            "pmid": rec.get("pmid", ""),
            "pmcid": rec.get("pmcid", ""),
            "doi": rec.get("doi", ""),
            "title": clean(rec.get("title", "")).rstrip("."),
            "abstract": clean(rec.get("abstractText", "")),
            "authors": rec.get("authorString", ""),
            "venue": venue_of(rec),
            "year": rec.get("pubYear", ""),
            "date": rec.get("firstPublicationDate", ""),
            "isOA": rec.get("isOpenAccess", "N"),
            "inEPMC": rec.get("inEPMC", "N"),
            "cited": rec.get("citedByCount", 0),
            "pubType": (rec.get("pubTypeList", {}) or {}).get("pubType", []),
            "src": rec.get("source", ""),
        }
    return new


def main():
    seen = {}
    log = open(LOG, "a")
    for domain, queries in QUERIES.items():
        for i, q in enumerate(queries):
            for sweep, scope, pages in SWEEPS:
                results, hits = epmc_top_cited(f"({q}) AND {scope}", pages)
                new = ingest(seen, results, domain, sweep)
                msg = (f"{sweep:12s} {domain}[{i}]: hits={hits} "
                       f"fetched={len(results)} new={new} total={len(seen)}\n")
                sys.stderr.write(msg)
                log.write(msg)
                log.flush()
                time.sleep(0.34)

    out = []
    for v in seen.values():
        v["also_domains"] = "|".join(sorted(v["also_domains"]))
        v["pubType"] = "|".join(v["pubType"]) if isinstance(v["pubType"], list) else str(v["pubType"])
        out.append(v)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=0)
    print(f"total unique records: {len(out)}")
    log.write(f"total unique records: {len(out)}\n")
    log.close()


if __name__ == "__main__":
    main()
