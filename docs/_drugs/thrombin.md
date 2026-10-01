---
layout: default
title: Thrombin
parent: Low Evidence (L5)
nav_order: 974
evidence_level: L5
indication_count: 10
---

# Thrombin
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

# Thrombin: From Topical Hemostasis (Fibrin Sealant Component) to Primary Release Disorder of Platelets

## One-Sentence Summary

Thrombin is the clot-forming enzyme in fibrin sealant products. The registration data do not state an original indication, but the Singapore products are all fibrin sealants for local bleeding control.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but this rests on mechanistic literature only. Of the 20 publications retrieved, none tests thrombin as a treatment for this condition. Of the many trials retrieved, only one involves a thrombin-containing product, and it addresses surgical bleeding rather than platelet disorders.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (registered products are fibrin sealants for topical hemostasis) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 96.82% |
| Evidence Level | L4 (preclinical and mechanism studies only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the Evidence Pack. From general knowledge, thrombin converts fibrinogen to fibrin and is also a strong physiological platelet agonist. In Singapore it is registered only as a component of fibrin sealants applied locally to stop bleeding.

Platelet release disorders are defects inside the platelet, in the secretion of granule contents. The retrieved literature is largely about how thrombin activates platelets, such as arachidonic acid release and calcium signalling, or about platelet function disorders in general. This link is mechanistic, not therapeutic. Externally applied thrombin cannot correct an intrinsic platelet defect.

The high TxGNN score most likely reflects how close thrombin sits to platelet biology in the knowledge graph, not therapeutic potential. A local hemostatic role during procedures is conceivable but unproven.

## Clinical Trial Evidence

No retrieved trial tests thrombin for this indication. The table lists the most relevant of those retrieved; the rest are unrelated.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01957852](https://clinicaltrials.gov/study/NCT01957852) | N/A | Completed | 86 | FloSeal (gelatin-thrombin matrix) to reduce intra-abdominal bleeding after cytoreductive surgery and HIPEC. It involves a thrombin product but addresses surgical bleeding, not a platelet disorder. |
| [NCT00043940](https://clinicaltrials.gov/study/NCT00043940) | Phase 3 | Completed | 50 | Bivalirudin (a direct thrombin inhibitor) for PCI in heparin-induced thrombocytopenia. Different drug and disease. |
| [NCT01178333](https://clinicaltrials.gov/study/NCT01178333) | N/A | Completed | 668 | Retrospective analysis of heparin-induced thrombocytopenia incidence and outcomes. No thrombin intervention. |
| [NCT06565364](https://clinicaltrials.gov/study/NCT06565364) | N/A | Completed | 160 | Protamine/heparin antibodies with platelet-activating properties in cardiac surgery. Observational. |
| [NCT03603769](https://clinicaltrials.gov/study/NCT03603769) | N/A | Completed | 6 | Salmon polar lipids and platelet aggregation. Unrelated to thrombin therapy. |

## Literature Evidence

No RCTs were found. The publications are reviews and in vitro studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1321709](https://pubmed.ncbi.nlm.nih.gov/1321709/) | 1992 | Review | Dis Mon | Overview of platelet function disorders. Platelets provide the surface where thrombin is generated. |
| [984037](https://pubmed.ncbi.nlm.nih.gov/984037/) | 1976 | In vitro | Am J Hematol | Thrombin activates phospholipases and releases arachidonic acid in human platelets, leading to aggregation and release of arachidonic acid metabolites. |
| [2016486](https://pubmed.ncbi.nlm.nih.gov/2016486/) | 1991 | Review | J Am Coll Cardiol | Role of platelets and thrombin in restenosis after coronary angioplasty. |
| [30986390](https://pubmed.ncbi.nlm.nih.gov/30986390/) | 2019 | Guideline/Review | Gastroenterology | AGA update on coagulation in cirrhosis, including use of pro-coagulants. |
| [33749992](https://pubmed.ncbi.nlm.nih.gov/33749992/) | 2021 | Review | Wound Repair Regen | Platelet gels activated with thrombin or calcium for wound healing. |
| [35226963](https://pubmed.ncbi.nlm.nih.gov/35226963/) | 2022 | Review | Hamostaseologie | Routine genetic analysis of hereditary bleeding, thrombotic and platelet disorders. |
| [26584277](https://pubmed.ncbi.nlm.nih.gov/26584277/) | 2015 | Preclinical | Cell Physiol Biochem | Thrombin and collagen-related peptide rapidly upregulate Orai1 in the platelet membrane. |
| [22841202](https://pubmed.ncbi.nlm.nih.gov/22841202/) | 2012 | Review | Transplant Proc | Coagulopathy management in liver transplantation. |

## Singapore Market Information

The registry does not state an approved indication for any of these products.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN14707P | TISSEEL Fibrin Sealant VH S/D (Frozen) | Solution |
| SIN16776P | Beriplast P Combi-Set 3 mL Powders and Solvents for Sealant | Other |
| SIN16775P | Beriplast P Combi-Set 1 mL Powders and Solvents for Sealant | Other |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by mechanistic literature. Platelet release defects are intrinsic to the platelet, so exogenous thrombin would not be expected to correct them, and no thrombin-specific clinical evidence exists for this indication.

For context, the same Evidence Pack shows stronger support for **esophageal disease** (endoscopic thrombin injection for bleeding gastric varices, supported by a systematic review/meta-analysis and EUS-guided cohort studies; rated L3, Proceed with Guardrails). It was not the top-ranked prediction, and its evidence concerns gastric varices, not esophageal disease broadly.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (this is a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Any thrombin-specific clinical data for platelet function disorders, or a decision to re-focus on the gastric varices indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

