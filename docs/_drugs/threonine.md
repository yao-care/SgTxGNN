---
layout: default
title: Threonine
parent: 僅模型預測 (L5)
nav_order: 973
evidence_level: L5
indication_count: 10
---

# Threonine
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

# Threonine: From No Established Indication to Predicted Gastroparesis

## One-Sentence Summary

> Threonine is an essential amino acid with no defined original therapeutic indication in the available regulatory records (not currently marketed in Singapore).
> The TxGNN model predicts it may be relevant to **gastroparesis**, but this is currently supported by **zero clinical trials** and only **one indirect mechanistic publication** that does not study threonine directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — Threonine is an essential amino acid with no recorded approved indication in this evidence pack |
| Predicted New Indication | Gastroparesis (disease) |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, threonine is an essential amino acid and a key precursor for gastrointestinal mucin synthesis, which gives a theoretical (but unproven) link to gastric mucosal/smooth-muscle function.

The one literature item retrieved for the top-ranked indication (gastroparesis) does not actually study threonine — it describes apoptosis and PI3K-AKT-mTOR/AMPK-mTOR signaling in a rat model of diabetic gastroparesis, with no threonine administration or measurement. Across all ten predicted indications in this evidence pack (dyspepsia, vitamin D deficiency, renal tubular acidosis, postgastrectomy syndrome, hypophosphatemic rickets variants, congenital prothrombin deficiency, albinism-deafness syndrome, postmenopausal osteoporosis), the supporting literature consists almost entirely of unrelated mechanistic, genetic, or traditional-medicine studies that happen to mention "threonine" only as an amino acid residue in unrelated proteins (e.g., WNK kinases, NBCe1, SGK3) — not as a therapeutic intervention.

Given the complete absence of drug-specific mechanistic or clinical evidence, this candidate should be treated as a network-embedding signal only, not a pharmacologically grounded hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28627597](https://pubmed.ncbi.nlm.nih.gov/28627597/) | 2017 | Basic/Mechanistic (animal) | Molecular Medicine Reports | Describes gastric smooth muscle cell apoptosis and PI3K-AKT-mTOR/AMPK-mTOR signaling in a rat model of diabetic gastroparesis; does not investigate threonine administration or supplementation |

---

## Singapore Market Information

Threonine has no marketed products registered in Singapore under this evidence pack (0 total licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications (including the top-ranked gastroparesis) sit at Evidence Level L5 with zero supporting clinical trials, and the associated literature is mechanistically unrelated to threonine itself. Combined with the absence of Singapore market presence, original indication data, and MOA data, there is insufficient basis to advance this candidate past S0.

**To proceed, the following is needed:**
- Original MOA and established indication data for threonine (DrugBank / pharmacology reference)
- TFDA/HSA package insert data for warnings, contraindications, and DDI (currently a Blocking data gap)
- Preclinical or clinical studies directly testing threonine (not just amino-acid-residue mentions) in gastroparesis or other candidate indications before any further prioritization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

