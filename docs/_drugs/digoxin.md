---
layout: default
title: Digoxin
parent: Low Evidence (L5)
nav_order: 326
evidence_level: L5
indication_count: 10
---

# Digoxin
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

# Digoxin: From Heart Failure and Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside, generally used for heart failure and atrial fibrillation rate control. The TxGNN model predicts it may be effective for **Prinzmetal angina** (coronary vasospasm), but there are **0 clinical trials** and only **2 publications** (reviews with no digoxin-specific findings), so support is essentially limited to the model score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heart failure and atrial fibrillation (general pharmacological knowledge; the Singapore registration records give no indication text) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 (as graded in the Evidence Pack; the two publications are indirect and do not test digoxin for this condition) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Digoxin inhibits the Na+/K+-ATPase pump. In the heart this increases contractility and slows atrioventricular conduction, which is why it is used in heart failure and atrial fibrillation.

The link to Prinzmetal angina is weak. The pump is also present in vascular smooth muscle, and inhibiting it may raise vascular tone. Prinzmetal angina is caused by coronary vasospasm, so a benefit is implausible and harm is possible. The very high TxGNN score (0.998) reflects graph-based similarity between the drug and the disease, not clinical data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | Chronopharmacology and its impact on antihypertensive treatment. Concerns circadian rhythms in blood pressure therapy; the provided abstract excerpt does not mention digoxin. |
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Review | Chin Med Sci J | Study of 30 patients with angina decubitus, who had severe coronary obstruction and raised myocardial oxygen consumption. It is about effort-type angina, not Prinzmetal angina, and the provided abstract excerpt does not mention digoxin. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN01198P | LANOXIN TABLET 0.25 mg | Tablet | Not stated in registry record |
| SIN17078P | DIGOKERN TABLETS 0.25MG | Tablet | Not stated in registry record |
| SIN00544P | LANOXIN PAEDIATRIC/GERIATRIC ELIXIR 0.05 mg/ml | Elixir | Not stated in registry record |
| SIN01203P | LANOXIN-PG PAEDIATRIC/GERIATRIC TABLET 0.0625 mg | Tablet | Not stated in registry record |
| SIN00547P | LANOXIN INJECTION 0.5 mg/2 ml | Injection | Not stated in registry record |

Available routes: oral (tablet), other (elixir), injectable.

## Safety Considerations

Please refer to the package insert for safety information.

One theoretical concern applies to this prediction. Na+/K+-ATPase inhibition can raise vascular tone, so digoxin could worsen coronary vasospasm.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. No trials exist, the two publications are unrelated to digoxin in Prinzmetal angina, and the pharmacology argues against benefit and raises a possible safety concern.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed Singapore approved-indication text and mechanism-of-action data from DrugBank
- Any direct evidence of digoxin's effect on coronary vasospasm, such as case series or mechanistic studies
- Review of the other predicted indications; among the top 10, only stroke disorder was staged as a research question (still L4), and it is driven by atrial fibrillation evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

