---
layout: default
title: Protamine Sulfate
parent: 僅模型預測 (L5)
nav_order: 829
evidence_level: L5
indication_count: 10
---

# Protamine Sulfate
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

# Protamine Sulfate: From Heparin Reversal to Self-Limited Neonatal/Infantile Seizures (Unsupported Prediction)

## One-Sentence Summary

Protamine sulfate is internationally known as a heparin reversal agent (antidote for heparin/UFH overdose), though it is **not currently registered or marketed in Taiwan/Singapore**. The TxGNN model's top-ranked prediction — **self-limited familial and non-familial neonatal/infantile seizures** — carries only a **baseline score (0.5)** with **no clinical trials, no literature, and no known mechanistic link**. Across all 10 predicted indications reviewed, evidence is either absent (L5) or, in one case, actively points the opposite direction — protamine is documented to *cause* anaphylaxis rather than treat it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Taiwan/Singapore registry (0 licenses on file); internationally used as a **heparin reversal agent** (heparin/UFH antidote) |
| Predicted New Indication | Self-limited familial and non-familial neonatal/infantile seizures |
| TxGNN Prediction Score | 50.0% (this is the model's baseline/no-signal score; rank 51,905 — far outside any meaningful signal range) |
| Evidence Level | L5 (model prediction only, no studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available (flagged as a blocking/high-severity data gap in this pack). Based on the information that is available, protamine sulfate is a strongly cationic polypeptide whose established pharmacology is **electrostatic binding and neutralization of heparin**, used clinically to reverse anticoagulation (e.g., after cardiac surgery, cardiac catheterization, or dialysis). It has no established role in ion-channel modulation, neuronal excitability, or antiepileptic mechanisms.

The predicted new indication — neonatal/infantile seizures — has **no mechanistic rationale connecting it to protamine's known pharmacology**, and the model's own rationale text explicitly states this: "no known ion channel or neuroexcitability-related mechanism links [protamine] to epilepsy." The TxGNN score of 0.5 is the model's neutral/baseline value (not an elevated confidence score), and the disease sits at rank ~51,900 among candidate diseases — consistent with a random or near-random pairing rather than a genuine repurposing signal.

Nine of the ten predicted indications reviewed in this pack (seizures, immune epilepsy, hypereosinophilia, PRPS1 deficiency, pericytoma, tyrosine hydroxylase deficiency, TH-deficient parkinsonism, episodic ataxia, mast cell activation syndrome) share this same pattern: baseline scores, no clinical trials, no literature, and no plausible mechanism. One indication — **anaphylaxis** — did return substantial literature (20 papers), but on inspection the evidence describes protamine **inducing** anaphylactic/anaphylactoid reactions (via IgE/IgG sensitization, non-immune histamine release, and cross-reactivity in fish- or NPH-insulin-exposed patients), not treating it. This is a known adverse-drug-reaction signal misclassified by the model as a therapeutic association, and should be read as a **safety flag, not a repurposing opportunity**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked indication (self-limited neonatal/infantile seizures).

*(Note: one Phase 4 trial, [NCT05774691](https://clinicaltrials.gov/study/NCT05774691), was returned under the "anaphylaxis" candidate, but it studies protamine's existing heparin-reversal use after TAVI — comparing routine vs. selective dosing to reduce bleeding — and is unrelated to treating anaphylaxis.)*

---

## Literature Evidence

Currently no related literature available for the top-ranked indication (self-limited neonatal/infantile seizures).

---

## Singapore Market Information

Protamine sulfate has **0 registered licenses** and is **not currently marketed** in Taiwan/Singapore per the regulatory data on file. No product/authorization records are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information (key warnings, contraindications, and DDI data are not available in this evidence pack).

**Supplementary note from literature evidence (not official label data):** Although not part of the formal safety dataset, the evidence collected under the "anaphylaxis" candidate independently corroborates a **well-documented risk of protamine-induced anaphylaxis/anaphylactoid reactions**, particularly in patients with:
- Prior exposure to protamine-containing insulin (NPH/PZI)
- Fish allergy (protamine is derived from salmon sperm)
- Prior vasectomy
- Prior protamine administration (IgE/IgG sensitization)

This should be treated as a relevant safety signal for any future evaluation of this drug, independent of the repurposing analysis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 reviewed predictions carry baseline TxGNN scores (0.5) with no clinical trial or literature support (L5), except one (anaphylaxis, L4) where the available evidence actually documents protamine as a **cause** of the condition rather than a treatment — the opposite of a repurposing signal. There is no basis to advance any candidate from this pack.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: TFDA/HSA label warnings and contraindications (currently unavailable — blocks any safety pre-screen)
- Resolve high-severity data gap DG002: confirmed mechanism of action from DrugBank (currently unavailable — blocks mechanistic plausibility review)
- If pursued further, a genuinely novel, mechanistically-grounded indication would need to emerge from a future model run with materially higher scores/rank than seen here, since none of the current top-10 candidates meet a minimum bar for further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

