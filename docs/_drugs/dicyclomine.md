---
layout: default
title: Dicyclomine
parent: Low Evidence (L5)
nav_order: 324
evidence_level: L5
indication_count: 10
---

# Dicyclomine
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

# Dicyclomine: From Functional Bowel Disorders to Cauda Equina Syndrome

## One-Sentence Summary

Dicyclomine is an antimuscarinic antispasmodic, generally used for functional bowel disorders such as irritable bowel syndrome. The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Functional bowel disorders (general drug knowledge; the Singapore registration records list no indication text) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on known pharmacology, dicyclomine is an antimuscarinic agent that also relaxes smooth muscle directly. Its efficacy in gastrointestinal spasm is long established. Mechanistically, it could plausibly act on bladder or bowel dysfunction, which is a major feature of cauda equina syndrome.

The link is indirect. Cauda equina syndrome is a neurological emergency caused by compression of the lumbosacral nerve roots. Its definitive management is surgical decompression, not drug therapy. At most, dicyclomine could relieve some downstream symptoms such as bladder or bowel spasm. The high TxGNN score reflects graph-based association, not clinical evidence. No trial or publication supports this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN10344P | ACOLIC SYRUP | Syrup |
| SIN03333P | COLIMIX SYRUP | Syrup |
| SIN10845P | MECLOSIL TABLET | Tablet |
| SIN02547P | VERAGEL-DMS TABLET | Tablet |

The registration records provided do not include approved indication text.

## Safety Considerations

Please refer to the package insert for safety information.

For context, a 1953 case report in the literature linked to other predicted indications describes acute glaucoma in a patient with peptic ulcer treated with dicyclomine. Anticholinergic activity may also affect cognition and attention, particularly in children.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score of 99.66%, with no clinical trials or literature and only an indirect mechanistic link. The standard treatment for cauda equina syndrome is surgical, so a drug-repurposing role is unlikely to be more than symptomatic.

Two other predictions have some evidence, but only historical:
- Gastroduodenitis (1 report from 1956).
- Peptic ulcer disease (reports from 1950 to 1984).

These are low-quality, largely 1950s reports, and current care has moved to acid suppression and H. pylori eradication. They look more like historical indications than new repurposing opportunities.

**To proceed, the following is needed:**
- The HSA package insert, to obtain warnings and contraindications and the approved indication text (the current blocking gap).
- Mechanism of action data, for example from the DrugBank API.
- A clinical rationale for a symptomatic role in cauda equina syndrome, plus any supporting trial or literature search.
- Remapping of the obsolete "neurogenic bladder" term to a current ontology term before further review.
- Route compatibility and similarity-to-original assessments, both still pending.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

