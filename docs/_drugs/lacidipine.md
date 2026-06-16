---
layout: default
title: Lacidipine
parent: 僅模型預測 (L5)
nav_order: 516
evidence_level: L5
indication_count: 10
---

# Lacidipine
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

# Lacidipine: From Hypertension to Migraine Disorder

## One-Sentence Summary

Lacidipine is a third-generation dihydropyridine (DHP) L-type calcium channel blocker (CCB), established in several markets for hypertension treatment but not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Migraine Disorder**, though **no clinical trials** and **no published literature** currently support this specific direction.
The prediction rests entirely on model inference from the knowledge graph (Evidence Level **L5**), and the mechanistic rationale for DHP CCBs in migraine is weak compared to non-DHP CCBs and T-type blockers.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (established pharmacological class use; not registered in Singapore) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 98.34% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Lacidipine from the retrieved sources. Based on known pharmacological class information, Lacidipine is a third-generation dihydropyridine (DHP) L-type calcium channel blocker with high vascular selectivity and lipophilicity, originally developed and used for hypertension. It selectively blocks L-type voltage-gated calcium channels in vascular smooth muscle, causing vasodilation and lowering peripheral resistance.

The mechanistic link between L-type DHP CCBs and migraine is indirect and weak. Certain CCBs do have established roles in migraine prophylaxis — notably flunarizine (a T-type CCB with additional dopamine/histamine receptor antagonism) and verapamil (a non-DHP CCB) — but these act via distinct mechanisms beyond simple L-type vascular channel blockade. Lacidipine's profile, focused on peripheral vascular L-type channels with limited central nervous system penetration, does not map well onto the neuronal and cortical pathways implicated in migraine pathophysiology.

The TxGNN prediction likely arises from shared graph nodes connecting Lacidipine's drug class to vascular and headache-related disease nodes. Without supporting clinical or preclinical data, and given the mechanistic mismatch with established migraine-effective CCBs, this prediction should be treated as a hypothesis-generating signal only. No direct neurovascular or cortical spreading depression studies exist for Lacidipine in the context of migraine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Lacidipine in Migraine Disorder.

---

## Literature Evidence

Currently no related literature available for Lacidipine in Migraine Disorder.

---

## Singapore Market Information

Lacidipine is not currently registered or marketed in Singapore. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction data, key warnings, or contraindication data were retrieved for Lacidipine in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero empirical evidence (no trials, no literature) supporting Lacidipine for migraine disorder, and the mechanistic rationale is weak — L-type DHP CCBs as a class lack neurological evidence for migraine prophylaxis, in contrast to the established migraine-relevant CCBs (flunarizine, verapamil). The TxGNN score reflects graph connectivity rather than validated biological plausibility.

**To proceed, the following would be needed:**

- Confirm Lacidipine's MOA from DrugBank (currently a data gap) to clarify whether any CNS-penetrant or neuronal calcium channel activity exists
- Retrieve full prescribing information / SmPC to assess any historical use or off-label signals in neurovascular conditions
- Conduct a targeted PubMed search on "dihydropyridine calcium channel blocker AND migraine prophylaxis" to assess class-level evidence before attributing to Lacidipine specifically
- Evaluate whether Lacidipine has meaningful blood-brain barrier penetration compared to flunarizine or verapamil
- If class-level evidence is found, design a preclinical study (e.g., cortical spreading depression model) to test Lacidipine's activity before considering any clinical investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

