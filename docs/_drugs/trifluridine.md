---
layout: default
title: Trifluridine
parent: 僅模型預測 (L5)
nav_order: 1015
evidence_level: L5
indication_count: 10
---

# Trifluridine
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

# Trifluridine: From Antiviral/Colorectal Cancer Therapy to Cecum Villous Adenoma

## One-Sentence Summary

Trifluridine is a thymidine-based nucleoside analogue known clinically as an ophthalmic antiviral for herpetic keratitis and, in combination with tipiracil (as TAS-102), as a cytotoxic antimetabolite for metastatic colorectal cancer. The TxGNN model predicts a possible new application in **Cecum Villous Adenoma**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the drug's own mechanistic profile argues against a genuine treatment rationale for this benign/premalignant lesion.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in this evidence pack (no Singapore license data); known global uses are herpetic keratoconjunctivitis (ophthalmic antiviral) and, as TAS-102, metastatic colorectal cancer |
| Predicted New Indication | Cecum Villous Adenoma |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known information, Trifluridine is a thymidine-based nucleoside analogue that acts by incorporating into DNA and inhibiting thymidylate synthase, blocking DNA synthesis. Clinically this mechanism is exploited in two very different settings: topically as an antiviral against herpes simplex keratitis, and systemically — combined with tipiracil as TAS-102 — as a cytotoxic chemotherapy for refractory metastatic colorectal cancer.

Cecum villous adenoma, however, is a benign-to-premalignant colonic polyp. Standard management is endoscopic resection or surveillance, not systemic cytotoxic therapy — there is no established clinical scenario where a DNA-synthesis-inhibiting antimetabolite would be indicated for an adenomatous polyp that has not progressed to invasive malignancy.

Because of this mismatch, the mechanistic link recorded in the evidence pack explicitly flags this prediction as more likely reflecting **knowledge-graph proximity bias** — trifluridine sits close to colorectal-cancer-related nodes in the TxGNN graph, and "cecum villous adenoma" shares graph neighbors with those nodes — rather than a real pharmacological relationship. The same pattern (high TxGNN score, no supporting evidence, and rationale text explicitly describing the prediction as likely noise) recurs across the other top-10 candidates for this drug (e.g., colon lipoma, colonic lymphangioma, cecal neuroendocrine tumor G1, colon leiomyoma, cavernous hemangioma of colon), suggesting a systemic clustering artifact around colonic-lesion nodes rather than a single strong signal worth prioritizing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Trifluridine currently has no marketing authorization in Singapore (0 registrations, market status: Not Marketed). No license records are available to summarize.

---

## Cytotoxicity

*(Included because trifluridine, in its established use as the active component of TAS-102 with tipiracil, is a conventional cytotoxic antimetabolite/nucleoside analogue.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (thymidine-based nucleoside analogue / antimetabolite; active component of TAS-102) |
| Myelosuppression Risk | High — leukopenia and neutropenia are commonly reported adverse effects in TAS-102 case literature (PMID 30677817) |
| Emetogenicity Classification | Moderate — nausea, vomiting, diarrhea, and fatigue reported alongside myelosuppression |
| Monitoring Items | Complete blood count with differential, liver and renal function, skin/cutaneous reactions (case reports describe leukocytoclastic vasculitis) |
| Handling Protection | Standard cytotoxic drug handling precautions required per institutional hazardous-drug protocols |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are not yet available for this drug — see data gap DG001, which is blocking for a full safety assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for Cecum Villous Adenoma has a high TxGNN score but zero clinical trials, zero publications, and a mechanistic rationale that itself identifies the signal as likely graph-proximity noise rather than a genuine drug-disease relationship — a benign/premalignant colonic lesion has no established clinical indication for systemic cytotoxic antimetabolite therapy. This pattern repeats across nearly all top-ranked candidates for this drug, further weakening confidence in the cluster.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: obtain TFDA/HSA label warnings and contraindications before any safety evaluation (S1) can begin
- Resolve high-priority data gap DG002: confirm mechanism of action via DrugBank API to properly assess mechanistic plausibility
- If this candidate is to be pursued further, obtain preclinical or case-level evidence specifically linking nucleoside-analogue/antimetabolite mechanisms to adenomatous polyp biology (not just colorectal cancer)
- Reassess whether "cecum villous adenoma" is being conflated with malignant colorectal neoplasms in the underlying knowledge graph, given the ambiguity seen in related candidates (e.g., "rectosigmoid junction neoplasm")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

