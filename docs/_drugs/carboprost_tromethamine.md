---
layout: default
title: Carboprost Tromethamine
parent: Low Evidence (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Carboprost Tromethamine
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

# Carboprost tromethamine: From Uterine Contraction (Obstetric Use) to Atypical Coarctation of Aorta

## One-Sentence Summary

Carboprost tromethamine is a prostaglandin F2-alpha (PGF2-alpha) analog whose known effects are uterine smooth muscle contraction and vasoconstriction. The TxGNN model predicts it may be effective for **atypical coarctation of aorta**, but there are **0 clinical trials** and **0 publications** supporting this prediction. The high score most likely reflects knowledge-graph topology rather than biology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA record (the approved indication text is blank); pharmacology points to obstetric uterine contraction |
| Predicted New Indication | Atypical coarctation of aorta |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, carboprost is a PGF2-alpha analog that contracts uterine smooth muscle and causes vasoconstriction. No mechanism has been documented that would make it applicable to atypical coarctation of aorta.

The predicted condition is a structural congenital aortic defect, and drugs cannot correct such defects. PGF2-alpha agonism offers no therapeutic rationale for it. Realistically, this is a knowledge-graph artefact and probably a false positive.

The other top predictions show the same pattern:
- **Aortic malformation and esophageal malformation:** no plausible mechanism.
- **Migraine (two entries):** prostaglandins are pro-nociceptive, and headache is a recognised adverse effect of carboprost, so the direction of benefit is doubtful.
- **Pulmonary hypertension:** carboprost causes pulmonary vasoconstriction, so this is more likely a harm signal than a benefit.
- **Amenorrhea:** the reproductive-tract link is conceivable, but carboprost induces uterine contraction and does not restore ovulatory cycles.
- **Primary hereditary glaucoma:** this is the only prediction with a class-level link. Topical PGF2-alpha analogs such as latanoprost lower intraocular pressure. That evidence does not extend to systemic carboprost, and the condition is usually treated surgically, so it stays a hypothesis-generating question.

## Clinical Trial Evidence

Currently no related clinical trials registered for atypical coarctation of aorta.

For reference, the only trial linked to any top-ranked prediction is [NCT04481503](https://clinicaltrials.gov/study/NCT04481503). It is a completed, N/A-phase observational echocardiography study of 150 women in labor, linked to aortic malformation (rank 2). It did not test carboprost, so it provides no efficacy evidence.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06722P | HEMABATE INJECTION 250 mcg/ml (Pharmacia & Upjohn Company LLC) | Injection | Not stated in the record |

## Safety Considerations

The Evidence Pack contains no package insert warnings, contraindications or drug interaction records (the DDI query returned no results). Please refer to the package insert for safety information.

The mechanism analysis raises these pharmacology-based concerns:
- Pulmonary vasoconstriction and bronchoconstriction, so caution is needed in cardiopulmonary disease.
- Common adverse effects include headache, nausea, vomiting and diarrhea.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no mechanistic basis, no clinical trials and no literature (evidence level L5). Several related predictions, such as pulmonary hypertension, conflict with carboprost's known pharmacology and may signal harm.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications (a blocking gap for safety screening).
- Mechanism of action data from DrugBank.
- For atypical coarctation of aorta, a credible mechanistic hypothesis; without one, further work is not justified.
- For primary hereditary glaucoma only, a literature review of PGF2-alpha analog evidence to decide whether the question is worth pursuing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

