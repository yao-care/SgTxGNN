---
layout: default
title: Pravastatin
parent: 僅模型預測 (L5)
nav_order: 809
evidence_level: L5
indication_count: 10
---

# Pravastatin
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

# Pravastatin: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pravastatin is a well-established HMG-CoA reductase inhibitor (statin) used to lower LDL cholesterol in patients with high cholesterol/dyslipidemia.
The TxGNN model predicts it may also be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
but this direction is currently supported by only **1 tangentially related clinical trial** (testing a different drug) and a small set of general statin/FH literature — evidence remains preliminary.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | High cholesterol / dyslipidemia (HMG-CoA reductase inhibitor class; drawn from trial background descriptions, not registered as a Singapore-labeled indication) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for pravastatin is not available in our records (data gap). Based on known information, pravastatin belongs to the statin (HMG-CoA reductase inhibitor) class, which lowers LDL cholesterol by inhibiting hepatic cholesterol synthesis and upregulating LDL receptor expression on hepatocytes. Its efficacy in general hypercholesterolemia and heterozygous familial hypercholesterolemia (heFH) is well documented in the literature included in this evidence pack (e.g., pediatric heFH RCTs, long-term follow-up studies).

However, the mechanistic bridge from pravastatin's proven use to **homozygous** FH is weak. HoFH patients typically have severely deficient or absent LDL receptor function, and since statins act primarily by upregulating this same receptor pathway, their efficacy in HoFH is inherently limited. In clinical practice, statins are used only as adjunct background therapy in HoFH, with primary treatment relying on PCSK9 inhibitors (e.g., alirocumab) or LDL apheresis — both mechanistically distinct from statins.

This is reflected in the evidence pack itself: the only clinical trial linked to this indication (NCT03510715) tests **alirocumab**, not pravastatin, and is flagged as low relevance (Grade C) precisely because of this mechanistic mismatch. The prediction should therefore be treated as a research hypothesis rather than an actionable repurposing candidate at this stage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated **alirocumab** (not pravastatin) in children/adolescents with HoFH; assessed LDL-C reduction at 12/24/48 weeks on top of background lipid-lowering therapy (which may include statins). Flagged as low relevance — different drug and mechanism than pravastatin. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Review (Cochrane) | Cochrane Database Syst Rev | Statins are effective and generally safe for lowering LDL-C in children with familial hypercholesterolemia; homozygotes have markedly more severe disease than heterozygotes, with limited statin monotherapy response. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE dyslipidemia management guidelines, including treatment algorithms for familial hypercholesterolemia (including HoFH combination approaches). |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Review (Cochrane) | Cochrane Database Syst Rev | Earlier version of the Cochrane review on statins in pediatric FH; supports efficacy/safety data mainly in heterozygous FH. |
| [31358055](https://pubmed.ncbi.nlm.nih.gov/31358055/) | 2019 | In vitro (iPSC hepatocyte model) | Stem Cell Res Ther | LDLR-deficient iPSC-derived hepatocyte model for FH; a potential preclinical platform to test statin response in receptor-deficient states relevant to HoFH. |
| [34425670](https://pubmed.ncbi.nlm.nih.gov/34425670/) | 2021 | Genetic case study | Iran Biomed J | Identifies a novel LDLRAP1 splice-site variant causing FH, illustrating genetic heterogeneity underlying HoFH phenotypes and variable statin responsiveness. |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin review noting that statins as a class (including pravastatin) are indicated across primary hypercholesterolemia, mixed dyslipidemia, and HoFH, generally as adjunct therapy. |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Comparative statin review showing pravastatin's lipid-lowering potency relative to other statins in general hypercholesterolemia trials (background context only). |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Atorvastatin pharmacology review used as comparator context for statin-class efficacy in hyperlipidemia (not HoFH-specific). |

---

## Singapore Market Information

Pravastatin currently has **no registered product licenses** in Singapore (0 licenses on file; market status: not marketed). No dosage form or approved indication text is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. Local (Singapore) prescribing warnings, contraindications, and drug-drug interaction data are not currently on file — resolving this is flagged as a **blocking gap** for any safety pre-assessment (see Next Steps).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only trial linked to this indication tests a different drug (alirocumab) rather than pravastatin, and the underlying mechanism — LDL receptor upregulation — is inherently limited in HoFH patients who often have absent or severely dysfunctional LDL receptors. Evidence level L3 reflects supportive literature on statins in FH generally, but not direct, disease-specific validation for pravastatin in HoFH.

**To proceed, the following is needed:**
- Direct clinical or observational data on pravastatin (not just statins as a class, or PCSK9 inhibitors) specifically in HoFH patients, stratified by LDL receptor genotype (receptor-negative vs. receptor-defective)
- Local regulatory safety documentation — Singapore HSA package insert warnings, contraindications, and DDI profile (currently a blocking data gap)
- Mechanism of action documentation from DrugBank to support formal mechanistic-relevance scoring
- Given the near-identical, better-evidenced candidate "hypercholesterolemia, autosomal dominant" in the same prediction set (L1 evidence, multiple completed trials, "Proceed with Guardrails" recommendation), consider prioritizing that indication over HoFH for near-term action.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

