---
layout: default
title: Mercaptopurine
parent: 僅模型預測 (L5)
nav_order: 645
evidence_level: L5
indication_count: 10
---

# Mercaptopurine
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

# Mercaptopurine: From Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Mercaptopurine (6-MP) is a classic purine-analog antimetabolite whose established clinical role, per the literature evidence in this pack, is treatment of acute lymphoblastic leukemia (and, off-label, inflammatory bowel disease). The TxGNN model's top-ranked prediction is that it is also effective for **Myeloid Leukemia** (AML/APL), with **29 clinical trials** and **20 publications** currently identified as supporting evidence — though, as detailed below, much of this evidence reflects 6-MP's already-established role as a maintenance-therapy component rather than a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Lymphoblastic Leukemia (per literature evidence in this pack; Singapore license text unavailable — drug is not currently registered here) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available for this candidate (data gap DG002). However, the evidence pack's own literature base documents 6-MP's mechanism consistently: it is a purine analog that, after metabolic activation to thioguanine nucleotides, is incorporated into DNA/RNA and inhibits de novo purine synthesis, producing an antiproliferative and cytotoxic effect on rapidly dividing cells (PMID 35654820). This mechanism is lineage-agnostic — it targets high-turnover hematopoietic blasts regardless of whether they are lymphoid or myeloid in origin.

