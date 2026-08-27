---
layout: default
title: Glycopyrronium
parent: 僅模型預測 (L5)
nav_order: 484
evidence_level: L5
indication_count: 10
---

# Glycopyrronium
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

# Glycopyrronium: From Hyperhidrosis/Sialorrhea to Irritable Bowel Syndrome

## One-Sentence Summary

Glycopyrronium is a peripheral antimuscarinic (anticholinergic) agent approved globally for conditions such as primary hyperhidrosis and sialorrhea, though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**, with **0 clinical trials** and **1 mechanistic publication** currently available to support this direction.
Evidence remains at the preclinical/mechanistic stage (L4), and substantial clinical investigation is required before this repurposing direction can be considered viable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 98.84% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this dataset. Based on established pharmacological knowledge, glycopyrronium is a quaternary ammonium compound that antagonises muscarinic M2 and M3 receptors peripherally. Because of its quaternary ammonium structure, it does not readily cross the blood-brain barrier, making its primary actions peripheral — on smooth muscle, secretory glands, the heart, and the bladder.

In the gastrointestinal tract, M3 receptor stimulation drives smooth muscle contraction and mucosal secretion. Blocking these receptors can reduce bowel spasm and secretory overactivity — the two core drivers of abdominal pain and altered bowel habits in IBS. This mechanism mirrors that of drugs already licensed for IBS: hyoscine butylbromide (Buscopan) and dicyclomine are both anticholinergics indicated for IBS-related spasm. Glycopyrronium shares the same receptor target, giving its TxGNN prediction clear biological plausibility.

However, analogy to a drug class does not substitute for direct clinical evidence. The current dataset contains no clinical trials and only one animal/mechanistic study involving glycopyrronium and IBS. Until prospective human data are generated, this prediction remains a mechanistically sound hypothesis awaiting clinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9696463](https://pubmed.ncbi.nlm.nih.gov/9696463/) | 1998 | Animal/Mechanistic | *Pain* | Investigated the effects of monoamine reuptake inhibitors on mechanosensitive pelvic nerve afferents innervating the rat colon; provides mechanistic context for cholinergic modulation of colonic visceral afferents relevant to IBS-associated pain pathways |

---

## Singapore Market Information

Glycopyrronium is not currently registered in Singapore. No Health Sciences Authority (HSA) product authorisations were identified in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between glycopyrronium's peripheral M3 receptor antagonism and IBS symptom relief is biologically plausible and supported by analogy to approved class members (hyoscine, dicyclomine), but current evidence consists solely of a 1998 rat model study with no human clinical trial data — placing this at L4 and below the threshold for a repurposing recommendation.

---

### Note on Higher-Priority Candidate in This Evidence Pack

Reviewers should be aware that **Autonomic Nervous System Disease (Rank 8, TxGNN score 95.55%)** presents materially stronger evidence within this same evidence pack:

- **2 Phase 4 clinical trials** directly measuring glycopyrronium's effects on cardiac autonomic function in COPD patients (NCT02872090: completed; NCT03662711: terminated early)
- **18 publications** spanning systematic reviews, pharmacotherapy guidelines, and clinical physiology studies
- **Evidence Level: L3** | **Recommendation: Proceed with Guardrails**

Glycopyrronium already carries globally approved indications spanning autonomic nervous system targets (hyperhidrosis via sympathetic cholinergic fibres; sialorrhea in Parkinson's disease dysautonomia), making this a more actionable repurposing pathway for Singapore evaluation.

---

**To proceed with IBS investigation, the following is needed:**

- Targeted systematic review of IBS clinical trials for the anticholinergic drug class (hyoscine, dicyclomine) to establish indirect class-level evidence
- Retrieval and analysis of the full glycopyrronium package insert to document contraindications and warnings (currently unavailable)
- Mechanism of action documentation from DrugBank API (DB00986) to formally confirm receptor binding profile
- Evaluation of appropriate oral or enteric formulation routes for IBS (no formulation data currently available for Singapore)
- Phase 2 proof-of-concept trial design if class-level evidence review is positive
- Regulatory pre-submission meeting with HSA to assess pathway for a new indication in an unregistered drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

