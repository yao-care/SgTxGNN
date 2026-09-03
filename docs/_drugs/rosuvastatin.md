---
layout: default
title: Rosuvastatin
parent: 僅模型預測 (L5)
nav_order: 876
evidence_level: L5
indication_count: 10
---

# Rosuvastatin
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

# Rosuvastatin: From Hypercholesterolemia to Familial Hypercholesterolemia

## One-Sentence Summary

> Rosuvastatin is a statin (HMG-CoA reductase inhibitor) globally used to treat hypercholesterolemia and mixed dyslipidemia, though it currently has **no marketed product or registration record in Singapore**.
> Across 10 TxGNN-predicted candidates, the strongest evidence-supported new/expanded indication is **Familial Hypercholesterolemia (FH)**,
> supported by **22 clinical trials** (multiple Phase 3, directly using rosuvastatin) and **13 publications**, including RCTs in pediatric HeFH/HoFH populations.
> The literal top-ranked TxGNN prediction (CETP deficiency) had a similar score but almost no supporting evidence and is not recommended to proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Singapore records (drug not locally marketed); globally, rosuvastatin is indicated for hypercholesterolemia and mixed dyslipidemia as an HMG-CoA reductase inhibitor |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.54% (rank 6,166 of TxGNN output) |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available from structured sources for this evidence pack. Based on well-established pharmacology, rosuvastatin belongs to the statin (HMG-CoA reductase inhibitor) class: it blocks hepatic cholesterol synthesis, which upregulates LDL receptor expression and lowers circulating LDL-C.

Familial Hypercholesterolemia (heterozygous and homozygous forms) is caused by defective LDL-receptor–mediated clearance, resulting in markedly elevated LDL-C from birth. Because rosuvastatin's core mechanism directly targets the same LDL-C pathway that is dysregulated in FH, the mechanistic link is strong and direct — unlike several other TxGNN-predicted candidates in this pack (e.g., CETP deficiency, hepatic triglyceride lipase deficiency) where the primary lipid abnormality is HDL-related and only weakly connected to statin pharmacology.

