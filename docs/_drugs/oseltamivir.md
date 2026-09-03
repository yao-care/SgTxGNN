---
layout: default
title: Oseltamivir
parent: 僅模型預測 (L5)
nav_order: 737
evidence_level: L5
indication_count: 10
---

# Oseltamivir
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

# Oseltamivir: From Influenza to Pneumonia

## One-Sentence Summary

Oseltamivir is a neuraminidase inhibitor used internationally for the treatment and prophylaxis of influenza A and B. Among the 10 TxGNN-predicted new indications evaluated for this candidate, most (including the top-ranked "pyelonephritis") were screened out as knowledge-graph false positives with no mechanistic or clinical support — but **Pneumonia** (influenza-associated) stands out with substantial evidence: **50 matched clinical trials** (including multiple completed Phase 3 studies) and **20 literature entries**, reaching **Evidence Level L1**.

> **Note on candidate selection**: TxGNN's #1-ranked prediction by raw score was "pyelonephritis" (97.85%), but the evidence review explicitly flagged this — and 6 of the other 9 candidates (tyrosine/phenylalanine metabolism disorders, Pierre Robin syndrome, PKU, cytochrome c oxidase deficiency) — as embedding artifacts with no supporting trials, literature, or mechanistic plausibility. This report focuses on the one candidate (**pneumonia**, rank 8) that survived evidence review with a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (treatment and prophylaxis) — established international indication; Singapore-specific label text unavailable (drug not currently marketed) |
| Predicted New Indication | Pneumonia (influenza-associated) |
| TxGNN Prediction Score | 92.14% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Oseltamivir carboxylate (the active metabolite of oseltamivir phosphate) is a potent and specific inhibitor of influenza A and B neuraminidase, blocking the release of progeny virions from infected respiratory epithelial cells and thereby limiting viral spread within the respiratory tract (per literature evidence, e.g. PMID 12103431).

Pneumonia — whether primary viral pneumonia from influenza itself or secondary bacterial pneumonia following influenza-induced epithelial damage — is a direct downstream complication of influenza infection. Since Oseltamivir's core mechanism reduces viral replication and load, its ability to lower the incidence and severity of influenza-associated pneumonia is a mechanistically direct extension of its approved antiviral action, not a speculative cross-disease association. This is reflected in the evidence level (L1) and decision stage (S3), both markedly stronger than any other candidate disease evaluated in this pack.

