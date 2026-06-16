---
layout: default
title: Diphenhydramine
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 10
---

# Diphenhydramine
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

# Diphenhydramine: From Allergic Reactions to Rhinitis

## One-Sentence Summary

Diphenhydramine (Benadryl®) is a first-generation H1 receptor antagonist historically used to treat allergic reactions, anaphylaxis, and urticaria.
The TxGNN model's highest-scoring prediction is rosacea conjunctivitis (99.20%), but that indication carries zero clinical evidence (L5, Hold); the most clinically actionable prediction is **Rhinitis** (98.35%), supported by **7 clinical trials** and **18 publications** reaching **L1 evidence level**.
The evidence firmly confirms efficacy in rhinitis, though contemporary guidelines favour second-generation antihistamines as first-line therapy due to diphenhydramine's CNS and anticholinergic side-effect burden.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic reactions, anaphylaxis, urticaria (first-generation H1 antihistamine) |
| Predicted New Indication | Rhinitis (best-evidenced; TxGNN top score: Rosacea Conjunctivitis) |
| TxGNN Prediction Score | 98.35% (Rhinitis) / 99.20% (Rosacea Conjunctivitis, no evidence) |
| Evidence Level | L1 (Rhinitis) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on established pharmacology, diphenhydramine is a first-generation competitive H1 receptor antagonist that directly blocks histamine binding at H1 receptors in the nasal mucosa, conjunctiva, skin, and central nervous system. Its additional anticholinergic properties suppress secretory gland activity, reducing nasal and ocular discharge. As one of the first antihistamines synthesised (1940s), diphenhydramine essentially established the pharmacological class now routinely used for allergic rhinitis.

The mechanistic link between diphenhydramine and rhinitis is direct and unambiguous: allergen exposure triggers IgE-mediated mast cell degranulation in the nasal mucosa, releasing histamine that binds H1 receptors to produce sneezing, nasal pruritus, and rhinorrhoea. H1 receptor blockade interrupts this cascade at its core. The anticholinergic component provides additional benefit by curtailing glandular hypersecretion, which is particularly relevant in non-allergic rhinitis. TxGNN's high prediction score (98.35%) for rhinitis reflects this robust biological plausibility, validated by decades of clinical data.

The primary clinical guardrail is well-characterised: unlike second-generation antihistamines, diphenhydramine readily crosses the blood–brain barrier. This causes significant sedation, cognitive impairment, and psychomotor performance decrements — risks confirmed across multiple RCTs (PMID 14582817, 8634878, 16800414). The 2019 CSACI position statement (PMID 31582993) explicitly recommends second-generation H1-antihistamines as first-line over diphenhydramine for both rhinitis and urticaria. Diphenhydramine therefore retains a role in specific contexts (acute short-term use, cost-constrained settings, parenteral formulations) rather than as a routine first-line rhinitis therapy.

---

## All Predicted Indications — Summary

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|------------|----------------|----------------|
| 1 | Rosacea Conjunctivitis | 99.20% | L5 | Hold |
| 2 | **Rhinitis** | **98.35%** | **L1** | **Proceed with Guardrails** |
| 3 | Allergic Urticaria | 98.24% | L2 | Proceed with Guardrails |
| 4 | Cold Urticaria | 95.92% | L3 | Research Question |
| 5 | Cauda Equina Syndrome | 95.57% | L5 | Hold |
| 6 | Nasopharyngitis | 94.96% | L4 | Hold |
| 7 | Viral Conjunctivitis | 93.97% | L5 | Hold |
| 8 | Neuralgia | 92.30% | L4 | Research Question |
| 9 | Trigeminal Autonomic Cephalalgia | 92.25% | L3 | Research Question |
| 10 | Glossodynia | 92.08% | L5 | Hold |

---

