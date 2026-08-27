---
layout: default
title: Leucovorin
parent: 僅模型預測 (L5)
nav_order: 585
evidence_level: L5
indication_count: 10
---

# Leucovorin
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

# Leucovorin: From Methotrexate Rescue/Chemotherapy Adjuvant to Primary Hyperoxaluria

## One-Sentence Summary

> Leucovorin (folinic acid) is an established rescue agent for methotrexate toxicity and a biochemical modulator used alongside fluorouracil-based chemotherapy; its own novel indications are not recorded in this evidence pack.
> The TxGNN model predicts it may be effective for **Primary Hyperoxaluria**,
> but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags a likely biological implausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Folinic acid rescue (methotrexate toxicity) / adjuvant to fluorouracil-based chemotherapy (established use; specific registered indication text unavailable — no Singapore license records) |
| Predicted New Indication | Primary hyperoxaluria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, leucovorin (calcium/levo-folinate) is primarily used clinically as a "rescue" agent following high-dose methotrexate therapy (bypassing dihydrofolate reductase inhibition to restore reduced-folate pools) and as a biochemical modulator that enhances the antitumor activity of 5-fluorouracil in colorectal and gastrointestinal chemotherapy regimens. These established uses are well documented, though the specific approved indication wording could not be extracted here because this drug has no license records in the Singapore registry data provided.

Primary hyperoxaluria, by contrast, is a rare inherited disorder (AGXT/GRHPR/HOGA1 gene defects) of glyoxylate metabolism that leads to oxalate overproduction and progressive nephrocalcinosis/renal failure. There is no known overlap between the folate/reduced-folate metabolic pathway that leucovorin acts on and the glyoxylate-to-oxalate pathway implicated in this disease.

The evidence pack's own mechanistic assessment for this candidate is explicit on this point: it states there is "no known direct or indirect connection" between leucovorin's pharmacology and oxalate metabolism, and assesses this as a likely **false-positive signal arising from knowledge-graph node proximity** rather than a genuine biological hypothesis. We report this candidate per the ranking, but flag that its biological plausibility is assessed as low by the source data itself — this is reflected in the L5 evidence level (model prediction only, no supporting studies) and the "Hold" recommendation.

For context, this evidence pack evaluated 10 candidate indications for leucovorin in total. Several lower-ranked candidates (e.g., "focal myositis," rank 8; "primary amyloidosis," rank 9) have associated literature or trial records, but those records predominantly describe leucovorin's established supportive role in methotrexate-based regimens (as a toxicity-rescue agent) rather than independent therapeutic activity against those diseases, and were separately flagged as likely ontology/mapping artifacts. None of the 10 ranked candidates in this pack currently reach a level of evidence supporting a "Go" decision.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score (99.41%), there are zero clinical trials and zero publications supporting leucovorin for primary hyperoxaluria, and the model's own rationale identifies no plausible biological mechanism linking leucovorin's folate-pathway pharmacology to oxalate metabolism — this is assessed as a probable graph-proximity false positive rather than a genuine repurposing signal. Additionally, leucovorin has no market registration in Singapore in the data reviewed, and a blocking data gap (missing package-insert warnings/contraindications) prevents even a preliminary safety (S1) assessment.

**To proceed, the following is needed:**
- Package insert warnings/contraindications for leucovorin (currently a blocking data gap, DG001)
- Confirmed mechanism of action data (DG002) to properly evaluate mechanistic plausibility
- Independent biological/preclinical rationale connecting folate metabolism to glyoxylate/oxalate metabolism, if this hypothesis is to be pursued further
- Confirmation of current Singapore market/registration status for leucovorin, since none was found in this dataset
- If this candidate is pursued at all, treat it as an exploratory research question rather than a clinical development candidate, given the source data's own assessment of low biological plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

