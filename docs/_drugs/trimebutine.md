---
layout: default
title: Trimebutine
parent: 僅模型預測 (L5)
nav_order: 1017
evidence_level: L5
indication_count: 10
---

# Trimebutine
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

# Trimebutine: From Functional Gastrointestinal Disorders to Migraine Disorder

## One-Sentence Summary

Trimebutine is a peripheral opioid receptor agonist historically used for functional gastrointestinal disorders such as irritable bowel syndrome (IBS); it is not currently registered in Singapore, and no formal Singapore-approved indication text is on file.
The TxGNN model predicts it may be effective for **Migraine Disorder**, likely through a pharmacokinetic (not antimigraine) mechanism,
with **0 clinical trials** and **4 publications** (including 1 RCT) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Singapore regulatory data (drug not registered). Based on published literature, trimebutine is used for functional gastrointestinal disorders (e.g., IBS) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for trimebutine is not available from DrugBank (flagged as a High-severity data gap). Based on known information, trimebutine is a peripheral opioid receptor (μ/δ/κ) agonist that acts selectively on receptors of the Meissner and Auerbach plexuses throughout the GI tract, modulating intestinal smooth muscle motility. It has no systemic absorption or central activity, and its established clinical use is in functional gastrointestinal disorders such as IBS.

The link to migraine is **not** a direct central or vascular antimigraine mechanism. Instead, the rationale is pharmacokinetic synergy: gastroparesis (delayed gastric emptying) frequently occurs during migraine attacks, which delays absorption of orally administered drugs, including triptans. As a gastrokinetic/prokinetic agent, trimebutine may accelerate gastric emptying and thereby improve the absorption, onset of action, and consistency of response of co-administered triptans such as rizatriptan — rather than exerting antimigraine activity on its own.

This mechanistic hypothesis is directly supported by a randomized, double-blind, placebo-controlled crossover trial comparing rizatriptan alone vs. rizatriptan plus trimebutine, and is further contextualized by a review on prokinetic agents' effects on diseases external to the GI tract, and a Lancet review on strategies to increase triptan efficacy. However, because the mechanism is adjunctive/pharmacokinetic rather than a primary antimigraine action, the strength of the "new indication" claim is inherently more limited than a direct pharmacodynamic repurposing case.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16776704](https://pubmed.ncbi.nlm.nih.gov/16776704/) | 2006 | RCT | Cephalalgia | Double-blind, randomized, crossover, placebo-controlled study: rizatriptan + trimebutine vs. rizatriptan alone for acute migraine; trimebutine's gastrokinetic action hypothesized to improve triptan absorption during migraine-associated gastroparesis |
| [19220673](https://pubmed.ncbi.nlm.nih.gov/19220673/) | 2009 | Review | J Gastroenterol Hepatol | Reviews effectiveness of prokinetic agents (including trimebutine) against diseases external to the GI tract, including CNS-related conditions |
| [17046449](https://pubmed.ncbi.nlm.nih.gov/17046449/) | 2006 | Review | Lancet | Discusses strategies (including gastrokinetic co-administration) to increase triptan efficacy in migraine |
| [16245431](https://pubmed.ncbi.nlm.nih.gov/16245431/) | 2005 | Case Report | Polski Merkuriusz Lekarski | Case of abdominal migraine in a 9-year-old girl who did not improve with trimebutine (and other antispasmodics) — a negative/non-supportive data point |

---

## Singapore Market Information

Trimebutine is not currently registered or marketed in Singapore (0 licenses on file). No product authorization, dosage form, or approved indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/HSA label warnings and contraindications are flagged as a Blocking data gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A single randomized, placebo-controlled crossover trial and supporting review literature suggest trimebutine may enhance triptan absorption during migraine attacks via a gastrokinetic (pharmacokinetic), not antimigraine, mechanism. Evidence is directional but limited to one small trial, no confirmatory Phase 2/3 studies exist, and the drug is not currently registered in Singapore.

**To proceed, the following is needed:**
- Official mechanism of action (MOA) data from DrugBank (currently a High-severity data gap, DG002)
- Package insert / label warnings and contraindications from the regulatory authority (currently a Blocking data gap, DG001) — required before any S1 safety review can proceed
- Confirmation of trimebutine's officially approved original indication(s), as no data currently exists in `original_indications`
- Additional RCTs evaluating trimebutine as a triptan-absorption adjunct in migraine, ideally with larger sample sizes and confirmatory design
- Drug-drug interaction data, particularly given trimebutine's opioid receptor activity and likely co-administration with triptans
- Singapore/regional market entry pathway assessment, since the drug currently has zero registrations here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

