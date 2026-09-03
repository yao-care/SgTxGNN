---
layout: default
title: Pyridostigmine
parent: 僅模型預測 (L5)
nav_order: 834
evidence_level: L5
indication_count: 10
---

# Pyridostigmine
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

# Pyridostigmine: From Myasthenia Gravis to Myasthenia Gravis with Thymus Hyperplasia

## One-Sentence Summary

Pyridostigmine is a well-established acetylcholinesterase inhibitor used as standard symptomatic therapy for myasthenia gravis (MG) — this is confirmed by the drug's own literature evidence base, though formal original-indication and MOA records are currently missing from the Evidence Pack (data gaps). The TxGNN model's top prediction, **Myasthenia Gravis with Thymus Hyperplasia**, is a clinical subtype of the disease pyridostigmine already treats, rather than a genuinely new disease area. Supporting evidence is limited to **3 publications** (no dedicated clinical trials) for this specific subtype.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Singapore regulatory data (data gap); literature evidence indicates established use in generalized myasthenia gravis |
| Predicted New Indication | Myasthenia Gravis with Thymus Hyperplasia |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L3 (retrospective observational study + reviews/case reports) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on the literature captured in this Evidence Pack, pyridostigmine is repeatedly described as a standard acetylcholinesterase inhibitor used in the symptomatic treatment of myasthenia gravis — for example, one review notes that "standard medical therapy consists of symptomatic treatment with acetylcholinesterase inhibitors (e.g., pyridostigmine)" (PMID 38212553), and pharmacokinetic studies directly measure its clinical effect in MG patients (PMID 199393, PMID 2166138).

Myasthenia Gravis with Thymus Hyperplasia is not a distinct disease but a well-recognized clinical phenotype of generalized MG, associated with thymic pathology and often managed with thymectomy alongside anticholinesterase therapy (PMID 25683765). Mechanistically, pyridostigmine's inhibition of acetylcholinesterase at the neuromuscular junction is disease-subtype agnostic within MG — it improves neuromuscular transmission regardless of whether thymic hyperplasia is present.

Importantly, this means the TxGNN prediction largely reflects an **already-established use pattern** rather than a novel repurposing opportunity. The value of this signal lies in identifying an underserved MG subtype/phenotype for more targeted evidence generation, not in discovering a new therapeutic area.

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific predicted indication.

*(Note: broader MG-related trials exist under other TxGNN-ranked predictions, e.g., NCT05095103 and NCT04101578 under "autoimmune disease of peripheral nervous system," but none are indexed specifically for the thymus hyperplasia subtype.)*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25683765](https://pubmed.ncbi.nlm.nih.gov/25683765/) | 2015 | Observational (retrospective cohort) | Journal of Neurology | 2-year outcomes of thymectomy in 39 patients with non-thymomatous late-onset generalized MG; anticholinesterase therapy continued alongside surgery |
| [34225443](https://pubmed.ncbi.nlm.nih.gov/34225443/) | 2021 | Review | Molecular Medicine Reports | Reviews MG pathology, autoimmunity, and phenotypic heterogeneity, including thymic hyperplasia-associated presentations |
| [18053719](https://pubmed.ncbi.nlm.nih.gov/18053719/) | 2008 | Case report | Neuromuscular Disorders | Describes dropped head syndrome as a prominent feature in MuSK-positive MG with thymus hyperplasia |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is a recognized clinical subtype of a disease pyridostigmine already treats, so novelty is low; combined with the absence of dedicated clinical trials for this subtype, a blocking safety data gap (no TFDA/HSA label warnings or contraindications available), and zero market presence in Singapore, the evidence does not yet support proceeding.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications, DDI) — currently blocking (DG001)
- Confirmed mechanism of action and formal original-indication record from DrugBank — currently missing (DG002)
- Subtype-specific clinical evidence (e.g., outcomes in thymus hyperplasia-associated MG specifically, beyond general MG data) to justify this as a distinct evaluation target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

