---
layout: default
title: Selpercatinib
parent: 僅模型預測 (L5)
nav_order: 894
evidence_level: L5
indication_count: 10
---

# Selpercatinib
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

# Selpercatinib: From RET Fusion-Positive Cancer to Pulmonary Hypertension

## One-Sentence Summary

> Selpercatinib is a selective RET kinase inhibitor whose established use, based on the available literature, is treatment of RET fusion-positive non-small-cell lung cancer (and related RET-altered malignancies).
> The TxGNN model predicts it may be effective for **Pulmonary Hypertension**,
> but currently only **2 indirect publications** support this direction — and no clinical trials exist. Notably, the same literature reports **hypertension as a known adverse event** of this drug class, which runs counter to the predicted therapeutic direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | RET fusion-positive non-small-cell lung cancer (from literature context; no formal Taiwan-registered indication text available) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for selpercatinib is currently a data gap. Based on the available literature, selpercatinib is a selective RET (rearranged during transfection) kinase inhibitor, used clinically to treat RET fusion-positive non-small-cell lung cancer and other RET-altered cancers. Its efficacy in this oncology setting has been demonstrated in early clinical trials and confirmed in real-world cohorts (e.g., the SIREN retrospective analysis, PMID 34178121).

The proposed mechanistic link between RET inhibition and pulmonary hypertension is biologically plausible in principle — RET/GDNF signaling has been implicated in vascular smooth muscle regulation — but the direction of the predicted effect is not supported by current evidence. In fact, a real-world pharmacovigilance study comparing RET inhibitors (PMID 39372206) identifies **hypertension** as a recognized adverse event of this drug class. This suggests selpercatinib may *elevate* blood pressure rather than relieve pulmonary vascular hypertension, which is the opposite of the predicted therapeutic benefit.

Given this contradiction between the TxGNN prediction and the known safety signal, this candidate should be treated as a low-plausibility, data-driven artifact rather than a mechanistically grounded repurposing hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Cohort | Frontiers in Pharmacology | Real-world FAERS comparison of pralsetinib vs. selpercatinib adverse events; **hypertension identified as a class adverse effect**, not a treatment benefit |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Cohort | Therapeutic Advances in Medical Oncology | SIREN real-world analysis of selpercatinib in RET fusion-positive NSCLC (oncology efficacy/access program data; no relevance to pulmonary hypertension) |

Neither publication directly studies selpercatinib for pulmonary hypertension; both are oncology-context/pharmacovigilance sources.

---

## Taiwan Market Information

Selpercatinib currently has no marketing authorization on record — no licenses, brand names, or approved indication text are available in the Taiwan regulatory dataset (`market_status: 未上市`, `total_licenses: 0`).

---

## Cytotoxicity (Antineoplastic Drug)

Selpercatinib is classified as antineoplastic based on its established use in RET-altered malignancies (per literature context).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective RET kinase inhibitor) |
| Myelosuppression Risk | No data available — please refer to the package insert |
| Emetogenicity Classification | No data available — please refer to the package insert |
| Monitoring Items | Blood pressure monitoring recommended, given the class-associated hypertension signal reported in real-world pharmacovigilance data (PMID 39372206); otherwise refer to package insert for full monitoring requirements |
| Handling Protection | No specific handling data available — please refer to institutional hazardous/oral oncolytic drug handling policy |

---

## Safety Considerations

Formal safety data (key warnings, contraindications, TFDA label, DDI) are not currently available for this drug — please refer to the package insert for safety information once obtained.

**Notable literature signal:** A real-world pharmacovigilance study (PMID 39372206) reports hypertension as a recognized adverse event associated with selpercatinib. This should be factored into any safety evaluation for the pulmonary hypertension repurposing hypothesis, as it points toward a potential safety concern rather than a therapeutic benefit.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN's model score (L5, no actual supportive studies), and the only related literature identifies hypertension as an adverse event of this drug class — directly contradicting the hypothesis that selpercatinib treats pulmonary hypertension. There is currently no clinical trial evidence and no confirmed original-indication data from Taiwan regulatory sources.

**To proceed, the following is needed:**
- Confirmed MOA data from DrugBank (currently a blocking data gap)
- TFDA-equivalent label warnings/contraindications for formal S1 safety screening (currently a blocking data gap, DG001)
- Preclinical or mechanistic studies specifically linking RET inhibition to pulmonary vascular effects (direction of effect must be clarified — vasodilation vs. vasoconstriction)
- Ongoing monitoring for new clinical trials or case reports addressing this indication, given the currently contradictory safety signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

