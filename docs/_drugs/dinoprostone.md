---
layout: default
title: Dinoprostone
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
---

# Dinoprostone
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

# Dinoprostone: From Obstetric Use to Esotropia

## One-Sentence Summary

Dinoprostone is the pharmaceutical form of prostaglandin E2 (PGE2), a naturally occurring lipid mediator widely used in obstetrics for cervical ripening, labor induction, and management of pregnancy complications.
The TxGNN model assigns it a high score of **98.26%** for **Esotropia** (convergent strabismus), yet **no clinical trials and no supporting literature** exist for this indication, and the mechanistic rationale is not biologically plausible.
This prediction is assessed as an **L5 model-only signal** and warrants no further development at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Obstetric use (cervical ripening, labor induction) — no Singapore HSA registration on record |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 98.26% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Dinoprostone is the synthetic equivalent of endogenous prostaglandin E2 (PGE2), acting through four G-protein–coupled receptors (EP1–EP4) that are distributed across smooth muscle, vascular endothelium, immune cells, and the reproductive tract. Through EP3 receptor activation, PGE2 promotes uterine contractility; through EP2/EP4, it induces cervical softening and smooth muscle relaxation. These mechanisms underpin its established obstetric use.

Esotropia is a form of strabismus in which one or both eyes deviate inward due to imbalance in extraocular muscle tone, neuromuscular signalling, or central oculomotor control. The EP1–EP4 receptors have no documented expression in the extraocular muscles or oculomotor nuclei that would mediate convergence control. No preclinical study, case report, or mechanistic study has proposed a link between PGE2 signalling and the pathophysiology of esotropia.

The high TxGNN score most likely reflects distant, multi-hop connections in the knowledge graph — for instance, shared inflammatory pathway nodes — rather than a direct pharmacological relationship. This is a recognised limitation of graph-based repurposing models when the predicted indication sits far from the drug's biological neighbourhood. In the absence of any supporting evidence or plausible mechanism, this prediction should not be advanced.

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
Dinoprostone has no biological mechanism connecting PGE2/EP receptor signalling to extraocular muscle control or strabismus, and the L5 evidence level (model prediction only) provides no clinical or preclinical support for this repurposing hypothesis. The high TxGNN score is most likely a knowledge-graph artefact.

**To revise this decision, the following would be required:**

- Demonstration of EP receptor expression in extraocular muscles or oculomotor pathways (preclinical, molecular)
- At least one animal model study showing PGE2 influence on ocular alignment or muscle tone
- A coherent mechanistic hypothesis explaining how PGE2 agonism would correct, rather than exacerbate, strabismus
- Safety and route-of-administration assessment for any proposed ophthalmic or systemic formulation

---

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

