---
layout: default
title: Glutamic Acid
parent: Low Evidence (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
---

# Glutamic Acid
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

# Glutamic Acid: From Parenteral Nutrition Amino Acid to Postmenopausal Osteoporosis

## One-Sentence Summary

Glutamic acid is an amino acid ingredient in parenteral nutrition (IV amino acid) solutions marketed in Singapore. The registration records do not state an approved indication, so this role is inferred from the product types.
The TxGNN model predicts it may be useful for **postmenopausal osteoporosis**. The search found **1 clinical trial** and **10 publications**, but none of them tests glutamic acid itself as a treatment for this condition. The prediction is therefore a research question, not a supported therapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records; the registered products are IV amino acid nutrition solutions |
| Predicted New Indication | Postmenopausal osteoporosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 (indirect and preclinical evidence only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for glutamic acid. It is a proteinogenic amino acid and a component of multi-amino-acid infusion products. The registration records give no approved indication text, so no established efficacy in an original indication can be cited.

The link to osteoporosis is indirect. Vitamin K-dependent enzymes convert glutamate residues in bone proteins (osteocalcin, matrix Gla protein) into γ-carboxyglutamate. That supports the role of vitamin K, not supplementation with glutamic acid. Two other weak signals exist:
- A related polymer, poly-γ-glutamic acid, affected calcium absorption in a small study of postmenopausal women.
- One ovariectomized mouse study reported that glutamic acid improved estrogen-deficiency symptoms.

The high score (0.993) most likely reflects knowledge-graph closeness to the vitamin K and bone-metabolism network. It does not reflect direct evidence about glutamic acid.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00048061](https://clinicaltrials.gov/study/NCT00048061) | Phase 3 | Completed | 1609 | Compares monthly oral ibandronate (100 mg, 150 mg) with 2.5 mg daily in postmenopausal osteoporosis. Glutamic acid is not an intervention, so this trial does not support the prediction. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19172219](https://pubmed.ncbi.nlm.nih.gov/19172219/) | 2009 | Randomized open-label study | J Bone Miner Metab | In 109 patients, 6 months of vitamin K2 (menatetrenone) increased osteocalcin γ-carboxylation. It tested vitamin K2, not glutamic acid. |
| [14529146](https://pubmed.ncbi.nlm.nih.gov/14529146/) | 2003 | Clinical review | Keio J Med | Vitamin D3 and/or K2 treatment for postmenopausal osteoporosis; vitamin K2 acts on glutamic acid residues in bone proteins. |
| [14584089](https://pubmed.ncbi.nlm.nih.gov/14584089/) | 2003 | Clinical review | Yonsei Med J | Vitamin K2 combined with bisphosphonates in postmenopausal osteoporosis. |
| [18187428](https://pubmed.ncbi.nlm.nih.gov/18187428/) | 2007 | Small clinical study | J Am Coll Nutr | Poly-γ-glutamic acid acutely affected calcium absorption in postmenopausal women. It is a related polymer, not glutamic acid. |
| [26144993](https://pubmed.ncbi.nlm.nih.gov/26144993/) | 2015 | Preclinical (mouse) | Nutr Res | Glutamic acid ameliorated menopausal-like symptoms in ovariectomized mice. |
| [34529430](https://pubmed.ncbi.nlm.nih.gov/34529430/) | 2021 | Preclinical | Nano Lett | A bone-targeting polymer vesicle (polyglutamic acid-based) delivers estradiol. Glutamic acid is only a material component. |
| [29437025](https://pubmed.ncbi.nlm.nih.gov/29437025/) | 2018 | Genetic association | Endocr Metab Immune Disord Drug Targets | VKORC1 polymorphism and osteoporosis in postmenopausal women; supports the role of vitamin K. |
| [18414001](https://pubmed.ncbi.nlm.nih.gov/18414001/) | 2008 | Genetic association | Mol Cells | SLC22A11 (hOAT4) variants in Korean women with osteoporosis. |
| [40950804](https://pubmed.ncbi.nlm.nih.gov/40950804/) | 2025 | Cross-sectional metabolomics | J Diabetes Metab Disord | Amino acid profiles, aging and sex hormones in elderly Iranians. |
| [11668761](https://pubmed.ncbi.nlm.nih.gov/11668761/) | 2001 | Dietary review | Tidsskr Nor Laegeforen | Short summary on vitamin K in the Norwegian diet and osteoporosis. |

---

## Singapore Market Information

The registration records list no approved indication text. The seven registrations are all injectable or infusion products. The five main ones are:

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN08352P | Aminoplasmal-15% Infusion | Injection |
| SIN07846P | Trophamine Injection 10% | Injection |
| SIN07428P | Vaminolact Intravenous Solution | Injection |
| SIN15411P | Aminoplasmal B.Braun 10% E Solution for Infusion | Infusion, solution |
| SIN16734P | Nutriflex Omega Special B. Braun Emulsion for Infusion | Injection, emulsion |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried database.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only trial retrieved tests an unrelated drug (ibandronate). The supporting literature is about vitamin K, a related polymer, or a single mouse study. The high TxGNN score is not backed by direct evidence for glutamic acid in osteoporosis. The other nine predicted indications are also at Hold, with the following notes:
- **Glaucoma:** the literature points toward glutamate excitotoxicity, which argues against supplementation.
- **Several other predictions:** they are prediction-only or retrieval noise.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical bone-outcome data (bone mineral density, bone turnover markers) for glutamic acid itself, beyond the single ovariectomized mouse study
- A rationale for an oral or supplemental route, since all current Singapore products are IV nutrition solutions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

