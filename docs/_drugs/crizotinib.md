---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: From ALK-Positive Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Crizotinib is an oral, ATP-competitive small-molecule inhibitor of the ALK, ROS1, and MET receptor tyrosine kinases, approved globally for treating ALK-positive and ROS1-positive non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Fibromatosis, Gingival**, with **0 clinical trials** and **0 publications** currently supporting this specific indication.
The high prediction score (99.81%) appears to reflect distant topological associations within the knowledge graph rather than established mechanistic evidence — this report also includes a consolidated overview of all 10 predicted indications from this multi-indication analysis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive / ROS1-positive NSCLC (not registered in Singapore; based on global regulatory approvals) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on literature cited throughout this analysis, Crizotinib is an ATP-competitive inhibitor of three receptor tyrosine kinases — ALK (Anaplastic Lymphoma Kinase), ROS1 (c-ros oncogene 1), and MET (Mesenchymal-Epithelial Transition factor). By blocking constitutive kinase activity caused by chromosomal rearrangements (such as EML4-ALK fusions or ROS1 gene fusions), Crizotinib inhibits tumor cell proliferation and survival. It was granted accelerated FDA approval in 2011 for EML4-ALK-positive NSCLC and subsequently extended to ROS1-rearranged NSCLC and MET exon 14–skipping mutations.

Gingival fibromatosis is a benign fibrous overgrowth condition predominantly driven by hereditary mutations in the *SOS1* gene and related connective tissue pathways. There is no known involvement of ALK rearrangements, ROS1 fusions, or MET amplification in its pathogenesis. The underlying disease biology is fundamentally distinct from the kinase-driven oncogenesis that Crizotinib targets.

