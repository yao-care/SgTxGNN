---
layout: default
title: Amiloride Hcl
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 0
---

# Amiloride Hcl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Amiloride HCL: Drug Repurposing Candidate — Insufficient Evidence Pack for Full Analysis

## One-Sentence Summary

Amiloride HCL is a potassium-sparing diuretic agent belonging to the pyrazine class, classically used in the management of hypertension and fluid retention.
However, the current Evidence Pack contains **no predicted new indications** from the TxGNN model, and the drug is **not registered in Singapore**.
Due to critical data gaps across regulatory, mechanistic, and predictive domains, a complete repurposing evaluation cannot be performed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — Model prediction absent; no supporting studies retrievable |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on publicly known pharmacology, Amiloride HCL is a potassium-sparing diuretic that blocks epithelial sodium channels (ENaC) in the distal nephron, thereby preventing sodium reabsorption while sparing potassium. It has historically been used in combination with other diuretics to manage hypertension, congestive heart failure, and liver cirrhosis with ascites.

No predicted repurposing direction has been returned by the TxGNN model in this Evidence Pack. This may be due to the absence of a DrugBank ID mapping, which is required for the TxGNN knowledge graph traversal. Without a valid DrugBank node, the model cannot generate scored candidate indications.

No further mechanistic-to-indication reasoning can be completed until the TxGNN pipeline successfully maps this drug and returns prediction results.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

---

## Singapore Market Information

Amiloride HCL has **no current product registrations** with the Health Sciences Authority (HSA) of Singapore. No authorisation records are available for this drug.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline was unable to generate repurposing predictions for Amiloride HCL, most likely because no DrugBank ID was resolved for this compound. Without predictions, mechanism data, or Singapore regulatory history, there is no viable repurposing case to evaluate at this stage.

**To proceed, the following is needed:**

- **Resolve DrugBank ID**: Query the DrugBank API using the INN "amiloride" (without the HCl salt suffix) to retrieve `DB00594` or equivalent entry; this is the prerequisite for TxGNN knowledge graph traversal
- **Re-run TxGNN prediction**: Once the DrugBank node is mapped, re-execute the KG and DL prediction pipelines to generate scored candidate indications
- **Retrieve MOA data**: Pull mechanism of action details from the DrugBank API to enable mechanistic plausibility assessment
- **Source package insert**: Download the SmPC or equivalent from a regulatory authority (e.g., EMA, FDA, or TFDA) to populate key warnings and contraindications
- **Check off-label research literature**: Even without TxGNN predictions, PubMed and ClinicalTrials.gov can be manually queried for known investigational uses of amiloride (e.g., cystic fibrosis, Liddle syndrome, cancer sodium channel studies)
- **Consider HSA registration pathway**: If a repurposing indication is identified, assess whether a parallel import or new registration is feasible given the current zero-registration status in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

