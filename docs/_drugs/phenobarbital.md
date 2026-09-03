---
layout: default
title: Phenobarbital
parent: 僅模型預測 (L5)
nav_order: 775
evidence_level: L5
indication_count: 10
---

# Phenobarbital
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

# Phenobarbital: From Epilepsy/Seizure Disorders to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenobarbital is a classic barbiturate anticonvulsant/sedative-hypnotic, long used to control epilepsy and seizure disorders.
The TxGNN model's top-ranked prediction for this drug is **Trigeminal Nerve Neoplasm**,
but this direction is currently supported by **0 clinical trials** and only **1 tangentially related publication**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / seizure disorders (anticonvulsant); no formal Singapore-registered indication text is available (drug is not currently marketed here) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for phenobarbital is not available in this evidence pack. Based on known pharmacology, phenobarbital is a barbiturate that acts as a positive allosteric modulator of the GABA-A receptor, producing broad CNS depression, anticonvulsant, and sedative-hypnotic effects. Its efficacy in generalized and neonatal seizures is well established and has been proven over decades of clinical use.

There is no known or plausible mechanistic link between GABA-A potentiation and antineoplastic activity against a trigeminal nerve tumor. The model's own rationale for this candidate states it directly: the high TxGNN score most likely reflects **semantic/embedding proximity** — "trigeminal" clustering with other trigeminal-region diseases in the knowledge graph — rather than a genuine drug–tumor mechanistic relationship. In other words, this is a case where a high prediction score does not correspond to biological plausibility.

Consistent with this, the only literature retrieved (a 1997 case series on Sturge-Weber syndrome) does not evaluate phenobarbital as a treatment for trigeminal nerve neoplasm; it is only thematically adjacent (a facial/trigeminal-distribution vascular disorder with associated seizures). No clinical trials link phenobarbital to this indication. Overall, this candidate should be treated as a low-confidence, likely artifactual signal rather than a genuine repurposing lead.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales españoles de pediatría | Reviewed 14 cases of Sturge-Weber syndrome (a facial/trigeminal vascular malformation syndrome) over a 25-year period, describing clinical characteristics, disease course, and treatment response; does not evaluate phenobarbital for trigeminal nerve tumor and is only topically related via the "trigeminal" anatomical association. |

## Singapore Market Information

Phenobarbital is currently **not marketed** in Singapore, and no product license records are available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is scored L5 (model prediction only, no supporting studies), and the drug's own repurposing rationale flags the signal as likely a knowledge-graph text/embedding artifact ("trigeminal" clustering) rather than a real pharmacological link — there is no known mechanism connecting GABA-A potentiation to antineoplastic activity, no clinical trials, and no directly relevant literature.

**To proceed, the following is needed:**
- TFDA/HSA product label data (warnings and contraindications) — currently a **Blocking** data gap that prevents any S1 safety evaluation
- Confirmed mechanism-of-action data from DrugBank — currently a **High** severity data gap needed to properly assess mechanistic plausibility
- Independent verification of whether the TxGNN score reflects a genuine biological signal or a text-similarity artifact before allocating further research resources
- If pursued, preclinical evidence establishing any plausible antineoplastic or anti-proliferative mechanism for phenobarbital in trigeminal nerve tumors
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

