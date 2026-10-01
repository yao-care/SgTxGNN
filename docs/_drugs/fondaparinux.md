---
layout: default
title: Fondaparinux
parent: Low Evidence (L5)
nav_order: 447
evidence_level: L5
indication_count: 10
---

# Fondaparinux
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

# Fondaparinux: From Anticoagulation (Thrombosis Prevention) to Primary Release Disorder of Platelets

## One-Sentence Summary

Fondaparinux is an injectable anticoagulant that blocks factor Xa through antithrombin. The TxGNN model predicts it may be effective for **primary release disorder of platelets**, a bleeding-tendency condition. There is **no direct clinical evidence** for this prediction, and the mechanism points to a safety concern rather than a benefit. The 2 related trials and 2 publications retrieved concern other conditions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA registration data (general pharmacology: prevention and treatment of thrombosis) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 93.06% |
| Evidence Level | L5 (no study directly addresses the predicted indication; the evidence pack lists L4) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Fondaparinux is a synthetic indirect factor Xa inhibitor that works through antithrombin, so it reduces thrombin generation and clot formation.

The predicted disease is a platelet function disorder in which platelets fail to secrete or release their granule contents. Fondaparinux does not act on this pathway. The disorder causes a bleeding tendency, and adding an anticoagulant would raise hemorrhagic risk rather than correct the defect.

The high score most likely reflects proximity in the knowledge graph to other platelet-related conditions, such as heparin-induced thrombocytopenia (HIT), and not a true therapeutic link. This prediction should be treated as a model artifact until proven otherwise.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00911300](https://clinicaltrials.gov/study/NCT00911300) | Phase 2 | Completed | 349 | Fondaparinux vs heparin or vitamin K antagonists for anticoagulation in atrial fibrillation patients undergoing cardioversion. Not the predicted indication, so it is indirect evidence at best. |
| [NCT01178333](https://clinicaltrials.gov/study/NCT01178333) | N/A | Completed | 668 | Retrospective analysis of incidence and outcomes in heparin-induced thrombocytopenia (HIT-RADIO). HIT is a different disease, so this is indirect, observational evidence only. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28646118](https://pubmed.ncbi.nlm.nih.gov/28646118/) | 2017 | Review | Blood | Direct oral anticoagulants (e.g., rivaroxaban) for treating HIT, with an update of the Hamilton experience. Concerns HIT, not platelet release disorder. |
| [30018843](https://pubmed.ncbi.nlm.nih.gov/30018843/) | 2017 | Case report | Journal of the Advanced Practitioner in Oncology | Palliative care in a young patient with metastatic adenocarcinoma. Not relevant to the predicted indication. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13587P | Arixtra Solution for Injection 5.0 mg/0.4 ml | Injection, solution | Not stated in registry data |
| SIN16809P | Diviti Solution for Injection in Pre-filled Syringe 2.5mg/0.5ml | Injection, solution | Not stated in registry data |
| SIN12059P | Arixtra Solution for Injection 2.5 mg/0.5 ml | Injection | Not stated in registry data |
| SIN13586P | Arixtra Solution for Injection 7.5 mg/0.6 ml | Injection, solution | Not stated in registry data |

## Safety Considerations

Please refer to the package insert for safety information.

The predicted disease is itself a bleeding disorder. Anticoagulation would add hemorrhagic risk, and this is a fundamental safety contradiction for this indication.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no direct clinical evidence, and the drug's mechanism is opposed to the disease biology. Anticoagulating a patient with a platelet function defect would likely worsen bleeding. The TxGNN score appears to come from graph proximity to HIT and other platelet-related conditions.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Manual review of the trials to confirm that none of them address the predicted indication
- Consider redirecting effort to the rank 5 prediction, **vertebral artery occlusion**. It is the most mechanistically plausible candidate (thrombotic arterial occlusion), though it also has no clinical evidence yet. Cerebrovascular bleeding risk and the lack of a reversal agent would need to be addressed.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

