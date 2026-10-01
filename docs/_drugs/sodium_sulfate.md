---
layout: default
title: Sodium Sulfate
parent: Low Evidence (L5)
nav_order: 913
evidence_level: L5
indication_count: 10
---

# Sodium Sulfate
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

# Sodium Sulfate: From Osmotic Laxative to Dyspepsia

## One-Sentence Summary

Sodium sulfate is an osmotic laxative. It is registered in Singapore as a component of a bowel-preparation oral solution, but the registry entry does not state an indication.
The TxGNN model predicts it may be effective for **dyspepsia** with a very high graph score, but **none of the 3 retrieved clinical trials and none of the 4 retrieved publications actually test sodium sulfate for dyspepsia**.
The prediction is model-only (L5), and the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore record (the drug is an osmotic laxative) |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available. Sodium sulfate is an osmotic laxative: it draws water into the bowel lumen and is used in bowel cleansing. The Singapore product is an oral granule for solution.

The evidence does not support a mechanistic link between bowel cleansing and dyspepsia. Sodium sulfate has no known role in treating upper-GI discomfort. The 99.09% score is a knowledge-graph association and should not be read as evidence of efficacy. Most of the retrieved literature concerns dextran sodium sulfate (DSS), a chemical used to induce colitis in animals, which is a different compound from the drug.

---

## Clinical Trial Evidence

All three trials were graded C (weak relevance). None studies sodium sulfate for dyspepsia.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06339697](https://clinicaltrials.gov/study/NCT06339697) | Phase 4 | Completed | 194 | Compared the effects of two bowel-preparation laxatives on gut microbiome recovery in patients with colonic polyps. It is related to bowel preparation but does not study dyspepsia. |
| [NCT07310927](https://clinicaltrials.gov/study/NCT07310927) | Phase 2/3 | Recruiting | 140 | Alginate vs sucralfate for GERD symptom relief alongside PPIs. Sodium sulfate is not an intervention; this is a keyword match only. |
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | Unknown | 150 | Oxycodone vs pregabalin for preemptive postoperative analgesia. Unrelated to the drug and the indication. |

---

## Literature Evidence

All four publications are animal studies (DSS colitis models). None is a clinical study of sodium sulfate.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [33918638](https://pubmed.ncbi.nlm.nih.gov/33918638/) | 2021 | Animal study | Molecules | DSS-induced intestinal injury in pigs altered donepezil pharmacokinetics and gastric myoelectric activity. Dyspepsia appears only as a donepezil side effect. |
| [34207410](https://pubmed.ncbi.nlm.nih.gov/34207410/) | 2021 | Animal study | Pharmaceuticals | DSS-induced injury further aggravated galantamine's effect on gastric myoelectric activity in pigs. |
| [36614242](https://pubmed.ncbi.nlm.nih.gov/36614242/) | 2023 | Animal study | Int J Mol Sci | Atractylodin, a herbal compound, reduced colitis in mice via PPARα agonism. Dyspepsia is mentioned only as a traditional use of the herb. |
| [40391232](https://pubmed.ncbi.nlm.nih.gov/40391232/) | 2025 | Animal study | J Inflamm Res | Si-Ni Decoction, a traditional Chinese formula, improved ulcerative colitis in a DSS model through gut microbiota modulation and AKT1 inhibition. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09234P | FORTRANS FOR ORAL SOLUTION (BEAUFOUR IPSEN INDUSTRIE) | Granule, for solution | Not provided in the record |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The dyspepsia prediction rests only on a graph score. There is no credible mechanism, no relevant clinical trial, and no relevant clinical literature. The other nine predicted indications (including dry eye syndrome, stomach disease and bronchitis) are also at L5 or L4 and on Hold.

**To proceed, the following is needed:**
- The HSA package insert, to obtain approved indications, warnings and contraindications. This is currently a blocking gap for safety screening.
- Mechanism-of-action data from DrugBank, to test whether any mechanistic link to dyspepsia exists.
- Any clinical study that actually uses sodium sulfate as the intervention in dyspepsia. Without one, the prediction should not advance beyond screening.
- Route and formulation compatibility. The only registered product is a bowel-preparation oral solution, and its fit for a dyspepsia indication has not been assessed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

