---
layout: default
title: Trihexyphenidyl
parent: 僅模型預測 (L5)
nav_order: 1016
evidence_level: L5
indication_count: 10
---

# Trihexyphenidyl
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

# Trihexyphenidyl: From Parkinsonism (Anticholinergic Therapy) to Attention-Deficit/Hyperactivity Disorder (ADHD)

## One-Sentence Summary

> Trihexyphenidyl is a classic anticholinergic drug traditionally associated with Parkinson's disease and drug-induced extrapyramidal symptoms (specific Singapore-approved indication text is not available in this evidence pack).
> The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
> but this is currently supported by **0 clinical trials** and only **1 tangentially related publication**, and the mechanistic rationale actually points in the opposite direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not currently registered in Singapore (no license records) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacology, Trihexyphenidyl is a **centrally acting anticholinergic (antimuscarinic) agent**, a drug class typically used to manage Parkinsonian tremor/rigidity and drug-induced extrapyramidal symptoms by blocking excess cholinergic activity in the basal ganglia.

There is no established pharmacological rationale linking this mechanism to ADHD. The single retrieved publication (a case series on tic disorder with dystonia) does not discuss ADHD or attention-related outcomes at all — it appears to be a knowledge-graph co-occurrence artifact rather than genuine supporting evidence.

More importantly, the mechanistic direction is **contradictory**: anticholinergic drugs are well known to be associated with anticholinergic burden and cognitive impairment (including attention and memory deficits) in clinical practice, which is the opposite of what would be expected for a drug intended to improve inattention. This prediction should be treated as a pure model-score artifact rather than a biologically plausible hypothesis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Case series | Movement Disorders | Describes a clinical series of primary tic disorder co-occurring with dystonia; does **not** address ADHD or attention outcomes, and does not evaluate Trihexyphenidyl treatment effect on ADHD symptoms |

---

## Singapore Market Information

This drug currently has **no registration records in Singapore** (market status: Not Marketed, 0 licenses). No approved indication text is available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/HSA label warnings and contraindications for this drug are currently a data gap flagged as Blocking severity — this must be resolved before any safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (ADHD) has no supporting clinical trials, only one irrelevant publication, and a mechanistic rationale that actively contradicts the hypothesis (anticholinergic burden is linked to cognitive/attention impairment, not improvement). This is an L5, model-score-only signal with no biological plausibility demonstrated.

**To proceed, the following is needed:**
- Resolve the Blocking data gap: obtain official label warnings/contraindications (source: regulatory agency label PDF)
- Resolve the High-severity data gap: confirm mechanism of action via DrugBank API to properly assess mechanistic linkage
- If pursuing repurposing research for this drug at all, note that **PLA2G6-associated neurodegeneration** (rank 5 in this evidence pack) shows a substantially more coherent mechanistic rationale (dystonia-parkinsonism phenotype matching known anticholinergic use in movement disorders, L4 evidence, staged as "Research Question") and may warrant separate evaluation instead of the ADHD hypothesis
- Do not advance the ADHD indication further without new experimental or clinical evidence directly linking anticholinergic mechanism to attention improvement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

