---
layout: default
title: Probenecid
parent: Medium Evidence (L3-L4)
nav_order: 826
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Probenecid: predicted new indication Hypouricemia, renal (evidence level L4). Approved use: Gout"
monitor_inn: "Probenecid"
predicted_indications: ["hypouricemia, renal", "Lesch-Nyhan syndrome", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "cholelithiasis", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "disorder of phenylalanine metabolism"]
---

# Probenecid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Probenecid: From Gout to Renal Hypouricemia

## One-Sentence Summary

Probenecid is a uricosuric drug originally used to treat gout and hyperuricemia.
The TxGNN model predicts it may be effective for **renal hypouricemia**, but there are **no registered clinical trials** and the **20 publications** retrieved describe the disease itself rather than probenecid treatment.
The prediction is more likely a knowledge-graph artifact than a real therapeutic signal, and it may even point to a pharmacological contraindication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; hyperuricemia (the Singapore licence has no approved indication text on file) |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for probenecid are not available in the data compiled for this report. From known pharmacology, probenecid inhibits URAT1 (SLC22A12) and the OAT1/OAT3 transporters. This blocks renal urate reabsorption and increases uric acid excretion in urine, which is why it lowers serum urate in gout.

The predicted new indication does not fit this mechanism. Hereditary renal hypouricemia is mainly caused by loss-of-function variants in URAT1 (SLC22A12) or GLUT9. Patients already lose too much urate in urine, so a drug that further blocks reabsorption would be expected to **worsen** the condition rather than treat it. The literature also shows that probenecid has been used as a **diagnostic probe**. Patients with renal hypouricemia show little or no uricosuric response to probenecid, which helps classify the type of tubular defect.

The high TxGNN score most likely reflects network proximity through urate transport, not a therapeutic rationale. Other ranked predictions are also weak: Lesch-Nyhan syndrome and partial HPRT deficiency (uricosurics raise stone risk in these uric acid overproducers, and xanthine oxidase inhibitors are preferred), and a group of rare liver diseases with identical scores that look like graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 20 publications retrieved for renal hypouricemia cover the disease and its pathophysiology. None tests probenecid as a treatment. The main ones are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Mol Genet Metab | Hereditary renal hypouricemia is mostly caused by loss-of-function mutations in SLC22A12 (URAT1) |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clin Rheumatol | Narrative update on causes and clinical handling of hypouricemia |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort (genetic) | J Am Soc Nephrol | SLC22A12 sequencing in 32 Japanese patients linked URAT1 mutations to urate excretion |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Review/Case report | Am J Kidney Dis | Exercise-induced acute renal failure in renal hypouricemia and its prevention |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Case report | Nephron | Uric acid clearance responded only weakly to probenecid and pyrazinamide, indicating a tubular reabsorption defect |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | Case report | Arch Intern Med | Increased urate clearance in diabetic patients with renal hypouricemia |
| [1944743](https://pubmed.ncbi.nlm.nih.gov/1944743/) | 1991 | Case report | Nephron | Renal hypouricemia in 14 patients with type 1 diabetes |
| [9583212](https://pubmed.ncbi.nlm.nih.gov/9583212/) | 1998 | Case report | Acta Paediatr Jpn | Exercise-induced acute renal failure in a girl with renal hypouricemia |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07685P | Probenecid Tablet 500 mg (Sunward Pharmaceutical Private Limited) | Tablet (oral) | Not specified in the data compiled for this report |

---

## Safety Considerations

- **Contraindications from the knowledge graph** (these are graph-derived associations, not package insert text): liver failure, kidney disease and impaired renal function, peptic ulcer disease, and blood disorders such as thrombocytopenia, leukopenia, agranulocytosis and neutropenia (including congenital forms). Muscle disorders (myopathy, rhabdomyolysis) and diarrheal or colitis conditions (including *Clostridium difficile* colitis) also appear.
- **Drug interactions**: 71 interactions were recorded. Major ones include **phenylbutyric acid** and **glycerol phenylbutyrate**. Moderate ones include **acetylsalicylic acid** and the sulfonylurea/glinide antidiabetics (chlorpropamide, glimepiride, glipizide, glyburide, tolbutamide, tolazamide, acetohexamide, repaglinide, nateglinide). Minor ones include famotidine, amoxicillin, levofloxacin and eluxadoline.

Warnings and contraindications from the Singapore package insert are not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is not supported. Probenecid's uricosuric mechanism would be expected to aggravate renal hypouricemia, no trials exist, and the literature only describes the disease or uses probenecid as a diagnostic probe. The other predictions (Lesch-Nyhan syndrome, HPRT deficiency, cholelithiasis, rare liver diseases, phenylalanine metabolism disorders) have either no evidence or only diagnostic-use evidence. Several have a clear mechanistic disadvantage.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (HSA)
- Detailed mechanism-of-action data from DrugBank
- A pharmacological review confirming whether the prediction reflects a contraindication or diagnostic-use artifact
- If any indication is pursued, mechanistic or preclinical evidence of a therapeutic benefit, not just a diagnostic one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

