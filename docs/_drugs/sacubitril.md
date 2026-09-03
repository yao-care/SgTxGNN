---
layout: default
title: Sacubitril
parent: 僅模型預測 (L5)
nav_order: 882
evidence_level: L5
indication_count: 10
---

# Sacubitril
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

# Sacubitril: From Heart Failure to Diabetic Nephropathy

## One-Sentence Summary

> Sacubitril is the neprilysin-inhibitor component of sacubitril/valsartan (ARNI, Entresto), a therapy originally developed and approved for heart failure. Among the TxGNN model's predictions, **Diabetic Nephropathy** is the highest-ranked candidate with a coherent mechanistic rationale, supported by **2 clinical trials** and **18 publications** — including a secondary analysis of the pivotal PARADIGM-HF RCT.

**Note on candidate selection:** TxGNN's single highest-scoring prediction (brain small vessel disease with ocular anomalies, score 99.58%) was explicitly flagged in the evidence pack's own rationale as a likely embedding-similarity false positive with no biological plausibility or supporting literature. This report therefore focuses on **Diabetic Nephropathy (rank 3)** — the top candidate with genuine mechanistic coherence, clinical trial activity, and literature support — as the actionable finding for decision-making.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heart failure (as sacubitril/valsartan, ARNI) — formal indication text not available in this evidence pack (data gap) |
| Predicted New Indication | Diabetic Nephropathy |
| TxGNN Prediction Score | 99.50% (rank 6456) |
| Evidence Level | L2 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed DrugBank mechanism-of-action data is not available for sacubitril (flagged as a High-severity data gap in this evidence pack). Based on available evidence, sacubitril is the prodrug component of sacubitril/valsartan (ARNI), which inhibits neprilysin — the enzyme responsible for degrading natriuretic peptides (ANP/BNP/CNP). Reduced degradation increases natriuretic peptide bioavailability, producing vasodilation, natriuresis, and anti-fibrotic effects; combined with valsartan's angiotensin receptor blockade, the combination provides dual RAAS blockade.

This mechanism is a direct pharmacological extension of the drug's approved use in heart failure rather than a cross-system leap. Diabetic nephropathy shares key pathophysiology with heart failure — glomerular hypertension, RAAS overactivation, and fibrotic remodeling — all targets addressed by neprilysin inhibition plus angiotensin receptor blockade. Preclinical models (rat and mouse diabetic nephropathy) consistently show sacubitril/valsartan reduces glomerulosclerosis, oxidative stress, and proteinuria beyond valsartan alone, and a secondary analysis of the PARADIGM-HF trial (PMID 29661699) found renoprotective signals in patients with type 2 diabetes. This convergence of mechanism, preclinical data, and post-hoc RCT evidence is why the model's prediction is biologically credible — in contrast to several other top-ranked but mechanistically unsupported predictions in this evidence pack (e.g., rare ocular/skeletal syndromes, hemoglobinopathies).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06501651](https://clinicaltrials.gov/study/NCT06501651) | Phase 4 | Not yet recruiting | 297 | Randomized, controlled, multicenter study comparing sacubitril/valsartan vs. valsartan in patients with mild-to-moderate essential hypertension and type 2 diabetic nephropathy over a 12-week treatment period (2:1 randomization). |
| [NCT04735354](https://clinicaltrials.gov/study/NCT04735354) | N/A | Completed | 268 | Real-world retrospective EMR study of sacubitril/valsartan in HFrEF patients in India; not primarily focused on diabetic nephropathy but captures an overlapping diabetic population. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29661699](https://pubmed.ncbi.nlm.nih.gov/29661699/) | 2018 | Secondary analysis of RCT (PARADIGM-HF) | Lancet Diabetes Endocrinol | Neprilysin inhibition assessed for effects on renal function course in patients with type 2 diabetes and chronic heart failure already on maximal RAAS inhibitor doses. |
| [40416927](https://pubmed.ncbi.nlm.nih.gov/40416927/) | 2025 | Clinical cohort (BOLD-MRI) | Diabetes Metab Syndr Obes | Imaging-based evaluation of sacubitril/valsartan's renal protective effects in type 2 diabetic patients. |
| [37549515](https://pubmed.ncbi.nlm.nih.gov/37549515/) | 2023 | Clinical study | Int Immunopharmacol | Sacubitril/valsartan combined with nifedipine improved renal function in diabetic nephropathy patients with hypertension. |
| [37625003](https://pubmed.ncbi.nlm.nih.gov/37625003/) | 2023 | Review | Diabetes Care | Updates on pillars of diabetic kidney disease therapy, including RAAS blockade and neprilysin inhibition pathways. |
| [34734359](https://pubmed.ncbi.nlm.nih.gov/34734359/) | 2023 | Review | Heart Fail Rev | Disease-modifying drug use in diabetic patients with HFrEF. |
| [34441977](https://pubmed.ncbi.nlm.nih.gov/34441977/) | 2021 | Review | J Clin Med | Diabetes mellitus and heart failure, including diabetic nephropathy comorbidity. |
| [35165832](https://pubmed.ncbi.nlm.nih.gov/35165832/) | 2022 | Review | Curr Hypertens Rep | Emerging drugs to reduce blood pressure and mitigate hypertensive target organ damage, including diabetic kidney disease. |
| [35975848](https://pubmed.ncbi.nlm.nih.gov/35975848/) | 2023 | Review | Curr Diabetes Rev | Diabetes and cardiorenal complications; existing therapies and novel combinations. |
| [34431635](https://pubmed.ncbi.nlm.nih.gov/34431635/) | 2021 | Review | Rev Med Suisse | Potential role of sacubitril/valsartan combination in type 2 diabetes. |
| [35992034](https://pubmed.ncbi.nlm.nih.gov/35992034/) | 2022 | Animal study (rat model) | Diabetes Metab Syndr Obes | Sacubitril/valsartan improved progression of early diabetic nephropathy via inhibition of the NLRP3 inflammasome pathway. |

---

## Singapore Market Information

Sacubitril is currently **not marketed** in Singapore under this evidence pack, and no license records are available (0 registrations).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (flagged as a Blocking data gap — DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Diabetic nephropathy is a mechanistically coherent extension of sacubitril/valsartan's approved heart-failure indication, supported by human RCT-derived data (PARADIGM-HF secondary analysis), an active Phase 4 RCT, a clinical imaging cohort study, and consistent preclinical models — meeting the L2 evidence threshold. However, no dedicated, completed RCT with diabetic nephropathy as the primary endpoint yet exists, and the drug is not currently registered in Singapore, so guardrails are warranted before clinical adoption.

**To proceed, the following is needed:**
- Full DrugBank mechanism-of-action data (DG002) to formally validate the mechanistic rationale
- TFDA/HSA package insert warnings, contraindications, and DDI data (DG001) — currently blocking safety review (S1)
- Results from the ongoing Phase 4 Hyper-Save Study (NCT06501651)
- A dedicated, adequately powered RCT with diabetic nephropathy (renal outcomes) as the primary endpoint
- Formal regulatory pathway assessment for Singapore market entry, since the drug is currently unregistered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

