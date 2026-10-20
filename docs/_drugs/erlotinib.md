---
layout: default
title: Erlotinib
parent: Medium Evidence (L3-L4)
nav_order: 396
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Erlotinib: predicted new indication Ewing sarcoma (evidence level L4). Approved use: Non-small cell lung carcinoma, lung cancer, pancreatic adenocarcinoma"
monitor_inn: "Erlotinib"
predicted_indications: ["Ewing sarcoma", "fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "lung germ cell tumor", "pulmonary sulcus neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa"]
---

# Erlotinib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Erlotinib: From Non-Small Cell Lung Cancer to Ewing Sarcoma

## One-Sentence Summary

Erlotinib is an EGFR tyrosine kinase inhibitor, originally used to treat non-small cell lung cancer (NSCLC), lung cancer and pancreatic adenocarcinoma.
The TxGNN model predicts it may be effective for **Ewing sarcoma**, but the evidence is very limited: **1 clinical trial** (withdrawn, no patients enrolled) and **2 publications** (one review and one preclinical study).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung carcinoma, lung cancer, pancreatic adenocarcinoma |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 95.77% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, erlotinib is a small-molecule inhibitor of the EGFR (HER1) tyrosine kinase. Its efficacy in EGFR-driven lung cancer is established, and mechanistically it may be applicable to other tumours in which EGFR/ErbB signalling plays a role.

EGFR/ErbB signalling has been explored in paediatric solid tumours, including Ewing sarcoma. One preclinical study (PMID 29080385) tested the anti-HER3 antibody patritumab, with or without erlotinib, combined with standard cytotoxic agents in paediatric sarcoma xenograft models. This offers a preclinical rationale only. No clinical data exist for erlotinib in Ewing sarcoma, and the link between lung cancer and Ewing sarcoma is a computational association rather than a demonstrated one.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02689336](https://clinicaltrials.gov/study/NCT02689336) | Phase 2 | Withdrawn | 0 | Erlotinib plus temozolomide in relapsed/refractory paediatric solid tumours with EGFR, ERBB2 or JAK2 mutations. No patients were enrolled, so no efficacy or safety data were generated. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29080385](https://pubmed.ncbi.nlm.nih.gov/29080385/) | 2018 | Preclinical study | Pediatric Blood & Cancer | Evaluated patritumab with or without erlotinib combined with cytotoxic agents (cisplatin, vincristine, cyclophosphamide) in paediatric sarcoma xenograft models. |
| [26835334](https://pubmed.ncbi.nlm.nih.gov/26835334/) | 2014 | Review | Translational Pediatrics | General review of advances in paediatric cancer treatment, including risk-adapted therapy. Not specific to erlotinib. |

## Singapore Market Information

Erlotinib has 14 valid single-ingredient registrations in Singapore, all oral film-coated tablets. Approved indication text is not available for any of them. The main authorizations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13184P | Tarceva Tablet 150 mg (Roche) | Film-coated tablet | Not available |
| SIN16137P | Erlonib 150 film-coated tablets (Hetero) | Film-coated tablet | Not available |
| SIN16236P | Tarlonib 150 film-coated tablet (Sun Pharma) | Film-coated tablet | Not available |
| SIN16488P | Erlotirel film-coated tablets 100 mg (Reliance) | Film-coated tablet | Not available |
| SIN17080P | Lotyro 150 erlotinib film-coated tablets (MSN) | Film-coated tablet | Not available |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver and renal function, and haematological parameters; monitor for pulmonary symptoms, skin and gastrointestinal toxicity |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindication-related conditions (from a knowledge graph, not label text)**: Associations include interstitial lung disease, pulmonary fibrosis, liver disease, kidney disease, hepatorenal syndrome, hyperbilirubinemia (including Gilbert syndrome), thrombocytopenia, blood coagulation disease, myocardial infarction and ischemia, coronary artery disease, stroke and cerebrovascular disorders, hemolytic anemia, corneal ulcer, and acute respiratory distress syndrome. These need verification against the official package insert.
- **Drug Interactions**: 100 interactions were found. The **major** ones are with acid-suppressing drugs: proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole). **Moderate** interactions include H2 blockers (famotidine, ranitidine, cimetidine, nizatidine), antacids (aluminium hydroxide, calcium carbonate, magnesium oxide, magaldrate), dexamethasone, clarithromycin, miconazole, eliglustat, naltrexone and rolapitant.
- **Disease-specific concern**: Erlotinib commonly causes EGFR-related skin toxicity, and drug-induced interstitial lung disease is a recognised risk. Package insert warnings were not available, so the label should be reviewed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only registered trial was withdrawn with no enrolment, and the supporting literature is a general paediatric oncology review plus one preclinical xenograft study. The high TxGNN score is a model prediction and is not backed by clinical evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical data specific to erlotinib monotherapy in Ewing sarcoma, including identification of any EGFR-dependent subgroup
- Clinical evidence in paediatric or sarcoma populations, plus a paediatric dosing and safety assessment
- Review of the drug-interaction risk with acid-suppressing agents in a paediatric oncology setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

