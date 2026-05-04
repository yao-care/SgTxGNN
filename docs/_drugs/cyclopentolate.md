---
layout: default
title: Cyclopentolate
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
---

# Cyclopentolate
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

# Cyclopentolate: From Ophthalmic Cycloplegia to Cauda Equina Syndrome

## One-Sentence Summary

Cyclopentolate is a well-established antimuscarinic cycloplegic/mydriatic agent used in ophthalmology for pupil dilation and ciliary muscle paralysis during eye examinations and anterior segment procedures.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, achieving the highest score among all predictions at **99.54%**.
However, this prediction is supported by **0 clinical trials** and **0 publications**, placing it at evidence level L5 with no empirical backing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ophthalmic cycloplegia/mydriasis (no Singapore regulatory registration on record) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from regulatory records. Based on known pharmacology, cyclopentolate is a competitive antagonist of muscarinic acetylcholine receptors — acting primarily at M3 receptors in the ciliary muscle and iris sphincter — producing cycloplegia and mydriasis when applied topically as an eye drop. As a broad anticholinergic agent, its receptor-blocking properties extend in principle to any smooth muscle or glandular tissue with muscarinic innervation, including bladder detrusor muscle and gastrointestinal smooth muscle. This class-level activity appears to be the basis for the TxGNN model's inference.

Cauda equina syndrome is a serious neurological emergency caused by acute compression of the lumbosacral nerve roots, characterised by saddle anesthesia, lower limb weakness, and neurogenic bladder/bowel dysfunction. Its core pathophysiology is mechanical nerve root injury — not muscarinic receptor overactivation. While anticholinergic drugs such as oxybutynin are used to manage neurogenic bladder (one downstream consequence of cauda equina injury), this represents symptomatic management of a sequela rather than any disease-modifying treatment for the syndrome itself.

The TxGNN model's high prediction score most likely reflects indirect knowledge graph paths linking cyclopentolate's anticholinergic drug class to the autonomic dysfunction component of cauda equina syndrome. However, biological plausibility for direct therapeutic application is poor: the ophthalmic dosage form provides negligible systemic drug exposure, and the underlying mechanism of cauda equina syndrome — mechanical nerve root compression — lies entirely outside cyclopentolate's pharmacological target. This prediction does not support clinical development at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Cyclopentolate is **not currently registered in Singapore** (HSA). No product authorizations are on record for any dosage form. Market entry would require a new regulatory submission to HSA before clinical use in Singapore can proceed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite achieving the highest TxGNN prediction score in this dataset (99.54%), the prediction for cauda equina syndrome has poor biological plausibility — cyclopentolate's anticholinergic mechanism does not address the mechanical nerve root compression that defines the condition — and there is zero supporting clinical or published evidence (L5). Proceeding with any development pathway cannot be justified under current evidence.

**To proceed, the following would be needed:**
- A credible mechanistic hypothesis connecting muscarinic receptor antagonism to cauda equina syndrome pathophysiology (beyond indirect KG graph paths)
- Preclinical evidence (animal models or mechanistic in vitro studies) demonstrating any therapeutic effect
- Formal MOA documentation from DrugBank to characterise receptor selectivity and systemic exposure potential
- Singapore HSA registration and full package insert review to establish a safety baseline
- Consideration of prioritising higher-evidenced TxGNN predictions from this same drug that represent more actionable repurposing opportunities, particularly: **Uveitis** (Rank 7, L3, Proceed with Guardrails — 20 publications including direct cyclopentolate studies), **Iris Disease** (Rank 8, L3, Proceed with Guardrails — 3 clinical trials, 20 publications), and **Ciliary Body Disease** (Rank 10, L3, Proceed with Guardrails — 1 completed clinical trial, 5 publications), all of which align directly with cyclopentolate's established ophthalmic pharmacology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

