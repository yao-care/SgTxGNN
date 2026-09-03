---
layout: default
title: Sennosides
parent: 僅模型預測 (L5)
nav_order: 897
evidence_level: L5
indication_count: 10
---

# Sennosides
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

# Sennosides: From Constipation to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Sennosides is an anthraquinone-glycoside **stimulant laxative** used to treat constipation by stimulating the colonic myenteric plexus.
The TxGNN model's top prediction suggests possible efficacy for **Hypotrichosis Simplex of the Scalp**, a hereditary hair-follicle disorder,
but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags it as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation (stimulant laxative; no formal approved-indication text available — drug is unlicensed in Singapore) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Sennosides is officially unavailable in DrugBank ([Data Gap], DG002). Based on the drug-class information available in the evidence pack, Sennosides is an anthraquinone-glycoside stimulant laxative: it is metabolized by colonic bacteria to active rhein-anthrone, which stimulates the myenteric plexus, increases colonic peristalsis, and enhances water/electrolyte secretion into the bowel lumen.

Hypotrichosis simplex of the scalp is a hereditary keratinization/hair-follicle developmental disorder. There is no known receptor-level, pathway-level, or clinical connection between colonic smooth-muscle stimulation and hair follicle growth cycling. The evidence pack's own mechanistic assessment concludes this prediction "has no known biological connection" to the drug and is "very likely a false positive caused by node co-occurrence in the knowledge graph."

This pattern repeats across the other 9 top-ranked predictions in this evidence pack (alopecia variants, open-angle/hereditary glaucoma, esophageal varices with/without bleeding) — all are scored highly by TxGNN (95–99%) yet none has a plausible mechanistic link to a stimulant laxative, and none is supported by disease-specific clinical or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Note: two trials were returned for the related term "alopecia" — NCT03082560 and NCT05348343 — but both were reviewed and graded "C" (irrelevant): neither evaluates Sennosides; one is a Lichen Planopilaris grading-tool validation study, the other a PRP trial for androgenetic alopecia. They are excluded as evidence.)*

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Sennosides currently holds **no marketing authorization in Singapore** (0 registered licenses found in the regulatory database). No dosage forms or approved indications are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Material data gap: TFDA label warnings and contraindications for Sennosides are currently unobtained — flagged as a **Blocking** gap (DG001) — meaning the mandatory S1 safety screening cannot be completed for any indication until this is resolved. No drug-drug interaction records were found.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All 10 top-ranked TxGNN predictions for Sennosides sit at Evidence Level L5 (model prediction only), with no supporting clinical trials or literature, and the mechanistic review explicitly assesses most as biologically implausible (hair-follicle disorders, glaucoma, esophageal varices) given the drug's stimulant-laxative mechanism.
- A Blocking data gap (missing TFDA label warnings/contraindications) independently prevents this candidate from advancing past initial safety screening, regardless of indication.

**To proceed, the following is needed:**
- Retrieve and parse the Sennosides package insert (warnings, contraindications) from TFDA/HSA to resolve DG001 (Blocking)
- Confirm original MOA via DrugBank API to resolve DG002
- Monitor future data-refresh cycles for any new trials/literature supporting the top-10 predicted indications before reconsidering
- No further development action recommended on any of the current top-10 predictions (hair-follicle disorders, glaucoma, esophageal varices) absent new mechanistic or clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

