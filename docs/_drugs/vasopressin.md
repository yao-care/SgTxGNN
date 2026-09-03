---
layout: default
title: Vasopressin
parent: 僅模型預測 (L5)
nav_order: 1047
evidence_level: L5
indication_count: 10
---

# Vasopressin
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

# Vasopressin: From Unregistered Indication to Congenital Prothrombin Deficiency

## One-Sentence Summary

> Vasopressin (DrugBank DB00067) is an endogenous peptide hormone; no original indication text is available in the current evidence pack, and the drug is not registered in Singapore.
> The TxGNN model predicts a possible link to **Congenital Prothrombin Deficiency**, but the only supporting literature (3 papers) actually describes **desmopressin (DDAVP)** — a synthetic vasopressin analog, not vasopressin itself — used for factor V/VIII deficiency, with **no clinical trials** and **no direct mechanistic pathway** to prothrombin (factor II) synthesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty and no Singapore license text exists (drug unregistered) |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Vasopressin is not available in this evidence pack (`original_moa: [Data Gap]`). Based on general pharmacology, vasopressin acts on V1 (vascular smooth muscle, vasoconstriction), V2 (renal collecting duct, water reabsorption), and V1b (pituitary ACTH release) receptors — none of which are known to regulate hepatic synthesis of coagulation factor II (prothrombin).

The three supporting literature items for this prediction all describe **desmopressin (DDAVP)**, a synthetic analog of vasopressin with selective V2-receptor activity, used to raise circulating factor VIII/von Willebrand factor levels in acquired or congenital factor V/VIII deficiency. This is a distinct drug from vasopressin itself, and none of the cases involve factor II (prothrombin). The TxGNN association therefore appears to be driven by drug-class similarity (vasopressin ↔ desmopressin) and disease-cluster proximity within the coagulation-disorder space, rather than by a validated mechanistic pathway specific to prothrombin deficiency.

Given the absence of a plausible mechanism and the complete absence of clinical trial evidence, this prediction should be treated as a hypothesis-generating signal only, not a basis for clinical or regulatory action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Review of acquired hemophilia A (factor VIII autoantibodies); does not involve vasopressin or prothrombin |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case Report | Rinsho Ketsueki | DDAVP (desmopressin) used in combined congenital factor V/VIII deficiency, not vasopressin or factor II |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case Report | Rinsho Ketsueki | Factor VIII concentrate + DDAVP management during cesarean section in combined factor V/VIII deficiency |

---

## Singapore Market Information

No registration record was found for Vasopressin in the Singapore evidence pack (`market_status: 未上市`, `total_licenses: 0`). The drug currently has no marketed license and no approved indication text on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (congenital prothrombin deficiency) is supported only by literature describing a *different drug* (desmopressin) in a *different disease* (factor V/VIII deficiency), with no clinical trials and no plausible mechanism linking vasopressin to prothrombin synthesis. All 10 predicted indications in this evidence pack carry a "Hold" recommendation; several (drug-induced osteoporosis, orofacial clefting syndrome, testicular tumors) have zero supporting evidence, and one (cystic neoplasm/ADPKD) is mechanistically **contradictory** — the supporting trials actually involve Tolvaptan, a vasopressin V2-receptor *antagonist*, whose therapeutic action is the opposite of vasopressin agonism.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for vasopressin from DrugBank/pharmacology references
- HSA/TFDA package insert data (warnings, contraindications, DDI) — currently a Blocking data gap per `DG001`
- Independent pharmacological verification distinguishing vasopressin from desmopressin before treating any factor-deficiency literature as supportive evidence
- Re-screening of all 10 candidates against mechanistic plausibility before any candidate advances past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

