---
layout: default
title: Rivastigmine
parent: Low Evidence (L5)
nav_order: 870
evidence_level: L5
indication_count: 10
---

# Rivastigmine
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

# Rivastigmine: From Alzheimer's Dementia to Glaucoma

## One-Sentence Summary

Rivastigmine is a cholinesterase inhibitor used for dementia, and the literature in this pack describes it as established treatment for Alzheimer's disease and Parkinson's disease dementia. The TxGNN model predicts it may help with **glaucoma**. The support is **no clinical trials** and **3 publications**, only one of which is an actual study (in rabbits), so this is an early-stage research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records; literature describes Alzheimer's disease and Parkinson's disease dementia |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L4 (preclinical/mechanism evidence only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. From the literature, rivastigmine inhibits acetylcholinesterase and butyrylcholinesterase, which raises acetylcholine levels. This is why it is used in Alzheimer's disease and Parkinson's disease dementia.

In the eye, higher acetylcholine acts on the ciliary muscle and trabecular meshwork. This increases aqueous humour outflow and lowers intraocular pressure (IOP), the same logic as cholinergic agents such as pilocarpine. A 2000 rabbit study found that topical rivastigmine lowered IOP in normotensive animals.

There is a gap between the original and new use. The only human evidence is indirect, and no clinical trials exist. Oral or transdermal use is not a validated route for glaucoma, so any move forward would need a topical ocular formulation with its own safety and tolerability work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Preclinical animal study (rabbit) | J Ocul Pharmacol Ther | Topical rivastigmine, a selective carbamate-type AChE inhibitor, lowered intraocular pressure in normotensive rabbits |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Systems genetics analysis and review | Front Mol Biosci | Reviews cholinergic agents for IOP reduction. Approved M3 agonists lower IOP but cause systemic cholinergic adverse effects, so understanding the eye's cholinergic system matters |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Review (patent literature) | Expert Opin Ther Pat | Notes that mild AChE inhibition has therapeutic relevance in Alzheimer's disease, myasthenia gravis and glaucoma |

## Singapore Market Information

Seven registrations exist; five are shown below. Approved indication text is not recorded in these licence entries.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN13450P | Exelon Patch 5 (4.6mg/24hr) | Patch, extended release |
| SIN13451P | Exelon Patch 10 (9.5mg/24hr) | Patch, extended release |
| SIN10036P | Exelon Capsule 3 mg | Capsule |
| SIN10037P | Exelon Capsule 4.5 mg | Capsule |
| SIN10038P | Exelon Capsule 6 mg | Capsule |

## Safety Considerations

Please refer to the package insert for safety information.

- Systemic oral or transdermal use is not a validated route for glaucoma.
- A topical ocular formulation would need its own safety and tolerability assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score is backed only by one rabbit study and two general reviews. There are no clinical trials, no human efficacy data, and no suitable ocular formulation. Package insert safety data are also missing, which blocks the safety screening step.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (download and parse from the HSA website)
- Detailed mechanism of action data (query the DrugBank API)
- Confirmation of the original approved indication in the Singapore licence records
- Human or further preclinical evidence of IOP lowering, plus a feasibility and ocular safety assessment for a topical formulation
- Evaluation of primary hereditary glaucoma (also predicted) only after the general glaucoma question is resolved

The other nine predictions (including acute intermittent porphyria and several movement disorders) have no supporting evidence and are all on Hold. For the movement disorders, the available literature points to a possible adverse-effect signal rather than benefit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

