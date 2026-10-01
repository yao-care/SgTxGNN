---
layout: default
title: Ampicillin
parent: Medium Evidence (L3-L4)
nav_order: 97
evidence_level: L4
indication_count: 10
---

# Ampicillin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Ampicillin: From Bacterial Infections (Indication Not Stated in HSA Records) to Laryngitis

## One-Sentence Summary

Ampicillin is a beta-lactam antibiotic marketed in Singapore as injectable powder, alone (Standacillin) and with sulbactam (Unasyn). The TxGNN model predicts it may be effective for **laryngitis**, but only **1 loosely related clinical trial** and **20 publications** were retrieved. None of them tests ampicillin for laryngitis directly, so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA licence records provided (approved indication text is blank) |
| Predicted New Indication | Laryngitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Ampicillin is a beta-lactam that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. It would therefore be expected to work only where laryngeal or epiglottic infection is bacterial and the organism is susceptible.

The link to laryngitis is plausible for bacterial infections such as epiglottitis, laryngeal abscess or laryngeal actinomycosis. The retrieved literature is mostly case reports and small reviews on these conditions. However, most laryngitis is viral and does not respond to antibiotics. The very high TxGNN score reflects graph proximity, not proven clinical benefit. The one related trial studies a different drug (amoxicillin/clavulanate).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01406275](https://clinicaltrials.gov/study/NCT01406275) | N/A (post-marketing surveillance) | Completed | 363 | Japanese pediatric surveillance of amoxicillin/clavulanate (CLAVAMOX) dry syrup across infections including laryngitis. It is a different drug, and no efficacy results are reported in the record. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | Review | CoDAS | Assessed the quality of clinical guidelines for laryngitis and pharyngitis using AGREE II. It is background only, with no ampicillin data. |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Case report | Ann Otol Rhinol Laryngol | Spontaneous laryngeal abscess in a patient with uncontrolled diabetes, with a review of modern cases. Laryngeal abscesses are rare in the antibiotic era. |
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Review | Anaesth Intensive Care | 161 children with acute epiglottitis, with complications in 34 and 5 deaths. It focuses on airway management, not antibiotic efficacy. |
| [5314768](https://pubmed.ncbi.nlm.nih.gov/5314768/) | 1971 | Review | Br Med J | Epiglottitis in adults, with no abstract available. |
| [12402494](https://pubmed.ncbi.nlm.nih.gov/12402494/) | 2002 | Case report | Acta Otorrinolaringol Esp | Two cases of paraglottic laryngeal abscess with a literature review. It stresses the need for prompt diagnosis. |
| [24930374](https://pubmed.ncbi.nlm.nih.gov/24930374/) | 2014 | Case report | J Voice | Laryngeal actinomycosis in a neutropenic patient, resolved after a prolonged penicillin course. |
| [30579693](https://pubmed.ncbi.nlm.nih.gov/30579693/) | 2019 | Case report | Auris Nasus Larynx | Laryngeal actinomycosis after bone marrow transplantation in a 14-year-old. |
| [6465636](https://pubmed.ncbi.nlm.nih.gov/6465636/) | 1984 | Case report | Ann Emerg Med | Three adults with epiglottitis. Diagnosis is often missed and airway obstruction can occur. |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | Observational | Otolaryngol Head Neck Surg | Perioperative antibiotic choice was associated with laryngectomy complications. It is not laryngitis-specific. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN00680P | Standacillin for Injection 0.5 g/vial | Injection, powder, for solution | Sandoz GmbH |
| SIN01949P | Unasyn 3000 for Injection | Injection, powder, for solution | Haupt Pharma Latina S.r.L |
| SIN01948P | Unasyn 1500 for Injection | Injection, powder, for solution | Haupt Pharma Latina S.r.L |
| SIN01950P | Unasyn 750 for Injection | Injection, powder, for solution | Haupt Pharma Latina S.r.L |

The approved indication text is blank in the records provided. All registered forms are injectable.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no trial or publication tests ampicillin for laryngitis. Most laryngitis is viral, and the only related trial involves a different drug. Evidence is limited to L4, meaning mechanistic plausibility for bacterial subtypes only.

**To proceed, the following is needed:**
- HSA package insert (approved indications, warnings, contraindications), which is currently missing
- Mechanism of action data from DrugBank
- Ampicillin-specific clinical data for bacterial laryngeal infections (epiglottitis, laryngeal abscess), separated from viral laryngitis
- Local resistance data (beta-lactamase producers) to judge whether plain ampicillin is still appropriate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

