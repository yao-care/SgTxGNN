---
layout: default
title: Protein C
parent: Low Evidence (L5)
nav_order: 839
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Protein C: predicted new indication Glanzmann thrombasthenia (evidence level L5). Approved use: Not stated in the licence data (approved indication text is empty)"
monitor_inn: "Protein C"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "Scott syndrome", "platelet-type bleeding disorder", "inherited thrombophilia", "fetal and neonatal alloimmune thrombocytopenia", "flood factor deficiency"]
---

# Protein C
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

# Protein C: From Unspecified Original Indication to Glanzmann Thrombasthenia (Top Prediction) — Best-Supported Use: Inherited Thrombophilia

## One-Sentence Summary

Protein C is a plasma-derived natural anticoagulant protein. The data compiled for this report do not list an approved indication text for the Singapore licence, but it is used clinically to replace the missing protein in severe congenital Protein C deficiency.
The TxGNN model's highest-scoring prediction is **Glanzmann thrombasthenia** (score 98.6%), but this is biologically implausible: the drug is an anticoagulant and the disease is a bleeding disorder, and no trials or relevant literature support it.
The only prediction with real support is **inherited thrombophilia** (rank 8), backed by **3 relevant clinical studies** (1 Phase 2/3, 1 retrospective study and 1 registry) and several review articles. This is essentially the drug's on-label use, not true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (approved indication text is empty) |
| Predicted New Indication | Glanzmann thrombasthenia (rank 1); best-supported prediction: inherited thrombophilia (rank 8) |
| TxGNN Prediction Score | 98.60% (Glanzmann thrombasthenia); 90.01% (inherited thrombophilia) |
| Evidence Level | L5 (Glanzmann thrombasthenia); L2 (inherited thrombophilia) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold (Glanzmann thrombasthenia); Proceed with Guardrails (inherited thrombophilia, restricted to severe Protein C deficiency) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the compiled data. Based on known information, Protein C is a vitamin K-dependent anticoagulant. Its activated form (APC) inactivates coagulation factors Va and VIIIa, which limits clot formation.

**Glanzmann thrombasthenia (top-ranked prediction):** This is a bleeding disorder caused by a defect in platelet integrin alphaIIb/beta3. Giving an anticoagulant would be expected to worsen bleeding, not relieve it. The high score (0.986) most likely reflects closeness within the haemostasis network of the knowledge graph rather than a real treatment rationale. The same reasoning applies to the other bleeding or platelet disorders in the top 10 (primary release disorder of platelets, pseudo-von Willebrand disease, constitutional thrombocytopenia, collagen receptor defect, Scott syndrome, platelet-type bleeding disorder, fetal and neonatal alloimmune thrombocytopenia). The tenth entry, "flood factor deficiency", appears to be a malformed term that cannot be mapped to a clinical entity.

