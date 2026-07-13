---
layout: default
title: Lovastatin
parent: 僅模型預測 (L5)
nav_order: 568
evidence_level: L5
indication_count: 10
---

# Lovastatin
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

# Lovastatin: From Hyperlipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Lovastatin is a well-established HMG-CoA reductase inhibitor (statin) used globally to treat various forms of hyperlipidemia by suppressing hepatic cholesterol synthesis and upregulating LDL receptors.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**, with **3 clinical trials** and **19 publications** identified in this therapeutic area — however, most evidence concerns competing drugs, and the direct clinical data for Lovastatin in HoFH reveals a critical mechanistic caveat tied to LDL receptor (LDLR) function.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Primary hypercholesterolemia / Hyperlipidemia (globally established; not registered in Singapore) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Lovastatin is not available in the current evidence pack. Based on established pharmacology, Lovastatin is a prodrug belonging to the statin class. After hepatic conversion to its active acid form, it competitively inhibits HMG-CoA reductase — the rate-limiting enzyme in cholesterol biosynthesis. This reduces endogenous cholesterol production and triggers compensatory upregulation of LDL receptors (LDLR) on hepatocyte surfaces, increasing LDL-C clearance from plasma. In patients with at least one functional LDLR allele, this mechanism reliably lowers LDL-C by 25–45%.

The challenge for HoFH lies in its genetics: biallelic loss-of-function mutations in the LDLR gene leave patients with severely deficient or absent receptor activity. In **receptor-negative** HoFH (both alleles non-functional), Lovastatin's principal mechanism of action — inducing LDLR upregulation — simply cannot operate. A 1988 clinical study (PMID 3397806) confirmed this directly: Lovastatin at 2 mg/kg/day in three receptor-negative HoFH children produced no decrease in LDL-C levels or LDL turnover. In contrast, a 1986 JAMA case report (PMID 3534334) demonstrated that Lovastatin could normalize cholesterol in a post-liver-transplant HoFH child — precisely because the transplant restored approximately 60% of normal LDLR activity.

This distinction is clinically decisive. **Receptor-defective** HoFH variants (compound heterozygotes retaining partial LDLR function) may derive some benefit from Lovastatin, while receptor-negative patients are unlikely to respond. The TxGNN model's prediction captures Lovastatin's broad relevance to the cholesterol metabolism pathway, but the clinical reality is that HoFH represents a pharmacogenomically stratified population where LDLR residual activity is the critical determinant of treatment response. Current standard-of-care trials for HoFH focus on agents that bypass LDLR dependence entirely — such as ezetimibe (intestinal cholesterol absorption blockade) and PCSK9 inhibitors — which further limits Lovastatin's repurposing value here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg added to atorvastatin or simvastatin in HoFH — primary endpoint was LDL-C reduction; established the ezetimibe + statin combination as a reference standard |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab (PCSK9 inhibitor) in children/adolescents aged 8–17 with HoFH — evaluated LDL-C reduction at Weeks 12, 24, and 48; represents current biologic first-line therapy |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | 24-month open-label safety extension of NCT03884452 — long-term tolerability of ezetimibe co-administered with atorvastatin or simvastatin in HoFH patients |

