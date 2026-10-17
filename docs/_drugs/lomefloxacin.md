---
layout: default
title: Lomefloxacin
parent: Medium Evidence (L3-L4)
nav_order: 610
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Lomefloxacin: predicted new indication Laryngotracheitis (evidence level L4). Approved use: Urinary tract infection, bronchitis"
monitor_inn: "Lomefloxacin"
predicted_indications: ["laryngotracheitis", "heart valve disease", "heart conduction disease", "congenital anomaly of ventricular septum", "heart neoplasm", "pericardium disease", "carcinoid heart disease", "cardiac anomalies-heterotaxy syndrome", "myocardial rupture", "heart aneurysm"]
---

# Lomefloxacin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Lomefloxacin: From Urinary Tract Infection and Bronchitis to Laryngotracheitis

## One-Sentence Summary

Lomefloxacin is a fluoroquinolone antibiotic originally used to treat **urinary tract infection and bronchitis**.
The TxGNN model predicts it may be effective for **laryngotracheitis**,
but **no clinical trials and no publications** currently support this direction, so it rests on a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, bronchitis (from the knowledge graph; the Singapore licence has no indication text recorded) |
| Predicted New Indication | Laryngotracheitis |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known information, lomefloxacin is a fluoroquinolone antibacterial with activity against respiratory pathogens. Its use in bronchitis is established, so it may mechanistically be applicable to other airway infections.

Laryngotracheitis is an infection of the upper and central airway. It lies close to the bronchi anatomically and can share some bacterial causes, which gives the prediction some indirect plausibility.

There are important limits, however. Laryngotracheitis (croup) is predominantly viral, and an antibacterial would not be expected to help in those cases. The high TxGNN score is a computational result and has not been checked against any trial or publication.

Other predicted indications are mostly cardiac conditions, such as heart valve disease, heart conduction disease and heart aneurysm. These are rated L5 and Hold, because they show no plausible therapeutic mechanism and may be artifacts of knowledge-graph connectivity. Fluoroquinolones carry known cardiac and vascular safety signals, including QT prolongation and aortic aneurysm or dissection risk. These signals point toward potential harm rather than benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10847P | LOMFLOX TABLET 400 mg (IPCA Laboratories Ltd) | Tablet, film coated (oral) | Not recorded |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database. The sample reviewed includes these main ones:
  - **Major**: hydrocortisone, dexamethasone, betamethasone, triamcinolone, bupropion, chlorpropamide
  - **Moderate**: antidiabetic drugs (metformin, pioglitazone, acarbose, alogliptin, albiglutide, canagliflozin), famotidine, loperamide, acetylsalicylic acid, balsalazide, bisacodyl, and calcium and potassium salts (calcium phosphate, calcium acetate, potassium citrate)
- **Class-level cardiovascular signals**: Fluoroquinolones are associated with QT prolongation and with aortic aneurysm or dissection. These should be weighed in any repurposing assessment.

Please refer to the package insert for the remaining safety information (warnings and contraindications), because this label data has not been obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for laryngotracheitis has a high model score but no supporting trials or literature, and the main disease is usually viral. The product is marketed in Singapore, but the label safety data has not been reviewed, so it is not ready to advance beyond a research question.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator (HSA), which is a blocking gap for safety screening
- Detailed mechanism of action data (for example from DrugBank)
- A literature and trial search on fluoroquinolones in bacterial laryngotracheitis or other upper airway infections
- A review of whether bacterial laryngotracheitis is a realistic target, and of the cardiovascular safety signals
- A check of the approved indication text for the Singapore licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

