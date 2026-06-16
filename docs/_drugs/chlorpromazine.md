---
layout: default
title: Chlorpromazine
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Chlorpromazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Chlorpromazine: From Adult Schizophrenia to Early-Onset Schizophrenia

## One-Sentence Summary

Chlorpromazine is the first-generation antipsychotic of the phenothiazine class, established as a cornerstone treatment for schizophrenia and related psychotic disorders in adults since the 1950s.
The TxGNN model generated 10 predictions, of which **early-onset schizophrenia** (onset before age 18) is the only actionable repurposing candidate, supported by **1 clinical trial** and **8 publications** at **Evidence Level L3**.
Nine of the ten predictions are assessed as "Hold" due to model artifacts or adverse-effect pathway misidentification; the top-ranked prediction carries a critical safety alert described below.

---

## ⚠️ Critical Model Alert: Reverse Warning on Rank 1 Prediction

The highest-scoring TxGNN prediction — **retinal dystrophy with or without extraocular anomalies (99.95%)** — triggers a **reverse warning**. Chlorpromazine is a well-documented **cause** of pigmentary retinal toxicity (chlorpromazine retinopathy), not a treatment for hereditary retinal disease. The model almost certainly traversed the chlorpromazine → retina adverse-effect path in the knowledge graph and misclassified it as a therapeutic signal. **This prediction must not be pursued clinically.** Ranks 2–4 (X-linked myopia, syndromic myopia, glycosylation defect) are similarly assessed as model artifacts with no mechanistic basis. This report focuses on **Rank 10 (early-onset schizophrenia)** as the sole viable candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Adult schizophrenia and psychotic disorders (Singapore regulatory data unavailable — 0 registered products) |
| Predicted New Indication | Early-Onset Schizophrenia (onset < 18 years) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## All-Prediction Summary

| Rank | Indication | TxGNN Score | Evidence | Decision | Key Note |
|------|-----------|-------------|----------|----------|----------|
| 1 | Retinal dystrophy with/without extraocular anomalies | 99.95% | L5 | ⛔ Hold | **Reverse warning: chlorpromazine CAUSES retinal toxicity — not a treatment** |
| 2 | Congenital disorder of glycosylation (fucosylation defect) | 99.94% | L5 | Hold | No mechanistic link; probable KG artifact via CNS → neurodelopment → glycosylation |
| 3 | Myopia X-linked | 99.94% | L5 | Hold | No therapeutic mechanism; known ocular toxicity is a contraindication concern |
| 4 | Syndromic myopia | 99.94% | L5 | Hold | Genetic/collagen etiology; no drug target; model over-predicts ophthalmic cluster |
| 5 | Hydranencephaly | 99.93% | L5 | Hold | Irreversible structural brain anomaly; sedation is symptom management only |
| 6 | Polymicrogyria with cerebellar hypoplasia & arthrogryposis | 99.93% | L5 | Hold | Irreversible cortical malformation; distant indirect KG linkage only |
| 7 | Myopia 26, X-linked, female-limited | 99.93% | L5 | Hold | Same as Rank 3; ARR3 gene defect, no known drug target |
| 8 | Charcot-Marie-Tooth disease type 1G | 99.93% | L5 | Hold | No remyelination mechanism; chlorpromazine may worsen peripheral neuropathy |
| 9 | Atypical glycine encephalopathy | 99.92% | L5 | Hold | Hypothetical NMDA co-agonist connection; no clinical or preclinical data |
| **10** | **Early-Onset Schizophrenia** | **99.47%** | **L3** | **✅ Proceed with Guardrails** | **Only actionable candidate; direct mechanistic applicability** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved from the DrugBank API in this Evidence Pack. However, chlorpromazine is one of the most pharmacologically well-characterised drugs in psychiatry. It is a **D2 dopamine receptor antagonist** of the phenothiazine class: by blocking dopamine D2 receptors in the mesolimbic pathway, it dampens the dopaminergic hyperactivity that underlies positive psychotic symptoms (hallucinations, delusions, disorganised thinking). Concurrent antagonism of muscarinic, H1, and α1-adrenergic receptors accounts for its well-known side-effect burden (sedation, anticholinergic effects, orthostatic hypotension).

