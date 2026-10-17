---
layout: default
title: Pyridostigmine
parent: Medium Evidence (L3-L4)
nav_order: 843
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Pyridostigmine: predicted new indication Myasthenia gravis with thymus hyperplasia (evidence level L4). Approved use: Myasthenia gravis, adult-onset myasthenia gravis…"
monitor_inn: "Pyridostigmine"
predicted_indications: ["hypersplenism (disease)", "atypical hemolytic-uremic syndrome with B factor anomaly", "fetal akinesia deformation sequence", "myasthenia, congenital, refractory to acetylcholinesterase inhibitors", "congenital myasthenic syndrome with tubular aggregates"]
---

# Pyridostigmine
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

# Pyridostigmine: From Myasthenia Gravis to Myasthenia Gravis with Thymus Hyperplasia

## One-Sentence Summary

Pyridostigmine is a cholinesterase inhibitor originally used for symptomatic treatment of myasthenia gravis and related neuromuscular junction disease.
The TxGNN model predicts it may be effective for **myasthenia gravis with thymus hyperplasia**, but this is essentially a subtype of the already established indication rather than a true repurposing case.
Currently there are **0 clinical trials** and **3 publications** (a review, a case report and a cohort study, none testing pyridostigmine in this subgroup) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myasthenia gravis, adult-onset myasthenia gravis, neuromuscular junction disease (the Singapore licence text lists no approved indication) |
| Predicted New Indication | Myasthenia gravis with thymus hyperplasia |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, pyridostigmine is a reversible acetylcholinesterase inhibitor. It slows the breakdown of acetylcholine, so more acetylcholine is available at the neuromuscular junction. This is the established symptomatic mechanism in myasthenia gravis.

Thymic hyperplasia is common in myasthenia gravis with acetylcholine receptor (AChR) antibodies. The predicted indication is therefore a subtype of the original one, and the same mechanism applies. The supplied literature (a review of MG genomics, a MuSK-positive case report, and a thymectomy outcome cohort) does not directly test pyridostigmine in this subgroup. The prediction is mechanistically reasonable, but the benefit over the current indication is unproven.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25683765](https://pubmed.ncbi.nlm.nih.gov/25683765/) | 2015 | Cohort | Journal of Neurology | Two-year outcomes of thymectomy in 39 patients with non-thymomatous, AChR-positive late-onset MG; thymectomy was reported as effective |
| [34225443](https://pubmed.ncbi.nlm.nih.gov/34225443/) | 2021 | Review | Molecular Medicine Reports | Genomic, phenotypic and epigenetic insights into MG pathology and autoimmunity |
| [18053719](https://pubmed.ncbi.nlm.nih.gov/18053719/) | 2008 | Case report | Neuromuscular Disorders | MuSK-positive MG with thymus hyperplasia presenting with dropped head syndrome |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN02898P | MESTINON TABLET 60 mg | Tablet, sugar coated (oral) | Not listed in the available record |

## Safety Considerations

- **Contraindications (from knowledge-graph disease associations, not package insert text)**: kidney disease, pyoureter, asthma (including intrinsic and allergic asthma), urinary tract obstruction.
- **Drug Interactions**: 78 interactions were identified. The 20 shown in the data are all Moderate level. They include:
  - Anticholinergics: atropine, scopolamine, hyoscyamine, glycopyrronium, dicyclomine, propantheline, trospium, clidinium, methscopolamine, mepenzolate.
  - Corticosteroids: hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone.
  - Aminoglycosides: neomycin, kanamycin, paromomycin.
- Please refer to the package insert for warnings and formal contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is a subtype of the established use of pyridostigmine in myasthenia gravis, and the mechanism is plausible. However, there are no trials and no literature that directly test pyridostigmine in myasthenia gravis with thymus hyperplasia, so evidence remains at L4.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (not currently available; this blocks formal safety screening)
- Approved indication wording for the Singapore licence
- Detailed mechanism of action data from DrugBank
- Subgroup data on pyridostigmine response in AChR-positive MG with thymic hyperplasia, including patients before and after thymectomy
- A review of the interaction and disease-contraindication list (especially asthma, urinary obstruction and kidney disease) in patient selection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

