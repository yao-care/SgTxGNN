---
layout: default
title: Timolol
parent: 僅模型預測 (L5)
nav_order: 982
evidence_level: L5
indication_count: 10
---

# Timolol
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

Using the drug-repurposing report template to generate the Timolol (DB00373) evaluation report from the supplied Evidence Pack.

---

# Timolol: From Glaucoma/Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

> Timolol is a non-selective beta-adrenergic blocker with established use in glaucoma/ocular hypertension and systemic hypertension, though the Singapore regulatory dataset in this pack contains no license record for it (currently **not marketed** in Singapore).
> The TxGNN model's top-ranked prediction suggests it may be effective for **Primary Hereditary Glaucoma**,
> but currently only **1 mismatched clinical trial** and **0 publications** directly support this specific candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the Singapore regulatory dataset (no licenses on file); Timolol is internationally established for glaucoma/ocular hypertension and hypertension |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Timolol is not available in this Evidence Pack. Based on known pharmacology, Timolol is a non-selective β1/β2-adrenergic receptor antagonist; topically it reduces aqueous humor production by ciliary epithelium β2-receptor blockade, lowering intraocular pressure (IOP), and systemically it is used to lower blood pressure and reduce cardiac workload.

Primary hereditary glaucoma (e.g., primary congenital/juvenile open-angle glaucoma) shares the same core pathophysiology as general open/closed-angle glaucoma — impaired aqueous outflow leading to elevated IOP — so a β2-blockade mechanism is theoretically transferable to this genetic subtype. This is mechanistically plausible on paper.

However, the single clinical trial attached to this specific prediction (NCT02484716) is **not actually about glaucoma** — it studies topical nasal Timolol for epistaxis in Hereditary Hemorrhagic Telangiectasia (HHT), an unrelated vascular bleeding disorder. This appears to be a mismatched evidence pairing (likely driven by keyword overlap on "hereditary" rather than a genuine mechanistic or clinical link to hereditary glaucoma). No literature is available to support the pairing either. Consequently, while the theoretical mechanistic rationale is reasonable, direct empirical support for this precise indication is effectively absent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02484716](https://clinicaltrials.gov/study/NCT02484716) | Phase 2 | Completed | 58 | Randomized trial of intranasal Timolol spray vs. placebo for epistaxis in Hereditary Hemorrhagic Telangiectasia (HHT). **Not related to hereditary glaucoma** — evidence relevance graded C ("unrelated pairing") by the underlying screening process. |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Timolol has no registered product license in the Singapore dataset used for this analysis (`total_licenses: 0`, market status: Not Marketed). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: this Evidence Pack flags a **Blocking** data gap — TFDA-equivalent label warnings/contraindications for Timolol are not yet retrieved, which by itself prevents completion of the S1 safety pre-screen for any indication, including this one.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical trial linked to this specific prediction is unrelated to hereditary glaucoma (it studies HHT-associated epistaxis), there is no supporting literature, and a **Blocking** safety data gap (missing warnings/contraindications) currently prevents entry into the S1 safety pre-assessment stage. Timolol is also not currently marketed in Singapore, so there is no local regulatory or safety-monitoring foundation to build on.

**To proceed, the following is needed:**
- Retrieve TFDA/Singapore-equivalent package insert warnings and contraindications (removes the Blocking gap)
- Confirm Timolol's mechanism of action via DrugBank API query
- Source clinical trials or literature that specifically address primary hereditary glaucoma (not proxy conditions or keyword-matched but clinically unrelated trials)
- Assess feasibility/rationale for Singapore market registration, since the drug currently has zero local licenses

**Additional note for reviewers:** within the same Evidence Pack, other TxGNN-predicted indications for Timolol — open-angle glaucoma (rank 9), closed-angle glaucoma (rank 2), and angle-closure glaucoma (rank 10) — reach **Evidence Level L1** with multiple Phase 3/4 RCTs and dozens of publications, and are flagged "Proceed with Guardrails." These act as useful internal positive controls confirming the model correctly recovers well-established glaucoma uses, but do not add support to the specific "primary hereditary glaucoma" candidate evaluated above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

