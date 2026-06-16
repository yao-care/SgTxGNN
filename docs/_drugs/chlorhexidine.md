---
layout: default
title: Chlorhexidine
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
---

# Chlorhexidine
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

根據 Evidence Pack 內容，以下是 Chlorhexidine 的老藥新用評估報告：

---

# Chlorhexidine: From Antiseptic/Disinfectant Use to Chronic Ethmoidal Sinusitis

## One-Sentence Summary

Chlorhexidine (CHX) is a broad-spectrum bisbiguanide antiseptic widely established globally for surgical site preparation, oral hygiene, and wound disinfection.
The TxGNN model predicts it may be effective for **Chronic Ethmoidal Sinusitis**,
with **0 clinical trials** and **1 publication** directly supporting this specific indication. The broader sinusitis cluster (sinusitis, chronic rhinosinusitis) shows incrementally stronger support, including a 2024 otorhinolaryngology review and a 2021 in vitro sinonasal stent study, suggesting that CHX's anti-biofilm properties hold mechanistic plausibility across the sinonasal disease spectrum.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; used globally as broad-spectrum antiseptic (surgical scrub, wound care, oral hygiene) |
| Predicted New Indication | Chronic Ethmoidal Sinusitis |
| TxGNN Prediction Score | 95.46% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known information, Chlorhexidine is a bisbiguanide compound that acts as a broad-spectrum antiseptic and anti-biofilm agent. Its efficacy in surface and mucosal disinfection — including nasal cavity antisepsis — has been demonstrated in clinical practice, forming the mechanistic basis for the TxGNN prediction.

Chronic ethmoidal sinusitis is primarily driven by persistent bacterial infection and biofilm formation within the ethmoidal air cells — the same pathological processes that CHX directly targets. Key pathogens in chronic sinusitis, including *Staphylococcus aureus* and *Pseudomonas aeruginosa*, fall within CHX's established antibacterial spectrum. The adjacent indication **chronic rhinosinusitis** (TxGNN rank #3) has slightly stronger empirical backing: a 2021 in vitro study (PMID 34834197) directly demonstrated that CHX slow-release varnish–coated sinonasal stents sustained antibacterial and anti-biofilm activity against both pathogens in a sinonasal cavity model. A 2024 HNO review (PMID 38592477) further confirmed CHX's role in ENT antisepsis, specifically for MRSA decolonization.

The lone directly relevant publication for ethmoidal sinusitis (PMID 16008068, *Rhinology* 2005) investigated nasal cavity disinfection with CHX in chronic sinusitis patients and studied the bacteriology of the bulla ethmoidalis — providing face-valid, if not efficacy-level, support for CHX's applicability to this anatomic site. Taken together, the mechanistic connection is biologically coherent, but clinical evidence remains at the preclinical/mechanistic stage.

---

## Clinical Trial Evidence

No clinical trials specifically targeting **chronic ethmoidal sinusitis** with Chlorhexidine are currently registered on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [16008068](https://pubmed.ncbi.nlm.nih.gov/16008068/) | 2005 | Clinical Study | Rhinology | Investigated the role of nasal cavity CHX disinfection in chronic sinusitis patients; examined bacteriology of the bulla ethmoidalis — anatomically and clinically the most directly relevant study for ethmoidal sinusitis |

---

## Singapore Market Information

Chlorhexidine is currently **not registered** in Singapore. No Health Sciences Authority (HSA) authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Clinical evidence for Chlorhexidine in chronic ethmoidal sinusitis is limited to a single bacteriological study (L4). No Singapore HSA registration exists, detailed MOA and safety data are unavailable, and no indication-specific clinical trials have been conducted. The prediction is mechanistically coherent but lacks the clinical data foundation required to advance beyond a research hypothesis.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank API (DG002 remediation)
- Singapore HSA and TFDA package insert review for safety warnings and contraindications (DG001 remediation)
- Drug interaction assessment for Chlorhexidine
- Route-of-administration compatibility assessment: evaluate whether a nasal irrigation or sinonasal stent formulation is feasible for the ethmoidal indication
- Dedicated preclinical or pilot clinical study assessing CHX nasal irrigation in chronic ethmoidal sinusitis patients
- Cross-indication scoping review across the sinusitis cluster (ranks 1–3: chronic ethmoidal sinusitis, sinusitis, chronic rhinosinusitis) to determine whether a unified research programme is warranted — chronic rhinosinusitis (rank #3, L3 evidence) may be the stronger entry point given the CHX-coated sinonasal stent in vitro data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

