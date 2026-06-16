---
layout: default
title: Encorafenib
parent: 僅模型預測 (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
---

# Encorafenib
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

# Encorafenib: From BRAF V600E/K Melanoma to Choroideremia

## One-Sentence Summary

Encorafenib (Braftovi) is a selective BRAF kinase inhibitor approved in multiple markets (EU, US) for BRAF V600E/K mutation-positive unresectable or metastatic melanoma, and in combination with cetuximab for BRAF V600E-mutated metastatic colorectal cancer — though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Choroideremia** with a prediction score of **97.1%**, however this remains a model-only prediction with **no clinical trials** and **no publications** directly supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | BRAF V600E/K mutation-positive melanoma; BRAF V600E metastatic colorectal cancer (approved in EU/US; not registered in Singapore) |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 97.1% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on known information, Encorafenib is a highly selective RAF kinase inhibitor that targets mutant BRAF V600E and V600K, blocking constitutive activation of the MAPK/ERK signaling cascade that drives unchecked tumor cell proliferation and survival. It is typically combined with a MEK inhibitor (binimetinib) to achieve more complete pathway blockade and delay acquired resistance.

Choroideremia is a rare X-linked recessive chorioretinal degenerative disease caused by loss-of-function mutations in the CHM gene, resulting in deficiency or absence of Rab escort protein-1 (REP-1). REP-1 is essential for the prenylation and membrane targeting of Rab GTPases, which regulate intracellular vesicle trafficking. Without functional REP-1, Rab GTPases cannot be correctly geranylgeranylated, causing progressive degeneration of the retinal pigment epithelium (RPE), photoreceptors, and choroid — ultimately leading to blindness.

There is currently **no known biological intersection** between the BRAF/MAPK signaling pathway (Encorafenib's target) and the CHM/REP-1/Rab GTPase prenylation pathway (choroideremia's disease mechanism). The TxGNN model's high prediction score of 97.1% most likely reflects structural similarities at the knowledge graph level — for example, shared retinal cell type annotations or overlapping disease network topology — rather than direct pharmacological plausibility. Without a mechanistic rationale, clinical translation of this prediction is not currently justified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Encorafenib is not currently registered with the Health Sciences Authority (HSA) in Singapore. No product authorizations are on record. If clinical investigation is pursued, market authorization would need to be sought through the standard HSA regulatory pathway.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Selective BRAF kinase inhibitor (RAF class kinase inhibitor; antineoplastic) |
| Myelosuppression Risk | Low (not a conventional cytotoxic; significant hematologic toxicity is uncommon compared to chemotherapy) |
| Emetogenicity Classification | Low to moderate (oral targeted agent; nausea reported in approximately 20–30% of patients in melanoma trials) |
| Monitoring Items | Liver function tests (ALT/AST/bilirubin), dermatological assessment (rash, palmar-plantar erythrodysesthesia, new primary cutaneous malignancies, keratoacanthoma), ophthalmological monitoring (uveitis, iritis, retinal vein occlusion), QTc interval, CBC |
| Handling Protection | Follow institutional cytotoxic handling policies for oral antineoplastic agents; standard precautions (gloves, dedicated dispensing) apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no established mechanistic link between BRAF kinase inhibition and choroideremia's underlying disease pathway (CHM gene / REP-1 / Rab GTPase prenylation), and no clinical trials or published literature currently support this repurposing direction. The high TxGNN prediction score is likely an artifact of knowledge graph topology rather than a signal of biological plausibility.

**To proceed, the following is needed:**
- Basic science investigation into whether BRAF/MAPK signaling plays any role in RPE or photoreceptor degeneration in CHM-deficient in vitro or animal models
- Review of the TxGNN knowledge graph edge connections underpinning this prediction to evaluate whether the mechanistic path is biologically meaningful or a graph artefact
- Full MOA data from DrugBank (DB11718) to complete mechanistic analysis
- Singapore (HSA) regulatory pathway assessment if further investigation is warranted
- Safety profile data from the full prescribing information (package insert) to complete contraindication and warning review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

