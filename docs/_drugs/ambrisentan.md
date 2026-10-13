---
layout: default
title: Ambrisentan
parent: High Evidence (L1-L2)
nav_order: 78
evidence_level: L2
indication_count: 10
---

# Ambrisentan
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Ambrisentan: From Pulmonary Arterial Hypertension to PAH Associated with Connective Tissue Disease

## One-Sentence Summary

Ambrisentan is an endothelin receptor antagonist originally used to treat pulmonary arterial hypertension (PAH).
The TxGNN model predicts it may be effective for **PAH associated with connective tissue disease (CTD-PAH)**,
with **2 clinical trials** and **19 publications** currently supporting this direction.
Note that this is largely an extension within the PAH class, not a completely new disease area.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension |
| Predicted New Indication | PAH associated with connective tissue disease (the top-ranked prediction, pulmonary arteriovenous malformation, has weak evidence and is discussed below) |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

**Note on the predictions:** The highest-scoring prediction is pulmonary arteriovenous malformation (99.41%). It has only one case report, on PAH coexisting with hereditary hemorrhagic telangiectasia, and no trials. It is rated L4 and **Hold**. This report focuses on CTD-PAH, which has the strongest evidence among the predictions.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ambrisentan is a selective endothelin type A (ETA) receptor antagonist. It reduces endothelin-mediated vasoconstriction and pulmonary vascular remodeling, and its efficacy in PAH has been established.

CTD-PAH, including systemic sclerosis-associated PAH, is a Group 1 PAH subtype. It shares the same endothelin-driven vasoconstriction and vascular remodeling as the original indication. Ambrisentan is therefore already used in this population, and subgroup analyses of larger PAH trials (ARIES-E, AMBITION) have looked at CTD-PAH patients specifically. This is largely an extension within the approved PAH class rather than true repurposing.

Other predictions follow a similar pattern. PAH associated with congenital heart disease (L3, Proceed with Guardrails) is supported by ambrisentan-specific cohort studies. PAH associated with HIV (L4) has only small case series and indirect data. PAH associated with chronic hemolytic anemia or schistosomiasis (L5) has no supporting evidence. The non-vascular predictions (malformation syndrome with odontal component, hypotrichosis simplex of the scalp, hypertrichosis, Dandy-Walker syndrome) have no plausible mechanism and no evidence, and are likely model artifacts. Because ambrisentan is teratogenic, use in developmental disorders is inappropriate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02290613](https://clinicaltrials.gov/study/NCT02290613) | Phase 2 | Completed | 38 | EDITA: randomized, double-blind, placebo-controlled proof-of-concept trial of early treatment in borderline PAH associated with systemic sclerosis; small sample limits conclusions |
| [NCT01042158](https://clinicaltrials.gov/study/NCT01042158) | Phase 4 | Completed | 25 | 36-week open-label single-arm study of ambrisentan plus tadalafil in scleroderma-associated PAH; measured 6-minute walk distance, NYHA class, hemodynamics and right ventricular function |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic review / meta-analysis | Intern Emerg Med | Meta-analysis of RCT subgroup data on PAH treatment in connective tissue disease |
| [23906950](https://pubmed.ncbi.nlm.nih.gov/23906950/) | 2013 | Meta-analysis | BMJ Open | Meta-analysis of clinical trials in CTD-PAH, which has few dedicated studies |
| [32161055](https://pubmed.ncbi.nlm.nih.gov/32161055/) | 2020 | Cohort (post hoc) | Ann Rheum Dis | AMBITION post hoc analysis of initial ambrisentan plus tadalafil combination versus monotherapy in CTD-PAH |
| [27492539](https://pubmed.ncbi.nlm.nih.gov/27492539/) | 2016 | Subgroup analysis | Respir Med | ARIES-E subgroup analysis of 3-year ambrisentan efficacy and safety in CTD-PAH |
| [26360334](https://pubmed.ncbi.nlm.nih.gov/26360334/) | 2015 | Cohort | Am J Respir Crit Care Med | Up-front ambrisentan plus tadalafil combination therapy in scleroderma-associated PAH |
| [28425346](https://pubmed.ncbi.nlm.nih.gov/28425346/) | 2017 | Review | Ther Adv Respir Dis | Ambrisentan is approved for idiopathic, heritable and CTD-associated PAH, with acceptable tolerability |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | Recent advances in treating PAH associated with connective tissue diseases |
| [27282418](https://pubmed.ncbi.nlm.nih.gov/27282418/) | 2017 | Observational registry | J Heart Lung Transplant | VOLT post-marketing registry focused on the incidence of aminotransferase elevations with ambrisentan |
| [21371683](https://pubmed.ncbi.nlm.nih.gov/21371683/) | 2011 | Cohort | Am J Cardiol | Ambrisentan in Eisenmenger syndrome (PAH due to congenital heart disease); relevant to the rank 2 prediction |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | Overview of PAH diagnosis and treatment |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15094P | VOLIBRIS FILM-COATED TABLET 10 MG | Film-coated tablet | Not listed in the compiled data |
| SIN15093P | VOLIBRIS FILM-COATED TABLET 5MG | Film-coated tablet | Not listed in the compiled data |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** congestive heart failure, anemia, macrocytic anemia, pulmonary veno-occlusive disease. These should be verified against the package insert.
- **Drug Interactions:** The interaction query returned 100 records. Moderate-level interactions include canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, eliglustat and naltrexone. Minor-level interactions include clarithromycin, miconazole and omeprazole.
- **Other considerations from the evidence review:** hepatotoxicity monitoring, embryo-fetal toxicity (ambrisentan is teratogenic), and fluid retention. For HIV-associated PAH, interactions with antiretrovirals also need evaluation.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
CTD-PAH is a Group 1 PAH subtype with a mechanism matching ambrisentan's approved use. It has one completed Phase 2 trial, one completed Phase 4 trial, and several meta-analyses and subgroup analyses. The trials are small, and the evidence largely reflects use within the existing PAH class rather than a new indication. The top-scoring prediction (pulmonary arteriovenous malformation) and the non-vascular predictions are not supported and should remain on **Hold**.

**To proceed, the following is needed:**
- Singapore package insert warnings, contraindications and approved indication text, which are currently missing and must be obtained from HSA before safety screening
- Detailed mechanism of action data from DrugBank
- A hepatic function monitoring plan and an embryo-fetal toxicity risk management plan
- Larger or controlled evidence specific to CTD-PAH
- For HIV-associated PAH (L4, research question only), HIV-specific efficacy data and an antiretroviral interaction assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

