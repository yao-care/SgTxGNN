---
layout: default
title: Folic Acid
parent: 僅模型預測 (L5)
nav_order: 445
evidence_level: L5
indication_count: 10
---

# Folic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Folic Acid: From Folate Deficiency to Biotin Metabolic Disease

## One-Sentence Summary

Folic acid (Vitamin B9, DrugBank ID DB00158) is a vitamin conventionally used to treat and prevent folate deficiency and its associated megaloblastic anemia. The TxGNN model predicts a possible link to **Biotin Metabolic Disease**, supported by **13 clinical trials** and **20 publications**, but on closer review this evidence is largely indirect — most trials studied multi-nutrient/multi-vitamin regimens rather than folic acid alone, and no study directly evaluated folic acid as a treatment for biotin metabolic disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Folate deficiency / prevention of megaloblastic anemia (general pharmacological knowledge — not present as structured data in this evidence pack) |
| Predicted New Indication | Biotin Metabolic Disease |
| TxGNN Prediction Score | 99.49% (rank 6,600 among predictions) |
| Evidence Level | L4 (preclinical / mechanism-level and non-specific studies only) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for folic acid is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, folic acid acts as a cofactor for one-carbon transfer reactions required for DNA synthesis and methylation, and its established clinical role is treating/preventing folate deficiency, megaloblastic anemia, and neural tube defects in pregnancy.

Biotin metabolic disease, in contrast, results from defects in biotin-dependent carboxylase enzymes — a pharmacologically distinct pathway from folate one-carbon metabolism. The evidence pack's own mechanistic analysis for this candidate notes that folic acid and biotin serve as cofactors in different enzymatic reactions, and that no direct evidence links folic acid to the biotin metabolic pathway.

The most plausible explanation for this prediction is that the TxGNN knowledge graph and the retrieved literature frequently group folate and biotin together under the broader category of "vitamin-responsive metabolic disorders" (several review articles in the evidence discuss cobalamin, folate, biotin, and B-vitamins jointly as cofactor-deficiency syndromes). This topical co-occurrence likely drove the embedding similarity rather than a genuine pharmacological mechanism. Notably, the standard treatment for biotin metabolic disorders is biotin supplementation itself, not folic acid. This prediction should therefore be treated as a hypothesis-generating signal requiring independent mechanistic verification, not a validated repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Unknown | 200 | RCT of Q10 ubiquinol + multivitamin B/E complex in autism spectrum disorder / Phelan-McDermid syndrome — not specific to biotin metabolic disease |
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | N/A | Completed | 40 | Multi-micronutrient palliative intervention in congestive heart failure; graded low relevance — not a folic acid–specific trial |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6,824 | Newborn genomic screening program (Baby Detect) for 126 treatable genetic diseases — a diagnostic study, not a treatment trial |
| [NCT02302729](https://clinicaltrials.gov/study/NCT02302729) | N/A | Completed | 1,730 | Micronutrient powder vs. placebo for childhood stunting in Guatemala |
| [NCT04586348](https://clinicaltrials.gov/study/NCT04586348) | Phase 4 | Active, not recruiting | 794 | Prenatal iodine supplementation and neurodevelopment — vitamin/mineral supplement study, not biotin-disease specific |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Completed | 39 | Targeted nutritional intervention for oxidative stress/methylation imbalance in autism |
| [NCT04067921](https://clinicaltrials.gov/study/NCT04067921) | N/A | Unknown | 1,963 | Nutrigenomics platform studying diet–genome interactions and disease |
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Phase 2 | Unknown | 1,000 | Fortified food vs. milk in malnourished children; measured serum/erythrocyte folic acid and B12 among other markers |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | N/A | Completed | 30 | Pilot comparison of natural vs. synthetic vitamin B-complex bioavailability; graded low relevance |
| [NCT07350538](https://clinicaltrials.gov/study/NCT07350538) | N/A | Active, not recruiting | 20 | Gut microbiome/prebiotic intervention for alcohol addiction recovery — tangential relevance |

*Note: none of the retrieved trials directly test folic acid as a treatment for biotin metabolic disease; most are multi-nutrient supplementation studies in unrelated populations. Three additional lower-relevance trials (NCT03360435, NCT01558193, NCT01173315) were identified but omitted here for brevity.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Reviews vitamin-responsive disorders including cobalamin, folate, biotin, B1, and E deficiencies — the most directly relevant reference, but a general review rather than folic acid–specific evidence for biotin disease |
| [30557456](https://pubmed.ncbi.nlm.nih.gov/30557456/) | 2019 | Review | Movement Disorders | Reviews movement disorders in treatable inborn errors of metabolism, including biotin- and folate-responsive conditions |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Reviews vitamins interfering with inborn metabolic errors via malabsorption, metabolic errors, or vitamin-dependent syndromes |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Not classified | Pediatric Clinics of North America | Discusses B-complex vitamins as coenzymes in megavitamin-responsive aminoacidopathies |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Not classified | Ryoikibetsu Shokogun Shirizu | Discusses vitamin dependency syndromes |
| [779426](https://pubmed.ncbi.nlm.nih.gov/779426/) | 1976 | Not classified | Advances in Human Genetics | Discusses vitamin-responsive inherited metabolic disorders |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Not classified | International Journal of Molecular Sciences | Discusses vitamin B12's role as cofactor alongside biotin and folic acid in related biochemical reactions; not a treatment study |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Not classified | Archives of Biochemistry and Biophysics | Notes that deficiency of B12, folic acid, B6, C, or E can mimic radiation-induced DNA damage; general nutrition-health hypothesis, not disease-specific |
| [4279121](https://pubmed.ncbi.nlm.nih.gov/4279121/) | 1974 | Not classified | Biomembranes | Reviews absorption mechanisms of water-soluble vitamins |
| [16343871](https://pubmed.ncbi.nlm.nih.gov/16343871/) | 2006 | Not classified | Archives de Pédiatrie | Reviews metabolic disorders, including neonatal epilepsy from inborn errors of metabolism |

*Note: 10 additional lower-relevance publications (largely on vitamin B12/diabetes, dermatology, or unrelated topics) were identified but omitted here for brevity; none provide direct evidence of folic acid efficacy in biotin metabolic disease.*

---

## Singapore Market Information

Folic acid currently has no marketing authorization on record in Singapore under this dataset (market status: Not Marketed; total registrations: 0). No license-level product information is available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not available in the current evidence pack; a drug-drug interaction query returned no results.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between folic acid and biotin metabolic disease is weak and likely reflects literature co-classification (folate and biotin both appearing in "vitamin-responsive metabolic disorder" reviews) rather than a genuine pharmacological relationship. No clinical trial or publication directly evaluates folic acid as a treatment for biotin metabolic disease, and the established standard of care for this condition is biotin itself — evidence level is L4 (mechanism/preclinical-adjacent only), supporting a Hold decision.

**To proceed, the following is needed:**
- Drug label warnings/contraindications from the regulatory source (currently a Blocking data gap — required before any safety pre-assessment, S1, can begin)
- Detailed mechanism-of-action data for folic acid (currently a High-severity data gap)
- A dedicated mechanistic or clinical study directly testing folic acid (not multi-vitamin combinations, and not biotin) in patients with biotin metabolic disease
- Clarification of whether the TxGNN association reflects a genuine drug-disease relationship or a topical/co-mention artifact in the underlying knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

