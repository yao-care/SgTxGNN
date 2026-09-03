---
layout: default
title: Potassium Chloride
parent: 僅模型預測 (L5)
nav_order: 803
evidence_level: L5
indication_count: 10
---

# Potassium Chloride
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

Using the Evidence Pack (candidate TW-DB00761-multi, v4, cutoff 2026-07-14) to generate the pharmacist evaluation report for the top-ranked TxGNN prediction (renal tubular acidosis). Note the raw JSON key is `taiwan_regulatory`, but per the report template this maps to "Singapore Market Status" in this deployment context.

---

# Potassium Chloride: From Potassium Supplementation to Renal Tubular Acidosis

## One-Sentence Summary

> Potassium chloride (DrugBank DB00761) is a basic electrolyte agent generally used for potassium supplementation/correction of hypokalemia; the evidence pack itself contains no locally registered original-indication text, since the drug is currently **not marketed in Singapore** (0 registrations).
> The TxGNN model predicts it may be effective for **Renal Tubular Acidosis (RTA)**, with **9 related clinical trials** and **19 supporting publications** currently identified — though none directly test KCl itself in an RCT for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Potassium supplementation / correction of hypokalemia (general pharmacologic use — no Singapore label text available; `original_indications` field empty in source data) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap in the source pack). Based on known pharmacology, potassium chloride is a direct electrolyte-replacement agent used to correct potassium deficiency; its efficacy in treating hypokalemia of any cause is well established, and mechanistically it may be applicable to Renal Tubular Acidosis, a condition in which chronic hypokalemia is a defining feature.

In distal (Type 1) RTA, impaired H⁺ secretion by the distal tubule triggers a compensatory renal potassium loss (kaliuresis), producing chronic hypokalemia that frequently requires long-term correction. Potassium salts (most commonly potassium citrate or potassium bicarbonate, with KCl as an alternative supplementation source) are already part of standard clinical practice for managing RTA-associated hypokalemia and acidosis — so the mechanistic link here is direct and clinically intuitive rather than a novel biological hypothesis.

