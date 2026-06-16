---
layout: default
title: Glycerin
parent: 僅模型預測 (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
---

# Glycerin
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

# Glycerin: From Osmotic Agent to Cauda Equina Syndrome

## One-Sentence Summary

Glycerin (glycerol) is a widely used osmotic agent and pharmaceutical excipient, historically applied to reduce intraocular pressure in acute glaucoma and as a rectal laxative; no formal therapeutic indication is registered in Singapore.
The TxGNN model predicts it may have potential for **Cauda Equina Syndrome**,
however **no clinical trials or publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal regulatory indication registered in Singapore (known uses: osmotic agent, laxative, pharmaceutical excipient) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known pharmacological properties, Glycerin (glycerol) is a small triol molecule that functions as an osmotic agent by creating an osmotic gradient across biological membranes. This property underlies its established clinical applications: oral or intravenous glycerol has been used to transiently reduce intraocular pressure (IOP) in acute angle-closure glaucoma attacks, and rectal glycerol suppositories exploit the same principle to stimulate bowel evacuation.

Cauda equina syndrome (CES) is a neurological emergency caused by acute or subacute compression of the lumbosacral nerve roots below the conus medullaris, typically by a large disc herniation or tumour. In theory, an osmotic agent capable of reducing perineural or intraspinal oedema could provide ancillary neuroprotection alongside definitive surgical decompression. This represents a mechanistically plausible but highly indirect rationale—analogous to how mannitol is occasionally used in acute spinal cord injury to reduce oedema—yet no clinical evidence exists to support this reasoning for CES specifically.

The TxGNN model's high prediction score (99.60%) most likely reflects the model's broader generalisation across neurological compression or pressure-related disorders rather than a specific, validated mechanistic link. Given the acute surgical nature of CES and the complete absence of preclinical or clinical data for Glycerin in this setting, the biological hypothesis remains speculative.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

No regulatory registrations for Glycerin were found in Singapore's Health Sciences Authority (HSA) database.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug–drug interaction data were identified in the current search. Package insert warnings and contraindications could not be retrieved and should be obtained directly from the TFDA official website by downloading and parsing the prescribing information PDF.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is currently no clinical trial evidence or peer-reviewed literature directly supporting Glycerin as a treatment for cauda equina syndrome. The condition is a neurosurgical emergency where timely decompression—not pharmacological osmotherapy—is the standard of care, and the proposed mechanistic link remains entirely speculative.

**To proceed, the following is needed:**
- Retrieve full MOA data from DrugBank (DB09462) to establish whether any secondary pharmacological targets are relevant to spinal nerve root compression
- Obtain package insert (PI) warnings and contraindications from official regulatory sources to complete the safety profile
- Commission a scoping review of osmotic agents (mannitol, glycerol) in acute spinal cord injury or cauda equina compression animal models to determine if a preclinical basis exists
- If preclinical data are identified, design a hypothesis-driven mechanistic study before any clinical translation is considered
- Clarify whether the high TxGNN rank reflects a true biological signal or a model artefact from proximity to other neurological pressure disorders in the knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

