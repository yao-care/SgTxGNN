---
layout: default
title: Hydroxyzine
parent: Medium Evidence (L3-L4)
nav_order: 508
evidence_level: L3
indication_count: 10
---

# Hydroxyzine
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

# Hydroxyzine: Repurposing Toward Allergic Urticaria

## One-Sentence Summary

Hydroxyzine is a first-generation H1 antihistamine that is currently marketed in Singapore. The TxGNN model predicts it may be effective for **allergic urticaria** (score 99.77%). Support is indirect: there is **1 related clinical trial** (on its active metabolite cetirizine, not on hydroxyzine itself) and **20 publications**, mostly reviews of second-generation antihistamines.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Singapore registration data provided |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not retrieved from DrugBank. Hydroxyzine is a first-generation H1 inverse agonist. In urticaria, histamine released from mast cells causes the wheals and itch, so blocking the H1 receptor is a direct and class-consistent mechanism.

Cetirizine, hydroxyzine's active metabolite, has the strongest supporting literature. Antihistamines are the standard first step in urticaria treatment. Reviews note that hydroxyzine and diphenhydramine were used this way in the past (PMID 28913986).

Current guidance has moved away from first-generation agents. The CSACI position statement (PMID 31582993) recommends newer-generation H1 antihistamines as first-line because of sedation, cognitive impairment and anticholinergic burden. Hydroxyzine-specific clinical evidence for urticaria in this package is therefore thin. The prediction is mechanistically sound, but hydroxyzine would not be expected to replace second-generation agents.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Pilot feasibility study of IV cetirizine vs IV diphenhydramine in acute urticaria. It tests feasibility, not efficacy, and studies cetirizine rather than hydroxyzine (indirect support only). |

## Literature Evidence

No randomized controlled trials were retrieved. The list is mostly reviews and one position statement.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Position statement | Allergy Asthma Clin Immunol | Newer H1 antihistamines are safer and should be first-line over first-generation agents such as hydroxyzine |
| [28913986](https://pubmed.ncbi.nlm.nih.gov/28913986/) | 2017 | Review | Allergy Asthma Immunol Res | Chronic spontaneous urticaria starts with antihistamines. Hydroxyzine was used similarly in the past, and omalizumab is the next step if high-dose antihistamines fail. |
| [22994340](https://pubmed.ncbi.nlm.nih.gov/22994340/) | 2012 | Review | Clin Exp Allergy | How to choose the best H1-antihistamine for urticaria, and the difficulty of comparing drugs |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Review | Drugs | Bilastine in allergic rhinitis and urticaria |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Review | Clin Pharmacokinet | Comparison of desloratadine, fexofenadine and levocetirizine |
| [19808127](https://pubmed.ncbi.nlm.nih.gov/19808127/) | 2009 | Review | Clin Ther | Levocetirizine for allergic rhinitis and chronic idiopathic urticaria in adults and children |
| [18201439](https://pubmed.ncbi.nlm.nih.gov/18201439/) | 2007 | Review | Allergy Asthma Proc | Levocetirizine pharmacology, safety and effectiveness |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Efficacy and safety of first- and newer-generation antihistamines in allergic rhinitis and chronic idiopathic urticaria |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Cetirizine, a carboxylated metabolite of hydroxyzine, without the CNS depressant effects of standard antihistamines |
| [21793329](https://pubmed.ncbi.nlm.nih.gov/21793329/) | 2010 | Open-label observational study | Chin J Physiol | Levocetirizine in 333 Taiwanese patients (236 allergic rhinitis, 97 urticaria) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN04142P | AA PHARMA HYDROXYZINE CAPSULE 25 mg | Capsule, liquid filled | Catalent Ontario Limited |
| SIN09981P | PHYMORAX TABLET 10 mg | Tablet | Medica Korea Co Ltd |
| SIN16328P | HYDROXYZINE MEVON FILM-COATED TABLETS 25 MG | Tablet, film coated | Centaur Pharmaceuticals Pvt Ltd / Medreich Limited |
| SIN16329P | HYDROXYZINE MEVON FILM-COATED TABLETS 10 MG | Tablet, film coated | Centaur Pharmaceuticals Pvt Ltd / Medreich Limited |
| SIN04096P | AA PHARMA HYDROXYZINE CAPSULE 10 mg | Capsule | Catalent Ontario Limited |

All registered products are oral formulations.

## Safety Considerations

Package insert warnings, contraindications and drug interaction data were not retrieved. Please refer to the package insert for safety information.

The literature supplies the following class-level concerns (PMID 31582993). First-generation antihistamines such as hydroxyzine commonly cause sedation, cognitive impairment, poor sleep quality, dry mouth, dizziness and orthostatic hypotension. They have also been linked to accidents, overdoses and sudden cardiac death. Additional cautions are QT prolongation and use in elderly and pediatric patients.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
H1 blockade is a direct, well-understood mechanism for urticaria, and hydroxyzine's active metabolite cetirizine has extensive supporting literature. However, the hydroxyzine-specific evidence in this package is thin, and guidance favors second-generation antihistamines because of hydroxyzine's sedation and anticholinergic burden.

**To proceed, the following is needed:**
- Singapore package insert warnings, contraindications and approved indication text (blocking for safety screening)
- Mechanism-of-action data from DrugBank
- A head-to-head safety and efficacy comparison of hydroxyzine against second-generation antihistamines in urticaria
- Sedation, anticholinergic and QT monitoring guardrails, with specific caution for elderly and pediatric patients
- Cold urticaria (score 99.66%) is a secondary candidate with a small 1984 hydroxyzine comparative study (PMID 6480953). It merits a research question, not a recommendation.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

