---
layout: default
title: Bezafibrate
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
---

# Bezafibrate
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

# Bezafibrate: From Dyslipidemia to Hypoalphalipoproteinemia

## One-Sentence Summary

Bezafibrate is a fibrate-class lipid-lowering agent widely used for dyslipidemia and hypertriglyceridemia, acting primarily as a PPARα agonist to lower triglycerides and raise HDL cholesterol.
The TxGNN model predicts it may be effective for **Hypoalphalipoproteinemia** (isolated low HDL syndrome),
with **0 clinical trials** and **3 publications** currently supporting this direction. The mechanistic rationale is strong, but available clinical evidence remains limited to small, early-era observational studies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Dyslipidemia / Hypertriglyceridemia (fibrate class; no Singapore registration on record) |
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 98.54% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, bezafibrate is a pan-PPAR agonist (primarily PPARα) belonging to the fibrate class. PPARα activation upregulates ApoA-I and ApoA-II gene expression, promoting HDL particle assembly and strengthening reverse cholesterol transport (RCT). This is the most pharmacologically direct pathway for raising plasma HDL-C levels among available lipid-modifying agents.

Hypoalphalipoproteinemia is defined as isolated low HDL cholesterol (below 35–40 mg/dL) and is a well-established independent cardiovascular risk factor associated with impaired reverse cholesterol transport and endothelial dysfunction. Because bezafibrate's PPARα-driven mechanism directly addresses the core pathology of this condition — insufficient ApoA-I–mediated HDL production — the TxGNN model's high-confidence prediction (98.54%) is mechanistically coherent and not surprising.

Crucially, the most relevant piece of literature (PMID 11483875, 2001) directly tests bezafibrate in patients with both hypoalphalipoproteinemia and coronary artery disease, reporting improved endothelial function as HDL-C levels were raised. This constitutes direct clinical validation of the predicted indication. However, all three supporting publications predate 2002, involve small patient numbers, and none meet the threshold for controlled trial evidence. No clinical trials have been registered for this specific indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bezafibrate in hypoalphalipoproteinemia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11483875](https://pubmed.ncbi.nlm.nih.gov/11483875/) | 2001 | Prospective Clinical Study | Journal of Cardiovascular Pharmacology | Bezafibrate raised HDL-C and significantly improved endothelial dysfunction in patients with isolated low HDL (< 0.91 mM) and coronary artery disease |
| [1575823](https://pubmed.ncbi.nlm.nih.gov/1575823/) | 1992 | Observational Cross-sectional | Atherosclerosis | Characterized the prevalence and TG–HDL relationship in hypertriglyceridemic patients with primary hypoalphalipoproteinemia; established the epidemiological link |
| [7567762](https://pubmed.ncbi.nlm.nih.gov/7567762/) | 1995 | Case Series | Postgraduate Medical Journal | Reported two cases of iatrogenic profound hypoalphalipoproteinemia from probucol + bezafibrate combination; confirmed that bezafibrate monotherapy raises HDL while co-administration with probucol paradoxically depletes ApoA-I |

---

## Singapore Market Information

Bezafibrate currently has **no registered products in Singapore**. There are no HSA authorizations or licensed products on record. This means any clinical use or repurposing pathway in Singapore would require a new drug application or named-patient/compassionate use arrangement.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Singapore HSA package insert data and TFDA warning/contraindication data were not retrieved in this evidence pack (Data Gap DG001). As a fibrate-class drug, bezafibrate carries well-known class-level risks including myopathy risk with concomitant statin use, potentiation of anticoagulant effect (particularly warfarin), and renal dose adjustment requirements — these should be verified from the full prescribing information before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a strong and direct mechanistic basis, the available clinical evidence for bezafibrate in hypoalphalipoproteinemia consists entirely of small observational studies and case reports from 1992–2001, with no registered clinical trials and no RCT-level data specific to this indication. Evidence Level L3 is insufficient to advance without additional prospective data.

**To proceed, the following is needed:**

- **MOA verification**: Retrieve complete bezafibrate DrugBank entry to formally document PPARα mechanism, toxicity profile, and pharmacokinetics
- **Safety package**: Obtain HSA/TFDA package insert to fill the blocking Data Gap (DG001) covering key warnings and contraindications — currently prevents entry into formal safety screening (Stage S1)
- **Drug interaction profile**: Confirm DDI risk with statins (rhabdomyolysis), warfarin (anticoagulation potentiation), and other co-medications relevant to cardiovascular patients
- **Clinical trial feasibility**: Design or identify a prospective pilot study or registry specifically targeting isolated low HDL patients treated with bezafibrate, with endothelial function or MACE endpoints
- **Competitive landscape review**: Evaluate unmet need against current standard-of-care options (niacin, CETP inhibitors, high-intensity statins) to determine whether bezafibrate offers a meaningful advantage in this indication
- **Updated literature search**: Conduct a systematic search for post-2001 publications, particularly given advances in understanding of HDL functionality vs. quantity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

