---
layout: default
title: Dosulepin
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
---

# Dosulepin
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

# Dosulepin: From Depression to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Dosulepin (dothiepin) is a tricyclic antidepressant (TCA) with a long history of clinical use in Europe for depression and anxiety-related neurotic disorders. The TxGNN model's top-ranked prediction is **benign paroxysmal torticollis of infancy** (score: 98.97%), yet **no clinical trials or published literature** currently support this direction — making it a likely false positive driven by knowledge graph topology rather than biological plausibility. Of greater clinical relevance in this evidence pack, indications such as **neurotic disorder**, **melancholia**, and **neurotic depression** are backed by Level L2 evidence, including direct randomised controlled trials using dosulepin itself.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Depression / Neurotic anxiety disorders (tricyclic antidepressant) |
| Predicted New Indication (Rank 1) | Benign Paroxysmal Torticollis of Infancy |
| TxGNN Prediction Score | 98.97% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known information, dosulepin (also known as dothiepin) is a tricyclic antidepressant structurally related to amitriptyline. Published reviews (PMID 2670509) describe its antidepressant activity as primarily mediated through facilitation of noradrenergic neurotransmission via reuptake inhibition, with enhancement of serotonergic neurotransmission as a secondary mechanism. Additional antihistamine (H1) and anticholinergic properties contribute to its sedative and anxiolytic profile.

Benign paroxysmal torticollis of infancy (BPTI) is considered a migraine equivalent in early childhood. Its pathophysiology is linked to cortical spreading depression (CSD) and ion channel dysfunction — particularly mutations in the CACNA1A gene encoding P/Q-type voltage-gated calcium channels. Episodes are typically self-limiting, resolving spontaneously before school age, and rarely require pharmacological prophylaxis.

The mechanistic link between dosulepin and BPTI is biologically implausible. Dosulepin's NET/SERT inhibition, anticholinergic, and antihistamine actions have no established relationship to CSD dynamics or CACNA1A channelopathy. The high TxGNN score most likely reflects indirect topological proximity between migraine-adjacent nodes and the broader depression cluster within the knowledge graph — not a genuine therapeutic signal. This prediction is assessed as a false positive and is not recommended for further clinical investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Dosulepin is not currently registered with Singapore's Health Sciences Authority (HSA). No marketing authorisations are on record. Any clinical use would require an import licence, Special Access Route (SAR) approval, or a formal regulatory pathway submission before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Literature-derived cardiac safety signal**: Two cross-sectional cardiac safety studies specific to dosulepin (PMID 15311996; PMID 15354946) documented statistically significant increases in QT dispersion (QTd) in treated patients compared to healthy volunteers, consistent with the known cardiotoxic potential of the TCA drug class. These findings underscore the need for baseline ECG assessment and ongoing QTc monitoring if dosulepin is considered for any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction — benign paroxysmal torticollis of infancy — has no biological plausibility and is supported by zero clinical or literature evidence. It represents a knowledge graph false positive and should not be prioritised for any repurposing programme.

---

**Higher-Priority Repurposing Opportunities Identified in This Evidence Pack:**

| Indication | Rank | Evidence Level | Recommendation | Key Evidence |
|-----------|------|---------------|----------------|-------------|
| Neurotic Disorder | 7 | L2 | Proceed with Guardrails | Direct dosulepin RCT (Nottingham study, PMID 2899234); 17 years of European experience (PMID 7440528) |
| Melancholia | 4 | L2 | Proceed with Guardrails | Dosulepin vs amitriptyline RCT (PMID 386873); multiple meta-analyses including dosulepin |
| Neurotic Depression | 5 | L2 | Proceed with Guardrails | Nottingham RCT series; naturalistic comparative cohort (PMID 19347769) |
| Dysthymic Disorder | 2 | L3 | Research Question | TCA meta-analysis (PMID 21527126); Nottingham longitudinal cohorts |

**To proceed with the psychiatric indications above, the following is needed:**

- **Regulatory pathway**: Dosulepin is not registered in Singapore; an import licence or Special Access Route application to HSA would be required before any clinical use
- **Cardiac safety protocol**: Mandatory baseline ECG and QTc monitoring must be built into any treatment plan, given documented QT dispersion risk in dosulepin-treated patients
- **MOA data retrieval**: Formal query to the DrugBank API to complete mechanism-of-action documentation (currently unavailable in this evidence pack)
- **Comparator safety review**: Head-to-head safety comparison against currently HSA-approved antidepressants (SSRIs, SNRIs) to establish the benefit-risk profile in the Singapore clinical context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

