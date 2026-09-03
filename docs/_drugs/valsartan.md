---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 1044
evidence_level: L5
indication_count: 10
---

# Valsartan
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

# Valsartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Valsartan is an angiotensin II receptor blocker (ARB) established for the treatment of hypertension and heart failure. The TxGNN model predicts potential efficacy for **Malignant Hypertensive Renal Disease**, but the only supporting literature examines a different drug's mechanism (endothelin antagonism), and no clinical trials currently exist to confirm this specific indication for Valsartan.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in the regulatory dataset (no licenses on file); Valsartan is a well-established ARB indicated for hypertension/heart failure per general product labeling |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, Valsartan is an AT1-receptor antagonist that blocks the renin-angiotensin-aldosterone system (RAAS), an effect well established for hypertension and heart failure.

Mechanistically, RAAS blockade can theoretically reduce intraglomerular pressure and vascular injury caused by malignant hypertension, giving biological plausibility to this predicted indication. However, the single literature reference retrieved for this candidate studies **Avosentan**, an endothelin-receptor antagonist, rather than Valsartan — a different drug class with a different target. This means the cited evidence does not directly demonstrate Valsartan's effect in this disease; it only supports the general concept that RAAS/vascular pathway modulation may help hypertensive nephropathy.

For comparison, a closely related candidate in this same evidence pack — **malignant renovascular hypertension** (rank 2) — is directly supported by a study of AT1-receptor blockade preventing lethal malignant hypertension (PMID 11560862), which is mechanistically identical to Valsartan's action. This suggests the current top-ranked candidate may be less well-supported than adjacent predictions in the same disease family.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Preclinical/Animal | Pharmacological Research | Avosentan (an endothelin-receptor antagonist, **not Valsartan**) showed protective effects against hypertensive nephropathy in a rat model, without causing fluid retention at lower doses. Relevant only as indirect mechanistic support for RAAS/vascular pathway involvement in hypertensive nephropathy — does not directly evidence Valsartan's efficacy. |

---

## Singapore Market Information

Valsartan currently has no registered authorizations in the Singapore dataset provided (0 licenses on file; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only literature evidence for this specific candidate concerns a different drug's mechanism (Avosentan, not Valsartan), and no clinical trials exist for malignant hypertensive renal disease with Valsartan. Evidence level L4 (mechanism/preclinical only, indirect) is insufficient to justify advancing this indication.

**To proceed, the following is needed:**
- Direct Valsartan-specific preclinical or clinical data in malignant hypertensive renal disease (current evidence is for a different drug class)
- TFDA/HSA product label warnings and contraindications (DG001, currently blocking safety review)
- Mechanism of action (MOA) documentation from DrugBank (DG002)
- Consider evaluating the closely related candidates **malignant renovascular hypertension** (rank 2, L3, direct AT1-blockade evidence) and **chronic pulmonary heart disease** (rank 6, L2, multiple Phase 4 RCTs on sacubitril/valsartan) as potentially stronger repurposing candidates for further investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

