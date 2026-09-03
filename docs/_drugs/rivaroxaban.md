---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 869
evidence_level: L5
indication_count: 10
---

# Rivaroxaban
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

# Rivaroxaban: From Anticoagulation Therapy to Rheumatoid Arthritis

## One-Sentence Summary

> Rivaroxaban is a Factor Xa inhibitor originally used for anticoagulation — treating and preventing venous thromboembolism (DVT/PE) and reducing stroke risk in atrial fibrillation.
> The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but this prediction is currently supported by **0 directly relevant clinical trials** and only **3 tangential publications**, none of which test rivaroxaban as an RA treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anticoagulation therapy (VTE treatment/prevention, stroke prevention in atrial fibrillation) — inferred from supporting literature context; not present in Singapore regulatory records |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available for this candidate. Based on the supporting evidence in this pack, Rivaroxaban is consistently described as a direct Factor Xa inhibitor used for anticoagulation — its efficacy in preventing and treating venous thromboembolism and reducing stroke risk in atrial fibrillation is well established in the cited literature (e.g., DVT/PE management, DOAC adherence studies).

The proposed link to rheumatoid arthritis is indirect. Chronic inflammation in RA is known to activate the coagulation cascade, raising patients' background thrombotic risk — one literature entry examines thrombin generation assays in autoimmune disease as a way to assess this hypercoagulable state. In theory, a Factor Xa inhibitor could reduce thrombotic complications in RA patients, but nothing in the current evidence shows any effect on the underlying autoimmune/inflammatory joint disease itself.

The high TxGNN score most likely reflects an indirect knowledge-graph connection — RA's association with thrombotic comorbidity — rather than a direct pharmacological mechanism linking Factor Xa inhibition to RA disease control. This should be treated as a hypothesis-generating signal only, not evidence of therapeutic benefit for RA.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | General review of DVT/PE diagnosis and treatment; establishes rivaroxaban's role in VTE management, no RA content |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Cohort/Lab study | La Revue de médecine interne | Thrombin generation assay used to assess hypercoagulability in autoimmune disease; supports the comorbidity rationale but does not test rivaroxaban in RA |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS ONE | Real-world adherence comparison of rivaroxaban vs apixaban in atrial fibrillation patients; unrelated to RA |

## Singapore Market Information

Rivaroxaban currently has no registered license in Singapore (0 authorizations on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (rheumatoid arthritis) rests only on an indirect comorbidity rationale — RA-associated hypercoagulability — with no clinical trials and no literature testing rivaroxaban as an RA therapy. The drug is also unregistered in Singapore, so there is no local regulatory or safety baseline to build on.

**To proceed, the following is needed:**
- Structured mechanism-of-action (MOA) data for rivaroxaban to formally support or refute the RA rationale
- HSA/TFDA-equivalent safety labeling (warnings, contraindications, DDI data) — currently a blocking data gap
- A study design that distinguishes "reduces RA-associated thrombotic risk" from "modifies RA disease activity," since these are pharmacologically very different claims
- Re-screening of lower-ranked candidates (e.g., HIV infection, L4/S1) for similar rigor before any further prioritization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

