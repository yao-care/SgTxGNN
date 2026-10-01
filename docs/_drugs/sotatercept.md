---
layout: default
title: Sotatercept
parent: Low Evidence (L5)
nav_order: 923
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: From a Marketed Use Not Recorded in the Evidence Pack to Acute Lymphoblastic Leukemia

## One-Sentence Summary

Sotatercept is marketed in Singapore as Winrevair, but the supplied record does not state its approved indication.
The TxGNN model predicts it may be effective for **acute lymphoblastic leukemia**, with a very high score.
However, there are **0 clinical trials** and **0 publications** behind this prediction, so it is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied record |
| Predicted New Indication | Acute lymphoblastic leukemia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. The supplied analysis describes sotatercept as an activin signaling trap (ActRIIA-Fc), a fusion protein that binds ligands of the TGF-beta/activin family.

No direct link between this mechanism and lymphoid leukemia biology is evident from the supplied data. The very high score may reflect knowledge-graph artifacts rather than real biology, particularly because the original indication and mechanism fields are missing. The score should be treated as a hypothesis-generating signal, not as support for efficacy.

**Other predicted candidates (all L5, prediction only, no supplied trials or literature):**

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Severe nonproliferative diabetic retinopathy | 99.77% | Speculative link to retinal vascular remodeling. Bleeding-related adverse effects would need careful review. |
| 3 | Diabetic retinopathy | 99.72% | Parent term of rank 2, so not an independent signal. |
| 4 | Drug-induced osteoporosis | 99.65% | Activin/ActRII ligand trapping is biologically plausible for bone metabolism. This is the most mechanistically coherent candidate and is flagged as a research question. |
| 5 | Diabetic cataract | 99.49% | No clear pathway to lens pathology. Likely reflects the diabetic-complication cluster in the graph. |
| 6 | HER2 positive breast carcinoma | 99.43% | Direction of effect of activin inhibition is uncertain and could be unfavorable. |
| 7–10 | Urothelial carcinoma variants (transitional cell, prostatic urethra, kidney pelvis sarcomatoid, bladder sarcomatoid) | 99.34–99.39% | Near-identical scores suggest a shared graph neighborhood, not independent evidence. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN17094P | WINREVAIR® Powder for Solution for Injection 60 mg (vial only) | Injection, powder, lyophilized, for solution |
| SIN17093P | WINREVAIR® Powder for Solution for Injection 45 mg (vial only) | Injection, powder, lyophilized, for solution |

Both products are manufactured by Patheon Italia S.p.A. The approved indication text is blank in the supplied record. Both forms are injectables.

---

## Safety Considerations

Please refer to the package insert for safety information.

The supplied analysis notes that sotatercept's known vascular and bleeding-related adverse effects would need careful review in any retinopathy population.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction rests on a model score alone, with no supporting trials or literature and no identifiable mechanistic link to acute lymphoblastic leukemia. The safety information needed for screening is also missing.

**To proceed, the following is needed:**
- The package insert from the Health Sciences Authority (HSA), covering warnings and contraindications, to allow safety screening
- The approved indication and detailed mechanism of action, to enable a proper mechanistic-link analysis
- A targeted trial and literature search for each candidate, starting with drug-induced osteoporosis, the most mechanistically coherent
- A route-compatibility check against the injectable-only formulations marketed in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

