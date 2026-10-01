---
layout: default
title: Gentamicin
parent: Medium Evidence (L3-L4)
nav_order: 472
evidence_level: L4
indication_count: 10
---

# Gentamicin
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

# Gentamicin: From Bacterial Infections to Rheumatoid Arthritis

## One-Sentence Summary

Gentamicin is an aminoglycoside antibacterial used to treat bacterial infections.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but the supporting evidence is weak: **1 clinical trial** (which does not test RA efficacy) and **20 publications** (all about infections in RA patients, not treatment of RA itself).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (the Singapore licence records contain no approved-indication text; this is based on gentamicin's known drug class) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 97.76% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, gentamicin is an aminoglycoside antibacterial that inhibits the bacterial 30S ribosome. Its efficacy in bacterial infections is well established.

The high TxGNN score is hard to justify mechanistically. The literature links gentamicin to RA only through infections that occur in RA patients, such as prosthetic joint infection, septic arthritis and bacteraemia, or through antibiotic-loaded bone cement. That is infection management in an RA population, not treatment of RA itself. The score most likely reflects knowledge-graph co-occurrence rather than a real disease-modifying effect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00872066](https://clinicaltrials.gov/study/NCT00872066) | Phase 4 | Completed | 243 | Single-centre post-market surveillance of two bone cements (SmartSet® HV and GHV) in total hip arthroplasty. It does not test RA efficacy and has no comparator. Relevance grade: C. |

---

## Literature Evidence

No randomised controlled trials were found. All of the 20 retrieved publications are case reports, reviews, infection-related clinical studies or preclinical work. The 10 most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14649677](https://pubmed.ncbi.nlm.nih.gov/14649677/) | 2003 | Clinical study | J Chin Med Assoc | Systemic antibiotics plus antibiotic-impregnated cement to prevent deep infection in 60 primary knee replacements in RA patients |
| [11233881](https://pubmed.ncbi.nlm.nih.gov/11233881/) | 2001 | Cohort/monitoring | Dtsch Med Wochenschr | Microbiological and immunological monitoring in polyarticular RA after joint replacement |
| [41221316](https://pubmed.ncbi.nlm.nih.gov/41221316/) | 2025 | Review | Acta Ortop Bras | Risk factors, prevention and treatment of infections after total hip arthroplasty |
| [4579913](https://pubmed.ncbi.nlm.nih.gov/4579913/) | 1973 | Case report | JAMA | Medical eradication of Serratia arthritis in an RA patient |
| [832090](https://pubmed.ncbi.nlm.nih.gov/832090/) | 1977 | Not classified | Br Med J | Septic arthritis in rheumatoid disease |
| [7019786](https://pubmed.ncbi.nlm.nih.gov/7019786/) | 1981 | Not classified | N Z Med J | Acute tubular necrosis in an RA patient treated with gentamicin and cefoxitin |
| [32751547](https://pubmed.ncbi.nlm.nih.gov/32751547/) | 2020 | Preclinical (rat) | Pharmaceutics | Tofacitinib elimination is slower in gentamicin-induced acute renal failure rats |
| [33812255](https://pubmed.ncbi.nlm.nih.gov/33812255/) | 2021 | Preclinical (mouse) | Int Immunopharmacol | Daphnetin, a coumarin used for RA, reduces gentamicin-induced kidney injury |
| [33827581](https://pubmed.ncbi.nlm.nih.gov/33827581/) | 2021 | Case report | Ann Clin Microbiol Antimicrob | Helicobacter canis bacteraemia in an RA patient on tofacitinib |
| [36074653](https://pubmed.ncbi.nlm.nih.gov/36074653/) | 2023 | Not classified | Ocul Immunol Inflamm | Acinetobacter-associated orbital cellulitis in an RA patient |

---

## Singapore Market Information

The Singapore records list no approved-indication text, so that column is omitted. Five of the 20 registrations are shown.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN01544P | Gentamicin Sulfate Cream 1 mg/g | Cream |
| SIN10243P | HOE Gentamicin Cream 0.1% w/w | Cream |
| SIN01849P | Miramycin Injection 80 mg/2 ml | Injection |
| SIN01848P | Miramycin Injection 280 mg/2 ml | Injection |
| SIN05260P | Gentamicin Injection BP 80 mg/2 ml | Injection |

---

## Safety Considerations

Package insert warnings, contraindications and drug-interaction data are not available. Please refer to the package insert for safety information.

The evidence review does flag gentamicin's nephrotoxicity and ototoxicity as concerns for any chronic-use scenario. This is especially relevant because RA patients often take other renally cleared or nephrotoxic drugs.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence concerns infections in RA patients and antibiotic-loaded cement, not treatment of RA itself. There is no plausible disease-modifying mechanism, and the score most likely reflects knowledge-graph co-occurrence. Long-term use carries a nephrotoxicity and ototoxicity risk. The other top-10 predictions (for example diabetic nephropathy, sclerosing cholangitis and several rare syndromes) also show no credible therapeutic support.

**To proceed, the following is needed:**
- Mechanism of action data (from DrugBank)
- Singapore package insert warnings and contraindications (from the HSA website), which are required before any safety screening
- Any direct evidence of gentamicin efficacy in RA (for example preclinical or controlled clinical data), rather than infection-related studies
- A clear reason to prefer gentamicin over established RA therapies, together with a nephrotoxicity and ototoxicity risk assessment

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

