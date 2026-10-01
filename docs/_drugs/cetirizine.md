---
layout: default
title: Cetirizine
parent: High Evidence (L1-L2)
nav_order: 230
evidence_level: L2
indication_count: 10
---

# Cetirizine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Cetirizine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Cetirizine is a second-generation antihistamine, widely used for allergic conditions such as allergic rhinitis.
The TxGNN model predicts it may be effective for **allergic urticaria**,
with **3 clinical trials** and **18 publications** currently supporting this direction.
Urticaria may already be an established use of cetirizine, so the label status should be checked before this is treated as true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (per published literature; Singapore label text not supplied) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Cetirizine is a peripheral histamine H1-receptor antagonist. In urticaria, histamine released from mast cells drives the wheal, flare and itch, so blocking H1 receptors directly targets the disease mechanism.

Allergic rhinitis and urticaria are both histamine-mediated allergic conditions. Older reviews describe cetirizine as effective in both allergic rhinitis and chronic idiopathic urticaria. Current guidelines cited in the literature treat second-generation antihistamines as first-line therapy for chronic spontaneous urticaria.

The supplied data suggest urticaria may already be an approved or guideline-supported use of cetirizine, and no original-indication text was provided. The candidate may therefore not be novel repurposing. It is graded L2 rather than L1 because the only Phase 3-labelled trial is a small feasibility pilot (n=36) that was not powered for efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Randomized, double-blind pilot of IV cetirizine vs IV diphenhydramine in acute urticaria. It tested the feasibility of a larger trial, so it is not definitive for efficacy. |
| [NCT03296358](https://clinicaltrials.gov/study/NCT03296358) | N/A | Completed | 75 | Randomized, double-blind trial of adding a short corticosteroid burst to conventional H1-antihistamine treatment. Cetirizine is probably background therapy, so the evidence is indirect. |
| [NCT01008592](https://clinicaltrials.gov/study/NCT01008592) | N/A | Terminated | 11 | Levocetirizine (the active enantiomer of cetirizine) and skin inflammatory mediators in dermatographism and chronic idiopathic urticaria. Mechanistic support only; small and terminated. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33030434](https://pubmed.ncbi.nlm.nih.gov/33030434/) | 2021 | Systematic Review | J Investig Allergol Clin Immunol | Reviews efficacy and safety of up-dosing second-generation antihistamines (up to 4× licensed dose) in chronic spontaneous urticaria. |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Review | Allergy | Reviews clinical studies of cetirizine in allergic rhinitis and chronic urticaria. |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Pharmacology and clinical potential of cetirizine in allergic rhinitis, pollen-induced asthma and chronic urticaria. |
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Review | Drugs | Cetirizine 10 mg/day reported as effective and well tolerated in chronic idiopathic urticaria in adults. |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Review | Drugs | Comparative review of second-generation antihistamines, including cetirizine. |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Efficacy and safety of oral antihistamines in allergic rhinitis and chronic idiopathic urticaria. |
| [18201439](https://pubmed.ncbi.nlm.nih.gov/18201439/) | 2007 | Review | Allergy Asthma Proc | Levocetirizine in allergic rhinitis and chronic idiopathic urticaria. |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Review | Clin Pharmacokinet | Comparative pharmacokinetics and pharmacodynamics of desloratadine, fexofenadine and levocetirizine. |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | Urticaria causes and treatment; non-sedating antihistamines are the mainstay for chronic idiopathic urticaria. |
| [41602253](https://pubmed.ncbi.nlm.nih.gov/41602253/) | 2025 | Case report | Cureus | Rebound pruritus and urticaria after stopping long-term cetirizine in a patient in Singapore. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN15437P | ZYRTEC-R ORAL SOLUTION 1 MG/ML | Solution | Aesica Pharmaceuticals S.R.L |
| SIN15298P | ALNIX TABLET 10mg | Tablet | Amherst Laboratories, Inc |
| SIN14890P | ZYRTEC-R FILM-COATED TABLET 10 MG | Tablet, film coated | UCB Farchim S.A. / Aesica Pharmaceuticals S.R.L (packagers) |
| SIN14240P | SUNIZINE TABLET 10MG | Tablet, film coated | Sunward Pharmaceutical Sdn Bhd |
| SIN08756P | ALLERCET TABLET 10 mg | Tablet, film coated | Micro Labs Limited |

## Safety Considerations

Please refer to the package insert for safety information.

One case report (PMID 41602253) describes rebound itching and urticaria after stopping long-term cetirizine.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The H1-blockade mechanism fits urticaria directly, the TxGNN score is very high, and the literature consistently supports antihistamine use in urticaria. Trial evidence for cetirizine itself is thin: the only Phase 3-labelled study is a small feasibility pilot. Urticaria may already be a labelled use, so this may not be true repurposing.

**To proceed, the following is needed:**
- Confirm whether urticaria is already an approved indication for cetirizine in Singapore. The HSA registration data supplied contain no indication text.
- Download and review the HSA package insert warnings and contraindications.
- Obtain the mechanism of action from DrugBank.
- Look for adequately powered efficacy trials of cetirizine in urticaria.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

