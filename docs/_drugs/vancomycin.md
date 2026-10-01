---
layout: default
title: Vancomycin
parent: Low Evidence (L5)
nav_order: 1045
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomycin: From Antibacterial Therapy to Diffuse Scleroderma

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic used against Gram-positive bacterial infections. The TxGNN model predicts it may be effective for **diffuse scleroderma**, but there are **0 clinical trials** and only **1 unrelated case report** supporting this, and the proposed mechanism does not hold up. This prediction is most likely a knowledge-graph artifact and should not be pursued.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Vancomycin is known to inhibit cell-wall synthesis in Gram-positive bacteria, which is the basis of its use against serious Gram-positive infections.

Diffuse scleroderma is an autoimmune, fibrotic disease. There is no plausible link between blocking bacterial cell-wall synthesis and the immune and fibrotic processes that drive it. The very high TxGNN score is most likely an artifact of the knowledge graph rather than a real pharmacological signal. **On current evidence, this prediction is not reasonable.**

Among the other top-10 predictions, only **streptococcal pneumonia** (rank 9, evidence level L4) is biologically plausible. *S. pneumoniae* is Gram-positive and vancomycin is used against penicillin-resistant strains. This is probably an existing use missing from the drug record rather than true repurposing. The other predictions are either contradicted by mechanism (paratyphoid fever, salmonellosis and typhoid fever, because Gram-negative *Salmonella* is intrinsically resistant to vancomycin) or have no rationale and no evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case report | The American Journal of Case Reports | A 56-year-old man with a diffuse exfoliative rash, sepsis and eosinophilia, evaluated as possible erythroderma. It is not a study of scleroderma, and it provides no evidence of vancomycin benefit. |

## Singapore Market Information

Ten registrations exist; five are listed below. Approved indication text is not recorded for any of them. Dosage forms cover both injectable and oral (capsule) routes.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN08069P | Vancomycin HCl Injection 500 mg/vial | Powder for solution for injection | BCWorld Pharm. Co., Ltd |
| SIN15417P | Vancosala Powder for Solution for Injection or Infusion 500 mg per vial | Lyophilized powder for solution for injection | Laboratorio Reig Jofre, SA |
| SIN16445P | Vancover Capsules 250 mg | Capsule | Orient Pharma Co., Ltd. |
| SIN16444P | Vancover Capsules 125 mg | Capsule | Orient Pharma Co., Ltd. |
| SIN15070P | Vancomycin Kabi Powder for Concentrate for Solution for Infusion 500 mg | Lyophilized powder for solution for infusion | Xellia Pharmaceuticals ApS |

## Safety Considerations

- **Known adverse effects of intravenous vancomycin** (from the summary of trial NCT05395520): nephrotoxicity, ototoxicity and hypersensitivity reactions.

No drug-interaction records were found. For warnings and contraindications, please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Diffuse scleroderma has no clinical trials, no supporting literature and no plausible mechanism, so the high TxGNN score appears to be a knowledge-graph artifact. The evidence level is L5.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications, since the safety data are currently missing
- Original indication and mechanism of action data for vancomycin in the drug record
- Re-evaluation of **streptococcal pneumonia** (rank 9) as an existing-use confirmation rather than a repurposing case, since it is the only plausible candidate in the top 10
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

