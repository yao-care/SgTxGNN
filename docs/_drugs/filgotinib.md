---
layout: default
title: Filgotinib
parent: 僅模型預測 (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
---

# Filgotinib
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

# Filgotinib: From Rheumatoid Arthritis / Inflammatory Diseases to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Filgotinib is a selective JAK1 inhibitor approved in Europe and Japan for rheumatoid arthritis and ulcerative colitis, but currently not registered in Singapore.
The TxGNN model predicts it may have potential activity against **HER2 Positive Breast Carcinoma** (prediction score **98.88%**),
however there are currently **0 clinical trials** and **0 publications** directly supporting this repurposing direction — placing this firmly in the high-score, low-evidence category.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; approved for rheumatoid arthritis and ulcerative colitis in EU/Japan |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 98.88% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on publicly known information, Filgotinib is a highly selective JAK1 inhibitor (JAK1 > JAK2/JAK3/TYK2) that blocks the downstream JAK-STAT signalling cascade triggered by inflammatory cytokines including IL-6, IL-2, IL-4, IL-13, and IFN-γ. Its proven efficacy in rheumatoid arthritis and ulcerative colitis stems from suppressing the chronic inflammatory milieu driven by these cytokines.

The mechanistic rationale linking Filgotinib to HER2-positive breast carcinoma centres on the JAK1-STAT3 axis. HER2/ErbB2 receptor overexpression can constitutively activate JAK1-STAT3 downstream signalling; STAT3 in turn promotes tumour cell survival, angiogenesis, and immune evasion in the tumour microenvironment. Selective JAK1 inhibition could theoretically disrupt this cross-talk, reducing STAT3-mediated oncogenic transcription. There is also a rationale for synergy with existing HER2-targeted therapies (trastuzumab, pertuzumab) or immune checkpoint inhibitors.

However, this remains a purely mechanistic hypothesis. No preclinical (cell line / animal model) or clinical data in any breast cancer subtype have been published for Filgotinib. Multiple breast cancer subtypes (HER2+, PR−, normal-like) appear simultaneously in the top predictions, suggesting the model may be capturing broad breast cancer node proximity in the knowledge graph rather than subtype-specific JAK1 biology. This is a textbook **high-score, low-evidence** case that requires preclinical validation before any clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for HER2 positive breast carcinoma.

> **Note — Safety Signal in Adjacent Prediction:** For the Rank 2 indication (thrombocytopenia), 2 publications were retrieved. One case report (PMID [41458193](https://pubmed.ncbi.nlm.nih.gov/41458193/), *Clinical Case Reports*, 2026) documents **immune-mediated thrombocytopenia (ITP) occurring after initiating Filgotinib** in an ulcerative colitis patient — indicating thrombocytopenia is a potential **adverse event**, not a treatable indication. This is a meaningful pharmacovigilance signal and should be included in safety monitoring plans.

---

## Singapore Market Information

Filgotinib is not registered in Singapore. No authorisation records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Emerging Safety Signal:** A published case report (PMID 41458193, 2026) documents immune-mediated thrombocytopenia (ITP) associated with Filgotinib initiation in an ulcerative colitis patient. Platelet count monitoring is recommended during treatment, particularly in patients with active inflammatory disease.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (98.88%), but the evidence foundation is entirely absent — no clinical trials, no published preclinical studies, and no literature link Filgotinib to HER2-positive breast carcinoma. Additionally, Filgotinib is not registered in Singapore, meaning regulatory groundwork would also need to be established from scratch. The simultaneous appearance of multiple breast cancer subtypes in the top-10 predictions further raises the concern that this reflects knowledge graph topology rather than genuine mechanistic signal.

**To proceed, the following is needed:**

- **Preclinical validation**: HER2-overexpressing cell line studies and xenograft models with JAK1 inhibition to confirm anti-tumour activity before any clinical hypothesis can be formed
- **MOA data**: Obtain full DrugBank/pharmacological profile to formally document JAK1 selectivity profile and downstream effects (DG002 remediation)
- **Singapore regulatory pathway**: Since Filgotinib is unregistered in Singapore, a full NDA/marketing authorisation application would be required — evaluate feasibility against existing EU/Japan approvals (rheumatoid arthritis, UC) as a first step
- **Safety package**: Retrieve full TFDA/prescribing information for key warnings and contraindications (DG001 remediation); incorporate the emerging ITP pharmacovigilance signal
- **Differentiation analysis**: Evaluate whether JAK1 inhibition adds meaningful benefit over established HER2-targeted therapies (trastuzumab, pertuzumab, T-DM1, T-DXd) before committing to preclinical resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

