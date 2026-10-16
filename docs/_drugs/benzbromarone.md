---
layout: default
title: Benzbromarone
parent: Medium Evidence (L3-L4)
nav_order: 145
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Benzbromarone: predicted new indication Hypouricemia, renal (evidence level L4). Approved use: Gout"
---

# Benzbromarone
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

# Benzbromarone: From Gout and Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Benzbromarone is a uricosuric drug (a URAT1 inhibitor) originally used to treat gout and hyperuricemia.
The TxGNN model predicts it may be effective for **renal hypouricemia**, but there are **no registered clinical trials** and **19 publications**, all of which describe the disease rather than test benzbromarone as a treatment.
Mechanistically, the prediction points in the wrong direction, so it should be treated as a likely model artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; hyperuricemia (obsolete hyperuricemia entry in the knowledge graph). The Singapore licence carries no indication text. |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 99.07% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, benzbromarone inhibits URAT1 (SLC22A12), the transporter that reabsorbs urate in the kidney. This raises urinary urate excretion and lowers serum urate, which is why it is used in gout.

Renal hypouricemia is mainly caused by loss-of-function variants in URAT1 or GLUT9 (SLC2A9). These variants cause excessive urinary urate loss and abnormally low serum urate. Benzbromarone would therefore push in the same direction as the disease and would aggravate the phenotype rather than treat it.

The high TxGNN score most likely reflects the strong association between the drug and urate transport. It does not reflect therapeutic benefit. Benzbromarone appears in the literature on this condition mainly as a **diagnostic probe**. Together with pyrazinamide, it is used in suppression tests to classify the type of urate transport defect (for example, presecretory reabsorption defects). Patients with this condition are also prone to exercise-induced acute kidney injury and urate nephropathy, so using a uricosuric drug could be harmful.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 19 publications found are mostly descriptive. None evaluates benzbromarone as a treatment for renal hypouricemia. The 10 most relevant are listed below. Reviews and cohort studies are listed first, followed by case reports and series.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative update on the causes, diagnosis and clinical features of hypouricemia (serum urate < 2 mg/dL) |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Review | Nihon Rinsho | Concept and classification of urate metabolism abnormalities, including hyperuricemia and hypouricemia |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort | J Am Soc Nephrol | SLC22A12 (URAT1) sequencing in 32 patients with renal hypouricemia, linking genotype to urinary urate excretion |
| [10879667](https://pubmed.ncbi.nlm.nih.gov/10879667/) | 2000 | Case series | Clinical Nephrology | Renal hypouricemia with recurrent exercise-induced acute renal failure and chronic renal dysfunction |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | Case series | J Pediatrics | Four children with hereditary renal hypouricemia; benzbromarone did not change urate clearance ratios in most patients |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Case report | Am J Kidney Dis | Two brothers with hereditary renal hypouricemia and exercise-induced acute renal failure |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | Case report | Acta Paediatrica | Recurrent exercise-induced acute renal failure; a benzbromarone/pyrazinamide test indicated a presecretory reabsorption defect |
| [8893184](https://pubmed.ncbi.nlm.nih.gov/8893184/) | 1996 | Case report | Nephron | Urate transport analysis in Fanconi syndrome with marked renal hypouricemia, using pyrazinamide and benzbromarone |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | Case report | Nephron | Isolated renal urate transport defect; urate clearance rose further after benzbromarone |
| [12862209](https://pubmed.ncbi.nlm.nih.gov/12862209/) | 2003 | Case report | Hypertension Research | Exercise-induced acute renal failure in idiopathic renal hypouricemia during losartan and trichlormethiazide therapy |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06371P | NARCARICIN MITE TABLET 50 mg | Tablet (oral) | Not stated in the registration data |

---

## Safety Considerations

- **Hepatotoxicity**: The data compiled for this report show that benzbromarone has a known hepatotoxicity concern. This is particularly relevant in liver-related or metabolic conditions and in mitochondrial disorders.
- **Kidney risk in renal hypouricemia**: Patients with this condition already have a predisposition to exercise-induced acute kidney injury and urate nephropathy. A further uricosuric effect could add to this risk.

No label-based warnings, contraindications or drug interaction data were available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Benzbromarone lowers serum urate, so it would worsen renal hypouricemia rather than treat it. The 19 publications are descriptive reports and diagnostic uses, with no efficacy evidence and no clinical trials.
- The other nine predictions (Lesch-Nyhan syndrome, partial HPRT deficiency, familial hypercholesterolemia, glycogen storage diseases, TCA cycle disorder, portal hypertension and portal vein thrombosis) have no supporting trials. Their literature is minimal or absent, and they are either mechanistically implausible or carry a hepatotoxicity concern. Their evidence levels are L4 to L5, and all are Hold.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, since safety screening cannot proceed without them
- Mechanism of action data for benzbromarone
- A clear mechanistic rationale for why a URAT1 inhibitor could benefit any predicted indication, followed by preclinical or clinical evidence of benefit
- A dedicated safety assessment of liver and kidney risk in the target populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

