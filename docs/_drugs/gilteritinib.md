---
layout: default
title: Gilteritinib
parent: 僅模型預測 (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
---

# Gilteritinib
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

# Gilteritinib: From Relapsed/Refractory AML to Myelodysplastic/Myeloproliferative Disease

## One-Sentence Summary

Gilteritinib (Xospata) is a highly selective FLT3/AXL kinase inhibitor approved internationally for relapsed or refractory FLT3-mutated acute myeloid leukemia (AML).
The TxGNN model generates 10 candidate predictions for new indications; after filtering out biologically implausible high-scoring false positives, **myelodysplastic/myeloproliferative disease (MDS/MPN)** emerges as the most evidence-supported repurposing candidate,
currently backed by **4 clinical trials** and **1 publication**, with an overall evidence level of **L2** and a TxGNN score of **97.00%**.

> **Note on top TxGNN prediction**: The highest-ranked prediction (Rank 1: bulbar polio, score 99.10%) is flagged as a biologically implausible false positive — the disease mechanism (enteroviral lower motor neuron infection) has no known connection to FLT3/AXL signaling, and the evidence pack itself identifies it as a likely knowledge-graph network artifact. This report focuses on the highest-quality actionable prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed/refractory FLT3-mutated acute myeloid leukemia (AML) |
| Predicted New Indication | Myelodysplastic/Myeloproliferative Disease (MDS/MPN) |
| TxGNN Prediction Score | 97.00% (Rank #10 among 10 candidates) |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Gilteritinib is a highly selective inhibitor of FLT3 (FMS-like tyrosine kinase 3) and AXL receptor tyrosine kinase. It works by binding to both the FLT3-ITD (internal tandem duplication) and FLT3-TKD (tyrosine kinase domain point mutation) variants, blocking downstream proliferative and anti-apoptotic signaling in FLT3-dependent leukemic cells. This dual FLT3/AXL inhibition distinguishes it from first-generation FLT3 inhibitors such as midostaurin.

MDS/MPN overlap syndromes — including chronic myelomonocytic leukemia (CMML), atypical CML (aCML), and MDS/MPN-unclassifiable — share key molecular features with AML. FLT3 mutations (FLT3-ITD, FLT3-TKD) and FLT3 gene fusions such as ETV6-FLT3 are recognized driver events in this disease group, conferring dependence on FLT3 signaling for clonal proliferation. The mechanistic rationale for Gilteritinib in FLT3-positive MDS/MPN therefore follows directly from its established AML biology.

Critically, MDS/MPN is biologically positioned on the continuum toward AML — many high-risk MDS/MPN cases eventually transform to overt AML. Gilteritinib has already been evaluated directly in combination with azacitidine and venetoclax in a Phase I/II trial (NCT04140487) that explicitly enrolls high-risk MDS/MPN patients alongside AML cases, providing the most direct clinical precedent available. A published case report (PMID 33792628) further demonstrates ex vivo sensitivity of ETV6-FLT3 fusion-driven myeloid neoplasm to Type I FLT3 inhibitors, reinforcing the therapeutic target hypothesis.

---

## Clinical Trial Evidence

*Primary indication: Myelodysplastic/Myeloproliferative Disease (Rank #10)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04140487](https://clinicaltrials.gov/study/NCT04140487) | Phase I/II | Recruiting | 97 | Azacitidine + Venetoclax + **Gilteritinib** triple combination in FLT3-mutation-positive AML or high-risk MDS/MPN (recurrent or refractory); Gilteritinib is the central investigational drug — provides direct Phase I/II safety and preliminary efficacy data in this disease group |
| [NCT03922100](https://clinicaltrials.gov/study/NCT03922100) | Phase I/II | Terminated | 63 | NMS-03592088 (FLT3/KIT/CSF1R triple inhibitor) in R/R AML or CMML; validates FLT3 inhibition as a mechanism in MDS-spectrum disease; trial terminated — reasons (safety vs. commercial) should be reviewed before extrapolation |
| [NCT05564390](https://clinicaltrials.gov/study/NCT05564390) | Phase 2 | Recruiting | 2,000 | NCI MyeloMATCH master screening and reassessment protocol; large platform trial for AML/MDS/MPN with FLT3 and other molecular biomarker stratification; provides a framework for FLT3-directed sub-studies, but Gilteritinib-specific sub-trial assignment requires confirmation |
| [NCT02115295](https://clinicaltrials.gov/study/NCT02115295) | Phase 2 | Recruiting | 508 | Cladribine + Idarubicin + Cytarabine + Venetoclax in AML/high-risk MDS; no FLT3 inhibitor component — serves as chemotherapy comparator benchmark only |

*Additional — Radiation-related AML/MDS (Rank #3, L3)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05564390](https://clinicaltrials.gov/study/NCT05564390) | Phase 2 | Recruiting | 2,000 | MyeloMATCH protocol also covers radiation-related AML/MDS subtypes under its broad AML/MDS eligibility framework; indirect platform support only |

---

## Literature Evidence

*Primary indication: Myelodysplastic/Myeloproliferative Disease (Rank #10)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [33792628](https://pubmed.ncbi.nlm.nih.gov/33792628/) | 2021 | Case Report | Blood Advances | ETV6-FLT3 fusion-driven myeloid/lymphoid neoplasm with eosinophilia in an infant; patient-derived ex vivo studies demonstrated increased sensitivity to Type I FLT3 inhibitors compared to Type II inhibitors — directly supports FLT3 fusion as a therapeutic target in MDS/MPN-spectrum disease, and validates the mechanistic rationale for Gilteritinib (a Type I FLT3 inhibitor) in this indication |

---

## Singapore Market Information

Gilteritinib is currently **not registered** in Singapore. There are no active product authorizations on record.

> Gilteritinib is not available through standard regulatory channels in Singapore. Any clinical use would require a Special Access Route (SAR) application or a compassionate use/clinical trial framework. This represents a key regulatory barrier that must be addressed before clinical deployment.

---

## Cytotoxicity

Gilteritinib is an antineoplastic targeted therapy (FLT3/AXL tyrosine kinase inhibitor) indicated for leukemia treatment.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective FLT3/AXL receptor tyrosine kinase inhibitor (small molecule, oral) |
| Myelosuppression Risk | Moderate — febrile neutropenia, anemia, and thrombocytopenia are recognized risks; differentiation syndrome (a potentially life-threatening complication unique to AML/MDS targeted therapies) has been reported |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (weekly for first month, then regularly), liver function tests (ALT/AST/bilirubin), renal function, QTc interval (ECG before and during treatment), serum electrolytes (Mg²⁺, K⁺, Ca²⁺), signs and symptoms of differentiation syndrome (fever, dyspnea, pleural/pericardial effusion, rapid weight gain) |
| Handling Protection | Please refer to the package insert warnings and precautions for cytotoxic handling requirements |

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interaction profile) was available in this evidence pack. All safety fields are identified as data gaps.

> Please refer to the full package insert (FDA prescribing information / EMA Summary of Product Characteristics) for safety information. Based on the drug class and published literature, clinicians should be particularly alert to: **differentiation syndrome** (potentially fatal, requires prompt corticosteroid treatment), **QTc prolongation** (avoid concurrent QT-prolonging agents), **embryo-fetal toxicity** (contraindicated in pregnancy), and **posterior reversible encephalopathy syndrome (PRES)**. Detailed DDI data was not retrieved and should be assessed separately, especially for CYP3A4 interactions given the metabolic profile of kinase inhibitors.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Among the 10 TxGNN-predicted indications, myelodysplastic/myeloproliferative disease is the only candidate with direct mechanistic grounding (shared FLT3 signaling with the approved AML indication) and clinical trial support — most critically, NCT04140487 directly tests Gilteritinib in high-risk MDS/MPN patients, providing Phase I/II-level evidence for this repurposing direction. However, Singapore has no existing Gilteritinib registration, and safety documentation is currently unavailable, both of which must be resolved before clinical translation.

**To proceed, the following is needed:**

- **Blocking — Safety review**: Retrieve full FDA label / EMA SmPC to complete the safety assessment; this is identified as a blocking data gap (DG001) and must be addressed before any clinical or regulatory step
- **High priority — MOA documentation**: Formally document FLT3/AXL mechanism of action from DrugBank or published sources (DG002); essential for regulatory dossier and mechanistic justification
- **FLT3 mutation prevalence in MDS/MPN**: Confirm FLT3-ITD/TKD mutation frequency in the specific MDS/MPN subtypes targeted (CMML, MDS/MPN-U, aCML) to define the eligible biomarker-selected patient population
- **Monitor NCT04140487**: Obtain interim or published results from the Azacitidine + Venetoclax + Gilteritinib Phase I/II trial; this is the most directly relevant evidence source
- **Singapore regulatory pathway**: Gilteritinib is not registered in Singapore; initiate a Special Access Route (SAR) or compassionate use application strategy, or plan a local Phase II trial
- **Biomarker stratification protocol**: Establish FLT3 mutation testing (PCR or NGS-based) as a mandatory inclusion criterion for any prospective study

---

### Summary of All 10 TxGNN Predictions

| Rank | Indication | TxGNN Score | Evidence Level | Decision |
|------|-----------|:-----------:|:--------------:|---------|
| 1 | Bulbar polio | 99.10% | L5 | **Hold** — biologically implausible (false positive) |
| 2 | AML/MDS related to alkylating agent | 98.99% | L4 | **Research Question** — FLT3 mutation prevalence needs confirmation |
| 3 | AML/MDS related to radiation | 98.99% | L3 | **Research Question** — indirect framework support only |
| 4 | 5q35 microduplication syndrome | 98.89% | L5 | **Hold** — biologically implausible (gene dosage mechanism, no FLT3 link) |
| 5 | Neuralgic amyotrophy | 98.10% | L5 | **Hold** — no mechanistic link to FLT3/AXL |
| 6 | Amyotrophic neuralgia | 97.96% | L5 | **Hold** — likely ontology synonym of #5, same assessment |
| 7 | Vertebral anomalies & T-cell dysfunction | 97.36% | L5 | **Hold** — no mechanistic basis |
| 8 | Ganglioneuroblastoma | 97.22% | L5 | **Hold** — AXL hypothesis requires preclinical validation first |
| 9 | Retroperitoneal neoplasm | 97.01% | L5 | **Hold** — diagnosis too broad; histological subtype must be defined |
| **10** | **Myelodysplastic/Myeloproliferative Disease** | **97.00%** | **L2** | **Proceed with Guardrails** ✓ |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

