---
layout: default
title: Natalizumab
parent: Low Evidence (L5)
nav_order: 701
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-20
description: "Natalizumab: predicted new indication Bronchitis (evidence level L5). Approved use: Crohn's disease, inflammatory bowel disease, Crohn's colitis…"
monitor_inn: "Natalizumab"
predicted_indications: ["bronchitis", "parapsoriasis", "psoriasis", "severe nonproliferative diabetic retinopathy", "acute lichenoid pityriasis"]
---

# Natalizumab
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

## Natalizumab: From Crohn's Disease and Multiple Sclerosis to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Natalizumab is an alpha4-integrin-blocking antibody, originally used for Crohn's disease, inflammatory bowel disease and multiple sclerosis.
The TxGNN model's top-ranked new prediction is **bronchitis**, but **no clinical trials and no publications** currently support it.
Among the other top-10 predictions, psoriasis has the most literature (**16 publications**), and these reports point in conflicting directions, including cases where natalizumab appears to cause or worsen the condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Crohn's disease, inflammatory bowel disease, Crohn's colitis, multiple sclerosis (the Singapore licence record contains no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9946 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for natalizumab: "Natalizumab binds to the α4-subunit of α4β1 and α4β7 integrins expressed on the surface of all leukocytes except neutrophils, and inhibits the α4-mediated adhesion of leukocytes to their counter-receptor(s). The receptors for the α4 family of integrins include vascular cell adhesion molecule-1 (VCAM-1), which is expressed on activated vascular endothelium, and mucosal addressin cell adhesion molecule-1 (MAdCAM-1) present on vascular endothelial cells of the gastrointestinal tract." ([DailyMed: Tysabri (natalizumab) prescribing information, Biogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c5fdde91-1989-4dd2-9129-4f3323ea2962), label version 2026-10-09; accessed 2026-11-19.) Based on known pharmacology, natalizumab blocks alpha4-integrin (VLA-4), which controls how white blood cells move from the bloodstream into tissue. This is how it reduces inflammation in Crohn's disease and multiple sclerosis.

For bronchitis, the mechanistic link is weak. Airway inflammation is involved, but bronchitis is mostly driven by infection or irritants. Systemic immune suppression could raise infection risk rather than help. The prediction is purely computational, with no trial or literature support.

The other top-ranked predictions are also poorly supported:

| Predicted Indication | Score | Evidence | Assessment |
|------|------|------|------|
| Parapsoriasis | 0.9937 | 1 case report (L5) | Reported as an adverse event, so the direction is opposite to a treatment |
| Psoriasis | 0.9919 | 16 publications (L4) | Conflicting: one cohort of 18 MS patients reported improvement, while several case reports describe natalizumab inducing or worsening psoriasis |
| Severe nonproliferative diabetic retinopathy | 0.9918 | None (L5) | No mechanistic or clinical support |
| Acute lichenoid pityriasis | 0.9904 | 1 case report (L5) | Adverse event, not benefit |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for bronchitis, the top-ranked prediction.

For the third-ranked prediction, psoriasis, the most relevant publications are shown below (cohort studies first, then case reports and safety reviews):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33589543](https://pubmed.ncbi.nlm.nih.gov/33589543/) | 2021 | Cohort | Neurol Neuroimmunol Neuroinflamm | Observations in 18 MS patients with comorbid psoriasis treated with natalizumab, reporting improvement of psoriasis |
| [40526577](https://pubmed.ncbi.nlm.nih.gov/40526577/) | 2025 | Review | Dtsch Arztebl Int | Treatment options for MS with comorbid chronic inflammatory diseases, including psoriasis and IBD |
| [30323758](https://pubmed.ncbi.nlm.nih.gov/30323758/) | 2018 | Case report | Case Rep Neurol | Plaque psoriasis developed in a 33-year-old patient during natalizumab treatment; limited evidence that natalizumab can induce or aggravate psoriasis |
| [28905124](https://pubmed.ncbi.nlm.nih.gov/28905124/) | 2018 | Case report | Neurol Sci | Arthritic psoriasis during natalizumab treatment |
| [35646438](https://pubmed.ncbi.nlm.nih.gov/35646438/) | 2022 | Case report | Dermatol Pract Concept | Natalizumab-induced pustular psoriasis of palms and soles |
| [25448040](https://pubmed.ncbi.nlm.nih.gov/25448040/) | 2015 | Review | Pharmacol Ther | Role of leukocyte integrins in leukocyte recruitment and as targets in inflammatory disease |
| [15955735](https://pubmed.ncbi.nlm.nih.gov/15955735/) | 2005 | Review | Curr Opin Pharmacol | Anti-adhesion therapies targeting cell adhesion molecules |
| [19647202](https://pubmed.ncbi.nlm.nih.gov/19647202/) | 2009 | Review | Lancet Oncol | Progressive multifocal leukoencephalopathy (PML) associated with rituximab, natalizumab and efalizumab |
| [20298966](https://pubmed.ncbi.nlm.nih.gov/20298966/) | 2010 | Review | Lancet Neurol | Clinical features and pathogenesis of PML and other JC virus disorders |
| [30324046](https://pubmed.ncbi.nlm.nih.gov/30324046/) | 2018 | Review | Cureus | Mini review of natalizumab-associated PML in MS |

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN14408P | Tysabri Concentrate for Solution for Infusion 300mg/15ml | INFUSION, SOLUTION CONCENTRATE | Valid |

<!-- licenses:end -->

---

## Safety Considerations

- **Contraindication signal (knowledge graph, not label text)**: Progressive multifocal leukoencephalopathy (PML) is listed as a contraindicated condition. The literature also describes natalizumab-associated PML as a rare but often fatal brain infection caused by JC virus reactivation.
- **Drug Interactions**: 100 interactions were found. Major-level interactions include:
  - Corticosteroids: hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone (including ophthalmic)
  - Radiopharmaceuticals and radio-immunotherapies: iobenguane (I-131), ibritumomab tiuxetan, tositumomab (including I-131)
  - Other agents: levamisole, trimetrexate, mercaptopurine
  - Moderate: naltrexone. Minor: zinc salts (sulfate, acetate, gluconate, chloride).
- **Adverse skin reactions reported in the literature**: hypersensitivity and delayed allergic reactions (some with neutralizing antibodies), generalized drug eruption, a sarcoidosis-like reaction, and induced or worsened psoriasis.

Please refer to the package insert for the full warnings and contraindications, as these were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, bronchitis, rests on a computational score alone, with no trials or publications and a mechanism that could even increase infection risk. For the other top-ranked predictions, the available literature mostly describes natalizumab causing the skin conditions rather than treating them. Psoriasis shows only a small, uncontrolled benefit signal that is outweighed by reports of paradoxical induction. Serious safety concerns, especially PML, add to the case for holding.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Controlled studies (ideally randomized trials) in any candidate indication; psoriasis is the only one with a hint of benefit, and it would need a dedicated safety assessment given the induction reports
- A risk-benefit analysis that accounts for PML and for the interactions with corticosteroids and immunosuppressants
- The approved indication text for the Singapore licence SIN14408P

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tysabri (natalizumab) prescribing information, Biogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c5fdde91-1989-4dd2-9129-4f3323ea2962) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

