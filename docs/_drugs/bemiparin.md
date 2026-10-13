---
layout: default
title: Bemiparin
parent: Low Evidence (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Bemiparin
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

# Bemiparin: From Anticoagulation (VTE Treatment and Prevention) to Primary Release Disorder of Platelets

## One-Sentence Summary

Bemiparin is a low molecular weight heparin (LMWH) anticoagulant, used for treating and preventing venous thromboembolism.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are **0 clinical trials** and **0 publications** supporting this prediction. The mechanism points the opposite way, because an anticoagulant would be expected to worsen a bleeding disorder.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records. The published literature describes bemiparin as indicated for deep vein thrombosis (with or without pulmonary embolism), VTE prophylaxis, and preventing clotting in the haemodialysis circuit. |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 98.71% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Bemiparin is a low molecular weight heparin that enhances antithrombin-mediated inhibition of factor Xa. This is an anticoagulant action.

Primary release disorder of platelets is a platelet function defect that causes bleeding. An anticoagulant does not correct a platelet release defect and would be expected to increase bleeding risk. No plausible therapeutic link is evident. The high score most likely reflects proximity in the knowledge graph (shared links to platelet and coagulation biology) rather than real therapeutic benefit.

The other top-ranked predictions are also platelet or bleeding disorders, with scores of 0.90 to 0.99:
- Glanzmann thrombasthenia
- pseudo-von Willebrand disease
- constitutional thrombocytopenia with haemorrhage
- collagen receptor defect bleeding diathesis
- Scott syndrome
- fetal and neonatal alloimmune thrombocytopenia
- platelet-type bleeding disorder
- autosomal dominant macrothrombocytopenia

The same mechanistic concern applies to all of them. None has clinical trial or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

Currently no related literature available for this predicted indication.

## Additional Note: The One Evidence-Backed Prediction (Rank 9, Pulmonary Embolism)

Among the 10 predictions, only **pulmonary embolism** (score 87.92%) has clinical evidence. It is rated L1 with a "Proceed with Guardrails" recommendation. This indication lies largely within bemiparin's known use as an anticoagulant, so it confirms an established use rather than a true repurposing.

**Clinical trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00219973](https://clinicaltrials.gov/study/NCT00219973) | Phase 3 | Completed | 526 | Randomised, double-blind trial of bemiparin 3,500 IU/day for 28 days vs 8 days as VTE prophylaxis after oncological abdominal/pelvic surgery |
| [NCT01164046](https://clinicaltrials.gov/study/NCT01164046) | Phase 3 | Terminated | 56 | Long-term treatment of cancer patients with DVT or PE. Terminated early, which limits its weight. |
| [NCT01727427](https://clinicaltrials.gov/study/NCT01727427) | N/A | Completed | 695 | Treatment of unsuspected pulmonary embolism in cancer patients |
| [NCT04420299](https://clinicaltrials.gov/study/NCT04420299) | Phase 2 | Terminated | 81 | Therapeutic vs prophylactic bemiparin dose in patients hospitalised with COVID-19 |
| [NCT01630148](https://clinicaltrials.gov/study/NCT01630148) | N/A | Completed | 774 | Randomised trial of bemiparin thromboprophylaxis after benign gynaecological surgery |
| [NCT01588171](https://clinicaltrials.gov/study/NCT01588171) | N/A | Completed | 7020 | Bemiparin vs enoxaparin thromboprophylaxis after vaginal and abdominal delivery |

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29214507](https://pubmed.ncbi.nlm.nih.gov/29214507/) | 2018 | RCT | Clin Drug Investig | Once-daily bemiparin vs twice-daily enoxaparin for acute DVT |
| [22242023](https://pubmed.ncbi.nlm.nih.gov/22242023/) | 2011 | RCT | Obstet Gynecol Int | Two bemiparin regimens (5 vs 10 days) for thromboprophylaxis after caesarean delivery in 646 women |
| [20384389](https://pubmed.ncbi.nlm.nih.gov/20384389/) | 2010 | RCT | Clin Drug Investig | ANCIANOS study of bemiparin thromboprophylaxis in elderly medical patients |
| [24657810](https://pubmed.ncbi.nlm.nih.gov/24657810/) | 2014 | Review | Vascul Pharmacol | Review of bemiparin as an effective and safe LMWH |
| [31030749](https://pubmed.ncbi.nlm.nih.gov/31030749/) | 2019 | Review | Prog Mol Biol Transl Sci | Overview of LMWHs and their clinical applications |
| [17532688](https://pubmed.ncbi.nlm.nih.gov/17532688/) | 2005 | Cohort | Clin Drug Investig | Prospective uncontrolled cohort on bemiparin use and safety in medical patients |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16463P | HIBOR Solution for Injection in Pre-filled Syringes 2,500 IU anti-Xa/0.2 mL | Injection, solution | Not stated in registration records |
| SIN16462P | HIBOR Solution for Injection in Pre-filled Syringes 3,500 IU anti-Xa/0.2 mL | Injection, solution | Not stated in registration records |

Both are valid single-ingredient licences. The manufacturer is ROVI Pharma Industrial Services, S.A.

## Safety Considerations

Please refer to the package insert for safety information.

Class-level cautions that apply to this prediction:
- Bemiparin is an anticoagulant and would be expected to increase bleeding risk, a particular concern in any bleeding or platelet disorder.
- LMWHs can rarely cause thrombocytopenia, which is especially relevant in patients who already have low platelet counts.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for primary release disorder of platelets rests on model score alone, with no trials or publications. The mechanism (anticoagulation) conflicts with the disease (a bleeding disorder). The same applies to the other platelet and bleeding disorders in the top ranks. The only evidence-backed prediction, pulmonary embolism, is an established use of bemiparin rather than new repurposing.

**To proceed, the following is needed:**
- Any mechanistic or preclinical rationale showing why an anticoagulant could benefit this platelet disorder. Without it, the prediction should not advance.
- Package insert warnings and contraindications from the Singapore regulator (HSA), plus detailed mechanism of action data.
- If the goal is a repurposing effort, redirect attention to the evidence-backed VTE-related indications. These would need approved-indication confirmation for the Singapore licences, renal function monitoring, bleeding risk assessment, platelet count monitoring for heparin-induced thrombocytopenia, and caution with neuraxial anaesthesia.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

