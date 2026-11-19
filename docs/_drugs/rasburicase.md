---
layout: default
title: Rasburicase
parent: Low Evidence (L5)
nav_order: 856
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Rasburicase: predicted new indication Hypouricemia, renal (evidence level L5). Approved use: Hyperuricemia"
monitor_inn: "Rasburicase"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "primitive portal vein thrombosis", "hepatoportal sclerosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "renal tubular acidosis", "disorder of phenylalanine metabolism"]
---

# Rasburicase
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

## Rasburicase: hypouricemia, renal
{: .text-alpha }

## One-Sentence Summary

Rasburicase is a recombinant urate oxidase originally used to lower uric acid in hyperuricemia.
The TxGNN model predicts it may be effective for **renal hypouricemia**, but **no clinical trials and no publications** support this prediction.
The mechanism also points the wrong way: the condition already involves low uric acid, so this prediction is most likely a model artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricemia (approved indication text is not listed in the Singapore registration) |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for rasburicase: "In humans, uric acid is the final step in the catabolic pathway of purines. Rasburicase catalyzes enzymatic oxidation of poorly soluble uric acid into an inactive and more soluble metabolite (allantoin)." ([DailyMed: Elitek (rasburicase) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0ae10bc4-6b65-402f-9db5-2d7753054922), label version 2026-07-30; accessed 2026-11-19.) Based on known information, rasburicase is a recombinant urate oxidase. It converts uric acid to allantoin and lowers serum urate, which is why it is used for hyperuricemia.

Renal hypouricemia is a condition in which serum urate is already low, for example from loss-of-function variants in URAT1 (SLC22A12) or GLUT9 (SLC2A9). Lowering urate further would be mechanistically counterproductive and could raise risk, for example exercise-induced acute kidney injury. The high score (0.9999) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top-ranked predictions are also weak. Several hepatic and portal conditions share an identical score (0.9997), which may reflect similarities the model learned between related diseases, not biological evidence. The one biologically plausible candidate is partial HPRT deficiency, where purine overproduction causes hyperuricemia. Even there, rasburicase is an injectable biologic with a short course and immunogenicity that limits repeat use, so it is unsuitable for chronic management. Allopurinol and febuxostat are already standard care.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN12055P | FASTURTEC POWDER FOR SOLUTION FOR INFUSION 1.5 mg/vial | INJECTION, POWDER, FOR SOLUTION | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 13 interactions were identified. Two are rated Major:
  - Prilocaine (Major)
  - Nitrous acid (Major)
- The other 11 are rated Moderate. They mainly involve local anaesthetics (tetracaine, lidocaine, benzocaine, cocaine, proparacaine, oxybuprocaine, cinchocaine) in topical, ophthalmic or nasal forms, plus idelalisib.
- **Screening point**: G6PD deficiency, hemolysis and methemoglobinemia are safety concerns that would need screening before any use.

Please refer to the package insert for further safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). Renal hypouricemia is already a low-urate state, so further urate lowering is mechanistically counterproductive and potentially harmful. No trials or publications support it.

**To proceed, the following is needed:**
- A mechanistic justification that explains why lowering urate would benefit renal hypouricemia (none is currently apparent)
- Mechanism of action data for rasburicase from DrugBank
- Package insert warnings and contraindications from the HSA
- If a more plausible indication (such as acute severe hyperuricemia in partial HPRT deficiency) is pursued, a comparison against standard therapy and a G6PD screening plan

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Elitek (rasburicase) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0ae10bc4-6b65-402f-9db5-2d7753054922) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

