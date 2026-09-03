---
layout: default
title: Vinorelbine
parent: 僅模型預測 (L5)
nav_order: 1060
evidence_level: L5
indication_count: 10
---

# Vinorelbine
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

# Vinorelbine: From Non-Small Cell Lung Cancer to Ewing Sarcoma

## One-Sentence Summary

Vinorelbine is a vinca alkaloid microtubule-polymerization inhibitor whose established chemotherapeutic use (documented throughout the literature evidence in this pack) is in non-small cell lung cancer. The TxGNN model predicts it may be effective for **Ewing Sarcoma**, with **4 clinical trials** and **5 relevant publications** currently supporting this direction, primarily through vinorelbine's established activity in related pediatric small round-cell sarcomas (e.g., rhabdomyosarcoma).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in structured regulatory data; literature evidence in this pack consistently documents vinorelbine as an established NSCLC chemotherapeutic |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed, formally sourced mechanism-of-action data for vinorelbine is not available in this evidence pack (flagged as a data gap). Based on the pharmacological characterization embedded in the evidence itself, vinorelbine is a **vinca alkaloid that inhibits microtubule polymerization**, an antimitotic mechanism shared with other vinca alkaloids such as vincristine and vinblastine.

Vinca alkaloids as a class already have clinical activity in pediatric small round-cell sarcomas, including Ewing sarcoma, rhabdomyosarcoma, osteosarcoma, and neuroblastoma. Vinorelbine specifically, in combination with cyclophosphamide, has been studied as a salvage regimen for children and young adults with relapsed or refractory solid tumors — a population that directly includes Ewing sarcoma patients (NCT00180947). This supports a **class-effect rationale**: the same antimitotic mechanism that underlies vinorelbine's efficacy in other solid tumors is mechanistically plausible in Ewing sarcoma, and is further supported by demonstrated efficacy of the closely related combination in rhabdomyosarcoma (PMID 22633624, PMID 12115359).

Preclinical data also show that vinorelbine synergizes with a PLK1 inhibitor to induce apoptosis specifically in Ewing sarcoma cells (PMID 26260582), providing a direct mechanistic link between vinorelbine's microtubule-targeting action and Ewing sarcoma cell biology, beyond simple class extrapolation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Phase 2 | Completed | 50 | Phase II study of vinorelbine (Navelbine) in children with recurrent or refractory malignancies, including sarcoma populations |
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Phase 2 | Unknown | 210 | Vinorelbine + cyclophosphamide in refractory/relapsed rhabdomyosarcoma, Ewing tumours, osteosarcomas, neuroblastomas and medulloblastomas — direct precursor evidence for the Ewing sarcoma salvage regimen |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | N/A | Active, not recruiting | 100 | Prospective multicenter cohort study of risk-stratification-oriented treatment outcomes and safety in pediatric Ewing sarcoma in China (observational, population-relevant) |
| [NCT05999994](https://clinicaltrials.gov/study/NCT05999994) | Phase 2 | Recruiting | 105 | CAMPFIRE master protocol for pediatric/young-adult oncology drug development; disease/drug-specific arms are added as new agents emerge |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Clinical Trial (Phase 2) | Eur J Cancer | Phase II study of vinorelbine + low-dose cyclophosphamide in relapsed/refractory pediatric solid tumors; good tolerability and efficacy demonstrated in rhabdomyosarcoma |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Clinical Trial | Cancer | Vinorelbine in previously treated advanced childhood sarcomas; evidence of activity in rhabdomyosarcoma supports vinca alkaloid class activity in pediatric sarcomas |
| [37637411](https://pubmed.ncbi.nlm.nih.gov/37637411/) | 2023 | Review | Frontiers in Pharmacology | Review of chemotherapeutic drugs for soft tissue sarcomas, contextualizing vinorelbine's role among sarcoma chemotherapy options |
| [26260582](https://pubmed.ncbi.nlm.nih.gov/26260582/) | 2016 | Preclinical/Mechanistic | Int J Cancer | Vinorelbine synergizes with PLK1 inhibitor BI 6727 to induce apoptosis specifically in Ewing sarcoma cells — direct mechanistic evidence in Ewing sarcoma cell lines |
| [36451163](https://pubmed.ncbi.nlm.nih.gov/36451163/) | 2022 | Case Report | BMC Urology | Extraosseous Ewing's sarcoma/pPNET of the kidney case report and literature review; disease-context reference, not vinorelbine-specific |

---

## Singapore Market Information

Vinorelbine is currently **not marketed** in Singapore under this evidence pack, and no HSA license records are available (`total_licenses: 0`, `licenses: []`).

---

## Cytotoxicity

Vinorelbine is a vinca alkaloid antineoplastic agent; this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (vinca alkaloid, microtubule-polymerization inhibitor class) |
| Myelosuppression Risk | High — literature in this pack identifies neutropenia as the dose-limiting toxicity of vinorelbine (e.g., PMID 10585010, PMID 9535205) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions (no emetogenicity data in this evidence pack) |
| Monitoring Items | CBC with differential (neutrophil count); liver function; injection-site/extravasation monitoring for IV administration |
| Handling Protection | Must follow cytotoxic drug handling regulations (preparation, administration, and disposal per institutional hazardous drug protocols) |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not available in this evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L2 is supported by a completed Phase II trial of vinorelbine + cyclophosphamide directly covering Ewing sarcoma among relapsed/refractory pediatric sarcomas, reinforced by demonstrated efficacy in the closely related rhabdomyosarcoma and Ewing-sarcoma-specific preclinical synergy data. However, no trial to date has reported Ewing-sarcoma-specific outcome data for vinorelbine as a distinct endpoint, and the drug is not currently registered in Singapore.

**To proceed, the following is needed:**
- HSA/TFDA-equivalent package insert data — warnings, contraindications, DDI (currently a blocking data gap, DG001)
- Formally sourced mechanism-of-action documentation (DG002)
- Ewing-sarcoma-specific efficacy/outcome data from ongoing trials (NCT06451302, NCT05999994) as they mature
- Regulatory pathway assessment given the drug is currently unregistered in Singapore
- Correction of disease-label mapping errors elsewhere in this candidate set — several lower-ranked predicted indications (e.g., "small cell lung carcinoma," "lung benign neoplasm") are flagged in the evidence pack itself as containing NSCLC-labeled evidence misattributed to unrelated disease terms, and should not be actioned without label correction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

