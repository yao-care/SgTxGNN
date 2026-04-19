# Amantadine: From Parkinson's Disease to Lewy Body Dementia

## One-Sentence Summary

Amantadine is a long-established neurological agent approved for Parkinson's disease and influenza A, acting through non-competitive NMDA receptor antagonism and dopaminergic modulation.
The TxGNN model predicts 10 new indications across the neurological spectrum; **Lewy Body Dementia (LBD)** emerges as the most clinically actionable candidate, supported by **4 clinical trials** and **20 publications** establishing NMDA antagonism as a viable therapeutic approach in the Lewy body disease spectrum.
While direct Amantadine trials in LBD are absent, extensive evidence from memantine — a structurally related NMDA antagonist — provides strong mechanistic class-effect support for this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease; influenza A prophylaxis and treatment |
| Best-Evidenced Predicted Indication | Lewy Body Dementia (LBD) |
| TxGNN Prediction Score (LBD) | 97.83% (Global rank: 17,849) |
| Evidence Level | L3 — Systematic reviews and RCTs via NMDA antagonist class-effect |
| Singapore Market Status | ✗ Not Marketed (0 registered products) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## All Predicted Indications — Overview

This Evidence Pack covers 10 TxGNN predictions (candidate ID: TW-DB00915-multi). Summary of all candidates:

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation |
|------|-----------|------------|----------------|----------------|
| 1 | Rasmussen subacute encephalitis | 99.48% | L5 | Hold |
| 2 | Transaldolase deficiency | 99.27% | L5 | Hold |
| 3 | Myelitis | 99.24% | L3 | Research Question |
| 4 | PLA2G6-associated neurodegeneration (PLAN) | 99.23% | L4 | Hold |
| 5 | Fructose-1,6-bisphosphatase deficiency | 98.97% | L5 | Hold |
| 6 | Paralysis agitans, juvenile, of Hunt | 97.86% | L4 | Hold |
| **7** | **Lewy body dementia** | **97.83%** | **L3** | **Proceed with Guardrails** |
| 8 | X-linked intellectual disability-ataxia-apraxia syndrome | 97.80% | L5 | Hold |
| 9 | Progressive supranuclear palsy-corticobasal syndrome (PSP-CBS) | 97.77% | L3 | Research Question |
| 10 | X-linked intellectual disability-cerebellar hypoplasia syndrome | 96.95% | L5 | Hold |

> **Key finding**: Despite Rasmussen subacute encephalitis scoring highest on TxGNN (99.48%), it carries zero supporting evidence. Lewy body dementia (rank 7, 97.83%) is the only candidate reaching an actionable evidence threshold. Myelitis (rank 3) and PSP-CBS (rank 9) represent secondary research questions. Five candidates are pure model predictions with no literature support and should be held pending preclinical validation.

---

## Why is This Prediction Reasonable?

**Shared NMDA receptor target**: Amantadine is a non-competitive NMDA receptor antagonist and dopaminergic modulator. In LBD, accumulation of α-synuclein protein aggregates disrupts glutamate homeostasis, leading to chronic NMDA receptor over-activation and excitotoxic neuronal damage. Blocking this pathway is mechanistically directly relevant to the core pathology of LBD. (Note: detailed package insert MOA documentation was unavailable for this review; the above is based on published pharmacological literature.)

**Class-effect from memantine**: Memantine is a structurally related NMDA antagonist that has been tested in multiple completed Phase 2, 3, and 4 RCTs specifically targeting LBD and Parkinson's Disease Dementia (PDD — the same Lewy body disease spectrum). Several systematic reviews and meta-analyses (PMID 26085043, PMID 24406251, PMID 24828899) confirm that NMDA receptor antagonism is both efficacious and well-tolerated in this patient population. Because Amantadine shares the same primary pharmacological target with comparable affinity, a class-effect extrapolation from memantine evidence to Amantadine is scientifically grounded and has established precedent in regulatory pharmacology.

