---
layout: default
title: Trifluridine
parent: Low Evidence (L5)
nav_order: 1015
evidence_level: L5
indication_count: 10
---

# Trifluridine
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

# Trifluridine: From Metastatic Colorectal Cancer to Cecum Villous Adenoma

## One-Sentence Summary

Trifluridine is a cytotoxic nucleoside analog, used together with tipiracil (as Lonsurf) for metastatic colorectal cancer. The TxGNN model predicts it may be effective for **cecum villous adenoma**, a benign precancerous colon lesion. Currently **0 clinical trials** and **0 publications** support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer (based on general pharmacology of trifluridine/tipiracil; the Singapore registration records provided do not include indication text) |
| Predicted New Indication | Cecum villous adenoma |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on general pharmacology, trifluridine is a thymidine analog. It acts by being incorporated into DNA and by inhibiting thymidylate synthase. In combination with tipiracil, it is established in metastatic colorectal cancer. Tipiracil prevents trifluridine from being rapidly broken down.

The prediction most likely reflects the closeness of cecal and colonic nodes to colorectal cancer in the knowledge graph, not a therapeutic rationale. A villous adenoma is a benign, premalignant lesion. It is normally managed by endoscopic resection, so systemic cytotoxic chemotherapy has no clear role. The same pattern holds for the other top predictions (benign colonic lipoma, lymphangioma, leiomyoma, hemangioma and grade 1 neuroendocrine tumor): all are prediction-only with weak or no mechanistic support.

Two further points matter for interpretation:
- "Rectosigmoid junction neoplasm" (rank 5) is too nonspecific to assess. If it means malignant disease, it overlaps the existing colorectal indication and is not true repurposing.
- "Photosensitivity disease" (rank 10) is likely a graph artifact. Photosensitivity is a recognized adverse-effect concern for some antimetabolites, not a therapeutic target.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

For context, the lower-ranked "cecal disease" prediction links to four case reports or small case series of trifluridine/tipiracil in colorectal cancer. These cover an adverse event (vasculitis), readministration, and long-term use. They support only the existing colorectal use, not a benign cecal indication.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15491P | LONSURF FILM-COATED TABLET 15MG/6.14MG | Tablet, film coated |
| SIN15494P | LONSURF FILM-COATED TABLET 20MG/8.19MG | Tablet, film coated |

Both products are oral tablets made by Taiho Pharmaceutical Co., Ltd. (Kitajima Plant).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nucleoside analog antimetabolite) |
| Myelosuppression Risk | High (neutropenia and other cytopenias are common) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential before each treatment cycle, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

These entries come from general knowledge of the drug class, not from the evidence pack. Please also refer to the package insert warnings and precautions.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score (98.60%) but no clinical trials or literature, and the evidence level is L5. The condition is a benign lesion normally treated by endoscopic resection, so a cytotoxic, myelosuppressive drug has an unfavorable risk-benefit profile. The high score most likely reflects graph proximity to colorectal cancer, not a therapeutic signal.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (MOA) from DrugBank
- Re-mapping of nonspecific labels (e.g., rectosigmoid junction neoplasm) to specific histologies, and removal of candidates that overlap the approved colorectal indication
- A clinical rationale for systemic cytotoxic therapy in a benign or premalignant lesion, or a shift of focus to malignant colorectal candidates

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

