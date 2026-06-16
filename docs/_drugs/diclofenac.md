---
layout: default
title: Diclofenac
parent: 僅模型預測 (L5)
nav_order: 323
evidence_level: L5
indication_count: 10
---

# Diclofenac
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

# Diclofenac: From Pain and Inflammatory Conditions to Juvenile Idiopathic Arthritis

## One-Sentence Summary

Diclofenac is a well-established non-steroidal anti-inflammatory drug (NSAID) widely used for pain relief and inflammatory conditions including rheumatic diseases in adults.
The TxGNN model predicts it may be effective for **Juvenile Idiopathic Arthritis (JIA)**,
with **2 clinical trials** and **18 publications** currently supporting this direction.

> **Note:** This is a multi-indication Evidence Pack (TW-DB00586-multi) covering 10 predicted indications. Nine of these (ranks 1–8, 10) are classified as L5 evidence with a "Hold" recommendation due to absent mechanistic linkage and no supporting clinical data. This report focuses on **Juvenile Idiopathic Arthritis (rank 9)**, the sole indication with actionable evidence (L3) and a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain and inflammatory conditions (no local registrations available; based on known pharmacology) |
| Predicted New Indication | Juvenile Idiopathic Arthritis (JIA) |
| TxGNN Prediction Score | 99.25% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Diclofenac is a non-selective COX-1/COX-2 inhibitor. By blocking cyclooxygenase enzymes, it reduces prostaglandin E2 (PGE2) synthesis, thereby decreasing the release of inflammatory mediators from synovial tissue and alleviating joint swelling and pain. Although detailed mechanistic data from the local package insert was not retrieved in this Evidence Pack (DG002), Diclofenac's anti-inflammatory pathway is extensively documented across four decades of international literature.

Juvenile Idiopathic Arthritis (JIA) is defined by persistent synovial inflammation arising in children under 16 years of age. The pathological core—chronic synovitis driven by immune dysregulation—directly aligns with Diclofenac's mechanism of action. NSAIDs, including Diclofenac at approximately 2 mg/kg/day, have served as first-line symptomatic therapy in JIA since the late 1970s. Multiple published studies confirm effectiveness and tolerability in the paediatric population across polyarticular and seronegative subtypes of juvenile chronic arthritis.

