---
layout: default
title: Isoflurane
parent: 僅模型預測 (L5)
nav_order: 499
evidence_level: L5
indication_count: 10
---

# Isoflurane
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

# Isoflurane: From General Anesthesia to Prinzmetal Angina

## One-Sentence Summary

Isoflurane is a halogenated ether volatile anesthetic, widely used for induction and maintenance of general anesthesia in surgical settings.
The TxGNN model predicts it may be effective for **Prinzmetal Angina**, with currently **no clinical trials** and **no publications** directly supporting this repurposing direction.
Given the mechanistic contradiction between isoflurane's known cardiovascular effects and the pathophysiology of Prinzmetal angina, this prediction warrants critical scrutiny before any further development.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | General anesthesia (induction and maintenance; no Singapore registration on file) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Isoflurane is a halogenated volatile anesthetic whose primary effects include potentiation of GABA-A receptor-mediated inhibitory neurotransmission and antagonism of NMDA glutamate receptors, collectively producing reversible loss of consciousness, analgesia, and muscle relaxation during surgical procedures.

One aspect of isoflurane's pharmacology that could theoretically link it to cardiac ischemic conditions is its well-documented **anesthetic preconditioning** effect: isoflurane activates mitochondrial ATP-sensitive potassium (K-ATP) channels, triggering downstream PKC and adenosine signalling cascades that can protect myocardium from ischemia-reperfusion injury. This cardioprotective mechanism forms the likely basis for the TxGNN model's high prediction score for Prinzmetal angina.

However, the mechanistic link is deeply contradictory in the clinical context of Prinzmetal angina. The core pathology of this condition is episodic coronary artery vasospasm — not fixed atherosclerotic obstruction. Isoflurane's sympathomimetic activation during anesthetic induction and emergence, combined with its known **"coronary steal phenomenon"** (preferential vasodilation of non-ischaemic vessels at the expense of ischaemic territory), may in fact provoke or aggravate coronary vasospasm in this population. This is a recognized clinical risk rather than a therapeutic opportunity, and no clinical research of any kind supports this repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Isoflurane is not registered with the Health Sciences Authority (HSA) in Singapore. No product authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data (warnings, contraindications, drug interactions) were not available in this evidence pack. Two data gaps have been flagged for remediation:
> - Package insert warnings and contraindications (Blocking severity — required before any safety evaluation can proceed)
> - Mechanism of action data from DrugBank (High severity — required for mechanistic linkage analysis)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a very high prediction score (99.67%) to Isoflurane for Prinzmetal angina based on knowledge graph structural inference, the proposed mechanistic link is internally contradictory — isoflurane's sympathomimetic and coronary steal effects could actively worsen the coronary vasospasm that defines this condition, and no clinical or preclinical evidence exists to support this repurposing direction.

**To proceed, the following is needed:**
- Full package insert review to document warnings and contraindications (DG001 — Blocking)
- DrugBank MOA data retrieval to formally characterize the pharmacological mechanism (DG002 — High)
- Preclinical mechanistic studies in validated coronary vasospasm models before any clinical hypothesis can be formulated
- Critical reassessment by a cardiovascular pharmacologist of whether the ischemic preconditioning mechanism could be meaningfully separated from the vasospasm-aggravating effects in a Prinzmetal angina patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

