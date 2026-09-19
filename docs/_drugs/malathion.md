---
layout: default
title: Malathion
parent: Low Evidence (L5)
nav_order: 627
evidence_level: L5
indication_count: 10
---

# Malathion
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

# Malathion: From Head Lice/Scabies External Parasiticide to Seborrheic Keratosis Prediction

## One-line Summary

Malathion is an organophosphate acetylcholinesterase inhibitor, and its currently known clinical uses are as an external parasiticide used to treat head lice (pediculosis capitis) and scabies infections. The TxGNN model predicts that it may be effective for **seborrheic keratosis**, but currently **no clinical trials exist**, **no related literature exists** to support this direction, and the evidence package's own mechanistic analysis also indicates **no reasonable biological linkage** between the two.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No record in Taiwan regulatory data (`taiwan_regulatory.licenses`), drug not marketed; based on known pharmacological uses, Malathion is an external parasiticide, clinically used for parasiticide/mite-killing treatment of head lice and scabies |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 96.45% |
| Evidence Level | L5 (Model prediction only, no clinical trials or literature evidence) |
| Taiwan Market Status | Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold (Suspend) |

---

## Why Is This Prediction Reasonable?

Currently no formal mechanism of action (MOA) data is available for consultation (`original_moa` is a data gap, High priority). Based on known pharmacological information, Malathion is an organophosphate compound that achieves insecticidal effects by inhibiting acetylcholinesterase (AChE), and is used clinically as an external formulation for the treatment of head lice and scabies infections.

However, regarding the target indication for this prediction—"seborrheic keratosis"—the mechanistic analysis attached to the evidence package clearly indicates: seborrheic keratosis is a benign epithelial proliferative lesion whose pathological mechanism is primarily related to mutations in genes such as FGFR3 and PIK3CA, as well as keratinocyte proliferation, **and there is no known biological association between this and AChE inhibition or parasiticide activity**.

In other words, this prediction **currently lacks mechanistic plausibility**, and is more likely an associational artifact in the knowledge graph due to node proximity effects (for example, proximity to other keratinization-related lesion nodes) rather than a genuine drug repurposing signal with pharmacological basis. This point is further reinforced in the evidence package's analysis of subsequent candidate indications ranking second (vulvar inverted follicular keratosis) and beyond, supporting this judgment further.

---

## Clinical Trial Evidence

Currently no related clinical trial registrations exist.

(Query records show that for the combination of Malathion + Seborrheic Keratosis, separate queries of ClinicalTrials.gov and ICTRP both returned zero results.)

---

## Literature Evidence

Currently no related literature can be found.

(PubMed query for the combination of Malathion + Seborrheic Keratosis returned zero results.)

> Supplementary note: The evidence package's third-ranked candidate indication, "seborrheic dermatitis," yielded 1 related literature result (PMID: [24126752](https://pubmed.ncbi.nlm.nih.gov/24126752/)), but the literature's subject is a case of **clinical presentation differential diagnosis confusion** between scalp scabies infection and seborrheic dermatitis, not "mechanistic evidence that Malathion has therapeutic efficacy for seborrheic dermatitis," and therefore does not constitute supporting literature for this report's primary target (seborrheic keratosis).

---

## Taiwan Market Information

Malathion is currently **not marketed in Taiwan**, with zero license registrations, and `taiwan_regulatory.licenses` contains no authorization records available for listing.

---

## Safety Considerations

For safety information, please refer to the drug package insert.

(Currently `key_warnings`, `contraindications`, and drug-drug interaction (DDI) queries all lack available data; DDI query status is "no records found.")

---

## Conclusions and Recommendations for Follow-up

**Decision: Hold (Suspend)**

**Rationale:**
- The top-ranked predicted indication (seborrheic keratosis) currently has **zero clinical trials and zero literature support**, and the evidence package's internal mechanistic analysis has already clearly indicated there is no known biological linkage between the two, suggesting this score may derive from knowledge graph node proximity effects rather than genuine pharmacological signals.
- Evidence level is L5 (model prediction only), the lowest among five levels.
- The drug is currently not marketed in Taiwan (number of licenses = 0), and **package insert warning/contraindication data is missing (DG001, Blocking level)**—this is a prerequisite for preliminary safety evaluation (S1), currently unable to pass.

**To proceed further, the following must be supplemented:**
- TFDA package insert warnings and contraindication data (DG001, Blocking, requires downloading and parsing official package insert PDF)
- Complete mechanism of action (MOA) data for Malathion (DG002, requires querying the DrugBank API)
- Independent in vitro/in vivo mechanistic studies specifically for seborrheic keratosis as an indication, to verify or refute the current preliminary judgment of "no reasonable mechanism"
- If mechanistic verification passes, re-evaluation of regulatory approval pathway feasibility in Taiwan/Singapore is required

---

*Candidate indications ranking 2–10 (vulvar inverted follicular keratosis, seborrheic dermatitis, mycotic corneal ulcer, inherited skin tumor, anogenital HPV infection, breast fibrocystic disease, benign mammary dysplasia, blunt duct adenosis of breast, apocrine adenosis of breast) all belong to L5 evidence level, recommended Hold status, and the evidence package mechanistic analyses all indicate no reasonable biological linkage or knowledge graph associational artifacts; individual expansion is temporarily not pursued.*

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

