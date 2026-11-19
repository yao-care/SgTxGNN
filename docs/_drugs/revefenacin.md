---
layout: default
title: Revefenacin
parent: Low Evidence (L5)
nav_order: 863
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Revefenacin: predicted new indication Bronchitis (evidence level L5). Approved use: Chronic obstructive pulmonary disease (COPD)"
monitor_inn: "Revefenacin"
predicted_indications: ["bronchitis"]
---

# Revefenacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Revefenacin: From Chronic Obstructive Pulmonary Disease to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Revefenacin is a once-daily nebulized long-acting muscarinic antagonist (LAMA), originally used for maintenance treatment of chronic obstructive pulmonary disease (COPD).
The TxGNN model predicts it may be effective for **bronchitis**, but only **1 clinical trial** is linked to this prediction. That trial was run in COPD patients, not a bronchitis-specific population, and **no publications** are linked to it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic obstructive pulmonary disease (COPD) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 (as scored; the supporting evidence is indirect, see below) |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Revefenacin is a lung-selective LAMA. By blocking M3 muscarinic receptors, it reduces cholinergic bronchoconstriction and mucus secretion. Both are plausibly relevant to chronic bronchitis.

Chronic bronchitis and COPD overlap clinically, and chronic bronchitis is one of the main COPD phenotypes. The high score (0.9961) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence for bronchitis. The one linked trial (NCT01704404) enrolled COPD patients, so it does not show efficacy in a bronchitis-specific population.

According to the Mechanism of Action section of the US FDA-approved prescribing information for revefenacin: "Revefenacin is a long-acting muscarinic antagonist, which is often referred to as an anticholinergic. It has similar affinity to the subtypes of muscarinic receptors M1 to M5. In the airways, it exhibits pharmacological effects through inhibition of M3 receptor at the smooth muscle leading to bronchodilation." ([DailyMed: Yupelri (revefenacin) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6dfebf04-7c90-436a-9b16-750d3c1ee0a6), label version 2022-05-03; accessed 2026-11-19.) The mechanistic reasoning above is therefore based on the drug's known pharmacological class.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01704404](https://clinicaltrials.gov/study/NCT01704404) | Phase 2 | Completed | 62 | 7-day multiple-dose study of TD-4208 (revefenacin) characterizing dose response, safety and pharmacokinetics in COPD. It is a dose-finding study that does not target bronchitis specifically, so it gives only indirect support. |

---

## Literature Evidence

Currently no related literature available for bronchitis.

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN16336P | YUPELRI® INHALATION SOLUTION 175MCG/3ML | SOLUTION | Valid |

<!-- licenses:end -->

The registration is a valid single-ingredient product. No approved indication text is recorded for it in the data compiled for this report.

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interactions in total. The 20 reviewed were all rated Moderate. Most are other anticholinergic or antimuscarinic agents, where additive anticholinergic effects would be expected:
  - Atropine, hyoscyamine, scopolamine
  - Glycopyrronium (including topical), trospium
  - Clidinium, dicyclomine, mepenzolate
  - Methscopolamine, propantheline
  - Other moderate-level interactions include promethazine, cobicistat, eluxadoline, obeticholic acid, prucalopride, eltrombopag, artesunate and abiraterone.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests on one early-phase trial in COPD patients, with no bronchitis-specific trials or publications. The high model score most likely reflects the overlap between chronic bronchitis and COPD. Revefenacin's strong evidence is for COPD, which is already its approved use.

**To proceed, the following is needed:**
- Bronchitis-specific clinical or observational data, for example a trial in a chronic bronchitis phenotype
- Package insert warnings and contraindications from the HSA record, to enable safety screening
- Detailed mechanism-of-action data (MOA)
- Confirmation of the approved indication wording for the Singapore registration (SIN16336P)

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data from DrugBank is currently unavailable" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Yupelri (revefenacin) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6dfebf04-7c90-436a-9b16-750d3c1ee0a6) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

