---
layout: default
title: Tiotropium
parent: 僅模型預測 (L5)
nav_order: 983
evidence_level: L5
indication_count: 10
---

# Tiotropium
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

Using no special skill here — this is a direct content-generation task per the fixed report template, not a coding/debugging task.

Note before the report: the evidence pack has two blocking data gaps (DG001: no HSA/TFDA label data; DG002: no MOA data) and `original_indications` is empty. The pipeline's own `repurposing_rationale` for the #1-ranked prediction explicitly states that "obstructive lung disease" is **Tiotropium's known, already-approved indication — not a new signal**. I've kept this flagged transparently rather than presenting it as a genuine repurposing find.

---

# Tiotropium: From Unconfirmed Original Indication to Obstructive Lung Disease (Confirmatory Signal, Not True Repurposing)

## One-Sentence Summary

Tiotropium's original indication could not be extracted from this evidence pack (regulatory and MOA data are both flagged as gaps), so it is unclear from the Evidence Pack alone what it was originally approved for.
The TxGNN model's top-ranked prediction is **Obstructive Lung Disease**, supported by **90+ clinical trials** and **20 publications** — but the model's own mechanistic rationale confirms this is Tiotropium's **existing, already-approved indication (COPD)**, not a novel repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — regulatory record empty in this pack (see Data Gap DG001/DG002 below) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails *(see caveat in Conclusion)* |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available as a standalone structured field. However, the model's own repurposing rationale supplies enough information to interpret the signal: **Tiotropium is a long-acting muscarinic antagonist (LAMA)** that blocks M3 receptors to inhibit airway smooth-muscle contraction, producing sustained bronchodilation.

This mechanism is the textbook basis for treating obstructive airway diseases (COPD, and to a lesser extent asthma) — which is exactly what "Obstructive Lung Disease" describes. The evidence pack's own annotation is explicit on this point: *"此為藥物原始核准適應症，非新預測"* ("this is the drug's original approved indication, not a new prediction").

In other words, this is not a case of the mechanism being applied to a genuinely new disease area — it is TxGNN re-identifying a known drug–disease pair, most likely because the `original_indications` field was empty going into the model (a data completeness issue upstream, not a scientific discovery). The 90+ registered clinical trials and multiple systematic reviews below reflect decades of established COPD therapy, not emerging repurposing evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02567214](https://clinicaltrials.gov/study/NCT02567214) | Phase 4 | Completed | 50 | Head-to-head: indacaterol/glycopyrronium vs tiotropium alone on exertional dyspnea in moderate–severe COPD |
| [NCT00793624](https://clinicaltrials.gov/study/NCT00793624) | Phase 3 | Completed | 906 | 48-week placebo-controlled comparison of inhaled BI 1744 CL vs Foradil in COPD |
| [NCT01550679](https://clinicaltrials.gov/study/NCT01550679) | N/A | Completed | 450 | Early detection of COPD in GOLD 0 (smoker) population |
| [NCT01316900](https://clinicaltrials.gov/study/NCT01316900) | Phase 3 | Completed | 846 | 24-week comparison of GSK573719/GW642444 vs tiotropium in COPD |
| [NCT00975195](https://clinicaltrials.gov/study/NCT00975195) | Phase 4 | Completed | 2,488 | Stepwise ICS withdrawal on top of dual bronchodilator therapy in severe/very severe COPD |
| [NCT02172482](https://clinicaltrials.gov/study/NCT02172482) | N/A | Completed | 63,127 | Large post-marketing surveillance of Spiriva 18 µg tolerability/efficacy in daily practice |
| [NCT01006135](https://clinicaltrials.gov/study/NCT01006135) | N/A | Completed | 4,852 | Observational SGRQ quality-of-life study in Central & Eastern European COPD patients |
| [NCT00624377](https://clinicaltrials.gov/study/NCT00624377) | N/A | Completed | 2,031 | Real-world safety/effectiveness of Spiriva in severe COPD |
| [NCT02850978](https://clinicaltrials.gov/study/NCT02850978) | N/A | Completed | 1,335 | Japan post-marketing surveillance of tiotropium+olodaterol FDC in COPD |
| [NCT05402020](https://clinicaltrials.gov/study/NCT05402020) | N/A | Completed | 17,018 | Taiwan NHI claims-based real-world comparison of tiotropium/olodaterol vs ICS/LABA |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | N Engl J Med | Long-term tiotropium improves lung function and slows decline in mild/moderate COPD |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | Systematic Review | Cochrane Database Syst Rev | Updated Cochrane review of tiotropium vs placebo in COPD |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Systematic Review | Cochrane Database Syst Rev | Cochrane review comparing tiotropium vs ipratropium in COPD |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Review | Respiratory Research | Review of tiotropium's clinical development as LAMA monotherapy in COPD |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | Review | Life Sciences | Original mechanistic and clinical profile characterization of tiotropium |
| [29670674](https://pubmed.ncbi.nlm.nih.gov/29670674/) | 2018 | Review | Canadian Respiratory Journal | Review of tiotropium use in asthma patient selection |
| [35510163](https://pubmed.ncbi.nlm.nih.gov/35510163/) | 2022 | Cohort | Int J Chron Obstruct Pulmon Dis | Taiwan multicenter real-world comparison of LABA/LAMA fixed-dose combinations |
| [29605624](https://pubmed.ncbi.nlm.nih.gov/29605624/) | 2018 | RCT (DYNAGITO) | Lancet Respir Med | Tiotropium+olodaterol vs tiotropium alone on COPD exacerbation prevention |
| [36714923](https://pubmed.ncbi.nlm.nih.gov/36714923/) | 2023 | Observational | Expert Rev Respir Med | Multicenter prospective study of tiotropium efficacy/safety in symptomatic Chinese COPD patients |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Review | Drugs | Comprehensive overview of tiotropium bromide pharmacology and clinical use |

---

## Singapore Market Information

Tiotropium is currently **not marketed** in Singapore according to this evidence pack, and no registration records (HSA/product licenses) are available (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails — with an important caveat**

**Rationale:**
The evidence base for "Obstructive Lung Disease" is exceptionally strong (L1: multiple completed Phase 3 RCTs, large real-world cohorts, and Cochrane systematic reviews spanning >25 years). However, this strength exists precisely *because* it is Tiotropium's established, already-approved use — not because TxGNN uncovered a novel therapeutic hypothesis. As the model's own rationale states, this signal should not be treated as a genuine repurposing candidate.

Among the other TxGNN predictions for this drug: rank 4 ("COPD, severe early onset," L3, decision stage S2, "Research Question") is the only other candidate with a plausible mechanistic and evidentiary basis, though it lacks a subgroup-specific prospective trial. Ranks 2, 3, and 6–10 (respiratory malformation, Rienhoff syndrome, hyperlucent lung, interstitial/compensatory emphysema, tracheal stenosis, CD8α-related immunodeficiency) are assessed as L4/L5 with no mechanistic plausibility or supporting evidence, and are recommended for **Hold**.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve HSA/TFDA label warnings and contraindications before any S1 safety screening can proceed
- Resolve DG002 (High): obtain confirmed MOA from DrugBank API to properly separate "known indication" signals from genuine repurposing candidates
- Backfill `original_indications` so the prediction pipeline does not re-surface already-approved uses as "new" candidates
- If pursuing rank 4 (early-onset severe COPD) as a genuine research question, commission a subgroup-specific study rather than relying on general COPD comparative-effectiveness data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

