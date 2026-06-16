---
layout: default
title: Caspofungin
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
---

# Caspofungin
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

# Caspofungin: From Invasive Candidiasis to Gastrin Secretion Abnormality

## One-Sentence Summary

Caspofungin is the first licensed echinocandin antifungal agent, used globally for invasive candidiasis, salvage treatment of invasive aspergillosis, and empirical antifungal therapy in immunocompromised patients with febrile neutropenia.
The TxGNN model predicts it may be effective for **Gastrin Secretion Abnormality**, with a prediction score of **99.44%**, but this direction is currently supported by **0 clinical trials** and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Invasive candidiasis; invasive aspergillosis (salvage); empirical therapy for febrile neutropenia — not registered in Singapore |
| Predicted New Indication | Gastrin Secretion Abnormality |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the current data source. Based on established pharmacological literature, Caspofungin belongs to the echinocandin class and acts by non-competitively inhibiting β-(1,3)-D-glucan synthase, an enzyme encoded by the fungal *FKS1* and *FKS2* genes. Disruption of this enzyme impairs fungal cell wall synthesis, causing osmotic instability and cell death. This mechanism is highly selective: mammalian cells do not possess β-(1,3)-D-glucan synthase, which explains the drug's relatively favourable tolerability profile in humans.

Gastrin is a gastrointestinal hormone secreted by G cells in the gastric antrum, responsible for stimulating acid secretion and gastric motility. Gastrin secretion abnormality — encompassing hypergastrinemia (e.g., Zollinger–Ellison syndrome) and hypogastrinemia — involves dysregulation of G-cell function, proton-pump feedback, and enteroendocrine signalling pathways that operate entirely within the mammalian host. There is **no known biological pathway** connecting caspofungin's fungal cell wall target to gastrin receptor signalling or G-cell biology.

The high TxGNN score (99.44%) for this indication most likely reflects a **knowledge graph propagation artefact**: indirect connections through shared immunomodulatory or endocrine network nodes, rather than a direct mechanistic relationship. Without supporting preclinical or clinical evidence, this prediction requires biological plausibility validation before any further investment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Caspofungin is currently **not registered in Singapore**. No product authorisations are on record. For reference, the drug is marketed globally under the brand name **Cancidas** (Merck/MSD) and is included in major international antifungal treatment guidelines (IDSA, ESCMID) as a first-line agent for invasive candidiasis.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is high (99.44%), the evidence level is L5 — model prediction only, with no clinical trials, no published literature, and no identifiable biological mechanism linking caspofungin's antifungal target to gastrin hormone physiology. This prediction is consistent with a knowledge graph propagation artefact and does not justify clinical development resources at this stage.

**To proceed, any future reconsideration would require:**
- Identification of a plausible biological pathway linking β-(1,3)-D-glucan synthase inhibition (or off-target echinocandin effects) to gastrin G-cell signalling
- Preclinical evidence (in vitro or animal model) demonstrating an effect on gastrin secretion
- Complete drug MOA data from DrugBank (currently unavailable; retrieval via DrugBank API is the recommended remediation)
- Singapore HSA package insert review for complete safety and contraindication data

---

> **Note on higher-priority repurposing opportunities:** While the top-ranked TxGNN prediction for this drug is not clinically actionable, the same Evidence Pack identifies several mechanistically sound and evidentially supported indications further down the ranked list — notably **Neonatal Candidiasis** (rank 9, L2 evidence including a published double-blind RCT, PMID 31586424) and **Candida glabrata infection** (rank 10, L2 evidence, recommended as first-line by IDSA and ESCMID guidelines). Both align directly with caspofungin's established mechanism of action. Since these drugs are not currently registered in Singapore, these represent potentially high-value repurposing targets for local regulatory submission — and may warrant a separate focused evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

