---
layout: default
title: Alfacalcidol
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Alfacalcidol
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

# Alfacalcidol: From Hypoparathyroidism to Familial Isolated Hypoparathyroidism due to Impaired PTH Secretion

## One-Sentence Summary

Alfacalcidol (1α-hydroxycholecalciferol) is a synthetic active vitamin D analog used for metabolic bone diseases including renal osteodystrophy and hypoparathyroidism, where it bypasses the renal activation step to directly provide active vitamin D.
The TxGNN model predicts it may be effective for the rare genetic subtype **Familial Isolated Hypoparathyroidism due to Impaired PTH Secretion**, with a prediction score of **99.61%**.
No clinical trials or publications targeting this specific genetic subtype were identified; the evidence rating of L4 reflects the rarity of this entity rather than weak pharmacological rationale — the mechanistic link to alfacalcidol is among the strongest possible, as active vitamin D analogs are already the established backbone of hypoparathyroidism management.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Renal osteodystrophy, osteoporosis, hypoparathyroidism (general indications) |
| Predicted New Indication | Familial Isolated Hypoparathyroidism due to Impaired PTH Secretion |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available from the current dataset. Based on established pharmacological knowledge, alfacalcidol is a synthetic prodrug of vitamin D that undergoes 25-hydroxylation in the liver to produce calcitriol (1,25-dihydroxyvitamin D₃) — the biologically active form. Critically, alfacalcidol **bypasses the renal 1α-hydroxylation step**, which is the rate-limiting and PTH-dependent bottleneck in vitamin D activation. This distinguishes it from plain vitamin D supplements and makes it particularly suited to situations where PTH signalling is absent or impaired.

In familial isolated hypoparathyroidism due to impaired PTH secretion, inadequate or absent PTH fails to upregulate renal 1α-hydroxylase (encoded by *CYP27B1*), resulting in insufficient calcitriol synthesis, hypocalcemia, hyperphosphatemia, and neuromuscular irritability. Alfacalcidol circumvents this deficiency entirely — it does not require PTH to be activated. The drug provides active vitamin D directly, restoring calcium absorption and suppressing the downstream consequences of PTH insufficiency. This is precisely the pharmacological rationale underpinning the use of active vitamin D analogs as the standard of care for all forms of hypoparathyroidism.

The TxGNN prediction score of 99.61% is scientifically coherent. The absence of publications specifically targeting this rare genetic subtype (PTH-secretion–impaired familial isolated hypoparathyroidism) reflects its extreme rarity in published literature, not a lack of biological plausibility. The mechanism that justifies alfacalcidol in surgical or autoimmune hypoparathyroidism applies equally to this PTH-secretion–impaired genetic form. The L4 evidence rating is a data gap artefact, not a biological verdict.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication.

---

## Literature Evidence

Currently no related literature available for this specific genetic subtype (familial isolated hypoparathyroidism due to impaired PTH secretion).

> **Context note:** Extensive literature exists supporting alfacalcidol and calcitriol in hypoparathyroidism broadly (surgical, autoimmune, and genetic forms). The absence of subtype-specific publications reflects the extreme rarity of this genetic entity. See the Renal Tubular Acidosis and Parathyroid Hyperplasia predictions (Ranks 5 and 8) in this pack for supporting literature on alfacalcidol's role in closely related calcium-phosphate disorders.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data were not available in the current dataset (DrugBank query returned no safety records; TFDA package insert data was not retrieved). Before clinical application, hypercalcemia and hypercalciuria monitoring are known concerns with all active vitamin D analogs and should be incorporated into any treatment protocol.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for alfacalcidol in this indication is essentially the same as for hypoparathyroidism broadly — a disease category in which alfacalcidol is already established standard of care — and the TxGNN model has correctly identified the PTH-secretion–impaired genetic subtype as pharmacologically equivalent. The absence of subtype-specific clinical trial data reflects disease rarity, not a failure of therapeutic logic, and does not justify "Hold" when the underlying pharmacology is so well characterised.

**To proceed, the following is needed:**

- **Retrieve MOA and safety data:** Query DrugBank API for DB01436 to obtain full mechanism of action, contraindications, and key warnings; download and parse TFDA/HSA package insert PDF
- **Design a prospective case series or patient registry:** Enrol genetically confirmed PTH-secretion–impaired hypoparathyroidism patients to document dosing, calcium/phosphate targets, and outcomes
- **Define safety monitoring protocol:** Establish regular monitoring parameters (serum calcium, phosphate, urinary calcium/creatinine ratio, renal function, eGFR) given the known hypercalcemia/hypercalciuria risk of active vitamin D analogs
- **Assess dosing specificity:** Determine whether dosing requirements differ between this genetic subtype and surgical or autoimmune hypoparathyroidism, particularly in paediatric patients where disease onset may be earlier
- **Explore Singapore registration pathway:** Alfacalcidol is currently unregistered in Singapore (0 authorizations); if clinical use is pursued, a regulatory submission with supporting international evidence will be required
- **Consider PTH replacement as comparator:** rhPTH(1-84) (natpara) is emerging as an alternative; a comparative effectiveness framework should be outlined in any prospective study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