By contrast, the other 9 TxGNN-predicted indications in this evidence pack (pyelonephritis, tyrosine/phenylalanine metabolism disorders, Pierre Robin syndrome, PKU, cytochrome c oxidase deficiency, aspergillosis susceptibility) either had zero supporting literature/trials or literature that was topically unrelated (e.g., neuraminidase *resistance mutation* studies misclassified as "tyrosine metabolism" due to the H274Y/H275Y mutation naming), and were correctly staged as Hold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03629184](https://clinicaltrials.gov/study/NCT03629184) | Phase 3 | Completed | 173 | Baloxavir marboxil vs. oseltamivir (active control) in pediatric patients with influenza-like symptoms; safety/PK/efficacy comparison |
| [NCT06774859](https://clinicaltrials.gov/study/NCT06774859) | Phase 3 | Completed | 100 | Baloxavir vs. 5-day oseltamivir BID in Chinese pediatric patients with influenza symptoms |
| [NCT02949011](https://clinicaltrials.gov/study/NCT02949011) | Phase 3 | Completed | 2184 | Baloxavir vs. placebo/oseltamivir in patients at high risk of influenza complications (incl. pneumonia) |
| [NCT02954354](https://clinicaltrials.gov/study/NCT02954354) | Phase 3 | Completed | 1436 | Baloxavir vs. placebo/oseltamivir 75mg BID x5d in otherwise healthy influenza patients |
| [NCT00545532](https://clinicaltrials.gov/study/NCT00545532) | Phase 3 | Completed | 228 | Conventional vs. double-dose oseltamivir in immunocompromised patients with influenza |
| [NCT00705406](https://clinicaltrials.gov/study/NCT00705406) | Phase 2 | Completed | 405 | Intramuscular peramivir vs. placebo in uncomplicated acute influenza |
| [NCT02293863](https://clinicaltrials.gov/study/NCT02293863) | Phase 2 | Completed | 168 | MHAA4549A + oseltamivir vs. placebo + oseltamivir in severe influenza A requiring hospitalization |
| [NCT01620307](https://clinicaltrials.gov/study/NCT01620307) | Phase 2 | Completed | 38 | Rapamune (mTOR inhibitor) as adjuvant therapy for severe H1N1 pneumonia with respiratory failure |
| [NCT01314911](https://clinicaltrials.gov/study/NCT01314911) | N/A | Completed | 716 | Oseltamivir vs. placebo in low-risk adults; examined viral shedding and complication (pneumonia) rates |
| [NCT00988325](https://clinicaltrials.gov/study/NCT00988325) | Phase 1 | Completed | 65 | Oseltamivir PK/PD and safety in infants 0–<12 months with confirmed influenza |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24718923](https://pubmed.ncbi.nlm.nih.gov/24718923/) | 2014 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Comprehensive review of neuraminidase inhibitors, including oseltamivir, for treating/preventing influenza in adults and children |
| [39172994](https://pubmed.ncbi.nlm.nih.gov/39172994/) | 2025 | Cohort | Clin Infect Dis | FluSurv-NET (2012–2019): timing of influenza antiviral therapy associated with reduced mortality risk in adults hospitalized with influenza-associated pneumonia |
| [32031570](https://pubmed.ncbi.nlm.nih.gov/32031570/) | 2020 | Cohort | JAMA | Clinical characteristics of 138 hospitalized patients with novel coronavirus pneumonia in Wuhan; oseltamivir among treatments assessed |
| [39189087](https://pubmed.ncbi.nlm.nih.gov/39189087/) | 2024 | Cohort | Influenza Other Respir Viruses | Retrospective cohort (Japan, n=15,345) comparing baloxavir vs. oseltamivir for preventing severe events, incl. pneumonia hospitalization, in influenza B |
| [30797703](https://pubmed.ncbi.nlm.nih.gov/30797703/) | 2019 | Review | An Pediatr | Review of oseltamivir treatment for influenza in children and adolescents, including complication prevention |
| [35993199](https://pubmed.ncbi.nlm.nih.gov/35993199/) | 2022 | Review | J Glob Health | Review of adjunctive treatments (incl. oseltamivir) for children with severe pneumonia in low/middle-income countries |
| [40050867](https://pubmed.ncbi.nlm.nih.gov/40050867/) | 2025 | Review | Virology J | Review of antiviral drugs (incl. oseltamivir) and natural compounds for treating viral pneumonia |
| [31189475](https://pubmed.ncbi.nlm.nih.gov/31189475/) | 2019 | Review | Crit Care | Review of prevention, diagnosis, and treatment of influenza-related critical illness |
| [21760915](https://pubmed.ncbi.nlm.nih.gov/21760915/) | 2011 | Retrospective Study | PLoS One | Early oseltamivir administration reduced occurrence/severity of pneumonia in pandemic H1N1 2009 (Mexico cohort) |
| [17355734](https://pubmed.ncbi.nlm.nih.gov/17355734/) | 2007 | Observational Study | Curr Med Res Opin | Evaluated effectiveness of oseltamivir in reducing pneumonia complication rates in children with clinically diagnosed influenza |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials and a Cochrane systematic review support Oseltamivir's role in reducing influenza-associated pneumonia risk/severity, giving this candidate Evidence Level L1 — the strongest evidence tier of all 10 TxGNN predictions reviewed for this drug. However, Oseltamivir is currently **not registered/marketed in Singapore** (0 licenses), and drug-level safety data (warnings, contraindications, DDI) are entirely unavailable, blocking a full safety assessment (see DG001).

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings & contraindications) — currently blocking (DG001)
- Detailed mechanism of action confirmation from DrugBank (DG002)
- Singapore market registration pathway assessment (product currently unmarketed, 0 licenses)
- Re-query DDI database (current status: not_found)
- Formal disposition (Hold, closed) of the 9 lower-confidence TxGNN candidates (pyelonephritis, tyrosine/phenylalanine metabolism disorders, Pierre Robin syndrome, PKU, cytochrome c oxidase deficiency, aspergillosis susceptibility, S. aureus infection, streptococcal pneumonia) to avoid re-surfacing unsupported signals in future review cycles
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

