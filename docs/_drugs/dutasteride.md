---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a dual 5α-reductase inhibitor (types 1 and 2), widely used off-label and approved internationally for benign prostatic hyperplasia (BPH) and androgenetic alopecia, though it holds **no Singapore marketing authorisation**.
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita** with a near-perfect model score (99.99%), yet **zero clinical trials and zero publications** currently support this specific direction.
Across all 10 TxGNN-ranked predictions, the model consistently clusters hair and connective tissue disorders — reflecting Dutasteride's known androgen–hair biology link — but mechanistic relevance varies substantially across specific disease subtypes.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign Prostatic Hyperplasia (BPH); Androgenetic Alopecia (international approvals; no Singapore registration found) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed (0 registrations) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack (Data Gap DG002). Based on established pharmacological knowledge, Dutasteride is a dual inhibitor of 5α-reductase isoenzymes type 1 and type 2, blocking the conversion of testosterone to dihydrotestosterone (DHT). This dual inhibition suppresses serum DHT by approximately 90–95% — a more complete reduction than Finasteride, which targets only type 2. Its clinical utility in conditions driven by androgen-dependent tissue responses (prostate enlargement, follicular miniaturisation in androgenetic alopecia) is well-established globally.

Ambras Syndrome (Ambras type hypertrichosis universalis congenita) is a rare congenital disorder caused by a chromosomal inversion at 8q23.3 affecting the TRPS1 gene, resulting in generalised, non-patterned excessive hair growth across the entire body. Critically, this condition is **androgen-independent**: the hair overgrowth is driven by a developmental genetic defect, not by elevated DHT or over-active 5α-reductase activity.

The extremely high TxGNN prediction score (99.99%, rank 102) most likely reflects knowledge-graph path connectivity along the route "hair disorder → DHT pathway → 5α-reductase inhibitor" rather than a true disease-specific mechanism. Since Ambras Syndrome does not involve androgen excess or signalling dysregulation, inhibiting 5α-reductase provides no direct therapeutic rationale for this genetically-defined condition. This prediction is assessed as a likely false positive arising from imprecise disease categorisation within the knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ambras Type Hypertrichosis Universalis Congenita and Dutasteride.

---

## Literature Evidence

Currently no related literature available for Ambras Type Hypertrichosis Universalis Congenita and Dutasteride.

---

## Singapore Market Information

Dutasteride is currently **not registered in Singapore**. No marketing authorisations have been identified in the regulatory database. Patients requiring Dutasteride-containing products would need to access them through special import or unregistered drug channels.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data (key warnings, contraindications) were not available in this Evidence Pack (Data Gap DG001 — package insert not retrieved). No drug–drug interaction records were identified in the DDI database query. Before any clinical use or trial planning, a full safety review against the international label (e.g., Avodart SmPC/USPI) is mandatory.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite an extremely high TxGNN model score (99.99%), the mechanistic basis for Dutasteride in Ambras Type Hypertrichosis Universalis Congenita is non-existent — the disease is caused by a TRPS1 chromosomal inversion unrelated to androgen signalling, and there is no supporting clinical trial or published literature evidence. This prediction is most likely a knowledge-graph artefact.

**To proceed, the following is needed:**

- Retrieve full safety data from the Dutasteride package insert (TFDA or international SmPC/USPI) to close Data Gap DG001 (Blocking severity)
- Retrieve complete MOA data from the DrugBank API to close Data Gap DG002 (High severity)
- Conduct a formal Singapore HSA regulatory pathway assessment before any local clinical use
- **Prioritise re-evaluation of Rank 8 (Diffuse Alopecia Areata / Female Androgenetic Alopecia, Evidence Level L4)**: the retrieved literature (PMID [41714473](https://pubmed.ncbi.nlm.nih.gov/41714473/), 2026 narrative review of AGA in women) provides indirect mechanistic support for Dutasteride's off-label use in female androgenetic alopecia — a clinically distinct and more mechanistically plausible target; if the disease classification is confirmed as androgenetic rather than autoimmune alopecia areata, the evidence level could be upgraded to L3–L2 and the recommendation revised to **Proceed with Guardrails**
- For Rank 2 (Hypertrichosis, general), clarify whether the target subtype is androgenic (Hirsutism) — if so, a limited mechanistic rationale exists and further literature search is warranted
- All remaining ranked predictions (Ranks 1, 3–7, 9–10) involve either genetic structural defects, developmental malformations, or neurological disorders with no plausible androgen-axis connection; these are recommended for **permanent Hold** unless new biological evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

