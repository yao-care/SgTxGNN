---
layout: default
title: Fedratinib
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
---

# Fedratinib
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

# Fedratinib: From Myelofibrosis to Benign PEComa

## One-Sentence Summary

Fedratinib (brand name Inrebic) is a selective JAK2 inhibitor approved for the treatment of intermediate-2 or high-risk primary or secondary myelofibrosis.
The TxGNN model predicts it may be effective for **Benign PEComa (Perivascular Epithelioid Cell Neoplasm)**,
with **no clinical trials** and **no published literature** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Myelofibrosis (intermediate-2 or high-risk primary/secondary) |
| Predicted New Indication | Benign PEComa |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Singapore Market Status | Not registered |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Fedratinib is a selective JAK2 inhibitor with secondary BRD4 inhibitory activity. Its proven efficacy in myelofibrosis stems from suppression of constitutive JAK2/STAT5 signalling — particularly in patients carrying the JAK2 V617F mutation or MPL/CALR alterations that drive aberrant cytokine receptor signalling.

Benign PEComa belongs to the perivascular epithelioid cell tumour family, which is primarily driven by inactivation of TSC1/TSC2, resulting in mTOR pathway hyperactivation. The clinically established treatment for mTOR-driven PEComas is mTOR inhibitors (e.g., everolimus). There is no direct preclinical evidence that Fedratinib's JAK2 or BRD4 inhibition meaningfully suppresses TSC/mTOR-mediated tumour proliferation.

The high TxGNN prediction score most likely reflects shared co-morbidity nodes or tissue-level topological proximity within the knowledge graph rather than a direct mechanistic bridge. Until preclinical models in PEComa specifically demonstrate sensitivity to JAK2 or BRD4 inhibition, the biological plausibility of this repurposing hypothesis remains unestablished.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Fedratinib is not currently registered in Singapore. No product authorisations are on record.

---

## Cytotoxicity

Fedratinib is a targeted anticancer agent indicated for myelofibrosis, a malignant haematological condition. It meets the criteria for antineoplastic classification.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (selective JAK2 / secondary BRD4 kinase inhibitor) |
| Myelosuppression Risk | High — anaemia, thrombocytopenia, and neutropenia are dose-limiting toxicities; CBC monitoring required |
| Emetogenicity Classification | Moderate — nausea and vomiting are commonly reported; anti-emetic prophylaxis is recommended |
| Monitoring Items | CBC with differential (weekly for first 3 months, then monthly); liver function tests; renal function; **thiamine levels** before initiation and periodically thereafter (Wernicke's encephalopathy black-box warning) |
| Handling Protection | Handle as a cytotoxic oral agent per institutional cytotoxic drug handling guidelines |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical note from evidence pack**: Fedratinib carries a **black-box warning for Wernicke's encephalopathy** (thiamine deficiency-associated). This risk is particularly relevant when considering use in malnourished or hypermetabolic patients. Thiamine status must be assessed and corrected before initiating treatment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.84%), the mechanistic link between Fedratinib (a JAK2/BRD4 inhibitor) and benign PEComa (an mTOR-driven tumour) is indirect and speculative, with no supporting clinical trials, literature, or preclinical data. An established standard of care (mTOR inhibitors) already exists for this indication.

**To proceed, the following is needed:**
- Preclinical studies in PEComa cell lines or TSC-null tumour models to determine whether JAK2 or BRD4 inhibition has any effect on mTOR-driven proliferation
- Full MOA and kinase selectivity profile from DrugBank to identify any secondary targets relevant to PEComa biology
- Regulatory strategy assessment: Fedratinib is currently unregistered in Singapore; a regulatory pathway would need to be identified before any clinical development
- Thiamine monitoring protocol to be built into any clinical or compassionate-use plan given the black-box warning
- **Priority note**: Consider evaluating HLH-associated indications (ranks 8–9 in this report, evidence level L4) as a nearer-term repurposing opportunity, given class-effect support from ruxolitinib (JAK1/2) in the same pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

