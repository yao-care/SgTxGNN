---
layout: default
title: Protein C
parent: Low Evidence (L5)
nav_order: 830
evidence_level: L5
indication_count: 10
---

# Protein C
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

# Protein C: From an Unrecorded Approved Use to Glanzmann Thrombasthenia

## One-Sentence Summary

Protein C is a vitamin K-dependent natural anticoagulant, and its original approved indication is not recorded in the Singapore registry data.
The TxGNN model predicts it may be effective for **Glanzmann thrombasthenia** with a very high score, but there are **0 clinical trials** and only **2 publications** (both general reviews with no protein C treatment data).
This top-ranked prediction looks like a knowledge-graph artifact and is not supported by mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the HSA licence data |
| Predicted New Indication | Glanzmann thrombasthenia |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the source database. Protein C is known as the body's own anticoagulant: once activated, it inactivates clotting factors Va and VIIIa and so limits clot formation.

Glanzmann thrombasthenia is the opposite kind of problem. It is a bleeding disorder caused by a defect in the platelet GPIIb/IIIa receptor. An anticoagulant would be expected to worsen bleeding, not treat it. The high score (0.986) therefore most likely reflects a link in the knowledge graph rather than a real therapeutic relationship. The two supporting papers are a veterinary diagnostic review and a coagulation physiology review, and neither contains protein C therapy data.

This does not mean the drug has no credible new use. Among the other ten predictions, **inherited thrombophilia** (rank 8, score 90.0%) is the only one with real support. Protein C concentrate is studied in severe congenital protein C deficiency, and the logic is direct: replacing the missing anticoagulant protein. That is closer to an established use than to true repurposing (see the conclusion below).

## Clinical Trial Evidence

Currently no related clinical trials registered for Glanzmann thrombasthenia.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32368218](https://pubmed.ncbi.nlm.nih.gov/32368218/) | 2020 | Review | Iranian Journal of Veterinary Research | Describes how hemostatic disorders are diagnosed in horses. No protein C treatment data. |
| [10494034](https://pubmed.ncbi.nlm.nih.gov/10494034/) | 1999 | Review | Haemostasis | Explains thrombin generation and platelet interaction in platelet-rich plasma. No protein C treatment data. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14933P | OCTAPLEX POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 500 IU | Injection, powder, for solution | Not stated in the registry entry |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Glanzmann thrombasthenia) has no clinical trials, no relevant literature and a mechanism that points the wrong way, so it should not be pursued. Safety data are also missing, because the package insert has not been retrieved, and this blocks progression to safety screening.

**Other predictions (summary):**
- **Inherited thrombophilia (rank 8)** is the only candidate with real evidence. It is graded L2 and rated "Proceed with Guardrails". The support is a Phase 2/3 open-label, single-arm study of protein C concentrate in severe congenital protein C deficiency (NCT00157118, n=18, not an RCT), plus a treatment registry and a Japanese post-marketing surveillance study. Any recommendation should be limited to **severe congenital protein C deficiency**, under hematology supervision with thrombosis and bleeding monitoring. Other inherited thrombophilias (for example factor V Leiden) are not supported.
- **Ranks 2–7, 9 and 10** (platelet and coagulation-factor bleeding disorders) have no mechanistic rationale and only L5 evidence. Rank 10, "flood factor deficiency", may be a mislabelled ontology term.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications) to complete safety screening. This is a blocking gap.
- The approved indication for SIN14933P, to define the original indication.
- Mechanism of action data from DrugBank.
- A decision on whether to re-scope the evaluation to severe congenital protein C deficiency, which is closer to an established use than to repurposing.
- Verification of the ontology mapping for "flood factor deficiency".
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

