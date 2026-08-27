---
layout: default
title: Galantamine
parent: 僅模型預測 (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
---

# Galantamine
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

# Galantamine: From Alzheimer's Disease to Psychogenic Movement Disorders

## One-Sentence Summary

Galantamine is an acetylcholinesterase inhibitor (AChEI) widely used for the treatment of mild to moderate Alzheimer's disease dementia.
The TxGNN model predicts it may have potential in **Psychogenic Movement Disorders**,
however **no clinical trials** and **no publications** currently support this specific direction — this prediction is derived entirely from the knowledge graph model.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's Disease (mild to moderate dementia) |
| Predicted New Indication | Psychogenic Movement Disorders |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this evaluation. Based on known pharmacological information, Galantamine is an acetylcholinesterase inhibitor that prevents the enzymatic breakdown of acetylcholine, thereby enhancing cholinergic neurotransmission throughout the central nervous system. It also functions as an allosteric potentiating ligand at nicotinic acetylcholine receptors (nAChRs) — a dual mechanism that distinguishes it from other AChEIs such as donepezil. Its proven efficacy in Alzheimer's disease rests on the cholinergic hypothesis: that cognitive decline in AD is driven by the progressive loss of cholinergic neurons in the basal forebrain.

Psychogenic movement disorders (PMD), by contrast, are functional neurological disorders primarily driven by psychological, psychosocial, and functional mechanisms — not by a structural deficit in the cholinergic system. Unlike Alzheimer's disease, PMD does not involve documented cholinergic neuron loss or measurable ACh deficiency as a core pathological feature. The high TxGNN score (99.90%) most likely reflects structural proximity within the knowledge graph — specifically, the clustering of movement disorder disease nodes near Alzheimer's and related cholinergic conditions — rather than a biologically grounded mechanistic link.

In summary, the mechanistic rationale connecting Galantamine's cholinergic mechanism to psychogenic movement disorders remains unsubstantiated. AChEI pharmacology does not address the core psychological/functional drivers of PMD, and no clinical or preclinical literature has explored this connection. This is a knowledge-graph artefact rather than a prioritised repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Galantamine is currently **not registered in Singapore**. No product authorizations are on record (total registrations: 0). Access would require special import approval or a compassionate use application through the Health Sciences Authority (HSA).

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Note:** Package insert warnings, contraindications, and drug–drug interaction data were not available at the time of this evaluation (data gaps DG001 and DG002). Safety review cannot be completed until these data are retrieved from official sources (TFDA/HSA product monograph and DrugBank API).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is based solely on TxGNN knowledge graph modelling (L5 evidence) with no supporting clinical trials, observational data, or published literature for psychogenic movement disorders specifically. The core biological mechanisms of PMD — functional/psychological — are not addressed by Galantamine's cholinergic pharmacology, making this a low-priority repurposing hypothesis at present.

**To proceed, the following is needed:**
- Retrieve full mechanism of action (MOA) data from DrugBank API (data gap DG002) to characterise pharmacological profile in detail
- Download and parse the Singapore/TFDA package insert PDF to extract safety warnings, contraindications, and special population guidance (data gap DG001, currently blocking S1 safety review)
- Re-run drug–drug interaction (DDI) query against an alternative database, as the current query returned no results
- Conduct a focused literature search to determine whether any preclinical evidence links cholinergic enhancement to functional movement disorder pathways
- If any mechanistic hypothesis emerges, consider re-ranking this candidate alongside higher-evidence predictions in the same evidence pack (e.g., Extrapyramidal and Movement Disease at Rank 4 with L3 evidence, or Lingual-Facial-Buccal Dyskinesia at Rank 7 with L4 evidence and 2 Cochrane reviews on cholinergic drugs for tardive dyskinesia)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

