---
layout: default
title: Isoleucine
parent: Low Evidence (L5)
nav_order: 550
evidence_level: L5
indication_count: 10
---

# Isoleucine
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

# Isoleucine: From Parenteral Amino Acid Nutrition Component to Gastroparesis

## One-Sentence Summary

Isoleucine is an essential branched-chain amino acid, marketed in Singapore mainly as a component of intravenous amino acid infusions.
The TxGNN model predicts it may be effective for **gastroparesis**, but the prediction rests on model output alone, with **0 clinical trials** and **0 publications** retrieved for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records; the listed products are parenteral amino acid infusions (nutritional supply) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 19 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Isoleucine is an essential amino acid, and it is used in parenteral nutrition products as a protein building block. No known mechanism links it to delayed gastric emptying.

The prediction most likely reflects proximity in the knowledge graph rather than a demonstrated biological link. Related gut-motility diseases (familial visceral myopathy, intestinal pseudo-obstruction) also scored highly, which points to the same pattern.

The nearest supporting signals are indirect and belong to a neighbouring predicted indication, dyspepsia. Metabonomic studies report altered plasma amino acid profiles in functional dyspepsia, and a rat barostat study found that amino acids influence gastric adaptive relaxation. Neither shows that isoleucine supplementation helps patients, and neither concerns gastroparesis directly.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for gastroparesis.

## Singapore Market Information

19 registrations exist. The 5 main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16337P | AMINOVEN SOLUTION FOR INFUSION 15% | Infusion, solution | Fresenius Kabi Austria GmbH (Graz) |
| SIN11682P | AMINOVEN SOLUTION FOR INFUSION 5% | Injection | Fresenius Kabi Austria GmbH |
| SIN11829P | AMINOVEN SOLUTION FOR INFUSION 10% | Injection | Fresenius Kabi Austria GmbH |
| SIN06299P | NEPHROSTERIL FOR INTRAVENOUS INFUSION | Injection | Fresenius Kabi Austria GmbH |
| SIN08352P | AMINOPLASMAL-15% INFUSION | Injection | B. Braun Melsungen AG |

All available forms are injectable or infusion products. Whether an oral or enteral route would be needed for gastroparesis has not been assessed.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gastroparesis prediction has a high model score but no trials, no literature and no known mechanism, so the evidence level is L5. The 19 Singapore registrations are all parenteral nutrition products, with no approved use related to gastric motility.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from the DrugBank API) to test any link to gastric motility
- A targeted literature search on branched-chain amino acids and gastric emptying or gastroparesis
- A route-compatibility assessment, since the marketed products are intravenous only

Among the other top-10 predictions, only **dyspepsia** has indirect supporting literature (L4, research question). It is a better candidate for further review than gastroparesis. The obsolete term "vitamin D deficiency" should be remapped to a current ontology term before any review.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

