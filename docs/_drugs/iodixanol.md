---
layout: default
title: Iodixanol
parent: Low Evidence (L5)
nav_order: 542
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Iodixanol: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not available"
monitor_inn: "Iodixanol"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "hemoglobinopathy", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "pseudoachondroplasia"]
---

# Iodixanol
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

# Iodixanol: From Radiographic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iodixanol is an iodinated, iso-osmolar radiographic contrast agent, marketed in Singapore as Visipaque injection.
The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility** (and to osteoarthritis itself), but **no clinical trials** and **no therapeutic publications** support this. The 5 osteoarthritis-related publications describe iodixanol only as an imaging tool.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the registered indication text is blank in the Singapore licences; the drug is a radiographic contrast agent) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iodixanol is an iodinated, iso-osmolar contrast agent that attenuates X-rays to enhance imaging. It has no known pharmacological action on the genetic susceptibility to osteoarthritis.

The high TxGNN score is a graph-based prediction only. For osteoarthritis (rank 2, score 99.07%), the retrieved publications cover contrast-enhanced CT of cartilage, solute diffusion across the osteochondral interface, and compatibility with platelet-rich plasma. They show that iodixanol is used to *visualise* cartilage, not to treat disease. The link most likely reflects co-occurrence of the drug and the disease in the imaging literature.

The other top predictions (rheumatoid arthritis, hemoglobinopathy, brachyolmia, Hunter-Thompson acromesomelic dysplasia, pseudoachondroplasia and other rare skeletal syndromes) have no plausible mechanism and no clinical evidence. Their scores likely reflect proximity to cartilage and skeletal disorders in the knowledge graph.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature exists for the top-ranked prediction (osteoarthritis susceptibility). The table below lists publications for the related prediction, osteoarthritis. None of them demonstrates a therapeutic effect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Imaging/diagnostic method study | Annals of Biomedical Engineering | CT and finite element study of nanoparticle diffusion to reveal cartilage function |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Computational modelling | Journal of Biomechanics | Finite element model of neutral solute transport across the osteochondral interface |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Experimental transport study | Journal of Biomechanics | Iodixanol used as a CT contrast agent to study permeability of the cartilage and subchondral bone interface |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro study | Journal of Experimental Orthopaedics | Iodine contrast agents did not affect platelet-rich plasma function at an early time point |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Imaging/diagnostic method study | Annals of Biomedical Engineering | Dual-contrast agent in photon-counting CT for assessing articular cartilage health |

For rheumatoid arthritis, the only publication ([36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/), 2022, Cureus) is a case report of desensitisation to a different contrast agent (iohexol). It is not evidence for iodixanol.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08883P | VISIPAQUE INJECTION 320 mgI/ml | Injection | Not stated in the licence data |
| SIN08882P | VISIPAQUE INJECTION 270 mgI/ml | Injection | Not stated in the licence data |

Both are valid single-ingredient licences. The manufacturers are GE Healthcare Ireland Limited, GE Healthcare AS and GE Healthcare (Shanghai) Co., Ltd.

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs. Most of the listed ones are Major-level, mainly with:
  - Metformin
  - Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
  - Aminosalicylates: mesalazine, balsalazide, olsalazine, sulfasalazine
  - Nephrotoxic antibiotics: vancomycin, kanamycin, neomycin, streptomycin, polymyxin B
- Mannitol is rated Moderate.
- Famotidine, acetylsalicylic acid, morphine, omeprazole and prednisone are of unknown severity.
- **Disease-specific note**: For hemoglobinopathy, iodinated contrast agents are used with caution in sickle cell disease. Any safety concerns would need separate consideration.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on graph-based scores alone (Evidence Level L5). There are no clinical trials, and the publications describe iodixanol as an imaging agent, not a treatment. A contrast agent has no known mechanism to modify osteoarthritis susceptibility or the other predicted conditions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore Health Sciences Authority (HSA), which are currently missing and block safety screening
- Mechanism of action data, for example from DrugBank
- Any preclinical or clinical evidence of a therapeutic effect (not imaging use) in osteoarthritis
- Registered indication text for the Singapore licences
- A route and formulation compatibility assessment (for example, intra-articular use versus the current intravascular injection)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

