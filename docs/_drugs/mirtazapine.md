---
layout: default
title: Mirtazapine
parent: 僅模型預測 (L5)
nav_order: 662
evidence_level: L5
indication_count: 10
---

# Mirtazapine
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

Using the drug-repurposing evaluation report format as specified. Before drafting, one important data-quality note from the Evidence Pack itself needs to shape the report: **rank 1–2 predictions (Ohdo syndrome and its variant) are explicitly flagged in `repurposing_rationale.mechanistic_link` as likely knowledge-graph false positives** ("無生物學合理連結，無任何臨床證據，高分應判定為知識圖譜假陽性"), with `decision_stage: S0` / `recommendation: Hold`. Reporting these as the headline candidate would misrepresent the evidence, so I selected the highest-ranked candidate that actually carries clinical/literature support — **rank 6, Dysthymic Disorder** — as the subject of this report, and explain the exclusion of ranks 1–2 explicitly below.

---

# Mirtazapine: From Major Depressive Disorder to Dysthymic Disorder

## One-Sentence Summary

> Mirtazapine is a NaSSA-class antidepressant, established in clinical literature for the treatment of major depressive disorder.
> The TxGNN model's two highest-scoring predictions (Ohdo syndrome and a related craniofacial-intellectual disability syndrome) were flagged by evidence review as **likely knowledge-graph false positives** with no biological plausibility, so the top *evidence-supported* candidate is **Dysthymic Disorder**,
> with **3 clinical trials** and **13 publications** identified, including a dedicated pilot study of mirtazapine specifically in dysthymic patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (based on consistent characterization across the DrugBank/literature evidence in this pack; **not available from Singapore regulatory licensing data**, see note below) |
| Predicted New Indication | Dysthymic Disorder |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L3 (systematic review/meta-analysis + observational/cohort evidence; no dedicated Phase 2/3 RCT of mirtazapine specifically in dysthymia) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

**Note on "Original Indication":** The Evidence Pack's `taiwan_regulatory.licenses` array is empty (drug is unregistered in Singapore), and `drug.original_indications` is also empty in this pack. The indication above is inferred from the consistent framing of mirtazapine as an antidepressant across the supplied literature (e.g., PMID 8930006, 10333982, 19453203) rather than from local regulatory source data — this should be confirmed against an authoritative label before use in a formal submission.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this Evidence Pack (`DG002`, High severity). Based on the supporting literature, mirtazapine is a **noradrenergic and specific serotonergic antidepressant (NaSSA)**: it antagonizes presynaptic α2-adrenergic auto- and heteroreceptors (increasing noradrenaline and serotonin release) and blocks postsynaptic 5-HT2 and 5-HT3 receptors (PMID 8930006, 10333982). This mechanism is well established for major depressive disorder.

Dysthymic disorder is a chronic, lower-grade form of depressive illness that shares core pathophysiological features with major depressive disorder and is frequently treated with the same antidepressant classes (PMID 11310816, 21527126). Since mirtazapine's serotonergic/noradrenergic modulation is not specific to acute major depression, it is mechanistically plausible that the same action would extend to the more chronic, dysthymic end of the depressive spectrum — a link directly tested in a small pilot study (PMID 10569129) and supported by a broader meta-analysis of antidepressant efficacy in dysthymia (PMID 21527126).

