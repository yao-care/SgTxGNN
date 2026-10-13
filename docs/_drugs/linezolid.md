---
layout: default
title: Linezolid
parent: Low Evidence (L5)
nav_order: 603
evidence_level: L5
indication_count: 10
---

# Linezolid
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

# Linezolid: From Gram-Positive Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Linezolid is an oxazolidinone antibiotic, originally used for streptococcal and staphylococcal infections, including pneumonia caused by these organisms.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **0 clinical trials** and **0 publications** currently support this prediction.
The prediction rests on the model score alone, and no mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal infection, staphylococcus aureus infection, staphylococcal infection, streptococcal pneumonia, staphylococcal pneumonia (the Singapore licence records contain no approved-indication text, so these come from the knowledge graph) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 92.45% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Linezolid is known to be a bacterial protein synthesis inhibitor (an oxazolidinone). Its efficacy in Gram-positive infections is well established.

For polyclonal hyperviscosity syndrome, however, no mechanistic link has been identified. Linezolid has no known action on serum viscosity or immunoglobulin dynamics. The high score (92.45%) is a graph-based prediction only and has no clinical or literature support. It should be treated as a hypothesis, not as evidence of efficacy.

The other top-ranked predictions show the same pattern. Several are laboratory findings or genetic and immunological conditions that an antibiotic cannot plausibly treat (hyperamylasemia, congenital analbuminemia, blood group incompatibility). Two are more relevant to infection:
- **Pyelonephritis** has a partial rationale for resistant Gram-positive pathogens (VRE, MRSA). Most cases are Gram-negative, which linezolid does not reliably cover. The literature is mainly case reports and reviews, and the closest controlled evidence (PMID 14520141) is a non-specific linezolid vs vancomycin comparison in neonates.
- **Septicemic plague** has only indirect support, because *Yersinia pestis* is Gram-negative and linezolid has limited activity against such organisms. The only retrieved paper is a tuberculosis review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for polyclonal hyperviscosity syndrome.

(The literature that was retrieved relates to other lower-ranked predictions, such as monoclonal gammopathy, congenital hematological disorder, septicemic plague and pyelonephritis. It consists mainly of case reports, reviews and in vitro studies of infections in patients with underlying conditions, not of treatment of those conditions themselves.)

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16950P | LINEZAN SOLUTION FOR INFUSION 2MG/ML | Infusion, solution | Not stated in the available records |
| SIN11405P | ZYVOX TABLET 600 mg | Tablet, film coated | Not stated in the available records |
| SIN15849P | LINEZOLID KABI SOLUTION FOR INFUSION 2MG/ML | Infusion, solution | Not stated in the available records |
| SIN11408P | ZYVOX GRANULES FOR ORAL SUSPENSION 20 mg/ml | Granule, for suspension | Not stated in the available records |
| SIN14946P | LINEZOLID SANDOZ FILM COATED TABLET 600MG | Tablet, film coated | Not stated in the available records |

All 7 licences are valid single-ingredient products (injectable, oral tablet and oral suspension forms).

## Safety Considerations

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for safety information.

**Contraindication signals from the knowledge graph** (not label text):
- Haematological: thrombocytopenia, leukopenia, pancytopenia, anaemia (including macrocytic anaemia)
- Neurological and visual: peripheral neuropathy, peripheral nervous system disease, optic nerve disease, vision disorder, blindness, epilepsy
- Serotonergic and sympathomimetic: serotonin syndrome, carcinoid syndrome, hypertension, hypertensive disorder, phaeochromocytoma, thyrotoxicosis, hyperthyroidism, Graves disease
- Metabolic and gastrointestinal: lactic acidosis, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis
- Several tumour-related entries (e.g. adrenal, small intestine, heart cancer, sympathetic paraganglioma)

**Drug interactions** (100 recorded; the first 20 returned are summarised):
- **Major:** isometheptene, epinephrine, bupropion, morphine, lorcaserin, diethylpropion, dolasetron, palonosetron, phentermine
- **Moderate:** metronidazole, chlorpropamide, picosulfuric acid, glimepiride, and multiple insulins (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular)

The haematological signals matter for the predicted haematology-related indications. Linezolid can cause myelosuppression and neuropathy, so it is a safety concern, not a benefit, in patients with underlying blood disorders.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, polyclonal hyperviscosity syndrome, is supported only by a graph-model score. There are no clinical trials or publications and no plausible mechanism, and linezolid's haematological toxicity argues against use in blood disorders. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A biological rationale linking linezolid to serum viscosity or immunoglobulin dynamics, with in vitro or animal data
- Consideration of lower-ranked, infection-related predictions (resistant Gram-positive urinary tract infection, plague) as research questions. These would need culture-proven pathogen restriction, preclinical data and, where appropriate, controlled trials.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

