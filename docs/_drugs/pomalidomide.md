---
layout: default
title: Pomalidomide
parent: 僅模型預測 (L5)
nav_order: 798
evidence_level: L5
indication_count: 10
---

# Pomalidomide
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

# Pomalidomide: From Relapsed/Refractory Multiple Myeloma to Indolent Plasma Cell Myeloma

## One-Sentence Summary

> Pomalidomide is a third-generation immunomodulatory drug (IMiD) with established efficacy in relapsed or refractory multiple myeloma.
> The TxGNN model predicts it may also be effective for **Indolent Plasma Cell Myeloma**,
> with **1 completed Phase 2 clinical trial** and **2 supporting publications** currently available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (no license data on file); internationally used for relapsed/refractory multiple myeloma, as reflected in the supporting trial evidence |
| Predicted New Indication | Indolent Plasma Cell Myeloma |
| TxGNN Prediction Score | 93.96% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A formal DrugBank mechanism-of-action summary is not available in this evidence pack. Based on the mechanistic evidence associated with the predicted indication, pomalidomide is a third-generation IMiD (structurally related to thalidomide and lenalidomide) that binds the cereblon (CRBN) E3 ubiquitin ligase complex, promoting degradation of the transcription factors IKZF1/IKZF3 (Ikaros/Aiolos). This suppresses plasma cell proliferation while activating T-cell and NK-cell antitumour immunity, and the drug also has antiangiogenic activity.

Indolent (smoldering) plasma cell myeloma sits on the same disease spectrum as relapsed/refractory multiple myeloma, the population in which pomalidomide's efficacy is already established. Since the underlying pathology — clonal plasma cell proliferation — is mechanistically identical, extending use to an earlier, less aggressive disease stage is biologically plausible. However, indolent/smoldering myeloma is clinically managed with watchful waiting rather than immediate treatment in most guidelines, so this represents a meaningful shift in treatment paradigm that requires indication-specific clinical validation rather than extrapolation from relapsed/refractory data alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02046915](https://clinicaltrials.gov/study/NCT02046915) | Phase 2 | Completed | 60 | Single-arm, open-label study of pomalidomide + dexamethasone with response-adapted cyclophosphamide in relapsed myeloma; explores balancing efficacy against myelosuppression risk when combined with alkylating agents |

*Note: this trial enrolled relapsed/refractory myeloma patients, not specifically an "indolent" subtype cohort.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22180161](https://pubmed.ncbi.nlm.nih.gov/22180161/) | 2012 | Review | American Journal of Hematology | Diagnosis, risk-stratification and management update for multiple myeloma |
| [21181954](https://pubmed.ncbi.nlm.nih.gov/21181954/) | 2011 | Review | American Journal of Hematology | Prior-year diagnosis, risk-stratification and management update for multiple myeloma |

---

## Singapore Market Information

Pomalidomide currently has no product registration on file in Singapore (0 authorizations). No dosage form or approved-indication data is available for the local market.

---

## Cytotoxicity

Pomalidomide is an antineoplastic agent (IMiD class, used in plasma cell myeloma), so cytotoxicity information is included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunomodulatory agent (IMiD) — not a conventional cytotoxic; acts via CRBN-mediated targeted protein degradation combined with immune activation |
| Myelosuppression Risk | High — trial evidence (NCT02046915) explicitly flags critical myelosuppression risk, particularly when combined with alkylating agents |
| Emetogenicity Classification | Low to Moderate (typical for the IMiD class; drug-specific data not available in this evidence pack) |
| Monitoring Items | Complete blood count with differential (regular monitoring for neutropenia/thrombocytopenia), renal function, and pregnancy status (IMiD class carries teratogenic risk) |
| Handling Protection | Special handling precautions recommended, consistent with thalidomide-analogue (IMiD) risk-management requirements |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial and supporting mechanistic literature establish pomalidomide's efficacy in the broader relapsed/refractory myeloma population, lending plausibility to extension into indolent plasma cell myeloma. However, no trial has directly studied the indolent/smoldering subtype, and the drug is not currently registered in Singapore.

**To proceed, the following is needed:**
- TFDA/HSA package insert with warnings, contraindications, and DDI data (currently blocking, DG001)
- Formal DrugBank/manufacturer mechanism-of-action documentation (DG002)
- Indication-specific clinical evidence (trial or systematic review) in indolent/smoldering plasma cell myeloma, rather than extrapolation from relapsed/refractory data
- Assessment of Singapore regulatory pathway, given zero current registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

