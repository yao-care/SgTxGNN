---
layout: default
title: Maraviroc
parent: Low Evidence (L5)
nav_order: 630
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: Repurposing Prediction for Multiple Endocrine Neoplasia

## One-Sentence Summary

Maraviroc is a marketed oral drug in Singapore, and the pack's own rationale notes it as a CCR5 antagonist.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but **no clinical trials and no publications** currently support this prediction.
It rests on a model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack, and the Singapore registration record lists no approved indication text. Maraviroc is a CCR5 antagonist, so it blocks a chemokine receptor involved in immune-cell trafficking. No link between CCR5 blockade and multiple endocrine neoplasia has been identified in the data provided.

The high score (99.82%, rank 3098) is a knowledge-graph pattern, not evidence of benefit. Without a defined original indication or mechanism, the relationship between the drug's existing use and this new disease cannot be assessed. The prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13640P | Celsentri Film-Coated Tablet 150mg (Pfizer Manufacturing Deutschland GmbH) | Film-coated tablet (oral) | Not listed in the registration record |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were available in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature, and no identified mechanistic link. That leaves it at L5, and it should not move forward on the score alone.

**To proceed, the following is needed:**
- Singapore package insert (HSA) for warnings, contraindications, and the approved indication
- Mechanism of action data from DrugBank
- A literature and trial search specific to maraviroc and multiple endocrine neoplasia
- Route compatibility assessment (oral tablet is the only registered form)

**Other candidates from the same prediction run** (for prioritisation, not part of this report's decision):
- **HER2-positive breast carcinoma** has the most coherent signal. A preclinical study (PMID 32404410) links autocrine CCL5 to trastuzumab resistance, and maraviroc could plausibly counter it through CCR5. It does not test maraviroc directly.
- **Primary cutaneous T-cell lymphoma** has only an indirect chemokine-network review (PMID 37006247), so it stays a research question.
- **Candidiasis and cytomegalovirus infection** have only HIV-context literature and are likely confounded signals.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

