---
layout: default
title: Brigatinib
parent: Low Evidence (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: From ALK-Positive NSCLC to Gingival Fibromatosis

## One-Sentence Summary

Brigatinib is a kinase inhibitor marketed in Singapore as ALUNBRIG and used for ALK-positive non-small cell lung cancer (NSCLC). The TxGNN model predicts it may be effective for **gingival fibromatosis** with a very high score, but **0 clinical trials** and **0 publications** currently support this prediction. It is a model prediction only, so the recommendation is Hold.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive NSCLC (inferred from the retrieved literature; the Singapore licence records do not list indication text) |
| Predicted New Indication | Gingival fibromatosis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on the literature retrieved for other candidates, brigatinib is a next-generation ALK tyrosine kinase inhibitor. Its efficacy in ALK-positive NSCLC is supported by Phase 3 trials (ALTA-1L and ALTA-3). Mechanistically it could be applicable to other diseases only if they depend on the kinases it inhibits.

No such link has been shown for gingival fibromatosis. It is a fibrous overgrowth of the gum tissue, and no ALK- or EGFR-driven mechanism is documented for it. The very high TxGNN score comes from knowledge-graph patterns, not from any retrieved trial or publication. The relationship between the original and new indication (a malignant lung cancer versus a benign gingival overgrowth) has not been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15659P | ALUNBRIG FILM-COATED TABLET 90mg | Film-coated tablet |
| SIN15660P | ALUNBRIG FILM-COATED TABLET 180mg | Film-coated tablet |
| SIN15658P | ALUNBRIG FILM-COATED TABLET 30mg | Film-coated tablet |
| SIN15661P | ALUNBRIG INITIATION PACK | Film-coated tablet |

The approved indication text is not recorded in the licence data. All four products are oral formulations.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |

Please refer to the package insert warnings and precautions for myelosuppression risk, emetogenicity, monitoring items and handling requirements.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanism, so it remains at evidence level L5. The safety information for Singapore is also not yet available.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications), which is required before any safety screening
- Brigatinib's mechanism of action data, for example from the DrugBank API
- A targeted literature and trial search for gingival fibromatosis, covering the kinase pathways involved in fibrous overgrowth
- A mechanistic rationale showing that the disease depends on a kinase brigatinib inhibits
- Route compatibility assessment, since the available formulation is oral only and a gingival use may need a different route

Among the other TxGNN predictions for brigatinib, the NF2-related schwannomatosis signal (a clinical report and preclinical data) is a genuine lead for a different disease. It should be assessed as a separate candidate.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