It is important to note the limitation acknowledged in the evidence pack's own rationale: this represents an **existing clinical practice pattern being surfaced by the model**, not a genuinely new indication, and there remains a lack of prospective RCT evidence testing KCl specifically (as opposed to citrate or bicarbonate salts) for RTA. The identified clinical trials are mostly indirect (alkali therapy in other diseases, related electrolyte-management studies) rather than head-to-head KCl trials in RTA populations.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03644706](https://clinicaltrials.gov/study/NCT03644706) | Phase 3 | Terminated | 3 | Randomized withdrawal study of ADV7103 vs. placebo in preventing metabolic acidosis in dRTA; terminated early with only 3 subjects enrolled, limiting statistical power. |
| [NCT01894594](https://clinicaltrials.gov/study/NCT01894594) | Phase 1 | Terminated | 7 | Alkali (sodium bicarbonate) repletion tested for effect on serum bicarbonate and potassium in Sickle Cell Disease patients with low bicarbonate — mechanistically analogous to RTA alkalinization/potassium correction, but different disease population. |
| [NCT03354507](https://clinicaltrials.gov/study/NCT03354507) | N/A (pilot) | Unknown | 40 | Sodium bicarbonate used to alkalinize serum/urine in pediatric patients with topiramate-induced renal tubular acidosis — supports the alkalinization/electrolyte-correction rationale relevant to RTA management. |
| [NCT00120731](https://clinicaltrials.gov/study/NCT00120731) | N/A | Withdrawn (n=0) | 0 | Directly tested potassium citrate (same drug class as KCl) for urinary chemistry/acid-base effects in children with hypercalciuria and urolithiasis — highly relevant mechanistically, but withdrawn with no data generated. |
| [NCT06867471](https://clinicaltrials.gov/study/NCT06867471) | N/A | Recruiting | 43 | Evaluates exogenous ketosis effects on proteinuria/renal function in CKD and polycystic kidney disease — only tangential relevance to KCl or acid-base correction. |
| [NCT01843309](https://clinicaltrials.gov/study/NCT01843309) | Phase 4 | Terminated | 36 | Spironolactone (potassium-sparing diuretic) tested to prevent Amphotericin B–related electrolyte abnormalities — different mechanism (renal potassium retention vs. supplementation). |
| [NCT01834768](https://clinicaltrials.gov/study/NCT01834768) | Phase 2 | Unknown | 31 | Safety of eplerenone (mineralocorticoid receptor antagonist) in cyclosporine-treated transplant recipients — no direct KCl/RTA relevance. |
| [NCT07273838](https://clinicaltrials.gov/study/NCT07273838) | Phase 2 | Not yet recruiting | 130 | SGLT2 inhibitor for acute cardiorenal syndrome — no mechanistic link to KCl or RTA. |
| [NCT06750172](https://clinicaltrials.gov/study/NCT06750172) | N/A | Recruiting | 33 | Methodology study on urinary aldosterone measurement for diagnosing primary aldosteronism — diagnostic, not a treatment trial; no KCl relevance. |

*Overall assessment: no trial in this set directly evaluates KCl as a therapeutic intervention for RTA. The most relevant trials (potassium citrate in urolithiasis, alkali therapy in SCD, bicarbonate in topiramate-induced RTA) support the general mechanistic class but were underpowered, withdrawn, or conducted in different patient populations.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [783200](https://pubmed.ncbi.nlm.nih.gov/783200/) | 1976 | Cohort | The Journal of Clinical Investigation | Classic study in 10 patients with classic (distal) RTA where acidosis correction was sustained using oral **potassium bicarbonate**, demonstrating that potassium-salt correction is a long-established therapeutic approach in this disease. |
| [8694660](https://pubmed.ncbi.nlm.nih.gov/8694660/) | 1996 | Review | Archives of Internal Medicine | Reviews RTA pathophysiology and diagnosis; confirms serum potassium and urinary electrolyte assessment as central to diagnosis and subtype classification. |
| [33459628](https://pubmed.ncbi.nlm.nih.gov/33459628/) | 2021 | Review | Archivos Españoles de Urología | Reviews RTA diagnosis and management, including distal RTA's characteristic hypokalemia and the role of alkali/potassium therapy in preventing nephrocalcinosis and stones. |
| [17297212](https://pubmed.ncbi.nlm.nih.gov/17297212/) | 2007 | Review | Acta Medica Indonesiana | General review of hypokalemia approach, including renal causes of potassium loss such as RTA, and principles of potassium replacement. |
| [38445406](https://pubmed.ncbi.nlm.nih.gov/38445406/) | 2023 | Cohort | La Tunisie Médicale | Genotype-phenotype correlation study of distal RTA, describing the hypokalemia and hypocitraturia phenotype requiring ongoing electrolyte management. |
| [14048071](https://pubmed.ncbi.nlm.nih.gov/14048071/) | 1963 | Review | Medical Bulletin (Ann Arbor) | Early foundational review describing RTA and its management, historically including potassium replacement as supportive therapy. |
| [37081692](https://pubmed.ncbi.nlm.nih.gov/37081692/) | 2023 | Review | Endocrine Journal | Reviews classification of pseudohypoaldosteronism type II as type IV RTA, relevant to the broader potassium/acid-base disorder spectrum (note: type IV RTA is hyperkalemic, opposite direction from KCl supplementation need). |
| [21314872](https://pubmed.ncbi.nlm.nih.gov/21314872/) | 2011 | Review (pending formal classification) | International Journal of Clinical Practice | Clinical approach to RTA in adults, covering the three major RTA subtypes and their differing potassium abnormalities (both hypo- and hyperkalemic forms exist). |
| [3518609](https://pubmed.ncbi.nlm.nih.gov/3518609/) | 1986 | Review (pending formal classification) | Annual Review of Medicine | Comprehensive review of the clinical spectrum of RTA, distinguishing proximal RTA, hypokalemic distal RTA, and hyperkalemic distal RTA. |
| [20228475](https://pubmed.ncbi.nlm.nih.gov/20228475/) | 2010 | Case Report (pending formal classification) | Neurology India | Case of RTA presenting as respiratory paralysis due to severe hypokalemia (1.6 mEq/L); patient improved following sodium bicarbonate **and potassium supplementation**, directly illustrating the clinical rationale for KCl-class therapy. |

*Note: all identified literature is Review/Cohort/Case-Report level; no RCT specifically testing KCl for RTA was found, consistent with the L3 (observational/review-level) evidence rating.*

---

## Singapore Market Information

Potassium chloride currently holds **no product registration in Singapore** (0 authorizations recorded in the evidence pack). No brand name, dosage form, or approved indication text is available for this market at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(The evidence pack's `key_warnings`, `contraindications`, and drug-interaction fields are all marked as data gaps, and the DDI database query returned no results — DG001 in the source pack flags local package-insert warnings/contraindications as a Blocking-severity gap for safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale connecting potassium chloride to Renal Tubular Acidosis is strong and well grounded in established clinical practice (RTA causes chronic renal potassium wasting that is routinely corrected with potassium salts), supported by multiple reviews and a classic cohort study using potassium bicarbonate. However, no trial or publication tests KCl specifically in an RCT for RTA, the drug is not currently marketed in Singapore, and core drug-level safety data (MOA, local package-insert warnings/contraindications) are missing — together these place the evidence at L3 and warrant guardrails before any clinical repositioning decision.

**To proceed, the following is needed:**
- Detailed mechanism of action data for potassium chloride (DG002 — query DrugBank API)
- Singapore/regional package insert warnings and contraindications (DG001 — Blocking; required before any S1 safety pre-assessment can proceed)
- Clarification of whether "renal tubular acidosis" here should be evaluated against KCl specifically or the broader potassium-salt drug class (citrate/bicarbonate), since most supporting evidence uses non-KCl potassium salts
- A regulatory pathway assessment given the drug currently has zero registrations in Singapore
- Formal safety/DDI database review, since the automated DDI query returned no data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

