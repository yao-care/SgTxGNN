---
layout: default
title: Vitamin D
parent: Medium Evidence (L3-L4)
nav_order: 1063
evidence_level: L4
indication_count: 10
---

# Vitamin D
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

# Vitamin D: From an Unspecified Registered Indication to Primary Release Disorder of Platelets

## One-Sentence Summary

Vitamin D (DrugBank DB11094) is registered in Singapore as a component of a combination tablet, but the registration record does not state its approved indication.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, a rare platelet function disorder.
Despite a high model score, **none of the 10 retrieved clinical trials is relevant** and only **one 1989 case report of two myelofibrosis patients** gives a weak, indirect signal, so this prediction is essentially unsupported.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration record |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 93.11% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Vitamin D is known to act through the vitamin D receptor (VDR), which influences cell differentiation and immune regulation. Its original approved indication is not recorded in the data supplied.

A plausible but speculative link is that VDR signalling can affect megakaryocyte and monocyte differentiation, and megakaryocytes produce platelets. The only supporting signal is a 1989 report of 1,25-dihydroxyvitamin D3 in myelofibrosis, a different disease that may involve platelet-function abnormalities. No established mechanism connects vitamin D to platelet release disorders.

The high TxGNN score (0.93) is not backed by any directly relevant clinical data. It should be read as a knowledge-graph hypothesis only.

## Clinical Trial Evidence

The 10 trials retrieved were all reviewed and none tests vitamin D, or any therapy, in platelet release disorders. Nine were graded "C" (not related). The tenth, NCT07120477, was not graded, but its title shows a suicide-prevention study with no platelet link.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04845971](https://clinicaltrials.gov/study/NCT04845971) | Phase 2 | Completed | 97 | Oral GcMAF immunotherapy in hospitalised COVID-19 pneumonia; not related |
| [NCT05393362](https://clinicaltrials.gov/study/NCT05393362) | N/A | Completed | 65 | Cardiac rehabilitation in elderly heart failure; not related |
| [NCT07087561](https://clinicaltrials.gov/study/NCT07087561) | N/A | Recruiting | 360 | Nutritional support after colorectal cancer surgery; not related |
| [NCT05711810](https://clinicaltrials.gov/study/NCT05711810) | Phase 4 | Completed | 1 | SARS-CoV-2 spike protein and hemodialysis; not related |
| [NCT03980132](https://clinicaltrials.gov/study/NCT03980132) | Phase 4 | Completed | 184 | Lugol solution before thyroidectomy in Graves disease; no platelet link |
| [NCT06907212](https://clinicaltrials.gov/study/NCT06907212) | N/A | Enrolling by invitation | 100 | Adipocyte transcriptional changes in obesity; not related |
| [NCT00596947](https://clinicaltrials.gov/study/NCT00596947) | Phase 4 | Terminated | 18 | Steroid withdrawal in kidney transplantation; not related |
| [NCT04659486](https://clinicaltrials.gov/study/NCT04659486) | N/A | Unknown | 100 | Paediatric COVID-19 cohort; not related |
| [NCT04537559](https://clinicaltrials.gov/study/NCT04537559) | N/A | Unknown | 240,000 | Pandemic impact on non-COVID hospital outcomes; not related |
| [NCT04291508](https://clinicaltrials.gov/study/NCT04291508) | Phase 2 | Completed | 488 | Acetaminophen and ascorbate in sepsis; not related |

## Literature Evidence

Only four publications were retrieved, and only one touches a related condition.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2811498](https://pubmed.ncbi.nlm.nih.gov/2811498/) | 1989 | Small clinical report | Medicina Clinica | Two myelofibrosis cases (one chronic idiopathic, one megakaryoblastic leukemia) treated with 1,25-dihydroxyvitamin D3, with the abnormal megakaryocyte population as the proposed target. The only indirect signal |
| [10640215](https://pubmed.ncbi.nlm.nih.gov/10640215/) | 1998 | Review | Bailliere's Clinical Haematology | Pathogenesis and management of idiopathic myelofibrosis, including inappropriate release of megakaryocyte/platelet-derived growth factors; background only, not about vitamin D |
| [31637855](https://pubmed.ncbi.nlm.nih.gov/31637855/) | 2019 | Veterinary cohort | J Vet Emerg Crit Care | 25-hydroxyvitamin D levels in critically ill dogs; not applicable to this indication |
| [27885969](https://pubmed.ncbi.nlm.nih.gov/27885969/) | 2016 | Conference abstract | Critical Care | Intensive care symposium abstracts; not relevant |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13152P | Fosamax Plus™ 70mg/2800IU Tablet | Tablet (oral) | Not stated in the registration record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (93.1%), but no trial or publication directly supports vitamin D for primary release disorder of platelets. The only signal is a 1989 two-patient report in a different disease, so this is a model-only hypothesis at evidence level L4.

Of the other ten predictions in the same Evidence Pack, **hypoparathyroidism** (score 84.1%, rank 9) has by far the strongest support. Active vitamin D (calcitriol or alfacalcidol) with calcium is its long-standing standard therapy, so this is established care rather than novel repurposing. Its guardrails are monitoring serum and urinary calcium and watching for hypercalcemia, hypercalciuria and nephrocalcinosis. I recommend evaluating that indication first.

**To proceed, the following is needed:**
- The approved indication and package-insert warnings and contraindications from the HSA record (currently blocking safety screening)
- Mechanism of action data for vitamin D from DrugBank
- Any direct evidence that links vitamin D or VDR signalling to platelet release function, such as in vitro platelet studies, before a clinical trial is considered
- Confirmation that the registered product (a combination tablet) is an appropriate vehicle, since the generic "Vitamin D" entry is not the usual active agent for this use

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