Early-onset schizophrenia (EOS, onset before age 18) is not a categorically different disease — it shares the same core dopaminergic dysregulation pathophysiology as adult-onset schizophrenia. The mechanistic bridge is therefore direct: chlorpromazine's D2 blockade is as relevant in the adolescent mesolimbic system as in the adult. Antipsychotics including first-generation agents such as chlorpromazine are the established first-line pharmacological treatment for EOS in current clinical guidelines. The TxGNN prediction for this indication reflects genuine pharmacological continuity between adult and paediatric schizophrenia rather than a speculative leap.

A clinically important nuance emerges from the pharmacogenomic literature in this Evidence Pack. BDNF gene polymorphisms modulate the risk of chlorpromazine-induced extrapyramidal syndrome (EPS) in Chinese patients (PMID 18408624), and AKT1 gene variants affect overall antipsychotic therapeutic response (PMID 17915974). Since children and adolescents are known to be substantially more sensitive to EPS than adults, this pharmacogenomic layer is particularly actionable for the EOS population — it points toward genotype-guided dosing and monitoring protocols as a meaningful refinement beyond simply extrapolating adult practice.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT06128408](https://clinicaltrials.gov/study/NCT06128408) | N/A | Unknown | 300 | Observational characterisation of treatment-resistant schizophrenia from illness onset (TRO). Prior studies show up to 30% of first-episode patients do not respond to standard antipsychotics, with TRO accounting for 80% of long-term TRS cases. Provides background on EOS treatment response patterns; does not directly test chlorpromazine efficacy but is relevant to identifying patients who may need dose adjustment or treatment switch. |

*No interventional clinical trials directly testing chlorpromazine in early-onset schizophrenia are currently registered.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18408624](https://pubmed.ncbi.nlm.nih.gov/18408624/) | 2008 | Genetic Association | Pharmacogenetics and Genomics | BDNF gene is both a schizophrenia risk factor and a modulator of chlorpromazine-induced EPS in Chinese patients — directly relevant to personalised dosing in EOS where EPS risk is heightened |
| [17915974](https://pubmed.ncbi.nlm.nih.gov/17915974/) | 2007 | Pharmacogenomics | Journal of Clinical Psychiatry | AKT1 gene polymorphisms associated with schizophrenia susceptibility and antipsychotic therapeutic response; supports genetic stratification of EOS patients prior to initiating chlorpromazine |
| [10703271](https://pubmed.ncbi.nlm.nih.gov/10703271/) | 1999 | Retrospective | Social Psychiatry & Psychiatric Epidemiology | Earlier age of schizophrenia onset is associated with different neuroleptic dosage requirements in outpatients — supports the need for age-specific dosing protocols for EOS |
| [28976410](https://pubmed.ncbi.nlm.nih.gov/28976410/) | 2017 | Observational | Clinical Neuropharmacology | OCD comorbidity is notably prevalent in early-onset schizophrenia; implications for antipsychotic selection and monitoring (some antipsychotics may exacerbate OCD) |
| [22802957](https://pubmed.ncbi.nlm.nih.gov/22802957/) | 2012 | MRI/Neuroimaging | PLoS ONE | Gray matter reduction in temporal gyrus documented in first-episode EOS; confirms shared neurodevelopmental substrate with adult schizophrenia, supporting pharmacological applicability of D2 antagonists |
| [24289465](https://pubmed.ncbi.nlm.nih.gov/24289465/) | 2013 | Retrospective Comparative | Psychogeriatrics | Clinical comparison of late-onset vs early-onset schizophrenia in Japanese population; highlights age-related phenotypic differences relevant to treatment selection |
| [26916502](https://pubmed.ncbi.nlm.nih.gov/26916502/) | 2016 | Observational | Acta Neuropsychiatrica | Theory of mind deficits in adolescents with EOS correlate with executive function impairment; relevant to functional outcome monitoring during antipsychotic treatment |
| [24854724](https://pubmed.ncbi.nlm.nih.gov/24854724/) | 2015 | Observational | L'Encéphale | Neurological soft signs in EOS support the neurodevelopmental model; relevant baseline reference for monitoring antipsychotic-related neurological adverse effects in this population |

---

## Singapore Market Information

Chlorpromazine has **no registered products in Singapore** (0 authorisations on record). Clinical use would require either an off-label pathway, a compassionate use application to HSA, or importation under special access.

For reference, chlorpromazine holds regulatory approval in the following comparable jurisdictions:

| Jurisdiction | Product Name | Dosage Form | Approved Indication (summary) |
|-------------|-------------|-------------|-------------------------------|
| USA (FDA) | Thorazine | Tablet, injection, syrup | Schizophrenia, bipolar mania, nausea/vomiting, intractable hiccups, pre-op sedation |
| UK (MHRA) | Largactil | Tablet, injection, syrup | Schizophrenia, other psychoses, mania, agitation, nausea... |
| Australia (TGA) | Chlorpromazine (generic) | Tablet, injection | Psychotic disorders, nausea, intractable hiccups |
| Japan (PMDA) | Contomin / Wintermin | Tablet, injection | Schizophrenia, mania, nausea, pre-op sedation |

---

## Safety Considerations

Formal safety data (warnings, contraindications, DDI profile) was not retrieved in this Evidence Pack. Please refer to the package insert for complete safety information.

**Safety concerns particularly relevant to the early-onset schizophrenia context** (drawn from evidence pack rationale and published literature):

- **Extrapyramidal Symptoms (EPS)**: Children and adolescents are significantly more susceptible to EPS (acute dystonia, parkinsonism, akathisia, tardive dyskinesia) than adults. BDNF gene polymorphisms (PMID 18408624) independently modulate EPS risk — genotyping before initiation is worth considering.
- **Chlorpromazine Retinopathy**: Long-term, high-dose use causes pigmentary deposits in the retina. Given that this adverse pathway was mistaken by TxGNN for a therapeutic signal (Rank 1 reverse warning), ophthalmological baseline assessment and periodic monitoring are mandatory.
- **Neurodevelopmental exposure**: Chronic antipsychotic use during active brain development warrants a documented benefit-risk assessment, with minimum effective dosing and regular re-evaluation of continued need.
- **QTc Prolongation**: A class effect of phenothiazines; ECG monitoring recommended, especially during dose titration.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Chlorpromazine's D2 receptor antagonism is directly applicable to early-onset schizophrenia, which shares identical dopaminergic pathophysiology with adult schizophrenia. The pharmacological case is strong, and antipsychotics are already the clinical standard of care for EOS. The L3 observational evidence base is modest, but the drug mechanism is not speculative — this is an established drug being extended to a younger patient population with specific safety monitoring requirements.

**To proceed, the following is needed:**

- **Regulatory pathway**: Identify Singapore HSA route (off-label, compassionate use, or parallel import) before clinical deployment
- **Safety dossier (DG001)**: Retrieve TFDA package insert warnings, contraindications, and DDI profile to complete the safety assessment
- **MOA data (DG002)**: Pull full DrugBank record for DB00477 to formally document receptor binding profile and pharmacokinetics
- **Paediatric dosing protocol**: Establish weight-based dosing guidance and titration schedule specific to patients under 18
- **EPS monitoring plan**: Define baseline and periodic assessments (AIMS, BARS, SAS scales); consider BDNF/AKT1 genotyping for EPS risk stratification
- **Ophthalmological monitoring**: Mandatory baseline and annual retinal examinations given known chlorpromazine retinopathy risk
- **Metabolic and cardiac monitoring**: BMI, fasting glucose, lipids, and QTc parameters appropriate for the paediatric age range
- **Reverse warning documentation**: Formally record the Rank 1 retinal dystrophy prediction as a model artifact and adverse-effect misidentification to prevent clinical misuse of the TxGNN output
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

