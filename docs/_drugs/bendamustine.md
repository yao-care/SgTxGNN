---
layout: default
title: Bendamustine
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Bendamustine
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

# Bendamustine: From CLL / Indolent B-cell NHL to Mantle Cell Lymphoma

## One-Sentence Summary

Bendamustine is a bifunctional alkylating agent with established global approval for chronic lymphocytic leukemia (CLL) and rituximab-refractory indolent B-cell non-Hodgkin lymphoma (NHL), though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Mantle Cell Lymphoma (MCL)**,
with **more than 30 clinical trials** and **20 publications** supporting this direction — including multiple completed Phase 3 RCTs in which the BR (bendamustine + rituximab) regimen serves as either the standard treatment backbone or active comparator.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | CLL; rituximab-refractory indolent B-cell NHL (globally approved; not registered in Singapore) |
| Predicted New Indication | Mantle Cell Lymphoma (MCL) |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bendamustine is structurally unique among alkylating agents. Its molecule contains two distinct pharmacophores: a 2-chloroethylamine group that causes DNA double-strand breaks and inter/intra-strand cross-links — triggering PARP-mediated apoptosis — and a benzimidazole ring that confers purine analogue properties, further disrupting nucleic acid synthesis in actively dividing cells. This dual mechanism means Bendamustine can induce cell death through pathways that are distinct from conventional alkylators like cyclophosphamide, which explains its partial non-cross-resistance with other chemotherapy agents. (Detailed MOA data from DrugBank was not retrieved during this analysis; the description above is based on published literature.)

Mantle cell lymphoma is a mature B-cell malignancy defined by the chromosomal translocation t(11;14)(q13;q32), which drives cyclin D1 overexpression and uncontrolled cell-cycle entry. MCL cells are highly proliferative and heavily dependent on B-cell receptor signalling for survival, making them biologically sensitive to Bendamustine's combined DNA damage and antimetabolite effects. Given that both MCL and CLL are mature B-cell neoplasms sharing overlapping oncogenic signalling pathways, it is mechanistically logical that therapies active in CLL translate effectively to MCL — a pattern well-documented in haematological oncology.

