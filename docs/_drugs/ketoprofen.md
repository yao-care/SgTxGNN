---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 512
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

# Ketoprofen: From Pain and Inflammation to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ketoprofen is a non-steroidal anti-inflammatory drug (NSAID) belonging to the propionic acid class, widely used for managing pain, fever, and inflammatory conditions such as arthritis.
The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare genetic skeletal dysplasia caused by CDMP1 mutations.
Currently, **no clinical trials** and **no supporting publications** have been identified for this indication, placing the evidence at the lowest tier (L5 — model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain and inflammatory conditions (NSAID class; no formal Singapore registration on record) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 — Model prediction only, no clinical or preclinical studies identified |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known pharmacological class information, Ketoprofen is a propionic acid-derivative NSAID that works by inhibiting cyclooxygenase enzymes (COX-1 and COX-2), thereby reducing prostaglandin synthesis. Its efficacy in managing pain and inflammation in musculoskeletal and joint conditions has been established clinically.

Acromesomelic dysplasia, Hunter-Thompson type, is caused by loss-of-function mutations in the *CDMP1* gene (also known as *GDF5*), which encodes a bone morphogenetic protein critical for limb and joint development. The disease is structural and genetic in origin — resulting in disproportionate shortening of the forearms and lower legs — rather than primarily driven by inflammation or prostaglandin excess.

The mechanistic link between COX inhibition and this genetic skeletal dysplasia is therefore weak. The TxGNN model's high prediction score most likely reflects topological proximity in the knowledge graph between Ketoprofen and musculoskeletal/skeletal diseases, rather than a true biological pathway overlap. Ketoprofen might theoretically offer symptomatic pain relief for associated joint discomfort, but it cannot address the underlying gene defect. This prediction should be treated with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ketoprofen in acromesomelic dysplasia, Hunter-Thompson type.

---

## Literature Evidence

Currently no related literature available for Ketoprofen in acromesomelic dysplasia, Hunter-Thompson type.

---

## Singapore Market Information

Ketoprofen currently holds **no product registrations** in Singapore. The drug is not marketed in this jurisdiction based on available regulatory data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Supplementary: Most Biologically Plausible Prediction (Rank 8)

While the top-ranked TxGNN prediction (acromesomelic dysplasia) lacks biological plausibility, the dataset contains a mechanistically stronger candidate worth flagging for context:

**Spondyloarthropathy, susceptibility to** (TxGNN score: 99.86%, rank #8 overall)

Spondyloarthropathy (SpA) is driven by chronic inflammation of the spine and peripheral joints, with prostaglandin E2 playing a central role in both inflammation and bone erosion. NSAIDs including Ketoprofen are **recommended as first-line treatment** in EULAR and ACR guidelines for axial SpA. One supporting publication was identified:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20470931](https://pubmed.ncbi.nlm.nih.gov/20470931/) | 2010 | Review/Case Series | Ann Dermatol Venereol | General review of reactive arthritis (Fiessinger-Leroy-Reiter syndrome), an SpA subtype; does not directly evaluate Ketoprofen efficacy |

This indication reaches Evidence Level **L4** and may warrant further investigation as a repurposing candidate, pending direct clinical evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (acromesomelic dysplasia, Hunter-Thompson type) scores highly due to knowledge graph topology among musculoskeletal diseases, but the biological basis for COX inhibition in a monogenic skeletal developmental disorder is not supported. There are no clinical trials or publications to substantiate this prediction, and the drug is not registered in Singapore.

**To reconsider or proceed on any indication, the following is needed:**

- **MOA data**: Retrieve full Ketoprofen mechanism of action from DrugBank API (DG002 remediation) to support mechanistic analysis
- **Safety data**: Obtain TFDA/HSA package insert warnings and contraindications (DG001 — currently blocking Safety Stage S1 evaluation)
- **Redirect to stronger candidates**: Prioritise evaluation of Ketoprofen for **spondyloarthropathy** (rank 8), which has established NSAID-class mechanistic relevance and guideline-level support, over rare genetic dysplasias where the prediction likely reflects graph artefact
- **Regulatory pathway**: Assess feasibility of Singapore registration before any repurposing study, given current zero-registration status
- **Preclinical evidence**: For any rare disease target, commission a targeted literature review and, if warranted, in vitro/in vivo feasibility studies before clinical consideration

> ⚠️ *This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

