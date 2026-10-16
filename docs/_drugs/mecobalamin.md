---
layout: default
title: Mecobalamin
parent: Low Evidence (L5)
nav_order: 639
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Mecobalamin: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not available"
---

# Mecobalamin
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

# Mecobalamin: From Unspecified Registered Indication to Sclerosing Cholangitis

## One-Sentence Summary

Mecobalamin (methylcobalamin, the coenzyme form of vitamin B12) is registered in Singapore in four single-ingredient products, but the data compiled for this report do not list an approved indication text.
The TxGNN model ranks **sclerosing cholangitis** as its top prediction, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting it.
The only publication found for any of the top 10 predictions concerns colorectal cancer (a 1989 study of supportive care after rectal cancer surgery), and it does not address the sclerosing cholangitis prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (approved indication text is blank in all registrations) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mecobalamin is the active coenzyme form of vitamin B12. It is widely used in peripheral neuropathy and B12-related conditions, but the data compiled for this report do not specify its registered indication.

No plausible mechanistic link between methylcobalamin and sclerosing cholangitis (a cholestatic, autoimmune-associated biliary disease) can be established from the available data. The high TxGNN score (0.995) reflects a graph-based computational association and should not be read as evidence of efficacy.

Other top-ranked predictions show the same pattern. Multiple endocrine neoplasia, juvenile Paget disease, osteomesopyknosis and choledocholithiasis have no supporting data and no evident mechanism. "Obsolete vitamin D deficiency" is an outdated ontology term and is probably a graph artifact. For acne, vitamin B12 has been anecdotally linked to acneiform eruptions rather than benefit, so the prediction direction is questionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For sclerosing cholangitis, currently no related literature is available.

The only publication found across the top 10 predictions relates to the rank 10 prediction, colorectal cancer. It is shown here for reference only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2694825](https://pubmed.ncbi.nlm.nih.gov/2694825/) | 1989 | Clinical evaluation (likely uncontrolled or observational) | Hinyokika Kiyo (Acta Urologica Japonica) | In 17 patients after rectal cancer surgery, randomised to mecobalamin (500 µg i.m., 3 times weekly for 4 weeks) or no treatment (8 vs 9 patients), bladder function was assessed. This addresses postoperative micturition dysfunction (supportive care), not anti-tumour activity. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06291P | METHYCOBAL TABLET 500 mcg | Sugar-coated tablet | Not specified |
| SIN06349P | METHYCOBAL INJECTION 500 mcg/ml | Injection | Not specified |
| SIN10917P | NEUROMETHYN CAP. 500 mcg | Capsule | Not specified |
| SIN16735P | MECONEURO CAPSULES 500 MCG | Capsule | Not specified |

---

## Safety Considerations

- **Disease-level contraindication signals (from a knowledge graph, not label text)**: potassium deficiency disease, chronic atrophic gastritis, Leber hereditary optic neuropathy.
- **Drug Interactions**: 13 interactions were identified. Two are Moderate: **arsenic trioxide** and **chloramphenicol**. The other 11 are Minor, all acid-suppressing agents:
  - H2 blockers: famotidine, ranitidine, ranitidine bismuth citrate, cimetidine, nizatidine
  - Proton pump inhibitors: omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sclerosing cholangitis prediction rests only on a model score, with no clinical trials, no literature and no identifiable mechanistic link. Package insert safety information is also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- HSA package insert warnings, contraindications and approved indications (download and parse the package insert PDFs)
- Mechanism of action data (for example from DrugBank)
- A systematic literature search for mecobalamin in sclerosing cholangitis and other cholestatic liver diseases
- Review of the knowledge-graph contraindication signals, especially chronic atrophic gastritis and Leber hereditary optic neuropathy
- Assessment of route compatibility (oral and injectable forms are available in Singapore) once a credible mechanistic rationale exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

