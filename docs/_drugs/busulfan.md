---
layout: default
title: Busulfan
parent: High Evidence (L1-L2)
nav_order: 186
evidence_level: L1
indication_count: 10
monitor_inn: "Busulfan"
predicted_indications: ["myelodysplastic syndrome", "refractory cytopenia of childhood", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "seborrheic keratosis", "simian immunodeficiency virus infection"]
last_modified_at: 2026-10-23
description: "Busulfan: predicted new indication Myelodysplastic syndrome (evidence level L1). Approved use: Not stated in the Singapore licence records"
---

# Busulfan
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

## Busulfan: From Hematologic Conditioning to Myelodysplastic Syndrome
{: .text-alpha }

## One-Sentence Summary

Busulfan is an alkylating agent registered in Singapore as an injection and as tablets. In practice it is used as a conditioning drug before blood stem cell transplantation.
The TxGNN model predicts it may be useful for **myelodysplastic syndrome (MDS)**, with **34 clinical trials** and **18 publications** compiled for this prediction.
The evidence is for busulfan as part of a transplant conditioning regimen, not as a stand-alone MDS treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L1 |
| Singapore Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Busulfan is a bifunctional alkylating agent that cross-links DNA. In transplant medicine it is used as a myeloablative or reduced-intensity conditioning backbone before allogeneic hematopoietic stem cell transplantation (HSCT).

For MDS, allogeneic HSCT is the only potentially curative therapy. Busulfan's role is to eradicate the abnormal marrow clone and create space for donor cells to engraft. This is a transplant-conditioning use rather than a classic repurposing, and busulfan is not expected to act alone against MDS.

Several lower-ranked predictions follow the same logic. Refractory cytopenia of childhood (a paediatric MDS subtype) and aregenerative anaemia (including aplastic anaemia) rely on busulfan-based conditioning, but the supporting studies are largely shared with the MDS and haematologic-malignancy transplant trials.

## Clinical Trial Evidence

