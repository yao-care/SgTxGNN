---
layout: default
title: Palonosetron
parent: 僅模型預測 (L5)
nav_order: 750
evidence_level: L5
indication_count: 10
---

# Palonosetron
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

# Palonosetron: From Antiemetic (CINV/PONV) to Migraine Disorder

## One-Sentence Summary

Palonosetron (DB00377) is a 5-HT3 receptor antagonist used as an antiemetic for chemotherapy- and surgery-induced nausea and vomiting (CINV/PONV), per the literature contained in this evidence pack. The TxGNN model predicts it may be effective for **Migraine Disorder**, but this direction is currently supported by **0 clinical trials** and only **1 case report** — and that case report actually describes the drug *causing* migraine-type headache, not treating it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (no regulatory license text available). Literature within the pack identifies palonosetron as a 5-HT3 receptor antagonist approved for chemotherapy-induced nausea and vomiting (CINV) and postoperative nausea and vomiting (PONV) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not available for this candidate (flagged as a High-severity data gap in the evidence pack). Based on the literature retrieved, palonosetron is a second-generation 5-HT3 (serotonin) receptor antagonist, used to block serotonin-mediated emetic signaling in chemotherapy and postoperative settings.

Migraine pathophysiology is primarily driven by 5-HT1B/1D receptor activity and the CGRP pathway, not the 5-HT3 receptor subtype that palonosetron targets. The evidence pack's own mechanistic assessment concludes there is no direct pharmacological link between 5-HT3 antagonism and migraine treatment.

More importantly, the only literature evidence tied to this prediction points in the opposite direction: a 2011 case report titled "Palonosetron-induced migraine-type headache" describes the drug **causing** migraine-type headache as an adverse effect, rather than providing any therapeutic signal. This means the single piece of evidence behind this prediction is a safety signal, not an efficacy signal — the TxGNN score here should be interpreted as a graph-embedding similarity artifact rather than a validated repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Case Report | Canadian Journal of Anaesthesia | Describes palonosetron **inducing** migraine-type headache as an adverse drug reaction — this is a safety signal, not evidence of therapeutic effect for migraine |

---

## Singapore Market Information

Palonosetron is not currently registered or marketed in Singapore according to this evidence pack (total licenses: 0; no license records available).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA/HSA label warnings and contraindications are flagged as a Blocking-severity data gap (DG001) in this evidence pack — this must be resolved before any safety (S1) review can proceed. No drug-drug interaction records were found (query status: not found).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and only a single literature record for the top-ranked prediction (migraine disorder), and that record documents the drug *inducing* migraine-type headache rather than treating it — the opposite of the hypothesized therapeutic direction. Combined with the absence of MOA data, a mechanistic rationale, and any Singapore market presence, the evidence does not support advancing this candidate at this time.

**To proceed, the following is needed:**
- Confirmed original indication and formal label text (Taiwan/HSA regulatory record currently absent)
- Detailed mechanism of action (MOA) data (DrugBank API query, currently a data gap)
- TFDA/HSA package insert warnings and contraindications (Blocking data gap — required before any safety review)
- Independent efficacy evidence for migraine (preclinical or clinical) beyond the single adverse-event case report
- Re-evaluation if new clinical trials or literature specifically studying palonosetron for migraine treatment (not adverse effects) become available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

