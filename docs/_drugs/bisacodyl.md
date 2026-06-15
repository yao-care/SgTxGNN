---
layout: default
title: Bisacodyl
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
---

# Bisacodyl
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

# Bisacodyl: From Constipation to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Bisacodyl is a well-established stimulant laxative used for the management of constipation and bowel preparation prior to colonoscopy or surgical procedures.
The TxGNN model predicts it may be effective for **Exercise-Induced Malignant Hyperthermia**, with a prediction score of **97.69%**;
however, **no clinical trials or published literature** currently support this direction, and the mechanistic rationale is considered biologically implausible.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Constipation; pre-procedure bowel preparation (standard pharmacological use; no Singapore HSA registration on file) |
| Predicted New Indication | Exercise-Induced Malignant Hyperthermia |
| TxGNN Prediction Score | 97.69% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not available for this report. Based on established pharmacological knowledge, Bisacodyl is a stimulant laxative that acts directly on the colonic mucosa. It inhibits water and electrolyte reabsorption, stimulates the myenteric plexus, and accelerates colonic transit — effects localised entirely to the gastrointestinal tract.

Exercise-induced malignant hyperthermia (MH) is a genetic disorder of skeletal muscle calcium regulation driven by loss-of-function or gain-of-function mutations in the **RYR1** or **CACNA1S** genes. During physical exertion or heat stress, these mutations cause uncontrolled calcium release from the sarcoplasmic reticulum, triggering a life-threatening hypermetabolic crisis characterised by rigidity, hyperthermia, and rhabdomyolysis.

There is no identifiable mechanistic bridge between Bisacodyl's colonic action and the calcium channelopathy underlying exercise-induced MH. The two pathologies involve entirely distinct anatomical locations, receptor systems, and signalling pathways. The elevated TxGNN score is most likely attributable to indirect graph noise around "hyperthermia"-related nodes in the knowledge graph, rather than any true pharmacological connection. This prediction is considered **biologically implausible** and is flagged as a model artefact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Bisacodyl is not currently registered with the Singapore Health Sciences Authority (HSA). No product authorisation records are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score (97.69%), this prediction lacks any mechanistic plausibility — Bisacodyl acts exclusively on the colonic mucosa while exercise-induced MH is a genetically-driven skeletal muscle calcium channelopathy — and is supported by zero clinical trials or published literature. The absence of Singapore market registration further removes any existing safety dataset to draw upon.

**To proceed, the following is needed:**
- Mechanism of action confirmation via DrugBank API to rule out any indirect pharmacological pathways not yet documented
- Preclinical data demonstrating any effect of Bisacodyl (or related stimulant laxatives) on RYR1/CACNA1S channel function or skeletal muscle calcium homeostasis
- Full Singapore package insert or equivalent (e.g., UK/EU SmPC, US label) for complete safety profile, contraindications, and drug interaction assessment
- Independent pharmacological expert review to formally assess biological plausibility before any further resource allocation
- Consideration of alternative drug candidates for exercise-induced MH with more mechanistically coherent TxGNN predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

