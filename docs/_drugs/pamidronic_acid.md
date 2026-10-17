---
layout: default
title: Pamidronic Acid
parent: Low Evidence (L5)
nav_order: 759
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pamidronic Acid: predicted new indication HIV infectious disease (evidence level L5). Approved use: Humoral hypercalcemia of malignancy"
monitor_inn: "Pamidronic acid"
predicted_indications: ["HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "obsolete familial combined hyperlipidemia", "osteomesopyknosis", "cholelithiasis", "GNE myopathy"]
---

# Pamidronic Acid
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

# Pamidronic Acid: From Humoral Hypercalcemia of Malignancy to HIV Infectious Disease

## One-Sentence Summary

Pamidronic acid is a bisphosphonate originally used for humoral hypercalcemia of malignancy and Paget disease of bone (including juvenile Paget disease).
The TxGNN model predicts it may be effective for **HIV infectious disease**, with a very high model score but **0 clinical trials** and **0 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Humoral hypercalcemia of malignancy; Paget disease of bone; juvenile Paget disease (the Singapore licence record contains no indication text) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pamidronic acid is a nitrogen-containing bisphosphonate that inhibits osteoclast-mediated bone resorption. This is why it works in hypercalcemia of malignancy and Paget disease.

A possible but unverified link is that nitrogen-containing bisphosphonates inhibit farnesyl pyrophosphate synthase. This may affect prenylation-dependent pathways and gamma-delta T cell activity. HIV-associated bone loss is a separate, bone-related context. The data compiled for this report do not confirm any of these links.

The high TxGNN score is a model prediction only. Related predictions (feline AIDS and simian immunodeficiency virus infection) most likely mirror the HIV prediction through shared disease-ontology neighbours. They are not independent support.

**Other predicted indications in the data:**
- **Paget disease of bone** (score 96.64%): this is already an original indication, so it is not a true repurposing candidate. Five publications were supplied, all reviews, a drug news note or a case report, with no Phase 3 RCT. The evidence is graded L4 and the stage is "Research Question".
- **Paget disease of bone 2, early-onset** (score 92.96%): a genetic subtype with the same high-turnover bone pathology, so antiresorptive therapy is mechanistically plausible. No subtype-specific evidence was supplied (L5, Research Question).
- **Other predictions** (neurodevelopmental disorder, obsolete familial combined hyperlipidemia, osteomesopyknosis, cholelithiasis, GNE myopathy): no mechanistic support and no evidence. Antiresorptive therapy would be expected to worsen osteomesopyknosis, a high-bone-density disorder.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for HIV infectious disease.

For reference, the following publications relate to the Paget disease of bone prediction, which is already an approved-use context:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11503825](https://pubmed.ncbi.nlm.nih.gov/11503825/) | 1999 | Review / drug news | Prescrire International | Short-course IV pamidronic acid (180-210 mg total) approved in France for Paget disease. Only non-comparative data, with clinical benefit and biochemical improvement. |
| [2078998](https://pubmed.ncbi.nlm.nih.gov/2078998/) | 1990 | Review | Drugs | Potent bisphosphonates can restore and maintain normal bone turnover in Paget disease. Discusses treatment indications and disease-activity markers. |
| [15799218](https://pubmed.ncbi.nlm.nih.gov/15799218/) | 2002 | Review | Treatments in Endocrinology | Overview of how Paget disease therapy has evolved, with a focus on bisphosphonates. |
| [7858370](https://pubmed.ncbi.nlm.nih.gov/7858370/) | 1994 | Review (etidronic acid, a different bisphosphonate) | Drugs & Aging | Etidronic acid rapidly lowers bone turnover markers in Paget disease. Not specific to pamidronic acid. |
| [14750233](https://pubmed.ncbi.nlm.nih.gov/14750233/) | 2003 | Case report (adverse effect) | Bulletin de la Société belge d'ophtalmologie | Two cases of posterior uveitis with pamidronate. Ocular adverse effects are rare but documented. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11543P | PAMISOL CONCENTRATED INJECTION 30 mg/10 ml (Hospira Australia Pty Ltd) | Injection | Not stated in the licence record |

## Cytotoxicity

Pamidronic acid is a bisphosphonate and is not an antineoplastic drug. It is used as supportive care for hypercalcemia of malignancy. This section does not apply.

## Safety Considerations

**Contraindication-related conditions from the knowledge graph** (these are model-graph associations, not package insert text):
kidney disease, pyoureter, potassium deficiency disease, hypercalcemia disease, nephrocalcinosis, phosphorus metabolism disease, periodontitis, osteonecrosis of the jaw, hypophosphatemia.

**Drug Interactions**: 100 interactions were identified. The 20 shown in the data include the following.
- **Moderate**: amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), mesalazine, acetylsalicylic acid, balsalazide, olsalazine, sulfasalazine, vancomycin, kanamycin, neomycin, streptomycin, polymyxin B, exenatide.
- **Unknown severity**: calcitriol, doxycycline, clotrimazole, pantoprazole, sucralfate.

Several of the moderate-level agents are nephrotoxic or ototoxic, so renal function monitoring is advisable when they are combined.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV prediction has a high model score but no clinical trials, no literature and no established mechanism (L5). The related animal-virus predictions appear to be artifacts of the same ontology neighbourhood. The Paget disease predictions overlap with existing indications and are not new repurposing opportunities.

**To proceed, the following is needed:**
- Mechanism of action data, to assess the proposed link to HIV
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- A targeted literature and trial search on bisphosphonates in HIV, particularly HIV-associated bone loss and gamma-delta T cell effects
- Approved indication text for the Singapore licence SIN11543P
- Evaluation of the kidney disease and osteonecrosis of the jaw associations in people living with HIV, who often take nephrotoxic antiretrovirals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

