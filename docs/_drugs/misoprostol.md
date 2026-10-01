---
layout: default
title: Misoprostol
parent: Low Evidence (L5)
nav_order: 674
evidence_level: L5
indication_count: 10
---

# Misoprostol
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

# Misoprostol: From an Unlisted Original Indication to Amenorrhea

## One-Sentence Summary

Misoprostol is a prostaglandin E1 analog marketed in Singapore as Cytotec 200 mcg tablets. The approved indication text is not recorded in the source data.
The TxGNN model predicts it may be effective for **amenorrhea**, but the retrieved evidence is only indirect: **0 clinical trials** and **7 publications**, none of which tests misoprostol as a treatment for amenorrhea.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Singapore licence record |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 (indirect, mechanism-level and off-target clinical data only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Misoprostol is a prostaglandin E1 analog that causes uterine contraction and cervical ripening. Its known effects on the uterus explain why the model links it to gynaecological conditions.

The retrieved papers all concern medical abortion or missed abortion, where misoprostol is used to induce bleeding and expel pregnancy tissue. In those studies "amenorrhea" is only a gestational-age criterion (for example, "amenorrhea ≤35 days"), not a disease being treated. No study evaluates misoprostol for treating amenorrhea.

The high TxGNN score is therefore probably driven by the shared uterine and pregnancy-related neighborhood in the knowledge graph, not by therapeutic evidence. There is also a directional concern: misoprostol induces uterine bleeding and pregnancy loss, and it is not known to restore menstrual function.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | 744 women with ultra-early pregnancy (amenorrhea ≤35 days) received low-dose mifepristone plus hospital-administered or self-administered misoprostol for medical abortion. Off-topic for amenorrhea treatment. |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT | Reproductive Sciences | Dose-ranging trial in 2,500 women. Mifepristone 50–150 mg followed by misoprostol 200 µg was tested for ultra-early pregnancy termination. Off-topic for amenorrhea treatment. |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Clinical study | Human Reproduction | Low-dose mifepristone plus misoprostol before expected menstruation to prevent unintended pregnancy. Design not confirmed. |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Clinical study | J Obstet Gynaecol Res | Safety and efficacy of self-administered misoprostol with low-dose mifepristone for early pregnancy termination. |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Clinical study / review | BMJ | Medical management of missed abortion and anembryonic pregnancy. No abstract available. |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Endometrial ablation for abnormal uterine bleeding. Off-topic. |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case report | Cureus | Acute fatty liver of pregnancy presenting with amenorrhea. Off-topic. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN03501P | CYTOTEC TABLET 200 mcg (Piramal Healthcare UK Limited) | Tablet (oral) | — |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug-interaction records were retrieved (the interaction query returned no results).

Misoprostol is a uterotonic with a recognised pregnancy-related risk, so any repurposing in women of reproductive age would need explicit pregnancy guardrails.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but no trial or publication tests misoprostol for amenorrhea. The retrieved literature concerns pregnancy termination, and the pharmacology (inducing uterine bleeding) does not point toward treating amenorrhea. The score appears to reflect graph proximity, not therapeutic evidence.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications, approved indication), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Evidence that misoprostol treats or restores menstruation in amenorrhea, or a rationale for a specific amenorrhea subtype
- Attention to other predictions in the same pack: esophageal disease (rank 6, L4) is the only one with a biologically coherent rationale. It rests on preclinical EP2 receptor work (PMID 25059824) and one case report (PMID 9820375), and no controlled trials exist.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

