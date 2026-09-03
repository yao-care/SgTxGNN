---
layout: default
title: Rufinamide
parent: 僅模型預測 (L5)
nav_order: 878
evidence_level: L5
indication_count: 10
---

# Rufinamide
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

# Rufinamide: From Lennox-Gastaut Syndrome to Childhood-Onset Epileptic Encephalopathy

> **Note on indication selection**: This Evidence Pack contains 10 TxGNN-predicted indications for rufinamide. The top-ranked prediction by score (febrile infection-related epilepsy syndrome) has **zero supporting evidence** (L5/Hold), as do 6 of the other 9 candidates. Rank #8 — **childhood-onset epileptic encephalopathy** — is the only candidate with L1 evidence and an actionable recommendation (Proceed with Guardrails), so this report focuses on that indication.

## One-Sentence Summary

Rufinamide is a triazole-derivative sodium-channel blocker with an established regulatory history (FDA/EMA-approved) as adjunctive therapy for seizures in **Lennox-Gastaut syndrome (LGS)**, though this original indication is not recorded in the local registry data available here. The TxGNN model predicts efficacy in the broader category of **childhood-onset epileptic encephalopathy**, and since LGS is itself a prototypical childhood-onset epileptic encephalopathy, this is less a novel repurposing signal than a confirmation of an already-approved use-case extending to related encephalopathy phenotypes. Evidence support is strong: **20 publications**, including a Phase 3 trial dataset, a systematic review/meta-analysis, and an AAN/AES practice guideline; no clinical trials are separately indexed under this specific disease label.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in registry data (data gap); literature confirms adjunctive treatment of seizures in Lennox-Gastaut syndrome |
| Predicted New Indication | Childhood-onset epileptic encephalopathy |
| TxGNN Prediction Score | 97.71% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (data gap). Based on literature evidence, rufinamide is a structurally novel triazole derivative believed to prolong the inactive state of voltage-gated sodium channels, limiting sustained repetitive neuronal firing — a mechanism distinct from other marketed antiseizure medications (PMID 21351809, 17696794).

The predicted indication, "childhood-onset epileptic encephalopathy," is a broad disease category that **already includes Lennox-Gastaut syndrome**, rufinamide's real-world approved indication (FDA 2008, EMA 2007) for patients aged 4+ (US) or 1+ (real-world dosing data). In other words, this TxGNN prediction largely reflects a category-level restatement of known efficacy rather than a genuinely novel mechanistic hypothesis. The one piece of incremental value is PMID 20666837, a multicenter Italian cohort study specifically testing rufinamide in **refractory childhood epileptic encephalopathies other than LGS**, suggesting the drug's utility may extend beyond the LGS label into adjacent encephalopathy phenotypes — this is the genuinely "new" part of the signal worth further investigation.

Mechanistically, sodium-channel blockade is a broadly applicable strategy across epileptic encephalopathies with multifocal, drug-resistant seizure types, which supports biological plausibility for class-effect extrapolation, though most cited literature remains LGS-specific rather than encephalopathy-generic.

---

## Clinical Trial Evidence

Currently no related clinical trials registered under this specific indication label. (Note: PMID 28284045 references Phase 3 trial data and real-world dosing experience, but this is captured as a publication, not a separately registered trial record in this Evidence Pack.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28284045](https://pubmed.ncbi.nlm.nih.gov/28284045/) | 2017 | RCT | Seizure | Compares Phase 3 trial dosing/titration of rufinamide in LGS with real-world clinical practice data |
| [34273668](https://pubmed.ncbi.nlm.nih.gov/34273668/) | 2021 | Meta-analysis | Seizure | Systematic review and meta-analysis confirming efficacy/safety of adjunctive rufinamide in LGS |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guideline | Neurology | AAN/AES practice guideline update on efficacy/tolerability of newer AEDs in new-onset epilepsy |
| [39854828](https://pubmed.ncbi.nlm.nih.gov/39854828/) | 2025 | Review | Epilepsy & Behavior | Comprehensive review of 8 FDA-approved ASMs (incl. rufinamide) for LGS with proposed treatment algorithm |
| [39700524](https://pubmed.ncbi.nlm.nih.gov/39700524/) | 2025 | Review | Epilepsia Open | Updated management algorithms for LGS, a developmental and epileptic encephalopathy |
| [33479851](https://pubmed.ncbi.nlm.nih.gov/33479851/) | 2021 | Review | CNS Drugs | Reviews expanding treatment landscape for LGS, a childhood-onset developmental/epileptic encephalopathy |
| [32103957](https://pubmed.ncbi.nlm.nih.gov/32103957/) | 2020 | Review | Neuropsychiatric Dis Treat | Literature review of adjunctive rufinamide in children with LGS |
| [24929673](https://pubmed.ncbi.nlm.nih.gov/24929673/) | 2014 | Review | Eur J Paediatr Neurol | Expert panel review of rufinamide's role across childhood epilepsy syndromes (~600 pediatric patients) |
| [20666837](https://pubmed.ncbi.nlm.nih.gov/20666837/) | 2011 | Cohort | Eur J Neurol | First multicenter Italian experience of rufinamide in refractory childhood epileptic encephalopathies **other than LGS** — key incremental evidence |
| [37212330](https://pubmed.ncbi.nlm.nih.gov/37212330/) | 2023 | Review | Expert Opin Pharmacother | Reviews current/emerging pharmacotherapy for LGS, including rufinamide's place in therapy |

---

## Singapore Market Information

No marketing authorizations are on file for rufinamide in Singapore (market status: 未上市 / not marketed; 0 registrations). No dosage form or product-level data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as data gaps in this Evidence Pack; DDI query returned no results.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base is strong (L1) but is largely a restatement of rufinamide's existing LGS approval rather than a novel indication — genuine incremental value rests on a single cohort study (PMID 20666837) covering non-LGS pediatric encephalopathies. Combined with the drug being unregistered in Singapore and having blocking-level safety data gaps, guardrails are warranted before any clinical or regulatory action.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label warnings/contraindications from a regulatory source (e.g., FDA/EMA label, since no local TFDA/HSA record exists) before any S1 safety assessment
- Resolve DG002 (High): confirm detailed MOA via DrugBank API to support mechanistic-link analysis
- Clarify whether "childhood-onset epileptic encephalopathy" should be scoped to non-LGS phenotypes specifically, since LGS itself is already a known indication elsewhere
- If pursuing Singapore market entry, obtain a full HSA regulatory pathway assessment given zero current registrations
- Deprioritize (Hold) the remaining 8 lower-evidence predicted indications (ranks 1–6, 9, 10) unless new clinical/literature evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

