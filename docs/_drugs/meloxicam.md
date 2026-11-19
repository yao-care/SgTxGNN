---
layout: default
title: Meloxicam
parent: Low Evidence (L5)
nav_order: 645
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-12
description: "Meloxicam: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis…"
monitor_inn: "Meloxicam"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Meloxicam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Meloxicam: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type
{: .text-alpha }

## One-Sentence Summary

Meloxicam is a COX-2-preferential NSAID, originally used for rheumatoid arthritis, osteoarthritis and juvenile idiopathic arthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, spondyloarthropathy (the Singapore licence records contain no indication text) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 3 of 3) |
| Number of Registrations | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for meloxicam: "Meloxicam has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of Zybic™, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Zybic (meloxicam) prescribing information, Redmont Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a1c2d65f-ebb1-48bf-8fa1-c216f7d570ec), label version 2026-09-25; accessed 2026-11-19.) Meloxicam is a COX-2-preferential NSAID that reduces prostaglandin-mediated inflammation and pain. Its efficacy in inflammatory and degenerative joint diseases is well established.

Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal dysplasia caused by loss-of-function variants in CDMP1/GDF5, which affect chondrogenesis. Meloxicam has no known effect on the GDF5/BMP signalling pathway. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At most, an NSAID might relieve secondary joint pain, and this has not been studied.

Other top-ranked predictions show the same pattern. Most are rare genetic skeletal or developmental disorders (brachyolmia, pseudoachondroplasia, WHIM syndrome and others) with no plausible mechanistic link. The only entries with a credible connection overlap with meloxicam's existing indications. These are spondyloarthropathy susceptibility, rheumatoid nodulosis and rheumatoid factor-positive polyarticular juvenile idiopathic arthritis. Rheumatoid factor-positive polyarticular JIA is the only prediction with any supporting literature, and that is a general NSAID safety registry rather than evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN09554P | MOBIC TABLET 7.5 mg | TABLET | Valid |
| SIN12127P | MELOX TABLET 7.5 mg | TABLET | Valid |
| SIN14305P | Arrox Tablet 7.5mg | TABLET | Valid |

<!-- licenses:end -->

All three licences are valid single-ingredient oral tablets.

## Safety Considerations

- **Contraindications (from the TxGNN knowledge graph, not package insert text)**: hypertension and hypertensive disorders, congestive heart failure, heart disease and cardiovascular disease, myocardial infarction and coronary thrombosis, stroke and cerebrovascular disorders, kidney disease and impaired renal function, active peptic ulcer disease, gastritis, blood coagulation disease, anaemia and hemoglobinopathy, diabetes mellitus and diabetic ketoacidosis, hyperlipidaemia (including familial), and substance abuse/dependence.
- **Drug Interactions**: The interaction query returned 100 records. Most are of Moderate severity, and one (linaclotide) is Minor. Examples include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide.
  - Other anti-inflammatory drugs: acetylsalicylic acid, mesalazine, balsalazide.
  - Antidiabetic agents: metformin, glimepiride, chlorpropamide.
  - Others: aprepitant, vancomycin, kanamycin, potassium citrate, potassium bicarbonate, and bowel-preparation products.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (Evidence Level L5). There is also no plausible mechanistic link between COX inhibition and a GDF5-related skeletal dysplasia. It is most likely a TxGNN model (deep learning) artefact. Meloxicam's safety profile, with cardiovascular, renal and gastrointestinal cautions, adds further risk to any speculative use.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (HSA), which are required before any safety screening.
- Mechanism of action data from DrugBank.
- Any preclinical or clinical evidence linking COX inhibition to GDF5/BMP-related skeletal disease.
- If a lower-risk lead is wanted, review the rheumatoid factor-positive polyarticular JIA prediction. It overlaps with the existing indication and has one supporting safety paper, so it would be an extension of current use rather than true repurposing.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available from the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Zybic (meloxicam) prescribing information, Redmont Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a1c2d65f-ebb1-48bf-8fa1-c216f7d570ec) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

