---
layout: default
title: Allopurinol
parent: Low Evidence (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: From Hyperuricaemia/Gout to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is an oral tablet marketed in Singapore. The local licence records do not state its approved indication, but it is generally known as a gout and hyperuricaemia medicine. The TxGNN model predicts it may be effective for **hepatic porphyria**, but there are **0 clinical trials** and only **2 publications** (a hypothesis paper and a rat study). Neither publication tests allopurinol in porphyria, so the evidence is weak and the prediction should be treated as a lead only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (all indication fields are blank). Gout/hyperuricaemia is the commonly known use, not taken from the supplied data. |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 (preclinical and hypothesis-level literature only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this drug. Allopurinol is commonly known as a xanthine oxidase inhibitor, but this is not confirmed in the supplied data. No direct link between allopurinol and the liver heme-synthesis pathway can be established from the two retrieved papers.

The two papers concern heme biosynthesis and heme metabolism in general:
- A 2019 hypothesis paper proposes targeting 5-aminolevulinate synthase (the rate-limiting enzyme of heme synthesis) to treat acute hepatic porphyrias.
- A 1992 rat study examines how carbamazepine, a drug known to worsen porphyria, affects hepatic heme metabolism.

Neither is a study of allopurinol in porphyria. The direction of effect is unknown, and perturbing the heme pathway could be harmful in porphyria, so benefit cannot be assumed. The high score most likely reflects knowledge-graph proximity rather than disease-specific evidence. The relevance of both papers was judged from truncated titles and abstracts only, not full text.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Review | Medical Hypotheses | Proposes metabolic targeting of liver 5-aminolevulinate synthase, via tryptophan or inhibition of heme use by tryptophan 2,3-dioxygenase, as a therapy for acute hepatic porphyrias. Allopurinol is not shown to be involved. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preclinical (animal) | Biochemical Pharmacology | Acute carbamazepine dosing in rats depleted liver heme available to tryptophan pyrrolase, consistent with how it exacerbates hepatic porphyria. Not about allopurinol. |

## Singapore Market Information

The Evidence Pack shows 5 of the 8 registrations. Approved indication text is blank in all of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05804P | ALLOPURINOL TABLET 100 mg (Beacons Pharmaceuticals) | Tablet | Not stated in record |
| SIN07051P | YSP ALLOPURINOL TABLET 100 mg (Y S P Industries) | Tablet | Not stated in record |
| SIN06060P | ZYLORIC TABLET 100 mg (Aspen) | Tablet | Not stated in record |
| SIN06247P | APO-ALLOPURINOL TABLET 300 mg (Apotex) | Tablet | Not stated in record |
| SIN06248P | APO-ALLOPURINOL TABLET 100 mg (Apotex) | Tablet | Not stated in record |

## Safety Considerations

Please refer to the package insert for safety information. Package-insert warnings and contraindications have not yet been retrieved. Because porphyria patients are especially sensitive to drugs that disturb heme metabolism, this gap needs to be closed before any further work.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials, and the only two papers are a hypothesis paper and a rat study that do not involve allopurinol. Heme-pathway effects could plausibly worsen porphyria, and safety data has not been retrieved.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications, approved indication), which currently blocks safety screening
- Mechanism-of-action data from DrugBank
- A targeted literature search for direct allopurinol and porphyria evidence, including any case reports of porphyria exacerbation or improvement
- Full-text review of the two retrieved papers
- Review of the other nine predictions: hepatopulmonary syndrome, idiopathic copper-associated cirrhosis, early-onset familial noncirrhotic portal hypertension, primitive portal vein thrombosis, hepatoportal sclerosis, disorder of phenylalanine metabolism, immune-mediated necrotizing myopathy, antisynthetase syndrome and idiopathic eosinophilic myositis. All are also on Hold and have almost no supporting evidence. Several share the identical score 0.99943, which suggests a graph-embedding cluster effect.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

