---
layout: default
title: Penicillamine
parent: 僅模型預測 (L5)
nav_order: 766
evidence_level: L5
indication_count: 10
---

# Penicillamine
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

# Penicillamine: From Wilson's Disease/Cystinuria to Megaloblastic Anemia

## One-Sentence Summary

Penicillamine is classically known as a copper-chelating agent used for Wilson's disease and cystinuria (as referenced in this evidence pack's own mechanistic literature); no formal original-indication text is available in this evidence pack, as the drug is not marketed in Singapore. TxGNN's top-ranked prediction is **Megaloblastic Anemia** (score 98.02%), but this evidence pack currently identifies **no clinical trials, no literature, and no supporting mechanism** for this specific association — the model's own rationale flags it as mechanistically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (data gap — drug not marketed in Singapore); classically documented as a copper chelator for Wilson's disease/cystinuria |
| Predicted New Indication | Megaloblastic anemia (disease) |
| TxGNN Prediction Score | 98.02% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Penicillamine in this evidence pack (Data Gap DG002). Based on known information referenced elsewhere in this evidence pack, Penicillamine is a copper-chelating agent whose established efficacy is in Wilson's disease (via ATP7B copper-transport dysfunction) and cystinuria (via renal cystine transport abnormality) — not in hematologic disease.

There is no established pathophysiological link between copper/cystine metabolic disorders and megaloblastic anemia (a disorder of impaired DNA synthesis typically caused by vitamin B12 or folate deficiency). The evidence pack's own repurposing rationale for this candidate is explicit on this point: Penicillamine is known to induce **pyridoxine (vitamin B6) deficiency**, which is mechanistically more relevant to **sideroblastic anemia**, not megaloblastic anemia. No clinical or literature evidence supports the megaloblastic anemia association.

In short, this is TxGNN's highest-scoring prediction by embedding similarity, but the mechanism, clinical trial evidence, and literature evidence all fail to substantiate it — consistent with the model's own "Hold" recommendation and L5 (model-only) evidence level.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Penicillamine is currently **not marketed in Singapore** — 0 registrations/licenses on file. No product, dosage form, or approved-indication data is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is TxGNN's top-ranked disease association by prediction score, but it has zero clinical trials, zero literature support, and the evidence pack's own mechanistic analysis argues against it (B6 depletion → sideroblastic, not megaloblastic, anemia). Evidence Level L5 (model prediction only) does not meet the bar to advance.

**To proceed, the following is needed:**
- Preclinical or mechanistic studies directly linking penicillamine to megaloblastic anemia pathways (currently absent)
- Resolution of Blocking data gap DG001 (Singapore/TFDA-equivalent package insert warnings and contraindications)
- Resolution of High-severity data gap DG002 (detailed MOA)

**Note:** Within this same evidence pack, two other ranked candidates carry materially stronger evidence and may warrant separate evaluation — rank 3 ("disease of transporter activity," L1, includes an RCT) and rank 9 ("pyruvate metabolism disorder," L3). Both, however, appear to largely reflect Penicillamine's *already-known* indications (Wilson's disease, cystinuria/cystinosis) rather than genuinely novel repurposing signals, and would need ontology-mapping review before being treated as new candidates.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

