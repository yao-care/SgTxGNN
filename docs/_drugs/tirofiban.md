---
layout: default
title: Tirofiban
parent: Medium Evidence (L3-L4)
nav_order: 995
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Tirofiban: predicted new indication Primary release disorder of platelets (evidence level L4). Approved use: Acute coronary syndrome"
monitor_inn: "Tirofiban"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "rheumatoid arthritis", "trigeminal autonomic cephalalgia", "headache disorder", "pseudo-von Willebrand disease", "congenital prothrombin deficiency", "thromboangiitis obliterans", "female breast carcinoma", "cholecystolithiasis"]
---

# Tirofiban
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

# Tirofiban: From Acute Coronary Syndrome to Primary Release Disorder of Platelets

## One-Sentence Summary

Tirofiban is an injectable antiplatelet drug originally used for acute coronary syndrome.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are **0 registered clinical trials** and only **3 publications**, none showing a therapeutic benefit for this condition.
The prediction rests on model output alone, and the mechanism argues against benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 96.27% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tirofiban is a glycoprotein IIb/IIIa (integrin αIIbβ3) antagonist. It blocks the final common pathway of platelet aggregation, which is why it is used in acute coronary syndrome and percutaneous coronary intervention (PCI).

In primary release disorders of platelets, granule secretion is already impaired. Further blocking aggregation would add little benefit and would raise bleeding risk. The retrieved literature covers tirofiban in ACS/PCI (antiplatelet regimens, troponin release) and tirofiban-induced thrombocytopenia, not treatment of this disorder. The high TxGNN score most likely reflects network proximity to platelet pathways rather than a real therapeutic rationale.

The second-ranked prediction, Glanzmann thrombasthenia, shows the same pattern. The disease is caused by a defect in the very target tirofiban inhibits, so the drug would reproduce the disease rather than treat it. The remaining top-10 predictions (rheumatoid arthritis, trigeminal autonomic cephalalgia, headache disorder, pseudo-von Willebrand disease, congenital prothrombin deficiency, thromboangiitis obliterans, female breast carcinoma, cholecystolithiasis) have little or no supporting evidence and are also rated Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16682384](https://pubmed.ncbi.nlm.nih.gov/16682384/) | 2006 | Clinical study | European Heart Journal | ELISA-2: dual vs. triple antiplatelet pre-treatment in non-ST-elevation ACS before early catheterization. Concerns ACS, not release disorders. |
| [16287613](https://pubmed.ncbi.nlm.nih.gov/16287613/) | 2005 | Case series / lab study | Platelets | Tirofiban-induced thrombocytopenia is caused by drug-dependent antibodies against GPIIb/IIIa. This is a safety finding. |
| [12204495](https://pubmed.ncbi.nlm.nih.gov/12204495/) | 2002 | Clinical study | J Am Coll Cardiol | TOPSTAR: effect of adding GPIIb/IIIa inhibition on troponin T release after elective PCI. |

None of these studies tests tirofiban as a treatment for primary release disorder of platelets.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10931P | AGGRASTAT CONCENTRATE FOR INFUSION 0.25 mg/ml | Injection | Not listed in the registration data |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: thrombocytopenia, blood coagulation disease, stroke disorder, cerebrovascular disorder, cerebral infarction, injury, brain cancer, brain neoplasm, intracranial hemorrhage, arteriovenous hemangioma/malformation. These are consistent with the bleeding risk of GPIIb/IIIa blockade and are particularly relevant to platelet and coagulation disorders.
- **Drug Interactions**: 100 interactions were found. Examples with a **Major** level include abciximab, deferasirox, acalabrutinib, ibritumomab tiuxetan, tositumomab, and trastuzumab emtansine. **Moderate** examples include acetylsalicylic acid, ketorolac, ibuprofen, fenfluramine, dexfenfluramine, and sibutramine. Several others, such as pantoprazole, omeprazole, morphine, metformin, simvastatin, and ranitidine, have an unclassified level.
- **Literature safety signal**: tirofiban-associated thrombocytopenia caused by drug-dependent antibodies has been reported, with a higher incidence of myocardial infarction and mortality in affected patients.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no clinical trials and no literature showing benefit. The mechanism (further aggregation blockade in a bleeding-type disorder) points toward harm rather than benefit, and the knowledge graph flags several related bleeding and platelet conditions as contraindications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (from the HSA website)
- Detailed mechanism of action data (from DrugBank)
- A targeted literature review showing a credible therapeutic rationale for primary release disorder of platelets
- A review of the other top-ranked predictions, and consideration of redirecting the analysis to indications with a plausible mechanism, such as thromboangiitis obliterans
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

