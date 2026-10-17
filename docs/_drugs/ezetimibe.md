---
layout: default
title: Ezetimibe
parent: High Evidence (L1-L2)
nav_order: 415
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Ezetimibe: predicted new indication Hyperlipoproteinemia (evidence level L1). Approved use: Hyperlipidemia (including familial hypercholesterolemia and sitostero…"
monitor_inn: "Ezetimibe"
predicted_indications: ["hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "cholesterol-ester transfer protein deficiency", "HIV infectious disease", "hypercholesterolemia, autosomal dominant", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
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

# Ezetimibe: From Hyperlipidemia to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is a cholesterol-absorption inhibitor originally used for hyperlipidemia, including familial and homozygous familial hypercholesterolemia and sitosterolemia.
The TxGNN model predicts it may be effective for **hyperlipoproteinemia**, with **40 clinical trials** and **20 publications** currently supporting this direction.
Because this predicted indication largely overlaps with the drug's established lipid-lowering use, it is effectively an on-label or near-label use rather than a true repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia (including familial hypercholesterolemia and sitosterolemia). The Singapore licence records contain no indication text, so this comes from the knowledge-graph indication data. |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, ezetimibe inhibits NPC1L1-mediated absorption of cholesterol in the intestine, which lowers LDL cholesterol. This is the drug's core mechanism and is the same one behind its use in hyperlipidemia.

Hyperlipoproteinemia is a disorder of elevated lipoproteins, closely related to the hyperlipidemia conditions ezetimibe is already used for. The mechanism therefore applies directly, and the prediction is well supported. It does not represent a new therapeutic area.

Other predictions in the same list fall into three groups:
- **Established or near-label lipid uses:** familial hypercholesterolemia and autosomal dominant hypercholesterolemia, both supported by Phase 3 trials.
- **A secondary-indication question:** HIV-associated dyslipidemia. Ezetimibe is not an antiviral. The benefit is in treating the metabolic complication, and ezetimibe has minimal CYP450 interaction with antiretrovirals.
- **Unsupported or irrelevant predictions:** CETP deficiency, feline and simian immunodeficiency, and an unrelated neurodevelopmental disorder. These have little or no evidence and appear to be graph-based artifacts.

---

## Clinical Trial Evidence

Trials most relevant to the predicted indication (hyperlipoproteinemia / hypercholesterolemia):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Phase 4 | Completed | 40 | Randomized comparison of ezetimibe versus statin in hypercholesterolemia |
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Phase 3 | Completed | 511 | Evolocumab versus ezetimibe in statin-intolerant patients (ezetimibe as comparator) |
| [NCT03847506](https://clinicaltrials.gov/study/NCT03847506) | Phase 4 | Completed | 127 | Ezetimibe/rosuvastatin plus candesartan/amlodipine in hypertension with hyperlipidemia |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | Terminated | 49 | Open-label ezetimibe 10 mg/day in homozygous FH or sitosterolemia |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe added to atorvastatin or simvastatin in homozygous FH |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Completed | 1,220 | Ezetimibe/simvastatin plus niacin in type IIa/IIb hyperlipidemia |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Fenofibrate plus ezetimibe in mixed hyperlipidemia |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin plus fenofibrate in mixed hyperlipidemia |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE: ezetimibe plus high-dose simvastatin versus simvastatin alone in heterozygous FH |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | N/A (post-marketing) | Completed | 4,105 | Safety, tolerability and efficacy of ezetimibe in Filipino patients |

Several other trials (for example NCT06005597 and NCT01763905) use ezetimibe as a comparator or background therapy, so they give only indirect support. NCT06789432 was withdrawn with no participants and provides no evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide in heterozygous FH (indirect; ezetimibe is background therapy) |
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | Phase 3 RCT | Lancet | TANDEM: obicetrapib/ezetimibe fixed-dose combination for LDL-C reduction |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | RCT | Lancet | RUTHERFORD-2: evolocumab in heterozygous FH despite statin with or without ezetimibe |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Mol Med Rep | Research advances in drugs targeting hyperlipidemia |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | New and emerging LDL-C and apoB lowering therapies on top of statins and ezetimibe |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovasc Pharmacol Ther | Comprehensive review of PCSK9 inhibitors |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Drug bulletin | Drug Ther Bull | Ezetimibe update: lowers LDL-C alone or with a statin |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Cohort | Lancet | Worldwide retrospective cohort of homozygous FH |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiol Clin | FH review listing ezetimibe among LDL-lowering treatments |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Consensus statement | Eur Heart J | European Atherosclerosis Society guidance on FH screening and treatment |

---

## Singapore Market Information

Ezetimibe has 20 valid licences in Singapore (single-entry records, including combination products such as ezetimibe with statins). The records contain no approved-indication text. The main ones are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12375P | EZETROL TABLET 10 mg | Tablet | Not stated in the records |
| SIN15179P | EZETIMIBE SANDOZ TABLET 10MG | Tablet | Not stated in the records |
| SIN15183P | ZIMIEX TABLET 10MG | Tablet | Not stated in the records |
| SIN15114P | ATOZET TABLET 10MG/20MG | Film-coated tablet | Not stated in the records |
| SIN13011P | VYTORIN 10/10 TABLET | Tablet | Not stated in the records |

---

## Safety Considerations

- **Contraindication-related conditions (knowledge-graph data, not label text):** pancreatitis, liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, substance abuse/dependence, rhabdomyolysis and nodular fasciitis. Several of these are likely to reflect combination products with statins.
- **Drug interactions:** 100 interactions were identified in total. Moderate-level ones include chenodeoxycholic acid, eluxadoline, rosuvastatin and simvastatin. Others, such as pantoprazole, metformin and omeprazole, are of unknown severity.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials, together with large post-marketing studies, support ezetimibe's lipid-lowering efficacy, and the drug is already marketed in Singapore. The indication is essentially an extension of existing hyperlipidemia use, so the main risk is label scope and safety, not efficacy.

**To proceed, the following is needed:**
- Singapore package-insert warnings and contraindications (currently unavailable)
- Mechanism-of-action data from DrugBank
- Confirmation of the approved-indication wording on each Singapore licence
- Safety review of statin-combination products, given the muscle and liver signals
- A decision on whether HIV-associated dyslipidemia should be handled as a separate research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

