---
layout: default
title: Meropenem
parent: 僅模型預測 (L5)
nav_order: 646
evidence_level: L5
indication_count: 10
---

# Meropenem
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

Using the report template exactly as specified in the prompt (this is a direct content-generation task per detailed instructions already given — no additional skill or clarification needed). I extracted directly from the Evidence Pack; where a field was `[Data Gap]` or an array was empty, I state that explicitly rather than fabricating values, and where the top-ranked prediction's own `scoring`/`repurposing_rationale` fields were `"pending"`, I derived an evidence-level judgment myself from the actual trial/literature content (noting the reasoning) rather than leaving it blank.

# Meropenem: From Severe Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

> Meropenem is a broad-spectrum carbapenem antibiotic; it is **not currently registered or marketed in Singapore**, but globally it is used for severe bacterial infections such as complicated intra-abdominal infection, complicated skin/soft-tissue infection, and bacterial meningitis.
> The TxGNN model predicts it may be effective for **Bacterial Arthritis**,
> with **1 clinical trial** and **20 publications** currently associated with this direction — though most of this evidence is indirect (bone/joint-infection cohort studies, case reports, and pharmacokinetic data) rather than a trial or review directly testing meropenem for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (see Market Status). Per global literature retained in this evidence pack (PMID 18416587), meropenem is used as empirical therapy for serious bacterial infections including complicated intra-abdominal infection, complicated skin/skin-structure infection, and bacterial meningitis. |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.92% (rank 1633 among candidates) |
| Evidence Level | L3 (see note below) |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

**Note on Evidence Level:** The one listed "Phase 3 completed" trial (NCT01371656) is a levofloxacin bacteremia-prevention study in leukemia/HSCT patients — it does not test meropenem, nor does it treat bacterial arthritis — so it does not count as direct L1/L2 evidence. The literature base instead consists mainly of retrospective cohort/observational studies on bone-and-joint infections (e.g., musculoskeletal melioidosis, paediatric bone/joint infection antibiograms) plus case reports and in-vitro/pharmacokinetic data. This profile corresponds to **L3 (observational studies)** rather than L1/L2, and there is no dedicated RCT for this specific indication.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for meropenem in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge of its drug class, meropenem is a **carbapenem** antibiotic that inhibits bacterial cell-wall synthesis by binding penicillin-binding proteins (PBPs), giving it broad-spectrum bactericidal activity against Gram-positive, Gram-negative, and anaerobic organisms — activity that has already been proven for severe systemic bacterial infections.

Bacterial (septic) arthritis is caused by many of the same organism classes meropenem already covers — *Staphylococcus aureus*, streptococci, Gram-negative bacilli (including *Haemophilus influenzae*, *Pseudomonas*, and Enterobacterales), and, in endemic regions, *Burkholderia pseudomallei* (melioidosis). Several publications retained in this evidence pack support in-vitro and real-world susceptibility of these organisms to meropenem in bone-and-joint infection contexts — for example, a 22-case retrospective review of musculoskeletal melioidosis reports that "all isolates were susceptible to meropenem" (PMID 39489417), and an orthopaedic-infection antibiogram study explicitly evaluates meropenem as an empiric option for septic arthritis and related bone/joint infections (PMID 37713001).