Of the 34 trials compiled, the ones with the most direct busulfan and MDS relevance are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02744742](https://clinicaltrials.gov/study/NCT02744742) | Phase 2/3 | Completed | 202 | G-CSF + decitabine + busulfan/cyclophosphamide vs busulfan/cyclophosphamide conditioning in RAEB-1, RAEB-2 and AML secondary to MDS |
| [NCT04708054](https://clinicaltrials.gov/study/NCT04708054) | Phase 2/3 | Recruiting | 324 | Venetoclax added to a fractionated busulfan regimen in high-risk AML and MDS; results not yet available |
| [NCT04713956](https://clinicaltrials.gov/study/NCT04713956) | Phase 2/3 | Unknown | 242 | G-CSF + decitabine + busulfan/cyclophosphamide vs G-CSF + decitabine + busulfan/fludarabine in RAEB and post-MDS AML |
| [NCT00005866](https://clinicaltrials.gov/study/NCT00005866) | Phase 3 | Completed | 240 | Busulfan-TBI vs cyclophosphamide-TBI preparative regimen in advanced MDS or MDS-related AML |
| [NCT01339910](https://clinicaltrials.gov/study/NCT01339910) | Phase 3 | Terminated | 272 | Myeloablative vs reduced-intensity conditioning in MDS or AML (BMT CTN #0901) |
| [NCT00361140](https://clinicaltrials.gov/study/NCT00361140) | Phase 4 | Completed | 72 | AUC-targeted busulfan dose escalation with fludarabine before allogeneic transplant |
| [NCT00027924](https://clinicaltrials.gov/study/NCT00027924) | Phase 2 | Completed | Not reported | Fludarabine and busulfan conditioning in chronic myeloid leukaemia or MDS |
| [NCT00582933](https://clinicaltrials.gov/study/NCT00582933) | Phase 2 | Completed | 96 | IV busulfan, melphalan and fludarabine followed by T-cell-depleted transplant |
| [NCT00357565](https://clinicaltrials.gov/study/NCT00357565) | Phase 2 | Completed | 34 | Busulfan-containing conditioning before cord blood transplant in infant leukaemia and MDS |
| [NCT00987480](https://clinicaltrials.gov/study/NCT00987480) | Phase 2 | Completed | 45 | Busulfan, cyclophosphamide and fludarabine conditioning for Fanconi anaemia, including MDS evolution |

Many other trials in the compiled set test graft-versus-host disease prevention or cell-therapy strategies, so they say little about busulfan itself.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT (phase 3) | Lancet Haematol | Treosulfan + fludarabine vs reduced-intensity busulfan + fludarabine in older AML or MDS patients |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | Final trial analysis | Am J Hematol | Treosulfan outperformed reduced-intensity busulfan for event-free survival in older AML or MDS patients |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | Phase 3 trial | Lancet Haematol | G-CSF + decitabine + busulfan/cyclophosphamide vs busulfan/cyclophosphamide for relapse in MDS or secondary AML |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Registry cohort | Transplant Cell Ther | Myeloablative vs reduced-intensity fludarabine/busulfan in MDS |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Registry cohort | Bone Marrow Transplant | Fludarabine/busulfan vs busulfan/cyclophosphamide myeloablative conditioning in MDS |
| [40901473](https://pubmed.ncbi.nlm.nih.gov/40901473/) | 2025 | Cohort | Front Immunol | Ruxolitinib + decitabine added to modified busulfan-cyclophosphamide for relapse prophylaxis |
| [38197938](https://pubmed.ncbi.nlm.nih.gov/38197938/) | 2024 | Phase 1 | Blood Adv | Venetoclax/azacitidine maintenance after venetoclax + fludarabine/busulfan transplant |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | Am J Hematol | Allogeneic HCT is the only potentially curative therapy for MDS and myelofibrosis |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Meta-analysis | Front Oncol | Long-term outcomes of treosulfan- vs busulfan-based conditioning in MDS and AML |
| [37856098](https://pubmed.ncbi.nlm.nih.gov/37856098/) | 2024 | Risk assessment | Pediatr Blood Cancer | Evidence-based review of subsequent malignancy risk after busulfan exposure |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13260P | BUSULFEX® INJECTION 60 mg/vial (Baxter Oncology GmbH) | Injection, solution, concentrate | Not stated in the licence record |
| SIN11001P | MYRAN TABLETS 2 mg (Korea United Pharmaceutical Inc) | Tablet | Not stated in the licence record |

Both are single-ingredient products with valid status.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High. Profound myelosuppression is the intended effect in conditioning. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Full blood count with differential, liver and renal function; AUC-guided dosing was used in one of the trials above |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindications (knowledge-graph relations, not label text):** The knowledge graph records contraindication relations with thrombocytopenia, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia and Fanconi anaemia), pulmonary fibrosis, epilepsy, hyperglycaemia, and several infectious or fungal diseases. These need checking against the official package insert.
- **Drug Interactions:** 100 interactions were recorded. The main ones are metronidazole (Major), aprepitant and miconazole (Moderate), and levofloxacin (Minor). Others, such as amphotericin B, vancomycin, corticosteroids, proton pump inhibitors and antiemetics, have an unclassified severity.
- Literature in the compiled set also flags a risk of secondary malignancy after busulfan exposure ([PMID 37856098](https://pubmed.ncbi.nlm.nih.gov/37856098/)) and long-term complications in children after transplant conditioning ([PMID 38176654](https://pubmed.ncbi.nlm.nih.gov/38176654/)).

Package insert warnings were not available in the data compiled for this report, so the label should be reviewed before any decision.

## Other Predicted Indications (Brief)

| Predicted Indication | Evidence Level | Note |
|------|------|------|
| Refractory cytopenia of childhood | L2 | Cohort data and busulfan-based transplant trials; Proceed with Guardrails |
| Aregenerative anaemia | L2 | Busulfan trials largely overlap with MDS and malignancy studies; limited aplastic-anaemia-specific data |
| Unclassified MDS | L3 | Only a 1994 transplant study; Research Question |
| HIV infectious disease | L3 | Small early-phase conditioning studies for gene therapy; Research Question |
| 5q deletion, congenital sideroblastic anaemia, neurodevelopmental disorder, seborrheic keratosis, SIV infection | L5 | No studies; Hold. The last three are likely model artefacts |

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Busulfan-based conditioning is directly studied in MDS, including a completed Phase 3 trial of busulfan versus cyclophosphamide with TBI, a completed Phase 2/3 trial, and an ongoing Phase 2/3 trial. Several published randomised and registry studies also support the link. The use is limited to transplant conditioning, however, and not stand-alone MDS therapy. The Singapore licence records list no approved indication text, and the safety data are limited.

**To proceed, the following is needed:**
- Review of the HSA package insert for warnings, contraindications and the approved indications (currently a blocking data gap)
- Confirmation of the mechanism of action from DrugBank
- A transplant-centre protocol covering dosing (including AUC-guided monitoring), myelosuppression management, and long-term and secondary malignancy follow-up
- A review of the major and moderate drug interactions before use in conditioning regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