The model's 99.81% prediction score most likely reflects remote topological connectivity within the biomedical knowledge graph — a recognized limitation of graph neural network-based repurposing tools, where high scores can arise from indirect network associations without direct biological support. This assessment is consistent with the mechanistic analysis in the evidence pack, which explicitly characterizes this prediction as a "distant topological association rather than molecular mechanistic plausibility." In the absence of any preclinical data, clinical trials, or supporting literature, this prediction represents a pure model output with no actionable clinical basis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Crizotinib is currently **not registered** in Singapore. No product authorizations have been recorded with the Health Sciences Authority (HSA). Clinicians requiring access would need to pursue an import license or the Special Access Route (SAR).

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — ALK/ROS1/MET tyrosine kinase inhibitor (oral small-molecule; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low to moderate (lymphopenia and neutropenia occasionally reported; significantly lower risk than conventional chemotherapy) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver function tests (ALT, AST, total bilirubin), renal function, ECG (QTc interval), pulmonary symptoms (ILD/pneumonitis surveillance), visual disturbances |
| Handling Protection | Follow institutional oral targeted therapy handling protocols; standard cytotoxic waste disposal required |

---

## Safety Considerations

> ⚠️ Formal safety data (package insert warnings and contraindications) is classified as a **Blocking Data Gap (DG001)**. Please refer to the complete package insert for safety information once obtained.

The following safety signals are identified from literature included in this evidence pack:

- **Hepatotoxicity**: Fatal fulminant liver failure has been reported after as few as 24 days of treatment initiation (PMID 26898609). ALT, AST, and bilirubin require close monitoring, particularly during the first 2–3 months of therapy.
- **Cardiotoxicity**: Simultaneous multiple cardiac events — including bradycardia, QT prolongation, ventricular arrhythmia, and pericarditis — have been documented (PMID 29717400). Baseline and periodic ECG monitoring is essential.
- **Interstitial Lung Disease (ILD) / Pneumonitis**: ILD is a recognized adverse event; successful drug rechallenge following resolution has been reported but requires careful clinical judgment and patient selection (PMID 24872405).
- **QT Prolongation**: A class effect shared among ALK/ROS1 TKIs (PMID 29413968); particular caution is required when co-administering with other QT-prolonging agents.
- **Skin Reactions**: Erythema multiforme has been reported (PMID 25994067).

---

## Multi-Indication Overview

This evidence pack encompasses 10 TxGNN-predicted indications for Crizotinib (candidate ID: TW-DB08865-multi). The following table provides a consolidated view across all predictions:

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation | Summary |
|------|-----------|-------------|----------------|----------------|---------|
| 1 | Fibromatosis, Gingival | 99.81% | L5 | Hold | No ALK/ROS1/MET pathway link; knowledge graph topology artifact |
| 2 | Fibroma of Lung | 99.75% | L5 | Hold | Rare benign mesenchymal tumor; no driver mutation evidence |
| 3 | Hamartoma of Lung | 99.75% | L4 | Hold | Only case report describes ALK-**negative** IMT — counter-evidence |
| 4 | Lung Hilum Carcinoma | 99.73% | L4 | Research Question | 2 case reports with confirmed ALK+ (68-month PFS) and ROS1+ (pCR) outcomes |
| 5 | Lung Benign Neoplasm | 99.73% | L3 | Research Question | 20 publications; primarily NSCLC data; ALK+ IMT sub-indication potentially actionable |
| 6 | Lung Germ Cell Tumor | 99.73% | L3 | Research Question | 4 clinical trials (incl. NCI-MATCH basket, n=6,452); 20 publications on ALK biology |
| 7 | Pulmonary Sulcus Neoplasm | 99.73% | L5 | Hold | ALK/ROS1 occurrence very low in Pancoast tumors (~1–3%); no direct evidence |
| 8 | IBMPFD† | 99.72% | L5 | Hold | VCP/p97 pathway disease; no known ALK/MET pathway intersection |
| 9 | Junctional Epidermolysis Bullosa | 99.70% | L5 | Hold | Structural basement membrane protein defect; no kinase pathway relevance |
| 10 | Leukomelanoderma Syndrome‡ | 99.69% | L4 | Hold | Novel RIPK1 inhibition (PMID 36534968, 2023) and megakaryopoiesis (PMID 40813622, 2025) signals found, but not disease-specific |

† Inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia (IBMPFD)
‡ Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome

**Most Biologically Viable Direction**: Indications at ranks 4–6 (lung hilum carcinoma, lung benign neoplasm, lung germ cell tumor) align with Crizotinib's established ALK/ROS1/MET mechanism and are supported by existing clinical and literature evidence. Clinical benefit is contingent on confirmed molecular biomarker status. In particular, ALK-positive inflammatory myofibroblastic tumor (IMT) — classifiable within "lung benign neoplasm" (rank 5) — may represent the highest-priority sub-indication given Phase II-level evidence for Crizotinib efficacy in this molecular subtype.

---

## Conclusion and Next Steps

**Decision: Hold** (for top-ranked prediction: Fibromatosis, Gingival)

**Rationale:**
The highest-ranked TxGNN prediction (fibromatosis, gingival) has no established mechanistic link to Crizotinib's known targets and is supported by neither clinical trials nor literature. Across all 10 predicted indications in this multi-analysis, lung-related malignancies with confirmed ALK/ROS1 molecular markers (ranks 4–6) represent the most credible repurposing directions, but none have sufficient evidence for immediate clinical implementation.

**To proceed, the following is needed:**

- **Resolve Blocking Data Gap (DG001)**: Obtain TFDA/HSA package insert to complete formal safety assessment (warnings and contraindications) — this is a prerequisite for any Stage 1 evaluation
- **Resolve High-Severity Data Gap (DG002)**: Obtain detailed MOA data from DrugBank to formally support mechanistic analysis and indication plausibility scoring
- **For lung-related indications (ranks 4–6)**: Molecular profiling data confirming ALK rearrangement, ROS1 fusion, or MET exon 14 skipping in the specific tumor subtype prior to any repurposing trial design
- **Singapore regulatory pathway**: Crizotinib is not registered with HSA; evaluate import license or Special Access Route (SAR) requirements before any local clinical investigation
- **Priority sub-indication review**: Commission a focused evaluation for ALK-positive inflammatory myofibroblastic tumor (IMT), which has the strongest existing biological rationale and Phase II-level evidence, and may merit a separate, dedicated evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

