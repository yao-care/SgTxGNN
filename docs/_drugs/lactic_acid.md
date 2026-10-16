---
layout: default
title: Lactic Acid
parent: Low Evidence (L5)
nav_order: 573
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lactic Acid: predicted new indication Atypical coarctation of aorta (evidence level L5). Approved use: Not stated in the approved indication text of the Singapore licences"
monitor_inn: "Lactic acid"
predicted_indications: ["atypical coarctation of aorta", "aortic malformation", "non-syndromic esophageal malformation", "amenorrhea (disease)", "dry eye syndrome", "esophageal disease", "double outlet right ventricle with atrioventricular septal defect, pulmonary stenosis, heterotaxy", "excretory apparatus of the lacrimal system anomaly", "eye disease", "cauda equina syndrome"]
---

# Lactic Acid
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

# Lactic Acid: From an Endogenous Metabolite and Topical/Infusion Agent to Atypical Coarctation of Aorta

## One-Sentence Summary

Lactic acid is an endogenous metabolite used in Singapore in topical products and as part of an intravenous infusion (compound sodium lactate).
The TxGNN model predicts it may be effective for **atypical coarctation of aorta**, but this is a network-based prediction only, with **0 clinical trials** and **0 publications** for this indication.
Of the 10 predicted indications, none has direct therapeutic evidence, so this is a weak repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the approved indication text of the Singapore licences |
| Predicted New Indication | Atypical coarctation of aorta |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Lactic acid is an endogenous metabolite (the end product of glycolysis) and is used as a topical and pH-adjusting agent. It also appears as lactate in intravenous fluid.

For atypical coarctation of aorta, no mechanistic link was identified. This is a structural developmental anomaly of the aorta, and lactic acid has no known role in aortic development or in treating vascular malformations. The high TxGNN score (99.59%) reflects network proximity in the knowledge graph rather than biological or clinical rationale.

The other top-ranked predictions were also reviewed, and none shows therapeutic support:

- **Aortic malformation:** The 14 retrieved papers concern congenital heart surgery, biodegradable devices made of poly-lactic acid, and perioperative monitoring. None tests lactic acid as a treatment.
- **Dry eye syndrome (L4):** The evidence concerns lactic acid bacteria (probiotics) in mouse models and metabolomic biomarkers, not lactic acid itself.
- **Esophageal disease and eye disease:** The literature includes adverse signals. Indole-3-lactic acid suppressed anti-PD-1 efficacy in esophageal squamous cell carcinoma, and lactic acid upregulated VEGF and promoted choroidal neovascularization in preclinical work.
- **Amenorrhea:** The only paper is a baboon vaginal microbiota study, which is not a treatment link.
- **Non-syndromic esophageal malformation, complex double outlet right ventricle, lacrimal excretory anomaly and cauda equina syndrome:** Prediction only, with no mechanistic rationale, trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was retrieved for atypical coarctation of aorta. The closest related set, for aortic malformation (rank 2), contained no study of lactic acid as a therapy. The most relevant items are listed below for context only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3367436](https://pubmed.ncbi.nlm.nih.gov/3367436/) | 1988 | Preclinical/Animal | Journal of Vascular Surgery | Aortic wall respiration and glycolysis above and below an experimental coarctation in rabbits on standard or atherogenic diets; a metabolic study, not a lactic acid treatment |
| [25157439](https://pubmed.ncbi.nlm.nih.gov/25157439/) | 2015 | Preclinical/Animal | Catheterization and Cardiovascular Interventions | Biodegradable poly-l-lactic acid stent in rabbit descending aorta; a device material, not a drug effect |
| [32382764](https://pubmed.ncbi.nlm.nih.gov/32382764/) | 2020 | Case report | Pediatric Cardiology | Absorbable poly-l-lactic acid microplates for bronchomalacia in infants with congenital heart disease; device material |
| [23791497](https://pubmed.ncbi.nlm.nih.gov/23791497/) | 2013 | RCT | Journal of Cardiothoracic and Vascular Anesthesia | Combined ultrafiltration strategy in pediatric cardiac surgery; unrelated to lactic acid |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04047P | DUOFILM COLLODION | Tincture | Not stated |
| SIN04987P | SATO UONOME SOLUTION | Solution | Not stated |
| SIN06281P | COMPOUND SODIUM LACTATE INTRAVENOUS INFUSION BP | Injection | Not stated |

---

## Safety Considerations

- **Drug Interactions:** 17 interactions were identified (DDInter source). None is rated major.
  - *Moderate (10):* doxycycline, tetracycline, minocycline, demeclocycline, oxytetracycline, acetylsalicylic acid, sodium salicylate, ephedrine (including nasal), pseudoephedrine.
  - *Minor (7):* chlorpropamide, tolazamide, glipizide, glyburide, acetohexamide, tolbutamide, methotrexate.
- **Signals from the literature (preclinical or case-level, not label data):** lactic acid-related signalling has been linked to promotion of choroidal neovascularization and immunosuppression in the tumour microenvironment. A case of ectropion followed over-the-counter acid treatment of xanthelasma. These argue for caution in the eye and oesophagus indications.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no trials, no literature on lactic acid in this condition, and no plausible mechanism for a structural aortic anomaly. None of the other nine predicted indications has therapeutic evidence either, and some show potential harm signals.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (this gap blocks safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the three Singapore licences, to establish the original indication
- A plausible pharmacological rationale for the predicted indication, and preclinical evidence supporting it
- Route compatibility assessment, since the available forms (topical and intravenous) have not been matched to what the condition would require
- If any indication is pursued, dry eye is the only one with some (indirect) evidence at L4, and it would first need direct tests of lactic acid itself rather than probiotics
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

