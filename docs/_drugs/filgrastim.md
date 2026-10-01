---
layout: default
title: Filgrastim
parent: Medium Evidence (L3-L4)
nav_order: 425
evidence_level: L4
indication_count: 10
---

# Filgrastim
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Filgrastim: From Neutropenia Support (G-CSF) to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a granulocyte colony-stimulating factor (G-CSF) that stimulates neutrophil production and mobilizes blood stem cells.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but the score comes from knowledge-graph proximity only.
The **24 retrieved clinical trials** and **1 publication** are mostly stem cell transplant studies, and none tests filgrastim for this disorder.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records. Filgrastim (G-CSF) is generally used for neutropenia and stem cell mobilization. |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on general pharmacology, filgrastim acts through the G-CSF receptor to drive neutrophil lineage proliferation and to mobilize hematopoietic stem cells.

Primary release disorder of platelets is a defect in platelet granule release and function. Filgrastim has no known effect on platelet granule release or platelet function. The only plausible link is indirect: filgrastim supports stem cell mobilization and engraftment in hematopoietic stem cell transplantation (HSCT), which can cure some severe inherited platelet function disorders.

The very high TxGNN score (0.99998) reflects proximity in the knowledge graph. It is not supported by disease-specific clinical data, so it should be read as a hypothesis, not as evidence of efficacy.

## Clinical Trial Evidence

The predicted indication returned 24 matched trials; the 10 most relevant are shown. None studies filgrastim as the tested treatment for a platelet release disorder. Most are HSCT or oncology studies in which G-CSF is at most supportive care.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSCT for hematologic malignancies. The most relevant match, but the target population is unclear and filgrastim is not the tested agent. |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Phase 1 | Withdrawn | 0 | Banked HLA-mismatched donor marrow transplant. Withdrawn, so no data. |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic stem cell transplant in high-risk pediatric sarcomas. Different disease. |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | Completed | 160 | Ganciclovir for CMV reactivation prevention in lung injury. Unrelated. |
| [NCT01503918](https://clinicaltrials.gov/study/NCT01503918) | Phase 2 | Completed | 124 | Antiviral prophylaxis for CMV reactivation in critical care. Unrelated. |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Intensified lymphodepletion with autologous HSCT in severe lupus. Small pilot, unrelated disease. |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | Terminated | 49 | Oral dapansutrile in COVID-19 with early cytokine release syndrome. Not a filgrastim study. |
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated-donor HSCT for hematological malignancies. Filgrastim at most supportive. |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity HSCT pilot for GATA2 mutations. Indirect transplant context only. |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | Autologous HSCT versus best available therapy in multiple sclerosis. Filgrastim would serve only for mobilization. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Cohort | Frontiers in Immunology | G-CSF mobilization of stem cells in healthy donors preferentially mobilizes lymphocyte subsets. It concerns transplant immunology, not platelet disorders. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16267P | ACCOFIL 48 Solution for Injection or Infusion in a Pre-filled Syringe, 48 MU/0.5 mL | Injection, solution |
| SIN16268P | ACCOFIL 30 Solution for Injection or Infusion in a Pre-filled Syringe, 30 MU/0.5 mL | Injection, solution |
| SIN14196P | Nivestim 300 mcg/0.5 mL Solution for Injection/Infusion | Infusion, solution |
| SIN10780P | NEUPOGEN Pre-filled Syringe 30 MU/0.5 mL | Injection |

All products are injectable formulations.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by disease-specific evidence. Filgrastim has no known effect on platelet function, no retrieved trial tests it for this condition, and the only literature is an unrelated stem cell mobilization cohort study. The other top-ranked predictions (pseudo-von Willebrand disease, Glanzmann thrombasthenia and Scott syndrome, among others) also have no supporting studies, so the whole prediction set looks like graph-proximity noise.

**To proceed, the following is needed:**
- Mechanism of action data linking G-CSF to platelet release or function
- Package insert warnings and contraindications for the Singapore-registered products, which are needed for safety screening
- Disease-specific clinical or preclinical evidence, such as case series of filgrastim-supported HSCT in inherited platelet function disorders
- Manual review of the 24 matched trials to confirm whether any include platelet function disorder patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

