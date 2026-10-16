---
layout: default
title: Iron Sucrose
parent: Low Evidence (L5)
nav_order: 550
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Iron Sucrose: predicted new indication Primary hyperoxaluria (evidence level L5). Approved use: Hyperphosphatemia"
---

# Iron Sucrose
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

# Iron Sucrose: From Hyperphosphatemia to Primary Hyperoxaluria

## One-Sentence Summary

Iron sucrose is an intravenous iron preparation. In the knowledge graph used for this prediction, its original indication is listed as hyperphosphatemia.
The TxGNN model ranks **primary hyperoxaluria** as its top predicted new indication, but there are **0 clinical trials** and **0 publications** for this indication, so the prediction is purely computational.
The data compiled for this report show more supporting evidence for hyperparathyroidism (indirect data from CKD and dialysis populations) than for the top-ranked prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperphosphatemia (from the knowledge graph; the Singapore licence record contains no approved indication text) |
| Predicted New Indication | Primary hyperoxaluria |
| TxGNN Prediction Score | 98.82% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, iron sucrose is an intravenous iron replacement product, and its established role is in iron-deficiency anaemia, particularly in patients with chronic kidney disease. The knowledge graph links it to hyperphosphatemia, but that link is not explained by the available data.

For the top prediction, **primary hyperoxaluria**, no plausible mechanism is evident. This is a genetic disorder of hepatic glyoxylate metabolism, and nothing in the data connects intravenous iron to oxalate metabolism. The high score of 0.988 is a model output only.

Among the other predictions, **hyperparathyroidism** has the most relevant indirect support. Studies in CKD and dialysis populations compared iron sucrose with other iron or phosphate-binding agents, including a rat CKD-MBD study of ferric citrate versus intravenous iron sucrose. However, secondary hyperparathyroidism is a co-morbidity in these studies and not a primary endpoint. It remains unclear whether iron sucrose itself alters PTH, and the effect may be confounded by phosphate binding with ferric citrate.

For **pancreatitis** (rank 2), the only related preclinical finding is that intravenous iron preparations cause pancreatic beta-cell toxicity, which points toward potential harm rather than benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was found for the top-ranked prediction (primary hyperoxaluria). The table below lists the publications compiled for the two predictions that had any, which are indirect at best.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28372549](https://pubmed.ncbi.nlm.nih.gov/28372549/) | 2017 | RCT (protocol/rationale) | BMC Nephrology | FACT trial background: ferumoxytol vs iron sucrose in haemodialysis patients with CKD anaemia; not about pancreatitis |
| [34629085](https://pubmed.ncbi.nlm.nih.gov/34629085/) | 2021 | RCT (protocol) | Trials | Oral polysaccharide iron complex vs iron sucrose in haemodialysis patients (IHOPE); anaemia focus |
| [35482713](https://pubmed.ncbi.nlm.nih.gov/35482713/) | 2022 | RCT (secondary mineral-bone endpoints) | Nephrol Dial Transplant | Ferric citrate vs intravenous iron sucrose on mineral, bone and iron markers in a rat CKD-MBD model |
| [32444112](https://pubmed.ncbi.nlm.nih.gov/32444112/) | 2020 | Review | Molecular Aspects of Medicine | Overview of intravenous iron therapy; modern formulations are generally safe for treating iron deficiency |
| [11929146](https://pubmed.ncbi.nlm.nih.gov/11929146/) | 2002 | Clinical study | Perit Dial Int | Low-dose intravenous iron sucrose regimen in peritoneal dialysis patients |
| [24349622](https://pubmed.ncbi.nlm.nih.gov/24349622/) | 2013 | Preclinical (in vitro) | Am J Transl Res | At pharmacologically relevant concentrations, intravenous iron preparations caused pancreatic beta-cell death |
| [17543848](https://pubmed.ncbi.nlm.nih.gov/17543848/) | 2007 | Preclinical (animal) | Transl Res | Intravenous iron sucrose affected intraperitoneal homeostasis in rats, with pro-oxidant and pro-inflammatory effects |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11354P | VENOFER SOLUTION FOR INJECTION 100 mg/5 ml | Injection | Not stated in the available record |

---

## Safety Considerations

- **Drug Interactions**: 42 interactions were identified in total. One is rated Major and the rest shown are Moderate.
  - **Major**: Dimercaprol
  - **Moderate (examples)**:
    - Tetracyclines: doxycycline, minocycline, tetracycline
    - Vitamin D analogues: cholecalciferol, calcifediol, ergocalciferol, dihydrotachysterol, doxercalciferol
    - Bisphosphonates: alendronic acid, risedronic acid, ibandronate
    - ACE inhibitors: benazepril, captopril, enalapril
    - Thyroid agents: levothyroxine, liothyronine, porcine thyroid
    - Others: chloramphenicol, oral iron
- **Preclinical signal**: In vitro data suggest intravenous iron may be toxic to pancreatic beta cells at pharmacologically relevant concentrations. This is relevant when considering any pancreas-related use.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, primary hyperoxaluria, rests only on a model score, with no trials, no literature and no plausible mechanism. The same applies to most of the other nine predictions. Only hyperparathyroidism has indirect supporting data (L3, "Research Question"), and the single preclinical safety signal for pancreatitis argues against that indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA, which are currently missing and block safety screening
- Mechanism of action data for iron sucrose, for example from DrugBank
- A focused review of the PTH, FGF23 and phosphate endpoints in the CKD and dialysis studies, to test whether iron sucrose itself affects mineral metabolism (the hyperparathyroidism hypothesis)
- Clarification of the approved indication text for the Singapore licence SIN11354P
- Mechanistic justification, or deprioritisation, of primary hyperoxaluria and the other prediction-only indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

