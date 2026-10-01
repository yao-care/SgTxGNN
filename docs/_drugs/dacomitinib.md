---
layout: default
title: Dacomitinib
parent: Low Evidence (L5)
nav_order: 293
evidence_level: L5
indication_count: 10
---

# Dacomitinib
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

# Dacomitinib: From Non-Small Cell Lung Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Dacomitinib is an oral pan-EGFR/HER inhibitor marketed in Singapore as Vizimpro, and it is used in lung cancer. The TxGNN model ranks **rheumatoid arthritis** as its top new-indication prediction, but **no clinical trials or publications** support it. Among the other predictions, only **pulmonary hypertension** has any supporting evidence, which is one animal study and one unrelated Phase 1 trial.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer (inferred from the trial context; the Singapore indication text was not supplied) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 97.79% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Dacomitinib is known as a pan-EGFR/HER tyrosine kinase inhibitor.

**Rheumatoid arthritis:** EGFR/ErbB signaling in synovial fibroblasts is a plausible but unverified link. The prediction is computational only, and the score is not clinical evidence.

**Pulmonary hypertension (rank 4, score 96.51%):** This is the best-supported alternative. EGFR/HER signaling drives pulmonary vascular smooth muscle proliferation and remodeling. A 2019 rat study reported that dacomitinib attenuated pulmonary vascular remodeling. This is animal-model evidence only, and no human pulmonary hypertension data exist. EGFR inhibitors also carry pulmonary toxicity such as interstitial lung disease, so a safety assessment would come first.

**Other predictions (ranks 2, 3, 5, 6, 7, 9, 10):** These include homozygous familial hypercholesterolemia, brachydactyly-syndactyly syndrome, nephrogenic syndrome of inappropriate antidiuresis, colobomatous microphthalmia-rhizomelic dysplasia syndrome, kyphoscoliotic heart disease, amyotrophic lateral sclerosis and leprosy. None has an identified mechanistic link or any supporting trial or literature.

## Clinical Trial Evidence

Rheumatoid arthritis has no registered trials. The trials below come from other predicted indications and are only indirectly relevant.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01121575](https://clinicaltrials.gov/study/NCT01121575) | Phase 1 | Completed | 70 | Dacomitinib plus crizotinib dose-escalation study in advanced NSCLC (listed under pulmonary hypertension). It has no pulmonary hypertension population and provides only general human safety and PK data. |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | SMMART PRIME personalized oncology platform (listed under multiple endocrine neoplasia). Only 2 patients were enrolled, and there is no interpretable efficacy or safety signal. |

## Literature Evidence

Rheumatoid arthritis has no supporting literature. The only publication supplied relates to pulmonary hypertension.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30753867](https://pubmed.ncbi.nlm.nih.gov/30753867/) | 2019 | Preclinical (animal model) | Eur J Pharmacol | Dacomitinib attenuated pulmonary vascular remodeling and pulmonary hypertension in hypoxia- and monocrotaline-induced rat models. Earlier EGFR inhibitors (gefitinib, erlotinib, lapatinib) had not been effective in this setting. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15965P | VIZIMPRO Film-Coated Tablet 45MG | Tablet, film coated |
| SIN15966P | VIZIMPRO Film-Coated Tablet 15MG | Tablet, film coated |
| SIN15967P | VIZIMPRO Film-Coated Tablet 30MG | Tablet, film coated |

All three are manufactured by Pfizer Manufacturing Deutschland GmbH and are for oral use.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

- **Pulmonary toxicity:** EGFR TKIs carry a risk of interstitial lung disease. This matters most for any exploration in pulmonary hypertension.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, rheumatoid arthritis, rests on the TxGNN score alone (L5) with no trials or literature. Pulmonary hypertension has the most support (L4, preclinical only), and it is best treated as a research question rather than a clinical candidate.

**To proceed, the following is needed:**
- The Singapore package insert (HSA) with warnings, contraindications and approved indications
- Detailed mechanism of action data (DrugBank)
- For rheumatoid arthritis, any preclinical or clinical evidence beyond the model score
- For pulmonary hypertension, confirmation of the animal findings and a pulmonary safety assessment before any human study
- Route compatibility and similarity-to-original assessments, which are still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

