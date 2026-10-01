---
layout: default
title: Cladribine
parent: Low Evidence (L5)
nav_order: 256
evidence_level: L5
indication_count: 10
---

# Cladribine
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

# Cladribine: From Unrecorded Original Indication to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is marketed in Singapore as MAVENCLAD 10 mg tablets, but the record does not state its approved indication.
The TxGNN model predicts it may be effective for **parameningeal embryonal rhabdomyosarcoma**, and the top six predictions all belong to the same rhabdomyosarcoma cluster.
There are **0 clinical trials** and **0 publications** for this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the registration data |
| Predicted New Indication | Parameningeal embryonal rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Cladribine is a deoxyadenosine analog. It is phosphorylated by deoxycytidine kinase and interferes with DNA synthesis and repair. Its clinical activity is mainly in lymphoid malignancies. The provided data contain no link between this mechanism and rhabdomyosarcoma, a solid tumour.

The high score appears to reflect the structure of the knowledge graph rather than drug-specific evidence. The top six predictions (parameningeal, vaginal botryoid, extrahepatic bile duct, prostate, and unspecified embryonal rhabdomyosarcoma, plus the parent term) are subtypes or anatomical variants of one disease cluster. They are correlated and should be read as a single signal, not six independent ones. If this direction is pursued, the parent term "rhabdomyosarcoma" is the sensible starting point, for example preclinical cladribine activity in rhabdomyosarcoma cell lines.

Among the other predictions, gestational trophoblastic neoplasm has a class-level rationale, because antimetabolite chemotherapy is standard in that disease. That is not evidence for cladribine itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

The only publication anywhere in the candidate list is a 2004 case report of cladribine in smoldering systemic mastocytosis ([15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/)). It is attached to the lower-ranked prediction "liver sarcoma". Its title does not mention liver sarcoma, so it is at most indirect evidence.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15691P | MAVENCLAD TABLET 10MG | Tablet | Not listed in the record |

Manufacturer: NerPharMa S.R.L. / R-Pharm Germany GmbH. Route: oral only.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog, antimetabolite) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert; follow local cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried records.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every prediction is at evidence level L5 or L4, with no trials and no directly relevant literature. The rhabdomyosarcoma predictions are one correlated cluster, and the mechanism gives no support for a solid-tumour indication.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications, approved indication), which is currently a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- Preclinical evidence of cladribine activity in rhabdomyosarcoma models, searched under the parent term
- A biological justification for the low-plausibility predictions, such as pleural adenomatoid tumor, before any further consideration

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

