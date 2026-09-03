---
layout: default
title: Siltuximab
parent: 僅模型預測 (L5)
nav_order: 903
evidence_level: L5
indication_count: 10
---

# Siltuximab
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

# Siltuximab: From Idiopathic Multicentric Castleman Disease to TAFRO Syndrome

## One-Sentence Summary

Siltuximab is an anti-IL-6 chimeric monoclonal antibody internationally approved for idiopathic multicentric Castleman disease (iMCD), a rare IL-6–driven lymphoproliferative disorder.
The TxGNN model — supported by independent literature evidence — predicts it may also be effective for **TAFRO syndrome**, a severe iMCD subtype,
with **1 completed randomized controlled trial** (on the parent iMCD indication), **multiple treatment guidelines**, and **case reports specific to TAFRO** currently supporting this direction. No dedicated clinical trials for TAFRO itself have been registered yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (0 licenses); internationally approved for idiopathic multicentric Castleman disease (iMCD), per literature evidence in this pack |
| Predicted New Indication | TAFRO Syndrome |
| TxGNN Prediction Score | 98.79% |
| Evidence Level | L3 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank in this evidence pack (flagged as a High-severity data gap). However, the literature evidence consistently describes siltuximab as a chimeric human-murine anti-IL-6 (interleukin-6) monoclonal antibody that binds IL-6 with high affinity, preventing it from engaging its receptor and thereby blocking downstream IL-6-driven inflammatory signaling.

Siltuximab's established indication — idiopathic multicentric Castleman disease (iMCD) — is a lymphoproliferative disorder characterized by dysregulated, excessive IL-6 production causing systemic inflammation, lymphadenopathy, and cytokine-storm-like symptoms. TAFRO syndrome (Thrombocytopenia, Anasarca, Fever, Reticulin fibrosis/Renal insufficiency, Organomegaly) is now widely recognized in the hematology literature as a rare, aggressive clinical subtype/variant within the iMCD spectrum, sharing the same underlying IL-6 hyperactivation pathophysiology.

Because TAFRO syndrome and siltuximab's approved indication (iMCD) sit on the same disease spectrum with a shared IL-6-driven mechanism, extending siltuximab's use to TAFRO is mechanistically well-supported — several published guidelines and case reports already describe "empiric anti-IL-6 therapy" in TAFRO patients, even though no dedicated randomized trial for TAFRO specifically has yet been completed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for TAFRO syndrome specifically.

*(Note: one Siltuximab trial exists in the dataset — NCT02796859, a Phase 1/2 study of adjunctive siltuximab in schizophrenia — but this is unrelated to TAFRO syndrome and was excluded as an evidence-mismatch.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25042199](https://pubmed.ncbi.nlm.nih.gov/25042199/) | 2014 | RCT | The Lancet. Oncology | Randomized, double-blind, placebo-controlled trial establishing safety and efficacy of siltuximab in HIV-negative multicentric Castleman's disease — the pivotal trial underlying regulatory approval |
| [30181172](https://pubmed.ncbi.nlm.nih.gov/30181172/) | 2018 | Review/Guideline | Blood | International, evidence-based consensus treatment guidelines for idiopathic multicentric Castleman disease, positioning anti-IL-6 therapy as first-line |
| [38927484](https://pubmed.ncbi.nlm.nih.gov/38927484/) | 2024 | Review/Guideline | Biomedicines | Management guidance specifically for TAFRO syndrome, discussing anti-IL-6 (siltuximab) as a treatment option within the iMCD spectrum |
| [38087716](https://pubmed.ncbi.nlm.nih.gov/38087716/) | 2024 | Review | Blood Reviews | Update on iMCD diagnosis/treatment advances, citing siltuximab as the approved anti-IL-6 antibody |
| [36219975](https://pubmed.ncbi.nlm.nih.gov/36219975/) | 2022 | Review | Oncology Research and Treatment | Recent advances in Castleman disease; MCD symptomatology driven by IL-6 overproduction/dysregulation |
| [36652167](https://pubmed.ncbi.nlm.nih.gov/36652167/) | 2023 | Case Report/Review | Journal of Nephrology | Siltuximab monotherapy used successfully in a TAFRO syndrome patient with renal involvement — direct clinical precedent |
| [32564425](https://pubmed.ncbi.nlm.nih.gov/32564425/) | 2020 | Case Report | European Journal of Haematology | Frontline siltuximab plus rituximab used in TAFRO syndrome |
| [28140696](https://pubmed.ncbi.nlm.nih.gov/28140696/) | 2017 | Review | Expert Opinion on Investigational Drugs | Reviews siltuximab's role in IL-6-driven hematologic malignancies beyond MCD |
| [25986720](https://pubmed.ncbi.nlm.nih.gov/25986720/) | 2015 | Review | Current Oncology Reports | Clinical development history of siltuximab across multiple IL-6-driven disease states |
| [24958337](https://pubmed.ncbi.nlm.nih.gov/24958337/) | 2014 | Review | Drugs | Siltuximab first global approval summary, confirming approved use in MCD and IL-6 mechanism |

---

## Singapore Market Information

Siltuximab is **not currently registered in Singapore** (0 authorizations, market status: 未上市/Not Marketed). No local product listing, dosage form, or approved indication text is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong — TAFRO syndrome is increasingly recognized as an IL-6-driven subtype within the same disease spectrum as siltuximab's approved indication (iMCD), and this is supported by a pivotal RCT (on iMCD), consensus guidelines, and TAFRO-specific case reports describing successful siltuximab use. However, no dedicated RCT for TAFRO itself exists yet, and the drug is not currently registered in Singapore.

**To proceed, the following is needed:**
- Official DrugBank/manufacturer MOA documentation (currently a Blocking/High-severity data gap)
- HSA package insert warnings, contraindications, and DDI data (Blocking gap — required before any S1 safety evaluation)
- Singapore market registration or named-patient/special access pathway assessment, given current "not marketed" status
- Prospective or larger-cohort clinical data specific to TAFRO syndrome, beyond existing case reports
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

