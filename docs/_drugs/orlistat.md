---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 735
evidence_level: L5
indication_count: 10
---

# Orlistat
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

# Orlistat: From Obesity Management to Fatty Liver Disease (NAFLD/NASH)

## One-Sentence Summary

Orlistat is a gastrointestinal lipase inhibitor originally used for weight management in obesity. Among the 10 TxGNN-predicted indications reviewed, **Fatty Liver Disease (NAFLD/NASH)** is the only candidate backed by real-world evidence — **7 clinical trials** and **20 publications**, including RCTs and meta-analyses directly testing orlistat in NAFLD/NASH populations — while the model's top-ranked hits (hypervitaminosis, rare craniofacial syndromes, etc.) have zero supporting trials or literature and are treated here as low-confidence knowledge-graph associations rather than viable leads.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity / weight management (global indication; not registered in Singapore per current dataset) |
| Predicted New Indication | Fatty Liver Disease (NAFLD/NASH) |
| TxGNN Prediction Score | 85.26% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

**Note on candidate selection:** TxGNN's rank-1 prediction ("hypervitaminosis") scored 99.42%, but its own rationale flags it as a reverse-speculation of a known orlistat side effect (fat-soluble vitamin deficiency) with high safety concern and zero supporting evidence (L5/Hold). Ranks 2–7, 9 (microdeletion syndrome, obsolete hypertelorism, frontorhiny, hypoalphalipoproteinemia, ischemic stroke susceptibility, ABri amyloidosis, homozygous familial hypercholesterolemia) are similarly unsupported — no trials, no literature, and several explicitly flagged as likely knowledge-graph noise. Fatty liver disease (rank 8) is the only candidate with substantive clinical and literature evidence, so it is used as the primary subject of this report. Amenorrhea (rank 10) has one small cohort study and is not covered in depth here.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field returned a data gap). Based on known information, Orlistat is a pancreatic/gastric lipase inhibitor used for obesity and weight management; its efficacy in reducing body weight has been well established, and mechanistically this fat-absorption-reducing effect may directly reduce dietary fat delivery to the liver, plausibly lowering hepatic fat accumulation.

