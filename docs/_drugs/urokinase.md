---
layout: default
title: Urokinase
parent: 僅模型預測 (L5)
nav_order: 1035
evidence_level: L5
indication_count: 10
---

# Urokinase
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

# Urokinase: From Unknown Original Indication to Primary Release Disorder of Platelets

## One-Sentence Summary

> Urokinase's original approved indication cannot be confirmed from available Singapore registry data, as the product is not currently marketed there.
> The TxGNN model's top prediction is **Primary Release Disorder of Platelets**,
> but supporting evidence is thin and mechanistically contradictory — only **1 loosely related clinical trial** and **3 tangential publications** are currently available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Singapore product license on file, and no original indication data provided |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for urokinase is not available in this evidence pack, and no confirmed original indication is on record for the Singapore market since the product is not currently registered here. Based on general pharmacological knowledge, urokinase is a plasminogen activator used to promote thrombolysis — its established clinical role is dissolving existing clots, not modulating platelet granule release.

The top-ranked predicted indication, "primary release disorder of platelets," is a platelet secretion defect rather than a thrombotic condition. The evidence review flags this as a likely direction mismatch: a thrombolytic agent would not be expected to treat a platelet release/function disorder, and the supporting literature (coronary thrombosis pathophysiology, u-PA levels in leukemia-associated hemorrhagic syndrome) does not directly address this specific disease. This is consistent with the L5 evidence level assigned — a model-only prediction without direct supporting studies.

Notably, several other candidates in this batch share the same mechanistic problem — bleeding disorders (Glanzmann thrombasthenia, pseudo-von Willebrand disease, constitutional thrombocytopenia, Scott syndrome) where a thrombolytic would be expected to worsen rather than treat bleeding risk. The one candidate with more substantive mechanistic and case-level evidence is **thrombotic thrombocytopenic purpura (rank 4)**, which includes historical case reports of urokinase use and literature on plasmin-mediated ADAMTS13/VWF interactions — though even this signal is mechanistically two-edged (plasmin can also degrade ADAMTS13 and fibrinogen, potentially worsening bleeding), and current standard-of-care (plasma exchange, caplacizumab) does not include thrombolytics. All ten candidates in this batch were assessed as Hold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06101667](https://clinicaltrials.gov/study/NCT06101667) | NA | Recruiting | 224 | Evaluates endovascular recanalization vs. medical management for acute basilar artery occlusion (24–72h window); relevance graded C — not directly related to platelet release disorder |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32089086](https://pubmed.ncbi.nlm.nih.gov/32089086/) | 2020 | Review | Circulation Research | Reviews cholesterol crystal embolism pathophysiology and treatment targets; not specific to platelet release disorder |
| [9173723](https://pubmed.ncbi.nlm.nih.gov/9173723/) | 1997 | Review | Zeitschrift für Kardiologie | Reviews coronary thrombosis and antithrombotic interventions; unrelated to platelet release disorder |
| [1414164](https://pubmed.ncbi.nlm.nih.gov/1414164/) | 1992 | Cohort | Acta Haematologica | Found elevated plasma u-PA levels in acute non-lymphoblastic leukemia patients with hemorrhagic syndrome; only an indirect association |

---

## Singapore Market Information

Urokinase is currently not registered or marketed in Singapore. No license records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug interaction data are currently available for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication shows a mechanistic mismatch (thrombolytic agent vs. platelet release disorder) with only indirect, low-relevance supporting evidence (L5). The drug is not marketed in Singapore, and core safety data (label warnings, contraindications, confirmed MOA) are unavailable, blocking any safety pre-assessment.

**To proceed, the following is needed:**
- HSA/product label data confirming urokinase's approved indications, warnings, and contraindications (currently a blocking data gap)
- Confirmed mechanism of action from DrugBank or equivalent source
- If pursuing further, re-scope evaluation toward the more mechanistically plausible candidate — thrombotic thrombocytopenic purpura (rank 4, L4/S1) — rather than the top-ranked platelet release disorder prediction
- Independent expert review of the plasmin/ADAMTS13 mechanistic trade-off before considering any indication involving bleeding-risk disorders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

