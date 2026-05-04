---
layout: default
title: Dactinomycin
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Dactinomycin
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

# Dactinomycin: From Rhabdomyosarcoma to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Dactinomycin (Actinomycin D) is a cytotoxic antibiotic that has been a cornerstone of pediatric oncology for decades, used as the "A" component of the VAC regimen (Vincristine + Actinomycin D + Cyclophosphamide) for rhabdomyosarcoma, Wilms' tumor, and related solid tumors.
The TxGNN model predicts it may have relevance in **Relapsing-Remitting Multiple Sclerosis (RRMS)**,
however, **0 clinical trials** and **0 supporting publications** currently exist for this direction, placing evidence at the lowest possible level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rhabdomyosarcoma, Wilms' tumor (VAC regimen component; pediatric solid tumors) |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Dactinomycin (Actinomycin D) is a DNA-intercalating antibiotic that binds to guanine-cytosine base pairs in double-stranded DNA, blocking RNA polymerase elongation and thereby halting RNA synthesis. This mechanism selectively targets rapidly proliferating cells, which underpins its longstanding role as the backbone of the VAC chemotherapy regimen for pediatric rhabdomyosarcoma and Wilms' tumor.

Relapsing-Remitting Multiple Sclerosis is an autoimmune demyelinating disease in which autoreactive T-cells (particularly Th17 cells) and B-cells attack myelin sheaths in the central nervous system. The theoretical basis for the TxGNN prediction is that dactinomycin's broad cytotoxicity could non-specifically suppress autoreactive lymphocyte proliferation — mechanistically similar to the reasoning behind early use of cyclophosphamide in MS. However, this is a blunt, non-selective mechanism with no MS-specific immune modulation (e.g., no selectivity for Th17/Treg axis, no remyelination support, no CNS trafficking modulation).

In contemporary RRMS management, approved disease-modifying therapies such as interferon-beta, natalizumab, and ocrelizumab offer targeted, well-characterised immune modulation with substantially more favourable safety profiles. Dactinomycin's significant myelosuppression risk, hepatotoxicity (including veno-occlusive disease), and lack of any published MS evidence make the benefit-risk ratio unfavourable. The high TxGNN score reflects a model-computed graph association rather than strong biological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Dactinomycin is currently **not registered or marketed in Singapore**. No product authorisations on record.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Antibiotic class — DNA intercalator / RNA synthesis inhibitor) |
| Myelosuppression Risk | High — neutropenia, thrombocytopenia, and anaemia are well-established class effects; dose-dependent bone marrow suppression is a primary toxicity |
| Emetogenicity Classification | Moderate |
| Monitoring Items | Full blood count (FBC) with differential before each cycle; liver function tests (ALT, AST, bilirubin); renal function; vigilance for hepatic veno-occlusive disease (particularly in young children) |
| Handling Protection | Must be handled in accordance with cytotoxic drug handling regulations; closed-system drug transfer devices, appropriate PPE, and negative-pressure preparation environment required |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or preclinical evidence supporting dactinomycin in relapsing-remitting multiple sclerosis, and the mechanistic link is weak — non-specific cytotoxicity is not a recognised nor sufficient mode of action for MS disease modification, and the drug's established toxicity profile is disproportionate to any theoretical immunosuppressive benefit when compared with approved RRMS therapies.

**To proceed, the following is needed:**
- Preclinical in vitro and in vivo data demonstrating selective suppression of autoreactive T-cell or B-cell populations at sub-cytotoxic dactinomycin concentrations
- Mechanistic studies distinguishing any immune-modulatory effect from general RNA synthesis inhibition
- Comparative benefit-risk modelling against existing RRMS first-line and second-line DMTs
- Formal MOA data from DrugBank to complete the mechanistic gap (Data Gap DG002)
- Full package insert review for warnings and contraindications (Data Gap DG001, currently blocking S1 safety evaluation)

> **Note on other TxGNN predictions:** While RRMS (Rank 1) holds the highest model score, it has the weakest clinical evidence (L5). For clinical teams seeking actionable repurposing leads, **Rank 5 — Parameningeal Embryonal Rhabdomyosarcoma — carries L1 evidence** (two Phase 3 IRS studies directly involving dactinomycin as a VAC regimen component) and a "Proceed with Guardrails" recommendation. Additional RMS subtypes (Ranks 2–6) and liver sarcoma (Rank 7, L2) represent a coherent mechanistic cluster where dactinomycin's role in the VAC backbone provides direct, biologically plausible support.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

