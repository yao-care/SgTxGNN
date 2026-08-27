---
layout: default
title: Linagliptin
parent: 僅模型預測 (L5)
nav_order: 595
evidence_level: L5
indication_count: 10
---

# Linagliptin
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

# Linagliptin: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

> Linagliptin (DrugBank ID: DB08882) is a DPP-4 inhibitor globally used to treat **Type 2 Diabetes Mellitus**.
> The TxGNN model predicts it may be effective for **Opsismodysplasia**,
> but this direction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags this score as a likely knowledge-graph embedding artifact rather than a real biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (general drug-class knowledge; not present in this evidence pack — no local license/indication data available) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 94.90% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (marked as a High-severity data gap, DG002). Based on general pharmacological knowledge, linagliptin is a dipeptidyl peptidase-4 (DPP-4) inhibitor that enhances incretin (GLP-1/GIP) signalling to improve glycaemic control — its efficacy in Type 2 Diabetes Mellitus is well established.

Opsismodysplasia, however, is a rare skeletal dysplasia caused by *INPPL1* gene mutations, with a pathophysiology rooted in disrupted phosphatase signal transduction — a pathway with no established connection to DPP-4 inhibition or incretin biology. The evidence pack's own mechanistic annotation is explicit on this point: it states there is no known mechanistic link between linagliptin's target pathway and opsismodysplasia, and attributes the high TxGNN score to embedding distortion caused by sparse knowledge-graph neighbours around this rare disease node, rather than a genuine biological signal.

Given this, the prediction should be treated as a hypothesis-generating artifact of the model rather than a credible repurposing candidate at this time. No clinical trials, ICTRP records, or PubMed literature were found linking linagliptin to opsismodysplasia (confirmed via targeted searches across ClinicalTrials.gov, ICTRP, and PubMed), which is consistent with the absence of a plausible mechanistic basis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA-equivalent warning/contraindication data is currently a Blocking-severity data gap in this evidence pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score (94.90%) is not accompanied by any clinical, trial-registry, or literature evidence, and the evidence pack's own mechanistic review indicates the score likely reflects a knowledge-graph embedding artifact for a data-sparse rare disease node rather than a real pharmacological signal. There is no plausible mechanistic pathway connecting DPP-4/incretin biology to opsismodysplasia's underlying *INPPL1*-driven pathology.

**To proceed, the following is needed:**
- Local (Singapore) drug warnings and contraindication data — currently a **Blocking** data gap preventing initial safety screening (S1)
- Confirmed mechanism of action (MOA) documentation from DrugBank or equivalent source
- Independent biological/mechanistic plausibility assessment for opsismodysplasia specifically, given the model's own flag of likely embedding distortion
- Re-evaluation against lower-ranked candidates with at least partial literature support (e.g., rank 8, pancreatic agenesis, which returned 2 PubMed records) before committing further review resources to this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

