---
layout: default
title: Iopamidol
parent: Low Evidence (L5)
nav_order: 543
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Iopamidol: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not stated in the Singapore licence records (iopamidol is known as an…"
---

# Iopamidol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Iopamidol: From Diagnostic Contrast Imaging to Prinzmetal Angina

## One-Sentence Summary

Iopamidol is an iodinated, non-ionic X-ray contrast agent used as a diagnostic imaging aid, not as a treatment.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (iopamidol is known as an iodinated contrast agent for diagnostic imaging) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 98.57% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Iopamidol is a non-ionic iodinated contrast medium. It absorbs X-rays and makes blood vessels and tissues visible on imaging. It has no known vasodilatory or anti-vasospastic pharmacology.

Prinzmetal angina is caused by coronary artery spasm, so a treatment would need to relax or prevent vascular spasm. No such mechanistic link has been identified for iopamidol. The only connection is diagnostic: contrast media are used in coronary angiography, including provocation testing. That is not a therapeutic use.

The high TxGNN score therefore reflects a pattern in the knowledge graph and is not supported by pharmacological or clinical evidence.

Other predicted indications were also reviewed. None has trial evidence or supports a therapeutic role:
- **Female breast carcinoma** (score 97.91%): the literature covers only imaging uses, such as CT lymphography for sentinel lymph node mapping and acidoCEST MRI for tumour pH and perfusion.
- **Pulmonary hypertension** (score 96.16%): the literature covers diagnostic pulmonary angiography and its haemodynamic safety, not treatment.
- **Migraine, myositis, fibromyalgia, tendinitis and hemoglobinopathy**: there is no therapeutic evidence. The only publications are a tendon-graft imaging study and an in vitro sickling safety study.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for Prinzmetal angina. The closest literature relates to other predicted indications and is diagnostic or safety-related only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14699178](https://pubmed.ncbi.nlm.nih.gov/14699178/) | 2004 | Cohort (preliminary diagnostic) | Radiology | Breast sentinel lymph node mapping by CT lymphography with small volumes of iopamidol (breast carcinoma) |
| [15905719](https://pubmed.ncbi.nlm.nih.gov/15905719/) | 2005 | Cohort (diagnostic) | Investigative Radiology | 3D multidetector CT lymphography with interstitial iopamidol to navigate breast sentinel node biopsy |
| [14976475](https://pubmed.ncbi.nlm.nih.gov/14976475/) | 2004 | Cohort (diagnostic) | Surgery | Sentinel lymph node biopsy using CT lymphography in breast cancer patients |
| [8539407](https://pubmed.ncbi.nlm.nih.gov/8539407/) | 1996 | Cohort | Radiology | Complications of pulmonary angiography with iopamidol in 1,434 patients (pulmonary hypertension) |
| [3659354](https://pubmed.ncbi.nlm.nih.gov/3659354/) | 1987 | Clinical study | Radiology | Iopamidol in pulmonary angiography: patient comfort, image quality and haemodynamics |
| [3436330](https://pubmed.ncbi.nlm.nih.gov/3436330/) | 1987 | Clinical study | European Heart Journal | Haemodynamic side effects of ionic vs non-ionic contrast media in pulmonary hypertension |
| [3788260](https://pubmed.ncbi.nlm.nih.gov/3788260/) | 1986 | Clinical study | Zeitschrift fur Kardiologie | Haemodynamic effects of iopamidol vs amidotrizoate in valvular disease with pulmonary hypertension |
| [7089282](https://pubmed.ncbi.nlm.nih.gov/7089282/) | 1982 | In vitro | Radiology | Iopamidol caused less sickling than an ionic agent, relevant to contrast safety in sickle cell disease (hemoglobinopathy) |
| [26108564](https://pubmed.ncbi.nlm.nih.gov/26108564/) | 2015 | Preclinical | Contrast Media & Molecular Imaging | Iopromide and iopamidol compared as acidoCEST MRI agents for tumour extracellular pH |
| [9442336](https://pubmed.ncbi.nlm.nih.gov/9442336/) | 1997 | Diagnostic imaging | Arthroscopy | Iopamidol used to visualise patellar tendon grafts (tendinitis); not therapeutic |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05906P | IOPAMIRO 300 INJECTION 6.12 g/10 ml | Injection | Not stated in the licence record |
| SIN05907P | IOPAMIRO 370 INJECTION 7.55 g/10 ml | Injection | Not stated in the licence record |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interactions. The 20 reviewed were all rated Major, and a few of them are listed below as examples. They include:
  - Metformin
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone)
  - Amphotericin B (including lipid, liposomal and cholesteryl sulfate formulations)
  - Vancomycin
  - Mesalazine and balsalazide
  - Morphine
  - Bupropion
  - Sympathomimetic and appetite-suppressant agents (ephedrine, phentermine, diethylpropion, fenfluramine, dexfenfluramine)
  - Dronabinol
- **Population-specific haemodynamic data**: In pulmonary hypertension, published studies describe the haemodynamic effects of iopamidol. These are relevant to guardrails if it is used in that population.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. There are no clinical trials, no therapeutic literature and no plausible mechanism linking a diagnostic contrast agent to coronary vasospasm. Across all ten predicted indications, the literature describes diagnostic or safety uses of iopamidol, not treatment.

**To proceed, the following is needed:**
- Mechanism of action data, and a credible pharmacological rationale for an anti-vasospastic or other therapeutic effect
- Package insert warnings and contraindications from the Singapore regulator, since the safety review is incomplete without them
- Approved indication text for the two Singapore licences
- Any preclinical or clinical data suggesting a therapeutic effect in the predicted conditions
- Reconsideration of whether a diagnostic agent suits therapeutic repurposing at all, or whether the finding is better treated as a diagnostic-use question (for example, provocation testing during coronary angiography)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

