---
layout: default
title: Sitagliptin
parent: 僅模型預測 (L5)
nav_order: 905
evidence_level: L5
indication_count: 10
---

# Sitagliptin
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

# Sitagliptin: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Sitagliptin is a DPP-4 inhibitor globally used to manage type 2 diabetes mellitus (T2DM) by prolonging incretin (GLP-1/GIP) activity.
The TxGNN model's top-ranked prediction for this drug is **Opsismodysplasia**, a rare skeletal dysplasia,
but this candidate is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the mechanistic link as unproven.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (globally established use; not registered in Singapore, so a local approved-indication text is unavailable) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 98.87% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for sitagliptin is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, sitagliptin belongs to the DPP-4 inhibitor (gliptin) class, which works by blocking the breakdown of incretin hormones (GLP-1, GIP) to enhance glucose-dependent insulin secretion — its efficacy in type 2 diabetes is well established.

Opsismodysplasia, however, is a rare genetic skeletal dysplasia caused by mutations in *INPPL1*, affecting bone growth and development. Per the evidence pack's own mechanistic assessment, **there is no known biological connection** between DPP-4 inhibition/incretin signaling and the *INPPL1*-driven skeletal pathway. The high TxGNN score is most likely an artifact of the knowledge-graph embedding space — sitagliptin and opsismodysplasia may share indirect neighboring nodes (e.g., through metabolic/endocrine pathways) without any genuine pharmacological rationale.

In short, this is a case where a high model confidence score does **not** translate into mechanistic plausibility. It should be treated as a research hypothesis to be interrogated (and likely deprioritized), not as an actionable repurposing lead.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Singapore Market Information

Sitagliptin is currently **not registered in the Singapore market** (0 authorizations on file). No product license, dosage form, or approved-indication information is available from local regulatory data at this time.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug–drug interaction data are all marked as data gaps in the current evidence pack — including the TFDA/HSA label review, which is flagged as a Blocking-severity gap. This must be resolved before any safety evaluation can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Opsismodysplasia) has a high TxGNN score but zero clinical or literature evidence, and the pack's own mechanistic review finds no credible biological link to sitagliptin's DPP-4/incretin mechanism — this pattern is consistent with a spurious knowledge-graph association rather than a genuine repurposing signal. Note also that a lower-ranked candidate (pancreatic agenesis, rank 6) has L4-level literature support, but that evidence concerns beta-cell function/pancreatic histology in diabetic patients, not the congenital organogenesis defect the disease label implies — a label–literature mismatch that also requires manual curation before use.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: obtain and parse the drug's official label (warnings/contraindications) from the regulatory source before any safety screening (S1) can occur
- Resolve High-severity data gap DG002: confirm mechanism of action via DrugBank API to support proper mechanistic-relevance analysis
- Manual review of the KG disease-node mapping for "opsismodysplasia" and "pancreatic agenesis" to rule out label mismatch
- If pursuing further, prioritize candidates with at least preliminary mechanistic or preclinical support over rank-1 by score alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

