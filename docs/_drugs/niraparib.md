---
layout: default
title: Niraparib
parent: 僅模型預測 (L5)
nav_order: 708
evidence_level: L5
indication_count: 10
---

# Niraparib
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

# Niraparib: From Ovarian Cancer to Epiglottis Neoplasm

## One-Sentence Summary

Niraparib is a PARP1/2 inhibitor whose established use, based on the evidence context in this pack, is maintenance therapy for platinum-sensitive recurrent ovarian, fallopian tube, or primary peritoneal cancer. The TxGNN model predicts it may be effective for **Epiglottis Neoplasm**, but this is currently a pure model prediction — **0 clinical trials** and **0 publications** support this specific link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; based on evidence-pack context, niraparib is known for maintenance treatment of recurrent epithelial ovarian, fallopian tube, or primary peritoneal cancer |
| Predicted New Indication | Epiglottis Neoplasm |
| TxGNN Prediction Score | 99.99% (rank 407) |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for niraparib is not available in this evidence pack (marked as a data gap). Based on contextual information found elsewhere in the pack (e.g., trial descriptions and rationale notes for other candidate indications), niraparib is a PARP1/2 inhibitor that exploits synthetic lethality in tumors with homologous recombination deficiency (HRD), including BRCA1/2-mutated cancers. Its efficacy has been established in ovarian, fallopian tube, and primary peritoneal cancer.

Epiglottis neoplasm is a squamous cell malignancy of the laryngopharyngeal region with no established link to HRD or BRCA-pathway biology in the general oncology literature, and no such link is documented anywhere in this evidence pack. There is no obvious tissue-lineage or mechanistic bridge between the original indication (gynecologic, HRD-driven tumors) and this predicted indication.

The 99.99% TxGNN score reflects the model's raw graph-embedding link-prediction confidence, not validated efficacy — this score range is typical across many of the top-407+ ranked candidates in this pack (several other candidates share nearly identical scores). Without any corroborating trial or literature signal specific to head-and-neck/epiglottis tumors, this prediction should be treated as a hypothesis-generation output only, consistent with the pack's own assessment ("缺乏機轉驗證與臨床證據，無法評估 PARP 抑制劑對會厭腫瘤之潛在作用路徑").

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Singapore Market Information

Niraparib is not currently registered in Singapore (0 authorizations on file; market status: Not Marketed).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP1/2 inhibitor) |
| Myelosuppression Risk | Not sourced from this evidence pack — PARP inhibitors as a class are associated with meaningful myelosuppression (notably thrombocytopenia and anemia); confirm against package insert |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential; liver and renal function (class-general recommendation, not confirmed from this evidence pack) |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but this indication has zero supporting clinical trials or literature (Evidence Level L5, Decision Stage S0), and both the mechanism-of-action data (DG002) and Singapore/TFDA safety labeling (DG001, blocking severity) are missing — there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (DG001 – blocking)
- Confirmed niraparib mechanism-of-action documentation (DG002)
- Primary literature or trial evidence specifically linking PARP inhibition to head-and-neck/epiglottis neoplasms
- Confirmation of Singapore registration status
- Consider redirecting evaluation toward other candidates in this same evidence pack with stronger, though ontology-mismatched, support — notably **cystic neoplasm** (L2, S1, Research Question) and **pre-malignant neoplasm** (L3, S1, Research Question), both of which have real trial and/or literature signal tied to niraparib's known HRD/ovarian-cancer mechanism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

