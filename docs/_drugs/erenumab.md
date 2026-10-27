---
layout: default
title: Erenumab
parent: Medium Evidence (L3-L4)
nav_order: 392
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Erenumab: predicted new indication Migraine with brainstem aura (evidence level L3). Approved use: Migraine disorder (migraine prevention). The Singapore licence record…"
monitor_inn: "Erenumab"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis", "amenorrhea (disease)", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis", "heparin cofactor 2 deficiency", "thrombophilia", "sciatic neuropathy", "severe nonproliferative diabetic retinopathy"]
---

# Erenumab
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Erenumab: From Migraine to Migraine with Brainstem Aura
{: .text-alpha }

## One-Sentence Summary

Erenumab is a monoclonal antibody against the CGRP receptor, originally used to prevent migraine.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, a migraine subtype with aura.
Support is indirect: **no registered clinical trials** and **20 publications** were compiled, mostly covering migraine with and without aura in general, and none specific to the brainstem aura subtype.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine disorder (migraine prevention). The Singapore licence records contain no indication text, so this comes from the knowledge graph. |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Based on known information, erenumab is a human monoclonal antibody that blocks the CGRP receptor. In cell-based assays it abolishes CGRP-stimulated cAMP production (IC50 about 2.3 nM) and is about 5000-fold selective for the CGRP receptor over other human calcitonin-family receptors. CGRP signalling is central to migraine pathophysiology, and erenumab is already used for migraine prevention.

Brainstem aura is a migraine subtype with aura, so it sits very close to the original indication. Secondary analyses of erenumab randomised trials in patients with and without aura (JAMA Neurology, 2022) suggest that erenumab is effective and safe in people with aura. A 2026 REFORM study also examined how erenumab affects aura frequency.

An important limit: no data specific to brainstem aura were identified. The link rests on extending the evidence from migraine with aura to this subtype, not on direct proof.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

The most relevant publications compiled for this report are listed below. The first six relate to aura or to systematic evidence; the last four are supportive migraine studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34928306](https://pubmed.ncbi.nlm.nih.gov/34928306/) | 2022 | Post-hoc analysis of RCTs | JAMA Neurology | Safety and efficacy of erenumab in patients with migraine with and without aura, given the higher vascular risk in the aura group |
| [36942409](https://pubmed.ncbi.nlm.nih.gov/36942409/) | 2023 | Pooled post-hoc analysis | Headache | Vascular risk in patients with and without aura treated with erenumab, using pooled long-term trial data |
| [41888647](https://pubmed.ncbi.nlm.nih.gov/41888647/) | 2026 | Clinical study (REFORM) | J Headache Pain | Changes in migraine aura frequency during and after erenumab treatment in adults with frequent aura |
| [37012858](https://pubmed.ncbi.nlm.nih.gov/37012858/) | 2023 | Systematic review | Int Immunopharmacol | Efficacy of erenumab in preventing episodic and chronic migraine |
| [32867533](https://pubmed.ncbi.nlm.nih.gov/32867533/) | 2021 | Mechanistic clinical study | Cephalalgia | Erenumab did not alter cerebral hemodynamics or endothelial function in migraine without aura |
| [35230406](https://pubmed.ncbi.nlm.nih.gov/35230406/) | 2022 | News/commentary | JAMA | Commentary: erenumab safe and effective in migraine with aura |
| [30360965](https://pubmed.ncbi.nlm.nih.gov/30360965/) | 2018 | Phase 3b RCT | Lancet | Efficacy and tolerability in episodic migraine after 2–4 failed preventive treatments |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handb Exp Pharmacol | Role of CGRP in migraine pathophysiology |
| [35538414](https://pubmed.ncbi.nlm.nih.gov/35538414/) | 2022 | Retrospective real-world study | J Headache Pain | 12-month safety and tolerability of erenumab in practice |
| [35151970](https://pubmed.ncbi.nlm.nih.gov/35151970/) | 2022 | Real-world study | Clin Neurol Neurosurg | Effectiveness and safety in treatment-resistant chronic migraine |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15925P | AIMOVIG Solution for Injection in Pre-filled Pen 140 mg/ml | Injection, solution | Not stated in the records |
| SIN15543P | AIMOVIG Solution for Injection in Pre-filled Pen 70 mg/ml | Injection, solution | Not stated in the records |
| SIN15926P | AIMOVIG Solution for Injection in Pre-filled Syringe 140 mg/ml | Injection, solution | Not stated in the records |
| SIN15545P | AIMOVIG Solution for Injection in Pre-filled Syringe 70 mg/ml | Injection, solution | Not stated in the records |

## Safety Considerations

- **Drug Interactions**: The interaction query found no drug–drug interactions; the only entry is the drug's own pharmacological target, the CGRP receptor.
- **Vascular safety**: CGRP is a vasodilator. Patients with aura have elevated vascular risk, and post-hoc analyses of erenumab trial data (JAMA Neurology 2022; Headache 2023) specifically examined this. Vascular risk should be monitored in any aura population.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Brainstem aura is a close subtype of the approved migraine indication. Existing systematic review and post-hoc trial evidence supports erenumab in migraine with aura, and the TxGNN score is high. However, there is no subtype-specific trial or study, so this remains an extension by subtype and should be treated as a research question rather than a ready indication.

**To proceed, the following is needed:**
- Data on patients with brainstem aura specifically (subgroup analysis, case series or a dedicated trial)
- Package insert warnings and contraindications from the Singapore regulator (HSA), plus the approved indication text for the four licences
- Detailed mechanism-of-action data from DrugBank
- A vascular safety monitoring plan for patients with aura
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

