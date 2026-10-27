---
layout: default
title: Insulin Lispro
parent: Low Evidence (L5)
nav_order: 539
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Insulin Lispro: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Type 1 and type 2 diabetes mellitus, diabetic ketoacidosis"
monitor_inn: "Insulin lispro"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Insulin Lispro
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

## Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis
{: .text-alpha }

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analogue, originally used to control blood glucose in type 1 and type 2 diabetes mellitus and to treat diabetic ketoacidosis.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but **no clinical trials and no publications** currently support this prediction.
The prediction is best regarded as a model-derived hypothesis rather than a therapeutic lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 1 and type 2 diabetes mellitus, diabetic ketoacidosis (from the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on general knowledge, insulin lispro is a rapid-acting insulin analogue that binds the insulin receptor to regulate glucose metabolism. Its efficacy in diabetes is well established.

Autoimmune oophoritis is an immune-mediated ovarian disorder. It often occurs within autoimmune polyendocrine syndromes, which can include type 1 diabetes. No direct mechanistic link between insulin lispro and this condition has been established. The high score most likely reflects proximity in the knowledge graph through shared autoimmune endocrine comorbidity, not a therapeutic effect.

**Other predictions (ranks 2–10)** were also reviewed. None has clinical trial support:

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Thiamine-responsive dysfunction syndrome | 99.37% | Insulin would treat only the accompanying diabetes, not the underlying defect |
| 3 | Focal stiff limb syndrome | 99.36% | Link through shared anti-GAD65 autoimmunity; no action on the neuromuscular pathology |
| 4 | Classic stiff person syndrome | 99.36% | Same as above; insulin would treat only comorbid diabetes |
| 5 | Opsismodysplasia | 99.34% | Biologically plausible link via INPPL1/SHIP2 in insulin signalling; direction of effect unproven |
| 6 | Drug-induced localized lipodystrophy | 99.09% | Insulin is a known cause, not a treatment; use would be inappropriate |
| 7 | Pancreatic agenesis | 99.09% | Insulin replacement is physiologically rational; the only linked paper is an indirect review (L4) |
| 8 | Centrifugal lipodystrophy | 99.04% | No established mechanism |
| 9 | Pressure-induced localized lipoatrophy | 99.03% | Likely a knowledge-graph artefact; injection-site lipoatrophy is a known insulin adverse effect |
| 10 | Idiopathic localized lipodystrophy | 98.97% | Association more likely adverse than therapeutic |

Pancreatic agenesis is the most biologically coherent of these, because insulin replacement for an insulin-deficient state is consistent with the drug's existing use. It would be an extension of the current indication rather than true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the top-ranked prediction (autoimmune oophoritis). One publication is linked to the rank 7 prediction (pancreatic agenesis):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | J Am Pharm Assoc | General review of insulin therapy in type 2 diabetes and practical aspects of starting it; indirect evidence only |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13719P | HUMALOG KWIKPEN 100 units/ml | Injection | Not stated in the data compiled |
| SIN11227P | HUMALOG MIX 25 Suspension for Injection 100 iu/ml | Injection | Not stated in the data compiled |
| SIN11171P | HUMALOG MIX25 KWIKPEN 100 units/ml | Injection | Not stated in the data compiled |

All three registrations are valid single-ingredient products, available as injectables only.

## Safety Considerations

**Drug Interactions**: The interaction screening returned 100 records. Most of the 20 listed were Moderate, with a few Minor. The main ones are:
- **Glucose-lowering agents (additive hypoglycaemia risk or altered glycaemic control)**: metformin, alogliptin, albiglutide, alpelisib
- **Sympathomimetics and beta-agonists (may reduce glucose-lowering effect)**: epinephrine, phenylephrine, pseudoephedrine, salbutamol, formoterol
- **Beta-blocker**: acebutolol (may mask hypoglycaemia symptoms)
- **Hormonal agents and corticosteroids**: estradiol, ethinylestradiol, levonorgestrel, hydrocortisone (Minor for topical forms)
- **Others**: acetazolamide, hydrochlorothiazide, doxycycline, ethanol

Injection-site lipodystrophy and lipoatrophy are known adverse effects of insulin therapy. This matters directly for the predicted lipodystrophy indications (ranks 6, 8, 9 and 10).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, autoimmune oophoritis, has no clinical trials or literature, no mechanistic link, and a score that likely reflects comorbidity proximity in the knowledge graph. Evidence is L5 (model prediction only).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, and approved indication text for the three Singapore licences
- Mechanism of action data from DrugBank
- A targeted literature search on insulin and autoimmune ovarian disease
- Consideration of pancreatic agenesis (L4) as a separate research question, given the physiological rationale for insulin replacement
- Exclusion of the lipodystrophy-related predictions, since insulin can cause these conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

