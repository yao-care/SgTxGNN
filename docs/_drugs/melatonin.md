---
layout: default
title: Melatonin
parent: 僅模型預測 (L5)
nav_order: 637
evidence_level: L5
indication_count: 10
---

# Melatonin
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

# Melatonin: From Circadian Rhythm/Sleep Disorders to Migraine with Brainstem Aura

## One-Sentence Summary

> Melatonin is an endogenous pineal hormone conventionally used to regulate sleep-wake and circadian rhythm (e.g., insomnia, jet lag), though this evidence pack contains no verified original-indication or Singapore licensing record for the drug.
> The TxGNN model's top-ranked prediction is that melatonin may be effective for **Migraine with Brainstem Aura**, a rare migraine subtype,
> but current support consists solely of **19 literature reports** extrapolated from general migraine populations, with **0 clinical trials** registered specifically for this subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack — no Singapore license records and no `original_indications` entries on file. Melatonin is generally known as an OTC agent for sleep-wake/circadian rhythm disorders, but this is not confirmed by pack data. |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 87.90% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for melatonin is not available in this evidence pack. Based on known pharmacology, melatonin is a pineal-secreted neurohormone that governs circadian timing and is thought to act through anti-inflammatory, antioxidant, and serotonergic-pathway effects; melatonin receptor agonists (e.g., agomelatine) have separately been explored in headache disorders, which supports biological plausibility for a migraine-related indication in general.

Migraine with brainstem aura (formerly "basilar-type migraine") is a rare migraine subtype. The repurposing rationale supplied with this prediction states explicitly that the mechanistic link is the *same* melatonin–serotonin–circadian pathway implicated in ordinary migraine (reduced nocturnal melatonin secretion is associated with migraine attacks), but that **all supporting evidence comes from general migraine populations, extrapolated to this subtype** — there is no subtype-specific clinical or mechanistic data confirming efficacy in brainstem-aura migraine specifically.

Notably, within this same evidence pack, a related but broader prediction — **"migraine disorder"** (rank 4, score 85.5%) — carries substantially stronger direct evidence: two completed Phase 2/3 RCTs (including a 192-patient Phase 3 trial vs. amitriptyline/placebo) and a published meta-analysis, yielding an L1 evidence level and a "Proceed with Guardrails" recommendation. This suggests that if melatonin's migraine-repurposing signal is to be pursued, the general migraine indication is currently far better substantiated than the brainstem-aura subtype covered by this report's top-ranked prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Migraine with Brainstem Aura specifically. (The query log confirms 0 ClinicalTrials.gov and 0 ICTRP results for this exact subtype; the RCTs cited under the literature section below were conducted in general migraine populations, not this subtype.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27165014](https://pubmed.ncbi.nlm.nih.gov/27165014/) | 2016 | RCT | J Neurol Neurosurg Psychiatry | Randomised trial: melatonin 3 mg vs. amitriptyline 25 mg vs. placebo for migraine prevention (general migraine, not brainstem-aura specific) |
| [38166859](https://pubmed.ncbi.nlm.nih.gov/38166859/) | 2024 | RCT | BMC Neurology | Agomelatine (melatonin receptor agonist) reduced headache severity/frequency in a parallel RCT of episodic migraine without aura |
| [18810607](https://pubmed.ncbi.nlm.nih.gov/18810607/) | 2008 | RCT | Neurol Sci | Open-label 3-month trial of melatonin 3 mg in children with migraine/tension-type headache; symptom improvement reported in most subjects |
| [24909684](https://pubmed.ncbi.nlm.nih.gov/24909684/) | 2015 | Review | Current Drug Safety | Review of safety and efficacy of melatonin in pediatric migraine prophylaxis |
| [7641249](https://pubmed.ncbi.nlm.nih.gov/7641249/) | 1995 | Cohort | Cephalalgia | Nocturnal melatonin excretion significantly decreased in women with menstrually-associated migraine without aura vs. controls |
| [30906963](https://pubmed.ncbi.nlm.nih.gov/30906963/) | 2019 | Review | Neurol Sci | Reviews sleep–headache interactions across migraine (with/without aura), cluster headache, and other primary headaches |
| [28194570](https://pubmed.ncbi.nlm.nih.gov/28194570/) | 2017 | Review | J Headache Pain | Reviews genetic/biochemical serotonergic pathway changes in migraine pathobiology, relevant to the melatonin-serotonin axis |
| [31054199](https://pubmed.ncbi.nlm.nih.gov/31054199/) | 2019 | Cohort | Headache | Found melatonin metabolite levels were not a reliable predictor biomarker of next-day migraine in children/adolescents |
| [9595871](https://pubmed.ncbi.nlm.nih.gov/9595871/) | 1998 | Case series | Headache | Melatonin-responsive headache described in patients with delayed sleep phase syndrome, including migraine without aura |
| [7954740](https://pubmed.ncbi.nlm.nih.gov/7954740/) | 1994 | Cohort | Cephalalgia | Urinary melatonin excretion decreased across the ovarian cycle in menstrually-related migraine without aura patients vs. controls |

*Note: none of the above studies enrolled patients specifically diagnosed with migraine with brainstem aura; all are drawn from general or menstrual/pediatric migraine populations.*

---

## Singapore Market Information

Melatonin currently has **no marketing authorization on file** in Singapore for this evidence pack (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack; a DDI query returned no results.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence for melatonin in migraine with brainstem aura specifically is L3 (observational/review literature only), with zero direct clinical trials for this subtype, and the drug's own repurposing rationale acknowledges the evidence is extrapolated from general migraine populations rather than subtype-specific.
- A Blocking-severity data gap (DG001: Singapore/TFDA label warnings and contraindications) means this candidate cannot yet pass a baseline safety screen, independent of the efficacy question.

**To proceed, the following is needed:**
- Subtype-specific evidence (trial or subgroup analysis) confirming melatonin efficacy in brainstem-aura migraine rather than migraine in general
- Singapore HSA product label / warnings and contraindications data (currently Blocking data gap, DG001)
- Detailed mechanism-of-action documentation from DrugBank or equivalent source (High-priority data gap, DG002)
- Drug-interaction (DDI) data, currently returning "not found"
- Confirmation of melatonin's actual original approved indication and any Singapore licensing status, since none is present in this evidence pack
- Given the much stronger L1 evidence base found elsewhere in this same evidence pack for the broader "migraine disorder" indication (2 completed Phase 2/3 RCTs, meta-analysis support), consider evaluating that broader indication as a separate, better-supported repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

