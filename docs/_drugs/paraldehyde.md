---
layout: default
title: Paraldehyde
parent: 僅模型預測 (L5)
nav_order: 755
evidence_level: L5
indication_count: 10
---

# Paraldehyde
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

# Paraldehyde: From Sedative-Anticonvulsant Use to Insomnia

## One-Sentence Summary

Paraldehyde is a classic central nervous system depressant historically used as a sedative and anticonvulsant (e.g., status epilepticus, alcohol-withdrawal sedation), though no Singapore registry data on its original indication is currently available. The TxGNN model's own evidence annotations point to **Insomnia** as the most defensible new-indication candidate — not because it scored highest, but because it is the only prediction in this evidence pack backed by any literature and a coherent mechanistic rationale, supported currently by **1 publication** and **0 clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Singapore registry (drug not marketed); historically used as a sedative and anticonvulsant |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacological classification, paraldehyde is a cyclic-ether CNS depressant that was historically grouped with barbiturates as a sedative-hypnotic and anticonvulsant, used for status epilepticus, procedural sedation, and alcohol-withdrawal delirium before safer alternatives became standard. It is generally understood to potentiate GABA-A receptor–mediated inhibition, a pathway directly relevant to sleep induction and maintenance.

The link between its original use (sedation/seizure control) and the predicted new indication (insomnia) is mechanistically close rather than novel — paraldehyde was in fact used off-label as a hypnotic before falling out of favor due to poor tolerability and abuse potential. This makes the insomnia prediction closer to a "rediscovery of a known effect" than a new hypothesis, consistent with the rationale attached to this candidate in the evidence pack.

Note, however, that TxGNN's single highest-scoring prediction in this evidence pack is actually **irritable bowel syndrome** (99.97%), but the model's own annotation states this candidate has no known mechanistic basis and zero supporting literature or trials. This illustrates that raw prediction rank should not be equated with evidence strength — insomnia, despite a lower score, is the more defensible candidate here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1585214](https://pubmed.ncbi.nlm.nih.gov/1585214/) | 1992 | Review | South African Medical Journal | General review of sleep disorder treatments; the retrieved abstract excerpt discusses narcolepsy and obstructive sleep apnea management and does not explicitly confirm paraldehyde-specific findings — evidentiary link is indirect and should be verified against the full text |

---

## Singapore Market Information

Paraldehyde is currently **not marketed in Singapore** — no registered licenses (0 registrations) were found in the regulatory dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: acquisition of formal label warnings/contraindications is flagged as a blocking data gap — see Next Steps.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the insomnia indication is limited to a single, indirectly-relevant review article with no supporting clinical trials, and the drug is not currently marketed in Singapore. Combined with a blocking gap in safety/label data, the evidence base is too thin to advance without further work.

**To proceed, the following is needed:**
- Singapore/HSA (or TFDA reference) label data — warnings and contraindications (currently a Blocking gap, DG001)
- Confirmed mechanism of action from DrugBank/primary sources (currently a High-severity gap, DG002)
- A targeted literature search specifically for "paraldehyde + insomnia/sedation/hypnotic" to move beyond the single indirect citation currently available
- A feasibility assessment given the drug's obsolete status, since manufacturing/formulation availability may itself be a practical barrier to repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

