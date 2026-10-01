---
layout: default
title: Pentetic Acid
parent: Low Evidence (L5)
nav_order: 767
evidence_level: L5
indication_count: 10
---

# Pentetic Acid
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

# Pentetic Acid: From Diagnostic Imaging Agent (Approved Indication Not Recorded) to Thrombocytopenic Purpura

## One-Sentence Summary

Pentetic acid (DTPA) is a metal-chelating agent. In Singapore it is registered as a Technescan DTPA injection kit, which appears to be a diagnostic imaging product, though the registration data do not state the approved indication.
The TxGNN model predicts it may be effective for **thrombocytopenic purpura**, but the supporting evidence is essentially absent: **1 clinical trial (an incidental match)** and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (the product is a DTPA injection kit) |
| Predicted New Indication | Thrombocytopenic purpura |
| TxGNN Prediction Score | 97.25% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pentetic acid is a metal chelator and a ligand used in imaging agents. It has no known effect on platelet production, platelet destruction, or the immune and ADAMTS13 pathways involved in thrombocytopenic purpura.

The high score (0.972) comes only from patterns in the TxGNN knowledge graph. No plausible mechanistic link between DTPA and thrombocytopenic purpura was identified, and the similarity to the original indication has not been assessed. This prediction should be treated as a model output, not a mechanism-based hypothesis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03784898](https://clinicaltrials.gov/study/NCT03784898) | Phase 4 | Completed | 13 | Blood-sample collection in relapsing multiple sclerosis patients who developed immune thrombocytopenic purpura after LEMTRADA treatment, for DNA biomarker analysis. It does not test pentetic acid, and the match appears incidental (relevance grade C). |

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12150P | TECHNESCAN DTPA FOR INJECTION 20.8 mg/vial (Curium Netherlands B.V.) | Injection, powder, for solution | Not stated in the data |

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the DDI query.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). The only trial found is unrelated to pentetic acid, there is no literature, and no mechanistic link to thrombocytopenic purpura exists. The safety review also cannot start without the package insert.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications, approved indication). This is a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- Any direct preclinical or clinical evidence of pentetic acid in thrombocytopenic purpura. Without it, this candidate should not advance.
- Consider other predictions from the same list:
  - **Idiopathic copper-associated cirrhosis** is the most biologically plausible, since DTPA chelates copper. It is still only a hypothesis, and DTPA also depletes zinc, manganese and other essential metals.
  - **Hepatic infarction** has preclinical papers (L4), but these support a diagnostic imaging role, not a therapeutic one.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

