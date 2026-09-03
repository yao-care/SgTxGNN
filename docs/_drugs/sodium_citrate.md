---
layout: default
title: Sodium Citrate
parent: 僅模型預測 (L5)
nav_order: 911
evidence_level: L5
indication_count: 10
---

# Sodium Citrate
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

# Sodium Citrate: From Undocumented Original Indication to Papillary Conjunctivitis

## One-Sentence Summary

> This evidence pack contains no confirmed original indication, formal mechanism-of-action record, or Singapore market registration for sodium citrate (DB09154).
> The TxGNN model's top-ranked prediction links it to **Papillary Conjunctivitis**,
> but this connection is supported by **0 clinical trials** and **0 publications** — a pure knowledge-graph inference with no pharmacological grounding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no DrugBank original indication or Singapore license record available) |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.95% (rank 1200) |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available (data gap DG002). Based on the limited information in this evidence pack, sodium citrate is described as functioning pharmacologically as a **calcium-chelating agent and alkalinizing agent**. No formal DrugBank MOA record, drug class assignment, or original indication was provided to establish what condition this pharmacology has been validated for.

Without a documented original indication, there is no basis for comparing disease-mechanism overlap between sodium citrate's established use and papillary conjunctivitis. The evidence pack's own rationale for this candidate states explicitly that there is **no known mechanistic link** between a calcium chelator/alkalinizing agent and papillary conjunctivitis — the TxGNN score reflects graph-embedding similarity only, not a pharmacological hypothesis.

Because this is the top-ranked candidate by TxGNN score but the weakest by supporting evidence, it should not be interpreted as the strongest repurposing opportunity in this batch — it is simply the highest graph-similarity score among ten candidates screened for this drug.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

No Singapore market authorization is on file. `taiwan_regulatory.market_status` is recorded as **未上市 (Not Marketed)**, with `total_licenses = 0` and no license entries in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as data gaps in this evidence pack — notably, data gap **DG001** flags TFDA/HSA package-insert warnings and contraindications as **Blocking**, meaning this candidate cannot proceed to an S1 safety pre-assessment until that data is obtained.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (papillary conjunctivitis) is an L5 candidate — model inference only, with zero clinical trial or literature support and no plausible mechanistic link per the evidence pack's own rationale. Combined with the drug's unregistered status in Singapore and missing MOA/safety data, there is no basis to advance this specific candidate.

**To proceed, the following is needed:**
- TFDA/HSA package-insert warnings and contraindications (Blocking gap DG001) — required before any S1 safety pre-assessment
- DrugBank mechanism-of-action detail (gap DG002) to support or refute mechanistic plausibility
- Confirmation of sodium citrate's original approved indication(s), since none are on file
- If further repurposing work on sodium citrate is warranted, prioritize the higher-evidence candidates already surfaced in this same batch rather than the top TxGNN-ranked one — specifically **stomach disease** (L4, S1, 3 in-vitro mechanistic studies on sodium citrate's anti-gastric-cancer glycolysis-inhibition effect) and **intestinal obstruction** (L3, S1, an RCT on the related citrate salt choline citrate for postoperative ileus), both of which currently carry more substantive, drug-specific evidence than papillary conjunctivitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