In practice, rosuvastatin (Crestor®) is already an internationally approved label indication for HeFH and HoFH, including in pediatric populations. This evidence pack therefore functions less as discovery of a *novel* indication and more as a **validation that the TxGNN model correctly recovers a known, clinically established use** — which is reassuring from a model-reliability standpoint but means the "new indication" framing should be treated with appropriate caution given Singapore has no local registration or label to confirm this use locally.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01078675](https://clinicaltrials.gov/study/NCT01078675) | Phase 3 | Completed | 315 | Rosuvastatin efficacy and 2-year safety/PK in children and adolescents (6–<18y) with FH |
| [NCT00355615](https://clinicaltrials.gov/study/NCT00355615) | Phase 3 | Completed | 173 | 12-week DB RCT + 40-week open-label follow-up of rosuvastatin in HeFH children aged 10–17 |
| [NCT02226198](https://clinicaltrials.gov/study/NCT02226198) | Phase 3 | Completed | 20 | Randomized, double-blind, placebo-controlled crossover study of rosuvastatin in HoFH children/adolescents |
| [NCT02434497](https://clinicaltrials.gov/study/NCT02434497) | Phase 3 | Completed | 9 | Open-label long-term extension evaluating rosuvastatin safety in HoFH children/adolescents |
| [NCT00654602](https://clinicaltrials.gov/study/NCT00654602) | Phase 3 | Completed | 1,500 | 48-week open-label, non-comparative study of rosuvastatin efficacy/safety in Fredrickson IIa/IIb dyslipidemia including HeFH |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | 6-week RCT assessing renal effects of rosuvastatin vs. simvastatin in Fredrickson IIa/IIb dyslipidemia including HeFH |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | RCT of alirocumab add-on to stable statin therapy (including rosuvastatin) in HeFH/high CV-risk patients |
| [NCT06686615](https://clinicaltrials.gov/study/NCT06686615) | Observational | Recruiting | 2,000 | Real-world effectiveness/safety of bempedoic acid + ezetimibe + rosuvastatin or atorvastatin in primary hypercholesterolemia/mixed dyslipidemia |
| [NCT05367310](https://clinicaltrials.gov/study/NCT05367310) | Observational | Active, not recruiting | 50 | Effect of breastfeeding on lipid profile/CV risk markers in women with FH |
| [NCT02976818](https://clinicaltrials.gov/study/NCT02976818) | Observational | Completed | 173 | Relationship between Lp(a) levels and aortic valve calcification in heterozygous FH |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28592434](https://pubmed.ncbi.nlm.nih.gov/28592434/) | 2017 | RCT | Circulation | CHARON study: 2-year rosuvastatin treatment reduced carotid intima-media thickness in children with HeFH |
| [28838366](https://pubmed.ncbi.nlm.nih.gov/28838366/) | 2017 | Cohort | J Am Coll Cardiol | Rosuvastatin efficacy in children with HoFH, association with underlying LDLR genetic mutations |
| [20223367](https://pubmed.ncbi.nlm.nih.gov/20223367/) | 2010 | Cohort | J Am Coll Cardiol | Efficacy and safety of rosuvastatin therapy for children with FH |
| [26687694](https://pubmed.ncbi.nlm.nih.gov/26687694/) | 2015 | Cohort (CHARON) | J Clin Lipidol | Efficacy and safety of rosuvastatin in children/adolescents with FH; results from the CHARON study |
| [26387811](https://pubmed.ncbi.nlm.nih.gov/26387811/) | 2016 | PK study | Eur J Clin Pharmacol | Population pharmacokinetics of rosuvastatin in pediatric HeFH patients |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Review | Endocr Pract | AACE/ACE guidelines for management of dyslipidemia and CVD prevention |
| [26988948](https://pubmed.ncbi.nlm.nih.gov/26988948/) | 2016 | Review | J Am Coll Cardiol | Improving the monitoring and care of patients with FH |
| [28838367](https://pubmed.ncbi.nlm.nih.gov/28838367/) | 2017 | Review | J Am Coll Cardiol | Managing patients with homozygous FH |

---

## Singapore Market Information

Rosuvastatin is currently **not marketed and has no registration records in Singapore** (0 licenses on file); no approved local label indication can be cited for this drug at this time.

---

## Other Predicted Indications Considered

This evidence pack evaluated 10 TxGNN-predicted candidates for rosuvastatin. Only Familial Hypercholesterolemia (above) and general Hyperlipidemia reached actionable evidence levels; the remainder lack sufficient clinical support:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|
| 1 | Cholesterol-ester transfer protein deficiency | 99.54% | L4 | Hold |
| 2 | **Familial hypercholesterolemia** | 99.54% | **L1** | **Proceed with Guardrails** |
| 3 | Hypercholesterolemia due to CYP7A1 deficiency | 99.51% | L4 | Hold |
| 4 | Brain stem infarction | 99.44% | L4 | Hold |
| 5 | HIV infectious disease | 99.37% | L2 | Research Question |
| 6 | Hypoalphalipoproteinemia | 99.25% | L3 | Research Question |
| 7 | Neurodevelopmental disorder (rare genetic) | 99.22% | L5 | Hold |
| 8 | Hyperlipidemia due to hepatic triglyceride lipase deficiency | 99.20% | L5 | Hold |
| 9 | ABri amyloidosis | 99.18% | L5 | Hold |
| 10 | Hyperlipidemia | 99.09% | L1 | Proceed with Guardrails |

Notes on other candidates:
- **HIV infectious disease (rank 5, L2)**: Evidence supports rosuvastatin as adjunct anti-inflammatory/lipid-lowering therapy for cardiovascular risk in HIV patients on antiretroviral therapy — not treatment of the HIV infection itself. The indication label is potentially misleading and should be reframed as "cardiovascular risk reduction in HIV" if pursued.
- **Hyperlipidemia (rank 10, L1)**: This is effectively rosuvastatin's core, already-established global indication rather than a novel repurposing candidate; included here as an internal consistency check on the model.
- **Ranks 1, 3, 4, 6, 7, 8, 9**: Driven by high TxGNN similarity scores but supported only by case reports, preclinical/mechanistic studies, or no evidence at all — not suitable for further evaluation at this time.

---

## Safety Considerations

Please refer to the package insert for safety information. Structured warning, contraindication, and drug-interaction data were not available in this evidence pack (TFDA/local label data and DDI query both returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Familial Hypercholesterolemia is supported by multiple completed Phase 3 trials directly studying rosuvastatin (including pediatric HeFH/HoFH populations) and consistent literature evidence (L1). However, this indication is already an established global label use rather than a novel discovery, and the drug currently has no marketed presence or safety label on file in Singapore, so local regulatory and safety documentation must be established before any guardrails can be finalized.

**To proceed, the following is needed:**
- Obtain TFDA/HSA-equivalent package insert (warnings, contraindications, DDI) — currently a blocking data gap (DG001)
- Confirm detailed mechanism of action (MOA) from DrugBank or primary literature (DG002)
- Determine local regulatory pathway/licensing status if repositioning for the Singapore market is intended
- If HIV-related cardiovascular risk-reduction use (rank 5) is of interest, relabel the indication explicitly to avoid confusion with antiretroviral therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

