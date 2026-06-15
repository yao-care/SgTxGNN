---
layout: default
title: Carbidopa
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Carbidopa
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

# Carbidopa: From Parkinson's Disease to Lewy Body Dementia

## One-Sentence Summary

Carbidopa is a peripheral DOPA decarboxylase inhibitor used exclusively as an adjunct to levodopa in Parkinson's disease, preventing peripheral levodopa breakdown to improve CNS dopamine delivery. The TxGNN model generated 10 predicted new indications; while the top-ranked prediction is Rasmussen subacute encephalitis (score: 98.43%), it carries no supporting evidence (L5). The best-evidenced repurposing target is **Lewy body dementia** (rank #6, score: 95.99%), backed by **1 clinical trial** and **18 publications** (L3), making it the most actionable candidate for further evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (peripheral levodopa adjunct) |
| Featured Prediction | Lewy Body Dementia *(highest-evidence among 10 predictions)* |
| TxGNN Prediction Score | 95.99% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## All Predicted Indications — Overview

| Rank | Disease | TxGNN Score | Evidence Level | Clinical Trials | Literature | Decision |
|------|---------|-------------|---------------|----------------|-----------|---------|
| 1 | Rasmussen subacute encephalitis | 98.43% | L5 | 0 | 0 | Hold |
| 2 | PLA2G6-associated neurodegeneration | 97.60% | L4 | 0 | 3 | Research Question |
| 3 | Transaldolase deficiency | 97.40% | L5 | 0 | 0 | Hold |
| 4 | Myelitis | 97.40% | L4 | 0 | 2 | Hold |
| 5 | Fructose-1,6-bisphosphatase deficiency | 97.09% | L5 | 0 | 0 | Hold |
| **6** | **Lewy body dementia** | **95.99%** | **L3** | **1** | **18** | **Research Question** |
| 7 | Paralysis agitans, juvenile, of Hunt | 95.60% | L5 | 0 | 0 | Hold |
| 8 | Progressive supranuclear palsy-corticobasal syndrome | 95.36% | L4 | 1 | 0 | Hold |
| 9 | X-linked intellectual disability-ataxia-apraxia syndrome | 94.87% | L4 | 0 | 3 | Research Question |
| 10 | X-linked intellectual disability-cerebellar hypoplasia syndrome | 93.72% | L4 | 0 | 1 | Hold |

---

## Why is This Prediction Reasonable?

Carbidopa is an irreversible inhibitor of aromatic L-amino acid decarboxylase (AADC, also known as DOPA decarboxylase) in peripheral tissues. By blocking the conversion of levodopa to dopamine before it reaches the brain, carbidopa dramatically increases the fraction of levodopa that crosses the blood-brain barrier and becomes available for central dopamine synthesis. Carbidopa itself does not cross the blood-brain barrier, so it has no direct central dopaminergic action — its entire utility lies in optimising levodopa delivery. Note: detailed mechanism of action data was unavailable in the DrugBank query for this report cycle; the above reflects established pharmacological knowledge.

Lewy body dementia shares its core neuropathology with Parkinson's disease. In both conditions, abnormal α-synuclein aggregates — Lewy bodies — accumulate in the substantia nigra and other brain regions, causing progressive degeneration of nigrostriatal dopaminergic neurons. This shared dopamine deficiency is why DLB patients develop prominent parkinsonism (bradykinesia, rigidity, postural instability), and why levodopa/carbidopa is clinically used in DLB to manage these motor symptoms. The TxGNN prediction reflects this mechanistic overlap accurately.

However, DLB presents a critical therapeutic challenge that distinguishes it from idiopathic Parkinson's disease: patients are substantially more sensitive to dopaminergic medications, with a markedly elevated risk of drug-induced hallucinations and neuropsychiatric deterioration. The levodopa response in DLB is often attenuated and shorter-lasting, and the therapeutic window is narrow. Any repurposing pathway must incorporate a rigorous neuropsychiatric safety monitoring protocol alongside careful dose titration.

---

## Clinical Trial Evidence (Lewy Body Dementia)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Phase 1 | Recruiting | 40 | [18F]F-DOPA PET imaging study in alpha-synucleinopathies including PD, MSA, and DLB, investigating the pattern of dopaminergic system dysfunction. This is a diagnostic/mechanistic imaging study, not a treatment efficacy trial. It provides indirect mechanistic support for dopamine pathway involvement across Lewy body pathologies, but does not generate direct carbidopa therapeutic outcome data. |

---

