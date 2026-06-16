---
layout: default
title: Ceftolozane
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
---

# Ceftolozane
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

# Ceftolozane: From Complicated Urinary Tract Infections to Gonococcal Urethritis

## One-Sentence Summary

Ceftolozane is a novel cephalosporin (beta-lactam) antibiotic, clinically used in combination with tazobactam (as Ceftolozane/tazobactam, brand name Zerbaxa) for complicated urinary tract infections and hospital-acquired/ventilator-associated bacterial pneumonia.
The TxGNN model predicts it may be effective for **Gonococcal Urethritis**, with a prediction score of **99.89%** — however, **0 clinical trials** and **0 publications** specifically support this repurposing direction, and mechanistic support is assessed as weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Complicated urinary tract infections (cUTI), hospital-acquired bacterial pneumonia — based on global drug profile (Zerbaxa); no Singapore registration data available |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Ceftolozane is a cephalosporin-class beta-lactam antibiotic that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs) — with particularly enhanced affinity for PBP1b, PBP1c, and PBP3 in Gram-negative bacteria and notable potency against *Pseudomonas aeruginosa*. In clinical use, it is always combined with the beta-lactamase inhibitor tazobactam to broaden its spectrum against beta-lactamase-producing organisms.

*Neisseria gonorrhoeae*, the causative agent of gonococcal urethritis, is a Gram-negative diplococcus that is theoretically susceptible to beta-lactam antibiotics — this is the theoretical basis for the TxGNN prediction. The global rise of Ceftriaxone-resistant *N. gonorrhoeae* (a serious public health concern) has created genuine interest in identifying alternative cephalosporins or beta-lactam combinations, which gives this prediction some contextual relevance as a research question.

However, the mechanistic support for Ceftolozane specifically is assessed as weak. There is minimal published in vitro data characterising Ceftolozane's activity against *N. gonorrhoeae*, and no PK/PD target-attainment data or clinical evidence for this indication exists. The current standard of care remains Ceftriaxone IM, and Ceftolozane/tazobactam is an IV-only formulation ill-suited for outpatient gonorrhea treatment. This prediction is best interpreted as a speculative signal for drug-resistant gonorrhea research rather than a near-term repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## All Predicted Indications — Overview

The TxGNN model generated 10 candidate indications for Ceftolozane. The mechanistic plausibility varies significantly across predictions:

| Rank | Disease | Score | Evidence Level | Assessment | Rationale Summary |
|------|---------|-------|---------------|------------|-------------------|
| 1 | Gonococcal Urethritis | 99.89% | L5 | Research Question | Gram-negative coverage theoretically applicable; no clinical data; IV formulation unsuitable for standard outpatient gonorrhea treatment |
| 2 | Ureaplasma Urethritis | 99.89% | L5 | **Hold — Mechanism Incompatible** | *Ureaplasma* lacks a peptidoglycan cell wall; beta-lactams are entirely ineffective |
| 3 | Uterine Inflammatory Disease | 99.88% | L5 | **Hold** | PID requires coverage for *Chlamydia* (intracellular; beta-lactam-insensitive) and anaerobes; does not match CDC treatment guidelines |
| 4 | Xanthogranulomatous Pyelonephritis | 99.88% | L4 | Research Question | Caused by Gram-negatives (*E. coli*, *Proteus*) within Ceftolozane's coverage; 1 indirect review reference; surgery is the primary treatment |
| 5 | Polyclonal Hyperviscosity Syndrome | 99.52% | L5 | **Hold — Mechanism Incompatible** | B-cell/immunoglobulin disorder; antibiotics have no known effect on immunoglobulin production |
| 6 | Hyperamylasemia | 99.52% | L5 | **Hold — Mechanism Incompatible** | Biochemical marker of pancreatic/salivary injury, not a bacterial target; no clinical rationale |
| 7 | Urogenital Tuberculosis | 99.50% | L5 | **Hold — Mechanism Incompatible** | *Mycobacterium tuberculosis* is intrinsically resistant to cephalosporins due to its unique cell wall lipid layer |
| 8 | Congenital Analbuminemia | 99.44% | L5 | **Hold — Mechanism Incompatible** | Genetic ALB mutation; antibiotics have no corrective effect on protein synthesis defects |
| 9 | Blood Group Incompatibility | 99.22% | L5 | **Hold — Mechanism Incompatible** | Red blood cell antigen–antibody reaction; entirely unrelated to antimicrobial mechanism |
| 10 | Premalignant Hematological Disease | 99.11% | L5 | **Hold — Mechanism Incompatible** | MDS and similar disorders are driven by genomic instability; antibiotics have no therapeutic effect |

> **Note:** 7 of 10 predictions are mechanistically incompatible with Ceftolozane's antibiotic mechanism of action. These high TxGNN scores likely reflect co-morbidity network noise in the knowledge graph rather than true pharmacological signal.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No safety data — including key warnings, contraindications, or drug interactions — was available in this Evidence Pack for Ceftolozane. Package insert retrieval from the global Zerbaxa label is recommended as a priority action.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.89%), the evidence level is L5 (model prediction only) with no supporting clinical trials, observational studies, or publications for any of the top-ranked indications. The only biologically plausible candidate (gonococcal urethritis) has weak mechanistic support and faces significant practical barriers (IV-only formulation vs. outpatient disease; no in vitro characterisation against *N. gonorrhoeae*). The majority of other predictions are mechanistically incompatible and should be deprioritised. Ceftolozane is also not registered in Singapore, and all safety data is currently unavailable.

**To proceed with the gonococcal urethritis research question, the following is needed:**

- **In vitro MIC data**: Characterise Ceftolozane's minimum inhibitory concentrations against *N. gonorrhoeae*, including WHO-designated Ceftriaxone-resistant reference strains
- **PK/PD modelling**: Determine whether standard Ceftolozane/tazobactam dosing achieves adequate concentrations at the urethral mucosa to eradicate *N. gonorrhoeae*
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank API (currently flagged as a data gap)
- **Safety data**: Download and parse the Zerbaxa international package insert for warnings, contraindications, and drug interactions (currently a blocking data gap)
- **Formulation feasibility review**: Assess whether an IV antibiotic can be practically positioned for a condition primarily managed in outpatient/STI clinic settings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

