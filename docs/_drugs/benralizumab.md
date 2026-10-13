---
layout: default
title: Benralizumab
parent: Low Evidence (L5)
nav_order: 142
evidence_level: L5
indication_count: 10
---

# Benralizumab
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

# Benralizumab: From Eosinophilic Pneumonia to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Benralizumab is an anti-IL-5 receptor alpha antibody, originally associated with eosinophilic pneumonia and pulmonary eosinophilia, and marketed for severe eosinophilic asthma.
The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting it.
Among the other top-ranked predictions, **dermatitis** has the most supporting evidence (3 clinical trials and 19 publications), and it is discussed below as the most developed alternative direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Eosinophilic pneumonia; pulmonary eosinophilia (the approved indication text in the Singapore licences is blank) |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From known information, benralizumab is a monoclonal antibody against the IL-5 receptor alpha subunit (IL5RA). It depletes eosinophils and basophils through antibody-dependent cell-mediated cytotoxicity (ADCC). It is approved in the US for severe eosinophilic asthma and, since September 2024, for eosinophilic granulomatosis with polyangiitis (EGPA).

The link between eosinophil-driven lung disease and immune thrombocytopenia is weak. Immune thrombocytopenia is caused by autoantibody-mediated platelet destruction, and no mechanistic route from eosinophil or basophil depletion to this condition is established. The high score is likely a graph-based propagation from related immune-mediated disease nodes and should not be read as evidence of efficacy.

**Dermatitis (rank 2, score 99.16%)** is the more plausible direction. Eosinophils, basophils and type 2 innate lymphoid cells contribute to type 2 skin inflammation, so depleting them has a reasonable rationale. However, the larger Phase 2 trial was terminated, and a published report describes a lack of effect (see below).

## Clinical Trial Evidence

No clinical trials are registered for the top predicted indication, thrombocytopenia due to immune destruction. Currently no related clinical trials registered.

For reference, trials for the second-ranked prediction (dermatitis) are:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Phase 2 | Terminated | 194 | HILLIER study: randomized, double-blind, placebo-controlled, 16 weeks plus 36-week extension, in moderate-to-severe atopic dermatitis despite topical treatment. Terminated early. |
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Phase 2 | Completed | 20 | Effects of benralizumab on eosinophils, basophils and innate lymphoid type 2 cells in atopic dermatitis. Small mechanistic study, no results in the data compiled. |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Phase 2 | Not yet recruiting | 96 | Anti-IL-5R therapy in DRESS (drug reaction with eosinophilia and systemic symptoms). Planned start January 2027, so no evidence yet. |

## Literature Evidence

No literature is available for the top predicted indication. Currently no related literature available.

For reference, the most relevant publications for dermatitis are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | Phase 2 RCT report | J Eur Acad Dermatol Venereol | HILLIER trial: reported lack of effect of benralizumab on signs and symptoms of moderate-to-severe atopic dermatitis. |
| [35987486](https://pubmed.ncbi.nlm.nih.gov/35987486/) | 2022 | Review | J Allergy Clin Immunol Pract | Safety of biologics, including benralizumab, for atopic diseases during pregnancy. |
| [34642091](https://pubmed.ncbi.nlm.nih.gov/34642091/) | 2021 | Review | Ann Allergy Asthma Immunol | Guidance on choosing biologics for asthma, atopic dermatitis and related conditions. |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Review | Allergologie Select | Update on biologics for atopic diseases, urticaria and angioedema, with safety focus on hypersensitivity. |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | Review | Immunol Allergy Clin North Am | Biologics for allergic disease during pregnancy and lactation. |
| [31690400](https://pubmed.ncbi.nlm.nih.gov/31690400/) | 2019 | Review | Allergy Asthma Proc | Immunobiologics, including anti-IL-5 agents, for severe asthma, atopic dermatitis and chronic urticaria. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16043P | FASENRA solution for injection 30 mg/mL (autoinjector pen) | Injection, solution | Not stated in the data compiled |
| SIN15683P | FASENRA solution for injection 30 mg/mL (pre-filled syringe) | Injection, solution | Not stated in the data compiled |

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction signals were identified in the data compiled; the single pharmacology record only confirms that the target is IL5RA. No knowledge-graph contraindications were identified.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication, thrombocytopenia due to immune destruction, has no registered trials or literature and no plausible mechanistic link to IL-5R-mediated eosinophil depletion. The same applies to the related autoimmune cytopenia predictions (autoimmune thrombocytopenic, Evans syndrome). The only prediction with trial activity, dermatitis, has an informative negative result: the HILLIER trial was terminated and reported no effect in atopic dermatitis.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA, which are required before any safety screening
- Mechanism of action data from DrugBank
- A mechanistic or clinical rationale connecting IL-5Rα blockade to immune thrombocytopenia, such as case reports or preclinical data
- If dermatitis is pursued instead, the reason for termination of NCT04605094, the results of NCT03563066, and the outcome of the DRESS trial (NCT06734884) once it starts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

