# Cholecalciferol: From Vitamin D Deficiency to Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion

---

## One-Sentence Summary

Cholecalciferol (Vitamin D3) is a well-established fat-soluble prohormone primarily used worldwide to prevent and treat vitamin D deficiency, rickets, and osteomalacia, though it is not currently registered as a pharmaceutical product in Singapore.
The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion** with a prediction score of **99.79%**;
however, there are currently **0 clinical trials** and **0 directly relevant publications** supporting this specific rare disease indication, placing the evidence firmly at **Level L4 (mechanistic prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin D deficiency, rickets, osteomalacia (internationally recognized use; not currently registered in Singapore) |
| Predicted New Indication | Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cholecalciferol (Vitamin D3) is a fat-soluble prohormone that requires two sequential hydroxylation steps to become biologically active. After absorption or cutaneous synthesis, it is converted in the liver to 25-hydroxyvitamin D (calcidiol, 25(OH)D), which then undergoes 1α-hydroxylation in the kidneys — catalyzed by CYP27B1 (1α-hydroxylase) — to produce 1,25-dihydroxyvitamin D3 (calcitriol), the active hormone. Calcitriol binds to the nuclear Vitamin D Receptor (VDR), a transcription factor expressed in over 30 tissues, regulating intestinal calcium and phosphate absorption, renal calcium reabsorption, PTH suppression in the parathyroid glands, and bone mineralization. Crucially, **the renal 1α-hydroxylation step is directly stimulated by PTH** — meaning that Cholecalciferol's conversion to active calcitriol is tightly coupled to PTH signaling.

Familial isolated hypoparathyroidism due to impaired PTH secretion is a rare genetic disorder in which parathyroid glands fail to secrete adequate PTH, causing hypocalcemia, hyperphosphatemia, and a relative deficiency of calcitriol. The TxGNN model's high prediction score reflects genuine biochemical proximity: PTH deficiency reduces renal CYP27B1 activity, creating a functional vitamin D activation bottleneck for which Cholecalciferol supplementation theoretically provides substrate. Additionally, extrarenal 1α-hydroxylase activity exists in macrophages, monocytes, and some epithelial cells — independent of PTH — offering an alternative conversion route. These are the mechanistic arguments the knowledge graph captures.

However, this reasoning has a critical limitation: because PTH is the primary driver of renal 1α-hydroxylation, the conversion efficiency of Cholecalciferol to calcitriol is substantially impaired in this exact patient population. This is precisely why clinical guidelines for hypoparathyroidism universally recommend **active vitamin D analogs (calcitriol or alfacalcidol)** that bypass the PTH-dependent activation step entirely, rather than Cholecalciferol as a precursor. The TxGNN prediction captures broad vitamin D–calcium axis node connectivity in the knowledge graph, but does not reflect disease-specific clinical utility. No clinical trial or dedicated literature evidence supports Cholecalciferol as a treatment for this rare genetic subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cholecalciferol in familial isolated hypoparathyroidism due to impaired PTH secretion.

---

## Literature Evidence

Currently no related literature available for Cholecalciferol specifically in familial isolated hypoparathyroidism due to impaired PTH secretion.

---

## Singapore Market Information

Cholecalciferol (DrugBank ID: DB00169) is not currently registered as a licensed pharmaceutical product with the Health Sciences Authority (HSA) of Singapore. No product authorizations were identified in the regulatory dataset (data cutoff: 2026-04-04).

> Cholecalciferol is widely available globally as an over-the-counter nutritional supplement and is included in numerous national pharmacopeias and essential medicines lists. Its absence from Singapore's pharmaceutical registration data likely reflects classification as a health supplement or nutraceutical in this market, which falls outside the pharmaceutical licensing pathway captured in this dataset. This is a known gap in the regulatory data layer rather than an indication of unavailability.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is high (99.79%), this reflects mechanistic overlap between Cholecalciferol and the calcium/PTH regulatory axis rather than disease-specific clinical evidence. For familial isolated hypoparathyroidism due to impaired PTH secretion specifically, the principal pharmacological barrier is the same PTH deficiency that defines the disease — which directly impairs the conversion of Cholecalciferol to its active form. Zero supporting clinical trials or literature exist for this indication (L4 evidence), and established clinical practice favors active vitamin D analogs. A Hold decision is appropriate until additional mechanistic and pharmacokinetic data in this patient population can be gathered.

**To proceed, the following is needed:**

- **Mechanistic clarification (DG002):** Retrieve full MOA and pharmacokinetic profile from DrugBank, specifically confirming the magnitude of extrarenal 1α-hydroxylase activity achievable in hypoparathyroid patients
- **Safety profile (DG001):** Obtain Singapore/TFDA package insert to document warnings, contraindications, and hypercalcemia/hypercalciuria risk thresholds
- **Targeted literature review:** Search for 25(OH)D supplementation outcomes specifically in hypoparathyroidism cohorts, and any case reports of Cholecalciferol as adjunct to calcitriol in this population
- **Clinical question refinement:** Determine whether the research hypothesis is Cholecalciferol as *monotherapy* (unlikely to be efficacious) or as *adjunct* to active vitamin D to achieve optimal 25(OH)D stores — the latter is more scientifically defensible
- **Rare disease consultation:** Engage with endocrinology specialists managing hypoparathyroidism to assess unmet need and practical feasibility of any exploratory protocol

---

> **Analyst Note — Broader Repurposing Landscape:** Among all 10 predicted indications in this evidence pack, the top-ranked indication by TxGNN score (rank #1, this report) carries the *lowest* evidence level. Review teams should be aware that **impaired renal function disease (CKD)** — ranked #10 by TxGNN score (98.40%) — represents a substantially stronger repurposing signal with **Evidence Level L2**, multiple Phase 2–4 RCTs directly testing Cholecalciferol in CKD patients (including PMID 40342405, 35657784, 26432706), and a **"Proceed with Guardrails"** recommendation. If program prioritization is the goal, CKD represents the most immediately actionable opportunity in this dataset. Similarly, **hypophosphatemic rickets** (rank #5, L3) and **renal tubular acidosis** (rank #7, L3) offer case-report and observational evidence supporting a mechanistic role for Cholecalciferol. A multi-indication evaluation strategy across ranks #5–#10 may be more productive than focusing solely on the highest TxGNN-scored prediction.

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content complies with YMYL medical disclaimer standards.*