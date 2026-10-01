---
layout: default
title: Orlistat
parent: Low Evidence (L5)
nav_order: 735
evidence_level: L5
indication_count: 10
---

# Orlistat
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

# Orlistat: From Obesity Management to Hypervitaminosis

## One-Sentence Summary

Orlistat is a gastrointestinal lipase inhibitor marketed as an anti-obesity drug. The Singapore licence records provided contain no approved-indication text, so obesity is inferred from the drug's mechanism and its trial history.
The TxGNN model gives its top-ranked prediction, **hypervitaminosis**, a score of 99.42%, but **0 clinical trials** and **0 publications** support it.
Of the ten predicted indications, only fatty liver disease has meaningful evidence (6 trials, 20 publications), so it is discussed below as the most credible signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence data (inferred: obesity, as a lipase inhibitor) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Orlistat is known to inhibit gastrointestinal lipases, which reduces dietary fat absorption. It also lowers absorption of fat-soluble vitamins (A, D, E, K).

This is the only conceivable link to hypervitaminosis. In routine use, reduced vitamin absorption is a documented adverse effect. In theory, that effect could lower vitamin levels in fat-soluble hypervitaminosis. No trial or publication tests this idea. The high TxGNN score is not backed by any clinical rationale, and the link is weak.

Of the other nine predictions, most are likely knowledge-graph artifacts or indirect associations. Examples are obsolete ontology terms, craniofacial phenotypes, and ABri amyloidosis. Fatty liver disease is the exception. Orlistat-driven weight loss and reduced fat absorption plausibly improve hepatic steatosis in patients with obesity.

---

## Clinical Trial Evidence

**Hypervitaminosis (top-ranked prediction):** Currently no related clinical trials registered.

**Fatty liver disease (best-supported alternative prediction, TxGNN score 85.26%):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00160407](https://clinicaltrials.gov/study/NCT00160407) | Phase 4 | Completed | 50 | Orlistat in overweight NASH patients; tests weight loss and improvement in necroinflammatory and fibrotic changes (most direct trial) |
| [NCT00207311](https://clinicaltrials.gov/study/NCT00207311) | Phase 4 | Completed | 30 | Randomized, placebo-controlled trial of Xenical for steatosis/NASH before hepatitis C treatment |
| [NCT00001723](https://clinicaltrials.gov/study/NCT00001723) | Phase 2 | Completed | 200 | Orlistat safety and efficacy in obese children and adolescents with obesity-related comorbidities; not liver-specific |
| [NCT05934110](https://clinicaltrials.gov/study/NCT05934110) | Phase 2 | Unknown | 320 | 26-week study in overweight or obesity with orlistat comparator arms; indirect link to fatty liver |

---

## Literature Evidence

**Hypervitaminosis (top-ranked prediction):** Currently no related literature available.

**Fatty liver disease (best-supported alternative prediction):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36781126](https://pubmed.ncbi.nlm.nih.gov/36781126/) | 2023 | RCT | Am J Clin Nutr | Diet versus orlistat in obesity with metabolic-associated fatty liver disease |
| [38081992](https://pubmed.ncbi.nlm.nih.gov/38081992/) | 2024 | RCT | Eur J Pediatr | Orlistat in 53 adolescents with overweight/obesity and NAFLD |
| [38910819](https://pubmed.ncbi.nlm.nih.gov/38910819/) | 2024 | Meta-analysis | Proc (Bayl Univ Med Cent) | Systematic review of RCTs on orlistat in obese NAFLD patients |
| [41768122](https://pubmed.ncbi.nlm.nih.gov/41768122/) | 2026 | Meta-analysis | Curr Ther Res | Effect of orlistat on cardiometabolic indices in MASLD, GRADE-assessed |
| [41069538](https://pubmed.ncbi.nlm.nih.gov/41069538/) | 2024 | Clinical study | Acta Endocrinol | Early effect of orlistat on NASH and atherogenicity indices in obese NAFLD |
| [35501557](https://pubmed.ncbi.nlm.nih.gov/35501557/) | 2022 | Review | Curr Obes Rep | Anti-obesity medications for NAFLD, focusing on hepatic histology |
| [18095746](https://pubmed.ncbi.nlm.nih.gov/18095746/) | 2008 | Review | Drug Saf | Orlistat adverse effects and drug interactions |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13046P | XENICAL CAPSULE 120MG | Capsule | Not listed in the record |
| SIN15312P | OBELIT 120 CAPSULE 120MG | Capsule, gelatin coated | Not listed in the record |

Both products are oral capsules.

---

## Safety Considerations

Please refer to the package insert for safety information.

The record shows no drug-interaction entries. The published review (PMID 18095746) notes that orlistat commonly causes mild-to-moderate gastrointestinal adverse effects, such as oily stools, diarrhoea and abdominal pain. It also reduces absorption of fat-soluble vitamins, which is relevant to any use in vitamin-related conditions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, hypervitaminosis, rests on a model score alone. It has no trials, no literature and a weak clinical rationale. Only fatty liver disease has real support (L2 in the record), and even that is limited to small Phase 4 studies, a few RCTs and meta-analyses, with no Phase 3 RCT using hepatic histology endpoints. The other eight predictions are L5 or L4 and should also be held.

**To proceed, the following is needed:**
- Singapore package insert warnings, contraindications and approved-indication text (currently missing)
- Mechanism-of-action data from DrugBank
- For fatty liver disease, as the more promising direction: a Phase 3 RCT with liver histology endpoints, plus a plan to monitor fat-soluble vitamins and GI adverse effects
- For hypervitaminosis: a literature and mechanism review to decide whether the prediction merits any study

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

