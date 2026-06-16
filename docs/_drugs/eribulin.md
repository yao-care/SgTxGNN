---
layout: default
title: Eribulin
parent: 僅模型預測 (L5)
nav_order: 391
evidence_level: L5
indication_count: 10
---

# Eribulin
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

# Eribulin: From Breast Cancer / Liposarcoma to Autosomal Recessive Familial Mediterranean Fever

## One-Sentence Summary

Eribulin (Halaven) is a synthetic halichondrin B analogue microtubule inhibitor, originally approved internationally for metastatic breast cancer and unresectable or metastatic liposarcoma.
The TxGNN model predicts it may be effective for **Autosomal Recessive Familial Mediterranean Fever (FMF)**,
however, this prediction is currently supported by **0 clinical trials** and **0 publications** — representing model-only evidence with no real-world validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic breast cancer; unresectable or metastatic liposarcoma (international approvals; not registered in Singapore) |
| Predicted New Indication | Autosomal Recessive Familial Mediterranean Fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacology, eribulin is a macrocyclic ketone analogue of halichondrin B that non-competitively suppresses microtubule polymerization — specifically targeting the plus-end of tubulin — causing G2/M cell cycle arrest and apoptosis. This binding site (halichondrin domain) is distinct from both taxanes (which stabilize polymerized microtubules) and vinca alkaloids (vinca domain). Beyond cytotoxicity, eribulin also demonstrates antivascular and epithelial-to-mesenchymal transition (EMT) reversal effects, which are thought to contribute to its efficacy in solid tumors.

Autosomal recessive FMF is a hereditary autoinflammatory disorder caused by MEFV gene mutations affecting pyrin protein function, leading to dysregulated inflammasome activation and recurrent fever attacks. Standard of care is colchicine — also a microtubule-targeting agent — which is believed to suppress neutrophil chemotaxis and IL-1β release. The TxGNN model likely identified this shared "microtubule-targeting" pharmacological feature as the mechanistic link between eribulin and colchicine's indication.

However, this analogy does not withstand clinical scrutiny. Colchicine's therapeutic action in FMF operates through anti-inflammatory modulation of neutrophil cytoskeleton function at very low concentrations, not cytotoxicity. Eribulin's cytotoxic mechanism requires concentrations that carry substantial myelosuppression and peripheral neurotoxicity risks — a toxicity profile entirely incompatible with chronic use in a non-proliferative autoinflammatory disease. Furthermore, eribulin binds to a completely different domain on tubulin than colchicine, suggesting the biological analogy used by the model is superficial. There is no preclinical, in vitro, or clinical evidence to support this prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Eribulin is a conventional cytotoxic antineoplastic agent approved for breast cancer and soft tissue sarcoma.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Halichondrin B analogue (non-taxane microtubule inhibitor) |
| Myelosuppression Risk | **High** — Neutropenia is the primary dose-limiting toxicity; febrile neutropenia and grade 3/4 neutropenia are commonly reported |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (especially ANC before each cycle), liver function tests, renal function, peripheral neuropathy assessment (NCI-CTCAE grading), QTc interval (risk of QT prolongation) |
| Handling Protection | Must follow cytotoxic drug handling regulations (closed-system transfer device recommended) |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Specific warnings and contraindications data were not available in this Evidence Pack. Known class-level concerns include QTc prolongation risk, embryo-fetal toxicity, and cumulative peripheral neuropathy, which are particularly relevant considerations when evaluating off-label use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high numerical score (99.82%) to this drug-disease pair, but the underlying biological rationale — a superficial analogy to colchicine's microtubule binding — does not support eribulin use in a hereditary autoinflammatory condition. The cytotoxic mechanism and toxicity burden of eribulin are fundamentally incompatible with the chronic, non-proliferative nature of FMF, and there is zero clinical or preclinical evidence to evaluate.

**To proceed, the following would be needed:**

- Credible in vitro mechanistic data demonstrating eribulin activity in MEFV-mutant or inflammasome-overactive cell models
- Comparative toxicity analysis versus colchicine to establish any therapeutic window in FMF
- Regulatory and ethics review for off-label cytotoxic use in a non-oncologic indication
- Clarification of the TxGNN model feature that drove this prediction, to assess whether it reflects genuine biological signal or a spurious pharmacophore association

---

> ⚠️ **Note on This Evidence Pack:** This is a multi-indication evaluation (candidate ID: TW-DB08871-multi) covering 10 predicted indications. Among these, **Fibroblastic Neoplasm (rank 8)** carries the strongest evidence — including a completed Phase 2 trial (ERASING, NCT03840772; eribulin in advanced Solitary Fibrous Tumor, n=16) and 8 supporting publications — warranting a separate **"Proceed with Guardrails"** report. The present report covers only the top-scored TxGNN prediction (rank 1, FMF), which is rated Hold on the basis of mechanistic implausibility and absence of any evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

