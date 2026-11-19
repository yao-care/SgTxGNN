---
layout: default
title: Panitumumab
parent: Low Evidence (L5)
nav_order: 760
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
monitor_inn: "Panitumumab"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy"]
description: "Panitumumab: predicted new indication Drug-induced osteoporosis (evidence level L5). In Singapore: 1 HSA registration (1 valid)"
---

# Panitumumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Panitumumab: Drug-induced osteoporosis
{: .text-alpha }

## One-Sentence Summary

Panitumumab is an anti-EGFR monoclonal antibody originally used for metastatic colon cancer.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**,
but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 0.9913 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for panitumumab: "The EGFR is a transmembrane glycoprotein that is a member of a subfamily of type I receptor tyrosine kinases, including EGFR, HER2, HER3, and HER4. EGFR is constitutively expressed in normal epithelial tissues, including the skin and hair follicle. […] Panitumumab binds specifically to EGFR on both normal and tumor cells, and competitively inhibits the binding of ligands for EGFR." ([DailyMed: Vectibix (panitumumab) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e0fa4bca-f245-4d92-ae29-b0c630a315c2), label version 2026-06-23; accessed 2026-11-19.) Panitumumab is known to be an anti-EGFR monoclonal antibody, and its efficacy in metastatic colon cancer is the basis of its original use.

EGFR signalling plays a role in osteoblast differentiation and bone remodelling, so a theoretical link to bone metabolism exists. However, the likely direction of effect is unfavourable: EGFR blockade is more likely to impair bone formation. Panitumumab is also associated with hypomagnesaemia and hypocalcaemia, which could worsen bone health. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and the mechanism does not clearly support benefit.

The other top-ranked prediction is an eye condition (severe nonproliferative diabetic retinopathy), at L5 with no trials or literature. Its rationale is weak or contradictory. Anti-EGFR antibodies also cause known ocular toxicities (keratitis, conjunctivitis), and a large intravenous antibody is not expected to penetrate the eye well.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN14498P | Vectibix Concentrate for Solution for Infusion 100 mg/vial | INFUSION, SOLUTION CONCENTRATE | Valid |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Electrolytes (magnesium, calcium) are relevant given the known effects; please refer to the package insert for the full list |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 27 interactions were identified in total. Those listed include:
  - **Major**: amiodarone, arsenic trioxide, bevacizumab, dofetilide, dronedarone, droperidol, irinotecan (including liposomal), levacetylmethadol, aminolevulinic acid
  - **Moderate**: proton pump inhibitors (rabeprazole, omeprazole, dexlansoprazole, esomeprazole, lansoprazole, pantoprazole), methoxsalen, topical aminolevulinic acid, disopyramide, idelalisib
- **Class-related effects noted in the mechanistic review**: hypomagnesaemia, hypocalcaemia, and ocular toxicities (keratitis, ulcerative keratitis, conjunctivitis).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials or literature (L5). The mechanistic review suggests EGFR blockade and panitumumab's calcium and magnesium effects could worsen rather than improve bone health. The same applies to the other predicted indications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, so safety screening can be done
- Mechanism of action data from DrugBank
- Preclinical or observational evidence on EGFR inhibition and bone metabolism, including the direction of effect
- Review of the benefit-risk balance of a systemic oncology biologic for a non-oncology bone indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vectibix (panitumumab) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e0fa4bca-f245-4d92-ae29-b0c630a315c2) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

