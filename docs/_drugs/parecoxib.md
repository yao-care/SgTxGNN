---
layout: default
title: Parecoxib
parent: 僅模型預測 (L5)
nav_order: 756
evidence_level: L5
indication_count: 10
---

# Parecoxib
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

Using the report template exactly as specified in your prompt (no additional skill applies — this is a direct data-to-markdown transformation task).

Note: the JSON's regulatory data is keyed `taiwan_regulatory` and references TFDA (Taiwan FDA) in the data gaps, not Singapore/HSA. I've labeled those sections "Taiwan" to match the actual data source rather than the template's placeholder "Singapore" wording, since mislabeling the jurisdiction would misstate a fact not in the pack.

---

# Parecoxib: From Acute Postoperative Pain to Migraine Disorder

## One-Sentence Summary

> Parecoxib is an injectable, selective COX-2 inhibitor internationally used for short-term management of acute postoperative pain.
> The TxGNN model predicts it may be effective for **Migraine Disorder**,
> with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Taiwan registry (drug not marketed locally); internationally indicated for short-term treatment of acute postoperative pain |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Parecoxib is not available in this evidence pack (flagged as a High-severity data gap). Based on generally known pharmacology, Parecoxib is a selective cyclooxygenase-2 (COX-2) inhibitor, administered parenterally, and clinically established for short-term management of acute postoperative pain.

The predicted new indication, migraine disorder, shares a plausible mechanistic bridge with Parecoxib's established use: COX-2 inhibition suppresses prostaglandin synthesis, which is believed to reduce neurogenic inflammation and pain sensitization in the trigeminovascular system — a key pathological mechanism in acute migraine attacks. This is consistent with the existing clinical practice of using NSAIDs and COX-2-selective inhibitors as options for acute migraine treatment.

The single available pilot RCT directly compared intravenous parecoxib against sumatriptan and rizatriptan for acute migraine attacks, lending some direct (if preliminary) clinical support to the mechanistic rationale, beyond pure knowledge-graph extrapolation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21996647](https://pubmed.ncbi.nlm.nih.gov/21996647/) | 2011 | RCT | Clinical Neuropharmacology | Pilot study comparing oral rizatriptan (10 mg), IV parecoxib (40 mg), and subcutaneous sumatriptan for treating acute migraine attacks; investigates COX-2 inhibition as an alternative to triptans given its anti-inflammatory and analgesic properties. |

---

## Taiwan Market Information

Parecoxib currently has no registered pharmaceutical licenses in Taiwan (0 records on file; market status: 未上市/Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(TFDA warnings/contraindications and DDI data are flagged in this evidence pack as an unresolved, Blocking-severity data gap — see Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic rationale is plausible and supported by one small pilot RCT (L2 evidence), but Parecoxib is not currently marketed in Taiwan (0 registrations) and TFDA warning/contraindication data is missing — a Blocking-severity gap that prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — required to clear S1 safety pre-assessment
- Confirmed mechanism of action from DrugBank
- Drug-drug interaction (DDI) dataset (current query: not found)
- A larger, adequately powered Phase 2/3 RCT specifically for migraine, beyond the single existing pilot study
- Regulatory pathway assessment, since the drug has no current market authorization in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