## Clinical Trial Evidence — Rhinitis (Primary Indication)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00648973](https://clinicaltrials.gov/study/NCT00648973) | Phase 4 | Completed | 1,021 | Randomised, double-blind, placebo- and pseudoephedrine-controlled study directly evaluating diphenhydramine 25 mg and 50 mg for nasal congestion relief in seasonal allergic rhinitis — the largest and most directly relevant efficacy confirmation trial for this indication |
| [NCT00599872](https://clinicaltrials.gov/study/NCT00599872) | Phase 3 | Completed | 430 | SLIT trial for ragweed-induced allergic rhinoconjunctivitis; diphenhydramine used as comparator/rescue medication, providing indirect head-to-head efficacy reference data |
| [NCT00762749](https://clinicaltrials.gov/study/NCT00762749) | Phase 1 | Completed | 36 | Open-label pharmacokinetics of diphenhydramine in children (2–11 years) and adolescents (12–17 years); critical dosing reference for paediatric rhinitis management |
| [NCT05586477](https://clinicaltrials.gov/study/NCT05586477) | Phase 4 | Completed | 20 | Investigated thermoregulatory and sweating responses during exercise in rhinitis patients taking diphenhydramine; confirms anticholinergic safety signal but not a rhinitis efficacy study |
| [NCT06217367](https://clinicaltrials.gov/study/NCT06217367) | Phase 4 | Unknown | 16 | OTC antihistamine effects on thermoregulatory responses under passive heat stress in rhinitis-affected participants; highlights heat-related safety concern |

> Two Phase 3 trials targeting rhinitis (NCT01177852, NCT01199497) were withdrawn with zero enrolment and contribute no usable evidence.

---

## Literature Evidence — Rhinitis (Primary Indication)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [40717751](https://pubmed.ncbi.nlm.nih.gov/40717751/) | 2025 | Review | J Pediatr Pharmacol Ther | Comprehensive review of diphenhydramine's clinical applications and adverse effect profile; confirms established role in allergic rhinitis, anaphylaxis, and urticaria alongside prominent toxicity risks with rapid IV administration |
| [40152721](https://pubmed.ncbi.nlm.nih.gov/40152721/) | 2025 | Review | The Medical Letter | Current treatment recommendations for allergic rhinitis and allergic conjunctivitis; contextualises diphenhydramine within the modern antihistamine hierarchy |
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Position Statement | Allergy Asthma Clin Immunol | CSACI 2019 position statement concluding that second-generation H1-antihistamines are safer and should be first-line over diphenhydramine for rhinitis and urticaria; cites sedation, cognitive impairment, cardiac risk, and overdose mortality as grounds |
| [16680933](https://pubmed.ncbi.nlm.nih.gov/16680933/) | 2006 | RCT | Ann Allergy Asthma Immunol | Double-blind RCT: diphenhydramine vs desloratadine vs placebo in moderate-to-severe seasonal allergic rhinitis; confirms diphenhydramine efficacy but highlights sedation as the key disadvantage relative to second-generation agents |
| [14582817](https://pubmed.ncbi.nlm.nih.gov/14582817/) | 2003 | RCT | Ann Allergy Asthma Immunol | RCT comparing diphenhydramine vs desloratadine in ragweed-induced rhinitis; diphenhydramine significantly impairs vigilance and cognitive function; desloratadine nonsedating at therapeutic doses |
| [8634878](https://pubmed.ncbi.nlm.nih.gov/8634878/) | 1996 | RCT | Ann Allergy Asthma Immunol | RCT in young adults with seasonal allergic rhinitis; diphenhydramine impairs learning ability measurably more than the combination acrivastine/pseudoephedrine and placebo |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Systematic review of first- and newer-generation antihistamines for allergic rhinitis and chronic idiopathic urticaria; practical pharmacy-focused management guidance |
| [33848281](https://pubmed.ncbi.nlm.nih.gov/33848281/) | 2021 | Review | The Medical Letter | Current drug comparison for allergic rhinitis and conjunctivitis; diphenhydramine positioned as legacy agent with established but safety-limited role |
| [16800414](https://pubmed.ncbi.nlm.nih.gov/16800414/) | 2006 | Review | Southern Med J | Efficacy and CNS impairment of antihistamines in seasonal allergic rhinitis; confirms diphenhydramine efficacy at recommended doses with accompanying sedation and performance impairment |
| [36420548](https://pubmed.ncbi.nlm.nih.gov/36420548/) | 2022 | Pilot Study | Tokai J Exp Clin Med | Pilot study of transdermal diphenhydramine applied to the nasal ala in allergic rhinitis/asthma patients; demonstrates novel delivery route with efficacy and reduced systemic side effects vs oral/intranasal routes |

---

## Literature Evidence — Allergic Urticaria (Rank 3, L2)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [40717751](https://pubmed.ncbi.nlm.nih.gov/40717751/) | 2025 | Review | J Pediatr Pharmacol Ther | Confirms diphenhydramine primary use includes urticaria; summarises adverse effect profile critical for monitoring |
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Position Statement | Allergy Asthma Clin Immunol | CSACI: recommends second-generation agents over diphenhydramine for urticaria; first-generation agents associated with sedation, cognitive impairment, and sudden cardiac death |
| [28913986](https://pubmed.ncbi.nlm.nih.gov/28913986/) | 2017 | Review | Allergy Asthma Immunol Res | Pathogenesis and treatment of chronic spontaneous urticaria; diphenhydramine (Benadryl) cited as historical first-line before second-generation agents; omalizumab for refractory cases |
| [34862952](https://pubmed.ncbi.nlm.nih.gov/34862952/) | 2022 | Narrative Review | Adv Therapy | Review of IV antihistamines landscape; IV diphenhydramine remains the only approved IV H1 antihistamine in the USA for acute urticaria until IV cetirizine approval in 2019 |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Management of allergic rhinitis and chronic idiopathic urticaria with oral antihistamines; diphenhydramine role in both conditions reviewed |

---

## Singapore Market Information

Diphenhydramine is **not currently registered** with the Health Sciences Authority (HSA) in Singapore. There are no product licences on record.

> If repurposing or market entry proceeds, a full HSA registration application (NDA or product licence) would be required. Given that diphenhydramine is off-patent and widely available globally (including OTC in the US, UK, and Australia), the regulatory pathway would likely focus on CMC documentation and local labelling requirements rather than clinical de novo evidence generation.

---

## Safety Considerations

Formal TFDA/HSA warning and contraindication data were not retrievable in this evidence pack. The following reflects safety signals consistently documented across the retrieved literature:

- **CNS Depression**: Significant sedation and drowsiness due to blood–brain barrier penetration — a primary reason current guidelines recommend second-generation antihistamines as first-line (PMID 31582993). Multiple RCTs confirm measurable impairment of driving performance, vigilance, and learning (PMID 14582817, 8634878, 15168099).
- **Anticholinergic Effects**: Dry mouth, urinary retention, constipation, blurred vision, and tachycardia — risks amplified in elderly patients and those on other anticholinergic agents.
- **Cardiovascular Risk**: Rapid IV administration associated with hypotension and arrhythmia risk (PMID 40717751); sudden cardiac death reported with overdose (PMID 31582993).
- **Paediatric and Geriatric Risk**: Not recommended in neonates; risk of paradoxical excitation in young children; anticholinergic burden particularly problematic in elderly (Beers Criteria listing).

Please refer to the package insert for complete prescribing information, contraindications, and drug interaction details.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Diphenhydramine demonstrates L1 evidence for rhinitis efficacy — anchored by a large Phase 4 RCT (NCT00648973, n=1,021) and multiple published RCTs — confirming both efficacy and the well-characterised safety trade-off profile. The drug is not registered in Singapore, limiting immediate clinical deployment, and contemporary rhinitis guidelines position it as a secondary option behind second-generation antihistamines.

**To proceed, the following is needed:**
- **Regulatory**: HSA registration application with full CMC, efficacy, and safety dossier; evaluation of OTC vs prescription classification in Singapore context
- **Safety data gap**: Obtain and review formal package insert warnings and contraindications (currently unavailable — marked as Blocking data gap DG001); TFDA/HSA-approved prescribing information
- **MOA documentation**: Retrieve DrugBank mechanism of action data (data gap DG002) to complete mechanistic link analysis for all predicted indications
- **Positioning strategy**: Define clinical niche for diphenhydramine vs second-generation antihistamines — e.g., acute/short-term use, parenteral formulations, cost-sensitive settings, or combination cold/allergy products
- **Risk minimisation plan**: Patient counselling materials addressing sedation risk; contraindication in vehicle operators; dose guidance for special populations (elderly, paediatric, renal/hepatic impairment)
- **Further investigation (Research Questions)**: Cold urticaria (L3), trigeminal autonomic cephalalgia (L3), and neuralgia (L4) merit prospective study design if mechanistic hypothesis validation succeeds; rosacea conjunctivitis, cauda equina syndrome, viral conjunctivitis, and glossodynia (all L5, Hold) require preclinical evidence before any clinical investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

