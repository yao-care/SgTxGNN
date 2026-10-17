---
layout: default
title: Amphotericin B
parent: Low Evidence (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Amphotericin B: predicted new indication Chronic rhinosinusitis (evidence level L5). Approved use: Candidiasis and other infections"
monitor_inn: "Amphotericin B"
predicted_indications: ["paranasal sinus neoplasm (disease)", "meningococcal infection", "endocardial fibroelastosis", "bacterial arthritis"]
---

# Amphotericin B
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

# Amphotericin B: From Fungal and Bacterial Infections to Chronic Rhinosinusitis

## One-Sentence Summary

Amphotericin B is a polyene antifungal, marketed in Singapore as liposomal injection (AmBisome), and its original indications in the knowledge graph are mainly infections such as candidiasis.
The TxGNN model predicts it may be effective for **chronic rhinosinusitis** (the highest-ranked prediction with direct trial evidence), with **1 Phase 3 clinical trial** and **19 publications** on this direction.
However, the clinical results are largely negative or inconsistent, so the evidence is extensive but does not show a convincing benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Candidiasis and other infections (the licence record has no approved indication text; this is taken from the knowledge graph) |
| Predicted New Indication | Chronic rhinosinusitis (the top-ranked prediction, paranasal sinus neoplasm, has only indirect evidence, so this report focuses on the best-supported prediction) |
| TxGNN Prediction Score | 97.44% (chronic rhinosinusitis); 97.45% for the top-ranked paranasal sinus neoplasm |
| Evidence Level | L1 (formally; one completed Phase 3 trial plus several RCTs and meta-analyses, but efficacy signal is weak) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

**Note on the predictions:** TxGNN ranked paranasal sinus neoplasm first (97.45%), but the literature there concerns fungal infections in cancer patients, not tumour treatment, so it is not a credible new indication (L4, Hold). Chronic rhinosinusitis is the prediction with the most direct clinical evidence and is the focus below.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Amphotericin B is known as a polyene antifungal that binds ergosterol in fungal cell membranes and disrupts them.

The rationale for chronic rhinosinusitis is the hypothesis that fungal colonisation of the nasal mucosa drives an exaggerated eosinophilic inflammatory reaction. If so, a topical antifungal could reduce the trigger. This links the drug's established antifungal activity to a chronic inflammatory sinus disease.

In practice, the hypothesis has not held up well. Nasal lavage studies and meta-analyses show no consistent clinical benefit, and a Cochrane review does not support routine topical or systemic antifungals for this condition. The high prediction score therefore reflects a plausible biological link rather than demonstrated efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00425620](https://clinicaltrials.gov/study/NCT00425620) | Phase 3 | Completed | 300 | Randomised, double-blind, placebo-controlled, multicentre trial of intranasal amphotericin B suspension for 16 weeks in refractory, postsurgical chronic sinusitis. Published literature suggests the primary efficacy outcome was not convincingly met. |

For other predictions, one Phase 2 trial exists: [NCT05468372](https://clinicaltrials.gov/study/NCT05468372) (completed, 82 participants) compares amphotericin B with posaconazole in pulmonary mucormycosis. It concerns a fungal infection and is only weakly relevant to the predicted "bacterial pneumonia" label.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30199594](https://pubmed.ncbi.nlm.nih.gov/30199594/) | 2018 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Review of topical and systemic antifungals for chronic rhinosinusitis; does not support routine use |
| [25217082](https://pubmed.ncbi.nlm.nih.gov/25217082/) | 2015 | Meta-analysis | Eur Arch Otorhinolaryngol | Meta-analysis of comparative studies of topical amphotericin B in chronic rhinosinusitis |
| [22287428](https://pubmed.ncbi.nlm.nih.gov/22287428/) | 2011 | Meta-analysis | Int Forum Allergy Rhinol | Efficacy of topical amphotericin B not consistently supported |
| [18284860](https://pubmed.ncbi.nlm.nih.gov/18284860/) | 2008 | RCT | Am J Rhinol | Amphotericin B irrigation in chronic rhinosinusitis without nasal polyps, placebo-controlled |
| [15637558](https://pubmed.ncbi.nlm.nih.gov/15637558/) | 2005 | RCT | J Allergy Clin Immunol | Pilot double-blind trial of intranasal amphotericin B in chronic rhinosinusitis |
| [31763315](https://pubmed.ncbi.nlm.nih.gov/31763315/) | 2019 | RCT | Indian J Otolaryngol Head Neck Surg | Itraconazole vs voriconazole vs amphotericin B in chronic invasive fungal rhinosinusitis (30 patients) |
| [17088142](https://pubmed.ncbi.nlm.nih.gov/17088142/) | 2006 | Clinical study | J Allergy Clin Immunol | Amphotericin B nasal lavages not a solution for chronic rhinosinusitis; trials conflicting |
| [31358093](https://pubmed.ncbi.nlm.nih.gov/31358093/) | 2019 | Clinical study | J Coll Physicians Surg Pak | Amphotericin B nasal irrigation in chronic rhinosinusitis with nasal polyps |
| [18360640](https://pubmed.ncbi.nlm.nih.gov/18360640/) | 2007 | Review | Ther Clin Risk Manag | Diagnosis and treatment of chronic rhinosinusitis, focus on intranasal amphotericin B |
| [20513020](https://pubmed.ncbi.nlm.nih.gov/20513020/) | 2010 | Review | Laryngoscope | Is topical amphotericin B efficacious in chronic rhinosinusitis? |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12021P | AmBisome for Injection 50 mg/vial | Injection, powder, for solution | Not stated in the licence record |

Only an injectable (intravenous) product is registered. The trials above use intranasal or irrigation formulations, so a topical nasal product would not be covered by the existing registration.

## Cytotoxicity

Not applicable. Amphotericin B is an antifungal, not an antineoplastic drug.

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** kidney disease, liver disease, gallbladder disease, potassium deficiency, pyoureter, *Clostridium difficile* colitis and perinatal necrotizing enterocolitis.
- **Drug interactions:** 100 interactions were found. Major-level interactions include foscarnet, gallium nitrate, amiodarone and arsenic trioxide. Moderate-level interactions include aminoglycosides (amikacin), loop and thiazide diuretics (furosemide, hydrochlorothiazide), corticosteroids (hydrocortisone, betamethasone, beclomethasone), ganciclovir, zidovudine and acetazolamide. Many of these relate to additive nephrotoxicity, electrolyte loss (especially potassium) or QT prolongation.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although a completed Phase 3 trial and several RCTs and meta-analyses exist for chronic rhinosinusitis, the results are largely negative or inconsistent and the Cochrane review does not support use. The other predictions are either infections already covered by antifungal use, mismatched to the drug's mechanism (bacterial pneumonia, meningococcal infection, bacterial arthritis, pneumocystosis), or purely computational (endocardial fibroelastosis, paranasal sinus neoplasm).

**To proceed, the following is needed:**
- Full results of NCT00425620, particularly the primary endpoint outcome
- Subgroup analyses (for example, patients with nasal polyps or invasive fungal rhinosinusitis) to define any responsive population
- Mechanism of action data and the package insert warnings and contraindications for the Singapore licence
- Assessment of a topical or intranasal formulation, since only an intravenous product is currently registered in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

