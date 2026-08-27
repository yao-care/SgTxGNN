---
layout: default
title: Lidocaine
parent: 僅模型預測 (L5)
nav_order: 594
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidocaine: From Local Anesthesia to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

> Lidocaine is a voltage-gated sodium channel blocker used clinically as a local/topical anesthetic (including routine ophthalmic surface anesthesia).
> The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
> but currently **0 clinical trials** and **0 publications** support this specific direction, and the drug's own rationale notes no clear mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anesthesia (topical/regional; voltage-gated Na⁺ channel blocker) — not formally documented in this evidence pack; Singapore licensing data unavailable because the product is not currently registered |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation was not retrieved for this evidence pack (flagged as a data gap, DG002). However, information embedded across the evidence pack's own rationale texts is consistent: lidocaine is a voltage-gated sodium channel blocker, and in ophthalmology it is used almost exclusively as a **topical/local surface anesthetic** — for example, to numb the eye during examinations, injections, or minor procedures (as reflected in several of the ophthalmic surgical anesthesia trials retrieved for other candidate indications in this pack, e.g. NCT05978687, NCT02324166).

Punctate epithelial keratoconjunctivitis, by contrast, is a corneal/conjunctival epithelial disorder most often driven by viral infection, toxic exposure, or dry-eye–related epithelial damage — its underlying pathology is epithelial injury and inflammation, not abnormal nerve signaling. Lidocaine's sodium-channel blockade addresses pain and sensory transmission, not epithelial healing, viral clearance, or inflammatory modulation, so there is no direct disease-modifying mechanism connecting the two.

Per the evidence pack's own repurposing rationale, the high TxGNN score for this candidate "may simply reflect its graph proximity to other ophthalmic drugs" rather than a genuine pharmacological signal — i.e., the model may be picking up on lidocaine's frequent co-occurrence with ophthalmic conditions in general (as an anesthetic adjunct during eye procedures) rather than a true therapeutic effect on this specific disease. This should be read as a low-confidence, mechanism-unsupported prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Lidocaine is not currently marketed in Singapore under this evidence pack (0 registrations, no license records available), so no product/dosage-form table can be generated at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/HSA-equivalent package insert warnings and contraindications are flagged as a blocking data gap — DG001 — and drug interaction data returned no results; these should be obtained before any safety evaluation proceeds.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only, with zero supporting clinical trials or literature), and the drug's own mechanistic rationale explicitly states there is no pharmacological basis linking lidocaine's anesthetic sodium-channel-blocking action to the epithelial/inflammatory pathology of punctate epithelial keratoconjunctivitis. The prediction likely reflects knowledge-graph proximity (lidocaine's common use as an ophthalmic anesthetic adjunct) rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Preclinical/mechanistic studies directly evaluating lidocaine's effect on corneal epithelial inflammation or healing (beyond its anesthetic effect)
- Any clinical trials or case evidence specifically testing lidocaine (as a disease-modifying, not anesthetic, agent) in punctate epithelial keratoconjunctivitis
- Resolution of the blocking safety data gap (DG001: package insert warnings/contraindications) before any S1 safety screening can begin
- Confirmation of Singapore registration/market status, since the drug currently has zero local licenses on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

