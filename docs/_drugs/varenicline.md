---
layout: default
title: Varenicline
parent: 僅模型預測 (L5)
nav_order: 1046
evidence_level: L5
indication_count: 10
---

# Varenicline
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

# Varenicline: From Smoking Cessation to Migraine Disorder

## One-Sentence Summary

> Varenicline (DrugBank DB01273) is a nicotinic receptor partial agonist originally used for smoking cessation / nicotine dependence.
> The TxGNN model predicts it may be effective for **Migraine Disorder**, with a prediction score of **99.92%**,
> but this is supported by only **1 case report** (an adverse cardiac event, not an efficacy study) and **no clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smoking cessation / nicotine dependence (not derivable from Singapore license data — drug is not marketed here; referenced as background context in the evidence pack's rationale text) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (single case report only; no RCT, no clinical trial) |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for varenicline is not available in this evidence pack. Based on general background pharmacology (not sourced from the structured MOA field in this dataset), varenicline is known as a partial agonist at the α4β2 nicotinic acetylcholine receptor (nAChR), which reduces nicotine craving and withdrawal — the basis for its approved use in smoking cessation.

The theoretical rationale linking varenicline to migraine rests on the fact that nAChR signaling has some involvement in trigeminovascular pain modulation. However, this is a mechanistic hypothesis only — the evidence pack contains no clinical trial or efficacy literature testing varenicline for migraine.

Critically, the single piece of literature evidence associated with this prediction (PMID 19585710) is a case report of **cardiac arrest following varenicline use** — an adverse safety event, not evidence of therapeutic benefit for migraine. This runs counter to, rather than supports, the repurposing hypothesis. Given the complete absence of efficacy data and the presence of only a safety-concerning case report, this prediction should be treated as a model-generated hypothesis requiring substantial further validation, not an actionable signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Case Report | Therapie | Reports a case of **cardiac arrest** associated with varenicline use — an adverse safety event, not evidence of efficacy for migraine |

---

## Singapore Market Information

Varenicline holds no marketing authorization in Singapore (market status: 未上市, 0 registrations). No product license data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. (No structured warnings, contraindications, or drug-interaction data are available in this evidence pack.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted migraine indication is supported only by a theoretical mechanistic hypothesis and a single case report describing a serious adverse cardiac event — not therapeutic efficacy. There are no clinical trials, RCTs, or efficacy literature specific to migraine, and the drug is not currently marketed in Singapore. Evidence level is L4 at best, and the only concrete clinical signal points toward a safety concern rather than benefit.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data from DrugBank or the official label
- Regulatory safety data (warnings, contraindications, DDI) from TFDA/HSA product labeling
- Dedicated preclinical or clinical studies evaluating varenicline specifically for migraine, not smoking-cessation trials with incidental headache mentions
- Further pharmacovigilance review of the cardiac arrest signal (PMID 19585710) before any therapeutic hypothesis is pursued
- Note: the other 9 predicted indications in this evidence pack (e.g., migraine with brainstem aura, alopecia subtypes, glaucoma, headache disorder, pulmonary hypertension) are all L4–L5 with either no evidence or evidence pack literature/trials that, on inspection, pertain only to the original smoking-cessation indication or adverse events — none currently warrant progression beyond Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