**Proximity to the approved indication**: Amantadine already carries an approved indication for Parkinson's disease — a condition that shares α-synuclein (Lewy body) pathology with LBD. Moving from PD motor symptom management to LBD cognitive and neuropsychiatric symptom management is an incremental extension within the same pathological spectrum, not a cross-disease leap. However, one critical distinction must be respected: LBD patients are markedly more sensitive to dopaminergic drugs than PD patients, with an established risk of worsening hallucinations and psychosis. This requires mandatory safety guardrails in any clinical programme.

---

## Clinical Trial Evidence

*(Lewy Body Dementia — primary candidate)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855686](https://clinicaltrials.gov/study/NCT00855686) | Phase 4 | Completed | 199 | Randomised, double-blind, placebo-controlled 6-month study of memantine in DLB and PDD; the largest completed NMDA antagonist RCT in the Lewy body dementia spectrum |
| [NCT00630500](https://clinicaltrials.gov/study/NCT00630500) | Phase 2 | Completed | 75 | 24-week placebo-controlled parallel-group trial of memantine in PDD and DLB; evaluated safety and efficacy of NMDA blockade with positive results |
| [NCT03858270](https://clinicaltrials.gov/study/NCT03858270) | Phase 3 | Unknown | 50 | Memantine inhibition of α-synuclein cell-to-cell transmission in LBD; directly targets LBD's core pathological mechanism and most mechanistically relevant to this repurposing rationale |
| [NCT04117178](https://clinicaltrials.gov/study/NCT04117178) | Phase 4 | Completed | 132 | Anti-dementia drug (donepezil + memantine) serum level monitoring study; pharmacokinetic design with indirect relevance to clinical monitoring context for LBD |

> ⚠️ All four trials tested **memantine**, not amantadine directly. No clinical trials specifically investigating Amantadine in LBD were identified in the current search. This gap is the primary rationale for the "Proceed with Guardrails" rather than "Go" recommendation.

---

## Literature Evidence

*(Lewy Body Dementia — primary candidate)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [26085043](https://pubmed.ncbi.nlm.nih.gov/26085043/) | 2015 | Systematic Review & Meta-analysis | Am J Psychiatry | Comprehensive pharmacological management review of LBD covering all drug classes; establishes NMDA antagonism as a supported treatment strategy |
| [24406251](https://pubmed.ncbi.nlm.nih.gov/24406251/) | 2015 | Systematic Review & Meta-analysis | Am J Geriatr Psychiatry | Meta-analysis of memantine specifically in Lewy body disorders; demonstrates statistically significant efficacy with acceptable safety across pooled RCT data |
| [24828899](https://pubmed.ncbi.nlm.nih.gov/24828899/) | 2015 | Systematic Review | J Neurol Neurosurg Psychiatry | Updated systematic review with meta-analysis and trial sequential analysis of ChEI and memantine in PD, PDD, and DLB; quantifies NMDA antagonist treatment effect sizes |
| [19517247](https://pubmed.ncbi.nlm.nih.gov/19517247/) | 2009 | RCT | Neurosci Behav Physiol | Open controlled 16-week RCT of memantine in clinically diagnosed LBD (n=23); positive findings for cognition and behavioural symptoms |
| [24737460](https://pubmed.ncbi.nlm.nih.gov/24737460/) | 2015 | RCT | Int J Geriatr Psychiatry | Memantine improves attention and episodic memory in DLB and PDD using automated cognitive testing; domain-specific benefit profile relevant to clinical endpoints |
| [39177108](https://pubmed.ncbi.nlm.nih.gov/39177108/) | 2024 | Prospective cohort | Alzheimer's Dement | Up to 10-year follow-up of ChEI and memantine in DLB: long-term effects on cognitive decline, major cardiovascular events, and all-cause mortality |
| [24993765](https://pubmed.ncbi.nlm.nih.gov/24993765/) | 2014 | Prospective study | BMJ Open | Memantine treatment associated with improved survival in DLB and PDD; supports disease-course modification potential of NMDA antagonism |
| [20872929](https://pubmed.ncbi.nlm.nih.gov/20872929/) | 2010 | RCT analysis | Int J Geriatr Psychiatry | Memantine effect on REM sleep behaviour disorder and excessive daytime sleepiness in DLB/PDD; evidence of broader symptomatic benefit beyond cognition |
| [22806065](https://pubmed.ncbi.nlm.nih.gov/22806065/) | 2012 | Clinical Trial Review | Curr Neurol Neurosci Rep | Comprehensive review of DLB and PDD clinical trials through 2012; summarises accumulating memantine evidence as "particularly effective for PDD" |
| [26411499](https://pubmed.ncbi.nlm.nih.gov/26411499/) | 2016 | Review | Parkinsonism Relat Disord | PD and DLB cognitive impairment: shared clinical and neuropathological features that underpin the class-effect mechanistic rationale for Amantadine in LBD |

---

## Singapore Market Information

Amantadine is currently **not registered** with Singapore's Health Sciences Authority (HSA). No product licences were identified in the regulatory database search (0 active registrations).

If this candidate proceeds to clinical implementation in Singapore, a regulatory pathway assessment and formal HSA product registration would be required prior to any prescribing activity.

---

## Safety Considerations

Complete package insert safety data (HSA-registered warnings, contraindications, and drug interactions for Amantadine) was not available for this review. Please refer to current international prescribing information (e.g., US FDA Prescribing Information or EMA SmPC) for the full safety profile.

**Critical safety signal specific to the LBD indication:**
- **Dopaminergic hypersensitivity in LBD**: LBD patients are well-documented to be highly sensitive to dopaminergic agents. Amantadine's dopamine-promoting mechanism may **precipitate or worsen hallucinations, psychosis, and agitation** in this population — a risk substantially greater than that seen in standard PD use. This represents the primary safety barrier to repurposing and must be addressed in any clinical programme design.
- **Mandatory monitoring requirement**: Neuropsychiatric assessment (hallucination frequency and severity, NPI score, UPDRS non-motor subscales) at baseline and regular intervals is non-negotiable for this indication.
- **Drug interaction consideration**: LBD patients are frequently co-prescribed cholinesterase inhibitors (rivastigmine, donepezil). Interaction data between Amantadine and these agents in the LBD context should be reviewed before clinical initiation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Amantadine shares the NMDA receptor pharmacological target with memantine, for which multiple completed Phase 2/3/4 RCTs and systematic meta-analyses demonstrate efficacy and tolerability in Lewy body dementia. The candidate's existing approval for Parkinson's disease — a condition on the same pathological spectrum as LBD — provides additional biological plausibility. The critical limiting factors are the complete absence of direct Amantadine trials in LBD and the well-documented dopaminergic hypersensitivity risk in this patient population, both of which can be addressed through a structured evidence-generation programme.

**To proceed, the following is needed:**

- Obtain complete prescribing information for Amantadine (HSA registered product or international label equivalent) to formally document contraindications and black-box warnings before any clinical use
- Commission a head-to-head pharmacological comparison of Amantadine vs memantine in the LBD context, specifically evaluating whether Amantadine's additional dopaminergic activity confers net benefit or harm in this hypersensitive population
- Design a prospective Phase 2 pilot study in early-stage LBD with mandatory neuropsychiatric safety monitoring as a primary safety endpoint (hallucination scales, Neuropsychiatric Inventory, UPDRS Part I)
- Review drug interaction data for Amantadine combined with cholinesterase inhibitors (standard-of-care co-medications in LBD)
- Initiate HSA regulatory pathway assessment for Singapore market entry (registration application or compassionate use framework)
- Address the four Hold candidates (Rasmussen, transaldolase deficiency, fructose-1,6-bisphosphatase deficiency, X-linked ID syndromes) only if targeted preclinical studies establish a mechanistic connection, as current TxGNN predictions for these appear to reflect graph diffusion artefacts rather than true biological signal