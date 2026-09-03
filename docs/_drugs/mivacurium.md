---
layout: default
title: Mivacurium
parent: 僅模型預測 (L5)
nav_order: 676
evidence_level: L5
indication_count: 10
---

# Mivacurium
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

# Mivacurium: From Neuromuscular Blockade to Cauda Equina Syndrome

## One-Sentence Summary

> Mivacurium is a nondepolarizing neuromuscular blocking agent (per the repurposing rationale in this evidence pack, it works by blocking nicotinic acetylcholine receptors at the neuromuscular junction); no formally verified original indication or mechanism-of-action record is on file for this evaluation.
> The TxGNN model's top prediction is **Cauda Equina Syndrome**, but this is a **pure model prediction (L5)** — **0 clinical trials** and **0 publications** support it, and the pack's own mechanistic review argues the prediction is biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Mivacurium is not marketed in Singapore/Taiwan and no approved indication text is on file (Data Gap). Known internationally as an anesthesia-adjunct neuromuscular blocker per this pack's own mechanistic notes. |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 97.91% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Mivacurium is officially a data gap in this evaluation (DG002, severity High). Based on the mechanistic notes accompanying this candidate, Mivacurium is understood to act as a competitive antagonist at postsynaptic nicotinic acetylcholine receptors (nAChR) at the skeletal-muscle neuromuscular junction — the pharmacological basis for its use as a short-acting muscle relaxant during anesthesia.

Cauda equina syndrome, however, is caused by structural compression of the lumbosacral nerve roots, producing lower-motor-neuron dysfunction (bladder, bowel, and perineal sensorimotor deficits). Its pathology is compressive and requires surgical decompression — it is **not** a disorder of neuromuscular junction transmission. Blocking nAChR does not address nerve root compression; it would only add pharmacological muscle weakness on top of the existing neurological deficit.

**Assessment: the mechanistic link is not supportive.** The evidence pack's own rationale explicitly flags this as having no plausible therapeutic mechanism, and further notes that neuromuscular blockade could be relatively **contraindicated** in this context, since it may mask or worsen the neuromuscular exam findings clinicians rely on to monitor these patients. This prediction should be treated as a knowledge-graph association rather than a credible repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Mivacurium currently has **0 registered licenses** and is **not marketed** in Singapore/Taiwan under this evidence pack (`market_status: 未上市`), so no local product or approved-indication text is available for comparison.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data were all unavailable in this evidence pack — DG001, Blocking severity — and must be sourced before any safety assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction sits at Evidence Level L5 (model score only, decision stage S0) with zero corroborating clinical trials or literature, and the drug's own mechanistic review argues against — rather than for — biological plausibility for cauda equina syndrome. Notably, the same pattern held across all ten of the model's top-ranked candidates for this drug (e.g., neurogenic bladder, migraine, glaucoma, hypotrichosis), each independently assessed in this pack as mechanistically unsupported or likely embedding-space noise, which further weakens confidence in this signal set overall.
- Safety data required for even an initial (S1) safety screen is a Blocking data gap (DG001), and the drug is not currently marketed locally, so there is no regulatory or real-world safety baseline to draw on.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert data (warnings, contraindications) to close the Blocking data gap (DG001)
- Verified mechanism-of-action documentation from DrugBank or another primary source (DG002)
- An independent pharmacology/neurology review to confirm or refute the mechanistic rationale before any further investment in this candidate
- If pursued, preclinical or case-level evidence specifically linking neuromuscular blockade to cauda equina syndrome management, since none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

