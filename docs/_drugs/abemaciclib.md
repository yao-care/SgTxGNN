---
layout: default
title: Abemaciclib
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Abemaciclib
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

# Abemaciclib: From Breast Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Abemaciclib is a CDK4/6 inhibitor globally approved for hormone receptor-positive (HR+)/HER2-negative breast cancer, though it holds no registration in Singapore.
The TxGNN model's top predicted new indication is **Rheumatoid Arthritis** (score: **97.32%**);
however, the sole supporting publication (PMID 40504547) documents CDK4/6 inhibitor-induced autoimmune adverse events — a **reverse safety signal** rather than therapeutic benefit — and **no clinical trials** directly explore this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HR+/HER2- Breast Cancer (globally approved; no Singapore registration on record) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 97.32% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Abemaciclib selectively inhibits cyclin-dependent kinases 4 and 6 (CDK4/6), blocking the G1-to-S phase transition of the cell cycle. In HR+/HER2- breast cancer, overactive CDK4/6 drives unchecked tumour proliferation, and blocking this pathway has demonstrated clear clinical benefit. Beyond oncology, CDK4/6 inhibition has been shown in experimental settings to suppress T-cell proliferation and reduce pro-inflammatory cytokines such as IL-6 and TNF-α — two central mediators of rheumatoid arthritis (RA) synovitis. This theoretical immunomodulatory overlap is likely what drove the TxGNN knowledge graph to assign a high score.

However, the only clinical evidence retrieved points in the **opposite direction**. PMID 40504547 is a retrospective pharmacovigilance study describing immune-mediated adverse events — including RA-like inflammatory arthritis — arising as **side effects** of CDK4/6 inhibitor therapy in breast cancer patients. This is a reverse safety signal: the drug may trigger, not treat, RA-like autoimmune conditions in some individuals.

The TxGNN score almost certainly reflects shared immune and inflammatory pathway nodes in the underlying knowledge graph rather than direct pharmacological evidence for efficacy. Without dedicated pre-clinical models or prospective trials, this prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Abemaciclib in Rheumatoid Arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Retrospective / Pharmacovigilance | *The Oncologist* | CDK4/6 inhibitors combined with endocrine therapy in HR+/HER2- breast cancer were associated with both pre-existing and new-onset immune-mediated diseases, including RA-like inflammatory arthritis. This represents a **safety signal rather than therapeutic benefit** for RA. |

---

## Singapore Market Information

Abemaciclib currently holds **no product registrations** in Singapore. The drug is marketed internationally as Verzenio® (Eli Lilly) for HR+/HER2- breast cancer and high-risk early-stage HR+/HER2- breast cancer adjuvant therapy, but no application has been recorded in Singapore's regulatory database.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — CDK4/6 inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Moderate — neutropenia is a known class effect; generally less severe than conventional chemotherapy |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (haematological toxicity), liver function tests (hepatotoxicity), renal function, QTc interval / ECG monitoring (cardiovascular risk) |
| Handling Protection | Standard oral targeted agent precautions; cytotoxic drug handling protocols are recommended as a precaution |

---

## Safety Considerations

Full package insert safety data (warnings, contraindications) were not available in this evidence pack and could not be assessed. Two clinically important safety signals are nonetheless identifiable from the retrieved evidence:

- **Cardiovascular risk**: Multiple systematic reviews and meta-analyses (identified in the heart disease evidence block of this pack — see PMIDs 39254653, 41422771) confirm that CDK4/6 inhibitors as a class are associated with QTc prolongation and increased risk of major cardiovascular adverse events. Abemaciclib appears to carry lower cardiovascular risk than ribociclib, but monitoring is still warranted.
- **Immune-mediated adverse events**: RA-like arthritis and other autoimmune conditions have been reported in breast cancer patients receiving CDK4/6 inhibitors, as documented in PMID 40504547.

Please refer to the Verzenio® (Abemaciclib) prescribing information for complete warnings, contraindications, and drug interaction details.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole publication identified for the rheumatoid arthritis indication constitutes a reverse safety signal — documenting the drug as a *cause* of RA-like arthritis rather than a *treatment* for it. No clinical trials or pre-clinical RA models exist to support pursuing this indication further at this stage.

**Notable alternative predictions worth monitoring:**

| Indication | Evidence Level | Key Signal |
|------------|---------------|------------|
| Multiple Endocrine Neoplasia (Rank 3) | L3 | Indirect Phase 1/2 trial coverage via pancreatic and endocrine tumour arms; CDK4 overexpression in pNETs provides a plausible mechanistic link |
| Amyotrophic Lateral Sclerosis (Rank 10) | L4 | Pre-clinical data (PMID 38596406) shows Abemaciclib accelerates autophagic flux and clears TDP-43 aggregates — the core pathological hallmark of ALS — in vitro and in vivo |

**To advance any of these candidates, the following steps are needed:**

- Obtain full mechanism of action (MOA) data from DrugBank (currently a data gap)
- Retrieve the Verzenio® Singapore/international package insert to complete the safety profile
- For RA specifically: dedicated pre-clinical studies in collagen-induced arthritis models to determine whether CDK4/6 inhibition is net anti-inflammatory or pro-autoimmune
- For ALS specifically: design a Phase 0/1 proof-of-concept trial powered by the autophagy/TDP-43 biomarker hypothesis
- For MEN specifically: review umbrella trial protocols (NCT03280563, NCT04802759) to determine whether endocrine neoplasia subtypes are explicitly enrolled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

