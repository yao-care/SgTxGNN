---
layout: default
title: Rituximab
parent: High Evidence (L1-L2)
nav_order: 868
evidence_level: L1
indication_count: 10
---

# Rituximab
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

# Rituximab: From an Unrecorded Original Indication to Follicular Lymphoma

## One-Sentence Summary

Rituximab is an anti-CD20 monoclonal antibody that is marketed in Singapore. The licence records supplied do not state its original approved indication.
The TxGNN model predicts it may be effective for **Follicular Lymphoma**, with **50 clinical trials** and **20 publications** retrieved for this direction.
Follicular lymphoma is a long-established use of rituximab, so the high score reflects known practice and is not a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied Singapore licence data |
| Predicted New Indication | Follicular lymphoma |
| TxGNN Prediction Score | 96.08% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Rituximab is an anti-CD20 monoclonal antibody. Follicular lymphoma cells are CD20-positive B cells, so the antibody can act through antibody-dependent cellular cytotoxicity (ADCC), complement-dependent cytotoxicity (CDC) and direct induction of apoptosis. The DrugBank mechanism field was not populated in the input, so this description comes from the evidence analysis rather than the drug record.

The input lists no original indications, so the relationship between the original and new indication cannot be shown from the data. Follicular lymphoma is nonetheless a well-established use of rituximab, supported by guidelines and reviews. The ESMO guideline and the long-term randomised trial of early rituximab monotherapy are in the literature table below. The high TxGNN score is consistent with that history and should not be read as a newly discovered use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01476787](https://clinicaltrials.gov/study/NCT01476787) | Phase 3 | Completed | 1030 | Rituximab + lenalidomide vs rituximab + chemotherapy in untreated follicular lymphoma. Rituximab is a core component. |
| [NCT01650701](https://clinicaltrials.gov/study/NCT01650701) | Phase 3 | Completed | 1030 | RELEVANCE trial. This is the companion registration of the same rituximab + lenalidomide vs rituximab + chemotherapy study. |
| [NCT01938001](https://clinicaltrials.gov/study/NCT01938001) | Phase 3 | Completed | 358 | Double-blind trial of rituximab + lenalidomide vs rituximab + placebo in relapsed/refractory follicular or marginal zone lymphoma. |
| [NCT01701232](https://clinicaltrials.gov/study/NCT01701232) | Phase 3 | Completed | 174 | Biosimilar BCD-020 vs MabThera monotherapy in indolent non-Hodgkin lymphoma. |
| [NCT00003204](https://clinicaltrials.gov/study/NCT00003204) | Phase 3 | Completed | 515 | Maintenance anti-CD20 antibody vs observation after induction in low-grade lymphoma. |
| [NCT00006721](https://clinicaltrials.gov/study/NCT00006721) | Phase 3 | Active, not recruiting | 571 | CHOP + rituximab vs CHOP + iodine-131 tositumomab in newly diagnosed follicular lymphoma. |
| [NCT06097364](https://clinicaltrials.gov/study/NCT06097364) | Phase 3 | Active, not recruiting | 733 | Odronextamab + chemotherapy vs rituximab + chemotherapy in untreated follicular lymphoma. Rituximab is the comparator, so the evidence is indirect. |
| [NCT05409066](https://clinicaltrials.gov/study/NCT05409066) | Phase 3 | Active, not recruiting | 549 | Epcoritamab + rituximab + lenalidomide vs rituximab + lenalidomide in relapsed/refractory follicular lymphoma. |
| [NCT04224493](https://clinicaltrials.gov/study/NCT04224493) | Phase 3 | Recruiting | 612 | Tazemetostat or placebo + lenalidomide + rituximab in relapsed/refractory follicular lymphoma. |
| [NCT00363636](https://clinicaltrials.gov/study/NCT00363636) | Phase 3 | Terminated | 340 | Galiximab + rituximab vs placebo + rituximab in relapsed/refractory follicular lymphoma. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40306831](https://pubmed.ncbi.nlm.nih.gov/40306831/) | 2025 | RCT (Phase 3, long-term follow-up) | Lancet Haematol | Early rituximab monotherapy vs watchful waiting in asymptomatic, low-tumour-burden advanced follicular lymphoma. The earlier report showed improved time to new treatment, and this report gives mature follow-up. |
| [33249059](https://pubmed.ncbi.nlm.nih.gov/33249059/) | 2021 | Guideline | Ann Oncol | ESMO Clinical Practice Guidelines for newly diagnosed and relapsed follicular lymphoma. |
| [36345167](https://pubmed.ncbi.nlm.nih.gov/36345167/) | 2022 | Meta-analysis | J Clin Pharm Ther | Efficacy and safety of rituximab biosimilars vs the reference product as first-line treatment in low-tumour-burden follicular lymphoma. |
| [39374535](https://pubmed.ncbi.nlm.nih.gov/39374535/) | 2024 | Molecular subtyping study | Blood | Follicular lymphoma has germinal centre-like and memory-like subtypes with prognostic significance. Samples came from the RELEVANCE trial (rituximab-chemotherapy or rituximab-lenalidomide). |
| [28628883](https://pubmed.ncbi.nlm.nih.gov/28628883/) | 2017 | Review | Cancer Treat Rev | Pros and cons of rituximab maintenance in follicular lymphoma. |
| [29120553](https://pubmed.ncbi.nlm.nih.gov/29120553/) | 2017 | Review | Acta Clin Croat | Rituximab maintenance in first- and second-line treatment of advanced follicular lymphoma, with improved progression-free survival. |
| [36255040](https://pubmed.ncbi.nlm.nih.gov/36255040/) | 2022 | Review | Am J Hematol | 2023 update on diagnosis and management of follicular lymphoma. |
| [31831752](https://pubmed.ncbi.nlm.nih.gov/31831752/) | 2019 | Review | Nat Rev Dis Primers | Overview of follicular lymphoma biology and disease features. |
| [12857561](https://pubmed.ncbi.nlm.nih.gov/12857561/) | 2003 | Review | Haematologica | Rituximab as primary treatment, treatment of relapsed disease, re-treatment and maintenance in follicular lymphoma. |
| [32683839](https://pubmed.ncbi.nlm.nih.gov/32683839/) | 2020 | Case report (adverse event) | Cancer Res Treat | Crohn's disease following rituximab induction and maintenance for follicular lymphoma. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15969P | Rixathon Concentrate for Solution for Infusion 500mg/50ml | Infusion, solution concentrate |
| SIN15970P | Rixathon Concentrate for Solution for Infusion 100mg/10ml | Infusion, solution concentrate |
| SIN09946P | MabThera Concentrate for Solution for Infusion 500mg/50ml | Injection |
| SIN15671P | Truxima Concentrate for Solution for Infusion 10mg/ml | Infusion, solution concentrate |
| SIN16452P | Ruxience Concentrate for Solution for Infusion 500mg/50ml | Infusion, solution concentrate |

Of the 8 registrations, 5 are shown here. Approved-indication text is empty in the supplied licence records, so it is not listed.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted immunotherapy (anti-CD20 monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

The literature includes one case report of Crohn's disease after rituximab induction and maintenance for follicular lymphoma (PMID 32683839). This is a single-case signal.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 3 trials (RELEVANCE and its companion registration, a double-blind rituximab + lenalidomide trial, and a biosimilar trial), together with guidelines and a long-term randomised trial, support rituximab in follicular lymphoma. Follicular lymphoma is an established use, so this should not be treated as a new repurposing finding until the local label is confirmed.

Of the other predicted indications, only "neoplasm of mature B-cells" reached L1/Proceed with Guardrails, on paediatric Phase 3 evidence. The CLL/SLL subtype, Burkitt lymphoma and MALT lymphoma sites are at "Research Question", based on case-level or mechanistic evidence. "Metastatic neoplasm", pregerminal-centre CLL/SLL and malignant spiradenoma are at "Hold". Malignant spiradenoma is likely a false-positive graph artefact.

**To proceed, the following is needed:**
- The Singapore package insert and approved-indication text for each of the 8 registrations, to confirm whether follicular lymphoma is already a labelled indication. Warnings and contraindications are also missing from the input.
- Detailed mechanism of action data from DrugBank, which was not populated in the input.
- A safety monitoring plan, including haematological parameters and infusion-reaction management.
- Confirmation of approved routes (intravenous infusion or subcutaneous) for any new use. Route compatibility is still pending.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

