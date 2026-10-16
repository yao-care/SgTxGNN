---
layout: default
title: Natalizumab
parent: Low Evidence (L5)
nav_order: 701
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Natalizumab: predicted new indication Bronchitis (evidence level L5). Approved use: Crohn's disease, inflammatory bowel disease, Crohn's colitis…"
---

# Natalizumab
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

# Natalizumab: From Crohn's Disease and Multiple Sclerosis to Bronchitis

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
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, natalizumab blocks alpha4-integrin (VLA-4), which controls how white blood cells move from the bloodstream into tissue. This is how it reduces inflammation in Crohn's disease and multiple sclerosis.

For bronchitis, the mechanistic link is weak. Airway inflammation is involved, but bronchitis is mostly driven by infection or irritants. Systemic immune suppression could raise infection risk rather than help. The prediction is purely computational, with no trial or literature support.

The other top-ranked predictions are also poorly supported:

| Predicted Indication | Score | Evidence | Assessment |
|------|------|------|------|
| Parapsoriasis | 99.37% | 1 case report (L4) | Reported as an adverse event, so the direction is opposite to a treatment |
| Psoriasis | 99.19% | 16 publications (L4) | Conflicting: one cohort of 18 MS patients reported improvement, while several case reports describe natalizumab inducing or worsening psoriasis |
| Severe nonproliferative diabetic retinopathy | 99.18% | None (L5) | No mechanistic or clinical support |
| Acute lichenoid pityriasis | 99.04% | 1 case report (L4) | Adverse event, not benefit |
| Pityriasis lichenoides | 98.65% | 1 case report (L4) | Adverse event, not benefit |
| Penile fibromatosis | 98.42% | None (L5) | No mechanistic or clinical support |
| Pustulosis palmaris et plantaris | 98.30% | Reviews plus one induced-onset case report (L4) | Drug-induced onset reported; reviews are indirect |
| Dermatitis | 98.25% | Mostly adverse-reaction reports (L4) | Evidence argues against repurposing |
| Neonatal dermatomyositis | 97.71% | None (L5) | Extremely rare, no support, and neonatal safety concerns |

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

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14408P | Tysabri Concentrate for Solution for Infusion 300mg/15ml | Infusion, solution concentrate | Not stated in the licence record |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

