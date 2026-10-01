---
layout: default
title: Temozolomide
parent: High Evidence (L1-L2)
nav_order: 951
evidence_level: L1
indication_count: 10
---

# Temozolomide
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Temozolomide: From a Registered Use (Indication Not Recorded) to Adult Astrocytic Tumour

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy agent. The Evidence Pack does not record its original approved indication.
The TxGNN model predicts it may be effective for **adult astrocytic tumour**.
This is supported by **2 clinical trials** (1 completed Phase 3 randomised trial) and **20 publications**, including several randomised Phase 3 trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (the Singapore licence indication text is empty) |
| Predicted New Indication | Adult astrocytic tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Based on the literature, temozolomide is a DNA alkylating agent that forms O6-methylguanine adducts and is cytotoxic to glial tumour cells. Its activity depends on MGMT promoter methylation: tumours that lack the MGMT repair enzyme respond better, and resistance arises through MGMT expression or mismatch repair deficiency.

Astrocytic tumours are glial-lineage brain tumours, which fits this mechanism. Published Phase 3 trials already test temozolomide in astrocytic tumours, for example against radiotherapy alone in elderly patients with malignant astrocytoma (NOA-08).

Because the original indication is not recorded, this prediction may be a rediscovery of an existing use rather than true repurposing. Confirming the approved Singapore indication would settle this.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Temozolomide alone vs procarbazine, lomustine and vincristine (PCV) in recurrent WHO grade III/IV astrocytic tumours (malignant glioma) |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding safety and PK study of XL184 with temozolomide and radiotherapy in first-line glioblastoma; supports combination safety only |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | Radiotherapy alone vs radiotherapy plus concomitant and adjuvant temozolomide in glioblastoma |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | Phase 3 RCT | Lancet Oncol | NOA-08: dose-dense temozolomide alone vs radiotherapy alone in elderly patients with anaplastic astrocytoma or glioblastoma |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | Phase 3 RCT | Lancet | CeTeG/NOA-09: lomustine-temozolomide vs standard temozolomide in MGMT-methylated glioblastoma |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | Tumour-treating fields plus temozolomide vs temozolomide alone as maintenance therapy |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | Adding bevacizumab to temozolomide and radiotherapy in newly diagnosed glioblastoma |
| [39480453](https://pubmed.ncbi.nlm.nih.gov/39480453/) | 2024 | RCT | JAMA Oncol | Adding veliparib to temozolomide in MGMT-methylated glioblastoma |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | RCT | J Neurooncol | Radiotherapy plus temozolomide in anaplastic astrocytoma and anaplastic oligo-astrocytoma |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | Phase II/III RCT | J Clin Oncol | NRG BN007: dual immune checkpoint blockade in MGMT-unmethylated newly diagnosed glioblastoma |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Overview of glioblastoma and other primary brain malignancies in adults |
| [10914698](https://pubmed.ncbi.nlm.nih.gov/10914698/) | 2000 | Review | Clin Cancer Res | Early review of temozolomide as an oral imidazotetrazine alkylator in malignant glioma |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN15710P | TemoRel Hard Capsule 20 mg | Capsule | Reliance Life Sciences Pvt Ltd. |
| SIN15709P | TemoRel Hard Capsule 100 mg | Capsule | Reliance Life Sciences Pvt Ltd. |
| SIN15066P | Astrodal Capsules 100 mg | Capsule | Lotus Pharmaceutical Co., Ltd. Nantou Plant |
| SIN15067P | Astrodal Capsules 20 mg | Capsule | Lotus Pharmaceutical Co., Ltd. Nantou Plant |
| SIN11707P | Temodal Capsule 100 mg | Capsule | Organon Heist bv (packaging) / Orion Corporation Orion Pharma |

Five of the 8 registrations are shown. All are oral capsules.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, imidazotetrazine class) |
| Myelosuppression Risk | Moderate (literature and trials in the pack mention thrombocytopenia, lymphopenia and dose-limiting bone marrow toxicity; grading not provided) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential (platelets and lymphocytes in particular), liver and renal function |
| Handling Protection | Follow local cytotoxic drug handling regulations for oral capsules |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Randomised Phase 3 evidence (NCT00052455, NOA-08, CeTeG/NOA-09) and a high prediction score support temozolomide in astrocytic tumours. However, the original indication, mechanism data and local safety information are missing, so a Singapore-specific review is needed first.

**To proceed, the following is needed:**
- Singapore package insert (approved indication, warnings, contraindications, interactions), the blocking gap
- Mechanism-of-action data from DrugBank
- Confirmation of whether adult astrocytic tumour is already an approved Singapore indication
- An MGMT promoter methylation testing pathway, since benefit depends on MGMT status
- A haematological monitoring plan

Other predicted indications are weaker and should not be bundled with this one: cauda equina neoplasm, diencephalic astrocytomas and subependymal giant cell astrocytoma are all at Hold.

*This report is for research reference only and does not constitute medical advice. Predicted repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

