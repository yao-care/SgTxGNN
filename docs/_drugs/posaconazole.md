---
layout: default
title: Posaconazole
parent: Low Evidence (L5)
nav_order: 800
evidence_level: L5
indication_count: 10
---

# Posaconazole
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

# Posaconazole: From Antifungal Use to Pneumocystosis

## One-Sentence Summary

Posaconazole is an azole antifungal marketed in Singapore, but the registration records provided do not state its approved indications.
The TxGNN model predicts it may be effective for **pneumocystosis**, but the mechanism does not support this, and **no clinical trial or publication** tests posaconazole for this condition.
Two registered trials are only loosely related, and the high score is probably a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records (posaconazole is an azole antifungal) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 (model prediction only; no study tests posaconazole for this indication) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Posaconazole inhibits fungal sterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis in the fungal cell membrane. This is how azole antifungals work.

The prediction is **hard to justify mechanistically**. *Pneumocystis* has little or no ergosterol in its membrane, so azoles are not expected to be effective. The very high score (0.998) is therefore probably a knowledge-graph artifact and not a real pharmacological signal.

Among the other predicted indications, **vulvovaginal candidiasis** (rank 2, score 98.92%) is mechanistically much more plausible, because Candida species depend on ergosterol and azoles are an established class for this disease. The retrieved literature on it is limited to in vitro susceptibility studies, epidemiology and case reports. It contains no clinical efficacy data for posaconazole.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Active, not recruiting | 602 | Rezafungin vs standard antimicrobial regimen to prevent invasive fungal disease after allogeneic transplant. Posaconazole probably sits in the comparator arm and is not tested for pneumocystosis. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform protocol comparing GVHD prophylaxis drug combinations after mismatched unrelated-donor stem cell transplant. Posaconazole likely appears only as background prophylaxis, so this gives no direct evidence. |

Neither trial tests posaconazole for pneumocystosis. Arm composition should be checked against the registry records.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN13654P | NOXAFIL ORAL SUSPENSION 40 mg/ml | Suspension |
| SIN15045P | NOXAFIL TABLET 100MG | Tablet, delayed release |
| SIN15897P | POSACONAZOLE SANDOZ GASTRO-RESISTANT TABLETS 100MG | Tablet, delayed release |
| SIN16477P | SINOTRX POSACONAZOLE DELAYED RELEASE TABLET 100MG | Tablet, delayed release |
| SIN17200P | POSATIF POSACONAZOLE GASTRO-RESISTANT TABLETS 100MG | Tablet, delayed release |

The approved indication text is not available for any of these authorizations.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trial or literature evidence, and the mechanism argues against it because *Pneumocystis* lacks ergosterol. The 99.77% score should not drive any development decision on its own.

**To proceed, the following is needed:**
- The HSA package insert, to confirm the approved indications and the safety profile (warnings, contraindications)
- Review of the NCT04368559 registry record to confirm which agents are in the comparator arm
- Reprioritisation toward **vulvovaginal candidiasis**, particularly azole-resistant or non-albicans isolates, which would need a clinical trial

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