Mechanistically, therefore, the prediction is plausible and consistent with meropenem's established real-world (often off-label/empiric) use in complicated or multidrug-resistant septic arthritis — particularly when first-line agents (e.g., anti-staphylococcal penicillins, cefazolin) are inadequate due to resistance or Gram-negative/polymicrobial involvement. However, no study in this pack directly evaluates meropenem's clinical efficacy as a primary treatment for bacterial arthritis in a controlled trial; the supporting evidence is observational, case-based, or drawn from adjacent infection types (e.g., prosthetic joint infection, melioidosis).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01371656](https://clinicaltrials.gov/study/NCT01371656) | Phase 3 | Completed | 624 | Studies **levofloxacin** (not meropenem) to prevent bacteremia in children with acute leukemia/HSCT — a bacteremia-prevention trial, not a bacterial-arthritis treatment trial. Included here because it is the only trial the pack associates with this candidate, but it is **not directly relevant** to meropenem's use in bacterial arthritis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | Retrospective Cohort | Indian J Med Microbiol | Review of 22 culture-confirmed musculoskeletal melioidosis cases (osteomyelitis, septic arthritis, or both); all isolates were susceptible to meropenem. |
| [37713001](https://pubmed.ncbi.nlm.nih.gov/37713001/) | 2024 | Retrospective Cohort | Eur J Orthop Surg Traumatol | Antibiogram study for empiric antibiotic selection in non-spinal orthopaedic infections, including septic arthritis, fracture-related infection, and prosthetic joint infection. |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Retrospective Cohort | Clin Lab | Analysis of pathogen distribution and antimicrobial resistance in bone-and-joint infections among children under 4 years old. |
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | Retrospective Cohort | Infezioni Med | Retrospective cohort study characterizing osteoarticular melioidosis, a neglected cause of bone/joint infection. |
| [33857030](https://pubmed.ncbi.nlm.nih.gov/33857030/) | 2021 | Preclinical (in vitro) | J Bone Joint Surg Am | Evaluates thermal stability and elution kinetics of meropenem (among other alternative antibiotics) in PMMA bone cement, supporting local delivery for orthopaedic infection. |
| [39288382](https://pubmed.ncbi.nlm.nih.gov/39288382/) | 2024 | Case Report + Systematic Review | J Infect Dev Ctries | Case of leptospirosis-melioidosis coinfection presenting with ARDS and osteomyelitis, with systematic literature review. |
| [38139869](https://pubmed.ncbi.nlm.nih.gov/38139869/) | 2023 | Case Report | Pharmaceuticals (Basel) | Hip septic arthritis in an immunocompetent adult due to *Bacillus pumilus*/*Paenibacillus barengoltzii*, managed with long-term **linezolid** (not meropenem) — relevant disease context but not a meropenem treatment case. |
| [36678359](https://pubmed.ncbi.nlm.nih.gov/36678359/) | 2022 | Review | Pathogens (Basel) | Review of antibiotic options for melioidosis (which frequently involves bone/joint infection), positioning meropenem as a preferred agent for severe disease. |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | Review of off-label vs. formally recommended antibiotics (including carbapenems) for multidrug-resistant bacterial infections. |
| [39681779](https://pubmed.ncbi.nlm.nih.gov/39681779/) | 2025 | Population PK Study | Clin Pharmacokinet | Population pharmacokinetic study of meropenem across the adult lifespan, informing dosing optimization. |

*10 of the 20 retrieved publications are shown above, prioritized by relevance to bone/joint infection and meropenem use; the remaining publications (e.g., in-vitro susceptibility papers, unrelated case reports on sepsis/endocarditis/meningitis, and autoimmune-arthritis animal models) were judged less directly relevant to this specific indication.*

---

## Singapore Market Information

Meropenem currently has **no marketing authorization registered in Singapore** (`market_status: 未上市`, `total_licenses: 0`, no license records available in this evidence pack). No authorization number, product name, or locally approved indication text can be extracted at this time.

---

## Safety Considerations

Please refer to the package insert for safety information. *(All safety fields in this evidence pack — key warnings, contraindications, and drug-drug interaction data — are marked as data gaps; the DDI query returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Efficacy evidence for meropenem specifically in bacterial arthritis is indirect (observational bone/joint-infection cohorts, case reports, and pharmacokinetic studies) — there is no direct RCT, and the one "Phase 3" trial linked to this candidate actually tests a different drug for a different purpose.
- A **Blocking**-severity data gap (DG001: missing TFDA/HSA label warnings and contraindications) means the candidate cannot yet enter the S1 safety pre-screen at all, independent of efficacy evidence quality.
- Meropenem is not currently registered in Singapore, so there is no local regulatory or safety-label basis to build on.

**To proceed, the following is needed:**
- Official product-label safety data (warnings, contraindications, DDI) — required to clear the S1 safety pre-screen (DG001, Blocking).
- Mechanism-of-action documentation from DrugBank or equivalent source (DG002, High).
- A study or review directly evaluating meropenem's clinical efficacy in bacterial/septic arthritis (as opposed to adjacent conditions such as melioidosis or prosthetic joint infection).
- Confirmation of whether Singapore registration is planned, since no local license currently exists.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

