---
layout: default
title: Naphazoline
parent: 僅模型預測 (L5)
nav_order: 690
evidence_level: L5
indication_count: 10
---

# Naphazoline
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

# Naphazoline: From Topical Decongestant to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Naphazoline is an imidazoline-derived, non-selective α-adrenergic agonist used topically as a nasal/ocular vasoconstrictor to relieve congestion and redness. The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but currently **0 clinical trials** and **0 publications** support this direction — the prediction is a pure model score with no corroborating mechanistic or clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Taiwan-approved indication on record (drug not marketed); per available data, used as a topical nasal/ocular vasoconstrictor for congestion relief |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data for Naphazoline is not available in this evidence pack. Based on information captured elsewhere in the pack, Naphazoline is an imidazoline derivative and non-selective α-adrenergic receptor agonist (predominantly α1, with weak α2 activity), used clinically only as a topical vasoconstrictor of nasal mucosa/conjunctiva to relieve congestion.

For the top-ranked prediction — hypotrichosis simplex of the scalp — the evidence pack itself states there is no known pharmacological link: Naphazoline has no reported activity on hair follicle growth cycles, androgen receptor signaling, or keratinocyte pathways, and the pairing has zero supporting trials or literature. This is flagged as a pure TxGNN prediction score with no clinical evidence behind it.

Notably, across the 10 ranked predictions in this pack, TxGNN assigns similarly high scores to both hair-loss conditions (alopecia, hypotrichosis) and a hair-*excess* condition (hypertrichosis) — physiologically opposite directions. The pack's own rationale for rank 6 attributes this to a likely knowledge-graph clustering artifact around a shared "skin appendage" disease-embedding neighborhood rather than a genuine pharmacological signal. None of the 10 predicted indications have clinical trial support, and only two (open-angle glaucoma, and a periodontal malformation syndrome) returned any literature at all — and in both cases the retrieved literature does not actually concern Naphazoline itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (hypotrichosis simplex of the scalp) has no supporting clinical trials or literature and no plausible mechanistic link — it is a model score only (L5). The drug is also not currently marketed in Taiwan (0 registrations), and a Blocking data gap on TFDA label warnings/contraindications means safety cannot yet be assessed.

**To proceed, the following is needed:**
- Confirmed DrugBank/TFDA mechanism-of-action data for Naphazoline
- TFDA label (warnings, contraindications) to close the Blocking data gap
- Independent pharmacological or preclinical evidence linking α-adrenergic agonism to hair follicle biology before further investment in this indication
- Re-evaluation of lower-ranked candidates (e.g., open-angle glaucoma) only if drug-specific literature can be located, since current hits are off-target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

