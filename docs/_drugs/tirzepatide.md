---
layout: default
title: Tirzepatide
parent: 僅模型預測 (L5)
nav_order: 986
evidence_level: L5
indication_count: 10
---

# Tirzepatide
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

# Tirzepatide: From [Original Indication Not Yet Established] to Knee Osteoarthritis

## One-Sentence Summary

Tirzepatide is a dual GIP/GLP-1 receptor agonist; its original approved indication data is currently unavailable in this evidence pack. The TxGNN model's top actionable prediction is **Knee Osteoarthritis** (in patients with obesity), supported by **2 clinical trials** (including an ongoing Phase 4 outcome trial) and **13 publications**. A second signal, **Gout**, is supported by post-hoc RCT analysis but no dedicated trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data (see Data Gap DG002) |
| Predicted New Indication | Osteoarthritis (knee, obesity-associated) |
| TxGNN Prediction Score | 95.92% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available (Data Gap DG002). Based on known pharmacology, tirzepatide is a dual GIP/GLP-1 receptor agonist used for weight management and glycaemic control. GLP-1 receptor signalling is known to produce substantial weight loss and has documented anti-inflammatory effects (reduced synovial pro-inflammatory cytokines such as TNF-α and IL-6), which together provide biological plausibility for benefit in obesity-associated knee osteoarthritis.

Obesity is a well-established mechanical and metabolic risk factor for osteoarthritis progression — reducing joint load through weight loss is a recognized non-pharmacological OA management strategy. Tirzepatide's substantial weight-loss efficacy (demonstrated in trials such as SURMOUNT-1) therefore offers a plausible indirect route to OA symptom improvement, reinforced by a class-level anti-inflammatory mechanism. This is currently being tested directly in an ongoing Phase 4 trial (NCT06191848) designed to assess whether tirzepatide reduces the need for knee replacement in patients with obesity and knee OA.

It is worth noting that a related but distinct top-ranked prediction, gout, has a similar rationale: weight loss and improved insulin sensitivity are associated with lower serum uric acid, supported by a post-hoc analysis of SURMOUNT-1. However, no dedicated gout trials currently exist, placing that signal at an earlier evidentiary stage (S1, Research Question) than osteoarthritis (S2).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06191848](https://clinicaltrials.gov/study/NCT06191848) | Phase 4 | Recruiting | 352 | Randomized, double-blind, placebo-controlled trial (STOP KNEE-OA) evaluating whether once-weekly subcutaneous tirzepatide reduces need for knee replacement in patients with obesity and knee osteoarthritis over 72 weeks |
| [NCT05912621](https://clinicaltrials.gov/study/NCT05912621) | Phase 2 | Recruiting | 66 | Investigates tirzepatide's effect on lipotoxicity and adipose tissue dysfunction in overweight/obesity; osteoarthritis referenced as an obesity-related comorbidity, not primary endpoint |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41039116](https://pubmed.ncbi.nlm.nih.gov/41039116/) | 2025 | Systematic Review/Meta-analysis | Nature Medicine | Network meta-analysis of obesity pharmacotherapy efficacy and safety, including impact on obesity-related complications |
| [39129529](https://pubmed.ncbi.nlm.nih.gov/39129529/) | 2024 | Review | Expert Opinion on Pharmacotherapy | Reviews impact of approved anti-obesity medications specifically on osteoarthritis risk and outcomes |
| [40953447](https://pubmed.ncbi.nlm.nih.gov/40953447/) | 2025 | Cost-effectiveness modeling | Annals of Internal Medicine | Models cost-effectiveness of semaglutide and tirzepatide for knee OA patients with obesity, noting substantial weight loss and pain reduction with GLP-1RAs |
| [40512029](https://pubmed.ncbi.nlm.nih.gov/40512029/) | 2025 | Cost-effectiveness modeling | Obesity (Silver Spring) | Models cost-effectiveness of tirzepatide vs. lifestyle modification for overweight/obesity management |
| [39743126](https://pubmed.ncbi.nlm.nih.gov/39743126/) | 2025 | Review | Progress in Cardiovascular Diseases | Reviews tirzepatide/semaglutide effects on obesity-related diseases via central reward pathway modulation |
| [40100584](https://pubmed.ncbi.nlm.nih.gov/40100584/) | 2025 | Review | Current Psychiatry Reports | Discusses sex differences in obesity treatment outcomes, including knee osteoarthritis, with semaglutide/tirzepatide |
| [41754149](https://pubmed.ncbi.nlm.nih.gov/41754149/) | 2026 | Narrative Review | Nutrients | Reviews GLP-1RA use for obesity in older women, noting association with osteoarthritis risk reduction |
| [41782434](https://pubmed.ncbi.nlm.nih.gov/41782434/) | 2026 | Guidance Statement | Obesity (Silver Spring) | Joint TOS/OMA/OAC GRADE-based guidance on pharmacological management of overweight/obesity in US adults |
| [40604322](https://pubmed.ncbi.nlm.nih.gov/40604322/) | 2024 | Review | npj Metabolic Health and Disease | Reviews incretin-based therapies for obesity-related diseases including osteoarthritis |
| [41212412](https://pubmed.ncbi.nlm.nih.gov/41212412/) | 2025 | Review | Journal of Endocrinological Investigation | Phenotype-guided precision framework for obesity pharmacotherapy across the lifespan |

*Note: A related gout signal (rank #1, score 96.75%) is supported by a single post-hoc analysis: [41198460](https://pubmed.ncbi.nlm.nih.gov/41198460/) (2026, Annals of the Rheumatic Diseases) — SURMOUNT-1 post-hoc analysis linking tirzepatide-associated weight loss to reduced serum uric acid.*

---

## Singapore Market Information

No registrations found. Tirzepatide is currently not marketed under this evidence pack's Singapore regulatory dataset (0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available — see Data Gap DG001, classified as Blocking.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the osteoarthritis signal has genuine mechanistic plausibility and an ongoing Phase 4 outcome trial (NCT06191848), no trial has yet reported efficacy results, and a critical safety data gap (TFDA/HSA label warnings and contraindications) is classified as **Blocking** — this alone prevents progression past initial safety screening (S1) regardless of efficacy evidence strength.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: obtain official product label warnings/contraindications (source: regulatory agency label, PDF parsing)
- Resolve High-priority data gap DG002: confirm original approved indication(s) and mechanism of action via DrugBank API
- Await interim/final results from NCT06191848 (completion not expected until 2037; consider interim readouts)
- If Singapore market entry is planned, confirm regulatory filing status and route availability (currently 0 registrations, route compatibility unassessed)
- Track the gout signal separately as an S1 research question — currently insufficient for action (single post-hoc analysis only, no dedicated trials)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