Notably, the literature confirms that Diclofenac is already licensed in multiple jurisdictions for children over 1 year of age for the treatment of juvenile rheumatoid arthritis—making this TxGNN prediction not only biologically credible but also supported by international regulatory precedent. The model score of 99.25% reflects this strong mechanistic and clinical alignment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00688545](https://clinicaltrials.gov/study/NCT00688545) | N/A (Observational) | Terminated | 275 | SINCERE Registry: prospective, multi-centre safety study comparing NSAIDs (including Diclofenac) vs. celecoxib in JIA patients in real-world clinical practice. Terminated early, but captures meaningful safety signals for NSAID use in this paediatric population. |
| [NCT05871086](https://clinicaltrials.gov/study/NCT05871086) | Phase 2/3 | Unknown | 60 | Coenzyme Q10 supplementation in JIA patients; NSAIDs used as standard background therapy, providing contextual data on JIA disease burden and current management landscape. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [3052965](https://pubmed.ncbi.nlm.nih.gov/3052965/) | 1988 | Crossover RCT | Clinical and Experimental Rheumatology | Single-blind crossover study in 28 children with seronegative JCA: diclofenac 2 mg/kg/day vs. naproxen vs. tolmetin over 12 weeks; all three showed comparable clinical and laboratory improvement with similar tolerability. |
| [6361986](https://pubmed.ncbi.nlm.nih.gov/6361986/) | 1983 | Clinical Trial | Scandinavian Journal of Rheumatology | Pharmacokinetics and efficacy of diclofenac sodium in children aged 2–7 with JRA; established plasma level profiles and renal elimination parameters to guide paediatric dosing of 25 mg enteric-coated tablets. |
| [2235663](https://pubmed.ncbi.nlm.nih.gov/2235663/) | 1990 | Clinical Study | La Pediatria Medica e Chirurgica | Open non-comparative study in 26 patients aged 2–16 with polyarticular JCA; Diclofenac sodium confirmed effective anti-inflammatory and analgesic effects equivalent to adult outcomes. |
| [10756785](https://pubmed.ncbi.nlm.nih.gov/10756785/) | 1997 | Comparative Study | Revista Medico-Chirurgicala | 8-year comparative study of NSAIDs in 100 children with JCA; diclofenac group demonstrated sustained clinical response at 2, 4, and 6 months and up to 3 years of follow-up. |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Review | British Journal of Rheumatology | Comprehensive review of NSAID use in paediatric rheumatic diseases; diclofenac identified as equal in efficacy and tolerability to ibuprofen, naproxen, and tolmetin for JIA joint symptom control, with a superior profile to salicylates. |
| [1884567](https://pubmed.ncbi.nlm.nih.gov/1884567/) | 1991 | PK/PD Study | Clinical Pharmacokinetics | Pharmacokinetics of drugs used in juvenile arthritis including Diclofenac; provides comprehensive dosing guidance for the paediatric rheumatology population. |
| [11735667](https://pubmed.ncbi.nlm.nih.gov/11735667/) | 2001 | Comparative Review | Paediatric Drugs | Risks and benefits of NSAIDs vs. paracetamol in children; JIA cited as a key therapeutic indication with COX inhibition mechanism reviewed for the paediatric context. |
| [17474954](https://pubmed.ncbi.nlm.nih.gov/17474954/) | 2007 | Survey | Paediatric Anaesthesia | Survey of paediatric anaesthetists across Great Britain and Ireland; explicitly confirms that Diclofenac is currently licensed for children over 1 year of age for juvenile rheumatoid arthritis treatment in these jurisdictions. |
| [723822](https://pubmed.ncbi.nlm.nih.gov/723822/) | 1978 | Clinical Study | Minerva Pediatrica | One of the earliest clinical reports of sodium Diclofenac (Voltaren) in infantile rheumatoid arthritis; establishes historical basis for this paediatric indication. |
| [6761640](https://pubmed.ncbi.nlm.nih.gov/6761640/) | 1982 | Clinical Study | Pediatriia | Clinical evaluation of Voltaren (Diclofenac) in children with rheumatoid arthritis; early Eastern European clinical experience supporting the JIA indication. |

---

## Singapore Market Information

Diclofenac currently has **0 approved product registrations** in Singapore's Health Sciences Authority (HSA) registry and is **not marketed** in this jurisdiction.

> International reference labels (FDA, EMA, or TFDA) should be consulted for full prescribing information. Multiple international markets have approved Diclofenac for juvenile rheumatoid arthritis, which may serve as a regulatory anchor for a future Singapore submission.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Key warnings and contraindications data were unavailable in this Evidence Pack (DG001 — **Blocking**). This gap must be resolved before formal safety assessment can proceed. Given the absence of local registration, the FDA, EMA, or TFDA label should be retrieved and reviewed. Known class-level safety concerns for NSAIDs include gastrointestinal toxicity, cardiovascular risk (with long-term use), and renal impairment — all of which require particular attention in the paediatric JIA population on chronic therapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Diclofenac's COX-1/COX-2 inhibitory mechanism directly targets the synovial inflammation that defines JIA, and clinical evidence spanning over four decades confirms its use and tolerability in paediatric arthritis populations. The drug is already approved for juvenile rheumatoid arthritis in multiple international jurisdictions (UK, EU, several others), providing strong regulatory precedent — even though Singapore registration data is currently absent.

**To proceed, the following is needed:**
- Retrieve the full package insert from an international source (FDA, EMA, or TFDA) to complete key warnings and contraindications assessment — this is a **Blocking** data gap (DG001)
- Obtain complete MOA data via DrugBank API (DG002 — High priority) to strengthen mechanistic documentation
- Confirm age-appropriate formulation availability (e.g., dispersible tablet, oral suspension) for the JIA target population, particularly younger children
- Conduct an HSA registration gap analysis using existing international JIA approvals as the regulatory anchor for a potential Singapore submission
- Review current JIA treatment guidelines (ACR 2021, EULAR 2023) to position Diclofenac appropriately relative to modern biologics (TNF inhibitors, IL-6 inhibitors, JAK inhibitors), particularly for the initial symptomatic management phase
- Design a long-term safety monitoring plan addressing GI, cardiovascular, and renal parameters specific to the paediatric chronic use setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

