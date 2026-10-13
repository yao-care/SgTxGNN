---
layout: default
title: L-Lysine
parent: Low Evidence (L5)
nav_order: 570
evidence_level: L5
indication_count: 10
---

# L-Lysine
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

# L-Lysine: From Parenteral Nutrition (Amino Acid Supply) to Gastroparesis

## One-Sentence Summary

L-Lysine is an essential amino acid used as a component of intravenous amino acid and parenteral nutrition products in Singapore.
The TxGNN model predicts it may be effective for **gastroparesis**, but there are **0 clinical trials** and only **1 publication** (a preclinical stem-cell delivery study that does not involve L-lysine as a treatment).
This prediction rests on the model score alone and should be treated as a hypothesis, not as supported evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records compiled for this report. The products are amino acid infusion and nutrition solutions. |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. L-lysine is an essential amino acid. It is part of parenteral nutrition and amino acid infusion products, and its role in protein supply is well established. Any mechanistic link to gastric motility is unproven.

The only retrieved paper concerns delivery of mesenchymal stem cells from gelatin-alginate hydrogels into the stomach lumen. It does not test L-lysine. The high TxGNN score is a computational prediction only, and no direct link between L-lysine and gastric emptying, interstitial cells of Cajal, or enteric neurons has been identified.

The other nine predicted indications were also reviewed. None has clinical trial support. Gastroparesis, vitamin deficiency disorder, renal tubular acidosis and biotin metabolic disease have some retrieved literature, but all of it is preclinical, case-report or indirect:

- **Vitamin deficiency disorder** (score 98.2%): the papers are basic biochemistry and animal studies on carnitine synthesis and biotinidase. They do not show that lysine treats deficiency. This is the only other candidate at evidence level L4.
- **Renal tubular acidosis** (score 97.8%): a case report describes a transient proximal tubulopathy after lysine-containing amino acid infusion. This is a safety signal, not support for repurposing.
- **Biotin metabolic disease** (score 97.8%): lysine is a product of the biotinidase reaction, but standard care is biotin, and the other papers are unrelated metabolomics studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29414870](https://pubmed.ncbi.nlm.nih.gov/29414870/) | 2018 | Preclinical | Bioengineering (Basel) | Mesenchymal stem cells delivered from gelatin-alginate hydrogels to the stomach lumen as a potential gastroparesis treatment. L-lysine is not the therapeutic agent. |

---

## Singapore Market Information

The approved indication text is not available in the licence records for any of these products.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16003P | LYSAKARE Solution for Infusion 25G/25G | Infusion, solution | Not stated |
| SIN11682P | AMINOVEN Solution for Infusion 5% | Injection | Not stated |
| SIN11829P | AMINOVEN Solution for Infusion 10% | Injection | Not stated |
| SIN06299P | NEPHROSTERIL for Intravenous Infusion | Injection | Not stated |
| SIN09353P | NUTRINEAL PD4 with 1.1% Amino Acid Solution | Solution, sterile | Not stated |

All seven registrations are valid single-ingredient licences. Two further products are OLICLINOMEL N7-1000 E and N4-550 E emulsions for infusion.

---

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: The TxGNN knowledge graph links L-lysine to contraindication-type relationships with the following conditions:
  - Kidney: kidney disease, chronic kidney disease, chronic renal failure syndrome, end-stage renal failure, acute urate nephropathy, nephrolithiasis, nephrocalcinosis
  - Calcium and phosphorus: hypercalcemia disease, humoral hypercalcemia of malignancy, sarcoidosis, phosphorus metabolism disease
  - Cardiac: heart disease, cardiovascular disease, digitalis poisoning, ventricular fibrillation
  - Metabolic: phenylketonuria, disorder of phenylalanine metabolism
- **Renal signal in the literature**: One case report (PMID 31876733) describes a transient proximal tubulopathy after amino acid infusion.

No drug interaction records were found. Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials, and the single retrieved paper does not involve L-lysine as a treatment. The knowledge graph also flags kidney and cardiac contraindication associations, which raise caution for a new use.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for L-lysine (for example from DrugBank)
- Approved indication text for the Singapore licences
- Direct preclinical or clinical evidence that L-lysine affects gastric motility or gastroparesis
- Route compatibility assessment: current products are intravenous or parenteral, and the suitability of this route for gastroparesis has not been evaluated
- Review of the renal and cardiac contraindication associations before any further work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

