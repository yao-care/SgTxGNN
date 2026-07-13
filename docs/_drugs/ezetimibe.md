---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 411
evidence_level: L5
indication_count: 10
---

# Ezetimibe
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

# Ezetimibe: From Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is a selective cholesterol absorption inhibitor globally established for reducing elevated LDL-cholesterol in hypercholesterolemia, though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Hyperlipoproteinemia** — a prediction tightly aligned with its known mechanism of action — with **multiple completed Phase 3 trials** and **19 publications** supporting this direction.
This case represents a high-confidence, mechanistically validated prediction, where the primary action required is Singapore regulatory registration rather than exploratory clinical development.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolemia (globally approved; not registered in Singapore) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence package. Based on established pharmacological knowledge, Ezetimibe selectively inhibits the Niemann-Pick C1-Like 1 (NPC1L1) transporter located in the intestinal brush-border membrane. This blocks absorption of both dietary and biliary cholesterol, reducing delivery of cholesterol to the liver. As a compensatory response, hepatic LDL receptors are upregulated, leading to increased clearance of LDL particles from the bloodstream and a net reduction in plasma LDL-C of approximately 15–25% as monotherapy — and greater reductions when combined with a statin.

Hyperlipoproteinemia encompasses a spectrum of disorders defined by elevated plasma lipoprotein concentrations (LDL, VLDL, IDL, and remnant particles), all directly targeted by Ezetimibe's mechanism. Unlike statins, which suppress cholesterol synthesis via HMG-CoA reductase inhibition, Ezetimibe blocks the absorption pathway — a complementary approach targeting a different node in the lipoprotein metabolic network. This dual-pathway rationale has been validated clinically: the landmark IMPROVE-IT trial demonstrated that adding ezetimibe to simvastatin reduced major cardiovascular events beyond what statin therapy alone could achieve. The mechanistic link to hyperlipoproteinemia pathophysiology is therefore both direct and well-established.

