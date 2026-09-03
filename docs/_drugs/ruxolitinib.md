---
layout: default
title: Ruxolitinib
parent: 僅模型預測 (L5)
nav_order: 880
evidence_level: L5
indication_count: 10
---

# Ruxolitinib
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

Using the drug-repurposing evaluation report template to produce the report from the supplied Evidence Pack.

---

# Ruxolitinib: From an Undetermined Original Indication to Uterine Corpus Perivascular Epithelioid Cell Tumor (PEComa)

## One-Sentence Summary

> Ruxolitinib is a JAK1/2 inhibitor; its original approved indication cannot be confirmed from this Evidence Pack because regulatory license data and mechanism-of-action (MOA) records are both flagged as data gaps.
> The TxGNN model's top-ranked prediction is **Uterine Corpus Perivascular Epithelioid Cell Tumor (PEComa)**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Singapore license records exist, and MOA is flagged as a data gap (DG002) |
| Predicted New Indication | Uterine Corpus Perivascular Epithelioid Cell Tumor (PEComa) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on general pharmacological knowledge, ruxolitinib is a JAK1/2 inhibitor that blocks JAK-STAT signal transduction; however, without a confirmed original indication in this Evidence Pack, its established efficacy baseline cannot be independently verified here.

The rationale provided alongside this prediction actively argues against strong mechanistic plausibility: PEComa (perivascular epithelioid cell tumor) is understood to be driven predominantly by **TSC1/TSC2 mutations activating the mTOR pathway**, not by JAK-STAT signaling. The evidence pack's own annotation states that the high TxGNN score likely arises from indirect knowledge-graph connections to other tumor/hematologic-malignancy nodes, rather than from a direct, validated molecular link between JAK inhibition and PEComa biology.

Given the absence of any clinical trials or literature for this specific indication, and a stated mechanistic mismatch, this prediction should be treated as exploratory only. Notably, other indications within this same evidence pack — particularly infection-associated hemophagocytic syndrome (rank 9, evidence level L2) — show substantially stronger mechanistic and clinical support for ruxolitinib repurposing and may warrant prioritized review instead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Ruxolitinib currently has **no registered product license in Singapore** (market status: Not Marketed; total licenses: 0). No authorization records are available for this section.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data are all flagged as data gaps in this Evidence Pack — most notably DG001, a "Blocking" severity gap for TFDA label warnings/contraindications, which currently prevents a full safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (PEComa) has no supporting clinical trials or literature, and the stated mechanistic rationale directly questions its biological plausibility (mTOR-driven pathology vs. JAK-STAT inhibition). Combined with a Blocking-severity data gap on TFDA safety labeling, this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA label warnings/contraindications) before any safety pre-assessment (S1) can begin
- Resolve DG002 (confirmed MOA) to properly evaluate mechanistic fit for any candidate indication
- Obtain preclinical or clinical evidence directly testing JAK1/2 inhibition in PEComa/TSC-mTOR–driven tumors before further pursuing this specific prediction
- Consider redirecting review priority toward higher-evidence candidates already present in this same pack — particularly **infection-associated hemophagocytic syndrome** (L2, Proceed with Guardrails, supported by a completed Phase 3 RCT design) and **myxoid liposarcoma** (L4, mechanistic literature via FUS-DDIT3/STAT3 activation)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

