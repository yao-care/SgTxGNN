---
layout: default
title: Peginterferon Alfa-2A
parent: 僅模型預測 (L5)
nav_order: 762
evidence_level: L5
indication_count: 10
---

# Peginterferon Alfa-2A
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

# Peginterferon Alfa-2a: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Peginterferon alfa-2a (Pegasys, DB00008) is a pegylated interferon originally developed and internationally approved for chronic hepatitis C, and in many markets it is already approved for chronic hepatitis B (CHB) as well. The TxGNN model's top prediction for this drug — **Hepatitis B Virus Infection** — is therefore best understood as **confirming an established, already-approved use** rather than a genuinely novel repurposing hypothesis, supported by **50 clinical trials** and **20 publications** in this Evidence Pack, including several completed Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Singapore HSA data (drug not locally registered); internationally approved for chronic hepatitis C |
| Predicted New Indication | Hepatitis B Virus Infection (chronic) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Interferon alfa acts through the JAK-STAT signaling pathway to induce host antiviral gene expression and to enhance immune-mediated clearance of HBV-infected hepatocytes — this is the classical mechanism by which interferon-class agents are used to treat chronic hepatitis B.

Importantly, this Evidence Pack flags that `original_indications` for this drug is empty in the underlying dataset, which is a data gap rather than a true absence of prior approval: Peginterferon alfa-2a (Pegasys) is already approved for chronic HBV in most markets worldwide. The TxGNN prediction ranking HBV infection at the top should therefore be read primarily as **data completion / confirmation of a known indication**, not as a novel old-drug-new-use hypothesis. Its practical relevance for this evaluation is regulatory: the drug is currently **not registered in Singapore at all** (0 licenses, market status "not marketed"), so the question is one of local market entry rather than mechanistic plausibility.

