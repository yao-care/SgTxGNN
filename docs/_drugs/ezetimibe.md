---
layout: default
title: Ezetimibe
parent: High Evidence (L1-L2)
nav_order: 411
evidence_level: L1
indication_count: 10
---

# Ezetimibe
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Ezetimibe: From Lipid Lowering (Label Indication Not Recorded) to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is an oral cholesterol absorption inhibitor, marketed in Singapore under 20 registrations. The TxGNN model predicts it may be effective for **hyperlipoproteinemia**, with over **40 registered clinical trials** (including several completed Phase 3 trials) and **19 publications** in the evidence pack. The source data does not record an original indication, so this is most likely an existing on-label use rather than true repurposing. The approved label should be checked before treating it as a novel candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Ezetimibe blocks NPC1L1-mediated absorption of cholesterol in the intestine, which lowers LDL cholesterol. This is a direct mechanistic match for hyperlipoproteinemia. Detailed mechanism-of-action data is not available in the source record, so this description reflects the known pharmacology of the drug class.

The completed Phase 3 trials support use as an add-on to statins and in combination products, such as ezetimibe/simvastatin and ezetimibe with atorvastatin or rosuvastatin. Because the original-indication field is empty in the source data, the model's prediction probably reflects a standard lipid-lowering use that is missing from the data.

Several other predictions in the pack are weak. Familial hypercholesterolemia largely overlaps this indication and has the same mechanistic rationale. The HIV prediction actually reflects HIV-associated dyslipidemia, a metabolic use. The rare metabolic, neurodevelopmental and veterinary predictions have no clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Completed | 1220 | Randomized, double-blind study of ezetimibe/simvastatin with niacin ER in Type IIa/IIb hyperlipidemia |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin with fenofibrate in mixed hyperlipidemia |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Completed | 587 | Fenofibrate and ezetimibe co-administration in mixed hyperlipidemia |
| [NCT02451098](https://clinicaltrials.gov/study/NCT02451098) | Phase 3 | Completed | 385 | Atorvastatin + ezetimibe vs atorvastatin alone in primary hypercholesterolemia (factorial design) |
| [NCT00195793](https://clinicaltrials.gov/study/NCT00195793) | Phase 3 | Completed | 174 | Fenofibrate or ezetimibe added to atorvastatin in combined hyperlipidemia |
| [NCT00651560](https://clinicaltrials.gov/study/NCT00651560) | Phase 3 | Completed | 167 | Vytorin (ezetimibe/simvastatin) vs atorvastatin for dyslipidemia in adults |
| [NCT02748057](https://clinicaltrials.gov/study/NCT02748057) | Phase 3 | Completed | 135 | 52-week safety and tolerability of ezetimibe + rosuvastatin in Japanese patients |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg added to atorvastatin or simvastatin in homozygous familial hypercholesterolemia |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Phase 4 | Completed | 245 | Coronary plaque regression on IVUS with a cholesterol absorption inhibitor vs a synthesis inhibitor |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | N/A | Completed | 4105 | Post-marketing surveillance of ezetimibe safety and efficacy in Filipino patients |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM Phase 3 trial of an obicetrapib + ezetimibe fixed-dose combination for LDL-C reduction |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide in heterozygous familial hypercholesterolemia, where ezetimibe is background therapy |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Cohort | Lancet | Worldwide retrospective cohort of homozygous familial hypercholesterolemia patients |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Drug review | Drug Ther Bull | Ezetimibe lowers LDL-C alone or with a statin, but cardiovascular outcome evidence was still limited |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiol Clin | Familial hypercholesterolemia treatments, including ezetimibe alongside statins and other agents |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | New LDL-C-lowering therapies built on statins, ezetimibe and PCSK9 inhibitors |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | Review | Circ Res | Overview of cholesterol-lowering agents and the safety of markedly lowering LDL-C |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Mol Sci | Pathophysiology, diagnosis and treatment of postprandial hyperlipidemia |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Consensus statement | Eur Heart J | European Atherosclerosis Society guidance on screening and treating familial hypercholesterolemia |
| [18638604](https://pubmed.ncbi.nlm.nih.gov/18638604/) | 2008 | Commentary | Am J Cardiol | Critique of the ENHANCE trial (ezetimibe + high-dose simvastatin), arguing the surrogate endpoint was limited |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12375P | EZETROL TABLET 10 mg | Tablet | Not stated in source data |
| SIN15183P | ZIMIEX TABLET 10MG | Tablet | Not stated in source data |
| SIN15179P | EZETIMIBE SANDOZ TABLET 10MG | Tablet | Not stated in source data |
| SIN16441P | EZETIMIBE MEVON TABLET 10 MG | Tablet | Not stated in source data |
| SIN16422P | EZOLETA TABLETS 10MG | Tablet | Not stated in source data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials support ezetimibe for hyperlipidemia, and it is widely marketed in Singapore. However, the source data has no original indication, no mechanism-of-action record and no safety data. The candidate therefore cannot be treated as a true repurposing finding until the label is confirmed.

**To proceed, the following is needed:**
- The HSA package insert, to confirm the approved indications (including hyperlipidemia), warnings and contraindications
- Detailed mechanism-of-action data from DrugBank
- A drug-interaction review, especially if the HIV-associated dyslipidemia use is pursued with antiretrovirals, since the interaction query returned no results
- Consideration of a repurposing case only for non-lipid indications, since this one is likely already on-label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

