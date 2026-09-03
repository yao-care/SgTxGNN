---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 748
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidone: From Schizophrenia to Treatment-Refractory Schizophrenia

## One-Sentence Summary

Paliperidone is an atypical (second-generation) antipsychotic in the risperidone class, with schizophrenia as its established core indication. The TxGNN model, combined with real evidence retrieval, points to a meaningful signal in **treatment-refractory schizophrenia**, supported by **4 clinical trials** and **2 publications**. Note: TxGNN's single highest-scoring prediction (retinal dystrophy with extraocular anomalies) is excluded from this report — see caveat below.

> **Caveat on prediction selection:** TxGNN's top-ranked candidate by raw score was "retinal dystrophy with or without extraocular anomalies" (score 99.92%). The evidence pack's own rationale flags this as a likely knowledge-graph embedding artifact — the 15 retrieved PubMed records are all descriptive ophthalmology literature on congenital eye disorders with no mention of Paliperidone or any drug intervention. Ranks 2–9 (X-linked myopia, hydranencephaly, Charcot-Marie-Tooth, etc.) show the same pattern: no clinical trials, no literature, no plausible mechanistic link. This report instead focuses on rank 10 — **treatment-refractory schizophrenia** — the only candidate with real trial and literature support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (known antipsychotic class; not separately confirmed by local label text — see below) |
| Predicted New Indication | Treatment-Refractory Schizophrenia |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this evidence pack. Based on the repurposing rationale accompanying the top evidence-backed candidate, Paliperidone is 9-hydroxy-risperidone, the active metabolite of risperidone, and acts as a dopamine D2 receptor and serotonin 5-HT2A receptor antagonist — the standard pharmacology of a non-typical antipsychotic.

Schizophrenia is Paliperidone's already-established core indication, so the mechanistic link to this disease family is not in question. What TxGNN is actually flagging here is a **sub-population signal**: efficacy specifically in the treatment-refractory subgroup, rather than a novel drug-disease pairing. This is a narrower and more plausible claim than the other nine predictions in this pack, which pair Paliperidone with unrelated congenital/genetic disorders with no supporting mechanism.

The clinical evidence found is consistent with this framing — most retrieved trials study Paliperidone or comparator antipsychotics in schizophrenia broadly, with only partial focus on the treatment-resistant subgroup specifically. This means the prediction is biologically credible but the evidence base addresses the general indication more than the "refractory" qualifier.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01860781](https://clinicaltrials.gov/study/NCT01860781) | Phase 4 | Completed | 30 | Prospective naturalistic case series directly evaluating Paliperidone Palmitate effectiveness in schizophrenia across three patient groups; not specific to treatment-refractory subgroup |
| [NCT06060886](https://clinicaltrials.gov/study/NCT06060886) | Phase 4 | Unknown | 244 | Open-label RCT (SchizOMICS) comparing Aripiprazole vs Paliperidone/Risperidone using multi-omics data in first-episode psychosis; same indication family but not refractory-specific, status unknown |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Recruiting | 40 | Evaluates pharmacotherapy combined with new recovery-oriented programs for treatment-resistant schizophrenia and treatment-resistant bipolar disorder; drug-specific link to Paliperidone unclear |
| [NCT05741502](https://clinicaltrials.gov/study/NCT05741502) | Phase 4 | Terminated | 5 | Compared Clozapine vs non-Clozapine antipsychotics for inflammatory markers in treatment-resistant schizophrenia; terminated early, not Paliperidone-specific, background evidence only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31648341](https://pubmed.ncbi.nlm.nih.gov/31648341/) | 2019 | Review | Actas Españolas de Psiquiatría | Reviews psychopharmacology evidence for schizoaffective disorder, noting the lack of disorder-specific treatment guidelines and reliance on antipsychotics generally |
| [23364281](https://pubmed.ncbi.nlm.nih.gov/23364281/) | 2013 | Review | Current Opinion in Psychiatry | Reviews psychopharmacological approaches for early-onset schizophrenia spectrum disorders in adolescents, including dosing and switching strategies |

---

## Singapore Market Information

Currently no registration or license information is available — Paliperidone is not marketed in Singapore per this evidence pack (0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information. (No drug interaction, warning, or contraindication data was retrievable in this evidence pack.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Paliperidone's mechanistic link to schizophrenia is well established, and one completed Phase 4 naturalistic study directly supports its effectiveness in the broader schizophrenia population. However, evidence specifically targeting the treatment-refractory subgroup is indirect (comparator trials, small/terminated samples, or unknown-status trials), so this should proceed only with additional guardrails rather than a full "Go."

**To proceed, the following is needed:**
- Confirmed mechanism-of-action documentation (currently a data gap)
- TFDA/HSA label warnings and contraindications (currently a data gap, marked Blocking severity in this evidence pack)
- Drug-drug interaction data (current query returned "not_found")
- A trial or study population specifically defined as treatment-refractory/treatment-resistant schizophrenia with Paliperidone as the primary intervention
- Confirmation of Singapore market/registration pathway status, since the drug currently has zero local licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

