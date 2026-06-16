---
layout: default
title: Etelcalcetide
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 10
---

# Etelcalcetide
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

# Etelcalcetide: From Secondary Hyperparathyroidism to Hyperphosphatemia

## One-Sentence Summary

Etelcalcetide is a novel intravenous calcimimetic agent approved for the management of secondary hyperparathyroidism (SHPT) in adult patients with chronic kidney disease (CKD) on hemodialysis.
The TxGNN model predicts it may be effective for **Hyperphosphatemia**, with **1 clinical trial** and **3 publications** currently supporting this direction.
The mechanistic rationale is biologically plausible: CaSR activation suppresses PTH, which in turn reduces bone resorption and phosphate release into the circulation — a pathway highly relevant to the CKD-mineral bone disorder (CKD-MBD) spectrum.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Secondary hyperparathyroidism in CKD patients on hemodialysis |
| Predicted New Indication | Hyperphosphatemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L2 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Etelcalcetide is an intravenous calcimimetic that acts as an agonist of the calcium-sensing receptor (CaSR), primarily expressed on parathyroid chief cells. By binding to CaSR, it amplifies the receptor's sensitivity to extracellular calcium, thereby suppressing parathyroid hormone (PTH) secretion. Reduced PTH in turn decreases osteoclast-driven bone resorption — one of the key sources of phosphate release into the bloodstream in CKD patients.

The connection between SHPT and hyperphosphatemia is not incidental: in patients with CKD on hemodialysis, both conditions co-exist as part of the CKD-MBD syndrome, driven by the same underlying failure of renal phosphate excretion and disordered mineral metabolism. CaSR is also expressed in proximal renal tubular cells, where it may directly modulate phosphate reabsorption, providing an additional biological mechanism beyond PTH suppression.

Importantly, existing clinical trials of etelcalcetide in the SHPT setting routinely measure phosphate as a secondary endpoint. The body of evidence thus captures hyperphosphatemia outcomes indirectly, even when it is not the primary trial endpoint. No Phase 3 RCT has yet targeted hyperphosphatemia as the primary endpoint for etelcalcetide, which explains why the evidence level is L2 rather than L1 — the efficacy signal is real but captured as a secondary outcome within SHPT trials.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03527511](https://clinicaltrials.gov/study/NCT03527511) | N/A | Completed | 21 | Mechanistic study evaluating the effect of etelcalcetide combined with active vitamin D on osteoclast activity in CKD patients; addresses CKD-MBD components including hyperphosphatemia and hyperparathyroidism, though phosphate reduction is not the primary endpoint |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33305109](https://pubmed.ncbi.nlm.nih.gov/33305109/) | 2020 | RCT | Kidney International Reports | DUET Trial: prospective RCT evaluating etelcalcetide efficacy in hemodialysis patients with SHPT; demonstrated effective PTH reduction with CKD-MBD management including phosphate control as part of multilateral treatment strategy |
| [29440923](https://pubmed.ncbi.nlm.nih.gov/29440923/) | 2018 | Review | International Journal of Nephrology and Renovascular Disease | Comprehensive review of SHPT management in hemodialysis; discusses etelcalcetide's role as an IV calcimimetic given thrice weekly, with PTH and phosphate co-management as core therapeutic goals; compares with cinacalcet |
| [33211001](https://pubmed.ncbi.nlm.nih.gov/33211001/) | 2021 | Case Report | Clinical Nephrology | Case of metastatic pulmonary calcification in a dialysis patient with SHPT; illustrates the clinical consequences of uncontrolled CKD-MBD including ectopic calcification driven by sustained hyperphosphatemia and hyperparathyroidism |

---

## Singapore Market Information

Etelcalcetide currently has **no registered products** in Singapore. The drug is not marketed and no Health Sciences Authority (HSA) authorization records are available.

> **Note for clinical teams:** Etelcalcetide (brand name: Parsabiv®) is approved in the United States (FDA, 2017) and the European Union (EMA, 2016) for secondary hyperparathyroidism in adults with CKD on hemodialysis. Any use in Singapore would require an import licence or special access pathway.

---

## Safety Considerations

Detailed safety data (warnings, contraindications, and drug interaction records) was not retrievable for this Evidence Pack. Based on the drug's known pharmacology and clinical use:

- **Hypocalcemia** is the most clinically significant risk of CaSR agonists; etelcalcetide should not be initiated if serum calcium is below the lower limit of normal
- **QT prolongation** risk associated with hypocalcemia warrants ECG monitoring in at-risk patients
- **Paresthesia and muscle spasms** are common manifestations of hypocalcemia during treatment

Please refer to the current package insert (Parsabiv® prescribing information) for complete warnings, contraindications, and drug interaction guidance before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The prediction is mechanistically sound — hyperphosphatemia and SHPT share the same CKD-MBD pathophysiology, and etelcalcetide's PTH-lowering and potential direct tubular effects provide a biologically coherent basis for phosphate reduction. An RCT (DUET Trial) and supporting review literature confirm clinically meaningful effects in the same patient population, with phosphate as a documented secondary outcome. The gap is the absence of a trial that designates hyperphosphatemia as the primary endpoint.

**To proceed, the following is needed:**

- **MOA documentation**: Obtain full DrugBank MOA profile for etelcalcetide to formalize mechanism-of-action rationale in regulatory submissions
- **Package insert safety data**: Download and parse the Parsabiv® prescribing information to complete contraindication and warning fields (currently blocking S1 safety evaluation)
- **Singapore import pathway assessment**: Confirm whether HSA Special Access Route or similar mechanism is available for clinical use, given no local registration
- **Phosphate-as-primary-endpoint trial identification**: Search for any ongoing trials where hyperphosphatemia is the primary endpoint (not only secondary) to determine if Phase 3 evidence can be anticipated
- **Calcium monitoring protocol**: Define a pre-specified hypocalcemia monitoring plan as a guardrail condition for any expanded use proposal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

