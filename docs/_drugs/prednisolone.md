---
layout: default
title: Prednisolone
parent: 僅模型預測 (L5)
nav_order: 812
evidence_level: L5
indication_count: 10
---

# Prednisolone
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

# Prednisolone: From Corticosteroid Anti-Inflammatory Therapy to Alopecia Areata

## One-Sentence Summary

> Prednisolone is a systemic corticosteroid broadly used for anti-inflammatory and immunosuppressive therapy across many conditions, though no formal Singapore-approved indication is on record for this drug.
> The TxGNN model predicts it may be effective for **Alopecia Areata**,
> with **18 clinical trials** and **20 publications** identified in the evidence pack (relevance varies — see evidence tables below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (0 licenses on file); generally used as a systemic corticosteroid for anti-inflammatory/immunosuppressive therapy |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for prednisolone is not available in the DrugBank record used for this evidence pack. However, based on well-established pharmacology, prednisolone is a systemic glucocorticoid that suppresses T-cell activation and reduces release of pro-inflammatory cytokines (e.g., IL-2, IFN-γ).

Alopecia areata (AA) is a T-cell-mediated, organ-specific autoimmune disease in which immune cells attack hair follicles in their normally immune-privileged state. Because prednisolone's core mechanism directly dampens the T-cell-driven inflammatory attack underlying AA, this is not a novel mechanistic hypothesis — it aligns with an already-established dermatologic practice known as "pulse corticosteroid therapy," which has been used clinically for AA for decades. In this sense, the TxGNN prediction reinforces existing clinical practice rather than proposing an entirely new use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Completed | 42 | Oral mega-pulse methylprednisolone evaluated in severe, treatment-resistant AA to test whether higher/more frequent dosing overcomes non-response |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Unknown | 20 | Compared corticosteroid delivery via DERMOJET (needle-free) vs. standard syringe injection for AA lesions |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A | Completed | 296 | Observational safety/efficacy study of tofacitinib with or without adjuvant prednisolone in alopecia patients |
| [NCT06759519](https://clinicaltrials.gov/study/NCT06759519) | N/A | Completed | 621 | Multicenter observational study (retrospective/prospective) describing a moderate-to-severe AA patient population |

*Note: Several additional trials in the source evidence pack target systemic lupus erythematosus with non-corticosteroid biologics (e.g., baricitinib, anifrolumab) and were graded low-relevance (Grade C) — these are excluded above as they do not test prednisolone in AA.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | RCT (placebo-controlled) | J Am Acad Dermatol | First placebo-controlled trial of oral pulse prednisolone in AA |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network Meta-Analysis | Cochrane Database Syst Rev | Comparative efficacy of AA treatments including immunosuppressants and steroids |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | Systematic Review | Australas J Dermatol | Systematic review of systemic treatments for AA, alopecia totalis, and universalis |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | Efficacy and adverse effects of corticosteroid pulse therapy in AA |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | Cohort | Dermato-Endocrinology | Medium-dose prednisolone pulse therapy shown effective in early-stage AA |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Retrospective Cohort | Dermatol Ther | Methylprednisolone alone vs. combined with methotrexate in extensive AA |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Retrospective Review | Pediatr Dermatol | Review of pulse-dose corticosteroid dosing regimens in pediatric AA |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | Case Series | J Dtsch Dermatol Ges | Sequential high- then low-dose systemic corticosteroids in severe childhood AA |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Cohort | Dermatol Ther | Combined oral pulse + topical corticosteroid, long-term follow-up in children with severe AA |
| [22426909](https://pubmed.ncbi.nlm.nih.gov/22426909/) | 2012 | Case Series | Saudi Med J | Efficacy/safety of oral mega-pulse methylprednisolone in severe therapy-resistant AA |

---

## Singapore Market Information

Prednisolone currently has no market authorization on record in Singapore (0 registrations, market status "Not Marketed"). No product/license data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong (AA is a T-cell-mediated autoimmune disease directly addressed by corticosteroid immunosuppression), and pulse corticosteroid therapy is already an established, if not first-line, dermatologic practice for AA — supported by one placebo-controlled trial, systematic reviews, and multiple cohort/case-series studies. However, no large completed Phase 2/3 RCT specifically validates prednisolone (vs. other corticosteroids) in AA, and several critical drug-level data points remain unresolved.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (currently a Blocking data gap — required before any S1 safety review)
- Confirmed mechanism of action documentation from DrugBank
- Drug-drug interaction (DDI) data (currently "not found" in source query)
- Confirmation of Singapore registration/import pathway, given the drug is not currently marketed locally
- A dedicated prednisolone-vs-comparator RCT in AA to upgrade evidence beyond L3
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

