---
layout: default
title: Nicotinamide
parent: Low Evidence (L5)
nav_order: 710
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Nicotinamide: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Acne, pellagra, beriberi"
monitor_inn: "Nicotinamide"
predicted_indications: ["zinc, elevated plasma", "isolated congenital adermatoglyphia", "Beare-Stevenson cutis gyrata syndrome", "Werner syndrome", "pyogenic arthritis-pyoderma gangrenosum-acne syndrome", "demodicidosis of sebaceous gland", "dyspepsia", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "inherited cutis laxa", "syndromic oculocutaneous albinism"]
---

# Nicotinamide
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

# Nicotinamide: From Acne to Elevated Plasma Zinc

## One-Sentence Summary

Nicotinamide (vitamin B3) is used for deficiency conditions such as pellagra and beriberi, and for acne.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but there are **0 clinical trials** and only **2 loosely related publications**, neither of which addresses this question.
This prediction is best treated as a model artifact, not an actionable lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, pellagra, beriberi (the Singapore licences list no indication text) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 97.83% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nicotinamide is a vitamin B3 form and a precursor of NAD+, a coenzyme central to cellular energy metabolism and redox balance. Its efficacy in niacin-deficiency states (pellagra) and in acne is established.

For elevated plasma zinc, no mechanistic link is evident. The two papers retrieved cover COVID-19 risk factors (hyperinsulinaemia, magnesium, vitamin D) and antioxidant enzymes in the kidneys of hypertensive rats. Neither addresses plasma zinc or nicotinamide as a treatment for it. Despite the high score, this looks like a graph-based prediction artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32938758](https://pubmed.ncbi.nlm.nih.gov/32938758/) | 2020 | Review | Open Heart | Rationale for managing COVID-19 through hyperinsulinaemia, magnesium, vitamin D and thrombosis. Does not address plasma zinc or nicotinamide therapy. |
| [15361776](https://pubmed.ncbi.nlm.nih.gov/15361776/) | 2004 | Preclinical (animal) | J Hypertens | Antioxidant enzymes (SOD, catalase, glutathione peroxidase) in the kidneys of hypertensive rats on an antioxidant-rich diet. Not relevant to the predicted indication. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05209P | SOLUVIT N FOR INFUSION | Powder for injection solution | Not specified |
| SIN11975P | CERNEVIT FOR INJECTION | Powder for injection solution | Not specified |

Both are valid single-ingredient registrations and are injectable only.

---

## Safety Considerations

- **Contraindications (knowledge-graph signals, not package-insert text):** The graph links nicotinamide to many conditions, including kidney disease, liver disease, gallbladder disease, peptic ulcer disease, diabetes mellitus, diabetic ketoacidosis, gout, blood coagulation disease, hemophilia, acute coronary syndrome, sickle cell anemia, thyroid gland disease, rhabdomyolysis, primary hyperoxaluria, and iron-metabolism disorders (hereditary hemochromatosis, hemosiderosis, Wilson disease). These need clinical verification against the label.
- **Drug Interactions:** 64 interactions were identified, mostly Moderate. The 20 listed in the data compiled for this report include:
  - Glucose-lowering drugs: metformin, chlorpropamide, acarbose, pioglitazone, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), DPP-4 inhibitors (alogliptin, linagliptin), and GLP-1 agonists (albiglutide, dulaglutide).
  - Oncology drugs: methotrexate, clofarabine, brentuximab vedotin, and asparaginase products.
  - Others: efavirenz, cannabidiol, and carbamazepine (Minor).

Package-insert warnings were not available, so please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not supported by any clinical trial, mechanistic data, or relevant publication. The only retrieved papers are off-target, so this is a model prediction only (L5).

**To proceed, the following is needed:**
- Evidence that nicotinamide affects plasma zinc, or a plausible mechanism for it
- Detailed mechanism of action data
- Package-insert warnings and contraindications from the Singapore authority
- Review of the diabetes and oncology drug interactions if any use is considered

**Alternative lead:** Among the other predictions, **Werner syndrome** (score 88.6%) has far stronger support. A 2025 double-blind randomized crossover trial of nicotinamide riboside, a related NAD+ precursor, was reported in Werner syndrome patients (PMID [40459998](https://pubmed.ncbi.nlm.nih.gov/40459998/)), alongside preclinical work on NAD+ depletion and mitophagy (PMIDs [31754102](https://pubmed.ncbi.nlm.nih.gov/31754102/), [40179319](https://pubmed.ncbi.nlm.nih.gov/40179319/)). The evidence concerns nicotinamide riboside, not nicotinamide itself, and the trial's design and outcomes need verification. It is a better candidate for further evaluation than elevated plasma zinc.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

