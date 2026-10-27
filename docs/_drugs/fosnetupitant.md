---
layout: default
title: Fosnetupitant
parent: Low Evidence (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fosnetupitant: predicted new indication Leprosy (evidence level L5). Approved use: Not available in the data compiled for this report (the registered pr…"
monitor_inn: "Fosnetupitant"
predicted_indications: ["leprosy", "mycotic corneal ulcer", "coronary artery disease", "anomalous left coronary artery from the pulmonary artery", "candidiasis", "myocardial ischemia", "uterine polyp", "polyp of vocal cord", "polyp of middle ear", "polyp of ureter"]
---

# Fosnetupitant
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

## Fosnetupitant: From Chemotherapy-Related Nausea and Vomiting to Leprosy
{: .text-alpha }

## One-Sentence Summary

Fosnetupitant is a prodrug of netupitant, an NK1 receptor antagonist. It is registered in Singapore as an intravenous product (Akynzeo® IV), and its approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **leprosy**, but **no clinical trials and no publications** currently support this prediction.
It is a purely computational signal and should be treated as a hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the registered product is an NK1 antagonist antiemetic) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 96.44% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, fosnetupitant is converted in the body to netupitant, which blocks the neurokinin-1 (NK1) receptor, the target of substance P. This is the basis for its use in preventing nausea and vomiting caused by chemotherapy.

The link to leprosy is speculative. One conceivable route is substance P and neurogenic inflammation in the nerve damage seen in leprosy. However, no study in the data compiled for this report tests this idea, and NK1 antagonism has no established activity against *Mycobacterium leprae*. The score of 96.44% reflects model-based similarity in a knowledge graph, not biological or clinical proof.

Other top predictions include mycotic corneal ulcer, coronary artery disease, candidiasis, myocardial ischemia and several polyp-type conditions. Several of these have no plausible mechanism, which suggests the model may be picking up graph-neighbourhood artefacts. This lowers confidence in the leprosy prediction as well.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16899P | Akynzeo® IV Concentrate for Solution for Infusion 235 mg/0.25 mg/vial (Baxter Oncology GmbH) | Infusion, solution concentrate | Not stated in the registration data |

## Safety Considerations

- **Drug Interactions**: 98 interacting drugs were identified. Netupitant is a CYP3A4 inhibitor, which is the likely reason for many of them. Examples by severity:
  - **Major**: Eliglustat, Naloxegol
  - **Moderate**: Aprepitant, Granisetron, corticosteroids (dexamethasone, betamethasone, budesonide, hydrocortisone, prednisolone, prednisone, triamcinolone), Repaglinide, Saxagliptin, Simvastatin, Tinidazole, Naldemedine, Nitisinone, Troglitazone
  - **Minor**: Cobicistat

  Many leprosy patients would be on multi-drug regimens, and corticosteroids are commonly used for leprosy reactions. These overlaps would need careful review.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The leprosy prediction rests only on a computational score. There are no clinical trials or publications, the mechanism is speculative, and package insert safety data has not yet been reviewed. This is an L5 candidate and does not justify moving forward at this time.

**To proceed, the following is needed:**
- Retrieve and review the HSA package insert for warnings, contraindications and approved indication
- Obtain DrugBank mechanism of action data
- Search for preclinical evidence (for example, substance P/NK1 in leprosy nerve injury or inflammation)
- Assess route and formulation fit, since the registered product is intravenous only
- Review the drug interaction burden against standard leprosy therapy and corticosteroids used for leprosy reactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