**Inherited thrombophilia (best-supported prediction):** Severe congenital Protein C deficiency causes purpura fulminans and venous thromboembolism through loss of the Protein C anticoagulant pathway. Protein C concentrate (Ceprotin) directly replaces the missing protein, so the mechanism is coherent. This is the drug's on-label use, i.e. replacement of the deficient protein rather than repurposing in the strict sense.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (Glanzmann thrombasthenia). The table below covers the best-supported prediction, inherited thrombophilia. Only trials directly involving Protein C concentrate are included.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00157118](https://clinicaltrials.gov/study/NCT00157118) | Phase 2/3 | Completed | 18 | Efficacy and safety of Protein C concentrate in severe congenital Protein C deficiency (acute episodes, short-term and long-term prophylaxis) |
| [NCT00161720](https://clinicaltrials.gov/study/NCT00161720) | N/A | Completed | 11 | Retrospective dosing and outcome data for patients treated under an emergency use IND; supports clinical use but is not a controlled trial |
| [NCT01127529](https://clinicaltrials.gov/study/NCT01127529) | N/A | Completed | 43 | Ceprotin treatment registry; real-world safety and effectiveness data |
| [NCT06590974](https://clinicaltrials.gov/study/NCT06590974) | N/A | Recruiting | 7 | Post-marketing surveillance of Ceprotin 1000 IU in Japan; no results available yet |
| [NCT04180657](https://clinicaltrials.gov/study/NCT04180657) | N/A | Unknown | 60 | Observational study of ghrelin levels in Protein C deficiency; not an intervention study with Protein C |

## Literature Evidence

No relevant literature supports Protein C for Glanzmann thrombasthenia. The two retrieved papers (a veterinary review of equine haemostatic disorders and a review of platelet coagulation) are only general background. The table below covers inherited thrombophilia; all are reviews or guidelines, and none is an RCT.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39233011](https://pubmed.ncbi.nlm.nih.gov/39233011/) | 2024 | Review (ISTH communication) | J Thromb Haemost | Use of direct oral anticoagulants in severe thrombophilia; evidence limited to cohort and single-centre studies |
| [38733983](https://pubmed.ncbi.nlm.nih.gov/38733983/) | 2024 | Review | Semin Thromb Hemost | Thrombophilia screening should be selective; thrombophilia does not always predict recurrence |
| [24739277](https://pubmed.ncbi.nlm.nih.gov/24739277/) | 2014 | Review | J Pharm Pract | Inherited thrombophilias, including rare natural anticoagulant deficiencies (antithrombin, Protein C, Protein S) |
| [23986205](https://pubmed.ncbi.nlm.nih.gov/23986205/) | 2013 | Review | Adv Clin Exp Med | Practical diagnostic issues in Protein C and Protein S deficiency |
| [29518638](https://pubmed.ncbi.nlm.nih.gov/29518638/) | 2018 | Review | Thromb Res | Thrombophilia testing in children, including Protein C deficiency |
| [37334488](https://pubmed.ncbi.nlm.nih.gov/37334488/) | 2023 | Guideline | BJOG | Recurrent miscarriage guideline; testing for acquired thrombophilia |
| [24365371](https://pubmed.ncbi.nlm.nih.gov/24365371/) | 2014 | Review | Handb Clin Neurol | Thrombophilic states and cerebral venous sinus thrombosis |
| [32204642](https://pubmed.ncbi.nlm.nih.gov/32204642/) | 2022 | Review | J Matern Fetal Neonatal Med | Neonatal thrombosis and its risk factors |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14933P | OCTAPLEX Powder and Solvent for Solution for Injection 500 IU | Injection, powder, for solution | Not stated in the licence data |

## Safety Considerations

- **Drug Interactions:** 32 interactions were identified in total. The only one rated Major is **caplacizumab**. The others are mostly rated Moderate and involve other anticoagulants and thrombolytics, such as warfarin, apixaban, edoxaban, enoxaparin, dalteparin, fondaparinux, argatroban, bivalirudin, alteplase, antithrombin III human and drotrecogin alfa, as well as celecoxib. Concurrent use with these agents needs close monitoring for bleeding.
- **Mechanism-related concern:** For the bleeding and platelet disorders predicted by the model, an anticoagulant would be expected to worsen bleeding.

Please refer to the package insert for further safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold (Glanzmann thrombasthenia and the other bleeding or platelet disorders); Proceed with Guardrails (inherited thrombophilia, limited to severe congenital Protein C deficiency)**

**Rationale:**
- The top-ranked prediction, Glanzmann thrombasthenia, has no trials, no relevant literature and an unfavourable mechanism (an anticoagulant for a bleeding disorder). It should be treated as a graph-proximity artefact.
- For inherited thrombophilia, a completed Phase 2/3 study (n=18), a retrospective study and a registry support Protein C replacement in severe congenital deficiency. Evidence is limited to small rare-disease studies and there is no controlled Phase 3 RCT, so the level is L2 rather than L1.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently missing and blocking for safety screening)
- Approved indication text for the Singapore licence
- Detailed mechanism of action data
- Clarification of whether the Singapore product (a product listed under the Octaplex name) matches the Protein C concentrate used in the trials
- Restriction to documented severe Protein C deficiency (not general thrombophilia), with monitoring of Protein C activity and bleeding; the broader thrombophilia literature does not support Protein C supplementation in non-deficient patients
- Verification of the term "flood factor deficiency" before any further assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

