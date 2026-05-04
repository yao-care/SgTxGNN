---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 256
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Gefitinib (Iressa) is a first-generation EGFR tyrosine kinase inhibitor originally developed for the treatment of EGFR-mutant non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Gingival Fibromatosis**, with **no clinical trials** and **no publications** currently directly supporting this specific indication.
This prediction carries the lowest possible evidence level (L5) and the mechanistic rationale is considered weak given the disease's distinct pathophysiology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-Small Cell Lung Cancer (NSCLC) with activating EGFR mutations |
| Predicted New Indication | Gingival Fibromatosis (fibromatosis, gingival) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the Singapore regulatory database. Based on established pharmacological knowledge, Gefitinib is a selective inhibitor of the Epidermal Growth Factor Receptor (EGFR) tyrosine kinase domain. By blocking EGFR-mediated downstream signaling — including the RAS/MAPK and PI3K/AKT cascades — it suppresses tumour cell proliferation, promotes apoptosis, and inhibits angiogenesis and invasion. Its efficacy in EGFR-mutant NSCLC (particularly exon 19 deletions and exon 21 L858R substitutions) is well established.

Gingival fibromatosis is primarily caused by mutations in the SOS1, HRAS, or KRAS genes, or is drug-induced (e.g., by cyclosporine, phenytoin, or calcium channel blockers). While EGFR signaling plays a subsidiary role in fibroblast proliferation within connective tissue, it is not the primary driver of this condition. The high TxGNN score (0.9989) most likely reflects a non-specific association between EGFR and connective tissue signaling nodes in the knowledge graph, rather than a genuine therapeutic relationship.

No published literature or registered clinical trials currently support the use of Gefitinib in gingival fibromatosis, and there is no established mechanistic bridge between EGFR inhibition and the pathophysiology of this disease. This prediction should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Gefitinib is currently not registered in Singapore. No product authorisations are on record in the regulatory dataset (total registrations: 0).

---

## Cytotoxicity

Gefitinib is an antineoplastic agent (EGFR-targeted therapy). The following applies:

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — First-generation EGFR tyrosine kinase inhibitor (4-anilinoquinazoline class) |
| Myelosuppression Risk | Low (haematological toxicity is uncommon; not conventionally myelosuppressive like cytotoxic chemotherapy) |
| Emetogenicity Classification | Minimal to Low |
| Monitoring Items | Liver function tests (ALT/AST — hepatotoxicity risk), pulmonary function assessment (interstitial lung disease risk), ECG monitoring (QTc interval prolongation), dermatological assessment (acneiform eruption, paronychia, xerosis) |
| Handling Protection | Standard oral antineoplastic precautions apply — do not crush or split tablets; handle with care and follow institutional cytotoxic drug handling procedures |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score to gingival fibromatosis, but this prediction lacks mechanistic plausibility — the disease is primarily driven by SOS1/HRAS/KRAS mutations or drug-induced mechanisms unrelated to EGFR — and is unsupported by any clinical trial or published literature evidence.

**To proceed, the following is needed:**
- Preclinical investigation (in vitro fibroblast proliferation models) to assess whether EGFR activity is meaningfully elevated in gingival fibromatosis tissue
- Retrieval and review of the Gefitinib package insert (e.g., AstraZeneca Iressa SmPC) to document key warnings, contraindications, and drug interactions
- Drug–drug interaction screening via a validated clinical database (e.g., Lexi-Interact, Micromedex)
- Formal assessment of whether the TxGNN knowledge graph is capturing a specific biological relationship or a non-specific connective tissue node association
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