The TxGNN model's 99.63% confidence score reflects the tight alignment between Ezetimibe and hyperlipoproteinemia. Multiple major regulatory agencies — including the FDA (Zetia®, Vytorin®), EMA (Ezetrol®, Inegy®), and Japan's PMDA (Zetia®) — have approved Ezetimibe for hypercholesterolemia, and international guidelines (EAS 2013, ACC/AHA) recommend it as first-line adjunct therapy. The fact that Ezetimibe is not yet registered in Singapore despite this robust global evidence base makes this an actionable regulatory filing opportunity rather than a traditional exploratory repurposing case.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Completed | 1,220 | Ezetimibe/Simvastatin co-administered with Niacin in Type IIa or IIb hyperlipidemia — core efficacy and safety evidence for the ezetimibe-based combination approach |
| [NCT02451098](https://clinicaltrials.gov/study/NCT02451098) | Phase 3 | Completed | 385 | Atorvastatin+Ezetimibe combination vs. atorvastatin monotherapy in primary hypercholesterolemia — multicenter, randomized, double-blind factorial design |
| [NCT00651560](https://clinicaltrials.gov/study/NCT00651560) | Phase 3 | Completed | 167 | Vytorin (ezetimibe+simvastatin) vs. atorvastatin in dyslipidemia — assessed ATP-III lipid goal achievement and cardiovascular risk reduction |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg added to atorvastatin or simvastatin in homozygous familial hypercholesterolemia — Phase 3 efficacy and safety evaluation |
| [NCT02748057](https://clinicaltrials.gov/study/NCT02748057) | Phase 3 | Completed | 135 | 52-week safety and tolerability of ezetimibe+rosuvastatin (MK-0653H) in Japanese patients with inadequate LDL-C control on monotherapy |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Phase 4 | Completed | 245 | PRECISE-IVUS: Compared cholesterol absorption inhibitor (ezetimibe arm) vs. synthesis inhibitor on coronary plaque regression measured by intravascular ultrasound |
| [NCT05661552](https://clinicaltrials.gov/study/NCT05661552) | Phase 4 | Completed | 108 | Early initiation of evolocumab combined with statin+ezetimibe in ACS patients undergoing PCI — evaluated lipid profile changes |
| [NCT02942602](https://clinicaltrials.gov/study/NCT02942602) | NA | Completed | 58 | Ezetimibe's effect on HDL function and composition in hyperlipidemia — mechanistic evidence for benefits beyond LDL reduction |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | N/A | Completed | 4,105 | Post-marketing surveillance of ezetimibe safety, tolerability, and efficacy in Filipino patients with hypercholesterolemia — large real-world dataset |
| [NCT04895098](https://clinicaltrials.gov/study/NCT04895098) | N/A | Completed | 1,000 | Retrospective observational study comparing statin monotherapy vs. statin+ezetimibe in both primary and secondary CVD prevention |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | Phase 3 RCT (TANDEM) | The Lancet | Fixed-dose obicetrapib+ezetimibe combination significantly reduced LDL-C vs. placebo — confirms ezetimibe's ongoing role as a cornerstone partner in novel combination therapies |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | Phase 3 RCT | JAMA | Oral PCSK9 inhibitor enlicitide in HeFH patients on background statin+ezetimibe — validates ezetimibe as the established standard-of-care foundation |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Guideline/Consensus | European Heart Journal | EAS consensus: ezetimibe recommended alongside statins for LDL-C reduction and coronary heart disease prevention in familial hypercholesterolemia |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | FH management overview: ezetimibe identified as key second-line agent for LDL-C reduction and cardiovascular event prevention alongside statins and LDL apheresis |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Review | Current Cardiology Reports | FH global burden and management: ezetimibe highlighted as essential guideline-recommended component of lipid-lowering regimens for high-risk patients |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nature Reviews Disease Primers | Comprehensive FH disease primer: ezetimibe's mechanism of intestinal cholesterol absorption inhibition and its clinical role in LDL-C management reviewed in detail |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | Journal of the American College of Cardiology | Emerging LDL-C lowering therapies (JACC Focus Seminar): ezetimibe positioned as the established second-tier foundation upon which newer agents (inclisiran, bempedoic acid) are added |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | Journal of Cardiovascular Pharmacology and Therapeutics | Comprehensive PCSK9 inhibitor landscape review: ezetimibe cited as standard alternative lipid-lowering therapy for statin-intolerant patients |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Review | Indian Heart Journal | FH in Asian populations: ezetimibe recommended for patients not achieving LDL-C targets on statin monotherapy — clinically relevant for Singapore context |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | International Journal of Molecular Sciences | Postprandial hyperlipidemia pathophysiology and treatment: ezetimibe discussed as a therapeutic option targeting intestinal lipoprotein absorption to reduce atherogenic remnant particles |

## Singapore Market Information

Ezetimibe (DrugBank ID: DB00973) is currently **not registered** in Singapore. There are no active HSA product licenses as of the data cutoff (June 2026). This contrasts with its approval in all other major regulatory jurisdictions:

- **FDA (United States)**: Approved as Zetia® (monotherapy) and Vytorin® (ezetimibe/simvastatin fixed-dose combination)
- **EMA (Europe)**: Approved as Ezetrol® and Inegy® (with Merck/MSD)
- **PMDA (Japan)**: Approved as Zetia®, with 12-week and 52-week post-marketing surveillance datasets available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ezetimibe has Level 1 evidence — multiple completed Phase 3 RCTs, major international guideline endorsements, and regulatory approvals across the US, EU, and Japan — firmly supporting its efficacy and safety in hyperlipoproteinemia. The TxGNN model has correctly identified an established, globally validated clinical use. The primary barrier to deployment in Singapore is HSA registration, not clinical uncertainty.

**To proceed, the following is needed:**
- Prepare and submit an HSA registration dossier, leveraging existing FDA/EMA approvals via the abridged evaluation pathway (referencing a well-established regulatory dossier)
- Obtain and review the complete package insert (FDA, EMA, or PMDA approved labeling) for warnings, contraindications, and known drug interactions — particularly with statins, fibrates, and bile acid sequestrants
- Retrieve formal mechanism of action and safety documentation from DrugBank to complete the pharmacological profile (currently flagged as a data gap)
- Assess the Singapore patient population need, prescribing patterns, and potential MOH formulary inclusion pathway
- Evaluate drug interaction profile for at-risk subpopulations, particularly patients on antiretroviral therapy (HIV-associated dyslipidemia), as this evidence gap was flagged in the DDI query log
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

