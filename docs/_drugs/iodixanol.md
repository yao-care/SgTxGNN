---
layout: default
title: Iodixanol
parent: Low Evidence (L5)
nav_order: 541
evidence_level: L5
indication_count: 2
monitor_inn: "Iodixanol"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis"]
last_modified_at: 2026-10-23
description: "Iodixanol: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not stated in the Singapore licence records"
---

# Iodixanol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Iodixanol: From Radiographic Contrast Imaging to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Iodixanol is an iodinated, non-ionic radiographic contrast agent used to enhance X-ray and CT imaging, and the Singapore licence records for it carry no approved-indication text.
The TxGNN model predicts it may be effective for **osteoarthritis**, but there are **no clinical trials** and only **5 publications**, all of which use iodixanol as an imaging or diffusion probe rather than as a treatment.
This prediction is a computational signal only and is not supported by therapeutic evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (radiographic contrast agent) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9907 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Number of Approvals | 2 (both single-ingredient licences) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iodixanol is an iodinated, non-ionic, iso-osmolar contrast agent. It has no known disease-modifying pharmacology, since it works by absorbing X-rays and so makes tissues visible on imaging.

The link to osteoarthritis appears to be an artifact. The retrieved publications use iodixanol to image articular cartilage and subchondral bone (contrast-enhanced CT and solute-transport modelling), and one checks its compatibility with platelet-rich plasma in vitro. None of these studies shows a therapeutic effect on osteoarthritis. The high TxGNN score most likely reflects co-occurrence of the drug and joint tissue in imaging research, not a repurposing signal.

A second prediction, rheumatoid arthritis (score 0.9900), is similarly unsupported. Its only publication is a case report on desensitization to a different contrast agent (iohexol).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below studies iodixanol as a treatment for osteoarthritis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Preclinical imaging study | Ann Biomed Eng | Dual-contrast agent (nanoparticle plus molecular) with photon-counting CT to assess articular cartilage health |
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Imaging methodology | Ann Biomed Eng | Nanoparticle diffusion CT combined with finite element modelling to reveal cartilage function |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Ex vivo transport study | J Biomech | Iodixanol (~1550 Da) used as a neutral CT contrast agent to study permeability of the cartilage–subchondral bone interface |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Computational modelling | J Biomech | Finite element model of neutral solute transport across the osteochondral interface |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro study | J Exp Orthop | Iodine contrast agents did not affect platelet-rich plasma function at an early time point |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08883P | VISIPAQUE INJECTION 320 mgI/ml | Injection | Not stated in the licence record |
| SIN08882P | VISIPAQUE INJECTION 270 mgI/ml | Injection | Not stated in the licence record |

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records; the first 20 returned are summarised here.
  - **Major**: metformin, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), mesalazine, balsalazide, olsalazine, sulfasalazine, vancomycin, kanamycin, neomycin, streptomycin and polymyxin B.
  - **Moderate**: mannitol.
  - **Unknown severity**: famotidine, acetylsalicylic acid, morphine, omeprazole and prednisone.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No clinical trial exists, and the publications use iodixanol as an imaging probe rather than a therapy, so there is no direct evidence of benefit in osteoarthritis (Evidence Level L5). Iodixanol also has no known therapeutic mechanism in joint disease.

**To proceed, the following is needed:**
- Mechanism-of-action data and a plausible biological rationale for a therapeutic effect in osteoarthritis
- Preclinical studies showing disease-modifying activity, not just imaging or diffusion behaviour
- The Singapore package insert warnings and contraindications, which are not yet available for safety screening
- A review of the route and dose, since the current products are intravascular injections and not intended as joint therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

