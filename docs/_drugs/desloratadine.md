---
layout: default
title: Desloratadine
parent: Low Evidence (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
---

# Desloratadine
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

# Desloratadine: From Registered Antihistamine Use to Cold Urticaria

## One-Sentence Summary

Desloratadine is a second-generation H1 antihistamine that is already registered and marketed in Singapore, although the registration records do not state an approved indication.
The TxGNN model predicts it may be effective for **cold urticaria**.
**3 clinical trials** and **7 publications**, including 3 randomized controlled trials, are currently linked to this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Singapore registration data (approved indication text is empty) |
| Predicted New Indication | Cold urticaria |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 (as assigned in the Evidence Pack; the supporting trials are small Phase 4 randomized studies, not Phase 3) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Desloratadine is a selective peripheral H1 inverse agonist. A formal mechanism-of-action record is not available, but this pharmacology is well established. Cold urticaria is driven by mast cell histamine release, so blocking H1 receptors is a direct mechanistic fit.

Non-sedating second-generation antihistamines are the standard symptomatic treatment for urticaria. Increasing the dose above the standard is the recognised approach for cold urticaria patients who respond poorly to the standard dose. The trials and randomized studies below test this idea with desloratadine at 5, 10 and 20 mg.

Because the registration data list no approved indication, the labelled-use status in Singapore should be confirmed. This matters because the evidence relies on doses above the standard 5 mg.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Completed | 30 | Multi-center, double-blind, dose-escalating comparison of desloratadine 5, 10 and 20 mg in acquired cold urticaria. It aims to find the dose sufficient to inhibit symptoms. |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Completed | 33 | Randomized, double-blind, placebo-controlled crossover of 5 mg vs. 20 mg desloratadine. It measures experimentally induced cold urticaria lesions using thermography, volumetry and time-lapse photography. |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Completed | 150 | Compares the inhibitory effect of 5 antihistamines in urticaria. It is larger, but the population may not be limited to cold urticaria and the desloratadine arm needs confirmation. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | Randomized, placebo-controlled crossover study. High-dose desloratadine decreased wheal volume and improved cold provocation thresholds compared with standard dose in acquired cold urticaria. |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | Randomized trial of H1-antihistamine dose escalation using critical temperature threshold measurement. The supplied abstract does not name the drug. |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatol Treat | 5 mg desloratadine for 4 days, tested with ice cubes before and after treatment in 12 cold urticaria patients. |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | Overview of the causes, management and current and future treatments of chronic urticaria. |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case report | Qatar Med J | Cold-induced urticaria after black ant bite anaphylaxis. Background on the condition, not evidence for desloratadine. |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Case report | J Allergy Clin Immunol Pract | Food-dependent cold urticaria described as a new variant of physical urticaria. Background only. |

## Singapore Market Information

Desloratadine has 6 registrations in Singapore, and 5 are listed below. All are oral tablets, and none records an approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15773P | Desloratadine Sandoz Film Coated Tablet 5mg | Tablet, film coated | — |
| SIN16298P | Destavell Film-Coated Tablet 5 mg | Tablet, film coated | — |
| SIN16170P | Alrinast Film-Coated Tablet 5mg | Tablet, film coated | — |
| SIN16670P | Glendes Tablet 5 mg | Tablet | — |
| SIN15938P | Airistar Film-Coated Tablet 5mg | Tablet, film coated | — |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is direct, and three randomized studies plus three completed Phase 4 trials support desloratadine, including dose escalation, in cold urticaria. The trials are small (n=30 and n=33 for the two directly relevant ones), and the best-supported benefit comes from doses above the standard 5 mg. The drug is already marketed in Singapore, so the remaining questions are labelling and safety at higher doses.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website, which are currently missing and block safety screening.
- Confirmation of the approved indications and labelled dose in Singapore, since the registration records are blank.
- A safety review of dosing above 5 mg, using the completed trials' safety data and the package insert.
- Confirmation of the desloratadine arm and the cold urticaria subgroup in NCT01940393, and of the exact comparator in NCT00600847.
- A formal mechanism-of-action record from DrugBank.

**Other predicted indications:** The nine lower-ranked predictions do not warrant follow-up now. Nasal cavity disease is a research question only, because its literature is animal work and uses other agents. The other eight are Hold, with prediction only or no relevant desloratadine evidence: acute laryngopharyngitis, recalcitrant atopic dermatitis, atopic IgE responsiveness, rosacea conjunctivitis, headache disorder, trigeminal autonomic cephalalgia, punctate epithelial keratoconjunctivitis and Angelucci syndrome.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