> **Important note:** None of these trials directly investigates Lovastatin as an intervention for HoFH. They characterize the current competitive treatment landscape — agents that Lovastatin would need to outperform or complement in this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12034651](https://pubmed.ncbi.nlm.nih.gov/12034651/) | 2002 | RCT | Circulation | Multicenter, double-blind RCT of ezetimibe + atorvastatin or simvastatin in 50 HoFH patients — additional 15–20% LDL-C reduction vs. statin alone; demonstrated ezetimibe utility in LDLR-independent pathway |
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | Clinical Study | J Pediatrics | **Key negative finding for Lovastatin in HoFH**: 3 receptor-negative HoFH children treated with Lovastatin 2 mg/kg/day — no decrease in LDL-C levels or LDL turnover, confirming LDLR dependence of statin efficacy |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | Clinical Study | Anales Espanoles de Pediatria | Lovastatin combined with probucol and cholestyramine in 2 HoFH patients — moderate cholesterol reduction observed in patients classified as receptor-defective (residual LDLR activity), not receptor-negative |
| [29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/) | 2018 | Cohort | Arterioscler Thromb Vasc Biol | HoFH patients with identical LDLR mutations showed highly variable LDLR protein expression, explaining differential response to evolocumab; underscores that genotype alone does not predict residual receptor function |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | Case Report | JAMA | Post-liver-transplant HoFH child treated with Lovastatin (mevinolin) — cholesterol normalized once transplant restored ~60% of normal LDLR activity; mechanistically confirms that Lovastatin efficacy in HoFH is gated by receptor availability |
| [7229037](https://pubmed.ncbi.nlm.nih.gov/7229037/) | 1981 | In Vitro | J Clin Invest | ML-236b (compactin, a statin precursor) on HoFH fibroblasts — receptor-defective cells showed compensatory LDL receptor upregulation; receptor-negative cells did not respond; foundational mechanistic basis for LDLR-dependence |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | Clinical Study | Eur J Pediatrics | LDL plasmapheresis with and without Lovastatin in a 7-year-old HoFH girl — Lovastatin did not meaningfully reduce baseline LDL-C but appeared to slow cholesterol rebound between apheresis sessions |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Ezetimibe pharmacology and clinical efficacy review — ~12% additional LDL-C reduction on top of statin therapy in hypercholesterolemia including HoFH subgroup; rationalizes LDLR-independent add-on strategies |
| [15554726](https://pubmed.ncbi.nlm.nih.gov/15554726/) | 2004 | Review | Am J Cardiovasc Drugs | Ezetimibe/simvastatin combination — complementary dual blockade of intestinal cholesterol absorption and hepatic cholesterol synthesis; relevant benchmark for multi-mechanism strategies in HoFH |
| [29233637](https://pubmed.ncbi.nlm.nih.gov/29233637/) | 2018 | Case Report | J Clin Lipidology | Compound heterozygous FH in a Chinese pediatric patient with de novo and transmitted LDLR mutations — illustrates phenotypic and genetic complexity of HoFH subtypes relevant to treatment selection |

---

## Singapore Market Information

Lovastatin currently has **no registered products** with the Health Sciences Authority (HSA) of Singapore (0 authorizations on record). Any clinical or commercial development in Singapore would require a full new drug registration process.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's 99.89% confidence score reflects Lovastatin's deep mechanistic relevance to cholesterol homeostasis broadly, but published clinical data in HoFH specifically reveals a binary response pattern: receptor-negative HoFH patients — who represent the majority of severe cases — show no measurable LDL-C response to Lovastatin, while receptor-defective variants with residual LDLR activity may derive partial benefit. All three identified Phase 3 trials test competing agents (ezetimibe, alirocumab) that bypass LDLR dependence, and Lovastatin holds no Singapore market authorization.

**To proceed, the following is needed:**
- **LDLR subtype stratification**: Characterize the target HoFH population by residual LDLR activity (receptor-negative vs. receptor-defective); Lovastatin repurposing is only viable in the receptor-defective subgroup
- **Safety package**: Obtain full package insert data including contraindications, key warnings, and drug interaction profile (currently absent) — particularly critical given the known risk of myopathy and rhabdomyolysis with statin class agents
- **Combination therapy positioning**: If receptor-defective patients are identified, evaluate Lovastatin as part of a multi-drug regimen (e.g., with ezetimibe or bile acid sequestrants) rather than as monotherapy, consistent with historical combination approaches
- **Singapore registration pathway**: Develop a regulatory strategy with HSA since Lovastatin is currently unregistered in Singapore
- **Pharmacogenomic baseline**: Consider SLCO1B1 rs4149056 genotyping in the target population given known associations with statin-associated muscle symptoms, particularly relevant for long-term therapy in FH patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

