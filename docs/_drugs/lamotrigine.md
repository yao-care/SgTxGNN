---
layout: default
title: Lamotrigine
parent: 僅模型預測 (L5)
nav_order: 570
evidence_level: L5
indication_count: 10
---

# Lamotrigine
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

Using the drug repurposing report template directly (no dedicated skill matches this task) to produce the evaluation report from the supplied Evidence Pack.

Before drafting, one important judgment call: **the literal `predicted_indications[0]` entry ("trigeminal nerve neoplasm", TxGNN rank #1) is explicitly flagged inside its own `repurposing_rationale` as a likely string-matching artifact** ("neuralgia" vs "neoplasm"), with no supporting clinical trials, only 2 tangential literature hits, Evidence Level L5, and a "Hold" recommendation. Reporting it as the headline finding would be misleading. I am therefore leading the report with **rank #2, "trigeminal neuralgia"** — the only candidate in this pack with direct lamotrigine trials, an L2 evidence level, and a "Proceed with Guardrails" call — and I disclose this substitution transparently in the rationale section. I've also added a short appendix table covering the other 8 candidates for completeness, since this pack (unusually) carries 10 ranked indications rather than one.

---

# Lamotrigine: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

> Lamotrigine is a broad-spectrum anticonvulsant, established for epilepsy and as maintenance therapy for bipolar I disorder.
> The TxGNN model predicts it may be effective for **Trigeminal Neuralgia**,
> with **4 clinical trials** (2 directly testing lamotrigine) and **19 publications**, including a European Academy of Neurology guideline, currently supporting this direction.
> Note: TxGNN's raw top-ranked hit, *trigeminal nerve neoplasm*, was excluded from this report as a likely keyword-similarity artifact (see rationale below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial and generalized seizures), maintenance treatment of Bipolar I Disorder — based on known drug information; no Singapore label text is available in this evidence pack |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.89% (rank #2,112) |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known pharmacology, lamotrigine is a phenyltriazine-class anticonvulsant that blocks voltage-gated sodium channels on presynaptic neurons, stabilizing neuronal membranes and inhibiting the release of excitatory neurotransmitters (notably glutamate). This mechanism underlies its efficacy in epilepsy and bipolar disorder.

Trigeminal neuralgia is a paroxysmal facial pain syndrome driven by aberrant, high-frequency neuronal discharges in the trigeminal nerve root — pathophysiology mechanistically analogous to epileptic hyperexcitability. The first-line drugs for trigeminal neuralgia, carbamazepine and oxcarbazepine, are themselves sodium-channel blockers in the same pharmacological family as lamotrigine. This shared mechanism is a reasonable basis for the repurposing signal, and it is corroborated by the 2019 European Academy of Neurology guideline, which lists lamotrigine as a recognized second-line/add-on option for trigeminal neuralgia.

It is worth being explicit about a data-quality issue in this evidence pack: TxGNN's literal #1-ranked prediction for lamotrigine was **"trigeminal nerve neoplasm"** (99.97%), not neuralgia. The evidence pack's own analyst annotation concludes this is very likely a false match caused by string similarity between "neuralgia" and "neoplasm" in the knowledge graph — the associated literature (case reports on Gamma Knife radiosurgery for a cavernous malformation, and a general review of neuralgia treatments) has no relevance to neoplastic disease, and lamotrigine has no known antineoplastic mechanism. That candidate has therefore been excluded, and this report focuses on trigeminal neuralgia (rank #2), which has genuine, drug-specific clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Head-to-head efficacy and safety comparison of lamotrigine vs. carbamazepine in trigeminal neuralgia; direct disease-specific evidence, small sample. |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | N/A | Completed | 20 | Double-blind, placebo-controlled add-on study of Lamictal (lamotrigine) in trigeminal neuralgia (tic douloureux); rigorous design, small sample. |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | N/A | Completed | 6 | fMRI study evaluating lamotrigine's mechanistic effect on neuropathic facial pain; supportive mechanistic evidence, not an efficacy endpoint trial. |
| [NCT04996199](https://clinicaltrials.gov/study/NCT04996199) | Phase 4 | Unknown | 132 | Compares carbamazepine vs. oxcarbazepine in trigeminal neuralgia; does not use lamotrigine, only indirectly supports the same drug class's utility. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | European Journal of Neurology | EAN guideline for trigeminal neuralgia management; lists anticonvulsants including lamotrigine among recommended treatment options. |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic Review | Biomedicines | Umbrella review of drugs used for trigeminal neuralgia, evaluating efficacy and side effects across published RCTs and reviews. |
| [21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/) | 2011 | RCT | Journal of the Chinese Medical Association | Direct efficacy/safety comparison of lamotrigine vs. carbamazepine in trigeminal neuralgia patients (companion publication to NCT00913107). |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Practical Neurology | Practical diagnostic and management guide; covers medical and surgical treatment decision-making for trigeminal neuralgia. |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | Overview from trigeminal neuralgia pathophysiology to pharmacological treatments, including sodium-channel-blocking anticonvulsants. |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Updated pharmacotherapy review noting limitations of first-line carbamazepine/oxcarbazepine and discussing alternative anticonvulsants. |
| [25299564](https://pubmed.ncbi.nlm.nih.gov/25299564/) | 2014 | Review | BMJ Clinical Evidence | Evidence review summarizing effectiveness data for pharmacological treatment of trigeminal neuralgia. |
| [30178160](https://pubmed.ncbi.nlm.nih.gov/30178160/) | 2018 | Review | Drugs | Reviews current and innovative pharmacological options for typical and atypical trigeminal neuralgia, including second-line anticonvulsants. |
| [30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/) | 2018 | Case Report | Multiple Sclerosis and Related Disorders | Refractory trigeminal neuralgia in an MS patient successfully treated with pregabalin + lamotrigine combination therapy after carbamazepine intolerance. |
| [34003166](https://pubmed.ncbi.nlm.nih.gov/34003166/) | 2021 | Review | Neurology India | Review of medical management strategies for trigeminal neuralgia. |

---

## Singapore Market Information

Lamotrigine currently holds **no HSA registration in Singapore** (market status: Not Marketed; 0 licenses on file). No product license, brand name, or approved-indication text is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. All safety fields in this evidence pack — key warnings, contraindications, and drug–drug interactions — are currently unavailable (DDI query returned no results), and the missing local package-insert warnings/contraindications are flagged as a **Blocking** data gap (DG001) that must be resolved before any safety pre-assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Two completed, disease-specific studies directly test lamotrigine in trigeminal neuralgia (a head-to-head Phase 2/3 comparison with carbamazepine, and a placebo-controlled add-on trial), and the 2019 EAN guideline lists lamotrigine among recognized treatment options — together supporting an L2 evidence level.
- However, both direct trials are small (n=21 and n=20), lamotrigine is not currently registered in Singapore, and no local safety/label data exists, so this cannot advance past guarded, evidence-gathering status.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain HSA/manufacturer package-insert warnings and contraindications before any safety pre-assessment.
- Resolve DG002 (High): obtain detailed DrugBank mechanism-of-action data to strengthen the mechanistic-link analysis.
- Complete the drug–drug interaction (DDI) query, which currently returns "not found."
- Assess feasibility of a Singapore HSA registration/import pathway, given the drug is not currently marketed locally.
- Consider a larger confirmatory RCT, since existing direct evidence is limited to two small studies (n=21, n=20).
- Formally document and exclude the TxGNN rank #1 "trigeminal nerve neoplasm" signal as a likely string-similarity artifact so it is not mistaken for a validated candidate in downstream systems.

---

## Appendix: Other Predicted Indications (Screening Overview)

This candidate (`TW-DB00555-multi`) carried 10 TxGNN-ranked predictions in total. Beyond trigeminal neuralgia, most fall into a cluster of rare reflex-epilepsy subtypes sharing an identical TxGNN score (99.38%), suggesting these diseases are tightly clustered nodes in the knowledge graph rather than independently differentiated signals — a pattern worth noting when triaging future TxGNN outputs for this drug.

| Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|---|---|---|---|---|
| Trigeminal nerve neoplasm | 99.97% | L5 | S0 | Hold (likely artifact — excluded, see rationale above) |
| Startle epilepsy | 99.38% | L4 | S1 | Research Question |
| Reading seizures | 99.30% | L4 | S1 | Research Question |
| Thinking seizures | 99.38% | L4 | S1 | Research Question |
| Audiogenic seizures | 99.38% | L3 | S2 | Research Question |
| Restless legs syndrome | 98.90% | L3 | S2 | Research Question |
| Eating seizures | 99.38% | L5 | S0 | Hold |
| Orgasm-induced seizures | 99.38% | L5 | S0 | Hold |
| Micturition-induced seizures | 99.38% | L5 | S0 | Hold |

Of these, **audiogenic seizures** (animal-model evidence plus human startle-induced-seizure case series) and **restless legs syndrome** (a pilot trial plus multiple case reports) are the most promising secondary leads and may warrant their own dedicated evaluation reports; the remaining candidates currently lack drug-specific evidence and are not recommended for further investment at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

