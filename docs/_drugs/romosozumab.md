---
layout: default
title: Romosozumab
parent: Low Evidence (L5)
nav_order: 881
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Romosozumab: predicted new indication Obsolete vitamin D deficiency (evidence level L5). Approved use: Postmenopausal osteoporosis / osteoporosis"
monitor_inn: "Romosozumab"
predicted_indications: ["obsolete vitamin D deficiency", "calcium-alkali syndrome", "primary bone dysplasia with defective bone mineralization", "severe nonproliferative diabetic retinopathy", "renal osteodystrophy", "osteomalacia (disease)", "autosomal dominant neovascular inflammatory vitreoretinopathy", "Worth syndrome", "impaired renal function disease"]
---

# Romosozumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Romosozumab: From Postmenopausal Osteoporosis to Obsolete Vitamin D Deficiency

## One-Sentence Summary

Romosozumab is a sclerostin-inhibiting antibody originally used to treat postmenopausal osteoporosis.
The TxGNN model predicts it may be effective for **obsolete vitamin D deficiency**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on model output alone, and the disease term is flagged as obsolete.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis / osteoporosis |
| Predicted New Indication | Obsolete vitamin D deficiency |
| TxGNN Prediction Score | 97.83% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Romosozumab is an anti-sclerostin monoclonal antibody. By blocking sclerostin, it releases the brake on Wnt signalling in bone, which supports bone formation. Its efficacy in postmenopausal osteoporosis is established.

The high score is most likely driven by network proximity between osteoporosis and other bone and mineral metabolism disorders in the knowledge graph. Mechanistically, the link is weak. Romosozumab does not correct vitamin D status. In practice, vitamin D and calcium repletion is a prerequisite for using it, not something it treats. The disease term is also flagged as obsolete, which further weakens the prediction.

Other predictions in this set have more support than this one. The strongest is **osteoporosis treatment in patients with impaired renal function**, which has a Phase 1 trial and several publications (see Conclusion).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16208P | EVENITY Solution for Injection in Pre-filled Syringe 105 mg/1.17 mL | Injection, solution |

The product is a single-ingredient injectable (1 valid registration, none cancelled). The manufacturer is Patheon Italia S.p.A.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): hypercalcaemia, nephrocalcinosis, and phosphorus metabolism disease.
- **Drug interactions**: 29 interactions were identified, and 20 are detailed in the data compiled for this report.
  - **Major**: etelcalcetide.
  - **Moderate, corticosteroids**: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisone, prednisolone, methylprednisolone, deflazacort, fludrocortisone.
  - **Moderate, other agents**: axitinib, bevacizumab, cabozantinib, dasatinib, lenalidomide, pazopanib, pomalidomide, ramucirumab, regorafenib.
- **Other points raised in the evidence review** for related predictions: romosozumab carries a cardiovascular warning (myocardial infarction, stroke) and can cause hypocalcaemia.

For full warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or literature behind it, and the mechanism does not fit. Romosozumab does not treat vitamin D deficiency, and the disease term is obsolete. The score most likely reflects graph proximity, not a real therapeutic signal.

**Context from other predictions in this set:**
- **Impaired renal function (osteoporosis treatment in renal impairment)** is the strongest signal, at Evidence Level L2 and "Proceed with Guardrails".
  - Support comes from a Phase 1 study (NCT01833754, n=24) and post hoc analyses of the FRAME and ARCH Phase 3 trials.
  - It would need to be framed as osteoporosis treatment in patients with renal impairment, not treatment of kidney disease.
  - Use should be restricted to mild-to-moderate impairment, with calcium and vitamin D monitoring and cardiovascular risk screening.
- **Renal osteodystrophy** and **pregnancy-associated osteoporosis** are at L4 ("Research Question"). They are supported only by reviews and case reports.
- The remaining predictions have no supporting evidence and should stay on Hold.

**To proceed, the following is needed:**
- Review of this prediction's relevance, or replacement with the better-supported renal impairment indication
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the Health Sciences Authority (HSA), which are required before any safety screening
- Approved indication text for the Singapore registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

