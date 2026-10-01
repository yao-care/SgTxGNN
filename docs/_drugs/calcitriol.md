---
layout: default
title: Calcitriol
parent: Low Evidence (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Calcitriol
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

# Calcitriol: From Active Vitamin D Therapy to Vitamin D Deficiency (Obsolete Ontology Term)

## One-Sentence Summary

Calcitriol is the active hormonal form of vitamin D, but the record does not list its original approved indication.
The TxGNN model's top-ranked prediction is **obsolete vitamin D deficiency**, an ontology term flagged as obsolete, so the score is likely a knowledge-graph artifact. It has **0 clinical trials** and **0 publications**.
Better-supported predictions are further down the list, especially **hereditary hypophosphatemic rickets** (6 trials, 20 publications).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA records (approved indication text is empty for all 4 licences) |
| Predicted New Indication | Obsolete vitamin D deficiency (top-ranked; see caveat below) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this record. Calcitriol is the active 1,25-dihydroxy form of vitamin D and acts as a vitamin D receptor (VDR) agonist, so a link to vitamin D-related disorders is biologically plausible.

The top-ranked term is flagged "obsolete" in the disease ontology. The very high score (99.96%) is therefore probably a knowledge-graph artifact. No trials or literature were retrieved, so this prediction should not be treated as a genuine repurposing signal.

The other predictions differ in strength:

| Rank | Predicted Indication | Score | Evidence Level | Decision |
|------|------|------|------|------|
| 2 | Renal tubular acidosis | 99.93% | L4 | Research Question |
| 3 | Familial isolated hypoparathyroidism (impaired PTH secretion) | 99.81% | L5 | Hold |
| 4 | Acromesomelic dysplasia, Campailla Martinelli type | 99.79% | L5 | Hold |
| 5 | Craniofacial conodysplasia | 99.78% | L5 | Hold |
| 6 | Dahlberg-Borer-Newcomer syndrome | 99.76% | L4 | Hold |
| 7 | Hereditary hypophosphatemic rickets | 99.28% | L3 | Proceed with Guardrails |
| 8 | Hypophosphatemic rickets | 98.08% | L3 | Proceed with Guardrails |
| 9 | Osteomalacia | 97.68% | L4 | Research Question |
| 10 | Vitamin D-dependent rickets | 97.42% | L3 | Research Question |

- **Hypophosphatemic rickets (ranks 7 and 8):** FGF23 excess lowers calcitriol synthesis and causes renal phosphate wasting. Calcitriol plus phosphate is a rational, long-established combination. This is close to existing standard care and is not novel repurposing. Rank 8 is the broader parent term and shares the same trials, so it is not independent evidence.
- **Vitamin D-dependent rickets (rank 10):** In type 1A, CYP27B1 mutations block conversion of 25-hydroxyvitamin D, so calcitriol bypasses the defect. Support comes from retrospective series, case reports and a systematic review. Response in type 2 (VDR defect) is variable and needs stratification.
- **Renal tubular acidosis (rank 2):** The rationale rests on correcting associated bone disease (osteomalacia), not on replacing a deficiency. One study reports that RTA does not alter circulating calcitriol.
- **Ranks 4 and 5:** These are skeletal dysplasias with no evident VDR-dependent mechanism, so they are not supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (obsolete vitamin D deficiency).

Trials retrieved for the best-supported candidate, **hereditary hypophosphatemic rickets** (rank 7):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Active, not recruiting | 20 | Calcitriol monotherapy (no phosphate) for one year in children and adults with XLH; outcomes are mineral ions, growth and skeletal parameters. Directly tests the drug, but is small and early-phase. |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | High versus low dose of active vitamin D combined with neutral phosphate in children with XLH. Relevant to dosing; no results available. |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | Active, not recruiting | 27 | ENERGY 3 study of INZ-701 in children with ENPP1 deficiency. A different investigational agent, so indirect for calcitriol. |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A | Completed | 260 | Observational study of inappropriate FGF23 secretion in hypophosphatemia. Pathophysiologic context only. |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | Not yet recruiting | 65 | Phosphorus-31 spectroscopy of ATP concentration in phosphate diabetes. Mechanistic, no calcitriol intervention. |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A | Unknown | 150 | Cross-sectional study of FGF23, Klotho and sclerostin in kidney stone formers. No calcitriol intervention. |

A withdrawn cinacalcet study (NCT00844740, n=0) was also retrieved; it is not about calcitriol and produced no data.

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction (obsolete vitamin D deficiency).

Key publications for **hereditary hypophosphatemic rickets / hypophosphatemic rickets** (ranks 7 and 8):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Review | Lancet | XLH review: PHEX defect raises FGF23, causing renal phosphate wasting and decreased calcitriol synthesis. |
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Review | Calcif Tissue Int | Diagnosis and therapy of XLH. |
| [30454743](https://pubmed.ncbi.nlm.nih.gov/30454743/) | 2019 | Review | Pediatr Clin North Am | Conventional treatment is phosphate plus calcitriol, requiring monitoring for adverse effects. |
| [26813507](https://pubmed.ncbi.nlm.nih.gov/26813507/) | 2016 | Review | Clin Calcium | FGF23-related rickets is treated with active vitamin D and phosphorus; does not target the underlying defect. |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical study | J Clin Invest | High-dose calcitriol plus phosphorus in five XLH patients, aimed at healing osteomalacia. |
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Clinical study | N Engl J Med | 11 children with vitamin D-resistant rickets; calcitriol raised circulating levels and increased intestinal phosphate absorption. |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Cohort | Pediatr Endocrinol Rev | Early calcitriol and phosphate therapy in 127 XLH patients from 49 centres. |
| [9316301](https://pubmed.ncbi.nlm.nih.gov/9316301/) | 1997 | Review | Acta Paediatr Jpn | Combined phosphate and calcitriol is the best current approach; complications include hypercalcemia, nephrocalcinosis and hyperparathyroidism. |

No randomised controlled trials were retrieved.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13449P | MEDITROL | Capsule, liquid filled | Not listed |
| SIN12258P | RASPUTIN SOFT CAPSULE 0.25 mcg | Capsule, liquid filled | Not listed |
| SIN03865P | ROCALTROL CAPSULE 0.25 mcg | Capsule, liquid filled | Not listed |
| SIN12160P | SILKIS OINTMENT 3 mcg/g | Ointment | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is an obsolete ontology term with no trials or literature, so its high score is most likely a graph artifact and cannot support a decision. Calcitriol is already established in hypophosphatemic rickets (L3, Proceed with Guardrails), but this is close to standard care rather than new repurposing. Safety and original-indication data are also missing.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (blocking for safety screening)
- Original approved indications and the mechanism of action from DrugBank
- Confirmation that the obsolete-term prediction is a knowledge-graph artifact, and re-prioritisation of the candidate list around rickets and related disorders
- For hypophosphatemic rickets, results from NCT03748966 and NCT03820518, and monitoring of calcium, phosphate, PTH and urinary calcium, with screening for nephrocalcinosis and hyperparathyroidism
- For vitamin D-dependent rickets and renal tubular acidosis, prospective data and stratification by disease subtype

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

