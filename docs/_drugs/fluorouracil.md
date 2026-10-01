---
layout: default
title: Fluorouracil
parent: Low Evidence (L5)
nav_order: 438
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracil: From Established Cancer Chemotherapy to Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Fluorouracil is a fluoropyrimidine chemotherapy drug that is marketed in Singapore as injections and a topical solution.
The TxGNN model predicts it may be effective for **botryoid-type embryonal rhabdomyosarcoma of the vagina**, but **no clinical trials and no publications** currently support this specific prediction. It is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Singapore registration data (all approved-indication fields are blank) |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Fluorouracil is a fluoropyrimidine antimetabolite. It inhibits thymidylate synthase and is incorporated into RNA and DNA, so it acts on rapidly dividing tumour cells.

Rhabdomyosarcoma is a fast-growing soft tissue sarcoma, mostly seen in children. A cytotoxic antimetabolite therefore has a plausible biological rationale.

The very high score most likely comes from graph propagation from the parent disease node (rhabdomyosarcoma) rather than from data specific to this vaginal subtype. Fluorouracil is also not a standard agent in rhabdomyosarcoma regimens. The rationale is theoretical only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN05050P | DBL Fluorouracil Injection BP 50mg/mL | Injection | Hospira Australia Pty Ltd |
| SIN09904P | Fluorouracil Injection 50 mg/ml | Injection | Pharmachemie BV |
| SIN04266P | Verrumal Solution | Solution | Almirall Hermal GmbH |

The registration records do not include approved-indication text.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Medium (neutropenia, thrombocytopenia and mucositis are recognised toxicities of systemic use) |
| Emetogenicity Classification | Low to moderate for the injectable form |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes. Consider DPD deficiency risk before systemic use |
| Handling Protection | Injectable products must follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for full details.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). There are no trials or publications for this subtype, and fluorouracil is not a standard agent in rhabdomyosarcoma. Extrapolation from the parent disease node is weak for a rare vaginal subtype.

**To proceed, the following is needed:**
- Subtype-specific or rhabdomyosarcoma-specific clinical evidence for fluorouracil
- HSA package insert warnings and contraindications for a safety screen
- Detailed mechanism of action data from DrugBank
- Approved-indication text for the Singapore licences
- Assessment of route compatibility (injectable versus topical) for the target disease

The parent condition, **rhabdomyosarcoma**, is a somewhat better-supported research question (L4). It has only indirect, old (1973–1991) general chemotherapy literature and no fluorouracil-specific trials, so it is best treated as a research question rather than an actionable candidate.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

