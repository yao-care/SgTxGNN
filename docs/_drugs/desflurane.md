---
layout: default
title: Desflurane
parent: Low Evidence (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
---

# Desflurane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Desflurane: From Inhalational General Anaesthesia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Desflurane is an inhalational anaesthetic, marketed in Singapore as Suprane, and used for general anaesthesia during procedures.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
but **0 clinical trials** and **0 publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inhalational general anaesthesia (drug class; the registration record has no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 98.90% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, desflurane is an inhalational anaesthetic that acts mainly on GABA-A, glycine, NMDA and K2P channels. Its efficacy in producing general anaesthesia is established.

NSIAD is a rare genetic condition caused by gain-of-function mutations in the AVPR2 gene. These mutations make the vasopressin V2 receptor constitutively active. Desflurane has no known effect on the vasopressin V2 pathway, so **no plausible mechanistic link was identified**.

The high score (0.989, rank 11,286) reflects a graph-based association in the knowledge graph, not independent clinical or literature evidence. Desflurane is also a short-term, procedure-only agent, so chronic use for a chronic genetic disease is not practical.

The other nine predictions in the top 10 are also L5, each with a Hold recommendation and no clinical trials:

- Prinzmetal angina
- Manic bipolar affective disorder
- Tourette syndrome
- Myositis fibrosa
- Idiopathic granulomatous myositis
- Trichotillomania
- Tendinitis
- Fibromyalgia
- Myofascial pain syndrome

Only tendinitis has a retrieved paper, and that paper is not relevant to it. Fibromyalgia has a weak theoretical link through NMDA receptor modulation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature directly supports the predicted indication. The only retrieved paper was attached to a different prediction (tendinitis, rank 8) and does not concern desflurane therapy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18835973](https://pubmed.ncbi.nlm.nih.gov/18835973/) | 2008 | Case report | Canadian Journal of Anaesthesia | Peripheral nerve blockade in a patient with Charcot-Marie-Tooth disease. It concerns regional anaesthesia, not desflurane, and does not support any predicted indication. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN08818P | SUPRANE INHALATION ANAESTHETIC | Solution | Baxter Healthcare Corporation |

## Safety Considerations

- **Malignant hyperthermia**: Desflurane is a known trigger, and caution is needed in patients with muscle disorders.
- **Cardiovascular effects**: It can cause sympathetic activation and tachycardia, especially with rapid concentration increases. This is undesirable in ischaemic heart disease.
- **Airway irritation**: This limits use outside supervised anaesthetic settings.
- **Drug Interactions**: No records were found in the interaction query.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. No clinical trials or supportive literature exist, and there is no plausible link between desflurane and the AVPR2 gain-of-function mechanism. A short-term anaesthetic also cannot serve as a chronic treatment.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or mechanistic evidence linking desflurane to the vasopressin V2 pathway
- A feasible route and dosing concept for chronic use, which has not yet been assessed

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

