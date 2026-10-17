---
layout: default
title: Glyburide
parent: Low Evidence (L5)
nav_order: 485
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Glyburide: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Glyburide"
predicted_indications: ["opsismodysplasia", "focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis", "autoimmune oophoritis"]
---

# Glyburide
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

# Glyburide: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Glyburide is a sulfonylurea originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.
The evidence is currently weak, and the prediction should be treated as a hypothesis, not a finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (from the knowledge graph; the Singapore licences carry no indication text) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 97.24% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, glyburide is a sulfonylurea that closes ATP-sensitive potassium (KATP) channels on pancreatic beta cells and stimulates insulin secretion. Its efficacy in type 2 diabetes is well established.

For opsismodysplasia, no mechanistic link is supported by the data. The disease is a skeletal dysplasia caused by mutations in INPPL1 (SHIP2), a negative regulator of PI3K/insulin signalling. The high TxGNN score (0.97) most likely reflects proximity in the knowledge graph (insulin-signalling-related neighbours), not a demonstrated therapeutic effect. Any link would be speculative.

### Other Predicted Indications (All Hold)

The same conclusion applies to the other nine predictions. None has clinical trials, and only pancreatic agenesis has any literature, which is indirect.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Focal stiff limb syndrome | 96.90% | L5 | Likely driven by the link between stiff-person spectrum disorders and autoimmune (anti-GAD) diabetes, not a therapeutic mechanism |
| 3 | Classic stiff person syndrome | 96.90% | L5 | Same reasoning as rank 2; the identical score suggests shared graph neighbours |
| 4 | Thiamine-responsive dysfunction syndrome | 96.77% | L5 | Probably reflects the diabetes feature of the syndrome; insulin is the usual treatment and no evidence was supplied |
| 5 | Drug-induced localized lipodystrophy | 95.22% | L5 | No plausible mechanism; adipose tissue disorder versus a pancreatic KATP blocker |
| 6 | Centrifugal lipodystrophy | 94.92% | L5 | Likely metabolic/insulin-resistance graph proximity only |
| 7 | Pressure-induced localized lipoatrophy | 94.79% | L5 | Mechanically induced fat loss; insulin secretagogue activity has no clear relevance |
| 8 | Idiopathic localized lipodystrophy | 94.47% | L5 | No demonstrated mechanism |
| 9 | Pancreatic agenesis | 94.34% | L4 | Little or no beta-cell mass for a secretagogue to act on; the retrieved papers are indirect |
| 10 | Autoimmune oophoritis | 82.22% | L5 | No mechanistic rationale; lowest score in the set |

## Clinical Trial Evidence

Currently no related clinical trials registered for opsismodysplasia or any of the other nine predicted indications.

## Literature Evidence

No literature is available for opsismodysplasia. The only literature retrieved for any of the predictions relates to pancreatic agenesis (rank 9). These papers are all preclinical, in vitro, ex vivo or veterinary, and provide no evidence of glyburide efficacy in that condition.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9033963](https://pubmed.ncbi.nlm.nih.gov/9033963/) | 1996 | Preclinical/Basic research | Acta Diabetologica | Prolonged glucose exposure alters beta-cell sensitivity and causes desensitization |
| [8603773](https://pubmed.ncbi.nlm.nih.gov/8603773/) | 1996 | Preclinical (rat islets) | Diabetes | Glucose-induced desensitization in rat islets reverses quickly and involves ionic fluxes |
| [7937694](https://pubmed.ncbi.nlm.nih.gov/7937694/) | 1994 | Preclinical (animal) | Pancreas | Aged rat beta cells show abnormal insulin release, tested with secretagogues including glyburide |
| [21573217](https://pubmed.ncbi.nlm.nih.gov/21573217/) | 2011 | In vitro study | PLoS One | ENPP1 affects insulin signalling and secretion in liver, muscle and beta-cell lines |
| [15742701](https://pubmed.ncbi.nlm.nih.gov/15742701/) | 2005 | Case report (veterinary) | J Am Vet Med Assoc | Diabetes mellitus in an aged Spanish Mustang mare, with low insulin and C-peptide |
| [41693148](https://pubmed.ncbi.nlm.nih.gov/41693148/) | 2026 | Ex vivo islet functional study | J Clin Endocrinol Metab | Islet function in patients with Beckwith-Wiedemann syndrome and congenital hyperinsulinism |

## Singapore Market Information

All six licences are valid, single-ingredient oral products. No approved indication text is recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN07284P | BENIL TABLET 5 mg | Tablet | Sunward Pharmaceutical Private Limited |
| SIN07380P | CLAMIDE TABLET 5 mg | Tablet | Hovid Bhd |
| SIN10998P | T.O.NIL TABLET 5 mg | Tablet | T O Chemicals (1979) Ltd |
| SIN04842P | APO-GLYBURIDE TABLET 5 mg | Tablet | Apotex Inc |
| SIN04206P | GLIMIDE TABLET 5 mg | Tablet | Beacons Pharmaceuticals Pte. Ltd. |

A sixth licence, SIN12322P (GLUCOVANCE TABLET 500 mg/5 mg, film-coated, Merck Santé SAS), is also valid.

## Safety Considerations

- **Disease contraindications (knowledge-graph based, not label text)**: Liver failure, liver disease, kidney disease, gallbladder disease, pyoureter, adrenocortical insufficiency and Addison disease, thymus gland disease, infectious disease, and a wide group of pituitary-deficiency and hypogonadotropic hypogonadism disorders (including hypopituitarism, Sheehan syndrome, Kallmann syndrome and growth hormone deficiencies).
- **Drug Interactions**: The interaction query returned 100 records; the 20 reviewed are mostly **Moderate**, with a few **Minor**.
  - Moderate: phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol, acebutolol, acetazolamide, famotidine, ranitidine, acitretin, ketorolac, ibuprofen, ethinylestradiol, hydrocortisone, albiglutide, ethanol, nitazoxanide, abametapir (topical).
  - Minor: topical hydrocortisone, topical alclometasone.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score of 0.97 for opsismodysplasia is a knowledge-graph prediction only, with no clinical trials or literature. The mechanism of glyburide (pancreatic KATP channel closure) has no evident connection to the INPPL1-related skeletal pathology. The other nine predictions are similarly unsupported. The best-supported one, pancreatic agenesis, is only weakly evidenced and is mechanistically implausible.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which is a blocking gap for safety screening
- Detailed mechanism of action data (MOA) from DrugBank
- Mechanistic or preclinical evidence linking KATP channel modulation or sulfonylurea action to SHIP2/INPPL1 biology
- Any case reports, trials or literature in opsismodysplasia before considering reassessment
- Review of the interaction profile and disease contraindications if any indication advances
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