Obesity and NAFLD/NASH are mechanistically and epidemiologically intertwined: excess adiposity and insulin resistance are the primary drivers of hepatic steatosis, and weight loss is recognized as first-line therapy for NAFLD. Since orlistat's core pharmacology (blocking ~30% of dietary fat absorption) produces sustained weight loss, a downstream reduction in hepatic fat content is biologically plausible — and this is not merely theoretical: orlistat has already been directly studied in NASH/NAFLD populations in multiple prospective and randomized trials (see below), rather than relying purely on an indirect "obesity → NAFLD" inference chain.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00207311](https://clinicaltrials.gov/study/NCT00207311) | Phase 4 | Completed | 30 | RCT of orlistat (Xenical) followed by PEG-interferon/Copegus for hepatitis C patients with significant hepatic steatosis or NASH |
| [NCT00160407](https://clinicaltrials.gov/study/NCT00160407) | Phase 4 | Completed | 50 | Orlistat (Xenical) in overweight NASH patients — assessed weight loss and improvement in necroinflammatory/fibrotic liver changes |
| [NCT00001723](https://clinicaltrials.gov/study/NCT00001723) | Phase 2 | Completed | 200 | Safety and efficacy of orlistat in adolescents with obesity-related comorbid conditions (African American and Caucasian cohorts) |
| [NCT04270656](https://clinicaltrials.gov/study/NCT04270656) | N/A | Completed | 46 | Insulin pump therapy effects on liver/metabolic outcomes in T2D patients with non-alcoholic hepatic steatosis (context trial, not orlistat-specific) |
| [NCT05934110](https://clinicaltrials.gov/study/NCT05934110) | Phase 2 | Unknown | 320 | Double-blind RCT comparing EMP16 (with acarbose) vs. modified-release orlistat, conventional orlistat, and placebo in overweight/obesity |
| [NCT06501326](https://clinicaltrials.gov/study/NCT06501326) | Phase 4 | Unknown | 102 | Efficacy/safety of liraglutide (comparator context) in obesity with metabolism-associated fatty liver disease |
| [NCT07437001](https://clinicaltrials.gov/study/NCT07437001) | N/A | Not yet recruiting | 60 | Electroacupuncture effect on central obesity and fatty liver in postmenopausal women (context trial, not orlistat-specific) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36781126](https://pubmed.ncbi.nlm.nih.gov/36781126/) | 2023 | RCT | Am J Clin Nutr | Randomized controlled trial comparing diet vs. orlistat for obesity and metabolic-associated fatty liver disease |
| [38081992](https://pubmed.ncbi.nlm.nih.gov/38081992/) | 2024 | RCT | Eur J Pediatr | RCT of orlistat in overweight/obese adolescents with NAFLD |
| [41768122](https://pubmed.ncbi.nlm.nih.gov/41768122/) | 2026 | Systematic Review / Meta-analysis (RCTs) | Curr Ther Res Clin Exp | GRADE-assessed meta-analysis of orlistat's effect on cardiometabolic indices in MASLD |
| [38910819](https://pubmed.ncbi.nlm.nih.gov/38910819/) | 2024 | Systematic Review / Meta-analysis (RCTs) | Proc (Baylor Univ Med Cent) | Meta-analysis of RCTs on orlistat efficacy in obese patients with NAFLD/MASLD |
| [41069538](https://pubmed.ncbi.nlm.nih.gov/41069538/) | 2024 | Prospective clinical study | Acta Endocrinol (Bucur) | Early effect of orlistat on NASH and atherogenicity indices in obese NAFLD patients |
| [33072533](https://pubmed.ncbi.nlm.nih.gov/33072533/) | 2020 | Systematic Review / Network Meta-analysis | Adv Pharm Bull | Network meta-analysis of pharmacologic treatments (including orlistat) for NAFLD |
| [35501557](https://pubmed.ncbi.nlm.nih.gov/35501557/) | 2022 | Review | Curr Obes Rep | Review of anti-obesity medications' hepatic histology effects in NAFLD |
| [18095746](https://pubmed.ncbi.nlm.nih.gov/18095746/) | 2008 | Review | Drug Safety | Critical review of orlistat-associated adverse effects and drug interactions |
| [27646933](https://pubmed.ncbi.nlm.nih.gov/27646933/) | 2017 | Review | Gut | Review of current and upcoming NAFLD pharmacotherapy, including repurposed agents |
| [30502373](https://pubmed.ncbi.nlm.nih.gov/30502373/) | 2019 | Review | Metabolism | Review of obesity-NAFLD pathophysiology and therapeutic rationale |

---

## Singapore Market Information

Orlistat currently holds no market authorization in Singapore under this dataset (0 registrations on record; market status: **Not Marketed**).

---

## Safety Considerations

Please refer to the package insert for safety information. (Local warnings, contraindications, and drug-interaction data could not be retrieved from the current sources — this is a **blocking** data gap for safety screening, see below.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Orlistat's use in NAFLD/NASH has real supporting evidence — completed Phase 2/4 trials and published RCTs plus two meta-analyses — making it a mechanistically and clinically plausible repurposing candidate. However, orlistat has no current Singapore market registration, and the drug-level safety label (warnings/contraindications) is entirely missing, which blocks the mandatory initial safety screening (S1) regardless of efficacy evidence quality.

**To proceed, the following is needed:**
- Obtain the official package insert (warnings/contraindications) to close the blocking data gap (DG001) and complete S1 safety screening
- Retrieve detailed DrugBank mechanism-of-action data (DG002) to strengthen the mechanistic rationale
- Clarify Singapore/regional regulatory pathway and registration status for orlistat before any local development plan
- Complete drug-drug interaction (DDI) profiling — current query returned no results
- Given most direct evidence is Phase 2/4 with modest sample sizes (N=30–200), consider whether a dedicated Phase 3 RCT in NAFLD/NASH is warranted before advancing beyond guardrail-stage evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

