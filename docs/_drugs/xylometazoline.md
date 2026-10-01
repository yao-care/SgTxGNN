---
layout: default
title: Xylometazoline
parent: High Evidence (L1-L2)
nav_order: 1070
evidence_level: L2
indication_count: 10
---

# Xylometazoline
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

# Xylometazoline: From Nasal Decongestant to Nasal Cavity Disease

## One-Sentence Summary

Xylometazoline is a topical nasal decongestant already marketed in Singapore. The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, supported by **2 clinical trials** and **7 publications**. The evidence is mostly procedural (nasal preparation for intubation and endoscopy) and is of modest strength.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

The registration records list no approved indication text, so the original indication is not shown here.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Xylometazoline is known to be an alpha-adrenergic agonist. It constricts blood vessels in the nasal mucosa, which reduces congestion and bleeding and widens the nasal airway.

This is a direct pharmacological fit for nasal cavity disease. Because the drug is already sold as a nasal decongestant, this prediction is probably a use already covered by the product labels rather than true repurposing. Procedural uses add support: preparing the nose for endoscopy, widening the nasal cavity before nasotracheal intubation, and intranasal analgesia in combination with lidocaine.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Blinded triple crossover comparing cocaine, lidocaine/xylometazoline and saline for intranasal analgesia before nasotracheal intubation. Xylometazoline was used in combination with lidocaine, and the endpoint was analgesia rather than disease treatment. |
| [NCT05072392](https://clinicaltrials.gov/study/NCT05072392) | Not applicable | Unknown | 80 | Foley catheter-assisted nasal intubation and nasal bleeding. Xylometazoline is not clearly the tested intervention; the link is vasoconstrictor use to prevent bleeding. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24158493](https://pubmed.ncbi.nlm.nih.gov/24158493/) | 2013 | RCT | JAMA Otolaryngol Head Neck Surg | Double-blind, placebo-controlled trial in children of a local anaesthetic plus decongestant nasal spray before flexible nasendoscopy. |
| [24023995](https://pubmed.ncbi.nlm.nih.gov/24023995/) | 2013 | Clinical study | Korean J Anesthesiol | Compared xylometazoline spray with epinephrine gauze packing for expanding the nasal cavity before nasotracheal intubation. |
| [22427029](https://pubmed.ncbi.nlm.nih.gov/22427029/) | 2013 | Prospective randomized blinded study | Eur Arch Otorhinolaryngol | In 100 patients, compared cotton pledget packing with topical spray for nasal preparation before endoscopy. |
| [8740084](https://pubmed.ncbi.nlm.nih.gov/8740084/) | 1996 | Double-blind randomized study | Arzneimittel-Forschung | Rhinomanometry in 18 healthy subjects comparing tuaminoheptane/N-acetylcysteine against xylometazoline and placebo. Xylometazoline was the comparator decongestant. |
| [1281924](https://pubmed.ncbi.nlm.nih.gov/1281924/) | 1992 | Physiological study | Rhinology | Xylometazoline altered the asymmetry of nasal airway resistance in healthy subjects and in people with acute rhinitis from the common cold. |
| [34783482](https://pubmed.ncbi.nlm.nih.gov/34783482/) | 2021 | Review | Vestn Otorinolaringol | Review of treating inflammatory nasal and sinus disease in elderly patients, including combined nasal sprays containing a decongestant. |
| [20632242](https://pubmed.ncbi.nlm.nih.gov/20632242/) | 2010 | Animal study (dog) | Pneumologie | Xylometazoline reduced raised nasal airway resistance by about 50% in brachycephalic dogs. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11622P | OTRIVIN NASAL DROPS 0.05% | Solution | Not stated in the record |
| SIN11624P | OTRIVIN NASAL SPRAY 0.1% | Spray | Not stated in the record |
| SIN15198P | SNUP STADA® SPRAY 0.1% | Spray | Not stated in the record |

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the database query.

Please refer to the package insert for warnings and contraindications.

The literature retrieved for the headache prediction also describes harms from nasal decongestants. These include reversible cerebral vasoconstriction syndrome with thunderclap headache (associated with xylometazoline, duloxetine and rhinitis medicamentosa) and hypertensive crisis with end-organ damage from over-the-counter nasal decongestant abuse. These are case reports and are relevant to prolonged or excessive use.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The mechanism fits nasal cavity disease well, and the drug is already marketed in Singapore as a nasal product.
- The supporting evidence is thin: one small Phase 3 crossover trial of a lidocaine/xylometazoline combination, plus procedural studies.
- The other nine predictions (acute laryngopharyngitis, allergic urticaria, trigeminal autonomic cephalalgia, headache disorder, nasopharyngitis, papillary conjunctivitis, faucial diphtheria, cervical disc degenerative disorder, anorectal stricture) have no supporting trials or are implausible, so they are on **Hold**.
- Headache disorder has a safety signal that argues against use.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications. This gap is blocking and prevents safety screening.
- The approved indication text for each Singapore registration, to confirm whether this use is already covered by the label.
- Detailed mechanism-of-action data from DrugBank.
- Confirmation of route compatibility between the marketed forms and the proposed use.
- Guidance limiting duration of use, given the reported rebound congestion and cardiovascular and neurovascular risks with overuse.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

