---
layout: default
title: Aprotinin
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Aprotinin
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

# Aprotinin: From Perioperative Hemostasis to Primary Release Disorder of Platelets

## One-Sentence Summary

Aprotinin is a broad-spectrum serine protease inhibitor historically used as an antifibrinolytic agent to reduce perioperative blood loss in cardiac surgery; it was voluntarily withdrawn from most global markets in 2007 following safety signals from the BART trial, and has not been registered in Singapore.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
with **2 indirectly relevant clinical trials** and **no direct publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Perioperative hemostasis in cardiac surgery (antifibrinolytic; no Singapore registration on record) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 92.71% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Aprotinin is a Kunitz-type serine protease inhibitor that acts on plasmin, kallikrein, trypsin, and related serine proteases. Its efficacy in reducing surgical blood loss during cardiac bypass procedures was extensively documented prior to its 2007 market suspension, and mechanistically it engages multiple points of the coagulation-fibrinolysis axis that could theoretically touch upon platelet biology.

The TxGNN model's mechanistic rationale centres on two indirect pathways: (1) Aprotinin inhibits plasmin, thereby protecting the platelet GP Ib-IX complex from proteolytic cleavage — preserving the receptor critical for platelet adhesion and signalling; and (2) Aprotinin inhibits kallikrein, reducing contact-activation-induced platelet stimulation, which could theoretically modulate granule release downstream. Both pathways represent plausible but non-primary connections to platelet granule secretion.

However, the mechanistic link is indirect and does not address the core defect. Primary platelet release disorder is fundamentally a granule secretion failure — either δ-granule (dense granule storage pool disease) or α-granule deficiency — driven by intrinsic platelet machinery dysfunction, not by excess protease activity. Inhibiting serine proteases does not restore granule biogenesis or secretion capacity. The high TxGNN score (92.71%) most likely reflects shared knowledge graph nodes between Aprotinin's hemostatic context and platelet-bleeding disorder ontology, rather than a direct therapeutic mechanism.

---

## Clinical Trial Evidence

Neither trial below directly tests Aprotinin in primary platelet release disorder. Both involve different study drugs in cardiac surgery settings where platelet function is a secondary endpoint. They are included because the retrieval algorithm identified contextual overlap, but they do not constitute supportive evidence for this repurposing hypothesis.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01596738](https://clinicaltrials.gov/study/NCT01596738) | N/A | Completed | 120 | Tests **tranexamic acid** (not Aprotinin) in CABG patients with premature clopidogrel cessation; Aprotinin is referenced only as the prior antifibrinolytic standard that was suspended in 2007; provides indirect context on antifibrinolytic strategies in platelet-compromised surgical patients |
| [NCT00724880](https://clinicaltrials.gov/study/NCT00724880) | Phase 4 | Completed | 135 | Evaluates **clopidogrel** (not Aprotinin) and optimal surgical delay to minimise CABG bleeding; explores ADP-receptor-mediated platelet inhibition in a surgical setting; no Aprotinin arm |

> ⚠️ Both trials carry Relevance Grade C — different study drugs, with platelet function as a contextual (not primary) endpoint. Neither constitutes direct evidence for Aprotinin in primary platelet release disorder.

---

## Literature Evidence

Currently no direct literature is available for Aprotinin in primary release disorder of platelets.

---

## Singapore Market Information

Aprotinin is not registered in Singapore. No authorization records are available for review.

---

## Safety Considerations

No formal safety data (warnings, contraindications, drug interactions) was retrievable from the current Evidence Pack. Please refer to the package insert for safety information.

> **Critical historical context**: Aprotinin (Trasylol®) was voluntarily withdrawn from most global markets in November 2007 after the BART (Blood Conservation Using Antifibrinolytics in a Randomized Trial) trial demonstrated a statistically significant increase in 30-day mortality, renal failure requiring dialysis, and serious cardiovascular events compared to tranexamic acid and epsilon-aminocaproic acid. It was conditionally re-approved by the EMA in 2012 for restricted use in adult patients undergoing isolated coronary artery bypass grafting when other antifibrinolytics are insufficient or contraindicated. Any repurposing pathway must address this safety history as a primary concern.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no direct clinical or preclinical evidence supporting Aprotinin in primary platelet release disorder; the mechanistic connection is indirect and does not address the granule secretion defect that defines this condition. Compounded by an unresolved safety profile (prior market withdrawal for mortality/renal risk), the benefit-risk calculation is unfavourable for advancing this candidate in a non-life-threatening indication without substantially more targeted data.

**To proceed, the following is needed:**
- Retrieve and review full TFDA/EMA package insert for current approved warnings, contraindications, and post-reinstatement risk minimisation measures
- Obtain complete DrugBank MOA entry and pharmacological profile (DrugBank DB06692)
- Commission dedicated preclinical studies testing Aprotinin specifically in δ-granule or α-granule deficiency platelet models (e.g., Hermansky-Pudlak or Gray Platelet syndrome cell lines)
- Assess route-of-administration compatibility: Aprotinin is administered intravenously, which may be poorly tolerated for a chronic platelet disorder requiring repeated dosing
- Conduct a formal benefit-risk analysis calibrated for the platelet release disorder patient population — the mortality/renal risk threshold acceptable for life-threatening cardiac surgery is unlikely to be acceptable for a rare bleeding diathesis
- Evaluate Singapore regulatory pathway requirements given zero current registrations and the drug's global post-withdrawal restricted status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