The clinical evidence base strongly validates this prediction. The BR (bendamustine + rituximab) regimen has been evaluated in two pivotal Phase 3 trials specifically including MCL patients (StiL NHL1 and BRIGHT studies), where it demonstrated superior progression-free survival compared to R-CHOP with a more favourable tolerability profile. More recently, multiple large Phase 3 trials — including the SHINE trial (ibrutinib + BR, n = 523) and ongoing studies with acalabrutinib, zanubrutinib, and orelabrutinib — have adopted BR as the chemotherapy backbone, adding targeted agents on top rather than replacing Bendamustine. This pattern unequivocally confirms BR as the established standard of care in MCL.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01456351](https://clinicaltrials.gov/study/NCT01456351) | Phase 3 | Completed | 230 | Randomized multicentre trial comparing BR vs fludarabine + rituximab in relapsed/progressive low-grade NHL and MCL; directly establishes BR efficacy in MCL at the highest evidence level |
| [NCT00991211](https://clinicaltrials.gov/study/NCT00991211) | Phase 3 | Completed | 549 | StiL NHL1: first-line BR vs R-CHOP in low-grade NHL and MCL; BR demonstrated non-inferior efficacy with significantly longer PFS and improved tolerability — a landmark MCL trial |
| [NCT02972840](https://clinicaltrials.gov/study/NCT02972840) | Phase 3 | Active, not recruiting | 635 | Double-blind placebo-controlled RCT of acalabrutinib + BR vs BR alone in previously untreated MCL; BR is the foundational backbone, confirming its established status |
| [NCT04002297](https://clinicaltrials.gov/study/NCT04002297) | Phase 3 | Active, not recruiting | 510 | Zanubrutinib + rituximab vs BR in transplant-ineligible untreated MCL; validates BR as the current standard comparator for novel agent registration trials |
| [NCT06363994](https://clinicaltrials.gov/study/NCT06363994) | Phase 3 | Recruiting | 476 | Orelabrutinib + BR vs BR in treatment-naïve MCL; further large-scale validation of BR as the standard backbone in the BTKi combination era |
| [NCT06084936](https://clinicaltrials.gov/study/NCT06084936) | Phase 3 | Recruiting | 182 | Glofitamab monotherapy vs investigator's choice (BR or lenalidomide + rituximab) in relapsed/refractory MCL; BR remains a recognised standard option in late-line disease |
| [NCT01415752](https://clinicaltrials.gov/study/NCT01415752) | Phase 2 | Active, not recruiting | 373 | Four-arm intergroup RCT (RB ± bortezomib, then R or lenalidomide maintenance) in ≥60-year-old untreated MCL; largest Phase 2 MCL study with BR as induction backbone |
| [NCT01457144](https://clinicaltrials.gov/study/NCT01457144) | Phase 2 | Completed | 76 | RiBVD regimen (rituximab + bortezomib + bendamustine + dexamethasone) as first-line treatment for MCL in patients >65 years or those ineligible for autograft; demonstrates bendamustine-based combination therapy in elderly MCL |
| [NCT06854003](https://clinicaltrials.gov/study/NCT06854003) | Phase 2 | Recruiting | 60 | BRAZAN study: bendamustine + rituximab + cytarabine + zanubrutinib induction, followed by zanubrutinib/rituximab ± sonrotoclax maintenance in treatment-naïve MCL |
| [NCT01437709](https://clinicaltrials.gov/study/NCT01437709) | Phase 2 | Completed | 30 | Ofatumumab ± bendamustine in MCL patients ineligible for autologous stem cell transplant; directly addresses the unmet need in transplant-ineligible MCL using bendamustine as the chemotherapy partner |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35657079](https://pubmed.ncbi.nlm.nih.gov/35657079/) | 2022 | Phase 3 RCT | N Engl J Med | SHINE trial: ibrutinib + BR significantly prolonged PFS vs BR alone in older untreated MCL (median 80.6 vs 52.9 months); definitively establishes BR as the standard chemotherapy platform |
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | Phase 3 RCT | J Clin Oncol | Acalabrutinib + BR vs BR in untreated MCL; acalabrutinib arm demonstrated superior PFS with a potentially improved tolerability profile compared to ibrutinib-BR |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | Phase 3 RCT | Lancet | ENRICH trial: ibrutinib + rituximab vs standard immunochemotherapy (R-CHOP or BR) in ≥60-year-old untreated MCL; BR confirmed as a guideline-standard comparator arm |
| [23433739](https://pubmed.ncbi.nlm.nih.gov/23433739/) | 2013 | Phase 3 RCT | Lancet | BR vs R-CHOP as first-line treatment for indolent NHL and MCL: BR non-inferior with significantly longer PFS (69.5 vs 31.2 months) and fewer adverse events; landmark trial establishing BR as a preferred first-line option |
| [30811293](https://pubmed.ncbi.nlm.nih.gov/30811293/) | 2019 | Phase 3 RCT (5-yr follow-up) | J Clin Oncol | BRIGHT 5-year follow-up: sustained PFS and OS benefit of BR over R-CHOP/R-CVP confirmed in treatment-naïve indolent NHL and MCL |
| [24591201](https://pubmed.ncbi.nlm.nih.gov/24591201/) | 2014 | Phase 3 RCT | Blood | BRIGHT study primary analysis: BR non-inferior to R-CHOP/R-CVP in treatment-naïve indolent NHL/MCL, with equivalent overall response rates |
| [32985902](https://pubmed.ncbi.nlm.nih.gov/32985902/) | 2021 | Phase 3 RCT (protocol) | Future Oncol | Phase 3 trial design of zanubrutinib + rituximab vs BR in transplant-ineligible untreated MCL; describes statistical rationale and BR as the gold-standard comparator |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Cohort study | Blood Adv | Pooled analysis of two Phase 2 trials and an off-trial cohort using RB/RC (rituximab-bendamustine/rituximab-high-dose cytarabine) induction for transplant-eligible MCL: high complete response rates and favourable mobilisation outcomes pre-ASCT |
| [36456154](https://pubmed.ncbi.nlm.nih.gov/36456154/) | 2022 | Retrospective cohort | Anticancer Res | Korean multicentre retrospective analysis of BR in treatment-naïve and relapsed/refractory MCL; demonstrates real-world effectiveness and tolerability in an East Asian patient population |
| [26755518](https://pubmed.ncbi.nlm.nih.gov/26755518/) | 2016 | Review | J Clin Oncol | Comprehensive MCL review: establishes BR + maintenance rituximab as standard for older/transplant-ineligible patients and high-dose cytarabine + ASCT for younger patients; key reference for current treatment paradigm |

---

## Singapore Market Information

Bendamustine (DrugBank ID: DB06769) has **no current HSA product licences** in Singapore. There are 0 approved registrations on record. Clinicians seeking to use this drug would need to apply via the Special Access Route (SAR) for unregistered therapeutic products, or identify a licensed parallel import channel. This access gap represents a practical barrier to adoption and should be factored into any implementation plan.

---

## Cytotoxicity

Bendamustine meets the criteria for antineoplastic/cytotoxic classification: it is a bifunctional alkylating agent with direct DNA-damaging activity, and its original indication is for haematological malignancies (CLL, indolent NHL).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — bifunctional alkylating agent with purine analogue properties (nitrogen mustard + benzimidazole hybrid structure) |
| Myelosuppression Risk | High — neutropenia and thrombocytopenia are the primary dose-limiting toxicities; Grade 3/4 neutropenia reported in 30–50% of patients across major trials; prolonged T-lymphocyte depletion is a distinctive feature compared to other alkylators |
| Emetogenicity Classification | Low to moderate (generally lower emetogenic risk than CHOP-based regimens; HEC prophylaxis not routinely required) |
| Monitoring Items | Complete blood count with differential (before each cycle and as clinically indicated during treatment); liver function tests; renal function and electrolytes; signs of active infection (especially opportunistic infections); CMV monitoring in high-risk patients; consider PCP and antiviral prophylaxis given deep lymphopenia |
| Handling Protection | Must be prepared and administered according to cytotoxic drug handling regulations — closed-system drug transfer devices (CSTDs) recommended during compounding; appropriate PPE (double gloves, protective gown, eye/face protection) required; disposal per cytotoxic waste protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings, contraindications, and drug–drug interaction data were not available in this evidence pack. These represent blocking data gaps that must be resolved prior to clinical use. Sources: FDA label, EMA SmPC, or TFDA prescribing information for bendamustine hydrochloride.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The BR regimen is backed by L1 evidence — including at least two completed Phase 3 RCTs (StiL NHL1 and the BRIGHT programme) specifically enrolling MCL patients — and has been adopted as the standard chemotherapy backbone in five or more additional ongoing Phase 3 trials. The mechanistic rationale is robust, and the global clinical community has clearly validated Bendamustine's role in MCL. The primary barriers to adoption in Singapore are regulatory (no HSA registration) and operational (safety data gap), not evidential.

**To proceed, the following is needed:**

- **Regulatory access**: Apply for HSA Special Access Route (SAR) or identify a licensed importer; this is a prerequisite for any clinical use in Singapore
- **Safety data retrieval**: Download and review the FDA label / EMA SmPC for Bendamustine to extract key warnings, contraindications, and major drug interactions (particularly with CYP1A2 inhibitors and immunosuppressants) — currently a blocking data gap
- **MOA documentation**: Query DrugBank API for the complete mechanism-of-action profile (DB06769) to support the pharmacological rationale section
- **Local protocol development**: Define BR dosing regimen, anti-infective prophylaxis protocol (PCP prophylaxis, herpes zoster prophylaxis), and haematological monitoring schedule aligned with institutional standards
- **Patient selection criteria**: Stratify MCL candidates by MIPI score, TP53 mutation status, Ki-67 index, and transplant eligibility to identify which patients would benefit most from a BR-based approach vs. newer BTKi-based regimens
- **Preferred pathway — clinical trial enrolment**: Consider enrolling eligible patients in active Phase 3 trials (e.g., NCT02972840 acalabrutinib + BR, NCT06363994 orelabrutinib + BR) as the most evidence-generating access route
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

