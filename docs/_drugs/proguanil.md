---
layout: default
title: Proguanil
parent: 僅模型預測 (L5)
nav_order: 821
evidence_level: L5
indication_count: 10
---

# Proguanil
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

# Proguanil: From Malaria to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Proguanil is a well-established antimalarial prodrug, though its specific original indication is not available from the current regulatory data source (the drug is not registered in Singapore). The TxGNN model predicts a possible link to **Smouldering Systemic Mastocytosis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph score with no pharmacological or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malaria (antimalarial prophylaxis/treatment — based on known drug classification; no Singapore regulatory record available, drug unregistered) |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 92.12% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the source database (flagged as a High-severity data gap). Based on established pharmacological knowledge, proguanil is an antimalarial prodrug metabolized by CYP2C19 into cycloguanil, which inhibits *Plasmodium* dihydrofolate reductase–thymidylate synthase (DHFR-TS), thereby blocking parasite folate synthesis and replication.

Smouldering systemic mastocytosis, in contrast, is a clonal mast cell disorder driven predominantly by activating **KIT D816V** mutations, with disease biology centered on tyrosine kinase signaling rather than folate metabolism. The evidence pack's own repurposing rationale explicitly states that proguanil has **no known KIT or tyrosine kinase inhibitory activity**, and that there is **no pharmacological or clinical basis** connecting its antifolate/antimalarial mechanism to mast cell proliferative disease.

In short, this candidate score reflects a knowledge-graph embedding similarity only, not a biologically grounded mechanistic hypothesis. It should be treated as a low-confidence, exploratory signal rather than a plausible repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Proguanil currently has no market authorization in Singapore (market status: 未上市, total registrations: 0). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5-level prediction (model score only) with zero supporting clinical trials or literature, and the drug's own repurposing rationale explicitly disclaims any known mechanistic link between proguanil's antifolate/antimalarial action and KIT-driven mast cell disease. Combined with the drug being unregistered in Singapore and lacking basic safety/MOA data, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert warnings and contraindications (Blocking data gap, DG001)
- Confirmed mechanism of action data via DrugBank or primary literature (High-severity gap, DG002)
- Independent pharmacological or preclinical rationale linking proguanil to mast cell/KIT pathway biology before any further evidence collection is warranted
- Re-evaluation only if new clinical or mechanistic evidence emerges — otherwise this candidate should remain deprioritized relative to higher-evidence-level predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

