---
layout: default
title: Norelgestromin
parent: 僅模型預測 (L5)
nav_order: 712
evidence_level: L5
indication_count: 10
---

# Norelgestromin
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

# Norelgestromin: From Hormonal Contraception to Amenorrhea

## One-Sentence Summary

Norelgestromin is the active metabolite of norgestimate and is used as the progestin component of combined hormonal contraceptive products (e.g., transdermal contraceptive patches). The TxGNN model's top-ranked prediction links it to **Amenorrhea**, but this association is **not currently supported by any clinical trials or published literature**, and the evidence pack itself flags the predicted relationship as potentially reflecting a known adverse effect (breakthrough bleeding/amenorrhea) or diagnostic use (progestin challenge test) rather than a genuine therapeutic indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hormonal contraception (progestin component of a transdermal contraceptive patch) — not separately confirmed in the Singapore registration data |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for norelgestromin is not available in this evidence pack. Based on the information that is available, norelgestromin is the active metabolite of norgestimate, a low-androgenic progestin used as a component of combined hormonal contraceptive products.

The link to amenorrhea is mechanistically plausible but directionally ambiguous. Progestins are well known to be associated with amenorrhea in two very different ways: (1) as a **diagnostic tool** (the progestin challenge test, used to evaluate secondary amenorrhea), and (2) as a **known adverse effect** of contraceptive patches (breakthrough bleeding or amenorrhea during use). A knowledge-graph model can capture either of these associations without distinguishing them from a true treatment relationship. Because there are zero clinical trials and zero publications supporting norelgestromin as a *treatment* for amenorrhea, this prediction should be read as an association flagged for manual review of the underlying knowledge-graph edge semantics, not as an emerging treatment hypothesis.

For context, the same evidence pack's second-ranked prediction — acne (score 98.49%, evidence level L4) — has a clearer mechanistic rationale: the related combination norgestimate + ethinyl estradiol is an approved treatment for acne vulgaris via reduction of free testosterone. That is analog evidence, not direct evidence for norelgestromin, but it is mechanistically more coherent than the amenorrhea signal and may warrant separate consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Norelgestromin currently has no marketing authorization in Singapore (0 registered products; market status: Not Marketed). No dosage form or approved-indication data is available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are not currently available for norelgestromin in this evidence pack. Note: the missing TFDA/HSA-equivalent warning and contraindication data is flagged as a Blocking gap for safety pre-assessment — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The amenorrhea prediction has the highest TxGNN score in this candidate set but is supported only by a model-level association (L5, decision stage S0), with no clinical trials, no literature, and a specific concern — noted in the evidence pack itself — that the underlying knowledge-graph relationship may reflect an adverse effect or diagnostic use rather than a treatment effect. The drug is also not currently marketed in Singapore, and safety labeling data is entirely unavailable, which blocks any S1 safety pre-assessment.

**To proceed, the following is needed:**
- Manual review of the knowledge-graph edge to determine whether it reflects a treatment relationship, an adverse-effect relationship, or a diagnostic-use relationship (progestin challenge test)
- TFDA/HSA-equivalent package insert data: warnings and contraindications (currently a Blocking data gap)
- Mechanism of action (MOA) data via DrugBank API query (currently a High-severity data gap)
- If pursuing further, consider prioritizing the acne (rank 2) candidate instead, which has a more coherent mechanistic rationale via the norgestimate/ethinyl estradiol analog, though it likewise lacks direct clinical trial or literature support for norelgestromin itself
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

