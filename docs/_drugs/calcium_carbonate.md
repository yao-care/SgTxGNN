---
layout: default
title: Calcium Carbonate
parent: Low Evidence (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Calcium Carbonate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Calcium carbonate: From Antacid to Calcium-Alkali Syndrome

## One-Sentence Summary

Calcium carbonate is a widely used antacid and calcium supplement. The Singapore products are all marketed as antacids, and the registration data give no approved indication text.
The TxGNN model predicts a link to **calcium-alkali syndrome** with a high score (93.2%), but this condition is an **adverse effect of excess calcium carbonate intake**, not a treatable disease. The evidence (**1 clinical trial**, an unrelated drug-interaction study, and **16 publications**, mostly reviews and case reports of harm) does not support a therapeutic use. The score most likely reflects a "drug causes disease" association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antacid (inferred from product names; approved indication text is not provided in the registration data) |
| Predicted New Indication | Calcium-alkali syndrome |
| TxGNN Prediction Score | 93.16% |
| Evidence Level | L4 (reviews and case reports of harm only; no therapeutic studies) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, calcium carbonate acts as an acid-neutralizing antacid and calcium source, and its use in acid-related symptoms is long established.

Calcium-alkali syndrome (formerly milk-alkali syndrome) is the triad of hypercalcemia, metabolic alkalosis, and renal impairment. It is caused by ingesting large amounts of calcium carbonate, historically to treat peptic ulcer disease. A knowledge-graph model can score a strong link between a drug and a disease even when the drug causes that disease, and this appears to be the case here.

In short, the link is real but runs in the wrong direction for repurposing. The literature describes the syndrome as a risk of over-the-counter antacid and calcium supplement use, particularly in older adults, in pregnancy, and alongside thiazide diuretics. This is a safety signal to monitor, not a new indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01622673](https://clinicaltrials.gov/study/NCT01622673) | Phase 1 | Completed | 27 | Effect of calcium carbonate and magnesium/aluminum hydroxide antacids on raltegravir pharmacokinetics in HIV-infected participants. A drug-interaction study that does not address calcium-alkali syndrome. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33732556](https://pubmed.ncbi.nlm.nih.gov/33732556/) | 2021 | Review | Cureus | Historical review and update of calcium-alkali syndrome. Incidence fell after H2 blockers and PPIs but has re-emerged with calcium supplement use. |
| [26260640](https://pubmed.ncbi.nlm.nih.gov/26260640/) | 2015 | Review | The Consultant Pharmacist | Guidance for pharmacists on identifying at-risk geriatric patients and on prevention and monitoring. |
| [23543983](https://pubmed.ncbi.nlm.nih.gov/23543983/) | 2013 | Review | Proc (Baylor Univ Med Cent) | Milk-alkali syndrome has evolved into calcium-alkali syndrome, now a common cause of hypercalcemia and alkalosis. |
| [38784190](https://pubmed.ncbi.nlm.nih.gov/38784190/) | 2024 | Case report | Obstetric Medicine | Severe hypercalcemia needing dialysis in an early twin pregnancy after calcium carbonate use for reflux and nausea. |
| [41444901](https://pubmed.ncbi.nlm.nih.gov/41444901/) | 2025 | Case report | Annals of General Psychiatry | Over-the-counter calcium carbonate overdose causing milk-alkali syndrome in a psychiatric patient. |
| [36712775](https://pubmed.ncbi.nlm.nih.gov/36712775/) | 2022 | Case report | Cureus | Hypercalcemic crisis associated with calcium carbonate (Tums). |
| [33842126](https://pubmed.ncbi.nlm.nih.gov/33842126/) | 2021 | Case report | Cureus | Acute kidney injury from overconsumption of calcium carbonate, treated with hemodialysis. |
| [25874082](https://pubmed.ncbi.nlm.nih.gov/25874082/) | 2012 | Case report | Clinical Kidney Journal | Hypercalcemic crisis in an elderly man on calcium supplements, facilitated by a thiazide diuretic and an ACE inhibitor. |
| [32675162](https://pubmed.ncbi.nlm.nih.gov/32675162/) | 2020 | Case report | Clinical Medicine (London) | Severe hypercalcaemia, staghorn calculus and renal impairment from long-term over-the-counter calcium carbonate antacids. |
| [38404648](https://pubmed.ncbi.nlm.nih.gov/38404648/) | 2024 | Case report | Case Reports in Endocrinology | Severe hypercalcemia from calcium-alkali syndrome in a patient with postoperative hypoparathyroidism on calcium carbonate and calcitriol. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05820P | OHTA'S ISAN ANTACID POWDER | Powder | Not stated in registration data |
| SIN08733P | RENNIE TABLET | Tablet | Not stated in registration data |
| SIN14016P | GAVISCON DOUBLE ACTION LIQUID, SUSPENSION | Suspension | Not stated in registration data |
| SIN13738P | GAVISCON LIQUID SACHETS | Suspension | Not stated in registration data |
| SIN13947P | GAVISCON PEPPERMINT TABLETS | Tablet, chewable | Not stated in registration data |

Eight registrations exist in total; five are shown.

---

## Safety Considerations

Package insert warnings and contraindications were not available. The points below come from the retrieved literature only.

- **Hypercalcemia risk with excess intake**: High or prolonged calcium carbonate intake is linked to calcium-alkali syndrome (hypercalcemia, metabolic alkalosis, acute kidney injury). Reported at-risk groups include older adults, pregnant women, and patients with hypoparathyroidism.
- **Drug interactions**: Case reports describe higher hypercalcemia risk alongside thiazide diuretics and ACE inhibitors. A Phase 1 study examined the effect of calcium carbonate antacids on raltegravir pharmacokinetics.

Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is an adverse effect of the drug, not a treatable condition, and no study supports therapeutic use. The high TxGNN score should not be read as repurposing potential.

**To proceed, the following is needed:**
- Reclassify this prediction as a safety signal for pharmacovigilance and patient counselling, not as a repurposing candidate.
- Package insert warnings and contraindications from the HSA, and mechanism of action data.
- Separately review other predictions with L3 evidence, namely gastroduodenitis, hyperlipidemia, and peptic ulcer disease. Gastroduodenitis and peptic ulcer overlap with existing antacid use. Hyperlipidemia has small older studies, and its trials were nutrition studies that cannot be attributed to calcium carbonate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

