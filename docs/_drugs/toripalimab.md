---
layout: default
title: Toripalimab
parent: 僅模型預測 (L5)
nav_order: 997
evidence_level: L5
indication_count: 10
---

# Toripalimab
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

# Toripalimab: From Anti-PD-1 Cancer Immunotherapy to Mixed-Type Autoimmune Hemolytic Anemia (Signal Requires Caution)

## One-Sentence Summary

Toripalimab is an anti-PD-1 monoclonal antibody used in oncology (documented in the evidence pack for esophageal, breast, nasopharyngeal, hepatocellular, and renal cancers, among others) to unleash T-cell-mediated anti-tumour immunity. The TxGNN model's top prediction suggests possible efficacy for **Mixed-Type Autoimmune Hemolytic Anemia**, but there are currently **0 clinical trials and 0 publications** supporting this specific direction — and the drug's known mechanism (breaking immune tolerance) points toward *causing*, not treating, this type of condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; internationally used as anti-PD-1 immunotherapy for solid tumours (inferred from literature evidence — no structured indication data available) |
| Predicted New Indication | Mixed-Type Autoimmune Hemolytic Anemia |
| TxGNN Prediction Score | 93.76% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the regulatory record (original_moa: Data Gap). However, evidence embedded across the predicted-indication rationales consistently describes toripalimab as an **anti-PD-1 monoclonal antibody**: it blocks the PD-1 checkpoint on T cells, removing a brake on immune activity so the immune system can attack tumour cells more effectively. This mechanism is the basis for its established use across multiple solid-tumour trials in this evidence pack (esophageal squamous cell carcinoma, HR+/HER2- breast cancer, nasopharyngeal carcinoma, hepatocellular carcinoma, renal cell carcinoma, mucosal melanoma).

**This mechanism runs in the opposite direction from the top prediction.** Mixed-type autoimmune hemolytic anemia (AIHA) results from the immune system inappropriately attacking red blood cells. Because toripalimab *removes* immune restraint rather than restoring tolerance, PD-1/PD-L1 inhibitors as a class are documented to **induce** immune-related adverse events (irAEs) — including autoimmune hemolytic anemia, dermatitis, SJS/TEN, immune nephritis/proteinuria, and dermatomyositis — rather than treat them. The TxGNN score here most plausibly reflects a "drug–adverse event" co-occurrence signal in the knowledge graph being misread as a "drug–treats–disease" signal, rather than a genuine therapeutic hypothesis.

No clinical trial or literature evidence in this evidence pack supports treating AIHA with toripalimab; zero records were retrieved for this candidate.

### Broader Pattern Across Top 10 Predictions

This is not an isolated issue with rank 1. **All 10 of the top-ranked predicted indications for toripalimab show the same reversed-mechanism pattern:**

| Rank | Disease | Evidence Level | Issue |
|------|---------|----------------|-------|
| 1 | Mixed-type autoimmune hemolytic anemia | L5 | No evidence; mechanism reversed (PD-1i induces, not treats) |
| 2 | Idiopathic aplastic anemia | L5 | No evidence; immune activation could worsen marrow damage |
| 3 | Dermatitis | L4 | Literature confirms PD-1i *causes* dermatitis/SJS-TEN as irAE |
| 4 | Paroxysmal nocturnal hemoglobinuria | L5 | No mechanistic link (complement-mediated, not T-cell) |
| 5 | Drug-induced autoimmune hemolytic anemia | L5 | PD-1i is itself a known cause of this condition |
| 6 | Proteinuria | L4 | Literature shows proteinuria as a treatment-emergent toxicity in combination oncology trials, not a treated condition |
| 7 | Acne keloid | L5 | No mechanistic link, no evidence |
| 8 | Neonatal autoimmune hemolytic anemia | L5 | No paediatric safety data; mechanism reversed |
| 9 | Primary CD59 deficiency | L5 | No biological overlap (complement regulatory defect) |
| 10 | Amyopathic dermatomyositis | L5 | Known irAE of checkpoint inhibitors, not a treatment target |

This systemic pattern suggests the underlying TxGNN prediction signal for this drug is being driven by adverse-event co-occurrence data rather than genuine therapeutic relationships, and warrants methodological review before any of these candidates are advanced.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Mixed-Type Autoimmune Hemolytic Anemia.

---

## Literature Evidence

Currently no related literature available for Mixed-Type Autoimmune Hemolytic Anemia.

---

## Singapore Market Information

Toripalimab is **not marketed** in Singapore (0 registered licenses). No product authorization records are available.

---

## Cytotoxicity (Antineoplastic Drugs Only)

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 immune checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (mechanism is immune-modulatory, not cytotoxic to bone marrow); however, immune-related adverse events (irAEs) affecting haematological, dermatological, and renal systems are well documented in the literature evidence above |
| Emetogenicity Classification | Low (typical for checkpoint inhibitor monotherapy) |
| Monitoring Items | Skin/mucosal exam (dermatitis, SJS/TEN risk), renal function and urinalysis (proteinuria/nephritis risk), CBC (autoimmune cytopenia risk), thyroid and liver function |
| Handling Protection | Standard biologic infusion precautions; cytotoxic drug handling regulations do not apply (monoclonal antibody, not chemotherapy) |

---

## Safety Considerations

Official warnings, contraindications, and drug interaction data are not available in this evidence pack (source: TFDA label pending — see remediation DG001).

**Immune-related adverse events identified from literature evidence (not official labeling):** Case reports and reviews associated with toripalimab and the PD-1/PD-L1 inhibitor class document Stevens-Johnson syndrome/toxic epidermal necrolysis (PMID 39347662, 41656837), lichenoid drug eruption (PMID 34632814), and treatment-emergent proteinuria/renal toxicity in combination regimens (PMID 38687583, 38862251, 35012303, 31403867). These findings reinforce that this drug class carries meaningful immune-mediated toxicity risk and should not be interpreted as evidence of therapeutic benefit for the conditions in question.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 top-ranked predicted indications for toripalimab are either unsupported by any clinical or literature evidence (L5) or supported only by evidence that documents the drug *causing* the condition as an adverse event rather than treating it (L4). No candidate in this set meets the threshold for further development.

**To proceed, the following is needed:**
- Official TFDA/manufacturer label data (warnings, contraindications, DDI) — currently blocking (DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- A methodological review of the TxGNN scoring for this drug, given the consistent reversed-causality pattern across all top 10 predictions, before any candidate from this drug's prediction set is escalated to S1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

