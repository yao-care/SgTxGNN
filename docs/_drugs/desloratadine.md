---
layout: default
title: Desloratadine
parent: High Evidence (L1-L2)
nav_order: 314
evidence_level: L2
indication_count: 10
---

# Desloratadine
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

# Desloratadine: From Allergic Rhinitis to Cold Urticaria

## One-Sentence Summary

Desloratadine is a second-generation oral antihistamine, originally used for allergic rhinitis, allergic conjunctivitis and urticaria.
The TxGNN model predicts it may be effective for **cold urticaria**,
with **2 clinical trials** and **6 publications** (2 of them RCTs) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, allergic and other conjunctivitis, idiopathic and allergic urticaria (per the knowledge graph; the Singapore licences carry no indication text) |
| Predicted New Indication | Cold urticaria |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Desloratadine is a selective peripheral H1-receptor antagonist (inverse agonist). Its efficacy in histamine-mediated allergic conditions, including idiopathic and allergic urticaria, is already established.

Cold urticaria is a physical urticaria in which cold exposure triggers mast cell degranulation and histamine release. Blocking H1 receptors therefore targets the main effector pathway directly. Raising second-generation H1 antihistamines above the standard dose is also supported by guidelines for patients who do not respond to the standard dose.

Cold urticaria is closely related to the urticaria indications desloratadine already holds, so this is a mechanistically coherent extension. The main question is the dose needed, which in the studies below goes beyond the standard 5 mg.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Completed | 30 | Multi-centre, double-blind dose-escalation study of 5, 10 and 20 mg desloratadine in acquired cold urticaria, aiming to find the dose that suppresses symptoms |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Completed | 33 | Randomised, double-blind, placebo-controlled crossover study comparing 5 mg vs 20 mg desloratadine on experimentally induced cold urticaria lesions (thermography, volumetry, photography) |

Both trials are small, and neither is a Phase 3 study.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | Randomised, placebo-controlled crossover study: high-dose desloratadine reduced wheal volume and improved cold provocation thresholds compared with standard dose in acquired cold urticaria |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | Randomised trial of H1-antihistamine dose escalation using critical temperature threshold measurement in cold urticaria |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | Clinical study | J Dermatolog Treat | 5 mg desloratadine for 4 days, tested with ice cubes before and after treatment in 12 cold urticaria patients |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | Aetiology, management and treatment options for chronic urticaria |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Review | Allergy | Ebastine in allergic rhinitis and chronic idiopathic urticaria (a different antihistamine; indirect relevance) |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case report | Qatar Med J | Cold-induced urticaria after black ant bite anaphylaxis (background on the condition only) |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15773P | Desloratadine Sandoz Film Coated Tablet 5 mg | Film-coated tablet | Not stated in the data compiled |
| SIN16298P | Destavell Film-Coated Tablet 5 mg | Film-coated tablet | Not stated in the data compiled |
| SIN16170P | Alrinast Film-Coated Tablet 5 mg | Film-coated tablet | Not stated in the data compiled |
| SIN16670P | Glendes Tablet 5 mg | Tablet | Not stated in the data compiled |
| SIN15938P | Airistar Film-Coated Tablet 5 mg | Film-coated tablet | Not stated in the data compiled |

A sixth licence, SIN11743P (Aerius Tablet 5 mg, film-coated), is also valid. All six are single-ingredient oral products, and all are currently valid.

---

## Safety Considerations

The package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Knowledge-graph contraindication signals (not label text):** hypertension and other hypertensive disorders, kidney disease, liver disease, gallbladder disease, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease and atherosclerosis, angle-closure glaucoma, and hyperthyroidism (Graves disease, thyrotoxicosis). These should be verified against the approved label before being relied on.
- **Drug Interactions:** The interaction screen returned 100 potential interacting drugs, none with a severity grade. Examples include calcitriol, phentermine, pantoprazole, omeprazole, metformin, morphine, cimetidine, simvastatin, prednisone and epinephrine. Severity should be confirmed from a clinical interaction reference.
- **Higher-dose use:** The supporting studies use up to 20 mg, which is four times the standard 5 mg dose. Safety at these doses, including sedation and psychomotor effects, needs specific review. One psychomotor study at 7.5 mg with alcohol is in the retrieved literature.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two randomised, controlled studies in cold urticaria (PMIDs 19201016 and 22242678) and two completed Phase 4 trials directly test desloratadine or H1 antihistamine up-dosing in this condition, and the mechanism is coherent. The evidence is limited by small sample sizes and the absence of Phase 3 trials, so the level is L2 rather than L1.

Other predicted indications (nasal cavity disease, acute laryngopharyngitis, recalcitrant atopic dermatitis, atopic IgE responsiveness, rosacea conjunctivitis, headache disorder, trigeminal autonomic cephalalgia, punctate epithelial keratoconjunctivitis, Angelucci syndrome) lack supporting clinical evidence, or largely overlap existing indications, and are on **Hold**.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website
- Detailed mechanism of action data from DrugBank
- Confirmation of the approved indication text for the Singapore licences
- A safety review of off-label dosing above 5 mg, with attention to the knowledge-graph contraindication signals
- Severity grading of the potential drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

