---
layout: default
title: Blinatumomab
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Blinatumomab
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

# Blinatumomab: From B-Cell Precursor Acute Lymphoblastic Leukemia to Primary Release Disorder of Platelets

## One-Sentence Summary

Blinatumomab (Blincyto) is a CD19×CD3 bispecific T-cell engager (BiTE) antibody established for the treatment of relapsed/refractory B-cell precursor Acute Lymphoblastic Leukemia (ALL). The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, but the 2 identified clinical trials both address B-ALL treatment rather than platelet function — neither is designed to evaluate the predicted indication. This prediction is currently assessed as a knowledge graph false positive with no supporting biological rationale or direct clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed/Refractory B-Cell Precursor Acute Lymphoblastic Leukemia (ALL) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 95.20% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on known information, Blinatumomab is a bispecific T-cell engager (BiTE) antibody that simultaneously binds CD19 on B-lymphocytes and CD3 on T-lymphocytes, physically redirecting cytotoxic T cells to recognize and destroy CD19⁺ B-cell precursors. Its efficacy in relapsed/refractory B-cell precursor ALL has been established through multiple international Phase 2 and Phase 3 clinical trials.

The apparent connection between Blinatumomab's established indication (B-ALL) and primary release disorder of platelets is indirect. Patients with B-ALL routinely develop thrombocytopenia — either from disease-related bone marrow infiltration or as a consequence of chemotherapy. This co-occurrence in the clinical literature has likely positioned these two conditions as network neighbors within the TxGNN knowledge graph, creating a statistical association that does not reflect any shared pathophysiology or therapeutic target.

Primary platelet release disorders involve dysfunction in platelet dense granule or alpha-granule secretion pathways, which operate entirely within the platelet-megakaryocyte axis and are mechanistically independent of the CD19⁺ B-cell / CD3⁺ T-cell immune axis that Blinatumomab engages. No published preclinical or clinical data supports a pharmacological link between BiTE-mediated B-cell depletion and correction of platelet granule release defects.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04524455](https://clinicaltrials.gov/study/NCT04524455) | Phase 1b | Completed | 17 | Safety and tolerability of Blinatumomab + AMG 404 in R/R B-ALL; primary objective was estimating MTD/RP2D of AMG 404. Platelet counts collected as safety monitoring only, not as an efficacy endpoint. |
| [NCT03476239](https://clinicaltrials.gov/study/NCT03476239) | Phase 3 | Completed | 121 | Multicenter Phase 3 study of Blinatumomab efficacy in Chinese adults with R/R B-precursor ALL; primary endpoint was hematological response (CR/CRh). Platelet parameters are safety monitoring, not therapeutic targets. |

> ⚠️ **Relevance caveat**: Both trials are B-ALL studies (relevance grade **C**). Neither investigates platelet release disorder as a therapeutic indication. Association with the predicted indication is system-generated and not clinically meaningful.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Blinatumomab holds no product registrations in Singapore. The drug is not currently marketed or authorized for any indication under HSA.

---

## Cytotoxicity

Blinatumomab is an antineoplastic immunotherapy approved for a hematological malignancy. The following applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy — CD19×CD3 BiTE antibody; not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Moderate to High — B-ALL patients are at baseline high risk; cytokine release syndrome (CRS) can transiently worsen neutropenia and thrombocytopenia during therapy |
| Emetogenicity Classification | Low — immunotherapy mechanism; not classified as a conventional emetogenic agent |
| Monitoring Items | CBC with differential (baseline and during infusion), liver function, renal function, neurological status (mandatory neurotoxicity monitoring), electrolytes, CRS surveillance (temperature, blood pressure, oxygen saturation) |
| Handling Protection | Standard biologic (protein-based therapeutic) handling precautions; Blinatumomab is not classified as a hazardous cytotoxic agent under NIOSH guidelines and does not require cytotoxic drug handling protocols |

---

## Safety Considerations

Safety data (key warnings and contraindications) was not available in the current evidence pack.

> Please refer to the package insert for complete safety information. It is noted that Blinatumomab carries a **black-box warning** in its FDA-approved labeling for **Cytokine Release Syndrome (CRS)** and **Neurological toxicity**, both of which can be severe or life-threatening. These require careful review before any clinical application, regardless of indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction of Blinatumomab for primary release disorder of platelets is biologically implausible under current evidence. The drug's CD19×CD3 BiTE mechanism has no established pharmacological connection to platelet granule secretion pathways, and the two identified clinical trials address B-ALL management — platelet values appear only as safety monitoring parameters, not therapeutic endpoints. The high TxGNN score (95.20%) reflects knowledge graph proximity between B-ALL complications and platelet disorders, not genuine mechanistic or clinical overlap.

**To proceed, the following is needed:**
- Identification of any published mechanistic link between CD19⁺ B-cell depletion or T-cell engagement and platelet granule release function — currently none is known
- Complete safety profile review including FDA/EMA black-box warnings for CRS and neurotoxicity before any expanded indication assessment
- Review of published B-ALL trial datasets for any secondary findings documenting improvement in platelet function beyond simple count recovery
- HSA/Singapore regulatory pathway feasibility assessment, noting that the drug is not currently approved or marketed in Singapore
- MOA data retrieval from DrugBank (DG002) and TFDA package insert (DG001) to enable formal mechanistic plausibility scoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

