---
layout: default
title: Carbetocin
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 10
---

# Carbetocin
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

# Carbetocin: From Postpartum Haemorrhage Prevention to Isotretinoin-Like Syndrome

## One-Sentence Summary

Carbetocin is a long-acting synthetic oxytocin analogue used clinically as a uterotonic agent for the prevention of postpartum haemorrhage following caesarean and vaginal delivery.
The TxGNN model predicts it may be effective for **Isotretinoin-Like Syndrome** (score: 99.15%),
however there are **0 clinical trials** and **0 publications** supporting this specific pairing — the mechanistic connection is entirely unestablished and the prediction is likely a knowledge-graph structural artefact.

> ⚠️ **Notable finding across all 10 predictions:** **Prader-Willi syndrome** (rank 3, score 98.99%) is the only candidate with a biologically coherent rationale — OTR signalling deficits are a documented feature of this condition, and levo-carbetocin (RG7314) has previously entered Phase 2 trials in PWS. This warrants a separate, dedicated evidence pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of postpartum haemorrhage (uterotonic use; not registered in Singapore) |
| Predicted New Indication | Isotretinoin-Like Syndrome |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Carbetocin is a structural analogue of oxytocin with a prolonged duration of action. It acts as an agonist at the oxytocin receptor (OTR), inducing sustained uterine contractions. Compared to native oxytocin, structural modifications at its N-terminus and C-terminus make it resistant to enzymatic degradation, resulting in a half-life approximately four to ten times longer. This property underpins its clinical role in uterotonic prophylaxis after delivery.

Isotretinoin-like syndrome (retinoic acid embryopathy) is a congenital malformation syndrome caused by gestational exposure to retinoids. The affected pathways involve retinoic acid receptor (RAR/RXR) signalling and neural crest cell development — neither of which has any known intersection with the oxytocin/OTR axis. There is no pharmacological, genetic, or epidemiological basis linking OTR agonism to isotretinoin-related teratogenicity.

The TxGNN model's high score for this pairing most likely reflects shared comorbidity structures or co-occurrence patterns within the knowledge graph rather than a genuine mechanistic relationship. Without an articulated biological hypothesis connecting these two, this prediction does not meet the threshold for further investment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Carbetocin is not currently registered with HSA (Health Sciences Authority) Singapore. No product authorisations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.15%), there is no established mechanistic pathway connecting oxytocin receptor agonism to isotretinoin-like syndrome, and the evidence base is entirely absent (L5 — model prediction only). Proceeding without any biological hypothesis or preclinical signal would not be a responsible use of resources.

**To proceed, the following is needed:**

- **Mechanistic hypothesis first:** Identify any biological pathway by which OTR agonism could intersect with retinoic acid teratogenicity before committing further resources to this pairing.
- **Re-prioritise to Prader-Willi syndrome (rank 3):** Open a dedicated evidence pack for the PWS indication. The OTR–PWS mechanistic link is well-documented; cross-validate CARE-PWS (Levo-carbetocin / RG7314) trial data directly against ClinicalTrials.gov, as the current dataset shows 0 trials despite external knowledge indicating a Phase 2 study was conducted.
- **Obtain complete safety profile:** Download and parse the relevant package insert (EMA SmPC or TFDA monograph) to populate key warnings, contraindications, and special population data (the primary data gap blocking S1 safety assessment).
- **Confirm MOA via DrugBank API:** Complete the mechanism-of-action record to support any downstream mechanistic analysis for higher-priority candidates.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

