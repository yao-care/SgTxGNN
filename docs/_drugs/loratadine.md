---
layout: default
title: Loratadine
parent: Medium Evidence (L3-L4)
nav_order: 608
evidence_level: L3
indication_count: 10
---

# Loratadine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Loratadine: From Antihistamine Therapy to Allergic Urticaria

## One-Sentence Summary

Loratadine is a widely used second-generation antihistamine, marketed in Singapore under 17 registrations.
The TxGNN model predicts it may be effective for **allergic urticaria**,
with **3 clinical trials** (none testing loratadine directly for urticaria) and **18 publications** (mostly reviews) currently supporting this direction.
This is probably an existing labelled use rather than a true repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 17 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the database. Loratadine is known as a selective peripheral H1-receptor inverse agonist. In urticaria, histamine released from mast cells drives the wheal-and-flare response, so blocking the H1 receptor targets the core pathophysiology directly.

The literature describes second-generation antihistamines as first-line treatment for chronic urticaria. Older reviews of loratadine (1989 and 1994) list urticaria among its evaluated uses.

The high score most likely reflects H1-antagonist class knowledge already in the knowledge graph. Because indication text is missing from the Singapore registration records, this pack cannot confirm whether urticaria is already on the label. Evidence specific to loratadine is limited. Much of the supportive data comes from related drugs such as desloratadine (its active metabolite), fexofenadine and bilastine.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00762983](https://clinicaltrials.gov/study/NCT00762983) | N/A (post-marketing survey) | Completed | 1003 | Japanese drug-use investigation of Claritin (loratadine) in children, collecting adverse reactions and symptom scores. Observational, with no control arm. |
| [NCT00757562](https://clinicaltrials.gov/study/NCT00757562) | Phase 3 | Completed | 97 | Safety and tolerance of desloratadine (the active metabolite, a different molecule) in children with allergic hypersensitivity or chronic hives. Indirect evidence for loratadine. |
| [NCT07101445](https://clinicaltrials.gov/study/NCT07101445) | Phase 4 | Recruiting | 94 | Dexamethasone vs methylprednisolone premedication to prevent allergic reactions to motixafortide. No loratadine arm is evident. Low relevance. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35593100](https://pubmed.ncbi.nlm.nih.gov/35593100/) | 2022 | Systematic review / meta-analysis of RCTs | Am J Rhinol Allergy | Bilastine for allergic rhinitis and chronic urticaria. Class-level support only, not loratadine. |
| [7528133](https://pubmed.ncbi.nlm.nih.gov/7528133/) | 1994 | Review | Drugs | Loratadine evaluated in allergic rhinitis and urticaria. Superior to placebo and comparable to several other antihistamines in controlled studies. |
| [35396016](https://pubmed.ncbi.nlm.nih.gov/35396016/) | 2022 | Review | Profiles Drug Subst Excip Relat Methodol | Drug profile of loratadine, noting use in allergic rhinitis, chronic urticaria and asthma. |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Review | Drugs | Comparative review of second-generation antihistamines, including loratadine. |
| [10730552](https://pubmed.ncbi.nlm.nih.gov/10730552/) | 2000 | Review | Drugs | Fexofenadine in seasonal allergic rhinitis and chronic idiopathic urticaria, with comparisons to loratadine 10 mg. |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | Urticaria causes and treatment. Non-sedating antihistamines are the mainstay for chronic idiopathic urticaria. |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Efficacy and safety of oral antihistamines in allergic rhinitis and chronic idiopathic urticaria. |
| [20067329](https://pubmed.ncbi.nlm.nih.gov/20067329/) | 2010 | Post-marketing surveillance | Clin Drug Investig | Desloratadine in seasonal allergic rhinitis and chronic urticaria. Second-generation antihistamines are recommended first-line for both. |
| [16259582](https://pubmed.ncbi.nlm.nih.gov/16259582/) | 2005 | Review | Expert Opin Pharmacother | Desloratadine in allergic rhinitis, chronic idiopathic urticaria and allergic inflammation. |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Review | Clin Pharmacokinet | Pharmacokinetics and pharmacodynamics of desloratadine, fexofenadine and levocetirizine. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12466P | LORACIN TABLET 10 mg | Tablet | Not stated in the registration record |
| SIN10351P | HALODIN TABLETS 10 mg | Tablet | Not stated in the registration record |
| SIN11617P | ARDIN TABLET 10 mg | Tablet | Not stated in the registration record |
| SIN12046P | CARIN TABLET 10 mg | Tablet | Not stated in the registration record |
| SIN16091P | CLARITYNE SYRUP 5 MG/5 ML (GRAPE FLAVOR) | Syrup | Not stated in the registration record |

Registered oral forms also include film-coated and sugar-coated tablets.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is direct, and the literature supports antihistamines as first-line therapy for urticaria. However, the trial evidence is indirect (post-marketing data and a desloratadine study), and the support is mostly narrative reviews. The prediction appears to overlap with existing labelled use, so it should not be treated as a novel repurposing finding without confirmation.

**To proceed, the following is needed:**
- The HSA package insert, to confirm the labelled indications and to complete warnings, contraindications and interaction data (currently blocking the safety screen).
- Mechanism-of-action data from DrugBank.
- Loratadine-specific randomized evidence in urticaria (published RCTs so far mainly involve other antihistamines).

**Other predictions in this pack:**
- Nasal cavity disease (allergic rhinitis) has L2 evidence, mainly from a Phase 2 trial that used loratadine as the comparator.
- Cold urticaria is a research question. Its randomized data involve desloratadine and other antihistamines, not loratadine.
- The remaining six predictions have no supporting trials or literature, or only a single case report, and are on Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

