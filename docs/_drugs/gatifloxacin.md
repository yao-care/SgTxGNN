---
layout: default
title: Gatifloxacin
parent: Low Evidence (L5)
nav_order: 470
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Gatifloxacin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Bacterial pneumonia, staphylococcal infections…"
monitor_inn: "Gatifloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "septicemic plague", "hematopoietic and lymphoid system neoplasm"]
---

# Gatifloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Gatifloxacin: From Bacterial Pneumonia to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Gatifloxacin is a fluoroquinolone antibacterial, originally used for bacterial infections such as pneumonia and conjunctivitis.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
The high score appears to be a computational artifact, and a more biologically plausible alternative among the other predictions is **septicemic plague**, supported by one preclinical animal study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, staphylococcal infections, streptococcal pneumonia, conjunctivitis and related infections (the Singapore license record contains no approved indication text) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 97.59% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, gatifloxacin is a fluoroquinolone antibacterial that inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy against bacterial infections is established, but this mechanism does not apply to polyclonal hyperviscosity syndrome.

Polyclonal hyperviscosity arises from elevated immunoglobulins or plasma proteins. Gatifloxacin has no known activity on these processes. The high TxGNN score (0.976) appears to be a graph-based artifact with no supporting trials or literature, so the prediction is **not considered mechanistically reasonable**.

**Other top predictions** were reviewed as well:

- **Septicemic plague (rank 9, score 93.27%)** is the only prediction with a credible link. The causative organism, *Yersinia pestis*, is susceptible to fluoroquinolones. A mouse study found gatifloxacin gave full protection for up to 6 hours after systemic challenge and up to 30 hours after aerosol challenge. Evidence is preclinical only (L4). Other fluoroquinolones such as levofloxacin, ciprofloxacin and moxifloxacin are better-supported options, particularly because systemic gatifloxacin was withdrawn in some markets due to dysglycaemia.
- **Hyperamylasaemia, congenital analbuminaemia, blood group incompatibility, premalignant haematological disease, monoclonal gammopathy, congenital haematological disorders and haematopoietic/lymphoid neoplasm** (ranks 2–6, 8 and 10) have no plausible mechanism and no clinical evidence.
- **Haematological disease associated with acquired peripheral neuropathy (rank 7)** raises a safety concern, because peripheral neuropathy is a known class adverse effect of fluoroquinolones.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top predicted indication (polyclonal hyperviscosity syndrome). For the alternative prediction, septicemic plague, one preclinical study was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15555886](https://pubmed.ncbi.nlm.nih.gov/15555886/) | 2004 | Preclinical (animal study) | International Journal of Antimicrobial Agents | In a mouse model of systemic and pneumonic plague, gatifloxacin and moxifloxacin were compared with ciprofloxacin (100 mg/kg orally, twice daily for 7 days). All gave full protection for up to 6 h after systemic challenge and up to 30 h after aerosol challenge. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12612P | ZYMAR OPHTHALMIC SOLUTION 0.3% (Allergan Sales LLC) | Solution | Not stated in the registration record |

Gatifloxacin is registered in Singapore only as an ophthalmic (eye) solution. Any systemic indication, such as plague, would therefore need a different route of administration.

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs. Many are rated **Major**, and the examples listed below are from the first 20 entries reviewed:
  - **Antidiabetic agents (Major)**: acarbose, albiglutide, alogliptin, metformin, pioglitazone, canagliflozin and chlorpropamide. This is consistent with the known dysglycaemia risk of gatifloxacin.
  - **Corticosteroids (Major)**: hydrocortisone, dexamethasone, betamethasone and triamcinolone.
  - **Other Major**: bupropion.
  - **Moderate**: famotidine, loperamide, acetylsalicylic acid, balsalazide, bisacodyl, calcium phosphate, calcium acetate and potassium citrate.
- **Class-related concern**: Peripheral neuropathy is a known fluoroquinolone adverse effect, which is relevant to rank 7 (haematological disease associated with acquired peripheral neuropathy).

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, polyclonal hyperviscosity syndrome, has no clinical trials, no literature and no plausible mechanism. The score is likely a network-proximity artifact (Evidence Level L5). The only credible alternative, septicemic plague, has preclinical evidence only and is better served by other fluoroquinolones.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For septicemic plague as a research question: human or comparative efficacy data, and a review of route of administration, since the Singapore license covers only an ophthalmic solution
- Review of the dysglycaemia risk and the major interactions with antidiabetic drugs before any systemic use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

