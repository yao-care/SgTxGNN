---
layout: default
title: Sugammadex
parent: Low Evidence (L5)
nav_order: 938
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sugammadex: predicted new indication Breast fibrocystic disease (evidence level L5). Approved use: Not stated in the Singapore licence records (reversal of rocuronium/v…"
monitor_inn: "Sugammadex"
predicted_indications: ["breast fibrocystic disease", "Prinzmetal angina", "peripheral arterial disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "thrombotic disease", "tendinitis", "antithrombin deficiency type 2", "benign mammary dysplasia", "female breast carcinoma"]
---

# Sugammadex
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

# Sugammadex: From Reversal of Neuromuscular Blockade to Breast Fibrocystic Disease

## One-Sentence Summary

Sugammadex is a modified gamma-cyclodextrin used in anaesthesia to reverse neuromuscular blockade caused by steroidal agents such as rocuronium and vecuronium. The TxGNN model predicts it may be effective for **breast fibrocystic disease**, but there are **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on model output alone and has no plausible mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (reversal of rocuronium/vecuronium-induced neuromuscular blockade, based on the drug's known pharmacology) |
| Predicted New Indication | Breast fibrocystic disease |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, sugammadex works by chemically encapsulating steroidal neuromuscular blocking agents (rocuronium, vecuronium), which removes them from the neuromuscular junction. It does not act on hormone receptors, epithelial proliferation or breast tissue.

**The prediction is not mechanistically supported.** Fibrocystic breast change is a benign condition linked to hormonal and epithelial proliferative processes. Nothing in sugammadex's mechanism relates to this. The high TxGNN score most likely reflects an artifact of the knowledge graph rather than a biological signal.

Other top-ranked predictions show the same pattern. Apocrine adenosis, blunt duct adenosis and benign mammary dysplasia all have near-identical scores. They form a cluster of related benign breast conditions, so they probably reflect one correlated graph artifact rather than independent signals. Prinzmetal angina, peripheral arterial disease, tendinitis and antithrombin deficiency type 2 also have no credible mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top predicted indication (breast fibrocystic disease). The publications retrieved for other lower-ranked predictions are perioperative or safety-oriented. They do not show therapeutic benefit:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28714298](https://pubmed.ncbi.nlm.nih.gov/28714298/) | 2018 | Clinical study | Minerva Anestesiol | Effect of sugammadex on coagulation (rotational thromboelastometry) in morbidly obese patients. Relevant to the "thrombotic disease" prediction as a safety question only. |
| [22577926](https://pubmed.ncbi.nlm.nih.gov/22577926/) | 2012 | Case series | Anaesth Intensive Care | Sugammadex antagonising rocuronium in three patients with liver dysfunction undergoing TIPS. |
| [20422852](https://pubmed.ncbi.nlm.nih.gov/20422852/) | 2010 | Case report | Rev Esp Anestesiol Reanim | Sugammadex used to reverse rocuronium-induced blockade in a patient with myasthenia gravis. |
| [33863374](https://pubmed.ncbi.nlm.nih.gov/33863374/) | 2021 | Case report | J Med Case Rep | Postoperative malignant hyperthermia after breast cancer surgery. Sugammadex had no therapeutic role against the cancer. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13812P | Bridion Solution For Injection 100mg/ml | Injection, solution | Not stated in licence records |
| SIN16880P | Sugammadex Sandoz Solution For Injection 100mg/ml | Injection, solution | Not stated in licence records |
| SIN16933P | Sugammadex Scigen Solution For Injection 100mg/ml | Injection, solution | Not stated in licence records |
| SIN16988P | Sugammadex Kabi Solution For Injection 100 mg/ml | Injection, solution | Not stated in licence records |
| SIN16994P | Accodex Solution For Injection 100mg/ml | Injection, solution | Not stated in licence records |

---

## Safety Considerations

**Drug Interactions**: The data compiled for this report list 31 interactions in total, of which 20 are shown here.

- **Major**: hormonal contraceptives and progestogens, namely levonorgestrel, norethisterone, desogestrel, norgestrel, drospirenone and medroxyprogesterone acetate. This is clinically relevant for any breast-related use, since these agents are hormonal.
- **Moderate**: anticoagulants and antithrombotics, including warfarin, apixaban, rivaroxaban, edoxaban, betrixaban, dalteparin, ardeparin, bivalirudin, argatroban, desirudin, danaparoid, anisindione, antithrombin III human and antithrombin alfa.

Other perioperative safety points from the evidence review:
- Sugammadex can cause small, transient prolongation of aPTT and PT.
- The evidence review also notes bradycardia, rare anaphylaxis and coronary vasospasm case reports. These raise concern for use in patients with Prinzmetal angina.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or literature for the predicted indication and no plausible mechanistic link. The score is most likely a knowledge-graph artifact. None of the other top-ten predictions has therapeutic evidence either.

**To proceed, the following is needed:**
- A plausible biological rationale linking cyclodextrin-based encapsulation to breast tissue pathology.
- Package insert warnings and contraindications from the Singapore regulator, which are currently missing and block safety screening.
- Approved indication text from the Singapore licence records.
- Mechanism of action data from DrugBank.
- Any preclinical or clinical data for the predicted indication, none of which currently exists.
- Review of the major interactions with hormonal agents, given the breast-related setting.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

