---
layout: default
title: Temozolomide
parent: Low Evidence (L5)
nav_order: 960
evidence_level: L5
indication_count: 1
monitor_inn: "Temozolomide"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-10-23
description: "Temozolomide: predicted new indication Cauda equina neoplasm (evidence level L5). Approved use: Anaplastic astrocytoma, astrocytoma (excluding glioblastoma)…"
---

# Temozolomide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Temozolomide: From Glioma to Cauda Equina Neoplasm
{: .text-alpha }

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy drug. The knowledge graph records it for anaplastic astrocytoma, astrocytoma (excluding glioblastoma) and brain glioblastoma.
The TxGNN model predicts it may be effective for **cauda equina neoplasm**. The supporting evidence is thin: **0 clinical trials** and **3 case reports**, and none of them is a controlled study of this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaplastic astrocytoma, astrocytoma (excluding glioblastoma), brain glioblastoma (relations recorded in the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Cauda equina neoplasm |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 8 of 8) |
| Number of Registrations | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled record. From general pharmacology, temozolomide is an oral alkylating agent. It methylates DNA (O6-guanine, N7-guanine, N3-adenine), which causes cytotoxic lesions and apoptosis in dividing cells. It crosses into the central nervous system. Its activity depends largely on MGMT promoter methylation in the tumour: low MGMT expression increases sensitivity.

Cauda equina neoplasms are mostly myxopapillary ependymomas, which are glial tumours of the CNS. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

There are important limits. A high score from the TxGNN model (deep learning) is not clinical evidence. The compiled data do not show whether MGMT status in myxopapillary ependymoma supports sensitivity to temozolomide.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | Case report | Eur Spine J | Temozolomide showed marked efficacy in a relapsed spinal myxopapillary ependymoma with multiple recurrences and cerebrospinal dissemination. This is the only item close to the predicted disease, and it is a single case. |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | Case report | Medicine | Nasal NUT carcinoma with repeated responses to multimodal treatment including radiotherapy. It is a different disease and only loosely related. |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | Case report | Neuro-Chirurgie | Neuromeningeal cryptococcosis in a child treated for pontine glioma. It is not about efficacy in the predicted disease. |

**Note on the evidence level.** The evidence level is L5 because no cited study directly examines cauda equina neoplasm as a defined disease. The myxopapillary ependymoma case report is the nearest supporting item. It is a single case in a related tumour type and does not meet the L1–L4 threshold.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15710P | TemoRel Hard Capsule 20 mg | Capsule | Not stated in the available records |
| SIN15709P | TemoRel Hard Capsule 100 mg | Capsule | Not stated in the available records |
| SIN15066P | Astrodal Capsules 100 mg | Capsule | Not stated in the available records |
| SIN15067P | Astrodal Capsules 20 mg | Capsule | Not stated in the available records |
| SIN11707P | Temodal Capsule 100 mg | Capsule | Not stated in the available records |

Three further single-ingredient licences are also valid: SIN15642P and SIN15641P (Gliotem 100 mg and 20 mg) and SIN11706P (Temodal 20 mg). All 8 licences are oral capsules.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | Medium to high. The knowledge graph records contraindication relations with thrombocytopenia, neutropenia, pancytopenia, anaemia, agranulocytosis, lymphopenia and aplastic anaemia, which indicates a bone marrow risk. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver function. Renal function and further items should follow the package insert. |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication relations recorded in the knowledge graph** (not label text): liver failure, thrombocytopenia, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, pneumocystosis, pancytopenia, lymphopenia, myelodysplastic syndrome, idiopathic aplastic anaemia, aplastic anaemia. These need to be checked against the Singapore package insert.
- **Drug Interactions**: The interaction screen returned 100 records. The most notable is **naltrexone (Moderate)** and **levofloxacin (Minor)**. The other listed interactions have no assigned severity level. They include pantoprazole, omeprazole, lansoprazole, metformin, morphine, prednisone, hydrocortisone, amphotericin B and doxycycline.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (0.9930), but the evidence is limited to a single relevant case report and no registered clinical trials. The package insert warnings and contraindications have not been reviewed, and the mechanism data are missing. The drug is already marketed in Singapore, but no licence text supports this predicted use. It should stay a research question for now.

**To proceed, the following is needed:**
- Download and review the HSA package insert for warnings, contraindications and approved indications.
- Mechanism of action data (for example from DrugBank).
- Evidence on MGMT promoter methylation in myxopapillary ependymoma and cauda equina tumours.
- A systematic literature search for case series, retrospective cohorts or trials in spinal and myxopapillary ependymoma.
- A haematological safety monitoring plan, given the bone marrow-related contraindication relations.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

