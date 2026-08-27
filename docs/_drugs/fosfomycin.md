---
layout: default
title: Fosfomycin
parent: 僅模型預測 (L5)
nav_order: 450
evidence_level: L5
indication_count: 10
---

# Fosfomycin
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

# Fosfomycin: From Bacterial Infections (Urinary Tract Infections) to Pyelitis

## One-Sentence Summary

> Fosfomycin is a broad-spectrum antibiotic long used for bacterial infections, most notably urinary tract infections (UTI).
> Among 10 diseases screened by the TxGNN model for this drug, **Pyelitis (renal pelvis infection)** stands out as the most clinically credible candidate,
> supported by **1 Phase 2/3 RCT** (the ZEUS trial) and **20 publications**, including cohort studies and treatment guidelines — while most of the other 9 candidates (e.g. Ureaplasma urethritis, xanthogranulomatous pyelonephritis, epiglottitis) show no supporting evidence or even mechanistic contradictions, and are best treated as model noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections, most notably urinary tract infections (UTI) — established antibacterial use; no Singapore label text is available in this evidence pack |
| Predicted New Indication | Pyelitis |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L1 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data from DrugBank has not yet been retrieved into this evidence pack (query pending resolution). Based on well-established pharmacology, however, fosfomycin is a phosphonic-acid antibiotic that inhibits **MurA (UDP-GlcNAc enolpyruvyl transferase)**, blocking an early, irreversible step of bacterial peptidoglycan (cell wall) synthesis. This mechanism requires an intact peptidoglycan cell wall to be effective — which is exactly why several other TxGNN-predicted candidates in this pack were rejected (e.g. *Ureaplasma urethritis*, a cell-wall-free mycoplasma, has no MurA target at all).

Pyelitis — inflammation of the renal pelvis, essentially an upper urinary tract infection — is caused predominantly by Gram-negative uropathogens such as *E. coli*, which possess a complete peptidoglycan cell wall. This makes pyelitis a textbook target population for fosfomycin's mechanism, and is consistent with fosfomycin's already well-documented efficacy in complicated UTI and acute pyelonephritis.

In other words, this is less a "surprising new indication" and more a **mechanistically confirmatory, evidence-rich extension** of fosfomycin's known antibacterial niche — the strongest and most defensible signal among the 10 candidates screened, which is why it is the focus of this report rather than the top-ranked-by-score but mechanistically implausible "Ureaplasma urethritis."

---

## Clinical Trial Evidence

Currently no related clinical trials are registered under this specific disease term ("pyelitis") on ClinicalTrials.gov. (Relevant Phase 2/3 randomized trial data exists but is captured in the Literature Evidence section below, since it was retrieved via PubMed rather than a trial registry match.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30861061](https://pubmed.ncbi.nlm.nih.gov/30861061/) | 2019 | RCT (Phase 2/3, ZEUS trial) | Clinical Infectious Diseases | IV fosfomycin (ZTI-01) vs piperacillin-tazobactam for complicated UTI including acute pyelonephritis — pivotal randomized trial establishing efficacy in upper UTI |
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Review / Network meta-analysis | Journal of Comparative Effectiveness Research | Systematic comparison of treatment options for complicated UTI/acute pyelonephritis, including fosfomycin, amid rising drug resistance |
| [31608743](https://pubmed.ncbi.nlm.nih.gov/31608743/) | 2020 | Review | Postgraduate Medicine | Reviews UTI treatment in the era of antimicrobial resistance; positions fosfomycin among recommended options |
| [33819054](https://pubmed.ncbi.nlm.nih.gov/33819054/) | 2021 | Guideline/Review | Annals of Internal Medicine | ACP best-practice advice on short-course antibiotics for common infections including UTI |
| [32303061](https://pubmed.ncbi.nlm.nih.gov/32303061/) | 2020 | Retrospective cohort | Journal of Antimicrobial Chemotherapy | 1-year real-world review of oral fosfomycin use and outcomes for pyelonephritis and complicated UTI in a large healthcare system |
| [30839061](https://pubmed.ncbi.nlm.nih.gov/30839061/) | 2019 | Editorial commentary on ZEUS trial | Clinical Infectious Diseases | Discusses clinical implications of using IV fosfomycin for complicated UTI |
| [30854892](https://pubmed.ncbi.nlm.nih.gov/30854892/) | 2019 | Review | Future Microbiology | Overview of IV fosfomycin (ZTI-01) microbiology, pharmacology, and clinical experience in hospitalized complicated UTI patients |
| [36031053](https://pubmed.ncbi.nlm.nih.gov/36031053/) | 2023 | Review | Clinical Microbiology and Infection | UTI in pregnancy, including treatment considerations relevant to upper tract infection |
| [31160291](https://pubmed.ncbi.nlm.nih.gov/31160291/) | 2019 | Preclinical (murine model) | Antimicrobial Agents and Chemotherapy | Demonstrates unexpected efficacy of oral fosfomycin against resistant *E. coli* strains in a pyelonephritis mouse model |
| [23958364](https://pubmed.ncbi.nlm.nih.gov/23958364/) | 2013 | Review | Primary Care | General UTI review identifying fosfomycin as a first-line agent for cystitis/pyelonephritis |

---

## Singapore Market Information

Fosfomycin currently has **no registered product license in Singapore** (0 registrations; market status: Not marketed). No authorization number, product name, or approved indication text is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Pyelitis is a strong mechanistic and clinical fit for fosfomycin, supported by an L1-grade evidence base — a completed Phase 2/3 RCT (ZEUS trial) plus multiple cohort studies and guideline citations — making it far more defensible than the other 9 TxGNN candidates screened, most of which lack any supporting evidence or contradict fosfomycin's known mechanism. However, the drug is not currently marketed in Singapore and blocking safety data (package insert warnings/contraindications) is still missing, so a full "Go" cannot yet be issued.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (currently blocking — DG001)
- Confirmed mechanism of action data via DrugBank API query (currently pending — DG002)
- Formal drug-drug interaction (DDI) database check (current query status: not found)
- Singapore-specific regulatory pathway assessment, since the product is not currently registered in the market
- Route/dosage form compatibility review for treating pyelitis specifically (oral vs. IV fosfomycin)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

