---
layout: default
title: Gabapentin
parent: 僅模型預測 (L5)
nav_order: 246
evidence_level: L5
indication_count: 10
---

# Gabapentin
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

# Gabapentin: From Partial Seizures / Neuropathic Pain to Acne

## One-Sentence Summary

Gabapentin is a well-established antiepileptic and neuropathic pain drug, widely known for its adjunctive use in partial seizures and postherpetic neuralgia via α2δ calcium channel binding. The TxGNN model predicts it may be effective for **Acne (disease)** as the top-ranked new indication (score: 98.46%), with **0 clinical trials** and **1 tangentially related case report** currently identified, providing essentially no evidentiary support for this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Singapore registry; widely known for: partial seizures (adjunctive), postherpetic neuralgia |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 98.46% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on widely established pharmacological knowledge, Gabapentin binds to the α2δ-1 and α2δ-2 auxiliary subunits of presynaptic voltage-gated calcium channels, reducing calcium influx and subsequent release of excitatory neurotransmitters such as glutamate. This mechanism underpins its clinical efficacy in suppressing neuronal hyperexcitability in epilepsy and in attenuating central sensitisation in neuropathic pain states.

The predicted new indication — acne — presents a substantial mechanistic gap. Acne pathology involves four core drivers: sebaceous gland hypersecretion (androgen-mediated), follicular hyperkeratosis, *Cutibacterium acnes* colonisation, and cutaneous innate immune inflammation. None of these processes are known to be modulated by voltage-gated calcium channel α2δ subunit inhibition. There is no established biological pathway connecting Gabapentin's primary mechanism to sebum production, keratinocyte differentiation, or dermal bacteriostasis.

The high TxGNN score (0.9846) most likely reflects a distant, indirect linkage within the knowledge graph — potentially through shared nodes in neurogenic skin inflammation or general inflammatory cascades — rather than a direct and actionable therapeutic rationale. In the absence of any preclinical model data or clinical signal, this prediction is considered a knowledge-graph artefact and cannot currently be regarded as biologically plausible.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [22278969](https://pubmed.ncbi.nlm.nih.gov/22278969/) | 2012 | Case Report | Arthritis Care & Research | Case of a swollen painful toe in a young man — clinical context involves Gabapentin and tophaceous gout, with no relevance to acne pathology or dermatological use |

---

## Singapore Market Information

Gabapentin is currently not registered in Singapore. No marketing authorisation records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no established mechanistic connection between Gabapentin's α2δ calcium channel pharmacology and the pathophysiology of acne, and the sole identified literature record is entirely unrelated to this indication. The TxGNN high score appears to reflect a remote knowledge graph linkage rather than genuine repurposing potential.

**To proceed, the following is needed:**
- Preclinical evidence (in vitro or animal model) demonstrating any biological connection between α2δ calcium channel modulation and sebaceous gland function, keratinocyte proliferation, or acne-related inflammation
- Full MOA data from DrugBank to identify any secondary mechanisms (e.g., anti-inflammatory, anti-androgenic) that could provide a plausible bridge to acne pathophysiology
- Singapore regulatory pathway assessment for Gabapentin registration, should future evidence emerge
- Safety profile documentation including TFDA package insert warnings, contraindications, and drug interaction data before any clinical development can be initiated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

