---
layout: default
title: Gatifloxacin
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
---

# Gatifloxacin
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

# Gatifloxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Gatifloxacin is a 4th-generation fluoroquinolone antibiotic originally developed for respiratory and urinary tract bacterial infections, but subsequently withdrawn from most major markets due to serious blood glucose dysregulation (dysglycemia).
The TxGNN model predicts it may be effective for **Polyclonal Hyperviscosity Syndrome**, with **0 clinical trials** and **0 publications** currently supporting this direction.
Among all 10 predicted indications, **Septicemic Plague** (rank 9) carries the strongest mechanistic rationale, supported by 1 animal study demonstrating fluoroquinolone class activity against *Yersinia pestis* — though the drug's market withdrawal status substantially limits its practical development pathway.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (respiratory tract, urinary tract) — original indication data not available in Evidence Pack |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 97.59% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, Gatifloxacin is a 4th-generation fluoroquinolone antibiotic that inhibits bacterial DNA gyrase (topoisomerase II) and topoisomerase IV, thereby blocking bacterial DNA replication. It was originally approved for community-acquired pneumonia, acute bacterial exacerbation of chronic bronchitis, sinusitis, and urinary tract infections.

Polyclonal hyperviscosity syndrome arises from excessive immunoglobulin production by plasma cells and B cells, causing blood hyperviscosity. There is no established mechanistic link between fluoroquinolone-class DNA gyrase inhibition and the plasma cell or B-cell biology underlying this syndrome. The repurposing rationale in this Evidence Pack explicitly cautions that the high TxGNN score likely reflects a **knowledge graph false positive** — a clustering artifact among hematological disease nodes — rather than a genuine drug-disease connection.

Of the 10 predicted indications, the first 8 (ranks 1–8 and rank 10) all receive a **Hold** recommendation with L5 evidence. The sole exception is **Septicemic Plague** (rank 9), which earns an L3 rating: fluoroquinolones are known to have potent bactericidal activity against *Yersinia pestis* via their core DNA gyrase mechanism, and CDC guidelines already list fluoroquinolones as alternative plague treatments. However, Gatifloxacin's market withdrawal and availability of safer in-class alternatives significantly limit its development feasibility even for this mechanistically plausible indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Polyclonal Hyperviscosity Syndrome.

> **Cross-indication note — Septicemic Plague (rank 9):** One relevant preclinical study was identified with mechanistic relevance to the fluoroquinolone class.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15555886](https://pubmed.ncbi.nlm.nih.gov/15555886/) | 2004 | Animal Study (In Vivo) | International Journal of Antimicrobial Agents | Prophylactic and therapeutic gatifloxacin (100 mg/kg oral, twice daily × 7 days) provided full protection in a BALB/c mouse model of both systemic and pneumonic plague, with efficacy comparable to ciprofloxacin; protection held for up to 6 h post-systemic challenge and 30 h post-aerosol challenge |

---

## Singapore Market Information

Gatifloxacin is not registered in Singapore. There are currently no product authorizations on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical Safety Notice:** Although formal safety data were not available in this Evidence Pack, the following is publicly established and must be considered in any repurposing assessment:
>
> - **Dysglycemia (Black Box–level concern):** Gatifloxacin was withdrawn from the US market (2006) and most other major markets due to clinically serious hypoglycemia and hyperglycemia, particularly in elderly patients and those with diabetes or renal impairment. This metabolic risk is unique to gatifloxacin compared to other fluoroquinolones and represents the primary driver of its withdrawal.
> - **Peripheral neuropathy:** Fluoroquinolone class FDA Black Box Warning — risk of serious, potentially irreversible peripheral neuropathy. This is especially relevant to indication rank 7 (hematological disease associated with acquired peripheral neuropathy), where gatifloxacin could actively worsen the underlying condition.
> - **QT prolongation:** Fluoroquinolone class effect; requires cardiac monitoring in at-risk populations.
> - **Tendinopathy / tendon rupture:** Fluoroquinolone class effect.
>
> The combination of market withdrawal and the dysglycemia liability substantially raises the regulatory and safety bar for any new clinical development program.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-ranked TxGNN prediction (Polyclonal Hyperviscosity Syndrome) lacks biological plausibility and is best interpreted as a knowledge graph artifact. Across all 10 predicted indications, there is zero clinical trial evidence and only one animal study (for Septicemic Plague). Critically, Gatifloxacin's documented market withdrawal due to serious dysglycemia — combined with the availability of safer, currently-marketed fluoroquinolones with comparable or superior antimicrobial profiles — makes investment in a Gatifloxacin-specific repurposing program very difficult to justify.

**To proceed, the following is needed:**

- **Regulatory clarification:** Obtain original approved indications and package insert (from TFDA, HSA, or EMA archives) to complete the drug profile
- **MOA data:** Retrieve full mechanism of action from DrugBank API (DB01044) to enable proper mechanistic-link analysis
- **Safety data:** Extract formal warnings and contraindications from the archived package insert, including the full dysglycemia risk characterization
- **Dysglycemia risk management plan:** Any clinical development pathway must include a strategy to manage or mitigate the blood glucose dysregulation risk that caused market withdrawal
- **Septicemic Plague pathway (if pursued):** Escalate from the single animal study to human pharmacokinetic/pharmacodynamic data; assess regulatory feasibility for a withdrawn drug seeking a new indication; compare against currently available fluoroquinolones (ciprofloxacin, levofloxacin) that already have plague-indication precedent and better safety profiles
- **Knowledge graph audit:** The preponderance of hematological/plasma cell predictions with low biological plausibility suggests a systematic KG bias for this drug node that warrants investigation before further evidence collection is prioritized
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

