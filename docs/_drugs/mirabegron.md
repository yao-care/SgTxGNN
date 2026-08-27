---
layout: default
title: Mirabegron
parent: 僅模型預測 (L5)
nav_order: 661
evidence_level: L5
indication_count: 10
---

# Mirabegron
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

# Mirabegron: From an Undocumented Original Indication to Thoracic Malformation

## One-Sentence Summary

Mirabegron's original approved indication is not documented in the current evidence pack — this is flagged as an open data gap requiring follow-up (see Data Gaps below). The TxGNN model predicts a possible association with **Thoracic Malformation**, but this signal is currently supported by **zero clinical trials** and **zero peer-reviewed publications**; the model's own rationale text attributes the high score to graph-topology proximity to ciliopathy/renal-disease clusters rather than to a demonstrated pharmacological mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap — see DG002) |
| Predicted New Indication | Thoracic Malformation |
| TxGNN Prediction Score | 83.06% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Mirabegron is not available in this evidence pack (flagged as data gap DG002, severity High). However, the rationale narratives attached to several of the model's predicted indications consistently describe Mirabegron as a **β3-adrenergic receptor (β3-AR) agonist** — this characterization recurs across multiple entries in the evidence pack (ranks 1, 3, 6, 7, 8, 9) even though it is not confirmed by a formal DrugBank MOA record.

Because the original indication is itself undocumented, it is not possible to assess the pharmacological or disease-category relationship between Mirabegron's approved use and the predicted new indication (Thoracic Malformation). The `similarity_to_original` field for this prediction is marked "pending" for the same reason.

Critically, the evidence pack's own mechanistic assessment for this specific prediction states that Thoracic Malformation belongs to a short-rib thoracic dysplasia/ciliopathy phenotype spectrum that shares genetic network proximity with renal cystic disease nodes in the TxGNN knowledge graph — and explicitly concludes this is **likely a graph-embedding artifact rather than a true pharmacological link**, since no known pathway connects β3-AR agonism to thoracic/skeletal development. Combined with the complete absence of trials or literature, this prediction should be treated as a low-confidence model signal rather than a substantiated hypothesis.

*Additional context: among the 10 predictions returned for this drug, only rank 3 (polycystic kidney disease 3 with or without polycystic liver disease) has any literature support (20 PubMed records, all disease-background reviews/guidelines, none drug-specific). Even there, the evidence pack flags a directional mechanistic conflict — published research (Schena et al., PMID 34676684) suggests a β3-AR **antagonist** may slow cyst growth, whereas Mirabegron is an **agonist**, theoretically working against the proposed therapeutic direction. This further reinforces that no candidate in this prediction set currently has a coherent, evidence-backed mechanistic case.*

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Mirabegron currently has no registered product licenses on file — market status is "Not marketed" with 0 total registrations. No authorization records are available to list.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Regulatory label warnings and contraindications for this drug are an outstanding, Blocking-severity data gap (DG001) — this data must be obtained before any safety pre-assessment (S1) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Thoracic Malformation) is supported only by a raw TxGNN model score (L5, no clinical trials, no literature), and the evidence pack's own mechanistic review concludes this is likely graph-topology noise rather than a real pharmacological signal. Safety pre-assessment cannot proceed because label warnings/contraindications are a Blocking data gap, and the drug is not currently marketed in Singapore.

**To proceed, the following is needed:**
- Product label warnings and contraindications (remediate DG001 — Blocking severity; source: TFDA/HSA label PDF)
- Confirmed mechanism-of-action data via DrugBank (remediate DG002 — High severity)
- Drug-specific (not merely disease-background) preclinical or clinical evidence directly linking Mirabegron to Thoracic Malformation or the broader ciliopathy spectrum
- If the polycystic kidney/liver disease (PKD3) candidate is pursued instead, resolution of the agonist-vs-antagonist mechanistic conflict noted in the evidence pack before any further prioritization
- Confirmation of Singapore/regional registration status for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

