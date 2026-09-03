---
layout: default
title: Tipiracil
parent: 僅模型預測 (L5)
nav_order: 984
evidence_level: L5
indication_count: 10
---

# Tipiracil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Tipiracil: From Metastatic Colorectal Cancer to Cecum Villous Adenoma

## One-Sentence Summary

> Tipiracil is a thymidine phosphorylase inhibitor combined with trifluridine (TAS-102/Lonsurf), originally used to treat metastatic colorectal cancer.
> The TxGNN model's top prediction suggests possible efficacy for **Cecum Villous Adenoma**,
> but this direction currently has **0 clinical trials** and **0 publications** supporting it, and the evidence pack itself flags the mechanistic rationale as weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer (as part of the trifluridine/tipiracil combination, TAS-102/Lonsurf) — not independently registered in Singapore |
| Predicted New Indication | Cecum Villous Adenoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for tipiracil is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, tipiracil is a thymidine phosphorylase inhibitor that is co-formulated with trifluridine — trifluridine is the active cytotoxic antimetabolite, and tipiracil's role is to block its degradation, prolonging exposure. This combination (TAS-102/Lonsurf) is an approved cytotoxic chemotherapy for refractory metastatic colorectal cancer.

Cecum villous adenoma, however, is a benign-to-premalignant colonic polyp, standardly managed by endoscopic resection rather than systemic cytotoxic therapy. The evidence pack's own rationale for this prediction states that the high TxGNN score likely reflects anatomical/embedding proximity ("colon" location) rather than genuine pharmacological relevance — there is no biological basis for a DNA-synthesis-targeting antimetabolite to be indicated for a non-proliferative, surgically curable lesion.

Taken together, this is a case where a high model confidence score is not corroborated by mechanistic logic or external evidence. Of the ten candidates in this pack, most (ranks 1, 2, 4, 5, 7, 8, 9, 10) are explicitly annotated as likely false positives (benign/vascular/mesenchymal lesions or genetically distinct tumors like GIST). Rank 3 ("rectosigmoid junction neoplasm") is too non-specific to evaluate, and only rank 6 ("cecal disease") has any supporting literature — four case reports on trifluridine/tipiracil use in colorectal cancer — though none specifically address the named condition.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Singapore Market Information

Tipiracil (as trifluridine/tipiracil) is not currently registered in Singapore — 0 licenses on record in this evidence pack.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite/nucleoside-analog combination — trifluridine/tipiracil, TAS-102/Lonsurf) |
| Myelosuppression Risk | High — leukopenia and neutropenia are reported adverse effects of the trifluridine/tipiracil combination (PMID [30677817](https://pubmed.ncbi.nlm.nih.gov/30677817/)) |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | CBC with differential, renal function (tipiracil is renally cleared), liver function |
| Handling Protection | Yes — must be handled per cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information. (No structured warnings, contraindications, or DDI data are available in this evidence pack — TFDA/label data is flagged as a Blocking gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (cecum villous adenoma) has no clinical trial or literature support, and the mechanistic rationale itself identifies the score as a likely embedding-space artifact rather than genuine pharmacological plausibility — a benign, endoscopically-curable lesion is not a rational target for cytotoxic antimetabolite therapy.

**To proceed, the following is needed:**
- TFDA/regulatory label (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action for tipiracil — currently High severity gap (DG002)
- If pursuing this indication class further, prioritize rank 6 ("cecal disease") instead, which has L4 evidence (four case reports on trifluridine/tipiracil in colorectal cancer contexts) and a "Research Question" recommendation, rather than rank 1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

