---
layout: default
title: Megestrol Acetate
parent: High Evidence (L1-L2)
nav_order: 642
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Megestrol Acetate: predicted new indication Uterine corpus endometrial carcinoma (evidence level L2). Approved use: Endometrial carcinoma"
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

# Megestrol Acetate: From Endometrial Carcinoma to Uterine Corpus Endometrial Carcinoma

## One-Sentence Summary

Megestrol acetate is a synthetic progestin, originally used as hormonal therapy for endometrial carcinoma.
The TxGNN model predicts it may be effective for **uterine corpus endometrial carcinoma**, with a very high score.
This is essentially the same disease as the original indication, so the prediction is not a true repurposing finding. Support consists of **1 clinical trial** (a randomized Phase 2) and **no indexed publications** for this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometrial carcinoma (the Singapore licence records contain no indication text, so this comes from the drug's known indications) |
| Predicted New Indication | Uterine corpus endometrial carcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Megestrol acetate is a synthetic progestin. Progesterone-receptor signalling is known to induce differentiation and growth inhibition in hormone-receptor-positive endometrioid tumours, which is why progestins are an established hormonal therapy for endometrial cancer.

The predicted disease, uterine corpus endometrial carcinoma, is the same disease as the original indication under a different name. The model's high score is therefore expected, and it largely reflects the drug's existing use. It does not point to a new therapeutic opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Completed | 73 | Randomized trial of temsirolimus alone versus a hormonal regimen (megestrol acetate plus tamoxifen) combined with temsirolimus in advanced, persistent or recurrent endometrial carcinoma. The primary question was temsirolimus efficacy, not megestrol itself. |

---

## Literature Evidence

Currently no related literature available for this predicted indication.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN10157P | APO-MEGESTROL TABLET 160 mg (Apotex Inc) | Tablet |
| SIN10156P | APO-MEGESTROL TABLET 40 mg (Apotex Inc) | Tablet |

Both are valid single-ingredient oral licences. Approved indication text is not recorded for either product.

---

## Cytotoxicity

Megestrol acetate is used in cancer treatment, but it is a hormonal agent rather than a conventional cytotoxic drug.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (progestin), not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Not a recognised feature of this drug class; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; the contraindication signals below (blood glucose, blood pressure, liver and renal function, adrenal function) suggest relevant areas |
| Handling Protection | Please refer to the package insert and local handling policy |

---

## Safety Considerations

- **Contraindications (knowledge-graph signals, not label text):** The TxGNN knowledge graph links megestrol acetate to the following conditions:
  - Hypertension
  - Kidney disease
  - Liver disease
  - Gallbladder disease
  - Hyperglycaemia, diabetes mellitus and diabetic ketoacidosis
  - Adrenocortical insufficiency and Addison disease
  - Male hypogonadism and eunuchism
  - Premature menopause
  - Androgen insensitivity syndrome
  - Pyoureter
- **Drug Interactions:** The interaction screen returned 100 interactions, and all 20 shown are rated Moderate. Most involve glucose-lowering drugs:
  - Metformin, pioglitazone and acarbose
  - DPP-4 inhibitors (sitagliptin, saxagliptin, linagliptin, alogliptin)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin)
  - GLP-1 agonists (semaglutide, dulaglutide, albiglutide)
  - Sulfonylureas and glinides (chlorpropamide, glimepiride, repaglinide)
  - Insulins (aspart, degludec)

  Other interacting drugs include aprepitant and clarithromycin. Blood glucose should be monitored closely when megestrol is combined with these agents.

Package insert warnings and contraindications have not been obtained. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication duplicates the existing endometrial carcinoma indication, so it adds no repurposing value. The only supporting trial was designed to test temsirolimus rather than megestrol. Although the evidence level is formally L2, it is weak for this question. Official label safety data is also missing.

**To proceed, the following is needed:**
- Redefine the question toward a genuinely new indication. Among the other predictions, ovarian cancer (a completed Phase 3 trial plus several Phase 2 studies of high-dose megestrol) is the most evidence-supported lead, though the literature suggests only modest activity.
- Obtain and review the HSA package insert for warnings and contraindications.
- Obtain detailed mechanism-of-action data.
- Verify the Singapore-approved indication wording, since it is not recorded in the licence data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