Acute lymphoblastic leukemia (the drug's classical indication) and myeloid leukemia (the top predicted indication) are both hematologic malignancies driven by rapidly proliferating blast populations, which gives the TxGNN prediction reasonable mechanistic plausibility. In fact, the clinical trial evidence shows that 6-MP is *already* a component of numerous acute myeloid leukemia (AML) and acute promyelocytic leukemia (APL) treatment protocols — most notably as part of ATRA + methotrexate + 6-MP maintenance regimens in APL (e.g., PETHEMA, AIDA-based studies).

This raises an important caveat for interpretation: several of the trials and publications supporting this "prediction" describe 6-MP's long-standing, already-established use in myeloid leukemia maintenance therapy rather than a novel repurposing signal. Modern AML/APL treatment has also shifted substantially toward targeted agents (e.g., FLT3/IDH inhibitors), hypomethylating agents, and arsenic trioxide-based regimens, with 6-MP's role now largely confined to maintenance phases in specific subtypes (particularly APL) rather than frontline induction therapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00136084](https://clinicaltrials.gov/study/NCT00136084) | Phase 3 | Completed | 238 | Compared two multi-agent chemotherapy regimens with different cytarabine dosages in newly diagnosed AML/myelodysplasia. |
| [NCT00962767](https://clinicaltrials.gov/study/NCT00962767) | Phase 3 | Completed | 168 | Compared gemtuzumab ozogamicin dosing vs. 2-year ATRA + chemotherapy maintenance in intermediate/high-risk APL. |
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Phase 4 | Completed | 300 | PETHEMA LPA2005: ATRA + idarubicin induction, risk-adapted consolidation, and maintenance with ATRA + low-dose methotrexate/mercaptopurine. |
| [NCT00002701](https://clinicaltrials.gov/study/NCT00002701) | Phase 3 | Unknown | 750 | Randomized ATRA + idarubicin induction/consolidation ± bone marrow transplant, with MRD-guided maintenance in APL. |
| [NCT02688140](https://clinicaltrials.gov/study/NCT02688140) | Phase 3 | Completed | 135 | Arsenic trioxide + ATRA + idarubicin vs. standard AIDA regimen in newly diagnosed high-risk APL. |
| [NCT00482833](https://clinicaltrials.gov/study/NCT00482833) | Phase 3 | Completed | 276 | Arsenic trioxide + ATRA vs. standard ATRA + anthracycline (AIDA) in non-high-risk APL. |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Completed | 420 | Tretinoin + chemotherapy ± arsenic trioxide induction; maintenance with intermittent tretinoin ± mercaptopurine/methotrexate in untreated APL. |
| [NCT00599937](https://clinicaltrials.gov/study/NCT00599937) | Phase 3 | Completed | 576 | Assessed optimal timing of chemotherapy relative to ATRA and the role of maintenance therapy in APL. |
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | Completed | 105 | S0521: maintenance therapy vs. observation in previously untreated low/intermediate-risk APL. |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | Recruiting | 10 | ApoAML trial: venetoclax + 6-mercaptopurine combination in relapsed/refractory AML. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | RCT | International Journal of Hematology | JALSG-AML92: adding etoposide to daunorubicin/cytarabine/6-MP induction showed no additional benefit in adult AML. |
| [31983177](https://pubmed.ncbi.nlm.nih.gov/31983177/) | 2020 | RCT | Asian Pacific Journal of Cancer Prevention | Multicenter open-label RCT comparing metronomic chemotherapy vs. palliative hydroxyurea in unfit AML patients. |
| [8558199](https://pubmed.ncbi.nlm.nih.gov/8558199/) | 1996 | RCT | Journal of Clinical Oncology | Randomized comparison of behenoyl cytarabine vs. cytarabine, ± ubenimex, in adult AML induction/consolidation. |
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohort | Journal of Korean Medical Science | Oral maintenance chemotherapy with 6-MP + methotrexate improved leukemia-free and overall survival in transplant-ineligible AML. |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | Cohort | Cancer Investigation | High-dose 6-MP + intermediate-dose cytarabine during first AML remission produced feasible responses in a pediatric pilot study. |
| [24492035](https://pubmed.ncbi.nlm.nih.gov/24492035/) | 2014 | Review | Rinsho Ketsueki (Japanese Journal of Clinical Hematology) | Overview of current therapy for AML and acute promyelocytic leukemia. |
| [28152123](https://pubmed.ncbi.nlm.nih.gov/28152123/) | 2017 | Cohort | JAMA Oncology | Association between autoimmune-disease therapy (including thiopurines) and subsequent MDS/AML. |
| [31658693](https://pubmed.ncbi.nlm.nih.gov/31658693/) | 2019 | Cohort | Cells | Metabolomic profiling of AML patients receiving ATRA + valproic acid disease-stabilizing treatment. |
| [1793832](https://pubmed.ncbi.nlm.nih.gov/1793832/) | 1991 | Cohort | International Journal of Hematology | Intensive induction with behenoyl cytarabine, daunorubicin, and 6-MP achieved 71% complete remission in adult AML. |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | RCT | Cancer Chemotherapy and Pharmacology | Nationwide randomized comparison of daunorubicin vs. aclarubicin combined with BH-AC/6-MP/prednisolone in untreated AML. |

---

## Singapore Market Information

Mercaptopurine is currently **not marketed** in Singapore under this evidence pack's regulatory data — there are 0 registered authorizations, and no license records are available to summarize product names, dosage forms, or approved indication text.

---

## Cytotoxicity

Mercaptopurine is a purine-analog antimetabolite historically used as an antileukemic chemotherapy agent (per literature evidence, e.g., PMID 37417972 describes it as "an antiproliferative purine analog used in acute lymphoblastic leukemia, non-Hodgkin lymphoma, and inflammatory bowel disease"), and its top-predicted new indication here is also a hematologic malignancy — meeting the criteria for antineoplastic/cytotoxic classification.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine/thiopurine antimetabolite) |
| Myelosuppression Risk | High — multiple pharmacogenomic studies in this pack (TPMT/NUDT15 polymorphism literature) document substantial risk of severe neutropenia/leukopenia, particularly in patients with reduced TPMT or NUDT15 enzyme activity |
| Emetogenicity Classification | Not directly evidenced in this pack; oral thiopurine antimetabolites are generally regarded as low-to-moderate emetogenic risk in oncology references — confirm against the package insert |
| Monitoring Items | CBC with differential (myelosuppression), liver function tests (hepatotoxicity/6-methylmercaptopurine-related), TPMT/NUDT15 genotype or enzyme activity, renal function, and blood glucose (rare hypoglycemia has been reported in this pack's literature) |
| Handling Protection | Yes — as a cytotoxic antimetabolite chemotherapy agent, standard hazardous/cytotoxic drug handling precautions apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials (APL maintenance regimens combining ATRA/methotrexate with mercaptopurine, and broader AML combination-chemotherapy studies) support the L1 evidence classification for this candidate. However, much of this evidence documents mercaptopurine's *already-established* role as a maintenance-therapy adjunct in myeloid leukemia (especially APL) rather than a genuinely novel indication, and contemporary AML treatment has increasingly moved toward targeted and hypomethylating-agent regimens — so the evidence supports guarded, not unconditional, progression.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications data (currently a Blocking data gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank (currently a High-severity data gap, DG002)
- A Singapore market registration/licensing pathway assessment, since the drug is not currently marketed here (0 registrations)
- A formal drug–drug interaction (DDI) profile, since the DDI query returned no results
- Clarification of which myeloid leukemia subtype and treatment phase (e.g., APL maintenance vs. de novo AML induction vs. relapsed/refractory) the indication would target, since the strongest evidence concentrates in APL maintenance rather than broad AML frontline use
- Note: this evidence pack also contains 9 additional predicted indications (ranks 2–10) with evidence levels ranging from L1 to L5. Two of these — precursor lymphoblastic lymphoma/leukemia (rank 9) and acute lymphoblastic leukemia (rank 10) — substantially overlap with mercaptopurine's already-known classical antileukemic use; these should be cross-checked against formal original-indication registry data to avoid double-counting "novel prediction" credit for already-established uses.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

