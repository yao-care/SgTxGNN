---
layout: default
title: Isavuconazole
parent: 僅模型預測 (L5)
nav_order: 548
evidence_level: L5
indication_count: 10
---

# Isavuconazole
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

# Isavuconazole: From Invasive Fungal Infections to Migraine Disorder

## One-Sentence Summary

Isavuconazole is a broad-spectrum triazole antifungal approved in multiple international jurisdictions for invasive aspergillosis and mucormycosis, working by inhibiting the fungal enzyme CYP51 to disrupt cell membrane synthesis.
The TxGNN model predicts it may be effective for **Migraine Disorder** with a score of 98.99%; however, there are currently **0 clinical trials** and **0 publications** directly supporting this repurposing direction.
The mechanistic rationale is absent, and the high prediction score is most likely a knowledge graph topology artifact — this candidate should be placed on **Hold** pending fundamental pharmacological review.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Invasive aspergillosis; mucormycosis (approved in other jurisdictions; not registered in Singapore) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 98.99% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Isavuconazole (administered as the prodrug isavuconazonium sulfate) is a third-generation triazole antifungal. Although a formal MOA data entry was not available in this Evidence Pack, isavuconazole's established mechanism involves selective inhibition of the fungal cytochrome P450 enzyme CYP51 (lanosterol 14α-demethylase), thereby blocking ergosterol biosynthesis and disrupting fungal cell membrane integrity. It is approved in the US, EU, and Japan for invasive aspergillosis and mucormycosis, with activity spanning *Aspergillus*, *Mucorales*, and select *Candida* species.

Migraine is a complex neurological disorder driven by trigeminovascular activation, CGRP (calcitonin gene-related peptide) release, cortical spreading depression (CSD), and central sensitisation. These mechanisms operate entirely within the human nervous and vascular systems and share no known biological intersection with fungal ergosterol metabolism or CYP51 inhibition.

Critically, the TxGNN model's very high score (0.990) for this pairing is most likely a **knowledge graph topology artifact**: the absence of registered original indications in the source data (`original_indications: []`) may have stripped the drug node of its anchor associations, causing the model to generate biologically implausible high-scoring links. No scientific rationale currently supports isavuconazole as a candidate for migraine treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Isavuconazole is a potent **CYP3A4 inhibitor**. Although formal DDI data was not retrieved in this Evidence Pack, this property is clinically significant and would interact with a wide range of co-medications (e.g., calcium channel blockers used in Prinzmetal angina, pulmonary hypertension drugs such as riociguat and macitentan). Any downstream repurposing evaluation must assess DDI risk as a priority safety item.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for isavuconazole in migraine disorder is not biologically plausible — there is no mechanistic link between fungal CYP51 inhibition and trigeminovascular pathophysiology, and zero clinical or published evidence exists. The high prediction score reflects a model artifact rather than a genuine repurposing signal. Isavuconazole is also not currently registered in Singapore, adding a regulatory barrier to any development pathway.

**To proceed with any further evaluation, the following is needed:**

- **Restore original indication data**: Retrieve and confirm approved indications and MOA from DrugBank (DB11633) or an official package insert to eliminate knowledge graph input bias
- **Re-run TxGNN** with corrected drug node context to assess whether migraine remains a high-ranking prediction after model correction
- **Prioritise mechanistically plausible candidates**: Among the top-10 predictions, rank 4 (pulmonary hypertension) carries an indirect but reviewable biological rationale (fungal infection → pulmonary vascular inflammation → secondary PH), and rank 6 (rheumatoid arthritis) has a documented case report of isavuconazole use in an RA patient — both warrant deeper investigation before migraine
- **Singapore regulatory pathway**: Initiate a pre-submission inquiry with HSA if any indication reaches L2 evidence level or higher, given the drug's current zero-registration status
- **DDI safety assessment**: Commission a formal CYP3A4 DDI evaluation relevant to any target indication before clinical consideration

---

> ⚠️ *This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

