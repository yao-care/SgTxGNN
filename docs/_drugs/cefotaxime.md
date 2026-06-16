---
layout: default
title: Cefotaxime
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Cefotaxime
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

The txgnn-pipeline skill covers model training and deployment — report generation is governed by the system prompt format. Proceeding directly with the evaluation report.

---

# Cefotaxime: From Bacterial Infections to Pneumococcal Meningitis

## One-Sentence Summary

Cefotaxime is a third-generation cephalosporin antibiotic with established global use for serious bacterial infections, including central nervous system infections.
Among the ten indications predicted by the TxGNN model, **Pneumococcal Meningitis** (TxGNN rank 8) is the only actionable candidate — ranked first by evidence quality — with **1 completed Phase 4 clinical trial** and **20 publications**, including multiple international treatment guidelines, collectively supporting an **Evidence Level L1** classification.
The top TxGNN-scored predictions (ranks 1–7, e.g., polyclonal hyperviscosity syndrome, congenital analbuminemia) all carry zero supporting evidence and a "Hold" recommendation; this report therefore focuses on the clinically meaningful finding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (formal dataset entry unavailable; pharmacologically well-established) |
| Predicted New Indication | Pneumococcal Meningitis |
| TxGNN Prediction Score | 96.73% (overall rank 8 by score; rank 1 by evidence strength) |
| Evidence Level | L1 |
| Singapore Market Status | Not marketed (0 HSA registrations on record) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cefotaxime exerts its bactericidal effect by binding to penicillin-binding proteins **PBP1A and PBP3**, thereby inhibiting bacterial cell wall synthesis and causing cell lysis. This mechanism is directly applicable to *Streptococcus pneumoniae*, the causative organism in pneumococcal meningitis, against which cefotaxime demonstrates high in vitro potency (MIC90 typically ≤ 0.5 μg/mL). While formal MOA data was not retrievable from the DrugBank entry in this dataset, the mechanism is confirmed by the pharmacokinetic and pharmacodynamic evidence cited in the literature below.

A critical pharmacokinetic feature that makes cefotaxime particularly suited for CNS infections is its ability to cross the blood-brain barrier under conditions of meningeal inflammation. Cerebrospinal fluid (CSF) penetration reaches **10–20% of serum levels**, sufficient to achieve and sustain bactericidal concentrations against susceptible pneumococci — a finding validated in a multicentre retrospective study of adult patients receiving high-dose cefotaxime for confirmed *S. pneumoniae* meningitis (PMID 34120184). This distinguishes cefotaxime from many antibiotics that fail to reach therapeutic CNS concentrations.

