---
layout: default
title: Brexpiprazole
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 10
---

# Brexpiprazole
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

# Brexpiprazole: From Major Depressive Disorder to Dysthymic Disorder

## One-Sentence Summary

Brexpiprazole (Rexulti) is an atypical antipsychotic approved by the FDA for schizophrenia and as adjunctive therapy for major depressive disorder (MDD).
The TxGNN model predicts it may be effective for **Dysthymic Disorder** (Persistent Depressive Disorder),
with **no clinical trials** and **no publications** currently directly supporting this specific direction — placing it at evidence level **L4** (mechanistic prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia; Major Depressive Disorder (adjunctive therapy) |
| Predicted New Indication | Dysthymic Disorder |
| TxGNN Prediction Score | 98.53% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. However, based on published literature included elsewhere in this candidate's analysis, brexpiprazole functions as a **serotonin-dopamine activity modulator (SDAM)**: it acts as a partial agonist at dopamine D2 and serotonin 5-HT1A receptors, and as an antagonist at serotonin 5-HT2A and adrenergic α1B receptors. Compared to aripiprazole (the prior generation D2 partial agonist), brexpiprazole has lower intrinsic activity at D2 and higher potency at 5-HT1A and 5-HT2A, which is associated with a more favourable tolerability profile — notably less akathisia and extrapyramidal side effects.

Dysthymic Disorder — now classified as **Persistent Depressive Disorder (PDD)** in DSM-5 — is a chronic, low-grade depression lasting at least two years. It shares the same core dopaminergic and serotonergic dysregulation pathways as MDD, meaning the receptors that brexpiprazole modulates in MDD are directly implicated in dysthymia's pathophysiology. Some patients experience "double depression" (dysthymia with superimposed MDD episodes), further blurring the diagnostic boundary. The TxGNN knowledge graph likely captures this mechanistic and nosological proximity, yielding a high prediction score.

However, non-typical antipsychotics have rarely been studied specifically in dysthymia. Clinical trials for MDD typically exclude patients with only dysthymia, meaning the substantial Phase 3 evidence for brexpiprazole in MDD cannot be directly transferred. This prediction represents a mechanistically plausible hypothesis that warrants exploratory investigation, not an immediately actionable clinical application.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for brexpiprazole in dysthymic disorder.

---

## Literature Evidence

Currently no related literature directly addressing brexpiprazole in dysthymic disorder is available.

> **Context note:** While no direct evidence exists for dysthymic disorder specifically, this evidence pack contains 20 publications supporting brexpiprazole in the closely related category of "neurotic depression" (rank 5 indication), including a Phase 3 RCT (PMID 26301701) and multiple systematic reviews/meta-analyses. The mechanistic overlap between dysthymia and these studied depressive conditions is substantial.

---

## Singapore Market Information

Brexpiprazole is currently **not registered** with the Health Sciences Authority (HSA) in Singapore. No product authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While brexpiprazole's serotonin-dopamine modulation mechanism is theoretically applicable to dysthymia's pathophysiology, the complete absence of direct clinical trial data or targeted publications for this indication means the prediction remains a research hypothesis. Regulatory, safety, and clinical practice frameworks for using an atypical antipsychotic in a chronic low-grade depression context have not been established.

**To proceed, the following is needed:**
- Full mechanism of action profile from DrugBank (currently unavailable)
- Package insert safety data including warnings, contraindications, and drug interactions from the HSA or originating regulatory agency
- Pilot or exploratory clinical trial design specifically targeting dysthymia / Persistent Depressive Disorder
- Assessment of whether existing MDD Phase 3 trial data (e.g., PMID 26301701) can support regulatory extrapolation under HSA's Drug Repurposing Framework
- Singapore market entry strategy, given zero current registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

