---
layout: default
title: Calcium Gluconate
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 10
---

# Calcium Gluconate
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

# Calcium Gluconate: From Calcium Supplementation to Calcium-Alkali Syndrome

## One-Sentence Summary

Calcium gluconate is a calcium salt used globally as an emergency treatment for hypocalcemia, cardiac membrane stabilization in severe hyperkalemia, and general calcium supplementation — it currently has no registered products in Singapore.
The TxGNN model predicts it may be effective for **Calcium-Alkali Syndrome** (top prediction, score 98.88%), but a critical directional error has been identified: calcium gluconate is a known *causative agent* of this syndrome, not a therapeutic candidate.
Across all 10 predicted indications, no clinical trial directly tests calcium gluconate as a treatment, and the only partially defensible research direction is **hypophosphatemia** (Rank 4, Evidence Level L3), where intravenous calcium gluconate is used as adjunctive supportive care.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not formally registered in Singapore; established clinical use for hypocalcemia treatment and calcium supplementation |
| Predicted New Indication | Calcium-Alkali Syndrome |
| TxGNN Prediction Score | 98.88% |
| Evidence Level | L5 (model prediction only; no direct supporting studies) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Calcium gluconate is the gluconate salt of calcium, dissociating to provide free calcium ions (Ca²⁺) upon administration. Intravenously, it is the preferred form for rapidly correcting life-threatening hypocalcemia, stabilizing cardiac membranes during severe hyperkalemia, and managing hydrofluoric acid toxicity. Orally, it functions as a dietary calcium supplement. Its pharmacological role is fundamentally that of an elemental calcium donor.

**Calcium-alkali syndrome** (historically known as milk-alkali syndrome) is defined by the clinical triad of hypercalcemia, metabolic alkalosis, and renal impairment, arising specifically from excessive ingestion of calcium and absorbable alkali. Calcium gluconate — as a direct and potent source of calcium ions — is mechanistically a **causative agent** of this syndrome, not a therapeutic option. A patient with calcium-alkali syndrome who receives additional calcium gluconate would be expected to deteriorate, not improve. The model's high prediction score (98.88%) almost certainly reflects the strong co-occurrence of the calcium node with calcium-alkali syndrome nodes in the TxGNN knowledge graph, a directional artifact rather than a true therapeutic signal.

This directional confusion appears to extend across multiple ranked predictions. Urolithiasis (Rank 9) and dyspepsia (Rank 3) are conditions where calcium administration can worsen pathology (hypercalciuria accelerates stone formation; calcium stimulates gastrin secretion and may aggravate acid-related conditions). Potassium deficiency disease (Rank 5) is a direction error in the opposite sense — calcium gluconate's established electrolyte role is in **hyperkalemia** management, not hypokalemia. Among all 10 predictions, the only indication where calcium gluconate has a partial, evidence-supported role is **hypophosphatemia** (Rank 4), where intravenous calcium gluconate is used as supportive therapy for comorbid hypocalcemia occurring in hungry bone syndrome and denosumab-induced mineral imbalance.

---

## Clinical Trial Evidence

No clinical trials directly testing calcium gluconate for calcium-alkali syndrome were identified. All 42 trials retrieved in the database search were classified as relevance grade C — unrelated to both the drug and the target indication (studies included HIV antiretroviral trials, cardiology biomarker studies, and unrelated metabolic disease trials).

Currently no related clinical trials registered for this indication-drug combination.

---

## Literature Evidence

Currently no related literature available for calcium gluconate in the treatment of calcium-alkali syndrome.

---

## Singapore Market Information

Calcium gluconate (DrugBank ID: DB11126) currently has no registered pharmaceutical products in Singapore. No product authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN top prediction (calcium-alkali syndrome, 98.88%) contains a fundamental directional error — calcium gluconate is the etiological agent of this syndrome, not a treatment. This pattern repeats across most of the top 10 predictions, suggesting the TxGNN knowledge graph is conflating strong co-occurrence of calcium-related nodes with therapeutic utility. At current evidence levels (L5 for 7 of 10 predictions), no repurposing pathway can be responsibly advanced.

**To proceed, the following is needed:**

- **Directional error audit of the TxGNN pipeline**: Distinguish calcium-as-cause from calcium-as-treatment signals in the knowledge graph before interpreting any high-scoring predictions for this drug
- **Re-evaluate Rank 4 (Hypophosphatemia, L3)** as the most defensible research direction: human case reports (PMID 39839473: hungry bone syndrome after parathyroidectomy in XLH; PMID 36859300: denosumab-induced hypocalcemia post-bariatric surgery) document intravenous calcium gluconate use as adjunctive supportive therapy in hypophosphatemia-associated mineral imbalance states — however, this is adjunctive care for comorbid hypocalcemia, not a primary treatment of hypophosphatemia itself, limiting its value as a formal repurposing claim
- **Retrieve full MOA and safety data**: DrugBank API query for mechanism of action, and TFDA/HSA package insert review for warnings and contraindications, are blocking prerequisites before any clinical pathway evaluation
- **Singapore regulatory pathway assessment**: No current Singapore registration exists; any clinical application would require HSA product registration as a prerequisite
- **Consider excluding this candidate** from further repurposing prioritization unless a mechanistically novel application (beyond calcium replacement) can be identified and substantiated with prospective evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

