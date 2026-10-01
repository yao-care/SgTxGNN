---
layout: default
title: Pyrazinamide
parent: Low Evidence (L5)
nav_order: 833
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide: From Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

Pyrazinamide is a first-line anti-tuberculosis drug. The TxGNN model predicts it may be effective for **infectious otitis media**, but **no clinical trials and no publications** were found for this exact term. The score is likely driven by TB-related neighbours in the knowledge graph, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (inferred from the drug class; the Singapore registration record gives no indication text) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pyrazinamide is a standard component of multidrug anti-tuberculosis regimens. Its efficacy in tuberculosis is established, and it may be mechanistically applicable to otitis media only where the infection is mycobacterial.

Common otitis media is caused by ordinary bacteria, and pyrazinamide is not expected to be active against those pathogens. The link holds only for the tuberculous subtype, a rare extrapulmonary form of TB. The high score is probably an artefact of TB-related graph neighbours, not evidence of a new mechanism.

Several related predictions in the same ear-disease cluster do have supporting literature. These are middle ear disease, chronic otitis media, suppurative otitis media and infectious otitis interna. All of it concerns tuberculous otitis media, which would be an extension of the existing TB indication, not a new one.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for "infectious otitis media" as a search term.

The publications below were retrieved for closely related predictions. They are indirect evidence, limited to tuberculous otitis media case reports and small series.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26785789](https://pubmed.ncbi.nlm.nih.gov/26785789/) | 2013 | Case Report | Int J Mycobacteriol | Nasal and middle ear TB treated with rifampicin, isoniazid and pyrazinamide for 9 months; no recurrence at 1 year |
| [21532520](https://pubmed.ncbi.nlm.nih.gov/21532520/) | 2011 | Case Series | Otol Neurotol | Variable presentation of TB otitis media; early detection improves treatment outcome |
| [12680299](https://pubmed.ncbi.nlm.nih.gov/12680299/) | 2003 | Case Series | An Otorrinolaringol Ibero Am | Three cases of tuberculous otitis media; anti-TB drugs usually effective, but diagnosis is often delayed |
| [15168420](https://pubmed.ncbi.nlm.nih.gov/15168420/) | 2004 | Case Report | Am J Kidney Dis | Tuberculous otitis media in a renal transplant recipient after repeated empiric antibiotic courses |
| [41783873](https://pubmed.ncbi.nlm.nih.gov/41783873/) | 2026 | Case Report | Cureus | Tuberculous otitis media presenting as otorrhea, diagnosed late in a low-TB-prevalence setting |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00900P | PYRAZINAMIDE TABLET 500 mg (Sunward Pharmaceutical Private Limited) | Tablet | — (not stated in the registry record) |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for infectious otitis media rests on the model score alone, with no trials or publications for this term. Pyrazinamide has no expected activity against common bacterial otitis media. The only credible link is tuberculous otitis media, which would be an extension of the existing TB use, not a new indication.

**To proceed, the following is needed:**
- Retrieve the Singapore (HSA) package insert, including warnings and contraindications and the approved indication text
- Obtain mechanism of action data for pyrazinamide (for example from DrugBank)
- Narrow the indication to tuberculous otitis media and review that evidence as a TB-extension question
- Check whether any ongoing studies cover TB otitis media
- Compare the prediction against standard TB treatment guidance for extrapulmonary disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

