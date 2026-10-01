---
layout: default
title: Ethinylestradiol
parent: Medium Evidence (L3-L4)
nav_order: 403
evidence_level: L4
indication_count: 10
---

# Ethinylestradiol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Ethinylestradiol: From Hormonal Contraception to Elevated Plasma Zinc

## One-Sentence Summary

Ethinylestradiol is an estrogen used in combined oral contraceptives. In the Singapore data, its registered products are pills such as Belara, Diane-35, Yasmin, Microgynon 30 and Mercilon.
The TxGNN model predicts it for **elevated plasma zinc** with a very high score, but this prediction has **0 clinical trials** and only **2 old, non-therapeutic publications**, and those studies do not show zinc rising.
Elevated plasma zinc is a laboratory finding, not a treatable disease, so this prediction is not a credible repurposing opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registry data (licences list no indication text); products are combined oral contraceptives |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ethinylestradiol is the estrogen component of combined oral contraceptives, and its use in contraception is well established.

The only link to this prediction is that oral contraceptive use changes zinc and copper levels in blood and tissue. Mestranol, a prodrug of ethinylestradiol, was studied in rats and lowered plasma zinc. In women taking oral contraceptives, zinc stayed roughly constant while copper rose. So the evidence points to no rise, or even a fall, in zinc, which is the opposite direction from the prediction.

The 99.63% score most likely reflects an association in the knowledge graph. It does not reflect a treatment opportunity. No therapeutic rationale exists for lowering or treating elevated zinc with an estrogen.

**A better-supported candidate in the same report:** among the other predictions, **amenorrhea** (score 94.68%) has 7 clinical trials and 19 publications, including a Phase 4 study of ethinylestradiol/cyproterone acetate in irregular menstruation. Its evidence level is L2, with a "Research Question" recommendation. It deserves separate evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [961877](https://pubmed.ncbi.nlm.nih.gov/961877/) | 1976 | Animal / mechanistic | The American Journal of Physiology | In female rats, mestranol (an ethinylestradiol prodrug) reduced plasma zinc, along with tibia copper and magnesium. Both steroids reduced weight gain. |
| [736629](https://pubmed.ncbi.nlm.nih.gov/736629/) | 1978 | Observational | Archives of Gynecology | In women on oral contraceptives, plasma and endometrial copper rose significantly, while zinc stayed fairly constant across the menstrual cycle. |

## Singapore Market Information

Five of the 7 registrations are listed. The registry data contain no approved indication text for these products.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14870P | BELARA film-coated tablet 0.03mg/2mg | Film-coated tablet | Not stated |
| SIN04784P | DIANE-35 TABLET | Sugar-coated tablet | Not stated |
| SIN12334P | YASMIN TABLET | Film-coated tablet | Not stated |
| SIN04834P | MICROGYNON 30 TABLET | Sugar-coated tablet | Not stated |
| SIN06136P | MERCILON TABLET | Tablet | Not stated |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found. As an estrogen, ethinylestradiol carries known thrombotic risk, so any new use needs a specific benefit-risk assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is a laboratory value change rather than a disease. The two available studies show zinc falling or unchanged, not rising, and no trials exist. The high TxGNN score reflects a graph association and does not justify further development.

**To proceed, the following is needed:**
- Re-prioritise the review toward amenorrhea, the best-supported prediction for this drug (L2)
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of whether the amenorrhea trials (for example NCT00946192 and NCT00088153) actually include an ethinylestradiol arm
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

