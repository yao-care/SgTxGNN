---
layout: default
title: Bemiparin
parent: Low Evidence (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Bemiparin
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

# Bemiparin: From Venous Thromboembolism Anticoagulation to Primary Release Disorder of Platelets

## One-Sentence Summary

Bemiparin is a low molecular weight heparin, used as an anticoagulant to treat and prevent venous thromboembolism (VTE).
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but no clinical trials or publications support this prediction.
This is a model-only signal, and the pharmacology points the opposite way: an anticoagulant is expected to worsen a bleeding disorder.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA registration records (literature describes DVT treatment and VTE prophylaxis) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 98.71% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Bemiparin is a low molecular weight heparin. It enhances antithrombin activity and inhibits factor Xa, which reduces clot formation and growth.

Primary release disorder of platelets is a bleeding disorder caused by defective platelet function. Treating it would call for supporting hemostasis, not suppressing coagulation. The mechanisms therefore point in opposite directions, and no therapeutic rationale was identified.

The high graph score (98.71%) most likely reflects shared coagulation and platelet network neighbors in the knowledge graph, not real therapeutic potential. This prediction should be read as a **safety caution**, not a repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16463P | HIBOR Solution for Injection in Pre-filled Syringes 2,500 IU anti-Xa/0.2 mL | Injection, solution | Not stated in the record |
| SIN16462P | HIBOR Solution for Injection in Pre-filled Syringes 3,500 IU anti-Xa/0.2 mL | Injection, solution | Not stated in the record |

Both products are made by ROVI Pharma Industrial Services, S.A.

## Safety Considerations

Please refer to the package insert for safety information.

Points specific to this prediction:
- **Bleeding risk**: further anticoagulation in a patient with a platelet function defect would be expected to increase bleeding.
- **Heparin-induced thrombocytopenia**: this is a further concern in any setting with low platelet counts.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or literature. The mechanism is biologically implausible and raises a bleeding safety concern, so this indication should not be pursued.

**To proceed, the following is needed:**
- No further work is recommended for this indication.
- Retrieve the HSA package insert to confirm the approved indication and safety warnings. Neither is in the current records.

**Note on other predictions in the same evidence pack:**
- **Pulmonary embolism (rank 9):** This is the only prediction with substantial evidence. It is graded L1, with several completed Phase 3 bemiparin trials in VTE treatment and prophylaxis. It is largely an established use within the VTE class, not a novel repurposing finding. The pack suggests Proceed with Guardrails, covering bleeding, renal impairment, HIT monitoring, neuraxial anesthesia timing, and dosing by risk group. The local label status should be confirmed first.
- **Platelet-type bleeding disorder (rank 8):** The single linked trial studies ICU VTE prophylaxis and does not enroll patients with platelet bleeding disorders, so it is not evidence for this indication.
- **Other platelet or bleeding-disorder predictions (ranks 2–7 and 10):** All are L5 with no supporting evidence and the same bleeding concern. They should be treated as caution signals.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

