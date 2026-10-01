---
layout: default
title: Piperacillin
parent: Low Evidence (L5)
nav_order: 787
evidence_level: L5
indication_count: 10
---

# Piperacillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Piperacillin: From Bacterial Infections to Rheumatoid Arthritis

## One-Sentence Summary

Piperacillin is a beta-lactam antibiotic, marketed in Singapore as piperacillin/tazobactam injection.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis** with a very high score (99.94%), but there are **0 clinical trials** and no publications that test piperacillin as a treatment for this disease.
The 18 retrieved publications are case reports and cohort studies of infections and drug toxicities in RA patients, so this prediction is most likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (inferred from the drug class; the Singapore registration data contain no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.94% (model rank 1283) |
| Evidence Level | L5 (model prediction only; the source pack's provisional L4 is not supported by any preclinical or mechanism study) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Piperacillin is a beta-lactam antibacterial that inhibits bacterial cell wall synthesis. Its efficacy in bacterial infections is established, but no anti-inflammatory or immunomodulatory mechanism relevant to rheumatoid arthritis is documented.

RA is an autoimmune joint disease, and an antibacterial has no obvious target in its pathogenesis. The 99.94% score therefore has no biological rationale behind it.

The literature hits explain why the graph links the two. Piperacillin/tazobactam appears in case reports as empirical treatment for infections in RA patients, who are often immunosuppressed. In those reports the drug treated the infection, not the arthritis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The 18 hits contain no therapeutic evidence for RA. The table lists the most relevant ones.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Cohort | Ann Transl Med | Prevalence and characteristics of antibiotic-associated drug-induced liver injury (a safety signal, not efficacy) |
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2025 | Cohort / predictive model | Br J Clin Pharmacol | Risk factors and a predictive score for eosinophilia in patients on ampicillin/sulbactam or piperacillin/tazobactam |
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Case report | Orthopadie (Heidelberg) | H. influenzae infection of a prosthetic knee in an RA patient on upadacitinib; piperacillin/tazobactam was given for pneumonia |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Case report | BMJ Case Rep | Purulent pericarditis in an RA patient on methotrexate and etanercept; empirical piperacillin/tazobactam started |
| [41268563](https://pubmed.ncbi.nlm.nih.gov/41268563/) | 2025 | Case report | Front Immunol | Atypical bullous erysipelas from E. coli with septic shock in a long-term immunosuppressed RA patient |
| [30371923](https://pubmed.ncbi.nlm.nih.gov/30371923/) | 2019 | Case report | Orthopedics | Emphysematous femoral osteomyelitis in an RA patient on prednisone, treated with antibiotic cement rods and IV antibiotics |
| [17576563](https://pubmed.ncbi.nlm.nih.gov/17576563/) | 2007 | Case report | Rheumatol Int | Disseminated candidiasis in a patient with Felty's syndrome and severe granulocytopenia |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Case report | Proc (Bayl Univ Med Cent) | Low-dose methotrexate toxicity with pancytopenia in RA, rescued with leucovorin (unrelated to piperacillin) |

## Singapore Market Information

All five products are piperacillin/tazobactam combination injections. The registration data contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13985P | Piperacillin/Tazobactam Sandoz Powder for solution for Injection/Infusion 4.5g vials | Powder for solution | Not stated in registration data |
| SIN13758P | TAZPEN FOR INJECTION 4.5g/VIAL | Injection, powder, for solution | Not stated in registration data |
| SIN15299P | SALATAZ POWDER FOR SOLUTION FOR INJECTION/INFUSION 4.5G/VIAL | Injection, powder, for solution | Not stated in registration data |
| SIN15482P | PIPTAZ-AFT POWDER FOR SOLUTION FOR INJECTION 4.5G/VIAL | Injection, powder, lyophilized, for solution | Not stated in registration data |
| SIN08362P | TAZOCIN FOR INJECTION 4.5 g/vial | Injection, powder, for solution | Not stated in registration data |

## Safety Considerations

Please refer to the package insert for safety information. Package insert warnings and contraindications were not available for this report, and no drug-interaction records were found.

The retrieved literature hints at antibiotic-associated liver injury and eosinophilia (PMIDs 33987340 and 41257433). These are general signals and do not replace the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, no plausible mechanism, and no therapeutic literature for piperacillin in RA. The high TxGNN score reflects graph associations, not evidence of benefit. The RA literature is about treating infections in RA patients.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and any evidence of an immunomodulatory effect relevant to RA
- The HSA package insert, including warnings, contraindications and approved indications (currently a blocking gap)
- Any preclinical study or trial of piperacillin in inflammatory arthritis; without one, this candidate should not advance beyond S0

Among the other predictions, only sclerosing cholangitis (rank 4, L5) is flagged as a Research Question. Its rationale is speculative (high biliary concentration, microbiome modulation), and beta-lactam-associated cholestatic liver injury is an unfavorable safety signal.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

