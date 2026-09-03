---
layout: default
title: Triamcinolone
parent: 僅模型預測 (L5)
nav_order: 1010
evidence_level: L5
indication_count: 10
---

# Triamcinolone
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

# Triamcinolone: From Corticosteroid Therapy to Alopecia Mucinosa

## One-Sentence Summary

> Triamcinolone is a synthetic corticosteroid (original indication data not specified in this evidence pack). The TxGNN model predicts it may be effective for **Alopecia Mucinosa** (follicular mucinosis), but this is currently supported only by **4 historical case reports** with **no registered clinical trials**, and no triamcinolone-specific efficacy data exists among them.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (drug record and Singapore license data are empty) |
| Predicted New Indication | Alopecia Mucinosa |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed original indication and mechanism of action data are not available in the evidence pack (both `original_indications` and `original_moa` are empty). Based on known pharmacological classification, triamcinolone is a synthetic glucocorticoid, and its therapeutic action is mediated through the glucocorticoid receptor, suppressing local inflammation and lymphocytic infiltration.

Alopecia mucinosa (follicular mucinosis) is a condition driven by perifollicular inflammatory infiltration. Intralesional or topical triamcinolone is already used in dermatology practice for this condition, which gives the mechanism a reasonable biological basis. However, the literature currently linked to this prediction consists entirely of case reports describing the disease itself — none of them evaluate triamcinolone specifically, so the mechanistic plausibility is not yet backed by drug-specific outcome data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4136515](https://pubmed.ncbi.nlm.nih.gov/4136515/) | 1974 | Case Report | Archives of Dermatology | Describes alopecia mucinosa with neurofollicular changes; disease characterization, not a treatment study |
| [14170262](https://pubmed.ncbi.nlm.nih.gov/14170262/) | 1964 | Case Report | Hifuka kiyo (Acta Dermatologica) | Japanese case report of alopecia mucinosa Pinkus (mucinosis follicularis Jablonska) |
| [23968145](https://pubmed.ncbi.nlm.nih.gov/23968145/) | 2014 | Case Report (bexarotene, non-triamcinolone) | International Journal of Dermatology | Idiopathic follicular mucinosis treated with topical bexarotene gel; not triamcinolone-related |
| [9917176](https://pubmed.ncbi.nlm.nih.gov/9917176/) | 1998 | Case Report / Clinical Image | European Journal of Dermatology | Clinical image case presentation of follicular mucinosis |

**Note:** None of the above literature evaluates triamcinolone directly; evidence supports disease characterization only.

---

## Singapore Market Information

Currently not registered in the Singapore market (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

**Important:** A Blocking-severity data gap exists for official regulatory safety labeling (warnings/contraindications), and drug interaction data was not found. This must be resolved before any safety evaluation (S1 stage) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (alopecia mucinosa) is supported only by tier-3 case reports with no triamcinolone-specific efficacy data and no clinical trials. Combined with the drug's unregistered status in Singapore and a Blocking-severity gap in safety labeling, there is currently insufficient evidence to advance beyond the research-question stage.

**To proceed, the following is needed:**
- Obtain official TFDA/manufacturer product insert (warnings, contraindications, DDI) to close the Blocking data gap
- Confirm drug mechanism of action via DrugBank API (currently missing)
- Identify triamcinolone-specific case series or controlled studies in alopecia mucinosa/follicular mucinosis
- Evaluate available dosage forms/routes (topical, intralesional) relevant to dermatologic use, since none are on file
- Note: among the other TxGNN-predicted indications in this evidence pack, **idiopathic steroid-sensitive nephrotic syndrome** (rank 8) has stronger evidence (L3, "Proceed with Guardrails") and may warrant separate evaluation as an alternative repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