Both original and predicted indications are chronic viral hepatitis conditions treated via the same antiviral/immunomodulatory mechanism, which is why the underlying pharmacology transfers directly and is backed by an unusually large and mature clinical evidence base (decades of Phase 3/4 trials).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01369212](https://clinicaltrials.gov/study/NCT01369212) | Phase 3 | Completed | 201 | PegIFN + tenofovir (24wk) then tenofovir alone vs. tenofovir monotherapy (4yr) in HBeAg-positive/negative CHB; primary endpoint HBsAg loss at 48 weeks off-treatment |
| [NCT01095835](https://clinicaltrials.gov/study/NCT01095835) | Phase 3 | Completed | 131 | 48-week vs. 96-week PEG-IFN alfa-2a, alone or with lamivudine, in HBeAg-negative CHB |
| [NCT01368497](https://clinicaltrials.gov/study/NCT01368497) | Phase 3 | Completed | 60 | Entecavir + peginterferon combination in immune-tolerant children (3–<18y) with chronic HBV infection |
| [NCT01697501](https://clinicaltrials.gov/study/NCT01697501) | Phase 3 | Completed | 88 | IL28B polymorphism evaluated in HBeAg-negative CHB patients treated with Pegasys |
| [NCT00435825](https://clinicaltrials.gov/study/NCT00435825) | Phase 4 | Completed | 551 | 4-arm RCT: PEGASYS 90 vs. 180 mcg for 24 vs. 48 weeks — HBeAg seroconversion and safety in HBeAg-positive CHB |
| [NCT02598063](https://clinicaltrials.gov/study/NCT02598063) | Phase 4 | Completed | 255 | PEGASYS vs. adefovir dipivoxil in lamivudine-resistant HBeAg-positive CHB |
| [NCT01641926](https://clinicaltrials.gov/study/NCT01641926) | Phase 3 | Terminated | 402 | Multicenter comparison of PEG-Intron vs. PEGASYS in HBeAg-positive/negative CHB; stopped early |
| [NCT00877760](https://clinicaltrials.gov/study/NCT00877760) | Phase 4 | Completed | 184 | Temporary peginterferon add-on to entecavir to augment response in HBeAg-positive CHB |
| [NCT03181113](https://clinicaltrials.gov/study/NCT03181113) | N/A | Completed | 473 | Long-term cohort assessing durability of benefit after standard peginterferon alfa therapy in HBeAg-positive CHB |
| [NCT02201407](https://clinicaltrials.gov/study/NCT02201407) | N/A | Completed | 50 | PRO B: real-world observational study of PEGASYS effectiveness in CHB |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15371578](https://pubmed.ncbi.nlm.nih.gov/15371578/) | 2004 | RCT | N Engl J Med | Landmark registration trial: peginterferon alfa-2a ± lamivudine vs. lamivudine alone in HBeAg-negative CHB |
| [15987917](https://pubmed.ncbi.nlm.nih.gov/15987917/) | 2005 | RCT | N Engl J Med | Landmark registration trial: peginterferon alfa-2a ± lamivudine vs. lamivudine alone in HBeAg-positive CHB |
| [30549279](https://pubmed.ncbi.nlm.nih.gov/30549279/) | 2019 | RCT | Hepatology | Entecavir + peginterferon alfa-2a safety/efficacy in immune-tolerant HBeAg-positive adults |
| [30865588](https://pubmed.ncbi.nlm.nih.gov/30865588/) | 2019 | Systematic Review/Meta-analysis | Antiviral Therapy | Individual-patient-data meta-analysis establishing PEG-IFN stopping rules in CHB |
| [22045673](https://pubmed.ncbi.nlm.nih.gov/22045673/) | 2011 | Cohort/Meta-analysis | Hepatology | Shorter duration/lower dose PEG-IFN alfa-2a linked to inferior HBeAg seroconversion in genotype B/C |
| [30318613](https://pubmed.ncbi.nlm.nih.gov/30318613/) | 2019 | RCT (pediatric) | Hepatology | Entecavir + peginterferon in children with immune-tolerant CHB |
| [29689122](https://pubmed.ncbi.nlm.nih.gov/29689122/) | 2018 | Phase 3 RCT | Hepatology | PEG-B-ACTIVE study: efficacy/safety of peginterferon alfa-2a in children with CHB |
| [29715359](https://pubmed.ncbi.nlm.nih.gov/29715359/) | 2018 | Review | JAMA | Overview of chronic HBV infection epidemiology, natural history, and treatment options |
| [21423260](https://pubmed.ncbi.nlm.nih.gov/21423260/) | 2011 | Review | Nat Rev Gastroenterol Hepatol | Review of hepatitis B treatment goals and response markers |
| [26700861](https://pubmed.ncbi.nlm.nih.gov/26700861/) | 2015 | RCT | Virology Journal | Long-term effects of peginterferon alfa-2a in Japanese CHB patients |

---

## Singapore Market Information

Peginterferon alfa-2a is **not currently registered with Singapore HSA** — the Evidence Pack records 0 licenses and a market status of "not marketed." No authorization numbers, product names, or approved indication text are available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and clinical case for peginterferon alfa-2a in chronic hepatitis B is very strong — supported by multiple completed Phase 3 RCTs (including two NEJM registration trials) and decades of real-world/observational data — but this reflects an **already internationally approved use**, not a novel hypothesis, and the drug currently has **zero registrations in Singapore**. The gating issue is therefore regulatory submission and local safety documentation, not efficacy evidence.

**To proceed, the following is needed:**
- Singapore/regional package insert warnings and contraindications (currently a Blocking data gap — required before any S1 safety review)
- Verified drug interaction (DDI) data (current DDI query returned no results)
- Formal DrugBank-sourced mechanism of action confirmation to replace the inferred mechanistic rationale used here (High-severity data gap)
- Confirmation of whether a Singapore HSA registration pathway/application is planned, given the drug is not currently marketed locally
- Note: predictions ranked #2–10 in this Evidence Pack (hepatitis E/A, animal hepatitis, Omsk hemorrhagic fever, Kyasanur forest disease, and several cardiac disease nodes) are lower-confidence (L3–L5) or likely graph/mapping noise and are not recommended for further action at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

