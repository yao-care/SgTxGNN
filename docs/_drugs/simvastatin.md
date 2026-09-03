---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 904
evidence_level: L5
indication_count: 10
---

# Simvastatin
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

# Simvastatin: From Hypercholesterolemia to Familial Hypercholesterolemia

## One-Sentence Summary

Simvastatin is a well-established HMG-CoA reductase inhibitor (statin) used globally for hypercholesterolemia and cardiovascular risk reduction. The TxGNN model's top prediction is **Familial Hypercholesterolemia (FH)** — a genetic subtype of the drug's own core indication rather than a genuinely novel use — and this direction is backed by **18 clinical trials** and **20 publications**, including multiple completed Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the Singapore regulatory data (product currently unregistered); internationally, simvastatin is approved for hypercholesterolemia/mixed dyslipidemia and cardiovascular risk reduction |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Simvastatin is an HMG-CoA reductase inhibitor: it blocks hepatic cholesterol biosynthesis, which compensatorily upregulates LDL-receptor (LDLR) expression and increases clearance of circulating LDL-C. This is the exact mechanism relevant to Familial Hypercholesterolemia, a genetic disorder caused by LDLR dysfunction (or related pathway defects) that leads to markedly elevated LDL-C and premature cardiovascular disease.

Importantly, the evidence pack itself flags that this is **not a strict repurposing case**: FH is already a core, well-established indication for statins as a drug class, and simvastatin has been extensively studied — alone and in combination with ezetimibe or PCSK9 inhibitors (alirocumab) — specifically in heterozygous and homozygous FH populations. The high TxGNN score therefore reflects the model correctly identifying a strong, biologically confirmed drug-disease relationship rather than uncovering an unexpected new use. Given that simvastatin is currently unregistered in Singapore, the practical value of this prediction lies in supporting a potential market re-entry or registration pathway targeting FH specifically, rather than discovering a new mechanism of action.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg added to atorvastatin or simvastatin in homozygous FH — efficacy/safety demonstrated |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: ezetimibe + high-dose simvastatin vs. simvastatin alone on carotid atherosclerosis progression in heterozygous FH |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | Alirocumab as add-on to stable statin therapy vs. placebo in HeFH/high CV risk patients |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Alirocumab (REGN727) in heFH inadequately controlled on lipid-modifying therapy |
| [NCT01414192](https://clinicaltrials.gov/study/NCT01414192) | N/A (observational) | Completed | 3,215 | Real-world bridging cohort on ezetimibe ± statin use patterns and LDL-C goal attainment |
| [NCT01507831](https://clinicaltrials.gov/study/NCT01507831) | Phase 3 | Completed | 2,341 | Long-term safety/tolerability of alirocumab added to statin therapy in high CV risk hypercholesterolemia |
| [NCT01954394](https://clinicaltrials.gov/study/NCT01954394) | Phase 3 | Completed | 986 | Open-label extension assessing long-term alirocumab safety/efficacy in heFH |
| [NCT01070966](https://clinicaltrials.gov/study/NCT01070966) | N/A (re-examination) | Completed | 2,089 | Post-marketing safety/efficacy survey of VYTORIN (ezetimibe/simvastatin) in routine practice |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3b | Completed | 442 | Head-to-head renal effects of rosuvastatin vs. simvastatin in FH/mixed dyslipidemia |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe + simvastatin efficacy/safety in adolescents with heterozygous FH |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | New England Journal of Medicine | Simvastatin with or without ezetimibe in FH (ENHANCE trial) — landmark RCT on atherosclerosis progression |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opinion on Drug Safety | Benefits and risks of simvastatin in familial hypercholesterolemia |
| [15554726](https://pubmed.ncbi.nlm.nih.gov/15554726/) | 2004 | Review | Am J Cardiovasc Drugs | Review of ezetimibe/simvastatin combination in hypercholesterolemia management |
| [2083515](https://pubmed.ncbi.nlm.nih.gov/2083515/) | 1990 | Review | Drugs | Pharmacological properties and therapeutic potential of simvastatin in hypercholesterolemia |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Statins for children with familial hypercholesterolemia — efficacy/safety synthesis |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort | Journal of the American College of Cardiology | Statin use in FH associated with reduced coronary artery disease and all-cause mortality |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Safety | Benefits and risks of simvastatin specifically in FH patients |
| [32800790](https://pubmed.ncbi.nlm.nih.gov/32800790/) | 2020 | Case Report | Journal of Clinical Lipidology | Long-term pharmacological management of a child with severe compound heterozygous FH |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cross-sectional Study | Journal of Clinical Medicine | Effects of simvastatin on cellular immunity parameters in children with FH |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice | AACE/ACE guidelines for dyslipidemia management and cardiovascular disease prevention |

---

## Singapore Market Information

Simvastatin currently holds **no marketing authorization in Singapore** (0 registrations, market status: Not Marketed). No product license, dosage form, or approved indication text is available in the current regulatory dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Supplementary note (not from the drug-level safety field, but surfaced in the evidence pack's literature for a separate indication): multiple publications flag clinically significant CYP3A4-mediated drug-drug interactions between simvastatin and HIV protease inhibitors, with case reports of rhabdomyolysis. This is a well-recognized class-level DDI risk relevant to overall prescribing safety and should be reviewed formally once official TFDA/local labeling data becomes available.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The FH indication is supported by an L1 evidence level (multiple completed Phase 3 RCTs, including the landmark ENHANCE trial), but this represents confirmation of simvastatin's existing indication class rather than novel repurposing, and the drug is currently unregistered in Singapore — creating a regulatory rather than scientific gap.

**To proceed, the following is needed:**
- Official TFDA-equivalent labeling data (warnings, contraindications, DDI) — currently blocked per data gap DG001
- Confirmed original/approved indication text and detailed MOA documentation (DG002)
- A regulatory pathway assessment for market registration in Singapore, since no license currently exists
- Formal review of CYP3A4-mediated DDI risk (e.g., with protease inhibitors) prior to any clinical guardrail protocol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

