---
layout: default
title: Codeine
parent: Medium Evidence (L3-L4)
nav_order: 273
evidence_level: L4
indication_count: 10
---

# Codeine
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

# Codeine: From Cough and Pain Relief to Nasal Cavity Disease

## One-Sentence Summary

Codeine is an opioid used for cough suppression and pain relief. The Singapore registrations include cough linctus and codeine-containing analgesic tablets. The TxGNN model predicts it may be effective for **nasal cavity disease**, but **no clinical trials** exist and the only **2 publications** are case reports of harm from opioid misuse, not treatment benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (product types suggest cough and pain relief) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Codeine is a well-known opioid antitussive and analgesic, and its efficacy in cough and pain is established. However, no mechanism links it to treating disease of the nasal cavity.

The evidence does not support a therapeutic link. Both retrieved papers describe harm from opioid abuse. One is necrosis of the nasal cavity and pharynx after snorting hydrocodone-acetaminophen. The other is a rhinolith formed around a hardened codeine-opium mixture. The very high TxGNN score most likely reflects a disease-association artifact rather than a treatment signal.

Other candidates in this run are more plausible, although none has been validated. The best example is bronchial disease, where codeine's central cough-suppressing action is relevant. It also carries prominent safety signals, and no trial confirms codeine efficacy for it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22965281](https://pubmed.ncbi.nlm.nih.gov/22965281/) | 2012 | Case report (adverse event) | The Laryngoscope | Intranasal abuse of crushed hydrocodone-acetaminophen tablets caused necrosis of the nasal cavity and pharynx |
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report (adverse event) | Ear, Nose & Throat Journal | A rhinolith formed around an impacted foreign body, a hardened codeine-opium mixture (an "opioma"), causing nasal obstruction and foul-smelling discharge |

Both papers describe harm, not treatment benefit.

## Singapore Market Information

The registration data does not list approved indication text for these products. Five of the 20 authorizations are shown.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN03413P | COLINCTUS 10 MIXTURE 10 mg/5 ml | Elixir |
| SIN03699P | L.T.R. COUGH LINCTUS 10 mg/5 ml | Elixir |
| SIN07044P | CODEINE TABLETS 30 mg | Tablet |
| SIN06870P | Linctus Tussis Rubra 10mg/5ml | Elixir |
| SIN06330P | PARACETAMOL CODEINE TABLETS | Tablet |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone. The only literature shows nasal injury from opioid misuse, and there are no clinical trials or plausible mechanism for treating nasal cavity disease. Pursuing this indication is not justified.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed products
- Mechanism of action data
- Any human evidence that codeine treats a nasal cavity condition, which none of the retrieved evidence provides
- A re-prioritization of the other predicted indications (e.g., bronchial disease) that have a more plausible antitussive rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

