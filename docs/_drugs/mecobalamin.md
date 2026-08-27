---
layout: default
title: Mecobalamin
parent: 僅模型預測 (L5)
nav_order: 633
evidence_level: L5
indication_count: 10
---

# Mecobalamin
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

# Mecobalamin: From Vitamin B12 Deficiency/Peripheral Neuropathy to Sclerosing Cholangitis

## One-Sentence Summary

Mecobalamin is the bioactive coenzyme form of vitamin B12, used internationally for vitamin B12 deficiency and peripheral neuropathy (it is not currently licensed in Singapore). The TxGNN model predicts a possible effect on **Sclerosing Cholangitis**, but this signal is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags it as a likely graph-embedding artifact rather than a genuine mechanistic finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file for Singapore (drug not licensed here). Internationally, Mecobalamin is used for vitamin B12 deficiency and peripheral neuropathy. |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Mecobalamin is not available in this evidence pack. Based on known pharmacology, Mecobalamin (methylcobalamin) functions as a coenzyme for methionine synthase, supporting homocysteine metabolism and myelin/nerve repair — its efficacy in vitamin B12 deficiency and peripheral neuropathy is well established.

Sclerosing cholangitis, however, is a chronic autoimmune/fibrotic biliary disease with no established connection to B12-dependent one-carbon metabolism or myelin repair pathways. The evidence pack's own rationale for this candidate states that the drug node has very sparse connections in the knowledge graph (consistent with the missing MOA data), and that the high TxGNN score is more likely a graph-embedding proximity artifact than a reflection of real biological overlap between the original and predicted indications.

This weak-mechanism pattern is consistent across the rest of the candidate list: none of the other nine TxGNN-predicted indications (multiple endocrine neoplasia, bone/juvenile Paget disease, gastroparesis, acne, osteomesopyknosis, vitamin D deficiency, choledocholithiasis, colorectal cancer) have a plausible, literature-supported mechanistic link either. Notably, the acne signal is flagged as a potential **adverse effect direction** (high-dose B12 has been reported to trigger acneiform eruptions), not a therapeutic opportunity — this is a safety signal disguised as an efficacy prediction and should not be pursued as repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Singapore Market Information

Mecobalamin is currently not marketed in Singapore — no license or registration records are available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data were all queried but returned no results; a formal HSA/manufacturer package insert review is still required before any clinical use is considered.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (Sclerosing Cholangitis) has zero supporting clinical trials or literature, and the evidence pack's own mechanistic assessment considers the high TxGNN score a likely embedding artifact rather than genuine biological signal. All 10 TxGNN-predicted indications for this drug carry a "Hold" recommendation at decision stage S0 — none has more than incidental, off-target trial/literature hits (e.g., the multiple endocrine neoplasia trial is an unrelated newborn screening study, and the colorectal cancer citation concerns post-surgical urinary dysfunction, not oncologic efficacy). One candidate (acne) even points toward a safety risk rather than a benefit.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- TFDA/HSA package insert (warnings, contraindications, DDI) — currently a Blocking data gap
- Independent mechanistic or preclinical rationale connecting B12 coenzyme pathways to any of the predicted indications before allocating further evaluation resources
- Re-screening once additional clinical trial or literature evidence becomes available, given the current complete absence of supporting studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

