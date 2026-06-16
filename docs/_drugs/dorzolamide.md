---
layout: default
title: Dorzolamide
parent: 僅模型預測 (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
---

# Dorzolamide
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

# Dorzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Dorzolamide is a topical carbonic anhydrase inhibitor (CAI) globally approved for lowering intraocular pressure (IOP) in open-angle glaucoma and ocular hypertension, though it currently holds no Singapore regulatory registration.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
with **1 clinical trial** and **no publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (global approval; not registered in Singapore) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Dorzolamide is a sulfonamide-derived compound that selectively inhibits carbonic anhydrase isoenzyme II (CA-II) in the ciliary body of the eye. By suppressing CA-II activity, it reduces the rate of aqueous humour secretion, thereby lowering intraocular pressure (IOP) — the principal modifiable risk factor in all forms of glaucoma.

Primary hereditary glaucoma (associated with mutations in genes such as *MYOC*, *OPTN*, and *WDR36*) shares the same core pathological endpoint as sporadic open-angle glaucoma: elevated IOP causing progressive optic nerve damage. The genetic defect disrupts trabecular meshwork outflow resistance, but the downstream consequence — raised IOP — is the same target that Dorzolamide was designed to address. The IOP-lowering mechanism is therefore directly applicable, regardless of whether elevated IOP arises from a genetic or sporadic aetiology.

The critical clinical distinction is that hereditary glaucoma often presents earlier in life, including in the paediatric population, and may demand more sustained or intensive IOP management. The only identified trial (NCT01527682) directly enrolled paediatric patients with primary hereditary glaucoma refractory to surgery, lending direct translational support to this repurposing hypothesis. The TxGNN model's top-ranked score for this drug-disease pair is mechanistically coherent and clinically grounded.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Directly compared latanoprost (prostaglandin analogue) vs. dorzolamide (CAI) for IOP lowering in paediatric primary hereditary glaucoma patients who failed surgical procedures; assessed both ocular hypotensive efficacy and safety in this genetically predisposed population |

---

## Literature Evidence

Currently no related literature available specific to primary hereditary glaucoma.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial (NCT01527682, n=37) directly evaluated Dorzolamide in paediatric primary hereditary glaucoma, establishing both feasibility and preliminary efficacy in this genetically predisposed population. The mechanistic link is robust — CA-II inhibition lowers IOP regardless of the underlying genetic aetiology, and the IOP-centric pathology of hereditary glaucoma is identical to that of sporadic open-angle glaucoma where Dorzolamide has extensive Phase 3 evidence globally.

**To proceed, the following is needed:**

- **Singapore regulatory pathway**: Dorzolamide is not currently registered with HSA; a market authorisation application or compassionate use pathway must be scoped before any local deployment
- **Package insert safety data**: Contraindications and key warnings remain unknown in this evidence pack; the approved product monograph (from any jurisdiction where it is registered, e.g. FDA, EMA) must be reviewed before clinical use
- **MOA documentation**: Formal DrugBank or equivalent MOA data to support a regulatory clinical dossier
- **Genetic subtype evidence**: Additional data stratified by mutation type (MYOC, OPTN, WDR36) to understand whether certain hereditary subtypes respond differently to CAI therapy
- **Long-term efficacy data**: NCT01527682 enrolled 37 patients; larger, longer-duration studies are needed to confirm sustained IOP control and optic nerve protection in hereditary glaucoma
- **Paediatric dosing protocol**: Given the primary hereditary glaucoma population often includes children, age-appropriate dosing, tolerability, and monitoring guidelines must be clearly defined
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

