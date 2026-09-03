---
layout: default
title: Ribociclib
parent: 僅模型預測 (L5)
nav_order: 855
evidence_level: L5
indication_count: 10
---

# Ribociclib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ribociclib: From HR+/HER2- Advanced Breast Cancer to Myeloid Leukemia

## One-Sentence Summary

> Ribociclib is a CDK4/6 inhibitor originally developed and approved for hormone receptor-positive (HR+), HER2-negative advanced breast cancer.
> The TxGNN model's top-ranked prediction suggests possible activity in **myeloid leukemia**,
> but this direction is supported only by **0 clinical trials** and **3 publications**, one of which reports ribociclib *causing* leukemia as an adverse event rather than treating it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HR+/HER2- advanced breast cancer (not formally recorded in Singapore regulatory data — drug is unregistered locally) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is currently a data gap. Based on the supporting literature retrieved, ribociclib is known to be a highly selective, orally administered **CDK4/6 inhibitor** that blocks cell-cycle progression by preventing phosphorylation of the retinoblastoma protein, thereby arresting proliferation of Rb-intact tumor cells. This mechanism is well established in its approved use for HR+/HER2- breast cancer (confirmed by the MONALEESA-2/3/7 and NATALEE Phase 3 trials, which also appear independently in this evidence pack at rank 7 — the model correctly re-identifying the drug's known, already-approved indication).

The proposed link to myeloid leukemia rests on a theoretical rationale (PMID 32560251) that CDK4/6 inhibition could help overcome pharmacokinetic drug resistance in AML cells in vitro. However, this is contradicted by direct clinical observation: PMID 30575100 describes a patient who **developed** acute myeloid leukemia with eosinophilia after CDK4/6 inhibitor treatment for breast cancer, i.e., the drug class is associated with *inducing* AML-related hematologic clonal evolution, not treating it. This is the opposite therapeutic direction from what the prediction implies, and is consistent with a broader pattern seen across this evidence pack: several other top-ranked TxGNN predictions for ribociclib (thrombocytopenia, heart neoplasm, multiple endocrine neoplasia) trace back to known **adverse-effect signals** (myelosuppression, QT prolongation/cardiotoxicity) or apparent knowledge-graph mismatches, rather than genuine repurposing opportunities.

Given this, the mechanistic plausibility for myeloid leukemia is weak and partially contradicted by the only human-subject evidence available.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32560251](https://pubmed.ncbi.nlm.nih.gov/32560251/) | 2020 | Preclinical/In vitro | Cancers | Proposes CDK4/6 inhibitors could help overcome ABCB1/ABCG2-mediated pharmacokinetic drug resistance in AML cells; in vitro rationale only, no ribociclib-specific AML efficacy data |
| [30575100](https://pubmed.ncbi.nlm.nih.gov/30575100/) | 2019 | Case Report (Adverse Event) | American Journal of Hematology | Reports AML with eosinophilia **arising after** CDK4/6 inhibitor treatment in a patient with underlying clonal hematopoiesis — an adverse drug reaction, not a therapeutic response |
| [41641105](https://pubmed.ncbi.nlm.nih.gov/41641105/) | 2026 | Case Report | Frontiers in Oncology | Describes a dual-primary vulvar/breast adenocarcinoma case; does not involve ribociclib treatment or myeloid leukemia — appears unrelated to this indication and is likely a knowledge-graph/evidence-matching artifact |

---

## Singapore Market Information

Ribociclib is currently **not registered** in Singapore (market status: 未上市／Not Marketed; total licenses: 0). No local product license or approved indication text is available.

---

## Cytotoxicity

Ribociclib's original indication (breast cancer) and drug class (CDK4/6 inhibitor) meet the criteria for inclusion of this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor; not a conventional cytotoxic agent) |
| Myelosuppression Risk | High — neutropenia, leukopenia, and thrombocytopenia are the most common dose-limiting toxicities across the class (documented in multiple pharmacovigilance and meta-analysis publications retrieved above, e.g. PMID 38753541, 29147869, 33233970) |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | CBC with differential (baseline and periodic, particularly first 2 cycles), liver function tests (transaminase elevation reported), ECG/QTc interval (class-associated QT prolongation risk) |
| Handling Protection | Oral targeted agent; institutional hazardous-drug handling precautions are generally still advised given cytotoxic/antineoplastic classification |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The myeloid leukemia prediction has no supporting clinical trials and is backed only by a preclinical rationale paper plus a case report describing the drug class *causing* AML rather than treating it — the mechanistic direction is contradicted rather than confirmed by available human evidence. Combined with the absence of Singapore market registration and missing MOA/safety label data, this candidate does not currently meet the threshold to advance.

**To proceed, the following is needed:**
- Confirmed DrugBank MOA data and official package insert warnings/contraindications (currently blocking Data Gaps)
- Resolution of the conflicting signal on AML: mechanistic studies or a prospective trial specifically testing CDK4/6 inhibition as AML therapy (not merely reporting AML as an adverse event)
- Re-evaluation of other TxGNN-ranked candidates in this pack (thrombocytopenia, heart neoplasm, multiple endocrine neoplasia), which on review reflect known adverse-effect associations or likely knowledge-graph mismatches rather than genuine repurposing signals, before further investment in evidence collection for those directions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