**Important caveat on the top-ranked TxGNN predictions:** ranks 1 and 2 in this Evidence Pack (Ohdo syndrome and variants; blepharophimosis–intellectual disability syndrome, Ohdo type) scored higher than dysthymic disorder (99.4% and 99.1% vs. 98.6%) but are rare *KAT6A/KAT6B*-related genetic syndromes with no plausible connection to mirtazapine's NaSSA mechanism and zero supporting clinical trials or literature. The Evidence Pack itself scores these as `Hold`/`S0` and labels them probable knowledge-graph artifacts. They are excluded from this report as not clinically actionable.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00080158](https://clinicaltrials.gov/study/NCT00080158) | Phase 2/3 | Completed | 120 | TASA trial comparing three treatment approaches for depressed adolescents who attempted suicide (general depression trial, not dysthymia- or mirtazapine-specific in the summary provided) |
| [NCT04437485](https://clinicaltrials.gov/study/NCT04437485) | Phase 2 | Completed | 46 | eIMPACT-DM pilot RCT testing a collaborative-care depression intervention on diabetes risk markers; explores whether somatic depressive symptoms moderate treatment effect |
| [NCT02458690](https://clinicaltrials.gov/study/NCT02458690) | Phase 2 | Completed | 216 | eIMPACT trial testing a modernized collaborative-care depression intervention to reduce future cardiovascular disease risk in depressed primary-care patients |

**Caveat:** none of these three trials name mirtazapine or dysthymic disorder specifically in the brief summaries provided — they are broader depression-treatment trials that were matched by the drug/disease query. They should be treated as indirect, population-level supporting context rather than direct trial evidence for mirtazapine in dysthymia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis (RCTs) | J Clin Psychiatry | Meta-analysis of placebo-controlled RCTs comparing antidepressant efficacy in dysthymic disorder vs. major depressive disorder |
| [10569129](https://pubmed.ncbi.nlm.nih.gov/10569129/) | 1999 | Open-label pilot study | Depression and Anxiety | 15 dysthymic patients treated with mirtazapine 15–45 mg; earliest direct clinical evidence for mirtazapine in dysthymia |
| [18833439](https://pubmed.ncbi.nlm.nih.gov/18833439/) | 2008 | Case report | Rev Bras Psiquiatr | Combined venlafaxine + mirtazapine in treatment of major depression with dysthymia ("double depression") |
| [36999619](https://pubmed.ncbi.nlm.nih.gov/36999619/) | 2023 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Review of antidepressants for depression in cancer patients; broader depressive-spectrum context |
| [10446741](https://pubmed.ncbi.nlm.nih.gov/10446741/) | 1999 | Review | J Clin Psychiatry | Reviews antidepressant use across psychiatric disorders beyond primary depression |
| [11310816](https://pubmed.ncbi.nlm.nih.gov/11310816/) | 2001 | Review | J Clin Psychiatry | Treatment algorithm for chronic depression, including dysthymic disorder and "double depression" |
| [17323021](https://pubmed.ncbi.nlm.nih.gov/17323021/) | 2007 | Review | Med Klin (Munich) | General review of depression management in family practice |
| [31265070](https://pubmed.ncbi.nlm.nih.gov/31265070/) | 2019 | Cohort study | J Clin Endocrinol Metab | Population-based Taiwan cohort study: antidepressant use associated with reduced mortality in diabetes patients |
| [26742677](https://pubmed.ncbi.nlm.nih.gov/26742677/) | 2015 | Retrospective comparative study | Arch Ital Biol | Compares hypnotic efficacy of trazodone vs. mirtazapine in chronic insomnia (relevant to comorbid symptom management) |
| [15183602](https://pubmed.ncbi.nlm.nih.gov/15183602/) | 2004 | Clinical study | J Affect Disord | Reboxetine augmentation in antidepressant partial/non-responders |

---

## Singapore Market Information

Mirtazapine currently has **no marketing authorizations on record in Singapore** (`market_status: 未上市`, `total_licenses: 0`). No product name, dosage form, or approved indication text is available from the regulatory data source in this Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information. *(All safety fields in this Evidence Pack — key warnings, contraindications, and drug interaction data — are marked as data gaps; `DG001` classifies the missing local label warnings/contraindications as a **Blocking** severity gap that prevents initial safety screening (S1).)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking data gap (`DG001`, missing local label warnings/contraindications) prevents any initial safety evaluation, and mirtazapine has zero market presence in Singapore.
- Evidence for the dysthymic-disorder indication is supportive but preliminary: one small open-label pilot study directly on mirtazapine, plus a broader antidepressant-class meta-analysis — not a dedicated confirmatory RCT of mirtazapine versus placebo in dysthymia.
- The two highest-scoring TxGNN predictions (Ohdo syndrome and variant) are assessed as probable false positives and are not actionable.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (`DG001`, blocking)
- Mechanism-of-action documentation from DrugBank (`DG002`)
- Drug–drug interaction (DDI) data (currently `not_found`)
- A dedicated Phase 2/3 RCT of mirtazapine specifically in dysthymic disorder to upgrade evidence level beyond L3
- Confirmation of Singapore regulatory pathway options given the drug is currently unregistered

---

*This report is generated for research purposes only and does not constitute medical advice. Repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

