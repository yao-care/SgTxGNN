---
layout: default
title: Deferasirox
parent: Medium Evidence (L3-L4)
nav_order: 308
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Deferasirox: predicted new indication HIV infectious disease (evidence level L4). Approved use: Beta-thalassemia and related hemoglobinopathies"
monitor_inn: "Deferasirox"
predicted_indications: ["HIV infectious disease", "chronic hepatitis C virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "dermatofibrosarcoma protuberans", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
---

# Deferasirox
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Deferasirox: From Transfusional Iron Overload in Beta-Thalassemia to HIV Infectious Disease

## One-Sentence Summary

Deferasirox is an oral iron chelator, originally associated with beta-thalassemia and related hemoglobinopathies.
The TxGNN model predicts it may be effective for **HIV infectious disease**,
but there are currently **0 clinical trials** and only **2 publications** (one general drug overview and one preclinical study), so this remains a research question rather than an established direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Beta-thalassemia and related hemoglobinopathies (from knowledge-graph indication data; the Singapore license records contain no indication text) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, deferasirox is an iron chelator, its use in iron overload from beta-thalassemia and other hemoglobinopathies is established, and mechanistically it may be applicable to conditions in which iron status influences disease biology.

The proposed link to HIV is indirect. A 2021 preclinical study (PMID 34550543) reports that iron in endolysosomes restricts Tat-mediated HIV-1 LTR transactivation by increasing Tat oligomerization and β-catenin expression. This suggests that iron chelation could modulate HIV-1 transcription. However, the direction of the effect is unresolved: depleting iron may relieve the restriction and increase Tat activity, which would work against the drug.

The other linked paper (PMID 16529348) is a general new-drug overview with no HIV-specific data. The high model score is therefore not backed by clinical evidence.

**Other predictions in the list**

Nine further predictions were generated. All are graded L4 or L5, and none has a clinical trial.

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Chronic hepatitis C virus infection | 99.39% | L4 | Iron accumulation is common in chronic HCV, but the only linked paper is a ferritin measurement method study |
| Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.23% | L5 | No mechanistic link or evidence |
| Obsolete familial combined hyperlipidemia | 99.20% | L5 | Obsolete disease term, likely an ontology artifact |
| Dermatofibrosarcoma protuberans | 99.11% | L5 | No documented link to iron chelation |
| Simian immunodeficiency virus infection | 98.96% | L5 | Likely propagated from the HIV association |
| Feline acquired immunodeficiency syndrome | 98.96% | L5 | Veterinary disease, likely propagated from the HIV association |
| Beta-thalassemia with other manifestations | 98.59% | L5 | Likely a variant of an existing indication, not true repurposing |
| Hereditary pyropoikilocytosis | 98.55% | L5 | Plausible indirect rationale via iron overload from chronic hemolysis |
| Pyruvate kinase deficiency of red cells | 98.50% | L5 | Iron overload is a recognized concern, and a targeted literature search would be a reasonable next step |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Preclinical/In vitro study | Journal of Neurovirology | Endolysosomal iron restricts Tat-mediated HIV-1 LTR transactivation by increasing Tat oligomerization and β-catenin expression |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Review | Journal of the American Pharmacists Association | General overview of new drugs, including deferasirox; no HIV-specific data |

No clinical trials are registered for this indication.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15213P | Jadenu Film Coated Tablet 90 mg | Film-coated tablet | Not stated in the licence record |
| SIN15215P | Jadenu Film Coated Tablet 360 mg | Film-coated tablet | Not stated in the licence record |
| SIN17174P | Desroxia Film-Coated Tablets 90 mg | Film-coated tablet | Not stated in the licence record |
| SIN17173P | Desroxia Film-Coated Tablets 360 mg | Film-coated tablet | Not stated in the licence record |
| SIN17088P | Ferasiro Film Coated Tablet 90 mg | Film-coated tablet | Not stated in the licence record |

A sixth licence, SIN17087P (Ferasiro 360 mg), is also valid. All six licences are single-ingredient oral products.

---

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** liver failure, liver disease, cirrhosis, kidney disease and impaired renal function, thrombocytopenia, neutropenia and agranulocytosis (including several congenital neutropenia syndromes), anemia, hyperbilirubinemia and Gilbert syndrome, gallbladder disease, active peptic ulcer disease, ocular hypertension, multiple organ dysfunction syndrome, and cancer.
- **Drug Interactions:** 100 interactions were identified. Major-level examples include:
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone)
  - Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
  - Aspirin
  - Mesalazine and balsalazide

  Moderate-level examples include rabeprazole, pioglitazone, alosetron, aprepitant, clarithromycin, saxagliptin, aluminum hydroxide, cisapride and dexfenfluramine.

Please refer to the package insert for label warnings and contraindications. The package insert was not available for this review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV prediction rests on one indirect preclinical study whose direction of effect is unclear, and no clinical trials exist. The model score alone does not justify moving forward.

**To proceed, the following is needed:**
- Obtain the Singapore package insert (HSA) to confirm approved indications, warnings and contraindications
- Obtain mechanism of action data from DrugBank
- Clarify in vitro whether iron chelation by deferasirox suppresses or enhances HIV-1 Tat activity
- Assess the safety concerns above (kidney, liver, and blood cell counts) for people living with HIV
- Run a targeted literature search for chelation in pyruvate kinase deficiency, the most mechanistically plausible alternative prediction, and check whether "beta-thalassemia with other manifestations" is only a variant of an existing indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

