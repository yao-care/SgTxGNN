---
layout: default
title: Urokinase
parent: Low Evidence (L5)
nav_order: 1035
evidence_level: L5
indication_count: 10
---

# Urokinase
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

# Urokinase: From Thrombolytic Therapy (Original Indication Not Recorded) to Primary Release Disorder of Platelets

## One-Sentence Summary

Urokinase is a plasminogen activator that dissolves blood clots (fibrinolysis). It is marketed in Singapore as an injectable powder.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but this is a model prediction only. There is **1 clinical trial** and **3 publications** retrieved, and none of them tests urokinase for this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, urokinase is a plasminogen activator that converts plasminogen to plasmin and drives clot breakdown. Its approved indication is not recorded in the Singapore data, so the link to the new indication cannot be traced.

On mechanism, the prediction is hard to support. A primary platelet release (secretion) disorder is a bleeding disorder caused by impaired granule release. A fibrinolytic offers no clear pathway to correct this defect. Because urokinase increases bleeding risk, it could worsen the condition.

The high score (98.63%) most likely reflects proximity in the knowledge graph rather than a real therapeutic relationship. The other platelet and bleeding disorders predicted for this drug (Glanzmann thrombasthenia, pseudo-von Willebrand disease, Scott syndrome and others) show the same pattern: all are bleeding disorders where a fibrinolytic would be expected to be counterproductive.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06101667](https://clinicaltrials.gov/study/NCT06101667) | N/A (procedure) | Recruiting | 224 | Endovascular treatment vs medical management in acute basilar artery occlusion at 24–72 hours (ANGEL-BAO). A stroke population, not a platelet function disorder, and it does not test urokinase. Relevance grade: C. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [9173723](https://pubmed.ncbi.nlm.nih.gov/9173723/) | 1997 | Review | Z Kardiol | Role of coronary thrombosis in chronic myocardial ischemia. Not about platelet release disorders. |
| [1414164](https://pubmed.ncbi.nlm.nih.gov/1414164/) | 1992 | Observational | Acta Haematol | High plasma urokinase-type plasminogen activator levels in acute non-lymphoblastic leukemia. Not about platelet release disorders. |
| [32089086](https://pubmed.ncbi.nlm.nih.gov/32089086/) | 2020 | Unclassified | Circ Res | Crystal clots as a therapeutic target in cholesterol crystal embolism. Not about platelet release disorders. |

None of these papers addresses the predicted disease.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN11140P | UROKINASE-GREEN CROSS INJ. 60,000 iu/vial | Injection, powder, for solution | China Chemical & Pharmaceutical Co., Ltd. |

The approved indication text is not available in the registration record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no supporting trials or literature. The mechanism points the wrong way: a fibrinolytic would be expected to aggravate bleeding in a platelet function disorder.

Among the other predictions for this drug, only **thrombotic thrombocytopenic purpura (TTP)** has some biological plausibility (evidence level L4, "Research Question"):
- **Supporting:** Preclinical work (Microlyse) and a 1981 case report of urokinase for severe neurological complications in TTP.
- **Against:** Plasmin can inactivate ADAMTS13, and fibrinogenolysis and bleeding are concerns in thrombocytopenic patients.
- **Standard of care:** Plasma exchange, immunosuppression and caplacizumab are not displaced by this evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- The approved indication in Singapore, to define the original-to-new indication link
- Any direct preclinical or clinical evidence of urokinase in the predicted disease. Without it, the evaluation should not advance beyond S0.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

