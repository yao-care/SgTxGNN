---
layout: default
title: Imidapril
parent: 僅模型預測 (L5)
nav_order: 518
evidence_level: L5
indication_count: 10
---

# Imidapril
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

# Imidapril: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Imidapril is an angiotensin-converting enzyme (ACE) inhibitor with established use for hypertension and diabetic nephropathy in Japan, but it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension with Unclear Multifactorial Mechanism (WHO Group 5)**,
however, **no clinical trials or direct publications** currently support this specific indication — the evidence base is limited to model prediction alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Diabetic nephropathy (not registered in Singapore; approved in Japan) |
| Predicted New Indication | Pulmonary Hypertension with Unclear Multifactorial Mechanism |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Singapore drug registry. Based on information embedded in the Evidence Pack, Imidapril is an ACE inhibitor: it blocks the conversion of Angiotensin I to Angiotensin II, thereby reducing systemic vasoconstriction, aldosterone secretion, and blood pressure. Its efficacy in hypertension has been well established, and Japan has additionally approved it for diabetic nephropathy — a renal protective indication mediated by reduced glomerular capillary pressure downstream of ACE inhibition.

The proposed link to pulmonary hypertension with unclear multifactorial mechanism (WHO Group 5) rests on the observation that lower Angiotensin II levels may produce mild pulmonary vasodilation. This is a theoretically plausible but mechanistically weak argument. The core pathological drivers of WHO Group 5 pulmonary hypertension are largely independent of the renin-angiotensin system — the endothelin-1 (ET-1) axis and prostacyclin (PGI₂) axis are the recognised therapeutic targets in established pulmonary arterial hypertension, and ACE inhibitors do not meaningfully engage these pathways.

The TxGNN score of 99.78% almost certainly reflects structural proximity within the knowledge graph between hypertension-related disease nodes, rather than a direct pathophysiological connection to WHO Group 5 pulmonary hypertension. Notably, two other predicted indications from the same Evidence Pack carry meaningfully stronger mechanistic and empirical grounding: **malignant hypertensive renal disease** (Rank 4, L4 evidence; Imidapril's Japan diabetic nephropathy approval directly supports this pathway) and **cerebrovascular disorder** (Rank 7, L3 evidence; 14 publications including multiple Imidapril-specific preclinical studies in stroke-prone hypertensive rats).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note:** Although 20 PubMed records were retrieved for the related query "pulmonary hypertension owing to lung disease and/or hypoxia" (Rank 2 indication), none of these publications are specific to Imidapril or ACE inhibitors in pulmonary hypertension — they address general hypoxia biology and are not directly relevant to this repurposing hypothesis.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Detailed warnings, contraindications, and drug interaction data for Imidapril were not available in this Evidence Pack. As an ACE inhibitor class, general considerations include risk of hyperkalaemia, acute kidney injury in patients with bilateral renal artery stenosis, and ACE inhibitor–induced cough. Singapore regulatory label data should be sought from the Japan PMDA package insert as a proxy given the absence of HSA registration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or direct published evidence supporting Imidapril for pulmonary hypertension with unclear multifactorial mechanism, and the mechanistic link is weak — the core pathological drivers of WHO Group 5 pulmonary hypertension (ET-1, PGI₂ pathways) are not targeted by ACE inhibition. A high TxGNN algorithmic score alone is insufficient to justify further development in this direction.

**To proceed with any repurposing programme, the following is needed:**

- **MOA data**: Query DrugBank API (DB11783) to retrieve full mechanism of action, pharmacokinetics, and toxicity profile
- **Singapore regulatory data**: Obtain Japan PMDA package insert as proxy; extract warnings, contraindications, and approved dosing
- **Mechanistic feasibility study**: Commission a basic science review of ACE inhibitor effects specifically in Group 5 pulmonary hypertension animal models before committing investigational resources
- **Reprioritisation consideration**: Evidence Pack data suggest that **Rank 4 (Malignant Hypertensive Renal Disease, L4)** and **Rank 7 (Cerebrovascular Disorder, L3, 14 Imidapril-specific publications)** are substantially more tractable repurposing candidates and may warrant dedicated evaluation reports ahead of the Group 5 pulmonary hypertension hypothesis

---

*⚠️ Disclaimer: This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

