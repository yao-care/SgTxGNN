---
layout: default
title: Calcium Carbonate
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Calcium Carbonate
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

# Calcium Carbonate: From Antacid / Calcium Supplement to Calcium-Alkali Syndrome

## One-Sentence Summary

Calcium carbonate (CaCO₃) is a widely used over-the-counter agent serving as an antacid and calcium supplement, with established use in acid reflux relief and osteoporosis prevention.
The TxGNN model predicts a strong association with **Calcium-Alkali Syndrome (CAS)**, supported by **1 clinical trial** (indirectly related) and **16 publications** — however, existing evidence consistently identifies CaCO₃ as the **primary causative agent** of CAS, not a therapeutic option.
This is an **iatrogenic association** rather than a repurposing opportunity, and the prediction score should be interpreted as a pharmacovigilance signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indications in Singapore (not marketed) |
| Predicted New Indication | Calcium-Alkali Syndrome |
| TxGNN Prediction Score | 93.16% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Calcium carbonate is a simple inorganic salt that dissolves in stomach acid via the reaction CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂, releasing calcium ions (Ca²⁺) and bicarbonate (HCO₃⁻). Its two primary clinical roles are acid neutralization (antacid) and elemental calcium provision (supplement for bone health). Detailed mechanism of action data from DrugBank was not available in this Evidence Pack; the pharmacology described here reflects established scientific consensus.

Calcium-Alkali Syndrome is defined by the triad of **hypercalcemia, metabolic alkalosis, and acute kidney injury**. The pathophysiological cascade triggered by excess CaCO₃ ingestion is: elevated calcium intake → hypercalcemia → renal calcium deposition → declining GFR → bicarbonate accumulation → worsening metabolic alkalosis → further impairment of renal calcium excretion. This is a self-reinforcing loop in which CaCO₃ is the **etiological trigger**. The syndrome was historically known as Milk-Alkali Syndrome, first described in patients treated with calcium carbonate for peptic ulcer disease, and has seen a modern resurgence driven by high-dose calcium supplementation for osteoporosis.

**Critical Interpretation of the TxGNN Score**: The model's high prediction score (93.16%) reflects a genuine and well-documented mechanistic link between CaCO₃ and CAS in the knowledge graph. However, this link is **causative rather than therapeutic** — the drug produces the disease under conditions of overuse. This prediction does not open a conventional repurposing pathway; rather, it surfaces a high-priority drug safety signal. CAS is currently the third most common cause of hypercalcemia in the United States, after primary hyperparathyroidism and malignancy, and its connection to OTC calcium carbonate remains underappreciated among prescribers and patients alike.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01622673](https://clinicaltrials.gov/study/NCT01622673) | Phase 1 | Completed | 27 | Evaluated effect of co-administering calcium carbonate antacid on the pharmacokinetics of raltegravir (HIV treatment) — CaCO₃ was studied as an interacting antacid, not as a CAS treatment; no direct relevance to CAS management |

