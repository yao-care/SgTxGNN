---
layout: default
title: Elacestrant
parent: 僅模型預測 (L5)
nav_order: 363
evidence_level: L5
indication_count: 10
---

# Elacestrant
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

# Elacestrant: From ER+ Breast Cancer to Amenorrhea

## One-Sentence Summary

Elacestrant is a selective estrogen receptor degrader (SERD) developed for the treatment of ER+/HER2- advanced or metastatic breast cancer — a role confirmed by the clinical trial evidence found during this search. The TxGNN model's top prediction is **Amenorrhea**, with a score of **92.50%**, yet **0 clinical trials** and **0 supporting publications** exist for this indication; all 10 top predictions carry the lowest possible evidence level (L5). Critically, the primary mechanistic rationale for the lead prediction runs counter to clinical benefit, making this a portfolio where the model's ranking likely reflects indirect graph connectivity rather than true therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ER+/HER2- advanced breast cancer (ESR1-mutated) — inferred from clinical trial context; not registered in Singapore |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 92.50% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Elacestrant is a selective estrogen receptor degrader (SERD) — a class of drugs that binds to the estrogen receptor (ER) and promotes its proteasomal degradation, thereby abolishing downstream estrogen signalling. Compared with older endocrine agents such as fulvestrant, elacestrant retains potency against tumours harbouring ESR1 ligand-binding domain mutations, which are a major mechanism of acquired resistance to aromatase inhibitors in advanced breast cancer. The drug's mechanism is fundamentally anti-estrogenic.

Amenorrhea is the absence of menstruation and may arise from a wide range of causes, including hypothalamic suppression, pituitary dysfunction, premature ovarian insufficiency, or intrauterine pathology. In the most common forms — particularly those driven by oestrogen deficiency or HPG-axis disruption — the therapeutic goal is to *restore* oestrogen signalling or normalise its feedback dynamics, not suppress them further. Deploying a SERD in this context would be expected to worsen, not improve, the condition.

The TxGNN model's high-ranking prediction for amenorrhea most plausibly reflects indirect connections within the knowledge graph — shared HPG-axis nodes link estrogen pharmacology to menstrual cycle regulation — rather than a direct, clinically exploitable mechanism. There is no biological or clinical rationale to support elacestrant development for amenorrhea, and the assessment is accordingly **Hold**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Elacestrant + Amenorrhea.

---

## Literature Evidence

Currently no related literature available for Elacestrant + Amenorrhea.

---

## Singapore Market Information

Elacestrant is not currently registered in Singapore. No marketing authorisations are on record.

---

## Cytotoxicity

Elacestrant is an antineoplastic agent (targeted endocrine therapy used in breast cancer), and this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Selective Estrogen Receptor Degrader (SERD); not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Standard oral oncology handling precautions apply; specific cytotoxic containment requirements should be confirmed per institutional policy |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every one of the 10 top-ranked TxGNN predictions carries an L5 evidence level with no supporting clinical trials or publications for the specific indication. More importantly, the lead prediction (amenorrhea) has a mechanistic direction that is actively contrary to therapeutic benefit — a SERD that blocks oestrogen signalling cannot be expected to treat a condition rooted in oestrogen deficiency.

**Notable observation before closing:**
Among the 10 predictions, one stands out as a genuine **Research Question**: **hypogonadotropic hypogonadism with or without anosmia** (rank 9, score 81.67%). The mechanistic rationale is biologically coherent — blocking oestrogen's negative feedback on the HPG axis could theoretically stimulate GnRH pulsatility, analogous to the well-established mechanism of clomiphene citrate. However, no clinical or preclinical evidence currently exists to support this, and SERDs' complete receptor degradation (versus SERM partial agonism) introduces unpredictable differences in effect. This hypothesis is scientifically worth flagging for basic research, not for clinical development at this stage.

**To proceed to any next stage, the following is needed:**

- Retrieve elacestrant's full mechanistic and safety data from DrugBank (MOA currently a data gap)
- Obtain package insert (e.g., FDA Orserdu label) for complete warnings, contraindications, and DDI profile
- For the hypogonadotropic hypogonadism hypothesis specifically: commission a literature review on SERD effects on GnRH pulsatility in preclinical models before any clinical hypothesis can be formed
- Singapore registration pathway assessment is premature until a biologically credible new indication is identified with at least L3-level evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

