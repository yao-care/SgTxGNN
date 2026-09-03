---
layout: default
title: Terlipressin
parent: 僅模型預測 (L5)
nav_order: 960
evidence_level: L5
indication_count: 10
---

# Terlipressin
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

# Terlipressin: From Portal Hypertension Bleeding to Open-Angle Glaucoma

## One-Sentence Summary

> Terlipressin is a vasopressin V1-receptor agonist used internationally for esophageal variceal hemorrhage and hepatorenal syndrome in cirrhosis.
> TxGNN predicts it may be effective for **Open-Angle Glaucoma** with a very high score (99.78%),
> but this prediction is currently supported by **zero clinical trials** and **zero publications**, and the drug's known vasoconstrictive mechanism runs counter to the direction needed to lower intraocular pressure.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; internationally indicated for esophageal variceal bleeding and hepatorenal syndrome in cirrhosis (per literature context in this evidence pack) |
| Predicted New Indication | Open-Angle Glaucoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Terlipressin is not available in this evidence pack (DrugBank MOA field is a data gap). Based on contextual information from trial and literature summaries collected across the ranked candidates, Terlipressin is a long-acting synthetic analog of vasopressin acting as a V1-receptor agonist, producing splanchnic (and systemic) vasoconstriction. It is used clinically to reduce portal pressure in variceal bleeding and to improve renal perfusion in hepatorenal syndrome.

Open-angle glaucoma management generally requires **reducing** intraocular pressure, typically through improved aqueous outflow or reduced aqueous production. Terlipressin's vasoconstrictive action does not have an established mechanistic pathway toward this goal — and could plausibly work in the opposite direction. This is explicitly noted in the evidence pack's own rationale: *"Terlipressin為血管收縮劑，理論上可能升高而非降低眼壓，與青光眼治療方向相反。"*

Given the absence of any clinical trial or literature evidence, and a mechanistic rationale that actively argues against efficacy, this top-ranked TxGNN hit is most likely an artifact of indirect knowledge-graph associations (e.g., shared nodes related to vascular/ocular blood flow) rather than a genuine biological signal. This pattern — very high model score but a mechanistically implausible link with no corroborating evidence — is a strong indicator of a false-positive prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Terlipressin currently has no marketing authorizations recorded in Singapore (0 registrations, market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are all currently data gaps for this product — see DG001 in the evidence pack, which is flagged as Blocking for safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Open-Angle Glaucoma) has no clinical trial or literature support, and its proposed mechanism plausibly opposes the therapeutic goal of lowering intraocular pressure. With no corroborating evidence and a contradictory mechanistic rationale, this does not meet the bar to advance past model-prediction stage (L5/S0).

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (resolves DG001 — currently Blocking for any safety pre-assessment)
- Confirmed mechanism of action via DrugBank API (resolves DG002)
- If pursuing repurposing further, note that a **more scientifically plausible signal exists lower in the ranked list**: rank 3, **Pulmonary Hypertension** (score 99.56%, evidence level L3, decision stage S1, recommendation "Research Question"), supported by cohort studies showing Terlipressin reduces pulmonary vascular resistance in cirrhotic patients with portopulmonary hypertension (e.g., PMID 22893473, 21733953, 18280605). This candidate is mechanistically coherent (vasoconstriction improving pulmonary hemodynamics in a hepatic-vascular context) and may warrant prioritization over the current top-ranked glaucoma hit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

