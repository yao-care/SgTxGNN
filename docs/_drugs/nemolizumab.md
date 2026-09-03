---
layout: default
title: Nemolizumab
parent: 僅模型預測 (L5)
nav_order: 696
evidence_level: L5
indication_count: 10
---

# Nemolizumab
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

# Nemolizumab: From Pruritic Skin Diseases to Diabetic Cataract

## One-Sentence Summary

Nemolizumab is an anti-IL-31 receptor A (IL-31RA) monoclonal antibody developed for pruritus-related skin conditions such as atopic dermatitis and prurigo nodularis. The TxGNN model predicts it may be effective for **Diabetic Cataract**, but currently **0 clinical trials** and **0 publications** support this direction, and the evidence pack itself flags the mechanistic link as absent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pruritus-related skin disease (atopic dermatitis, prurigo nodularis) — not confirmed by structured data, see MOA note below |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.55% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for Nemolizumab is not available in this evidence pack (`original_moa` is a data gap), and `original_indications` is empty. However, the evidence pack's own repurposing rationale identifies Nemolizumab as an anti-IL-31RA monoclonal antibody that blocks pruritus (itch) signalling on sensory neurons, with known/investigational use in atopic dermatitis and prurigo nodularis — both itch-driven skin conditions.

Diabetic cataract is a lens-opacity disorder driven by hyperglycemia-induced polyol pathway activation and osmotic damage to the lens, a pathology unrelated to cutaneous itch signalling. The evidence pack explicitly states that no known mechanistic connection exists between IL-31/IL-31RA blockade and lens opacification, and concludes this prediction is likely model noise.

Notably, 9 of the top 10 TxGNN-ranked predictions for this drug are cataract subtypes (diabetic, immature, mature, tetanic, craniostenosis-associated, nuclear senile, cortical, senile) plus diabetic retinopathy — all clustered in ophthalmology with near-identical scores (~98.2–98.6%) and zero corroborating evidence across all of them. This pattern suggests a systematic knowledge-graph artifact (e.g., an embedding-space proximity effect) rather than a genuine pharmacological signal, and should be treated with heightened skepticism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Nemolizumab currently holds no marketing authorization in Singapore (0 registrations on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5, no clinical trials, no literature), and the evidence pack's own mechanistic analysis finds no plausible biological link between IL-31RA blockade and cataract/diabetic retinopathy pathology — flagging it as likely model noise. Combined with the drug's absence from the Singapore market, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed original indication and MOA data (currently blocked, DG001/DG002 flagged as Blocking/High severity)
- TFDA/HSA label warnings and contraindications (currently a data gap)
- Independent mechanistic or preclinical rationale connecting IL-31RA to lens/retinal pathology before further investment
- Re-screening of lower-ranked TxGNN candidates for this drug with plausible mechanistic overlap with pruritus/inflammatory pathways, which may be more credible repurposing leads than the current top-10 (ophthalmology-clustered) results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

