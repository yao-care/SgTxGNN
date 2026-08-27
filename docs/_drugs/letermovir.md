---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 582
evidence_level: L5
indication_count: 10
---

# Letermovir
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

# Letermovir: From CMV Infection Prophylaxis to Vulvovaginal Candidiasis

## One-Sentence Summary

> Letermovir is an antiviral used for the prophylaxis of cytomegalovirus (CMV) infection/reactivation in hematopoietic stem cell transplant (HSCT) recipients.
> The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the mechanistic rationale itself flags it as a likely model false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CMV infection prophylaxis in HSCT recipients (based on context in the evidence pack; Letermovir is **not registered in Singapore**, so no local label text is available) |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for Letermovir is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on information embedded in related clinical trial records, Letermovir is a viral **terminase complex (UL56/UL89) inhibitor** — it blocks DNA packaging specifically in human cytomegalovirus (HCMV), a herpesvirus, and is approved for CMV prophylaxis after hematopoietic stem cell transplantation.

Vulvovaginal candidiasis is a fungal infection caused by *Candida* species. Fungi do not possess a herpesvirus-type terminase/DNA-packaging complex, so there is no known or plausible molecular target through which Letermovir could act against *Candida*. The repurposing rationale attached to this candidate explicitly states there is **no mechanistic link** and **no clinical or literature evidence** supporting this indication, and assesses the prediction as most likely a **false positive arising from embedding-space similarity** in the TxGNN model rather than a genuine pharmacological signal.

In other words: this prediction does not currently have a scientifically reasonable basis. It should be treated as a low-priority, unverified model output rather than a candidate for further clinical development at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Letermovir is currently **not marketed in Singapore** (0 registrations on file), so no local authorization/product records are available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug interaction data are all currently unavailable — DDI query returned "not_found," and label warnings/contraindications are marked as a Blocking-severity data gap, DG001, which also prevents this candidate from entering the S1 safety pre-assessment stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanistic basis, no clinical trial evidence, and no published literature supporting Letermovir's use in vulvovaginal candidiasis. The evidence level is L5 (model prediction only), and the candidate's own rationale identifies it as a likely false positive — this does not meet the bar to advance past initial screening.

**To proceed, the following is needed:**
- Letermovir's confirmed mechanism of action (MOA) data (DG002, High severity)
- TFDA/HSA label warnings and contraindications, required before any S1 safety pre-assessment can be performed (DG001, Blocking severity)
- Any future *in vitro* or preclinical data demonstrating antifungal activity, since none currently exists
- If repurposing work continues for this drug, consideration should shift toward the higher-evidence candidate in this evidence pack — "fungal infectious disease" (rank 2, L4, 3 clinical trials + 9 publications) — noting that even that evidence base is epidemiological/observational (CMV-prophylaxis cohorts examining co-incident fungal infection rates) rather than direct efficacy data, and it is also currently scored **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

