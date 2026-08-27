---
layout: default
title: Fosaprepitant
parent: 僅模型預測 (L5)
nav_order: 449
evidence_level: L5
indication_count: 10
---

# Fosaprepitant
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

# Fosaprepitant: From Chemotherapy-Induced Nausea/Vomiting Prevention to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

> Fosaprepitant is the intravenous prodrug of aprepitant, an NK1/Substance P receptor antagonist used in evidence-pack trial data primarily as an antiemetic in chemotherapy-induced nausea and vomiting (CINV) regimens.
> The TxGNN model's top-ranked prediction for this drug is **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this candidate is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags it as a likely knowledge-graph false positive rather than a genuine repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded (data gap — see below); evidence-pack trial data indicate use as an NK1-antagonist antiemetic for chemotherapy-induced nausea and vomiting (CINV) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.92% (model rank 1,710) |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Fosaprepitant is not available in the structured record (data gap DG002). Based on information present elsewhere in this evidence pack — trial descriptions and the model's own rationale text — Fosaprepitant is the water-soluble intravenous prodrug that is rapidly converted to aprepitant, an NK1 (neurokinin-1)/Substance P receptor antagonist. Within the clinical trial evidence collected here, this mechanism is consistently used to block the central emetic reflex, i.e., as an antiemetic co-administered with 5-HT3 antagonists and dexamethasone during cisplatin- or cyclophosphamide-based chemotherapy.

NSIAD, the model's top-scoring predicted indication, is caused by gain-of-function mutations in the V2 vasopressin receptor (AVPR2), an entirely separate signaling pathway from NK1/Substance P. The evidence pack's own mechanistic rationale explicitly states there is "no known intersection" between NK1 antagonism and AVPR2-driven pathophysiology, and no clinical trials or literature exist to support this link.

Given the absence of any mechanistic bridge, clinical trial, or published evidence, this specific prediction is best interpreted as a **graph-embedding artifact** — the TxGNN score reflects statistical proximity in the knowledge graph rather than a validated biological hypothesis. Of the 10 candidates in this evidence pack, only one (retinitis, rank 7) has any supporting evidence — a single preclinical/mechanistic publication showing Fosaprepitant blocks NK1 receptor upregulation in a UV-induced ocular inflammation model — and even that is far from a clinical repurposing case. The remaining candidates (pneumocystosis, leprosy, cryptococcal meningitis, multiple endocrine neoplasia, intracranial abscess, malaria, echinococcosis, hyperargininemia) are infectious or metabolic/genetic diseases with no plausible mechanistic link to NK1 antagonism, and none have supporting clinical or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication (Nephrogenic Syndrome of Inappropriate Antidiuresis).

---

## Literature Evidence

Currently no related literature available for the predicted indication (Nephrogenic Syndrome of Inappropriate Antidiuresis).

---

## Singapore Market Information

Fosaprepitant currently has no market authorizations on file in Singapore (0 registrations; market status: not marketed). No product listing table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack — TFDA label data collection is flagged as a blocking data gap, see Conclusion.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (NSIAD) has an L5 evidence level — model prediction only, with no clinical trials, no literature, and no plausible mechanistic pathway connecting NK1/Substance P antagonism to AVPR2-driven pathophysiology. The evidence pack's own review assesses this as a likely false-positive association rather than a genuine repurposing signal, so it does not meet the threshold to advance beyond initial screening.

**To proceed, the following is needed:**
- Resolve the blocking data gap (DG001): TFDA/HSA label warnings and contraindications, required before any safety pre-screening (S1) can begin
- Resolve the high-priority data gap (DG002): confirmed mechanism-of-action data from DrugBank to properly assess mechanistic plausibility
- If pursuing repurposing research on this drug, prioritize retinitis (rank 7) instead — it is the only candidate with supporting mechanistic literature (PMID 32058829) and is already at decision stage S1 ("Research Question"), warranting a dedicated preclinical-to-clinical translation review rather than the NSIAD candidate
- No further action recommended on the NSIAD, pneumocystosis, leprosy, cryptococcal meningitis, multiple endocrine neoplasia, intracranial abscess, malaria, echinococcosis, or hyperargininemia candidates unless new clinical or mechanistic evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