The connection between bacterial meningitis (cefotaxime's established domain) and pneumococcal meningitis specifically is direct and mechanistically unambiguous: *S. pneumoniae* remains the most common bacterial cause of meningitis in children beyond the neonatal period and in adults. National and international treatment guidelines from the United States (PMID 12182395), France (PMID 37741342), and other jurisdictions explicitly list cefotaxime or ceftriaxone as the empiric first-line backbone for bacterial meningitis, with or without vancomycin depending on local resistance patterns. The absence of Singapore HSA marketing authorisation represents a **regulatory gap**, not a gap in clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01540838](https://clinicaltrials.gov/study/NCT01540838) | Phase 4 | Completed | 375 | RCT conducted at Hospital Pediátrico David Bernardino, Angola. Tested whether slow continuous β-lactam (cefotaxime) infusion combined with high-dose oral paracetamol over the first 4 days reduces mortality in childhood bacterial meningitis, including pneumococcal meningitis, compared to traditional bolus dosing four times daily. Directly evaluates cefotaxime dosing optimisation in pneumococcal meningitis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36326246](https://pubmed.ncbi.nlm.nih.gov/36326246/) | 2022 | Real-World Cohort | Antimicrobial Agents and Chemotherapy | 40-year cohort (1977–2018) on treatment of penicillin- and cephalosporin-resistant pneumococcal meningitis; defines cefotaxime MIC breakpoints per EUCAST and documents real-world therapy patterns |
| [37741342](https://pubmed.ncbi.nlm.nih.gov/37741342/) | 2023 | Review / Guideline | Infectious Diseases Now | French national paediatric meningitis guideline; confirms that conjugate vaccination has eliminated most beta-lactam-resistant strains; cefotaxime/ceftriaxone remain standard of care for empiric treatment |
| [12182395](https://pubmed.ncbi.nlm.nih.gov/12182395/) | 2002 | Review / Guideline | Pediatric Infectious Disease Journal | U.S. management guideline for pneumococcal meningitis; recommends cefotaxime or ceftriaxone + vancomycin as empiric therapy for all infants and children; discusses optimisation for strains with elevated MICs |
| [34120184](https://pubmed.ncbi.nlm.nih.gov/34120184/) | 2021 | Multicentre Retrospective | Journal of Antimicrobial Chemotherapy | First multicentre study to describe CSF cefotaxime concentrations in adult pneumococcal meningitis patients receiving high-dose regimens; validates 10–20% CSF penetration as sufficient for bactericidal activity |
| [4055060](https://pubmed.ncbi.nlm.nih.gov/4055060/) | 1985 | Clinical Study | Infection | 46 consecutive patients (ages 1–79 years) with pneumococcal meningitis treated with cefotaxime monotherapy 200 mg/kg/day for 12–27 days; all isolates susceptible; established proof-of-concept clinical efficacy |
| [19047432](https://pubmed.ncbi.nlm.nih.gov/19047432/) | 2008 | Review | Pediatrics in Review | Paediatric meningitis overview; empiric therapy in non-neonates is parenteral vancomycin + cefotaxime or ceftriaxone; reviews clinical presentation and outcome prediction |
| [38558854](https://pubmed.ncbi.nlm.nih.gov/38558854/) | 2024 | Multicentre Cohort | Frontiers in Cellular and Infection Microbiology | Multicentre epidemiology of paediatric pneumococcal meningitis in China (2019–2020); reports drug sensitivity patterns of *S. pneumoniae* isolates relevant to Asian clinical settings |
| [41342594](https://pubmed.ncbi.nlm.nih.gov/41342594/) | 2025 | Cohort Study | Revista Española de Quimioterapia | Tertiary hospital cohort; analyses serotype distribution, vaccination status, and clinical outcomes; identifies serotypes with highest invasive potential in the post-conjugate-vaccine era |
| [16216469](https://pubmed.ncbi.nlm.nih.gov/16216469/) | 2005 | Comparative Study | International Journal of Antimicrobial Agents | Head-to-head comparison of CSF penetration and antimicrobial efficacy of cefotaxime (50 mg/kg q6h) vs ceftriaxone (100 mg/kg once daily) in paediatric bacterial meningitis caused by *S. pneumoniae*, *H. influenzae*, and *N. meningitidis* |
| [33774218](https://pubmed.ncbi.nlm.nih.gov/33774218/) | 2021 | In Vitro Study | Journal of Global Antimicrobial Resistance | Evaluated daptomycin combinations with cefotaxime, amoxicillin, and rifampicin against major meningitis pathogens; cefotaxime used as the clinical reference standard, confirming its benchmark status |

---

## Singapore Market Information

Cefotaxime is **not currently recorded as holding any HSA marketing authorisation** in Singapore (0 licences on record in this dataset).

> **Important note:** The absence of Singapore registration is clinically surprising given cefotaxime's worldwide guideline-endorsed status for bacterial meningitis. This finding likely reflects either a genuine market access gap (ceftriaxone may have displaced cefotaxime in this market) or an incomplete data capture. Current HSA registration status should be verified directly at [HSA PRISM](https://www.hsa.gov.sg/therapeutic-products/information-for-registrants) before drawing regulatory conclusions.

---

## Safety Considerations

Formal product-specific safety data (HSA-approved warnings, contraindications, and drug interaction profiles) were not available in this dataset.

> Please refer to the approved package insert (SmPC or local equivalent) for comprehensive safety information.

**General class considerations applicable to cephalosporins:**
- **Hypersensitivity:** Anaphylaxis and other allergic reactions can occur; cross-reactivity with penicillins is estimated at 1–2%
- **GI effects:** *Clostridioides difficile*-associated diarrhoea with prolonged use
- **Haematological:** Rare drug-induced immune haemolytic anaemia (a case involving cefotaxime-sulbactam in a newborn with ABO incompatibility was identified in the literature, PMID 35003054 — relevant for neonatal use)
- **Renal:** Generally low nephrotoxicity compared to aminoglycosides; dose adjustment required in severe renal impairment

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pneumococcal meningitis is an L1-evidence indication for cefotaxime, endorsed by multiple international treatment guidelines and supported by validated CSF pharmacokinetics and decades of clinical use; the barrier to deployment is regulatory (no Singapore HSA registration on record), not clinical.

**To proceed, the following is needed:**

- **Verify HSA registration status** — confirm whether cefotaxime is genuinely unregistered in Singapore or whether the dataset is incomplete; if unregistered, assess whether ceftriaxone (a closely related agent) is already registered and covers the same clinical need
- **Obtain the full package insert** — required for Singapore-specific prescribing information including approved dosing, renal dose adjustments, and contraindications
- **Confirm local resistance surveillance data** — review HSA or National Centre for Infectious Diseases (NCID) antibiogram data on *S. pneumoniae* cephalosporin susceptibility in Singapore to establish whether empiric cefotaxime remains appropriate without mandatory vancomycin co-administration
- **Establish the regulatory pathway** — if product registration is required, evaluate HSA's abridged evaluation route (referencing established international approvals) or consider whether existing ceftriaxone registration already satisfies the clinical need
- **Safety review for vulnerable populations** — given the neonatal safety signal identified (PMID 35003054), document risk-mitigation measures for paediatric use before finalising the clinical protocol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

