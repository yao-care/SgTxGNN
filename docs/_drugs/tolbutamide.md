---
layout: default
title: Tolbutamide
parent: Low Evidence (L5)
nav_order: 1002
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tolbutamide: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Tolbutamide"
predicted_indications: ["opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis", "autoimmune oophoritis"]
---

# Tolbutamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Tolbutamide: From Type 2 Diabetes Mellitus to Opsismodysplasia
{: .text-alpha }

## One-Sentence Summary

Tolbutamide is a sulfonylurea originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia** (a rare skeletal dysplasia), but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** directly supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (the registered indication text for the Singapore licences is blank) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 96.77% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for tolbutamide were not available in the data compiled for this report. Tolbutamide is known as a sulfonylurea that closes ATP-sensitive potassium (KATP) channels in pancreatic beta cells, which stimulates insulin secretion. Its efficacy in type 2 diabetes is established.

Opsismodysplasia is a skeletal dysplasia caused by INPPL1 mutations (SHIP2 deficiency), which affect PI3K/insulin signalling. A link to tolbutamide is only speculative. No mechanistic connection has been established, and the high score reflects a graph-based association rather than a therapeutic rationale.

Other top-ranked predictions show the same pattern. Stiff person syndrome and thiamine-responsive syndromes are linked mainly through diabetes comorbidity. The lipodystrophies appear to reflect an insulin/metabolic network association. Pancreatic agenesis is biologically implausible, because tolbutamide needs functional beta cells. Autoimmune oophoritis scored lower (77%) and has no identified mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for opsismodysplasia, the top prediction. The only literature retrieved was for the ninth-ranked prediction, pancreatic agenesis. It covers general sulfonylurea and beta-cell biology rather than treatment of that condition.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15115830](https://pubmed.ncbi.nlm.nih.gov/15115830/) | 2004 | Clinical/genetic study | N Engl J Med | Activating KCNJ11 (Kir6.2) mutations cause permanent neonatal diabetes, showing the role of KATP channels |
| [3057892](https://pubmed.ncbi.nlm.nih.gov/3057892/) | 1988 | Review | Am J Med | Hyperinsulinemia and insulin responses, including to tolbutamide, in non-insulin-dependent diabetes |
| [791727](https://pubmed.ncbi.nlm.nih.gov/791727/) | 1975 | Review | Diabete & metabolisme | Diabetes mellitus secondary to liver disease |
| [180358](https://pubmed.ncbi.nlm.nih.gov/180358/) | 1976 | Case series | Mayo Clin Proc | Clinical and diagnostic features of 60 insulinoma cases |
| [23274908](https://pubmed.ncbi.nlm.nih.gov/23274908/) | 2013 | Not classified | Diabetes | Congenital hyperinsulinism caused by hexokinase I expression or a glucokinase-activating mutation |
| [10482920](https://pubmed.ncbi.nlm.nih.gov/10482920/) | 1999 | Preclinical (islets) | Br J Pharmacol | Sulphonylurea pretreatment disturbs Ca2+ regulation and insulin secretion in mouse islets |
| [9519717](https://pubmed.ncbi.nlm.nih.gov/9519717/) | 1998 | Preclinical (animal) | Diabetes | Streptozotocin/nicotinamide rat model of NIDDM with responsiveness to sulfonylureas |
| [6114005](https://pubmed.ncbi.nlm.nih.gov/6114005/) | 1981 | Preclinical (animal) | Diabetes | Islet secretion in a neonatal streptozotocin rat model of non-insulin-dependent diabetes |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04045P | TOBUMIDE TABLET 500 mg | Tablet | Not stated in the registration record |
| SIN04257P | TOLMIDE TABLET 500 mg | Tablet | Not stated in the registration record |

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** kidney disease, liver disease, gallbladder disease, hepatic porphyria, Addison disease and chronic primary adrenal insufficiency, thymus gland disease, substance abuse/dependence, and a wide range of pituitary deficiency and hypogonadotropic hypogonadism conditions (e.g., hypopituitarism, growth hormone deficiency, Kallmann syndrome, Sheehan syndrome).
- **Drug Interactions:** 100 interactions were identified, and 20 are shown in the data. Most are Moderate, and a few topical corticosteroids are Minor. Notable moderate ones include:
  - Beta-agonists and sympathomimetics: epinephrine, salbutamol, formoterol, phenylephrine, pseudoephedrine
  - Beta-blocker: acebutolol
  - Acid suppressants: famotidine, ranitidine
  - NSAIDs: ibuprofen, ketorolac
  - Others: hydrochlorothiazide, acetazolamide, ethanol, ethinylestradiol, hydrocortisone, acitretin, albiglutide, nitazoxanide

Package insert warnings were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 96.77% TxGNN score is not backed by any clinical trial or literature, and no plausible mechanism connects KATP channel blockade to INPPL1-related skeletal dysplasia. Evidence is L5 (model prediction only). None of the other nine predictions has stronger support.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently a blocking gap for safety screening)
- Detailed mechanism of action data (MOA) from DrugBank
- Preclinical or mechanistic evidence linking tolbutamide to SHIP2/INPPL1 or PI3K signalling in skeletal development
- Approved indication text for the two Singapore licences, which is currently blank
- Assessment of route compatibility and similarity to the original indication, both still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

