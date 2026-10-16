---
layout: default
title: Pegaspargase
parent: High Evidence (L1-L2)
nav_order: 768
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Pegaspargase: predicted new indication Precursor lymphoblastic lymphoma/leukaemia (evidence level L1). Approved use: Acute lymphoblastic leukaemia"
monitor_inn: "Pegaspargase"
predicted_indications: ["precursor lymphoblastic lymphoma/leukemia", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "follicular lymphoma", "acute lymphoblastic leukemia", "methylcobalamin deficiency type cblE", "lymphoid neoplasm", "Hodgkins lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma", "blast phase chronic myelogenous leukemia, BCR-ABL1 positive"]
---

# Pegaspargase
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Pegaspargase: From Acute Lymphoblastic Leukaemia to Precursor Lymphoblastic Lymphoma/Leukaemia

## One-Sentence Summary

Pegaspargase is a PEGylated form of the enzyme L-asparaginase, originally used to treat acute lymphoblastic leukaemia (ALL).
The TxGNN model predicts it may be effective for **precursor lymphoblastic lymphoma/leukaemia**, a disease that is essentially the same family as its approved use.
This direction is supported by **35 clinical trials** and **20 publications** in the compiled data, although almost all of them test pegaspargase as one component of multi-drug regimens rather than on its own.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukaemia (the Singapore licence record contains no indication text) |
| Predicted New Indication | Precursor lymphoblastic lymphoma/leukaemia |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known information, pegaspargase is a PEGylated L-asparaginase that depletes circulating asparagine. Lymphoblasts have low asparagine synthetase expression and depend on asparagine from the blood, so depletion leads to selective death of leukaemic cells. PEGylation prolongs circulation time, so dosing is less frequent, and it may reduce immune reactions compared with native E. coli L-asparaginase.

The predicted indication is not a true repurposing case. Precursor lymphoblastic lymphoma/leukaemia largely overlaps with the approved ALL use, and lymphoblastic lymphoma is commonly treated with the same ALL-type regimens. Pegaspargase is already a core component of standard paediatric and adult ALL regimens. The prediction is therefore mechanistically consistent, but it mainly confirms an existing use.

Other predicted diseases in the model output are much weaker. Several (the chronic lymphocytic leukaemia subtypes, follicular lymphoma, methylcobalamin deficiency cblE, and chronic lymphocytic leukaemia/small lymphocytic lymphoma) have no trials or literature and look like artefacts of the model's graph propagation. Extranodal NK/T-cell lymphoma has some supporting literature, but it appears under other predicted terms rather than this one.

## Clinical Trial Evidence

