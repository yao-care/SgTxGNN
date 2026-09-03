---
layout: default
title: Verapamil
parent: 僅模型預測 (L5)
nav_order: 1053
evidence_level: L5
indication_count: 10
---

# Verapamil
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

# Verapamil: From Cardiovascular Disease to Obsolete Bundle Branch Block

## One-Sentence Summary

Verapamil is a non-dihydropyridine calcium channel blocker generally used for hypertension, angina pectoris, and supraventricular arrhythmias (this evidence pack does not contain registry-level indication text). The TxGNN model's top prediction is **Obsolete Bundle Branch Block**, but this prediction is supported by **zero clinical trials** and **zero publications**, and the pack's own mechanistic review flags it as directionally contradictory. This candidate does not currently warrant advancement.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in evidence pack registry data. General pharmacology: hypertension, angina pectoris, supraventricular arrhythmias |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a data gap (DG002) in this evidence pack. Based on the mechanistic notes attached to the prediction itself, verapamil is a non-dihydropyridine calcium channel blocker with a pronounced **negative dromotropic effect** — it slows AV-nodal conduction. This is the opposite of what would be needed to treat a conduction/bundle branch block, which is a defect in impulse propagation rather than a state of pathological over-conduction.

The rationale field for this candidate explicitly notes that "obsolete bundle branch block" is an **obsolete ontology term with unclear semantics**, and that the mechanistic direction contradicts the proposed indication — clinically, non-dihydropyridine CCBs like verapamil are typically **contraindicated or used with caution** in patients with AV block or bundle branch block, not indicated for treating it. In other words, this is very likely a knowledge-graph artifact rather than a biologically plausible repurposing signal.

Among the other nine candidates in this pack, rank 9 (arrhythmogenic right ventricular cardiomyopathy) is mechanistically the most coherent: verapamil's Class IV antiarrhythmic action (L-type calcium channel blockade, suppression of triggered activity) has an established, literature-supported role in **verapamil-sensitive idiopathic fascicular ventricular tachycardia**. However, ARVC is a structural cardiomyopathy where VT is usually scar-related re-entry rather than verapamil-sensitive, and structural heart disease is a known risk factor for hemodynamic decompensation with verapamil — so even this better-supported candidate only reaches L3/S1 ("Research Question"), not a "Go."

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Verapamil currently has **no marketing authorizations registered** in this evidence pack (`total_licenses: 0`, `market_status: 未上市`). No dosage form or approved-indication data is available to populate a registration table.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data are all marked as data gaps or "not found" in this evidence pack — notably, DG001 flags missing HSA/regulatory label warnings as a **Blocking** severity gap.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction ("obsolete bundle branch block") is built on an ambiguous, obsolete ontology term and is mechanistically contradictory to verapamil's known pharmacology — it has no clinical trial or literature support (L5/S0). Combined with the drug being unmarketed in Singapore (0 registrations) and missing safety label data, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain HSA/official package insert warnings and contraindications before any safety screening can occur
- Resolve DG002 (High): confirm verapamil's mechanism of action via DrugBank API to properly evaluate mechanistic plausibility for any candidate indication
- If repurposing interest continues, redirect evaluation toward rank 9 (arrhythmogenic right ventricular cardiomyopathy / verapamil-sensitive fascicular VT), which has the strongest mechanistic and literature basis in this pack, and requires structural heart disease to be ruled out before consideration
- Reject or deprioritize rank 1 and other candidates flagged as "obsolete term" or mechanistically contraindicated (ranks 1, 4, 5, 8)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

