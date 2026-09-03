---
layout: default
title: Phenytoin
parent: 僅模型預測 (L5)
nav_order: 781
evidence_level: L5
indication_count: 10
---

# Phenytoin
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

Using the report template directly — this is a data-formatting/synthesis task against a fixed schema, not a coding or debugging task, so no other skill applies here.

One important call I made: `predicted_indications[0]` ("trigeminal nerve neoplasm," score 99.99%) is TxGNN's numerically top-ranked hit, but its own evidence pack literature is entirely about trigeminal *neuralgia* and unrelated conditions — the rationale text itself flags this as an ontology/label mismatch (score L5/Hold, no real evidence). Reporting that as the headline "predicted new indication" would be misleading. I instead built the report around **trigeminal neuralgia** (rank 9 by score, but the only candidate reaching L3/S2/"Proceed with Guardrails" with a real completed trial), and explain this substitution explicitly in the report rather than silently deviating.

---

# Phenytoin: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

> Phenytoin is a classic voltage-gated sodium-channel blocker long established for controlling epileptic seizures. Of the ten TxGNN-predicted indications in this evidence pack, most — including the algorithm's single highest-scoring hit ("trigeminal nerve neoplasm") — turn out to be false positives, ontology mismatches, or animal-only findings with no real supporting evidence. The one credible signal is **Trigeminal Neuralgia**, backed by **1 completed clinical trial** and **19 publications**, including a European Academy of Neurology guideline and a 144-patient retrospective cohort on IV phenytoin for acute pain crises.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — Phenytoin has no Singapore license record; internationally established as a first-generation antiepileptic (sodium-channel blocker) |
| Predicted New Indication | Trigeminal Neuralgia (acute pain exacerbation / IV rescue therapy) |
| TxGNN Prediction Score | 99.97% (candidate rank 854) |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

The structured `original_moa` field is marked as a data gap. However, the evidence pack's own literature and rationale text consistently describe phenytoin as a voltage-gated **sodium-channel blocker** that stabilizes neuronal membranes and suppresses abnormal repetitive firing — the same mechanism underlying its established role as an antiepileptic drug.

Trigeminal neuralgia (TN) is a hyperexcitability disorder of the trigeminal nerve / root entry zone, most often driven by neurovascular compression causing focal demyelination and ectopic firing. Carbamazepine and oxcarbazepine — sodium-channel blockers structurally and mechanistically close to phenytoin — are the established first-line drugs for TN. This shared mechanism is the pharmacological basis for using **IV phenytoin as a rescue option** when oral first-line agents cannot be used, e.g. during severe pain crises with dehydration or inability to swallow.

**Data-quality note:** TxGNN's numerically top-ranked prediction for this drug was "trigeminal nerve neoplasm" (score 99.99%), but every literature item retrieved for that candidate is actually about trigeminal *neuralgia* (a pain syndrome) or unrelated conditions (Sturge-Weber syndrome, an institutional dermatology case series) — none concerns a neoplasm. This is best explained by a disease-ontology label collision in the knowledge graph rather than a genuine oncology signal, and the evidence pack itself scores it L5/Hold. Similarly, six of the ten candidates are reflex-epilepsy subtypes (micturition-, startle-, audiogenic-, eating-, reading-, thinking-induced seizures) that share phenytoin's genuine antiepileptic mechanism but rest only on animal models or isolated case reports (L4–L5, Hold/Research Question). Trigeminal neuralgia is therefore the only candidate in this pack with disease-specific human clinical trial evidence, which is why it — not the top raw score — is the focus of this report.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03712254](https://clinicaltrials.gov/study/NCT03712254) | N/A | Completed | 15 | Prospective study of IV phenytoin as rescue treatment for acute exacerbations of trigeminal neuralgia, for patients unable to tolerate oral first-line therapy (carbamazepine/oxcarbazepine) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Clinical Guideline | Eur J Neurol | EAN guideline on TN diagnosis and management; anticonvulsants are first-line therapy |
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | Retrospective cohort | Cephalalgia | 144 cases: IV lacosamide and phenytoin effective/safe for acute TN pain exacerbations |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | Evidence-based review | J Pain Res | Compares evidence base for phenytoin vs. carbamazepine in TN |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | Pathophysiology and pharmacological treatment overview of TN, including phenytoin |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | Case series | Headache | Retrospective cohort on IV phenytoin as acute rescue treatment for TN crisis |
| [39993829](https://pubmed.ncbi.nlm.nih.gov/39993829/) | 2024 | Review | Clin Med Res | In-hospital management approach to acute TN pain crises |
| [19445753](https://pubmed.ncbi.nlm.nih.gov/19445753/) | 2009 | Review | BMJ Clin Evid | General TN clinical evidence overview |
| [15062534](https://pubmed.ncbi.nlm.nih.gov/15062534/) | 2004 | Review | Neurol Clin | Antiepileptic drugs remain the most effective agents for TN and glossopharyngeal neuralgia |
| [11903537](https://pubmed.ncbi.nlm.nih.gov/11903537/) | 2001 | Review | Headache | Antiepileptic drugs in management of cluster headache and TN |
| [29114270](https://pubmed.ncbi.nlm.nih.gov/29114270/) | 2017 | Review | Asian J Neurosurg | Comprehensive review of TN classification, mechanism, and management |

## Singapore Market Information

Currently no marketing authorization on record. Per the evidence pack, `market_status = 未上市` with **0** registered licenses. A new-registration or import-license pathway would need to be established before local clinical use.

## Safety Considerations

Please refer to the package insert for safety information — the evidence pack's structured `safety.key_warnings`, `safety.contraindications`, and `safety.ddi` fields are all marked as data gaps (see DG001, severity **Blocking**).

**Supplementary note from literature (not from structured safety fields):** case reports surfaced during the literature review flag reactions relevant to clinical judgement — EMPACT syndrome (erythema multiforme associated with phenytoin and cranial radiation), phenytoin-induced thrombocytopenia, and paradoxical seizure aggravation with rapid IV infusion. These should be verified against the official label once DG001 is resolved.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Of the ten TxGNN-predicted indications, trigeminal neuralgia is the only one backed by a completed, disease-specific prospective trial (NCT03712254), a 144-patient retrospective cohort, and an EAN clinical guideline; the other candidates are either ontology mismatches (e.g., "trigeminal nerve neoplasm") or supported only by animal/preclinical data.
- Phenytoin is not currently marketed in Singapore, and the TFDA-equivalent safety labeling (warnings/contraindications) is a **Blocking** data gap (DG001) that must be resolved before any S1 safety review can proceed.

**To proceed, the following is needed:**
- Resolve DG001 — official label warnings/contraindications (Blocking)
- Resolve DG002 — structured MOA data from DrugBank API
- Confirm regulatory pathway for a currently non-marketed drug (new registration vs. named-patient/import use)
- Define the specific clinical use case: current evidence supports IV rescue therapy for **acute** TN exacerbation, not chronic first-line management — scope should be narrowed accordingly
- Do not pursue "trigeminal nerve neoplasm" further given the apparent disease-ontology mismatch; the other reflex-epilepsy candidates remain Hold/Research Question pending human-level evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

