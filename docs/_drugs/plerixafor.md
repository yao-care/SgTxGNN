---
layout: default
title: Plerixafor
parent: 僅模型預測 (L5)
nav_order: 794
evidence_level: L5
indication_count: 10
---

# Plerixafor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Plerixafor: From Hematopoietic Stem Cell Mobilization to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Plerixafor is a CXCR4 antagonist originally used to mobilize hematopoietic stem cells from the bone marrow for autologous transplantation in patients with lymphoma and multiple myeloma. The TxGNN model predicts it may be effective for **Indolent Plasma Cell Myeloma**, but this specific prediction is currently supported by **0 clinical trials** and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hematopoietic stem cell (HSC) mobilization for autologous transplantation in patients with lymphoma/multiple myeloma (per FDA-approved use referenced in trial records) |
| Predicted New Indication | Indolent Plasma Cell Myeloma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available in this evidence pack. However, the trial and literature records consistently identify Plerixafor as a **CXCR4 antagonist** that blocks the SDF-1(CXCL12)/CXCR4 axis — the signaling pathway that keeps hematopoietic and malignant cells anchored in the bone marrow niche. Its approved use exploits this mechanism to mobilize stem cells out of the marrow for collection prior to transplant.

Multiple myeloma cells, including indolent forms, are also known to reside and proliferate within the bone marrow microenvironment via the same SDF-1/CXCR4 axis — the same biological niche-dependence that Plerixafor already disrupts in its approved indication. This provides a plausible mechanistic rationale: blocking CXCR4 could theoretically mobilize myeloma cells out of their protective marrow niche and increase their sensitivity to therapy, analogous to the "chemosensitization" strategy already studied in acute myeloid leukemia (see rank #7 in this prediction set, which has 29 completed/ongoing trials and 20+ publications built on exactly this CXCR4-blockade-plus-chemotherapy concept).

That said, **no clinical trial or published study in this evidence pack directly tests Plerixafor in indolent plasma cell myeloma**. The mechanistic link is inferred by analogy to AML chemosensitization data and general CXCR4 biology in plasma cell/marrow-niche interactions, not from direct evidence in this disease. This prediction should therefore be read as a hypothesis generated purely by the TxGNN model, distinct from the much better-evidenced myeloid leukemia and melanoma predictions elsewhere in this drug's prediction list.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Plerixafor currently has **no drug registration on file in Singapore** (0 licenses; market status: Not Marketed). No authorization number, product name, or approved indication text is available for this jurisdiction.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in the evidence pack — this is flagged as a **Blocking** data gap (DG001) that must be resolved before any safety evaluation.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (indolent plasma cell myeloma) is supported only by a TxGNN model score with zero corroborating clinical trials or literature (Evidence Level L5), and the drug is not currently marketed in Singapore. Combined with missing safety/label data, there is insufficient basis to advance this specific indication.

**To proceed, the following is needed:**
- HSA-equivalent label data — key warnings and contraindications (DG001, Blocking)
- Confirmed mechanism-of-action documentation from DrugBank (DG002, High)
- Disease-specific preclinical or clinical evidence connecting Plerixafor to indolent plasma cell myeloma (currently none exists)
- Consideration of redirecting research priority toward the drug's better-evidenced predictions (myeloid leukemia — L4/S1 with 29 trials and 20 publications; melanoma — L4 preclinical mechanistic support), which may represent more actionable repurposing candidates for this compound
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

