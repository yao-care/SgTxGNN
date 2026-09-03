---
layout: default
title: Methyldopa
parent: 僅模型預測 (L5)
nav_order: 655
evidence_level: L5
indication_count: 10
---

# Methyldopa
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

# Methyldopa: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Methyldopa (DrugBank DB00968) is a centrally acting antihypertensive, originally used to control hypertension through suppression of central sympathetic outflow. The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, but currently only **0 clinical trials** and **3 publications** support this specific direction, and the literature is topic-adjacent rather than drug-specific — evidence is preliminary and mechanism-based only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (inferred from mechanistic description; no Singapore registration record available to confirm the approved label wording) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 96.63% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for Methyldopa is flagged as a data gap in DrugBank (DG002, High severity), so the following is based on the repurposing-rationale analysis rather than a verified DrugBank MOA record and should be treated as provisional. Methyldopa is understood to act as a centrally acting α2-adrenergic agonist: it lowers central sympathetic outflow, which produces a systemic blood-pressure-lowering effect. This decades-old mechanism has an established, if dated, clinical safety track record in general hypertension management.

Malignant renovascular hypertension is a severe subtype of hypertension driven by renal artery pathology with markedly elevated sympathetic/renin-angiotensin activity. Because Methyldopa's central sympatholytic mechanism is not specific to any one hypertension subtype, it is theoretically applicable across severe/malignant hypertension presentations, including the renovascular form — which is the basis of the TxGNN prediction.

However, none of the three supporting publications directly studies Methyldopa in malignant renovascular hypertension. They are topic-adjacent: one concerns confounders of the aldosterone/renin ratio test (which happens to mention malignant/renovascular hypertension as a confounding condition), one is a case report of unrelated renovascular pathology (coarctation with neurofibromatosis), and one concerns other antihypertensive agents in hypertensive emergencies. The prediction is mechanistically plausible but lacks a direct evidentiary anchor.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22147655](https://pubmed.ncbi.nlm.nih.gov/22147655/) | 2012 | Review/Cohort | Hormone and Metabolic Research | Discusses factors that confound the aldosterone/renin ratio screening test for primary aldosteronism, noting that concomitant malignant or renovascular hypertension is one such confounder — not a study of Methyldopa itself |
| [6424340](https://pubmed.ncbi.nlm.nih.gov/6424340/) | 1984 | Case Report | Wiener Klinische Wochenschrift | Case of a 16-year-old girl with renovascular hypertension, aortic coarctation, and neurofibromatosis; describes disease presentation only, no treatment data on Methyldopa |
| [41307](https://pubmed.ncbi.nlm.nih.gov/41307/) | 1979 | Review | Revista de Medicina Interna... | Reviews sodium nitroprusside and diazoxide use in hypertensive emergencies; abstract unavailable, relevance to Methyldopa is indirect (different agents) |

---

## Singapore Market Information

Methyldopa is currently **not registered or marketed in Singapore** — 0 product authorizations are on file in this evidence pack. No dosage form, brand name, or approved-indication text is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are currently marked as data gaps in this evidence pack — notably, missing TFDA label warnings/contraindications is flagged as a **Blocking** data gap, DG001, since it prevents a proper S1 safety screen.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on Evidence Level L4 (mechanism-based reasoning only) with no clinical trials and no drug-specific literature directly studying Methyldopa in malignant renovascular hypertension. Combined with the drug's absence from the Singapore market and a Blocking-severity gap in safety-labeling data (DG001), there is not yet enough evidence to proceed past a research-question stage.

**To proceed, the following is needed:**
- TFDA/official label warnings and contraindications for Methyldopa (DG001, Blocking — required before any S1 safety evaluation)
- Confirmed mechanism-of-action record from DrugBank API (DG002, currently a data gap)
- Direct clinical or preclinical studies evaluating Methyldopa specifically in malignant/renovascular hypertension populations
- Confirmation of Singapore regulatory pathway options, given the drug is not currently marketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

