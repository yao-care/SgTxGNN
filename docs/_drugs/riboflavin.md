---
layout: default
title: Riboflavin
parent: 僅模型預測 (L5)
nav_order: 856
evidence_level: L5
indication_count: 10
---

# Riboflavin
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

# Riboflavin: From Vitamin B2 Supplementation to Biotin Metabolic Disease

## One-Sentence Summary

> Riboflavin (Vitamin B2) is a water-soluble vitamin conventionally used to prevent and correct riboflavin deficiency; it is not currently marketed in Singapore and has no on-file approved indication.
> The TxGNN model's top prediction is **Biotin Metabolic Disease** (score 94.88%), supported by **9 clinical trials** and **19 publications**,
> but the drug's own evidence pack flags a likely **mechanistic mismatch** — the underlying signal appears driven by co-occurrence in newborn metabolic-screening literature rather than a direct pharmacological pathway.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — riboflavin is not marketed in Singapore. As general background, riboflavin (Vitamin B2) is conventionally used to prevent/treat riboflavin deficiency. |
| Predicted New Indication | Biotin Metabolic Disease |
| TxGNN Prediction Score | 94.88% |
| Evidence Level | L4 (mechanism/preclinical-level; clinical trials are largely indirect, C-grade relevance) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for riboflavin is not available in this evidence pack. Based on known pharmacology, riboflavin is the precursor of FAD and FMN, cofactors required by mitochondrial flavoproteins — including multiple acyl-CoA dehydrogenases. This pathway is well established as the basis for treating **riboflavin-responsive multiple acyl-CoA dehydrogenase deficiency (RR-MADD)**.

However, the target predicted here — **biotin metabolic disease** — reflects a defect in biotin/biotinidase metabolism (multiple carboxylase deficiency), a mechanistically distinct pathway for which riboflavin is not a standard treatment. The evidence pack's own rationale explicitly flags this: the high TxGNN score likely arises because riboflavin and biotin frequently co-occur in the same clinical context (newborn screening panels and combined pediatric metabolic-disease vitamin regimens), rather than from a genuine shared mechanism.

This distinction matters for decision-making: the clinical trials and literature retrieved largely concern general micronutrient/vitamin-B-complex supplementation or newborn screening programs, not biotin metabolic disease treatment specifically. The prediction should be treated as a hypothesis-generating signal requiring target validation, not as mechanistically confirmed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | N/A | Completed | 40 | Multi-micronutrient palliative intervention in CHF patients; not disease-specific to biotin metabolism |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6,824 | Universal genomic newborn screening program (Baby Detect); includes but is not limited to biotin/riboflavin-responsive disorders |
| [NCT03655223](https://clinicaltrials.gov/study/NCT03655223) | N/A | Enrolling by Invitation | 30,000 | Early Check newborn screening platform for rare treatable conditions |
| [NCT02302729](https://clinicaltrials.gov/study/NCT02302729) | N/A | Completed | 1,730 | Micronutrient powder vs. placebo for childhood stunting in Guatemala |
| [NCT04586348](https://clinicaltrials.gov/study/NCT04586348) | Phase 4 | Active, not recruiting | 794 | Prenatal iodine supplementation and neurodevelopment RCT |
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Phase 2 | Unknown | 1,000 | Fortified food vs. milk on micronutrient status in malnourished children |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | N/A | Completed | 30 | Pilot crossover study: natural vs. synthetic vitamin B-complex bioavailability |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Transdermal vitamin absorption in post-bariatric surgery patients |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Completed | 75 | Vitamin/mineral supplementation for neuropathy/nephropathy in Type 2 diabetes |

**Note:** None of these trials directly enroll or treat biotin metabolic disease patients; relevance is indirect (general vitamin supplementation, screening infrastructure).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40258084](https://pubmed.ncbi.nlm.nih.gov/40258084/) | 2025 | Formulation Study | PLoS One | Compounded thiamine/riboflavin/pyridoxine/biotin capsules for pediatric metabolic disease treatment — most directly relevant hit, but addresses drug delivery, not efficacy |
| [37085971](https://pubmed.ncbi.nlm.nih.gov/37085971/) | 2023 | Case Report | J Investig Med High Impact Case Rep | Twin premature infants with combined riboflavin + biotin deficiency during prolonged parenteral nutrition, presenting with lactic acidosis and multiorgan failure |
| [39234898](https://pubmed.ncbi.nlm.nih.gov/39234898/) | 2024 | Review | Clin Pharmacol Ther | Rare diseases linked to mutations in vitamin transporters at the blood-brain barrier |
| [34797406](https://pubmed.ncbi.nlm.nih.gov/34797406/) | 2022 | Case Series | Human Genetics | SLC gene mutations and pediatric neurological disorders, including vitamin transporter defects |
| [7015958](https://pubmed.ncbi.nlm.nih.gov/7015958/) | 1980 | Review | Ann NY Acad Sci | Interactions of thiamin, riboflavin, and other B-vitamins in metabolic pathways |
| [40563372](https://pubmed.ncbi.nlm.nih.gov/40563372/) | 2025 | Preclinical Study | Antioxidants | Mitochondrial unfolded protein response activation in ethylmalonic encephalopathy cell models |
| [15231238](https://pubmed.ncbi.nlm.nih.gov/15231238/) | 2004 | Review | Ageing Res Rev | Heme biosynthesis requires vitamin B6, riboflavin, biotin, pantothenic acid, and lipoic acid; role in mitochondrial ageing |
| [33158037](https://pubmed.ncbi.nlm.nih.gov/33158037/) | 2020 | Review | Nutrients | B vitamins as enzyme cofactors in immune regulation and cancer biology |
| [40076592](https://pubmed.ncbi.nlm.nih.gov/40076592/) | 2025 | Review | Int J Mol Sci | Recent advances on B vitamins' role in cancer prevention and progression |
| [37189771](https://pubmed.ncbi.nlm.nih.gov/37189771/) | 2023 | Review | Biomedicines | Physiological associations between vitamin B deficiency and diabetic kidney disease |

**Note:** No RCTs specific to biotin metabolic disease treatment with riboflavin were identified; evidence is predominantly reviews and single case reports on general B-vitamin biology and co-deficiency states.

---

## Singapore Market Information

Riboflavin currently has **no registered product license in Singapore** (total licenses on file: 0). No market authorization data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug interaction data are flagged as blocking data gaps — TFDA/HSA label information has not yet been retrieved, per data gap DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (biotin metabolic disease) carries a documented mechanistic mismatch — riboflavin's established pathway (FAD/FMN-dependent flavoprotein disorders) does not directly explain treatment of biotin/biotinidase-pathway disease, and supporting evidence is indirect (screening programs, general supplementation trials, case reports of co-deficiency). Combined with the absence of Singapore market presence, missing MOA data, and missing label/safety data, the evidence base is not yet sufficient to advance past a research question.

**To proceed, the following is needed:**
- TFDA/HSA product label (warnings, contraindications) — currently a blocking gap (DG001)
- Confirmed mechanism of action via DrugBank API (DG002)
- Validation of the TxGNN disease-node mapping to rule out ontology/co-occurrence artifacts (biotin vs. riboflavin pathway confusion)
- If pursuing further, consider re-scoping toward rank 3 ("corneal pigmentation"), where the underlying evidence (44 trials, mostly on riboflavin/UVA corneal collagen cross-linking for keratoconus — an FDA-approved use) is substantially stronger, though the disease label itself also appears mismatched and needs verification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

