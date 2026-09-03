---
layout: default
title: Polatuzumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 795
evidence_level: L5
indication_count: 10
---

# Polatuzumab Vedotin
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

# Polatuzumab Vedotin: From B-Cell Malignancies to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Polatuzumab vedotin is an antibody-drug conjugate (ADC) that targets CD79b, a surface marker expressed almost exclusively on normal and malignant B lymphocytes, delivering the cytotoxic payload MMAE to B-cell malignancies.
The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**, but this prediction is currently supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic review flags it as likely a knowledge-graph artifact rather than a biologically plausible signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — no Singapore license on file; drug's target biology (CD79b) indicates B-cell malignancy use |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available for this drug (Data Gap, high severity). However, the evidence pack's own repurposing rationale confirms the drug class: Polatuzumab vedotin is an antibody-drug conjugate combining an anti-CD79b monoclonal antibody with the microtubule-disrupting cytotoxin MMAE. CD79b is a component of the B-cell receptor complex and is expressed on normal and malignant B lymphocytes only — it has no known expression in breast epithelial or breast tumor tissue, including HER2-positive subtypes.

Because HER2-positive breast carcinoma has no known CD79b expression, there is no target-based mechanism connecting this drug to the predicted indication. The evidence pack explicitly assesses this as likely **knowledge-graph noise**, possibly arising from indirect connections through generic "tumor" or "antibody therapy" nodes rather than a genuine pharmacological relationship.

This assessment is reinforced across the full top-10 prediction list: predictions 2, 3, and 5 (PR-positive, PR-negative, and "normal breast-like" breast cancer subtypes) share the identical lack of CD79b expression rationale; prediction 4 initially appears literature-supported (19 PubMed records) but on inspection all 19 articles concern B-cell biology or Hepatitis B vaccines — a keyword collision between "luminal B" breast cancer subtype and "B cell," not genuine evidence; and predictions 6–10 (drug-induced osteoporosis, acne, and three coagulation-factor disorders) have no plausible mechanistic link to an anti-CD79b/MMAE ADC at all. Taken together, this candidate cluster shows a pattern consistent with model score inflation rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: rank-4 candidate "breast tumor luminal A or B" returned 19 PubMed records, but all concern B-cell immunology/lymphoma/hepatitis B vaccination — a false match on the letter "B" — and are not relevant to the rank-1 predicted indication above.)*

---

## Singapore Market Information

Polatuzumab vedotin is currently **not marketed** in Singapore. No license records (SIN numbers) are on file, so no authorization table can be produced.

---

## Cytotoxicity

Polatuzumab vedotin is an antineoplastic agent (ADC with a cytotoxic MMAE payload, historically used in B-cell malignancies).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (CD79b-directed ADC) delivering a conventional cytotoxic payload (MMAE, a microtubule inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no toxicity data available in this evidence pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | ADC with cytotoxic payload — handle per cytotoxic drug handling regulations pending confirmation from official labeling |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (HER2 positive breast carcinoma) has no clinical trial or literature support, sits at Evidence Level L5 (model prediction only), and lacks any plausible target-based mechanism — CD79b is not expressed in breast tissue. The evidence pack's own review, together with the pattern across all 10 top-ranked candidates for this drug, indicates the signal is most likely knowledge-graph noise rather than a genuine repurposing opportunity.

**To proceed, the following is needed:**
- TFDA/HSA label warnings and contraindications (currently blocking — DG001)
- Confirmed DrugBank mechanism-of-action data (DG002)
- Independent biological rationale or preclinical data specifically linking CD79b/MMAE ADC activity to HER2-positive breast carcinoma before this candidate can advance beyond S0
- If no such evidence emerges, this candidate cluster should be deprioritized in favor of higher-scoring, mechanistically coherent predictions for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

