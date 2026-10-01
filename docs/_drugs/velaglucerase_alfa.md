---
layout: default
title: Velaglucerase Alfa
parent: Low Evidence (L5)
nav_order: 1049
evidence_level: L5
indication_count: 10
---

# Velaglucerase Alfa
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

# Velaglucerase alfa: From Gaucher Disease to Steel Syndrome

## One-Sentence Summary

Velaglucerase alfa is a recombinant glucocerebrosidase enzyme replacement therapy, used for Gaucher disease. The TxGNN model predicts it may be effective for **Steel syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it. The prediction is most likely a knowledge-graph artifact, so we recommend holding it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (the Singapore registration record gives no indication text, so this comes from the drug's known use and the Evidence Pack rationale) |
| Predicted New Indication | Steel syndrome |
| TxGNN Prediction Score | 97.0% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, velaglucerase alfa is a recombinant form of the lysosomal enzyme glucocerebrosidase. It replaces the deficient enzyme in Gaucher disease so that glucosylceramide can be broken down.

Steel syndrome is a connective tissue and skeletal disorder caused by a collagen defect (*COL27A1*). It has no known link to glucosylceramide metabolism or lysosomal enzyme deficiency, and no mechanistic link was identified. The high score (0.970, rank 21,318) is probably a knowledge-graph artifact rather than a real biological signal. Because the route compatibility and similarity-to-original-indication checks are still pending, the prediction has not been assessed further.

The other top-ranked predictions have similar problems:
- **Esophageal varices (with and without bleeding) and varicose disease:** The only link is that Gaucher disease can cause splenomegaly and, rarely, portal hypertension. Enzyme replacement does not act on variceal pathophysiology.
- **Hypophosphatasia, Wolman disease and cholesteryl ester storage disease:** The link is class-level only (enzyme replacement or lysosomal storage). Each condition has a different enzyme deficiency and its own targeted therapy (asfotase alfa, sebelipase alfa).
- **Ichthyosis syndrome, STAT5B-related growth hormone insensitivity and proximal myopathy with extrapyramidal signs:** The links are hypothesis-level at best or absent.

None of these predictions has clinical trial or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16107P | VPRIV Powder for Solution for Infusion 400 Units/Vial | Injection, powder, lyophilized, for solution | Not provided in the registration record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no clinical trials or publications, and no plausible mechanistic link between glucocerebrosidase replacement and a *COL27A1*-related collagen disorder. A high TxGNN score by itself is not enough to justify further investment.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis connecting glucocerebrosidase activity to Steel syndrome pathophysiology
- Preclinical or clinical evidence, or at least relevant published literature
- Singapore package insert warnings and contraindications, which are missing from the current record
- Detailed mechanism of action data from DrugBank
- A route compatibility assessment, which is still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

