---
layout: default
title: Ofloxacin
parent: Low Evidence (L5)
nav_order: 725
evidence_level: L5
indication_count: 10
---

# Ofloxacin
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

# Ofloxacin: From Antibacterial Use to Hyperamylasemia

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibacterial. The Singapore registration records supplied do not state the approved indication text.
The TxGNN model predicts it may be effective for **hyperamylasemia** (raised serum amylase), with a very high score of about 99.9%.
However, **no clinical trials and no publications** support this prediction, so it rests on the model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records (ofloxacin is a fluoroquinolone antibacterial) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.91% (model rank 1740) |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ofloxacin inhibits bacterial DNA gyrase and topoisomerase IV. This is an antibacterial action, and it has no known effect on serum amylase.

Hyperamylasemia is a laboratory finding, typically linked to pancreatic or salivary gland disorders, and it is not an infection. No mechanistic bridge between ofloxacin's antibacterial action and this condition has been identified. The high score most likely reflects proximity in the knowledge graph rather than a real pharmacological relationship.

Detailed mechanism-of-action data is also missing from the source record. The reading above comes from the known class pharmacology of fluoroquinolones.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Six licences are recorded in total; five are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11433P | OFLOX TABLET 200 mg | Film-coated tablet | Not recorded |
| SIN08409P | FUGACIN TABLET 200 mg | Film-coated tablet | Not recorded |
| SIN11377P | AKILEN TABLET 200 mg | Film-coated tablet | Not recorded |
| SIN10118P | OFCIN FILM COATED TABLET 400 mg | Film-coated tablet | Not recorded |
| SIN10119P | OFCIN FILM COATED TABLET 200 mg | Film-coated tablet | Not recorded |

All listed products are oral film-coated tablets.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature and no plausible mechanism. It is best treated as a knowledge-graph artifact rather than a repurposing lead.

**To proceed, the following is needed:**
- The HSA package insert, to confirm approved indications, warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Any evidence linking fluoroquinolone use to serum amylase, which would need a rationale before further work

**Other predictions for this drug:**
- Two other predictions have preclinical or indirect evidence (L4) and could be considered as research questions. These are monoclonal gammopathy, where the evidence is levofloxacin infection prophylaxis in myeloma, and septicemic plague, where the evidence is animal studies.
- Both are class-level signals. Neither shows ofloxacin treating the disease itself, and levofloxacin and ciprofloxacin already cover these uses.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

