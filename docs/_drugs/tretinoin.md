---
layout: default
title: Tretinoin
parent: Low Evidence (L5)
nav_order: 1009
evidence_level: L5
indication_count: 10
---

# Tretinoin
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

# Tretinoin: From Retinoid Therapy (Acne and Leukaemia Formulations) to Rheumatoid Nodulosis

## One-Sentence Summary

Tretinoin is a retinoid marketed in Singapore as topical creams and an oral capsule. The registry records do not state a formal indication.
The TxGNN model ranks **rheumatoid nodulosis** as its top prediction, but this prediction is **model-only**, with **0 clinical trials** and **0 publications**.
Among the ten predictions, only **osteoarthritis** has any supporting literature. That literature is preclinical and conflicting, with no human trials of tretinoin.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registry records. The products are a topical cream and an oral capsule (Vesanoid), which are typically used for acne and acute promyelocytic leukaemia. This is general knowledge, not taken from the registry. |
| Predicted New Indication | Rheumatoid nodulosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 (5 listed in the data) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tretinoin is a retinoic acid receptor (RAR) agonist, and retinoids affect cell differentiation and immune modulation. This is the only mechanistic basis available. Nothing in the supplied data links it to the biology of rheumatoid nodules.

The top ten predictions are mostly inflammatory arthritis and skeletal conditions. Several are near-synonyms of one another, such as the juvenile idiopathic arthritis entries. The high scores (about 99.3–99.8%) likely reflect closeness within the same disease cluster of the knowledge graph. They do not reflect independent evidence. One entry is a genetic susceptibility node rather than a treatable condition.

Osteoarthritis (score 99.44%) is the only prediction with a mechanistic story, and the evidence points in conflicting directions:
- Genetic and GWAS-derived work suggests retinoic acid signalling may be anti-inflammatory and protective in cartilage.
- A 2025 study of retinoic acid-induced osteoarthritis suggests a possible harm signal at high exposure.

Dose, route (topical or systemic) and direction of effect remain unresolved.

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid nodulosis, or for any of the other nine predicted indications.

## Literature Evidence

No related literature is available for rheumatoid nodulosis.

The table below shows the most relevant publications for the **osteoarthritis** prediction (rank 7). These are preclinical or genetic studies, and none is a tretinoin trial. Only 10 of the 20 retrieved publications were visible for review, and the other 10 should be screened before any evidence upgrade.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36542696](https://pubmed.ncbi.nlm.nih.gov/36542696/) | 2022 | Genetic association with preclinical validation | Sci Transl Med | ALDH1A2 variants (the retinoic acid synthesis enzyme) are linked to severe hand osteoarthritis. This supports an anti-inflammatory role for retinoic acid. |
| [37418291](https://pubmed.ncbi.nlm.nih.gov/37418291/) | 2023 | Genetic / in silico analysis | DNA Cell Biol | Proposes retinoic acid metabolism blocking agents to suppress mechanoflammation in osteoarthritis. |
| [40564983](https://pubmed.ncbi.nlm.nih.gov/40564983/) | 2025 | Preclinical (RNA-seq, network pharmacology, docking) | Int J Mol Sci | Models retinoic acid-induced osteoarthritis, so it is a possible harm signal. |
| [38302538](https://pubmed.ncbi.nlm.nih.gov/38302538/) | 2024 | In vitro | Sci Rep | Tests a retinoic acid analogue on BMP-driven stem cell chondrogenesis. |
| [15946654](https://pubmed.ncbi.nlm.nih.gov/15946654/) | 2005 | In vitro | Biochem Pharmacol | All-trans retinoic acid blocks cytokine-induced MMP production in human chondrocytes via JNK-AP-1 signalling. |
| [12505482](https://pubmed.ncbi.nlm.nih.gov/12505482/) | 2003 | In vitro | Osteoarthritis Cartilage | Runx2 expression in chondrocytes is regulated by retinoid signalling and PTHrP. |

For folliculitis decalvans (rank 10), the single retrieved paper ([PMID 27814407](https://pubmed.ncbi.nlm.nih.gov/27814407/), 2016, *Cutis*) is a case report on a related but distinct condition. It does not mention tretinoin, so it is not counted as evidence.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08057P | VESANOID CAPSULE 10 mg | Capsule | Not stated in registry record |
| SIN16390P | TRETINON CREAM 0.05% W/W | Cream | Not stated in registry record |
| SIN12368P | RETRIEVE CREAM 0.05% w/w | Cream | Not stated in registry record |
| SIN08095P | RETACNYL 0.025 CREAM 0.025% | Cream | Not stated in registry record |
| SIN08098P | RETACNYL 0.05 CREAM 0.05% | Cream | Not stated in registry record |

## Safety Considerations

- **Paediatric concern**: For the juvenile arthritis predictions, the evidence review notes that systemic retinoids carry skeletal toxicity risks in children.
- **Possible harm signal**: One 2025 preclinical study models retinoic acid-induced osteoarthritis, which suggests possible harm at high exposure.

Please refer to the package insert for warnings, contraindications and drug interaction information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions rest on model scores alone or on indirect preclinical evidence, and there are no human interventional data for tretinoin in any of them. Osteoarthritis is the only candidate worth keeping as a research question (evidence level L4), and its direction of effect is still unclear.

**To proceed, the following is needed:**
- The package insert warnings and contraindications from the HSA website
- Mechanism of action data (for example from the DrugBank API)
- Screening of the other 10 osteoarthritis publications that were not visible for review
- A decision on route and dose (topical versus systemic) and on the direction of effect in cartilage
- Approved indication text for the Singapore licences
- Paediatric skeletal safety assessment before any juvenile arthritis candidate is considered

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

