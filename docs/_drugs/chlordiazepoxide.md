---
layout: default
title: Chlordiazepoxide
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Chlordiazepoxide
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

The design-tokens skill applies to visual document output. Since this report is Markdown with tables, I'll follow the clean structure and hierarchy rules. Now generating the report:

---

# Chlordiazepoxide: From Anxiety Disorders to Insomnia

## One-Sentence Summary

Chlordiazepoxide (Librium) is the world's first benzodiazepine, introduced in 1960 and historically prescribed for anxiety disorders and alcohol withdrawal management.
The TxGNN model predicts it may be effective for **Insomnia**, with **1 clinical trial** (limited relevance to this indication) and **6 publications** currently supporting this direction.
However, chlordiazepoxide's very long half-life and next-day sedation hangover profile raise significant concerns for its suitability under modern insomnia treatment standards.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Singapore registration; historically indicated for anxiety disorders and alcohol withdrawal |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacological knowledge, chlordiazepoxide is the founding member of the benzodiazepine class — its efficacy as an anxiolytic and sedative has been documented since the early 1960s, and mechanistically it acts as a positive allosteric modulator of GABA-A receptors, enhancing the inhibitory effect of gamma-aminobutyric acid throughout the central nervous system.

This GABA-A potentiation provides a plausible mechanistic link to insomnia: enhanced inhibitory tone reduces cortical and subcortical arousal, shortens sleep-onset latency, decreases the number of nocturnal awakenings, and increases total sleep time. This is the same pathway exploited by modern benzodiazepine receptor agonists (z-drugs) and explains why the TxGNN model — trained on drug–disease relationships in the knowledge graph — assigns insomnia such a high prediction score.

The critical limitation, however, is pharmacokinetic rather than pharmacodynamic. Chlordiazepoxide's elimination half-life ranges from 5 to 30 hours, and its primary active metabolite (desmethyldiazepam) accumulates with a half-life of 36–200 hours. This results in significant next-day residual sedation ("hangover"), psychomotor impairment, and cognitive blunting — properties that directly conflict with modern insomnia treatment standards, which prioritise agents with minimal carry-over effects and low risk of morning impairment. Contemporary guidelines explicitly prefer short-to-medium half-life options (e.g., temazepam, zolpidem, eszopiclone) for this reason.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01109030](https://clinicaltrials.gov/study/NCT01109030) | Phase 2/3 | Completed | 50 | Pioglitazone (PPAR-γ agonist) as adjunct to Citalopram for moderate-to-severe depression — **this trial studies a different drug for a different indication and carries no direct evidence value for chlordiazepoxide in insomnia** (retrieved as search noise; relevance Grade C) |

> ⚠️ No clinical trials directly evaluating chlordiazepoxide for insomnia were identified. The single retrieved trial is not relevant to this repurposing hypothesis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4628683](https://pubmed.ncbi.nlm.nih.gov/4628683/) | 1972 | RCT | Current Therapeutic Research | Randomised comparison of molindone vs. chlordiazepoxide in anxious outpatients; demonstrates chlordiazepoxide's sedative-anxiolytic efficacy in a clinical setting, though primary endpoint is anxiety rather than sleep |
| [30680986](https://pubmed.ncbi.nlm.nih.gov/30680986/) | 2019 | Cross-sectional | Medicinski Glasnik | Beers Criteria 2012 evaluation of potentially inappropriate medications in elderly Iranians; benzodiazepines (including chlordiazepoxide) are flagged as inappropriate for insomnia in older adults due to fall and cognitive impairment risk |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opinion on Drug Metabolism & Toxicology | Comprehensive review of anxiolytic pharmacokinetics; places chlordiazepoxide's long half-life and active metabolite burden in context of the broader benzodiazepine class |
| [2883822](https://pubmed.ncbi.nlm.nih.gov/2883822/) | 1986 | Review | Acta Psychiatrica Scandinavica (Suppl.) | Controlled single-dose studies across multiple benzodiazepines consistently show 2–3× greater pharmacodynamic sensitivity in elderly subjects independent of disease or plasma concentrations — directly relevant to hypnotic risk stratification |
| [6111745](https://pubmed.ncbi.nlm.nih.gov/6111745/) | 1981 | Review | The Medical Letter on Drugs and Therapeutics | Comparative guidance on benzodiazepine selection; highlights the distinction between anxiolytic and hypnotic applications, and the trade-offs of long vs. short half-life agents |
| [14085195](https://pubmed.ncbi.nlm.nih.gov/14085195/) | 1963 | Clinical study | Acta Psychiatrica Scandinavica | Early clinical investigation of a Librium metabolite (RO 4-5360) in anxiety and psychosomatic syndromes; provides historical mechanistic context for the sedative/hypnotic spectrum of chlordiazepoxide-derived compounds |

---

## Singapore Market Information

Chlordiazepoxide has **no products registered with the Health Sciences Authority (HSA) of Singapore**. There are no active or historical authorisation records on file.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|-------------------|
| — | No registered products | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Data Gap (Blocking):** TFDA package insert warnings and contraindications have not been retrieved. This constitutes a blocking gap that must be resolved before any safety assessment can proceed. Source: TFDA official website (download and parse package insert PDF).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the GABA-A mechanism provides a pharmacologically coherent link between chlordiazepoxide and insomnia, the drug's very long half-life and accumulating active metabolites produce next-day sedation that is incompatible with modern insomnia treatment standards — making it a mechanistically plausible but clinically suboptimal candidate for this indication. Compounding this, chlordiazepoxide has no Singapore market presence and the single retrieved clinical trial is entirely irrelevant to the insomnia hypothesis.

**To proceed, the following is needed:**
- Resolve the **blocking safety data gap**: retrieve and parse the TFDA (or equivalent) package insert to extract warnings, contraindications, and special population precautions
- Obtain mechanism of action data from DrugBank (DB00475) to formally document the GABA-A allosteric modulation pathway
- Conduct a regulatory feasibility assessment for HSA registration in Singapore, given zero current licences
- Evaluate whether any modified-release formulation strategies could mitigate the long half-life concern before advancing the insomnia hypothesis
- **Consider prioritising the Rank 7 prediction instead** — chlordiazepoxide for barbiturate/sedative withdrawal management (L3 evidence; decision: *Proceed with Guardrails*) is pharmacologically sounder: the long half-life is an *advantage* in withdrawal settings by providing smooth blood-level tapering and cross-tolerance with GABA-depressant substances, and this use has RCT support with multiple systematic reviews
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