## Literature Evidence (Lewy Body Dementia)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36402160](https://pubmed.ncbi.nlm.nih.gov/36402160/) | 2022 | Phase 3 RCT | The Lancet Neurology | Foslevodopa-foscarbidopa 24-h subcutaneous infusion vs oral levodopa in advanced Parkinson's disease; demonstrates superior motor control with continuous carbidopa delivery. High-quality pharmacological evidence; population is PD, not DLB. |
| [14594099](https://pubmed.ncbi.nlm.nih.gov/14594099/) | 2003 | Review | Canadian Family Physician | Clinical guide to DLB diagnosis and pharmacological management. Explicitly addresses levodopa/carbidopa use for DLB parkinsonism and highlights medications to avoid (conventional antipsychotics). |
| [11581527](https://pubmed.ncbi.nlm.nih.gov/11581527/) | 2001 | Review | Current Treatment Options in Neurology | Comprehensive DLB treatment review. States levodopa/carbidopa as the preferred therapy for motor symptoms; covers cognitive, psychiatric, and motor management approach across the disease spectrum. |
| [37016564](https://pubmed.ncbi.nlm.nih.gov/37016564/) | 2023 | Review | American Journal of Case Reports | Evaluation of dopamine deficiency in non-Alzheimer dementias including DLB. Discusses dopamine transporter (DAT) imaging as a core diagnostic biomarker and the role of dopaminergic therapy in both diagnosis and treatment. |
| [11790237](https://pubmed.ncbi.nlm.nih.gov/11790237/) | 2002 | Cohort | Archives of Neurology | Neuropathological substrates of dementia and loss of levodopa response in Parkinson's disease. Defines the Lewy body burden threshold beyond which levodopa efficacy diminishes — directly relevant to understanding DLB pharmacodynamics. |
| [41031701](https://pubmed.ncbi.nlm.nih.gov/41031701/) | 2025 | Clinical Trial | Pharmacotherapy | Pharmacodynamic study of oral levodopa/carbidopa on blood pressure in Parkinson's disease; characterises hypotensive effects across levodopa concentration ranges — clinically relevant to DLB patients with autonomic instability. |
| [9748031](https://pubmed.ncbi.nlm.nih.gov/9748031/) | 1998 | Observational | Neurology | Early dopaminergic drug-induced hallucinations in PD; characterises patient profiles at highest risk. This safety data is critical context for DLB patients, who face substantially higher hallucination risk. |
| [15040654](https://pubmed.ncbi.nlm.nih.gov/15040654/) | 2004 | Case Report | Pharmacotherapy | Dose-dependent reversal of apraxia of lid opening with carbidopa-levodopa in a patient diagnosed with both PD and Lewy body dementia. Demonstrates a clinically meaningful pharmacodynamic response specifically in a DLB patient. |
| [40585751](https://pubmed.ncbi.nlm.nih.gov/40585751/) | 2025 | Case Report | Cureus | Sublingual levodopa/carbidopa in a DLB patient unable to swallow oral formulations. Demonstrates a practical route-of-administration innovation for a common clinical barrier in advanced DLB. |
| [11808350](https://pubmed.ncbi.nlm.nih.gov/11808350/) | 2001 | Case Report | Rinsho Shinkeigaku | DLB patient who developed hallucinations and agitation within 2 days of starting levodopa/carbidopa, requiring discontinuation; subsequently improved on donepezil. Illustrates the neuropsychiatric risk of dopaminergic therapy in DLB. |

---

## Singapore Market Information

Carbidopa is **not registered** in Singapore (HSA). There are zero active marketing authorisations for standalone carbidopa. Globally, carbidopa is almost universally co-formulated with levodopa (e.g., Sinemet®, Stalevo®); standalone carbidopa registration is rare. Any repurposing pathway in Singapore would require confirming whether levodopa/carbidopa combination products are registered and evaluating the indication expansion strategy accordingly.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinical note from available literature**: Levodopa/carbidopa in DLB carries a substantially elevated risk of drug-induced psychosis, hallucinations, and neuropsychiatric deterioration compared to idiopathic Parkinson's disease. Low starting doses, slow titration, and close neuropsychiatric monitoring are essential. Concomitant cholinesterase inhibitors may partially mitigate cognitive and psychiatric side effects.

---

## Conclusion and Next Steps

**Decision: Research Question** *(for Lewy body dementia; Hold for all other predicted indications)*

**Rationale:**
Lewy body dementia shares the core nigrostriatal dopaminergic pathophysiology of Parkinson's disease, and levodopa/carbidopa is already applied in clinical practice for DLB motor symptoms, supported by multiple published reviews, cohort studies, and case reports (L3 evidence). However, no dedicated randomised controlled trial has evaluated levodopa/carbidopa efficacy and safety specifically in DLB, and the benefit-risk profile is meaningfully more complex than in Parkinson's disease due to heightened neuropsychiatric sensitivity.

**To proceed, the following is needed:**

- **Regulatory clarity**: Determine whether carbidopa-levodopa combination products (Sinemet® or equivalents) are registered in Singapore, as standalone carbidopa is unlikely to be the regulatory target
- **Safety data retrieval**: Obtain and review the full package insert warnings, contraindications, and special population precautions (DG001 — currently Blocking)
- **DrugBank MOA data**: Retrieve complete pharmacological profile including drug interactions via DrugBank API (DG002)
- **Dedicated DLB RCT**: A Phase 2 randomised trial evaluating levodopa/carbidopa efficacy specifically in DLB (separating from PD populations) is the key evidence gap
- **Neuropsychiatric safety protocol**: Design a structured monitoring framework for hallucinations, cognitive fluctuations, and autonomic adverse events before any prospective use
- **PLA2G6-NBIA and MCT8 deficiency follow-up**: Indications ranked #2 and #9 show mechanistically coherent, carbidopa-relevant pathophysiology with emerging case series evidence — these merit dedicated literature reviews and may reach L3 with targeted searches
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

