---
layout: default
title: Imiglucerase
parent: Medium Evidence (L3-L4)
nav_order: 519
evidence_level: L4
indication_count: 10
---

# Imiglucerase
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Imiglucerase: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

Imiglucerase is a recombinant glucocerebrosidase enzyme (Cerezyme) used as enzyme replacement therapy, most likely for Gaucher disease.
The TxGNN model predicts it may be effective for **Hurler syndrome**, but there are **0 clinical trials** and only **2 general publications** on lysosomal enzyme replacement therapy (ERT), neither with imiglucerase-specific data for this disease.
The evidence for this prediction is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (inferred from the enzyme's function; the Singapore record has no indication text) |
| Predicted New Indication | Hurler syndrome (MPS I) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on known biochemistry, imiglucerase is a recombinant human glucocerebrosidase (GBA). It breaks down glucosylceramide, the substance that accumulates in Gaucher disease.

The mechanistic link to Hurler syndrome is weak. Hurler syndrome is caused by a deficiency of a different enzyme, alpha-L-iduronidase (IDUA), which leads to glycosaminoglycan buildup. Imiglucerase does not supply the missing enzyme and does not act on the accumulating substrate. The only shared concept is that both are lysosomal storage diseases treated with ERT.

The very high TxGNN score most likely reflects how closely lysosomal storage diseases sit to each other in the knowledge graph, not a drug-specific mechanism. Treat it as a hypothesis, not a supported finding.

The same problem applies to Scheie syndrome (score 99.29%), an attenuated form of MPS I. Other high-scoring predictions, such as Wolman disease and cholesteryl ester storage disease, involve a different enzyme (lysosomal acid lipase) that already has its own dedicated ERT.

One lower-ranked prediction is notable: **lysosomal storage disease with skeletal involvement** (rank 6, score 98.94%). It maps to Gaucher disease with bone involvement and has an evidence level of L3. That is very likely the drug's existing labeled use, so it is probably not true repurposing and should be checked against the label.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de médecine interne | Overview of ERT for lysosomal storage diseases. It traces the move from placenta-derived alglucerase to recombinant imiglucerase for Gaucher disease. No imiglucerase-specific data for Hurler syndrome. |
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Other (ERT imaging) | Proceedings of the National Academy of Sciences | PET imaging of enzyme replacement therapy. Mentions Hurler syndrome among diseases where ERT has been used, but does not test imiglucerase in it. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN13842P | Cerezyme® (Imiglucerase) 400U Powder for solution for injection (Genzyme Ireland Ltd) | Injection, powder, for solution |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted use in Hurler syndrome has no clinical trials and no drug-specific literature. Imiglucerase replaces a different enzyme from the one missing in this disease, so the high TxGNN score is not backed by a plausible mechanism.

**To proceed, the following is needed:**
- The HSA package insert (indications, warnings, contraindications), which is also needed to confirm the original indication
- Detailed mechanism of action data from DrugBank
- Evidence of any biochemical activity of glucocerebrosidase against MPS I substrates, which is currently unsupported
- Separate review of the "lysosomal storage disease with skeletal involvement" prediction, to confirm whether it is an on-label Gaucher indication rather than repurposing

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

