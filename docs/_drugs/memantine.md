---
layout: default
title: Memantine
parent: 僅模型預測 (L5)
nav_order: 641
evidence_level: L5
indication_count: 10
---

# Memantine
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

# Memantine: From Unspecified Original Indication to Migraine Disorder

## One-Sentence Summary

> Memantine is an NMDA-receptor antagonist; this evidence pack does not specify its originally approved indication or mechanism of action (data gap), and the drug is currently **not marketed in Singapore**.
> Across 10 TxGNN-predicted indications, **Migraine Disorder** stands out as the strongest candidate, supported by **2 clinical trials** (including one completed Phase 3 trial) and **20 publications**, among them a meta-analysis, a systematic review, and a randomized placebo-controlled trial.
> The remaining 9 predicted indications are largely unsupported by clinical or literature evidence and are not recommended for further action at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no original indication or Singapore license data provided in this evidence pack |
| Predicted New Indication | Migraine Disorder (leading candidate of 10 predicted indications; see appendix below for the rest) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Memantine in this evidence pack, and no original approved indication is recorded either — both are flagged as blocking/high-severity data gaps that must be resolved before a full mechanistic and safety comparison can be made.

Based on the information that is available, Memantine is an NMDA (N-methyl-D-aspartate) receptor antagonist. The predicted link to migraine is mechanistically grounded: cortical spreading depression (CSD) and central sensitization are considered core pathophysiological drivers of migraine, and glutamate/NMDA receptor signaling plays a central role in both processes. This gives the TxGNN prediction reasonable biological plausibility, independent of knowing the drug's original approved use.

This mechanistic rationale is corroborated by a substantial existing literature base specifically studying memantine for migraine prophylaxis — including a completed Phase 3 trial, a placebo-controlled RCT, a systematic review, and a meta-analysis — which is unusually deep supporting evidence for a TxGNN-generated hypothesis. However, one commentary in the same evidence set ("Memantine for migraine—Big promise but little evidence", PMID 34510445) explicitly cautions that clinical evidence remains limited, which should temper the overall confidence level.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Phase 3 | Completed | 33 | Direct comparison of memantine vs. sodium valproate for prophylactic treatment of episodic migraine; active-comparator design (not placebo-controlled), small sample size limits statistical power |
| [NCT02670161](https://clinicaltrials.gov/study/NCT02670161) | Phase 4 | Enrolling by Invitation | 3300 | EMR-based pragmatic quality-improvement registry across 10 common neurological disorders; not a memantine-specific interventional trial, included only as background context (low relevance) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/) | 2016 | RCT (Double-Blind, Placebo-Controlled) | Headache | Randomized placebo-controlled study suggesting memantine may be effective for prophylaxis of migraine without aura |
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Meta-Analysis (RCT) | Clinical Neuropharmacology | Systematic review and meta-analysis of memantine vs. placebo in migraine; efficacy for migraine "remains controversial" |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Systematic Review | Headache | Assesses efficacy and safety of memantine for prophylactic treatment of episodic migraine |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Network Meta-Analysis | Frontiers in Pharmacology | Comparative effectiveness/safety of oral preventive migraine medications in adults 18–65, network meta-analysis |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Clinical Practice Guideline | Annals of Internal Medicine | 2023 VA/DoD Clinical Practice Guideline for management of headache, covering migraine prevention recommendations |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Review | Naunyn-Schmiedeberg's Archives of Pharmacology | Reviews memantine and ketamine (NMDA receptor antagonists) as potential anti-migraine agents |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Commentary/Critical Appraisal | Headache | Cautionary commentary: "Memantine for migraine—Big promise but little evidence" |
| [29508147](https://pubmed.ncbi.nlm.nih.gov/29508147/) | 2018 | Review | Neurotherapeutics | Reviews glutamate and its receptors, including NMDA receptors, as therapeutic targets for migraine |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Retrospective Study | The Journal of Headache and Pain | Retrospective analysis of 60 cases using memantine as preventive therapy for frequent migraine |
| [19031499](https://pubmed.ncbi.nlm.nih.gov/19031499/) | 2008 | Open-Label Study | Headache | Assesses efficacy and tolerability of memantine in preventive treatment of refractory migraine |

---

## Singapore Market Information

Memantine currently has **no marketing authorization on record** in Singapore (0 registrations; market status: Not Marketed). No product listings, dosage forms, or approved indication text are available in this evidence pack.

---

## Other Predicted Indications (Appendix)

For completeness, the remaining 9 TxGNN-predicted indications from this evidence pack are summarized below. None currently meet the evidentiary bar for further action:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|
| 1 | Pulmonary Hypertension | 99.54% | L4 | Hold — mechanistic link indirect; a related compound (MN-08) is in Phase 1, but compound identity vs. memantine is unclear |
| 4 | Migraine with Brainstem Aura | 99.41% | L3 | Research Question — shares NMDA/CSD mechanism with typical migraine, but existing RCT population does not match this subtype |
| 5 | Rheumatoid Arthritis | 98.73% | L4 | Hold — preclinical/in vitro support only, no human treatment evidence |
| 6 | Nephrogenic Syndrome of Inappropriate Antidiuresis | 98.67% | L5 | Hold — no supporting evidence, model prediction only |
| 7 | Atrophoderma Vermiculata | 98.48% | L5 | Hold — no supporting evidence, model prediction only |
| 8 | Migraine With or Without Aura, Susceptibility To | 98.43% | L4 | Hold — genetic susceptibility literature, not treatment evidence |
| 9 | Ulerythema Ophryogenesis | 98.21% | L5 | Hold — no supporting evidence, model prediction only |
| 10 | Brachydactyly-Syndactyly Syndrome | 98.12% | L5 | Hold — no supporting evidence, model prediction only |
| 3 | Kyphoscoliotic Heart Disease | 99.43% | L5 | Hold — no supporting evidence, model prediction only |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction, warning, or contraindication data is currently available for Memantine in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A blocking data gap (missing TFDA/regulatory label — warnings and contraindications) prevents even an initial safety screen (S1) from being completed, regardless of the efficacy signal.
- The strongest candidate indication (migraine) has real but modest-quality evidence: a small (n=33), non-placebo-controlled completed Phase 3 trial, plus a systematic review and meta-analysis that explicitly describe the evidence as "controversial" and "little evidence" despite mechanistic plausibility.
- All other 9 predicted indications lack clinical trial or credible literature support and should not be prioritized.

**To proceed, the following is needed:**
- Obtain the drug's regulatory label/package insert (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- Obtain confirmed mechanism of action data from DrugBank or equivalent source (High-severity data gap, DG002)
- If pursuing migraine further: a larger, placebo-controlled confirmatory RCT, given existing evidence is limited to a small active-comparator trial and retrospective/open-label series
- Clarify original approved indication(s) for Memantine, which are not recorded in this evidence pack, to properly assess indication-to-indication mechanistic similarity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

