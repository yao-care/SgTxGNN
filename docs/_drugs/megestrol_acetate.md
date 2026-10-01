---
layout: default
title: Megestrol Acetate
parent: High Evidence (L1-L2)
nav_order: 636
evidence_level: L2
indication_count: 10
---

# Megestrol Acetate
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Megestrol Acetate: From an Unrecorded Original Indication to Uterine Corpus Endometrial Carcinoma

## One-Sentence Summary

Megestrol acetate is a synthetic progestin, sold in Singapore as oral tablets. The Singapore registration records do not state its approved indication.
The TxGNN model predicts it may be effective for **uterine corpus endometrial carcinoma**, with **3 clinical trials** and **no publications** retrieved for this indication.
Progestins are already used as hormonal therapy in endometrial cancer, so this may be closer to an established use than a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records |
| Predicted New Indication | Uterine corpus endometrial carcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this record. Megestrol acetate is a synthetic progestin. Progestins can slow the growth of hormone-receptor-positive endometrial tissue and push it toward differentiation. Estrogen drives the growth of many endometrial cancer cells, and progestin therapy works against that stimulation.

Because megestrol is already used as hormonal therapy in endometrial cancer, this prediction may reflect an established use rather than a new one. The original indication and mechanism fields in the record are empty, so this should be checked against the approved label before any repurposing claim is made.

The other nine predicted indications are much weaker. Most are supported only by the model score, or only by indirect hormone-receptor rationale. The exception is ovarian cancer, whose retrieved trials mostly concern endometrial cancer. This report focuses on the top-ranked prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00503581](https://clinicaltrials.gov/study/NCT00503581) | Phase 2 | Terminated | 9 | Randomized comparison of continuous vs sequential progestin (megestrol) therapy in endometrial intraepithelial neoplasia or atypical hyperplasia, for patients wanting uterine preservation. It tests the drug class directly, but only 9 patients enrolled, so conclusions are weak. |
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Completed | 73 | Temsirolimus alone vs temsirolimus plus hormonal therapy (megestrol acetate and tamoxifen) in advanced, persistent or recurrent endometrial carcinoma. Megestrol appears to be part of a combination arm rather than the investigational agent. The arm structure needs manual confirmation. |
| [NCT04046185](https://clinicaltrials.gov/study/NCT04046185) | Early Phase 1 | Unknown | 60 | PD-1 inhibitor plus progesterone vs progesterone alone in early-stage endometrial cancer for patients who want to preserve fertility. It is exploratory, and the contribution of megestrol specifically is unclear. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN10157P | APO-MEGESTROL TABLET 160 mg (Apotex Inc) | Tablet |
| SIN10156P | APO-MEGESTROL TABLET 40 mg (Apotex Inc) | Tablet |

Both products are oral tablets. The registration records do not state an approved indication.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The model score is very high, and one completed randomized Phase 2 trial includes a megestrol-containing regimen in endometrial carcinoma. However, that trial's megestrol arm is a combination, and the trial that tests the drug class directly was terminated after 9 patients. No publications were retrieved, so the evidence is moderate at best.

**To proceed, the following is needed:**
- The Singapore package insert (HSA), covering approved indications, warnings and contraindications. The lack of safety data currently blocks safety screening.
- Mechanism-of-action data, for example from DrugBank.
- A check of the label to establish whether endometrial cancer is already an approved use, which would make this an established use rather than repurposing.
- Manual confirmation of the arm structure in NCT00729586.
- A targeted literature search for megestrol in endometrial carcinoma, since none was retrieved.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

