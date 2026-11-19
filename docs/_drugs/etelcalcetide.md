---
layout: default
title: Etelcalcetide
parent: Medium Evidence (L3-L4)
nav_order: 405
evidence_level: L4
indication_count: 4
last_modified_at: 2026-11-20
monitor_inn: "Etelcalcetide"
predicted_indications: ["hyperphosphatemia (disease)", "esophageal varices without bleeding", "esophageal varices with bleeding", "varicose disease"]
description: "Etelcalcetide: predicted new indication Hyperphosphatemia (disease) (evidence level L4). In Singapore: 3 HSA registrations (3 valid)"
---

# Etelcalcetide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

## Etelcalcetide: Hyperphosphatemia (disease)
{: .text-alpha }

## One-Sentence Summary

Etelcalcetide is an intravenous calcimimetic that activates the calcium-sensing receptor and is already marketed in Singapore.
The TxGNN model predicts it may be useful for **hyperphosphatemia**.
Currently **0 registered clinical trials** and **6 publications** touch on this direction, and only one of them, a 2026 preclinical study, directly studies hyperphosphatemia. The evidence level is therefore **L4**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hyperphosphatemia (disease) |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L4 |
| Singapore Market Status | Marketed (valid licences: 3 of 3) |
| Number of Registrations | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Etelcalcetide activates the calcium-sensing receptor (CaSR) and lowers parathyroid hormone (PTH). According to the Mechanism of Action section of the US FDA-approved prescribing information for etelcalcetide: "Etelcalcetide is a calcimimetic agent that allosterically modulates the calcium-sensing receptor (CaSR). Etelcalcetide binds to the CaSR and enhances activation of the receptor by extracellular calcium. Activation of the CaSR on parathyroid chief cells decreases PTH secretion." ([DailyMed: Parsabiv (etelcalcetide) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd270093-c6a8-4596-a4ab-e6aa0a2c8a0c), label version 2026-03-08; accessed 2026-11-19.) The mechanistic rationale below comes from the evidence review.

Lower PTH can indirectly improve mineral metabolism, including calcium, phosphate and FGF23. Hyperphosphatemia is closely tied to the disturbances this drug already addresses, so the biological link is plausible.

The effect is probably indirect and secondary to PTH suppression, not a direct phosphate-lowering action. A 2026 preclinical study (PMID 42044867) reports that etelcalcetide restored cardiac function in chronic hyperphosphatemia through CaSR-cAMP activation. This suggests a possible organ-protective benefit, but it does not show that the drug lowers phosphate in patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33305109](https://pubmed.ncbi.nlm.nih.gov/33305109/) | 2020 | RCT | Kidney Int Rep | DUET trial: prospective randomized study of intravenous etelcalcetide in haemodialysis patients, assessing control of mineral and bone disorder. Not specific to hyperphosphatemia. |
| [29440923](https://pubmed.ncbi.nlm.nih.gov/29440923/) | 2018 | Review | Int J Nephrol Renovasc Dis | Reviews etelcalcetide given at the end of haemodialysis. It effectively reduces PTH in clinical trials with thrice-weekly dosing. |
| [42495460](https://pubmed.ncbi.nlm.nih.gov/42495460/) | 2026 | Review | Cureus | Narrative review of calcimimetics, vitamin D analogs and phosphate binders in dialysis patients. Phosphate retention is a key driver of mineral disturbance. |
| [42044867](https://pubmed.ncbi.nlm.nih.gov/42044867/) | 2026 | Preclinical/mechanistic study | Kidney Int | Etelcalcetide restored cardiac function in chronic hyperphosphatemia via CaSR-cAMP activation. This is the only study directly addressing the predicted disease. |
| [42853437](https://pubmed.ncbi.nlm.nih.gov/42853437/) | 2026 | Case report | CEN Case Rep | Uremic tumoral calcinosis regressed after a switch from cinacalcet to etelcalcetide in a haemodialysis patient without severe hyperphosphatemia. |
| [33211001](https://pubmed.ncbi.nlm.nih.gov/33211001/) | 2021 | Case report | Clin Nephrol | Temporary metastatic pulmonary calcification in a peritoneal dialysis patient, illustrating ectopic calcification in this setting. |

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN15450P | PARSABIV SOLUTION FOR INJECTION 2.5 mg/0.5 mL | INJECTION, SOLUTION | Valid |
| SIN15451P | PARSABIV SOLUTION FOR INJECTION 5 mg/mL | INJECTION, SOLUTION | Valid |
| SIN15452P | PARSABIV SOLUTION FOR INJECTION 10 mg/2 mL | INJECTION, SOLUTION | Valid |

<!-- licenses:end -->

All three authorizations are currently valid. The manufacturers are Patheon Manufacturing Services LLC and Amgen Manufacturing Limited LLC.

---

## Safety Considerations

- **Drug Interactions**: 21 interactions were identified. 20 are rated Major and 1 is rated Moderate (burosumab). Main groups:
  - Other calcimimetic: cinacalcet
  - Bisphosphonates: alendronic acid, risedronic acid, ibandronate, pamidronic acid, zoledronic acid, etidronic acid, tiludronic acid
  - Bone-active biologics and hormones: denosumab, romosozumab, salmon calcitonin
  - Loop diuretics: furosemide, bumetanide, torasemide, etacrynic acid
  - Others: cisplatin, foscarnet, pentamidine, amifostine

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9942), and the biological rationale is plausible through indirect PTH-mediated effects. However, direct support for hyperphosphatemia is limited to one preclinical study, and no registered trials address it. Evidence is therefore L4.

**To proceed, the following is needed:**
- Clinical data, ideally a controlled trial, with serum phosphate as a primary or key secondary endpoint
- Analysis of whether any phosphate effect is independent of PTH and calcium changes
- Package insert warnings and contraindications from the HSA for a safety review
- Review of the interaction profile, especially with other calcium-lowering agents, in the intended population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action text is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Parsabiv (etelcalcetide) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd270093-c6a8-4596-a4ab-e6aa0a2c8a0c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

