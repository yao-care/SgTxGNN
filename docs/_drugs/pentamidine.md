---
layout: default
title: Pentamidine
parent: Low Evidence (L5)
nav_order: 775
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Pentamidine: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Pneumocystosis, human African trypanosomiasis, trypanosomiasis"
monitor_inn: "pentamidine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "neurotrophic keratopathy", "exposure keratitis", "non-human animal disease", "congenital analbuminemia"]
---

# Pentamidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Pentamidine: From Pneumocystosis and Trypanosomiasis to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Pentamidine is an injectable antimicrobial originally used to treat pneumocystosis and human African trypanosomiasis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pneumocystosis, human African trypanosomiasis, trypanosomiasis (the Singapore licence text for the approved indication is blank) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pentamidine is an antimicrobial with antiprotozoal and antifungal activity. Its efficacy in pneumocystosis and trypanosomiasis is established, and a speculative link to punctate epithelial keratoconjunctivitis would be an anti-infective or anti-inflammatory effect on the ocular surface.

This link is not supported by any trial or publication in the data compiled for this report. The high score (0.997) is a model prediction only.

Other predictions with high scores are similarly unsupported:
- **Neurotrophic keratopathy** (99.67%): driven by corneal nerve damage and impaired healing, which is not an established target of pentamidine.
- **Exposure keratitis** (99.36%): mainly a mechanical and desiccation problem of the cornea, so any benefit would be speculative.
- **Non-human animal disease** (99.13%): a non-specific ontology category, likely a knowledge-graph artifact.
- **Congenital analbuminemia** (99.09%): a rare genetic disorder of albumin synthesis with no pharmacological rationale, likely a graph-based artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06766P | DBL Pentamidine Isethionate for Injection BP 300 mg/vial (Hospira Australia Pty Ltd) | Injection, powder, for solution | Not stated in the available licence record |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: The knowledge graph links pentamidine to a broad set of conditions of concern:
  - Cardiac: torsades de pointes, sudden cardiac arrest, heart conduction disease.
  - Blood pressure: hypertension, hypotensive disorder.
  - Glucose: hyperglycemia, hypoglycemia, diabetes mellitus, diabetic ketoacidosis.
  - Kidney: kidney disease, nephrocalcinosis.
  - Liver and biliary: liver disease, gallbladder disease.
  - Pancreas: pancreatitis.
  - Blood: thrombocytopenia, leukopenia, anemia (including macrocytic).
  - Respiratory: asthma (intrinsic and allergic).
  - Metabolic: hypercalcemia, phosphorus metabolism disease.
  - Urinary tract: pyoureter.
- **Drug Interactions**: 337 interactions were recorded. All 20 listed in the compiled data are rated Moderate. They include:
  - Glucose-lowering drugs: acarbose, alogliptin, albiglutide, canagliflozin, chlorpropamide, dapagliflozin, metformin, pioglitazone.
  - Amphotericin B (including the lipid complex).
  - Clarithromycin.
  - Acid suppressants: famotidine, omeprazole, rabeprazole.
  - Gastrointestinal agents: bisacodyl, loperamide, mesalazine, balsalazide, picosulfuric acid, polyethylene glycol with electrolytes.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score. There are no clinical trials or publications, the mechanism is unknown, and the systemic safety signals (cardiac, glycaemic, renal) are a concern for any new use. The Singapore product is an injectable, and route compatibility with an ocular indication has not been assessed.

**To proceed, the following is needed:**
- The HSA package insert, to obtain warnings, contraindications and the approved indication (a blocking gap for safety screening)
- Mechanism of action data (e.g. from DrugBank) to assess a mechanistic link to ocular surface disease
- A literature and trial search specific to pentamidine in keratoconjunctivitis and related ocular conditions
- An assessment of route and formulation feasibility (for example, whether a topical ocular preparation is even plausible), together with systemic exposure and toxicity considerations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

