---
layout: default
title: Dacarbazine
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
---

# Dacarbazine
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

# Dacarbazine: From Malignant Melanoma to Upper Aerodigestive Tract Neoplasm

## One-Sentence Summary

Dacarbazine (DTIC) is a classic DNA alkylating agent, established internationally as first-line treatment for malignant melanoma and as the "D" component of the ABVD regimen for Hodgkin's lymphoma — though it currently holds no product registration in Singapore.
The TxGNN model predicts it may be effective for **Upper Aerodigestive Tract Neoplasm**,
with **1 clinical trial** and **20 publications** identified for this direction; critically, however, the sole trial tested Dacarbazine's pharmacological analog Temozolomide — not Dacarbazine itself — and was **terminated early due to insufficient efficacy**, representing a meaningful negative signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malignant melanoma; Hodgkin's lymphoma (ABVD regimen) — established internationally, not currently registered in Singapore |
| Predicted New Indication | Upper Aerodigestive Tract Neoplasm |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L4 — Mechanistic / preclinical rationale only; no direct Dacarbazine trial data |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory database (data gap DG002). Based on established pharmacology, Dacarbazine is a triazene prodrug that undergoes hepatic metabolic activation to MTIC (methyltriazeno imidazole carboxamide), which methylates DNA at guanine O⁶ positions, causing replication errors, strand breaks, and ultimately cell death in proliferating tumor cells. The key pharmacological insight is that **Dacarbazine and Temozolomide share the identical active metabolite MTIC** — Temozolomide can be understood as the second-generation, orally bioavailable successor designed to overcome Dacarbazine's limitations in CNS penetration and route of administration.

Upper aerodigestive tract neoplasms span cancers of the oral cavity, pharynx, larynx, esophagus, and related sites. Within this broad category, specific subtypes carry biological rationale for MTIC-class agents: neuroendocrine tumors (e.g., medullary thyroid carcinoma, paraganglioma) have been treated with Dacarbazine-containing regimens historically, and angiosarcoma of the head and neck has been managed with CYVADIC (a combination containing DTIC). The TxGNN model likely generalizes from these precedents via knowledge-graph connectivity.

