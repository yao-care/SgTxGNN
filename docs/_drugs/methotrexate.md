---
layout: default
title: Methotrexate
parent: Low Evidence (L5)
nav_order: 651
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: From Its Established Uses to Pulmonary Blastoma

## One-Sentence Summary

Methotrexate is an antifolate chemotherapy and immunosuppressive drug that is marketed in Singapore in tablet and injection forms.
The TxGNN model predicts it may be effective for **pulmonary blastoma** with a very high score (99.45%), but **0 clinical trials** and **0 publications** support this prediction, so it is an unsupported model output.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the HSA licence data supplied |
| Predicted New Indication | Pulmonary blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the input. Based on general pharmacology, methotrexate is an antifolate that inhibits dihydrofolate reductase and blocks nucleotide synthesis in rapidly dividing cells. This gives it a broad antineoplastic rationale and is why it is used across many cancers.

Pulmonary blastoma is a rare lung tumour. The only link to methotrexate is this generic antiproliferative mechanism. No study, case series or trial was retrieved that tests methotrexate in this disease.

The very high TxGNN score therefore reflects proximity in the knowledge graph rather than clinical support. It should be treated as a hypothesis only.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16395P | Methotrexate Orion Tablets 2.5 mg | Tablet | Orion Corporation, Orion Pharma |
| SIN00260P | Methotrexate Tablet 2.5 mg | Tablet | Excella GmbH & Co. KG |
| SIN16737P | Merex 2.5 (Methotrexate Tablets USP 2.5 mg) | Tablet | Intas Pharmaceuticals Limited |
| SIN00758P | DBL Methotrexate Injection BP 50 mg/2 ml (without preservative) | Injection | Hospira Australia Pty Ltd |
| SIN12414P | Emthexate 2.5 Tablet 2.5 mg | Tablet | Teva Czech Industries s.r.o. |

Approved indication text is not provided in these records. Both oral (tablet, including film-coated) and injectable forms are registered.

## Cytotoxicity

This section is based on the drug class, because the input contains no toxicity data.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, antifolate) |
| Myelosuppression Risk | High (especially at high doses) |
| Emetogenicity Classification | Low to moderate, dose-dependent |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, respiratory symptoms |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for full details.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the input.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or literature support methotrexate in pulmonary blastoma, so the 99.45% score rests on model prediction alone (L5). Methotrexate is widely marketed in Singapore, but this specific prediction has no clinical support.

**To proceed, the following is needed:**
- A targeted search for pulmonary blastoma case series or trials involving methotrexate-containing regimens
- The HSA package insert (warnings, contraindications, approved indications), which is currently missing and blocks safety screening
- Detailed mechanism-of-action data from DrugBank
- A route-compatibility assessment (pending)
- **Consider other candidates from the same run, which have stronger evidence:**
  - Rhabdomyosarcoma: L2, including a phase II high-dose methotrexate trial (PMID 9329466)
  - Small cell lung carcinoma and Hodgkin lymphoma: L3, but historical, combination-regimen data only
  - Primary pulmonary lymphoma: L4, indirect evidence
  - The two CLL/SLL predictions have identical scores and should be treated as one prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

