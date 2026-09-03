---
layout: default
title: Remdesivir
parent: 僅模型預測 (L5)
nav_order: 850
evidence_level: L5
indication_count: 10
---

# Remdesivir
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

# Remdesivir: From COVID-19 to Multiple Endocrine Neoplasia

## One-Sentence Summary

Remdesivir is an RNA-dependent RNA polymerase (RdRp) inhibitor originally developed for Ebola and repurposed for COVID-19 (SARS-CoV-2 infection). The TxGNN model's top-ranked prediction — **Multiple Endocrine Neoplasia (MEN)** — has **no supporting clinical trials or literature**, and the model's own mechanistic review flags it as a knowledge-graph embedding artifact with no biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | COVID-19 / SARS-CoV-2 infection (per associated trial and literature evidence; formal license text not available) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on trial and literature context, Remdesivir is a nucleotide analog prodrug that inhibits viral RdRp, and its clinical use has centered on RNA viruses (Ebola, SARS-CoV-2).

Multiple Endocrine Neoplasia is a hereditary endocrine tumour syndrome driven by *RET* or *MEN1* germline mutations — a genetic/oncogenic disease mechanism entirely unrelated to RdRp inhibition. The model's own rationale states explicitly that this pairing has **no biological plausibility** and reflects knowledge-graph embedding similarity rather than a genuine mechanistic or clinical signal.

**Important context on lower-ranked candidates:** several other top-10 predictions (e.g., HIV infection, rank 2) initially appear well-supported with 23 clinical trials and 20 publications. However, closer review shows these are a **systematic label-mismatch artifact**: virtually all of the underlying trials and literature (e.g., NCT04292730/ACTT-1, PMID 33264556/WHO Solidarity Trial) are Remdesivir-in-COVID-19 studies, not HIV studies. None of the 10 ranked predictions in this evidence pack carry genuine, disease-specific supporting evidence for the labeled indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Remdesivir is not currently marketed in Singapore (market status: Not Marketed; 0 registrations on file). No license records are available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Multiple Endocrine Neoplasia) has zero clinical trial or literature support and is explicitly assessed as mechanistically implausible. Review of other top-10 candidates in this evidence pack reveals a recurring KG label-mismatch issue rather than genuine repurposing signals, so no candidate in this batch meets the threshold to proceed.

**To proceed, the following is needed:**
- Verified mechanism of action (MOA) data for Remdesivir from DrugBank/primary literature
- Confirmed original indication and regulatory status (Singapore has no license data on file)
- Re-run or manually audit the KG/literature matching pipeline to resolve the disease-label mismatch seen in rank 2 (HIV) and rank 8/10 (leprosy, CMV) candidates before treating their evidence counts as meaningful
- TFDA/HSA warning and contraindication data (currently a blocking data gap, DG001) before any safety-relevant decision can be made
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

