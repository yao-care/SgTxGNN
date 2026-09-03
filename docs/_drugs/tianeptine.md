---
layout: default
title: Tianeptine
parent: 僅模型預測 (L5)
nav_order: 976
evidence_level: L5
indication_count: 10
---

# Tianeptine
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

# Tianeptine: From Depression to Migraine Disorder

## One-Sentence Summary

> Tianeptine is an atypical tricyclic antidepressant, historically used in the treatment of **depression** (including dysthymic disorder), though this is not confirmed in official Singapore regulatory records.
> The TxGNN model's top-ranked prediction is **Migraine Disorder** (score 96.91%), but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure algorithmic signal with no direct evidence behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression / dysthymic disorder (based on literature; not found in official Singapore regulatory data — `original_indications` is empty) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 96.91% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for Tianeptine is not available in the evidence pack (flagged as a High-severity data gap). Based on literature retrieved for related indications, Tianeptine is described as a novel antidepressant that — unlike most other antidepressants — **stimulates** (rather than inhibits) serotonin reuptake, and its antidepressant/anxiolytic effects have also been linked to glutamatergic (AMPA receptor) modulation and mu-opioid receptor agonism, alongside effects on hippocampal neuroplasticity.

For the top-ranked prediction, **Migraine Disorder**, the evidence pack explicitly states there is no direct clinical trial or literature support — the rationale notes only a thematic overlap with an ongoing Phase 2 trial for the related "headache disorder" category (NCT06012552, testing Tianeptine for post-COVID "brain fog" including headache-related symptoms). This means the 96.91% score reflects graph-based pattern similarity in the TxGNN model rather than any confirmed pharmacological or clinical link to migraine specifically.

It is worth noting that other, lower-ranked predictions in this same evidence pack carry meaningfully stronger evidence: **Dysthymic Disorder** (rank 3, L2, 8 supporting publications including RCTs and a meta-analysis) and **Headache Disorder** (rank 5, L2, 1 actively recruiting Phase 2 RCT plus supporting literature) both have documented pharmacological plausibility tied to Tianeptine's serotonergic/antidepressant mechanism. These may represent more actionable repurposing candidates than the top TxGNN-ranked migraine indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Migraine Disorder.

*(For reference, an actively recruiting Phase 2 RCT — [NCT06012552](https://clinicaltrials.gov/study/NCT06012552) — is testing Tianeptine for headache-related "COVID fog" symptoms, a related but distinct predicted indication ranked #5 in this evidence pack.)*

---

## Literature Evidence

Currently no related literature available for Migraine Disorder.

---

## Singapore Market Information

Tianeptine is currently **not marketed** in Singapore (0 registrations recorded in the evidence pack). No dosage form, brand name, or approved indication data is available locally.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Key warnings, contraindications, and drug interaction data are all flagged as data gaps (`[Data Gap]`) in the current evidence pack, including a **Blocking**-severity gap for TFDA/HSA package insert warnings and contraindications (DG001). This must be resolved before any safety evaluation (S1 stage) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Migraine Disorder) has no clinical trial or literature support and is classified as Evidence Level L5 — a pure model-generated hypothesis. Combined with a **Blocking** data gap in core safety information (TFDA/HSA warnings and contraindications) and the drug's non-marketed status in Singapore, there is currently no basis to advance this specific candidate.

**To proceed, the following is needed:**
- Resolve **DG001** (Blocking): obtain and parse the official package insert for warnings/contraindications before any S1 safety evaluation
- Resolve **DG002** (High): obtain confirmed mechanism of action data from DrugBank to support mechanistic-link analysis
- Confirm the drug's officially approved original indication(s), as `original_indications` is currently empty in regulatory data
- If pursuing repurposing for this drug, consider re-scoping toward **Dysthymic Disorder** or **Headache Disorder**, which carry substantially stronger evidence (L2, active/completed RCTs) than the current top-ranked Migraine Disorder prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

