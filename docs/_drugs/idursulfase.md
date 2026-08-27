---
layout: default
title: Idursulfase
parent: 僅模型預測 (L5)
nav_order: 514
evidence_level: L5
indication_count: 10
---

# Idursulfase
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

# Idursulfase: From Hunter Syndrome (MPS II) to Ptosis-Strabismus-Ectopic Pupils Syndrome

## One-Sentence Summary

Idursulfase (brand name: Elaprase) is a recombinant enzyme replacement therapy originally developed for Hunter syndrome (Mucopolysaccharidosis Type II, MPS II), a rare X-linked lysosomal storage disorder caused by deficiency of iduronate-2-sulfatase (I2S).
The TxGNN model predicts it may be effective for **Ptosis-Strabismus-Ectopic Pupils Syndrome**, a rare congenital structural eye condition.
However, **no clinical trials or published literature** currently support this direction, and mechanistic analysis strongly suggests this prediction is a knowledge graph topology artefact rather than a genuine therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hunter Syndrome (Mucopolysaccharidosis Type II, MPS II) |
| Predicted New Indication | Ptosis-Strabismus-Ectopic Pupils Syndrome |
| TxGNN Prediction Score | 97.89% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Idursulfase (Elaprase) is a recombinant human iduronate-2-sulfatase (I2S), the lysosomal enzyme deficient in Hunter syndrome (MPS II). In MPS II, absence of I2S leads to progressive accumulation of glycosaminoglycans (GAGs) — specifically heparan sulfate and dermatan sulfate — within lysosomes throughout the body. This causes multi-organ damage including skeletal deformities, cardiopulmonary disease, hepatosplenomegaly, and, in severe cases, neurological deterioration. Weekly intravenous infusions of Idursulfase partially restore I2S activity, slowing GAG accumulation.

Ptosis-strabismus-ectopic pupils syndrome is a rare congenital structural eye disorder characterised by drooping eyelids (ptosis), misalignment of the eyes (strabismus), and abnormal positioning of the pupils. Its pathogenesis lies in embryonic developmental anomalies or neuromuscular deficits occurring during organogenesis — a fundamentally different disease category from lysosomal storage disorders.

**The mechanistic link between Idursulfase and this syndrome is not biologically plausible.** While MPS II can cause certain ocular manifestations (e.g., corneal clouding, papilloedema) via GAG deposition in ocular tissues, these are categorically different from the structural congenital malformations that define ptosis-strabismus-ectopic pupils syndrome. The TxGNN analysis itself flags this as a likely non-specific topological correlation — the high prediction score (97.89%) is attributed to clustering of "ocular disease" nodes in the knowledge graph rather than shared molecular aetiology. Enzyme replacement targeting I2S has no known mechanism to reverse congenital developmental malformations of the eyelid, extraocular muscles, or pupillary apparatus.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is classified at Evidence Level L5 — model output only, with zero supporting clinical trials or published literature. Mechanistic review confirms the prediction lacks biological plausibility: ptosis-strabismus-ectopic pupils syndrome is a congenital structural disorder with no established relationship to lysosomal GAG accumulation or I2S deficiency, and the high TxGNN score is consistent with a knowledge graph topology artefact driven by co-clustering of ocular disease nodes.

**To proceed, the following is needed:**
- Retrieve complete MOA data from DrugBank API (DG002: currently blocking mechanistic analysis)
- Obtain Singapore HSA package insert to assess safety profile and contraindications (DG001: currently blocking S1 safety evaluation)
- Conduct a formal biological plausibility triage across all 10 predicted indications; rank 10 (Scheie syndrome) warrants a separate assessment note as it involves a related lysosomal storage disorder, despite the key enzymatic target mismatch
- Do not advance this specific indication (ptosis-strabismus-ectopic pupils syndrome) to any further evaluation stage without independent mechanistic evidence linking I2S deficiency to congenital ocular structural development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

