---
layout: default
title: Repaglinide
parent: 僅模型預測 (L5)
nav_order: 852
evidence_level: L5
indication_count: 10
---

# Repaglinide
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

# Repaglinide: From Type 2 Diabetes to Pancreatic Agenesis

## One-Sentence Summary

> Repaglinide is a meglitinide-class insulin secretagogue that closes pancreatic β-cell K-ATP channels to stimulate insulin release, historically used for type 2 diabetes mellitus.
> Among the TxGNN model's top 10 predictions, nine (including the #1-ranked opsismodysplasia) carry **no supporting evidence and an explicit "no known biological basis"** annotation.
> The only candidate with any literature support and mechanistic coherence is **Pancreatic Agenesis** (rank 8), backed by **2 mechanism-review publications** — evidence remains preclinical/mechanistic only, with no disease-specific trials.

*Note: This report focuses on Pancreatic Agenesis rather than the #1-ranked prediction (opsismodysplasia, score 98.77%), because the evidence pack itself flags opsismodysplasia as having "no known association with repaglinide's K-ATP channel/insulin secretion mechanism — high TxGNN score only, no biological basis." Pancreatic Agenesis is the only one of the 10 candidates scored above Hold (decision stage S1, "Research Question").*

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Singapore regulatory data (drug not marketed locally); internationally known as Type 2 Diabetes Mellitus |
| Predicted New Indication | Pancreatic Agenesis |
| TxGNN Prediction Score | 97.58% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Research Question stage) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for repaglinide is not available in this evidence pack. Based on known pharmacology (reflected in the evidence pack's own rationale fields), repaglinide binds to sulfonylurea receptor sites on pancreatic β-cells, closing ATP-sensitive potassium (K-ATP) channels and triggering calcium influx that promotes insulin secretion. This mechanism underlies its established use in type 2 diabetes.

Pancreatic Agenesis — particularly partial forms and neonatal diabetes caused by K-ATP channel gene mutations (e.g., *KCNJ11*, *ABCC8*) — shares a direct mechanistic link with repaglinide's mode of action, since some neonatal diabetes subtypes are already treated by K-ATP channel modulation. This is why the model surfaces a plausible connection.

However, the mechanistic argument has an important limitation: if the condition involves **complete** pancreatic agenesis with no residual β-cell mass, there would be no functional target for repaglinide to act on. The two supporting publications identified are general reviews of insulin secretion physiology and repaglinide pharmacology — neither addresses pancreatic agenesis directly. The prediction should therefore be read as a mechanistically plausible hypothesis for a specific subtype (residual β-cell/K-ATP-mutation-driven neonatal diabetes), not as evidence of efficacy in classic complete pancreatic agenesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10746006](https://pubmed.ncbi.nlm.nih.gov/10746006/) | 1999 | Review | Diabetes & Metabolism | General review of progressive β-cell dysfunction and insulin secretion abnormalities in type 2 diabetes; not disease-specific |
| [10746008](https://pubmed.ncbi.nlm.nih.gov/10746008/) | 1999 | Review | Diabetes & Metabolism | Review of postprandial glucose regulation and insulin secretagogue use; not disease-specific |

---

## Singapore Market Information

Repaglinide currently holds no marketing authorization in Singapore (0 registrations recorded); no local product listings are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No key warnings, contraindications, or drug-interaction data are currently available in this evidence pack — including drug label warnings/contraindications, tracked as a Blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold (Research Question stage)**

**Rationale:**
Evidence is limited to two non-specific mechanism reviews (L4, mechanistic/preclinical only) with no disease-specific trials or literature, and the mechanistic rationale only applies to a subtype of the condition (residual β-cell/K-ATP-mutation-driven cases), not classic complete pancreatic agenesis. Repaglinide is also not currently marketed in Singapore, and drug label safety data (warnings/contraindications) are missing (DG001, Blocking).

**To proceed, the following is needed:**
- TFDA/HSA product label with warnings and contraindications (DG001 — Blocking; required before any S1 safety review)
- Confirmed drug mechanism of action from DrugBank (DG002)
- Disease-subtype clarification: differentiate partial vs. complete pancreatic agenesis, and confirm presence of residual β-cell mass as a prerequisite for mechanistic relevance
- Disease-specific literature or case reports directly evaluating repaglinide (or meglitinides) in neonatal diabetes/pancreatic agenesis populations
- Reassessment of the remaining 9 candidates (all currently "Hold," L5, no evidence) is not recommended unless new evidence emerges — several rationale fields explicitly state no biological basis for association
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

