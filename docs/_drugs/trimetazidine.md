---
layout: default
title: Trimetazidine
parent: 僅模型預測 (L5)
nav_order: 1018
evidence_level: L5
indication_count: 10
---

# Trimetazidine
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

# Trimetazidine: From Undocumented Original Indication to Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies

## One-Sentence Summary

> Trimetazidine (DrugBank DB09069) has no original indication or mechanism-of-action data on file in this evidence pack, and it is not currently marketed in Singapore.
> TxGNN's top-ranked prediction suggests potential effectiveness for **Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies**,
> but this is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale flags the direction as potentially contradictory rather than supportive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (drug not marketed in Singapore; no license record available) |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 98.83% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for trimetazidine is not available in this evidence pack (flagged as a High-severity data gap). However, the model's own rationale describes trimetazidine's known pharmacology: it inhibits the fatty-acid β-oxidation enzyme 3-ketoacyl-CoA thiolase (3-KAT), which forces cells to shift energy production toward glucose oxidation. This strategy depends on the downstream oxidative phosphorylation (OXPHOS) pathway being functionally intact.

This is precisely where the prediction becomes questionable: the target indication is an OXPHOS disorder caused by *nuclear DNA anomalies* — meaning the patient's OXPHOS machinery is already impaired. Blocking fatty-acid oxidation in such patients could theoretically deprive them of an alternative energy source they may be relying on, rather than helping. The evidence pack itself explicitly notes this as a "mechanistic direction conflict" (機轉方向矛盾), and no clinical trial or published literature exists to resolve or support the claim — the score is derived purely from the TxGNN network embedding.

Because no original indication data is on file for this drug in this evidence pack, we cannot assess similarity between the original and predicted indications. Notably, other lower-ranked predictions in this evidence pack (e.g., Ménière's disease / vertigo, ranks 2–5 and 7) are actually backed by real historical literature, including two 1990s double-blind comparative trials against betahistine — a stronger and more coherent evidence base than the top-ranked candidate discussed here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Trimetazidine is not currently marketed in Singapore, and no drug licenses/authorizations are on file for this product in the evidence pack (total registrations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: Regulatory-source label warnings and contraindications for trimetazidine were not available at the time of this report (flagged as a **Blocking** data gap — DG001), which by itself is sufficient to prevent progression past the initial safety screening stage regardless of efficacy evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by a raw TxGNN model score (L5), with zero clinical trials or publications, and the model's own mechanistic reasoning suggests the drug's fatty-acid oxidation-inhibiting action could be counterproductive — or even harmful — in patients whose OXPHOS pathway is already compromised by nuclear DNA defects. Combined with a Blocking-severity gap in regulatory safety data, this indication does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Official label warnings and contraindications (TFDA/HSA) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- Preclinical or mechanistic studies specifically addressing whether fatty-acid oxidation inhibition is safe in OXPHOS-deficient patients, to resolve the identified mechanistic contradiction
- Consider redirecting evaluation resources toward the endolymphatic hydrops / Ménière's disease candidate (rank 2), which already has double-blind trial literature and a coherent, non-contradictory mechanistic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

