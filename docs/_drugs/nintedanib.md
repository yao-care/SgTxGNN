---
layout: default
title: Nintedanib
parent: Low Evidence (L5)
nav_order: 707
evidence_level: L5
indication_count: 10
---

# Nintedanib
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

# Nintedanib: From Its Singapore-Registered Use to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Nintedanib is an oral kinase inhibitor marketed in Singapore as OFEV soft capsules, but the supplied data does not state its approved indication.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**, a rare soft-tissue sarcoma.
So far this is a computational prediction only, with **0 clinical trials** and **0 publications** in the evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on general pharmacology, nintedanib inhibits several receptor tyrosine kinases: PDGFR, VEGFR and FGFR. These pathways drive fibroblast proliferation, migration and angiogenesis. This mechanistic reasoning comes from general knowledge, not from the supplied data.

DFSP is typically driven by a COL1A1-PDGFB gene fusion, which causes constant PDGFR-beta signalling. A drug that blocks PDGFR could therefore plausibly act on this tumour. Even so, the link is only a hypothesis. No trial or publication was supplied to support it, and the very high TxGNN score is a computational output, not clinical proof.

The other top predictions form two groups:
- **Sarcoma and fibroblastic tumours** (liposarcoma, conventional fibrosarcoma, fibroblastic neoplasm, and organ-specific fibrosarcoma or liposarcoma subtypes). Their rationale is inherited from the same kinase-inhibitor hypothesis, and it is indirect for the rare organ-specific subtypes.
- **Genetic skeletal and ALS-related entries** (axial spondylometaphyseal dysplasia, ALS type 22, ALS susceptibility). No credible mechanistic link is apparent, and these scores likely reflect knowledge-graph artefacts. The source name "amyotrohpic lateral sclerosis type 22" also contains a spelling error, which may hamper entity matching in later searches.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14922P | OFEV Soft Capsules 150mg | Capsule, liquid filled (oral) | Not provided in the supplied data |
| SIN14921P | OFEV Soft Capsules 100mg | Capsule, liquid filled (oral) | Not provided in the supplied data |

Both products are packaged by Catalent Germany Eberbach GmbH and Boehringer Ingelheim Pharma GmbH & Co. KG.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is at level L5: the only support is a model score, with no trials, no literature and no mechanism data in the pack. DFSP has a plausible PDGFR-based rationale and could be kept as a research question. The safety data is also missing, so the candidate cannot move to safety screening yet.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications and the approved indication), which currently blocks safety screening
- Mechanism of action data from DrugBank (DB09079)
- Targeted searches for trials and publications on nintedanib or PDGFR inhibitors in DFSP and soft-tissue sarcoma
- Resolution of broad or misspelled disease terms (for example "fibroblastic neoplasm" and "amyotrohpic") into specific entities
- Assessment of route compatibility, since only an oral capsule is registered in Singapore

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

