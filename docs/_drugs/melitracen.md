---
layout: default
title: Melitracen
parent: 僅模型預測 (L5)
nav_order: 638
evidence_level: L5
indication_count: 10
---

# Melitracen
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

Using the drug-repurposing evidence pack, I've drafted the report below in English per the v5 template. A few notes on data-handling choices (flagged per project's "cite = verify" and "no [Data Gap] output" rules):

- `taiwan_regulatory.licenses` is empty and `original_moa`/`original_indications` are both empty/`[Data Gap]` — so "Original Indication" in the title/table is stated as inferred background (TCA class / Deanxit combination), explicitly marked as unconfirmed rather than fabricated as a registered indication.
- I used the `scoring.evidence_level` and `scoring.recommendation` values already computed in the evidence pack rather than re-deriving them, since they're upstream-verified.
- Cytotoxicity section omitted — Melitracen is a TCA, not antineoplastic.
- Safety section collapses to the fallback sentence since all three safety fields are Data Gap/empty — but the **Blocking** severity of DG001 (missing TFDA/HSA label warnings) is carried into the Conclusion's next-steps, since it directly gates any S1 safety go/no-go.

---

# Melitracen: From Depression/Anxiety (TCA Class) to Insomnia

## One-Sentence Summary

Melitracen is a tricyclic antidepressant (TCA), best known internationally as a component of the Flupentixol/Melitracen combination (Deanxit) used for depression and anxiety — though a confirmed, registered original indication is not present in this dataset. The TxGNN model predicts it may be effective for **Insomnia**, but this is currently supported only by **0 clinical trials specific to melitracen** and **4 indirect publications**, none of which directly test melitracen's efficacy for insomnia.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in dataset (original_moa and original_indications are data gaps); based on general drug-class knowledge, Melitracen is a TCA marketed as part of the Flupentixol/Melitracen (Deanxit) combination for depression/anxiety |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 97.24% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Melitracen in this dataset. Based on known information, Melitracen is a tricyclic antidepressant (TCA), most commonly used as part of the Flupentixol/Melitracen (Deanxit) combination for mild depression and anxiety. TCAs are pharmacologically associated with sedating antihistaminic and anticholinergic activity, which is the class-level rationale for a theoretical benefit on sleep latency and sleep maintenance.

However, the evidence attached to this candidate does not directly test that hypothesis. The four supporting publications are either studies of a *different* drug (eszopiclone) in a different population (post-stroke insomnia), an unrelated indication (chronic refractory cough responding to Deanxit), or real-world/cross-sectional surveys of insomnia patients' comorbidities and medication patterns in which melitracen appears only incidentally, if at all. None is a controlled trial of melitracen for insomnia specifically.

Given this, the mechanistic link should be treated as a plausible, class-level hypothesis rather than a validated pharmacological pathway — consistent with the L4 evidence level assigned (preclinical/mechanistic reasoning, not direct clinical validation).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38315683](https://pubmed.ncbi.nlm.nih.gov/38315683/) | 2024 | RCT (network meta-analysis) | PLoS One | Evaluates eszopiclone-based combination therapy for post-stroke insomnia; does not study melitracen directly |
| [34330350](https://pubmed.ncbi.nlm.nih.gov/34330350/) | 2021 | Case series/Review | Int J Tuberc Lung Dis | Flupentixol/melitracen (Deanxit) improved chronic refractory cough in 101 patients unresponsive to gabapentin/baclofen — indirect evidence of CNS-modulating effect, not an insomnia study |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Cross-sectional/Real-world | China J Chinese Materia Medica (Zhongguo Zhong Yao Za Zhi) | Real-world survey of comorbidities and medication patterns among 1,067 insomnia patients across 20 hospitals; not a melitracen efficacy study |
| [40827342](https://pubmed.ncbi.nlm.nih.gov/40827342/) | 2025 | Cross-sectional | Psychiatry and Clinical Psychopharmacology | Cross-sectional study of insomnia drug utilization at a Chinese Medicine hospital in Shenzhen; descriptive prescribing patterns, not an efficacy trial |

## Singapore Market Information

Melitracen is currently not marketed in Singapore (market status: Not Marketed, 0 registrations); no license records are available in this dataset.

## Safety Considerations

Please refer to the package insert for safety information. (No TFDA/HSA warnings, contraindications, or drug-interaction data are available in this dataset — this is flagged as a **Blocking** data gap, since it prevents a proper S1 safety assessment.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L4 with no clinical trials or direct efficacy literature specific to melitracen for insomnia — the supporting publications are indirect (different drug, different population, or descriptive utilization data). Combined with the Blocking data gap on safety warnings/contraindications and the drug's non-marketed status in Singapore, there is not yet a sufficient basis to advance beyond a research hypothesis.

**To proceed, the following is needed:**
- TFDA/HSA label warnings and contraindications (currently a Blocking data gap — required before any S1 safety evaluation)
- Confirmed mechanism of action via DrugBank API query (currently a High-severity data gap)
- A dedicated literature/trial search specifically targeting "melitracen AND insomnia" (or "Deanxit AND insomnia") to determine whether direct efficacy evidence exists beyond the incidental references found here
- Drug-drug interaction (DDI) profile, given TCA-class interactions are typically clinically significant (e.g., with other serotonergic/anticholinergic agents) but none are recorded for melitracen in this dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

