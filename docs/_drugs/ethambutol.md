---
layout: default
title: Ethambutol
parent: Low Evidence (L5)
nav_order: 406
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ethambutol: predicted new indication Epiglottitis (evidence level L4). Approved use: Pulmonary tuberculosis"
monitor_inn: "Ethambutol"
predicted_indications: ["epiglottitis", "laryngitis", "meningococcal infection", "peritonitis", "infectious otitis media"]
---

# Ethambutol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ethambutol: From Pulmonary Tuberculosis to Epiglottitis
{: .text-alpha }

## One-Sentence Summary

Ethambutol is an anti-tuberculosis drug originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **epiglottitis**, but there are currently **0 clinical trials** and only **1 publication** (a case series on laryngeal tuberculosis), so the supporting evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

*Note: The registered Singapore product labels in the data compiled for this report have no approved-indication text. The original indication is therefore given as pulmonary tuberculosis.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ethambutol is a well-established anti-mycobacterial agent. Its efficacy in pulmonary tuberculosis is proven, and it is generally understood to act on mycobacterial cell wall synthesis (arabinosyl transferase inhibition).

The only retrieved paper describes laryngeal tuberculosis. In that series, the epiglottis was one of the affected sites, and patients were treated with multi-drug anti-TB regimens that included ethambutol. This is the existing anti-TB indication applied to a specific anatomical site, not a genuine repurposing signal. Epiglottitis is typically bacterial (for example, *Haemophilus influenzae*), and ethambutol has no known activity against these organisms. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top-ranked predictions show the same pattern. Laryngitis, peritonitis, endocarditis and middle ear disease are supported only by reports of tuberculous or other mycobacterial involvement. Meningococcal infection, infectious otitis media, endocardial fibroelastosis, middle ear cholesterol granuloma and otosalpingitis are prediction-only, with no literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Case series | European Respiratory Journal | 41 cases of laryngeal tuberculosis. All had current or earlier pulmonary TB. The epiglottis was the second most frequently affected site after the true vocal cords. Patients were usually treated with isoniazid, rifampicin and ethambutol. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN03004P | EBUTOL-100 TABLET 100 mg | Film-coated tablet | Not stated in available data |
| SIN03005P | EBUTOL-400 TABLET 400 mg | Film-coated tablet | Not stated in available data |

Both products are single-ingredient, currently valid, oral tablets made by Sunward Pharmaceutical Private Limited.

## Safety Considerations

- **Disease associations from the knowledge graph** (not label text): the drug is linked to kidney disease, pyoureter, gout, diabetic retinopathy, diabetic cataract and optic neuritis. These should be checked against the package insert, since ethambutol is known to affect the optic nerve.
- **Drug Interactions**: 100 interactions were recorded. Moderate-level ones include metronidazole, picosulfuric acid, naltrexone, rosuvastatin, simvastatin, tinidazole and aluminium hydroxide. Other interactions are of unknown severity, including proton pump inhibitors (omeprazole, pantoprazole, lansoprazole), corticosteroids (prednisone, prednisolone, hydrocortisone), morphine, vancomycin, sulfasalazine, ranitidine, clotrimazole, nystatin and potassium chloride.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Epiglottitis has no registered trials and only one case series, which concerns tuberculous laryngeal disease where ethambutol is part of standard anti-TB therapy. The mechanism does not plausibly extend to typical bacterial epiglottitis. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. This is not a repurposing opportunity.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are currently missing and block safety screening
- Confirmed mechanism of action data
- Evidence that ethambutol has activity in a non-tuberculous form of epiglottitis, or a narrower focus on tuberculous laryngeal and epiglottic disease, which falls under the existing anti-TB indication
- A review of the other predicted indications for any with genuine non-TB evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