However, the prediction faces a critical counterfactual. The only identified clinical trial in this indication space (NCT00423150) enrolled patients with advanced aerodigestive tract cancers specifically selected for MGMT promoter methylation — the biomarker that predicts sensitivity to MTIC — and was **terminated early because even this enriched population showed insufficient response to Temozolomide**. Since Temozolomide is the pharmacodynamically superior agent (better oral bioavailability, more predictable CNS exposure), this negative result casts serious doubt on the prospects for Dacarbazine in this broad indication. The TxGNN high score most likely reflects mechanistic topology in the knowledge graph rather than validated clinical benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00423150](https://clinicaltrials.gov/study/NCT00423150) | Phase 2 | Terminated | 86 | Tested **Temozolomide** (not Dacarbazine) in MGMT-methylation-selected patients with advanced colorectal, NSCLC, head and neck, and esophageal cancers; terminated early due to insufficient efficacy — constitutes an indirect negative signal for MTIC-class agents across this indication |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [23443801](https://pubmed.ncbi.nlm.nih.gov/23443801/) | 2013 | Phase II | Mol Cancer Ther | Published results of NCT00423150: Temozolomide in MGMT-methylated aerodigestive tract cancers; response rates were insufficient to support continued development |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Prospective Clinical Trial | Ann Oncol | **Direct Dacarbazine evidence**: DTIC + 5-FU combination in advanced medullary thyroid carcinoma (a neuroendocrine tumor of the aerodigestive region); explored cytotoxic activity in this chemotherapy-resistant neuroendocrine subtype |
| [8346929](https://pubmed.ncbi.nlm.nih.gov/8346929/) | 1993 | Case Series | Gan to Kagaku Ryoho | CYVADIC regimen (cyclophosphamide + vincristine + doxorubicin + **DTIC**) in head-and-neck angiosarcoma; documents historical use of Dacarbazine-containing combinations in rare aerodigestive vascular tumors |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | Case Series | Ear Nose Throat J | Clinicopathological and genetic features of malignant paragangliomas of the head and neck; neuroendocrine subtype where DTIC-based regimens have been considered |
| [11163509](https://pubmed.ncbi.nlm.nih.gov/11163509/) | 2001 | Retrospective Study | Int J Radiat Oncol Biol Phys | Esthesioneuroblastoma (rare intranasal tumor of the upper aerodigestive tract) treated with radiotherapy; provides anatomical and clinical context for this rare neoplasm category |
| [34705104](https://pubmed.ncbi.nlm.nih.gov/34705104/) | 2022 | Epidemiological Study | J Cancer Res Clin Oncol | Global burden of EBV-related cancers including nasopharyngeal and head-and-neck malignancies; epidemiological background for aerodigestive neoplasms |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Review | Clin Oncol | Medullary thyroid carcinoma: neuroendocrine tumor subtype of the aerodigestive region for which DTIC + 5-FU has been evaluated |

---

## Singapore Market Information

Dacarbazine currently holds **no product registrations** with the Health Sciences Authority (HSA) of Singapore. There is no local approved indication text, licensed dosage form, or Singapore package insert available for reference. Clinicians would need to rely on international labeling (e.g., EMA, FDA, or TGA-approved SmPCs) for prescribing guidance under an unregistered drug framework.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Alkylating agent (Triazene class); prodrug requiring hepatic CYP1A2-mediated activation to MTIC |
| Myelosuppression Risk | High — leukopenia and thrombocytopenia are dose-limiting toxicities; blood count nadir typically occurs 3–4 weeks after administration with slow recovery |
| Emetogenicity Classification | High — Dacarbazine is classified as a highly emetogenic agent; prophylactic antiemetic therapy (5-HT₃ antagonist + NK₁ antagonist + dexamethasone) is required |
| Monitoring Items | Complete blood count with differential (before each cycle and at nadir), liver function tests (Dacarbazine is hepatically activated; hepatotoxicity including veno-occlusive disease reported), renal function, monitoring for febrile neutropenia |
| Handling Protection | Must be handled following cytotoxic drug handling regulations; photosensitive — intravenous solution must be protected from light during preparation and infusion |

---

## Safety Considerations

No Singapore-specific safety data is available for Dacarbazine (unregistered drug, data gap DG001 classified as Blocking severity). International prescribing information should be consulted directly. Two specific safety alerts commonly associated with Dacarbazine internationally include hepatic veno-occlusive disease (rare but potentially fatal) and severe myelosuppression requiring treatment delays or dose reductions.

Please refer to the current international package insert (e.g., FDA label or EMA SmPC) for complete warnings, contraindications, and drug interaction information before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole identifiable clinical trial in this indication space tested Temozolomide — the pharmacodynamically superior MTIC-class analog — in MGMT-biomarker-selected patients and was terminated early for insufficient efficacy. Dacarbazine has no direct clinical trial data in upper aerodigestive tract neoplasms, and the mechanistic evidence alone (L4) is insufficient to justify clinical development in this broad indication category. The TxGNN high score (99.26%) likely reflects graph-structural proximity rather than validated efficacy.

**To proceed, the following is needed:**

- **Resolve Blocking data gap (DG001)**: Obtain international package insert (FDA/EMA) to document contraindications, key warnings, and known drug interactions before any clinical safety assessment can proceed
- **Resolve High-severity data gap (DG002)**: Retrieve full MOA documentation from DrugBank API to support mechanistic link analysis
- **Narrow the target population**: Rather than pursuing the broad "upper aerodigestive tract neoplasm" category, focus analysis on specific subtypes with pre-existing Dacarbazine evidence — particularly **head and neck mucosal melanoma**, **medullary thyroid carcinoma**, and **head and neck angiosarcoma** — each of which has independent historical data supporting DTIC use
- **Interpret the Temozolomide negative trial**: Formally assess whether NCT00423150's early termination applies mechanistically to Dacarbazine (likely yes, given shared active metabolite) or whether patient selection differences could create a residual opportunity
- **Evaluate alternative indications with stronger evidence**: The TxGNN candidate list includes **primary pulmonary lymphoma** (Rank 3, L2 evidence, Dacarbazine as part of ABVD for Hodgkin's lymphoma — a well-established regimen) and **head and neck cancer** subtypes (Rank 7, L3 evidence with direct DTIC trial data); these carry stronger evidence bases and may be more productive evaluation priorities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