> **Note**: No clinical trials directly investigating the treatment or prevention of Calcium-Alkali Syndrome with calcium carbonate were identified. The single retrieved trial assessed CaCO₃ as a confounding antacid in an HIV drug interaction study.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [33732556](https://pubmed.ncbi.nlm.nih.gov/33732556/) | 2021 | Review | *Cureus* | Comprehensive historical review and updated pathophysiology of CAS; CaCO₃ identified as the key causative agent; modern incidence driven by calcium supplementation for osteoporosis |
| [23543983](https://pubmed.ncbi.nlm.nih.gov/23543983/) | 2013 | Review | *Proc (Baylor Univ Med Ctr)* | Documents the resurgence of CAS as a modern counterpart to milk-alkali syndrome; describes clinical features, diagnostic criteria, and management principles |
| [26260640](https://pubmed.ncbi.nlm.nih.gov/26260640/) | 2015 | Review | *Consult Pharmacist* | Pharmacist-focused guide for identifying geriatric patients at risk for CAS; emphasises prevention strategies and calcium intake monitoring thresholds |
| [33178509](https://pubmed.ncbi.nlm.nih.gov/33178509/) | 2020 | Review | *Cureus* | Describes Calcium-Alkali-Thiazide Syndrome; co-administration of thiazide diuretics markedly amplifies CAS risk from CaCO₃; CAS accounts for higher proportion of hypercalcaemia than previously estimated |
| [41444901](https://pubmed.ncbi.nlm.nih.gov/41444901/) | 2025 | Case Report | *Ann Gen Psychiatry* | OTC CaCO₃ overdose in a psychiatric patient causing milk-alkali syndrome; highlights vulnerability of patients with limited health literacy to inadvertent CAS from self-medicated antacids |
| [38784190](https://pubmed.ncbi.nlm.nih.gov/38784190/) | 2024 | Case Report | *Obstetric Medicine* | Severe CAS at 14-week twin gestation; patient had taken CaCO₃ for pregnancy-related nausea from week 5; presented with severe hypercalcemia, metabolic alkalosis, renal injury; required ICU admission and dialysis |
| [38404648](https://pubmed.ncbi.nlm.nih.gov/38404648/) | 2024 | Case Report | *Case Rep Endocrinol* | CAS after 15 years of routine CaCO₃ + calcitriol therapy for post-thyroidectomy hypoparathyroidism; undiagnosed hyperaldosteronism acted as a precipitating comorbidity |
| [36712775](https://pubmed.ncbi.nlm.nih.gov/36712775/) | 2022 | Case Report | *Cureus* | Life-threatening hypercalcaemic crisis directly attributed to CaCO₃ (Tums) ingestion; emphasises that OTC availability does not equate to unlimited safety |
| [33842126](https://pubmed.ncbi.nlm.nih.gov/33842126/) | 2021 | Case Report | *Cureus* | Hypercalcemia and acute kidney injury from CaCO₃ (Tums) overconsumption; treatment required hemodialysis; highlights under-recognition of CAS in acute settings |
| [32675162](https://pubmed.ncbi.nlm.nih.gov/32675162/) | 2020 | Case Report | *Clin Med (London)* | Long-standing OTC CaCO₃ antacid use (~1,800 mg elemental calcium/day) causing severe hypercalcaemia, staghorn renal calculus, and renal impairment; concurrent antihypertensive acted as amplifier |

---

## Singapore Market Information

Calcium carbonate (DB06724) is currently **not registered or marketed in Singapore**. No HSA drug licenses were identified in the regulatory database.

> For reference to approved formulations, consult regulatory filings in jurisdictions where CaCO₃ products are registered (e.g., US FDA, European Medicines Agency). Standard OTC products include Tums® (calcium carbonate 500–750 mg tablets) and Os-Cal® (calcium carbonate 1,250 mg tablets) in the United States.

---

## Safety Considerations

Please refer to standard pharmacological references and package inserts from approved jurisdictions for complete safety information.

**Key safety signals identified from this evidence review:**

- **Calcium-Alkali Syndrome risk**: Excessive or prolonged CaCO₃ ingestion can cause the triad of hypercalcaemia, metabolic alkalosis, and acute kidney injury. Populations at elevated risk include:
  - Postmenopausal women on high-dose calcium supplements for osteoporosis
  - Patients concurrently using thiazide diuretics (Calcium-Alkali-Thiazide Syndrome)
  - Patients with pre-existing renal impairment
  - Pregnant women using CaCO₃ for nausea or reflux
  - Patients with hypoparathyroidism on long-term CaCO₃ + calcitriol replacement therapy

- **Acid rebound**: CaCO₃ stimulates gastrin secretion via released calcium ions, which can paradoxically increase gastric acid secretion after the initial neutralizing effect — a consideration for long-term antacid use.

- **Drug interactions**: CaCO₃ is a divalent cation antacid that can chelate and reduce absorption of co-administered medications (e.g., fluoroquinolones, tetracyclines, thyroid hormones, integrase inhibitors such as raltegravir).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's high-scoring association between calcium carbonate and Calcium-Alkali Syndrome accurately reflects a mechanistically robust drug-disease relationship, but the direction of that relationship is **causative, not therapeutic** — CaCO₃ induces CAS under conditions of overuse, making this a pharmacovigilance finding rather than a repurposing candidate.

**To proceed productively, the following is recommended:**

- **Reframe the clinical question**: If the intent is to leverage this finding, explore a **safety monitoring protocol** for patients on long-term CaCO₃, rather than a therapeutic repurposing pathway.
- **Evaluate alternative predicted indications**: Ranks 7 (Gastroduodenitis, L3, *Proceed with Guardrails*) and 9 (Peptic Ulcer Disease, L3, *Proceed with Guardrails*) represent mechanistically sound and clinically actionable repurposing directions consistent with calcium carbonate's established pharmacology as an antacid.
- **Obtain full MOA data from DrugBank** to support mechanistic rationale for any alternative indication.
- **Clarify Singapore regulatory pathway**: Since CaCO₃ is not currently registered in Singapore, any clinical application would require an HSA new drug registration or notification submission.
- **Establish safe upper dosing thresholds**: Define calcium intake ceilings to prevent CAS in populations identified above, drawing on reviewed literature to set evidence-based monitoring parameters.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

