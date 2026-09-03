---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 683
evidence_level: L5
indication_count: 10
---

# Mupirocin
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

Using the drug-repurposing evaluation report format from the system prompt (no dedicated skill matches this task type; proceeding directly per the detailed instructions provided).

Note: among the 10 TxGNN-predicted indications for Mupirocin, rank 1 ("pleural empyema") has **zero evidence** (pure model score, `Hold`, explicitly flagged in its own rationale as "無任何臨床或臨床前證據支持"). I selected **Staphylococcal Scalded Skin Syndrome (rank 9)** as the reportable candidate instead — it is the only prediction reaching `decision_stage: S2` with 14 supporting publications and a coherent mechanistic rationale, making it the substantively evaluable candidate in this pack.

---

# Mupirocin: From Topical Staphylococcal Skin Infections to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

Mupirocin is a topical antibacterial that inhibits bacterial isoleucyl-tRNA synthetase, historically used against skin infections and nasal carriage caused by *Staphylococcus aureus* (including MRSA). Among 10 TxGNN-predicted indications, **Staphylococcal Scalded Skin Syndrome (SSSS)** shows by far the strongest supporting evidence, with **14 publications** identified, though **no dedicated clinical trials** are currently registered for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Topical treatment of bacterial skin infections (e.g., impetigo) and nasal *S. aureus*/MRSA decolonization — no Singapore license record available to cite directly |
| Predicted New Indication | Staphylococcal Scalded Skin Syndrome (SSSS) |
| TxGNN Prediction Score | 95.57% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The drug-level `original_moa` field is a data gap, but the mechanism is documented within the evidence pack itself: mupirocin inhibits bacterial isoleucyl-tRNA synthetase, blocking protein synthesis, and is bactericidal against *Staphylococcus aureus*, including MRSA.

SSSS is a toxin-mediated disease caused by exfoliative toxin (ETA/ETB)-producing strains of *S. aureus* — the same organism mupirocin's original clinical use targets. Topical/intranasal mupirocin is already established for eradicating *S. aureus* carriage and as adjunct therapy for staphylococcal skin infections such as impetigo, so extending it to SSSS management (reducing toxin-producing bacterial load as an adjunct to systemic therapy) is mechanistically coherent rather than a novel hypothesis.

This is reinforced directly by the literature: one cohort study (PMID 37404367) specifically evaluates 2% mupirocin ointment combined with IV antibiotics in pediatric SSSS treatment, and several molecular-epidemiology papers track mupirocin-resistant *S. aureus* clones as a clinically relevant resistance concern in SSSS outbreaks — implying mupirocin is already part of real-world SSSS management practice.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37404367](https://pubmed.ncbi.nlm.nih.gov/37404367/) | 2023 | Cohort | Clinical, Cosmetic and Investigational Dermatology | Compared IV antibiotics combined with 2% mupirocin ointment in pediatric SSSS, evaluating treatment duration, influencing factors, and cost |
| [15482208](https://pubmed.ncbi.nlm.nih.gov/15482208/) | 2004 | Review | Expert Review of Anti-Infective Therapy | Reviews treatment of bullous impetigo and SSSS in infants, both caused by exfoliative toxin-producing *S. aureus* |
| [8435912](https://pubmed.ncbi.nlm.nih.gov/8435912/) | 1993 | Review | Dermatologic Clinics | Review on controlling staphylococcal skin disease; notes topical mupirocin as a valuable addition to antistaphylococcal management |
| [16009455](https://pubmed.ncbi.nlm.nih.gov/16009455/) | 2005 | Outbreak Investigation/Cohort | Journal of Hospital Infection | Nosocomial SSSS outbreak in 13 neonates; epidemiological and case-control investigation of transmission and control |
| [9576389](https://pubmed.ncbi.nlm.nih.gov/9576389/) | 1998 | Cohort/Molecular Epidemiology | Pediatric Infectious Disease Journal | Molecular epidemiology of SSSS in premature infants in a NICU, with infection-control strategy outcomes |
| [35901469](https://pubmed.ncbi.nlm.nih.gov/35901469/) | 2022 | Case Report Series | Advances in Neonatal Care | Case series on neonatal SSSS identification and wound care management |
| [27047925](https://pubmed.ncbi.nlm.nih.gov/27047925/) | 2014 | Case Report | Dermatopathology | SSSS in an adult undergoing chemotherapy — an uncommon presentation outside the typical pediatric population |
| [30418106](https://pubmed.ncbi.nlm.nih.gov/30418106/) | 2019 | Case Report/Epidemiology | Journal of Medical Microbiology | Emergence of SSSS linked to a new toxinogenic, mupirocin- and fusidic acid-resistant MSSA clone |
| [31725120](https://pubmed.ncbi.nlm.nih.gov/31725120/) | 2020 | Epidemiological | Pediatric Infectious Disease Journal | Rising SSSS case numbers caused by ST121 *S. aureus* strain in Houston, Texas |
| [28592549](https://pubmed.ncbi.nlm.nih.gov/28592549/) | 2017 | Epidemiological | Journal of Clinical Microbiology | Emergence of a mupirocin- and fusidic acid-resistant *S. aureus* clone causing skin infections — relevant to resistance monitoring |

## Singapore Market Information

Mupirocin currently has **no registration records** in Singapore (0 licenses on file; market status "未上市/Not marketed"). No authorization details are available to report.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The literature base (14 publications, evidence level L3) supports a mechanistically plausible role for mupirocin as adjunct therapy in SSSS, driven by shared pathogen biology with mupirocin's established staphylococcal indications. However, this evidence pack has a **Blocking** data gap (DG001: HSA/product-label warnings and contraindications unavailable), which prevents even an initial safety assessment, and mupirocin is not currently registered in Singapore.

**To proceed, the following is needed:**
- HSA-approved package insert (warnings, contraindications) to clear the blocking safety gap (DG001)
- DrugBank-confirmed MOA record to close the mechanism-of-action data gap (DG002)
- Regulatory pathway assessment for Singapore registration, since no local license currently exists
- A prospective study (RCT or larger controlled cohort) specifically testing mupirocin as adjunct SSSS therapy, since current evidence is observational/case-based
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

