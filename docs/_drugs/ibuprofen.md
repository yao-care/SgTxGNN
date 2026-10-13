---
layout: default
title: Ibuprofen
parent: Low Evidence (L5)
nav_order: 514
evidence_level: L5
indication_count: 10
---

# Ibuprofen
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

# Ibuprofen: From Rheumatoid Arthritis and Pain Conditions to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a widely used non-steroidal anti-inflammatory drug (NSAID), originally used for rheumatoid arthritis, osteoarthritis, headache, juvenile idiopathic arthritis and patent ductus arteriosus.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
This prediction has **no clinical trials and no publications** behind it, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, headache disorder, osteoarthritis, juvenile idiopathic arthritis, spondyloarthropathy, patent ductus arteriosus (from the knowledge graph; no approved indication text is available in the Singapore licence records) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ibuprofen is generally known as a non-selective COX inhibitor that reduces prostaglandin production, which explains its anti-inflammatory, analgesic and antipyretic effects in arthritis and headache.

Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal dysplasia linked to the CDMP1/GDF5 pathway. It is a developmental bone disorder, not an inflammatory one. No plausible link between COX inhibition and this pathology is evident. The high score (0.997) is probably driven by network proximity to skeletal and arthropathy-related terms in the knowledge graph, not by a biological mechanism.

At most, ibuprofen might relieve joint pain as symptomatic management. That is not a repurposing rationale, because it does not modify the disease.

The other nine top-ranked predictions show the same pattern. They include brachyolmia, pseudoachondroplasia, myosclerosis, WHIM syndrome and hereditary hair disorders. All have scores between 0.983 and 0.997, all are Level L5, and none has trial or literature support or an established mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Ibuprofen has 20 valid single-ingredient registrations in Singapore and none cancelled. The approved indication text is not recorded for any of them. The main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10707P | Spedifen 400 Sachet 400 mg/sachet | Granule, for solution | Not recorded |
| SIN05464P | Ibufen Tablets 200 mg | Tablet, film coated | Not recorded |
| SIN14587P | Nurofen Tablet 400 mg | Tablet, sugar coated | Not recorded |
| SIN16467P | B. Braun Ibuprofen Solution for Infusion 4 mg/ml | Infusion, solution | Not recorded |
| SIN14561P | Nurofen Express Liquid Capsule 400 mg | Capsule, liquid filled | Not recorded |

Other registered forms include suspensions and syrups (for example Nurofen for Children and Brufen) as well as further tablets.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label-based safety information.

- **Conditions flagged in the knowledge graph (not label text):** The drug-disease contraindication links in the TxGNN knowledge graph cover many conditions. The main groups are:
  - Cardiovascular and cerebrovascular: hypertension, hypotension, myocardial infarction, stroke, cerebral infarction.
  - Gastrointestinal: peptic ulcer disease, inflammatory bowel disease.
  - Kidney and liver: kidney disease, liver disease, liver failure.
  - Bleeding and blood: blood coagulation disease, thrombocytopenia.
  - Others: epilepsy, COPD, systemic lupus erythematosus, diabetes mellitus, diabetic ketoacidosis, hypothyroidism, potassium deficiency, benign prostatic hyperplasia, substance abuse/dependence.
- **Drug interactions:** The interaction screen found 100 interacting drugs, and the first 20 returned are summarised here.
  - **Major:** acetylsalicylic acid (aspirin).
  - **Moderate:**
    - Corticosteroids: betamethasone, budesonide, dexamethasone, hydrocortisone.
    - Sulfonylurea antidiabetics: acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide.
    - Others: aprepitant, balsalazide, dexfenfluramine, fenfluramine, exenatide, kanamycin, levofloxacin.
  - **Minor:** famotidine, ranitidine, cimetidine.
- **Condition-specific caution:** For WHIM syndrome (rank 9), NSAIDs could theoretically worsen cytopenia-related risks, so caution would be required.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. It has no clinical trials, no literature, no known mechanistic link between COX inhibition and the disease, and the evidence level is L5. Ibuprofen is well established and widely marketed in Singapore, but that does not support this new indication.

**To proceed, the following is needed:**
- Mechanism of action data for ibuprofen, and a biological rationale linking it to the GDF5/CDMP1 pathway or to skeletal development
- Preclinical studies, such as cell or animal models of the disease, to test any disease-modifying effect
- A literature and trial search to confirm that no relevant studies exist
- The Singapore package insert, to establish approved indications, warnings and contraindications
- A clear definition of the intended goal. If it is symptomatic pain relief, this should be treated as standard NSAID use, not as repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

