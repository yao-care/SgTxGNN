---
layout: default
title: Pinazepam
parent: 僅模型預測 (L5)
nav_order: 785
evidence_level: L5
indication_count: 10
---

# Pinazepam
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

# Pinazepam: From Anxiolytic Use to Insomnia

## One-Sentence Summary

> Pinazepam is a benzodiazepine derivative; based on published pharmacology literature it has historically been used as an anxiolytic/sedative, though this evidence pack does not contain a formally documented original indication.
> The TxGNN model's top-ranked prediction suggests it may be effective for **Insomnia**,
> but currently only **1 clinical trial** (unrelated to pinazepam) and **no drug-specific literature** support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented (drug not marketed in Singapore); historically used as an anxiolytic/sedative per published pharmacology literature |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Pinazepam is a benzodiazepine derivative that is metabolized to N-desmethyldiazepam — the same active metabolite shared with diazepam. Pharmacology literature (e.g., PMID 6147192) indicates it has anxiolytic and mild sedative properties in animal and early human studies, with lower hypnotic activity than diazepam.

Anxiety and insomnia are both CNS conditions commonly managed with benzodiazepines via GABA-A receptor positive allosteric modulation, which produces both anxiolytic and sedative-hypnotic effects. This shared mechanism is the basis for TxGNN linking pinazepam to insomnia.

However, this mechanistic plausibility is class-level, not drug-specific: the repurposing rationale explicitly notes that pinazepam's original MoA is a data gap and there is no insomnia-specific clinical evidence for this compound. The single associated clinical trial (NCT04151485) was flagged internally as **Grade C relevance** — it studies a fertility psychological intervention and has no connection to pinazepam or sleep pharmacology. Other pinazepam-related predictions in this evidence pack (e.g., anxiety, anxiety disorder) are supported by actual pinazepam-specific open-label studies from the 1970s–80s and carry stronger evidence levels (L3), which may be a more promising repurposing direction than insomnia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04151485](https://clinicaltrials.gov/study/NCT04151485) | N/A | Unknown | 177 | Study of a psychological Mind/Body fertility program in Hungary; **not related to pinazepam or insomnia treatment** — internally graded as low relevance (Grade C), included only due to disease-keyword overlap |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Pinazepam has no marketing authorizations on record in Singapore (0 registrations; market status: Not Marketed). No product-level licensing data is available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (insomnia) is supported only by a class-level mechanistic argument (benzodiazepine GABA-A modulation); the one linked clinical trial is unrelated to pinazepam, and no literature directly evaluates pinazepam for insomnia. This corresponds to Evidence Level L5 — model prediction only.

**To proceed, the following is needed:**
- Original mechanism of action (MOA) data for pinazepam (currently a blocking data gap)
- Singapore/TFDA-equivalent package insert warnings and contraindications (currently a blocking data gap for safety screening)
- Insomnia-specific preclinical or clinical studies on pinazepam (none currently exist)
- Consider evaluating the **anxiety / anxiety disorder** predictions instead (rank 6 and rank 8 in this evidence pack), which are supported by pinazepam-specific open-label clinical studies (PMID 12907, PMID 7006888) and carry a stronger L3/S2 evidence rating
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