The table lists the most relevant trials. Most test pegaspargase as part of a combination regimen, so they support the regimen rather than the single drug.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00905034](https://clinicaltrials.gov/study/NCT00905034) | Phase 2 | Completed | 37 | MOAD regimen (methotrexate, vincristine, pegylated asparaginase, dexamethasone) in salvage ALL |
| [NCT00967057](https://clinicaltrials.gov/study/NCT00967057) | Phase 3 | Completed | 470 | ALLR3 international trial in relapsed/refractory ALL; regimen includes pegylated asparaginase |
| [NCT00103285](https://clinicaltrials.gov/study/NCT00103285) | Phase 3 | Completed | 5377 | Combination chemotherapy regimens in standard-risk B-precursor ALL; pegaspargase is part of the backbone |
| [NCT02003222](https://clinicaltrials.gov/study/NCT02003222) | Phase 3 | Active, not recruiting | 488 | Blinatumomab plus chemotherapy in newly diagnosed B-ALL; pegaspargase is in the backbone, not the tested variable |
| [NCT03643276](https://clinicaltrials.gov/study/NCT03643276) | Phase 3 | Recruiting | 5000 | AIEOP-BFM ALL 2017 protocol for children and adolescents with ALL |
| [NCT05602194](https://clinicaltrials.gov/study/NCT05602194) | Phase 3 | Active, not recruiting | 440 | Levocarnitine to prevent asparaginase-associated liver toxicity (a safety, not efficacy, study) |
| [NCT00890656](https://clinicaltrials.gov/study/NCT00890656) | Phase 2 | Completed | 90 | Augmented hyper-CVAD salvage regimen in ALL or lymphoblastic lymphoma |
| [NCT01005914](https://clinicaltrials.gov/study/NCT01005914) | Phase 2 | Terminated | 11 | Adding PEG-asparaginase to hyper-CVAD in newly diagnosed adult ALL |
| [NCT02396043](https://clinicaltrials.gov/study/NCT02396043) | Phase 2 | Unknown | 50 | Modified BFM-95 regimen in adult T-lymphoblastic lymphoma |
| [NCT01451515](https://clinicaltrials.gov/study/NCT01451515) | Phase 2 | Completed | 23 | Risk-adapted ALL-based therapy for newly diagnosed acute lymphoblastic lymphoma |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | RCT | J Clin Oncol | COG AALL1231: bortezomib in newly diagnosed T-ALL and T-lymphoblastic lymphoma |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | RCT | J Clin Oncol | COG AALL0434: nelarabine in newly diagnosed T-ALL |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | RCT | J Clin Oncol | COG AALL0232: dexamethasone and high-dose methotrexate improve outcomes in high-risk B-ALL |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohort | Blood Adv | GIMEMA LAL1913: pegaspargase added to a risk-oriented adult ALL programme |
| [31030380](https://pubmed.ncbi.nlm.nih.gov/31030380/) | 2019 | Review | Drugs | Review of pegaspargase in ALL; longer circulation time than native asparaginase |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Review | Haematologica | Expert consensus on recognising and managing asparaginase adverse events in adults with ALL |
| [40858769](https://pubmed.ncbi.nlm.nih.gov/40858769/) | 2025 | Cohort | Ann Hematol | Pegaspargase tolerability in patients aged 55 or older treated with LAL1913 |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Study | J Clin Oncol | DFCI 11-001: efficacy and toxicity of pegaspargase versus calaspargase pegol in childhood ALL |
| [14499708](https://pubmed.ncbi.nlm.nih.gov/14499708/) | 2003 | Review | Adv Drug Deliv Rev | Review of clinical studies of pegaspargase |
| [27643446](https://pubmed.ncbi.nlm.nih.gov/27643446/) | 2017 | Review | Leuk Lymphoma | Hypersensitivity with intravenous versus intramuscular pegaspargase |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16408P | ONCASPAR POWDER FOR SOLUTION FOR INJECTION/INFUSION 750 U/ML | Injection, powder, lyophilised, for solution | Not stated in the licence record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Enzyme-based antineoplastic (asparagine-depleting agent), used within multi-agent chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (it is usually combined with myelosuppressive agents) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function, pancreatic enzymes, triglycerides and glucose, coagulation parameters, signs of hypersensitivity and thrombosis |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for safety information.

**Drug Interactions**: The interaction screen returned 100 records, and the 20 reviewed were all of Moderate level. They include:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
- Glucose-lowering drugs: metformin, acarbose, alogliptin, canagliflozin, dapagliflozin, saxagliptin, albiglutide, dulaglutide, chlorpropamide
- Antibiotics: doxycycline, tetracycline, clarithromycin
- Others: acetylsalicylic acid, bupropion, chenodeoxycholic acid

**Toxicities reported in the literature**: hepatotoxicity, pancreatitis, thrombosis, hypertriglyceridaemia, hyperglycaemia and hypersensitivity reactions. The risk appears higher in older adults and obese patients. Dose capping and levocarnitine have been studied as ways to reduce it.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pegaspargase is already an established component of multi-agent ALL regimens, and the predicted indication largely overlaps with its approved use. Several large Phase 3 trials include it in the backbone, but few isolate its effect, and its toxicity requires careful management.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator (currently missing, and a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Confirmation of the approved indication wording on the Singapore licence
- A toxicity monitoring plan, especially for adults over 40 or 55, obese patients and patients on corticosteroids or glucose-lowering drugs
- Separate, direct evidence before considering other predicted diseases (for example extranodal NK/T-cell lymphoma); the remaining predictions without evidence should stay on hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

