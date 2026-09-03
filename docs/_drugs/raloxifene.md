---
layout: default
title: Raloxifene
parent: 僅模型預測 (L5)
nav_order: 839
evidence_level: L5
indication_count: 10
---

# Raloxifene
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

# Raloxifene: From Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

> Raloxifene is a selective estrogen receptor modulator (SERM) globally known for the treatment/prevention of postmenopausal osteoporosis; formal original-indication and MOA records for this pack are currently unavailable.
> The TxGNN model's top prediction is **Duodenal Ulcer (disease)**, but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic analysis flags the prediction as likely knowledge-graph noise rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Singapore regulatory data (drug not marketed); globally known for postmenopausal osteoporosis |
| Predicted New Indication | Duodenal Ulcer (disease) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this pack is not available (Data Gap). Based on general drug knowledge, Raloxifene is a SERM that acts primarily on bone tissue (reducing bone resorption) and, to a lesser extent, on lipid metabolism (modest LDL-C and Lp(a) lowering). It has no known pharmacological activity related to gastric acid secretion, mucosal protection, *H. pylori*, or NSAID-mediated mucosal injury — the core pathophysiological pathways of duodenal ulcer.

Critically, the evidence pack's own repurposing rationale for this top-ranked prediction states that the mechanistic link is unsupported: *"Raloxifene 主要作用於骨組織與部分脂質代謝路徑，與十二指腸潰瘍病理機轉（Hp感染、NSAID、胃酸-黏膜屏障失衡）無已知關聯。TxGNN 高分推測為知識圖譜共現雜訊，缺乏生物學合理性"* — i.e., the model's high confidence score is assessed as likely a knowledge-graph co-occurrence artifact rather than a biologically plausible repurposing signal.

Reviewing the remaining top-10 predictions for this drug reinforces the same pattern: nearly all (hypoalphalipoproteinemia, duodenal obstruction, duodenogastric reflux, Worth syndrome, homozygous familial hypercholesterolemia, ADNIV, brain stem infarction, obsolete familial combined hyperlipidemia) are rated L5 with no clinical or literature support, and several are flagged as mechanistically implausible or even *contraindicated* (e.g., Worth syndrome — a bone-**hardening** disorder, where an anti-resorptive drug is mechanistically opposed; brain stem infarction — where Raloxifene carries a known black-box VTE/fatal stroke risk in the opposite direction). Only one candidate (pregnancy-associated osteoporosis, rank 8) has any trial evidence, but it is Grade C relevance and the indication is excluded on safety grounds (Pregnancy Category X). Overall, this drug's current prediction set does not present a credible repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Raloxifene is **not currently registered or marketed in Singapore** (0 authorizations on file). No product-level licensing data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information — structured safety data (key warnings, contraindications, DDI) is currently a Data Gap (DG001, flagged **Blocking**), which prevents this candidate from entering formal S1 safety evaluation.

**Additional safety signals noted within the evidence pack's rationale narratives (not from structured safety data, included for awareness):**
- Raloxifene carries a known black-box warning for increased risk of venous thromboembolism and fatal stroke (observed in the RUTH trial).
- Raloxifene is Pregnancy Category X (teratogenic in animal studies) and is contraindicated in women who are or may become pregnant.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (duodenal ulcer) has no clinical trial or literature support and is assessed by the pack's own mechanistic analysis as likely model noise rather than a plausible biological signal. All 10 predicted indications for this drug are individually recommended "Hold," and a Blocking-severity data gap (TFDA/HSA warnings and contraindications) prevents any progression to safety evaluation.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official package insert / regulatory warnings and contraindications before any S1 safety screening.
- Resolve DG002 (High): obtain confirmed MOA data from DrugBank to properly assess mechanistic plausibility.
- If pursuing repurposing for this drug at all, prioritize re-screening for indications with stronger biological rationale (e.g., lipid-related or bone-related conditions) rather than the current top-ranked candidate.
- No further evidence collection (trial/literature search) is recommended for duodenal ulcer given the lack of biological plausibility already identified.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

