---
layout: default
title: Fludarabine
parent: 僅模型預測 (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
---

# Fludarabine
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

# Fludarabine: From B-cell Malignancies to Plasma Cell Myeloma

## One-Sentence Summary

Fludarabine is a purine analogue nucleoside antimetabolite established in the treatment of chronic lymphocytic leukaemia (CLL) and indolent B-cell lymphoid malignancies.
The TxGNN model predicts it may be effective for **Plasma Cell Myeloma** (multiple myeloma),
with **50 clinical trials** and **20 publications** currently supporting this direction — primarily through its role as the immunosuppressive backbone of allogeneic stem cell transplant conditioning and as standard lymphodepletion before CAR-T cell therapy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | CLL and indolent B-cell malignancies (established clinical use; no Singapore HSA registration found) |
| Predicted New Indication | Plasma Cell Myeloma (Multiple Myeloma) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the current evidence pack. Based on known pharmacology, fludarabine is a fluorinated purine nucleoside analogue that is phosphorylated intracellularly to its active triphosphate form (F-ara-ATP). This metabolite competitively inhibits DNA polymerase alpha, ribonucleotide reductase, and DNA primase, thereby blocking DNA synthesis and triggering apoptosis in proliferating lymphoid cells. Its selectivity for lymphoid lineages reflects preferential intracellular accumulation due to high deoxycytidine kinase activity in these cell types.

Plasma cell myeloma and the B-cell malignancies for which fludarabine is established both arise from B-lymphocyte lineage precursors. Plasma cells are terminally differentiated B-cells, and fludarabine's documented cytotoxicity against B-cell populations provides a direct mechanistic rationale for anti-myeloma activity. A key preclinical study (PMID 17976186) confirmed that fludarabine directly inhibits the myeloma cell line RPMI8226 both in vitro and in xenograft mouse models, demonstrating suppression of Akt phosphorylation — a survival pathway frequently dysregulated in myeloma.

Clinically, fludarabine operates in multiple myeloma through two distinct pathways. First, as a core component of reduced-intensity conditioning (RIC) regimens (Flu+Mel, Flu+Bu, Flu+Treosulfan) before allogeneic haematopoietic stem cell transplantation (allo-HSCT), it provides immunosuppression sufficient to facilitate engraftment without the full toxicity of myeloablative conditioning — enabling a graft-versus-myeloma (GvM) effect in patients ineligible for conventional transplant. Second, fludarabine/cyclophosphamide has become the standard lymphodepletion platform before BCMA-targeted CAR-T cell therapies, where it enhances T-cell expansion and persistence. Both roles place fludarabine at the centre of several active and completed Phase 1–3 trials specifically enrolling myeloma patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03303950](https://clinicaltrials.gov/study/NCT03303950) | Phase 2 | Terminated | 6 | Busulfan + **Fludarabine** + post-transplant cyclophosphamide followed by donor SCT for MM and myelofibrosis; Fludarabine is a primary study drug; terminated due to recruitment challenges, not safety concerns |
| [NCT00781170](https://clinicaltrials.gov/study/NCT00781170) | Phase 2 | Completed | 20 | Melphalan/**Fludarabine**-based dose-reduced allograft after autologous HSCT for Stage II/III MM; evaluates tandem auto-allo approach to induce graft-versus-myeloma effect |
| [NCT01163357](https://clinicaltrials.gov/study/NCT01163357) | Phase 1 | Completed | 18 | Bortezomib ± total marrow irradiation (TMI) + **Fludarabine** + Melphalan as allo-HSCT conditioning for high-risk/relapsed refractory MM; directly tests Flu+Mel backbone augmented with bortezomib and radiation |
| [NCT00856388](https://clinicaltrials.gov/study/NCT00856388) | Pilot | Completed | 62 | **Fludarabine** + Melphalan + low-dose TBI as reduced-intensity allo-SCT conditioning for haematologic cancers including MM; demonstrates feasibility and tolerability |
| [NCT00134004](https://clinicaltrials.gov/study/NCT00134004) | Phase 2 | Completed | 210 | Non-myeloablative **Fludarabine** + cyclophosphamide + radiation for partially HLA-mismatched BM transplant in haematologic malignancies (MM included); large Phase 2 supporting Flu-based NMA regimen |
| [NCT04093596](https://clinicaltrials.gov/study/NCT04093596) | Phase 1 | Active, not recruiting | 132 | ALLO-715 allogeneic BCMA CAR-T with ALLO-647 ± **Fludarabine**/cyclophosphamide lymphodepletion for R/R MM (UNIVERSAL trial); Fludarabine is standard lymphodepletion partner enabling CAR-T engraftment |
| [NCT05257083](https://clinicaltrials.gov/study/NCT05257083) | Phase 3 | Active, not recruiting | 759 | DVRd + ciltacabtagene autoleucel vs DVRd + ASCT for newly diagnosed MM; **Fludarabine**-based lymphodepletion included in the CAR-T treatment arm |
| [NCT07149857](https://clinicaltrials.gov/study/NCT07149857) | Phase 2 | Recruiting | 60 | Head-to-head comparison of **fludarabine**-free vs standard Cy/**Flu** lymphodepletion before cilta-cel infusion in MM; directly examines Fludarabine's necessity and role in this context |
| [NCT03832127](https://clinicaltrials.gov/study/NCT03832127) | Phase 1 | Recruiting | 35 | 18F-**Fludarabine** PET imaging for initial staging and end-of-treatment response assessment in symptomatic MM (first-in-kind diagnostic application); explores Fludarabine uptake as a biomarker for plasma cell burden |
| [NCT02507479](https://clinicaltrials.gov/study/NCT02507479) | Phase 2 | Unknown | 24 | **Fludarabine** + IV thiotepa followed by allo-HSCT for lymphoid malignancies including MM; explores thiotepa as substitute for busulfan/melphalan in Flu-based conditioning |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 Trial | Am J Clin Oncol | Phase 1 study of Bortezomib + **Fludarabine** + Melphalan ± total marrow irradiation as allo-HSCT conditioning for high-risk/R-R MM; documents safety and activity of Flu+Mel backbone with bortezomib intensification |
| [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/) | 2007 | Preclinical | Eur J Haematol | **Foundational preclinical evidence**: Fludarabine directly inhibits RPMI8226 myeloma cell line in vitro and in xenograft mouse models; mechanism involves Akt phosphorylation suppression, supporting direct anti-myeloma cytotoxicity |
| [15389436](https://pubmed.ncbi.nlm.nih.gov/15389436/) | 2004 | Retrospective Cohort | Biol Blood Marrow Transplant | Prognostic factor analysis of Melphalan/**Fludarabine** dose-reduced allo-HSCT in 120 MM patients (1998–2002); 1-year TRM 18%; prior relapse after autograft identified as strongest risk factor for poor outcome |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | Retrospective Cohort | Bone Marrow Transplant | **Fludarabine** + treosulfan reduced-toxicity conditioning before allo-SCT in 34 MM patients; demonstrates feasibility of low-toxicity Flu-based conditioning in a population not eligible for standard conditioning |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Phase 2 Trial | Leuk Res Rep | Split-dose busulfan + **Fludarabine** + post-transplant cyclophosphamide conditioning for allo-SCT in 6 MM and 4 myelofibrosis patients; 1-year OS 50%, non-relapse mortality 33%; reports early outcomes of this novel regimen |
| [37833271](https://pubmed.ncbi.nlm.nih.gov/37833271/) | 2023 | Retrospective Cohort | Blood Cancer J | Bendamustine vs **Fludarabine**/cyclophosphamide lymphodepletion prior to BCMA CAR-T therapy in MM; **Flu/Cy is the reference standard** against which alternative lymphodepletion regimens are evaluated |
| [36690811](https://pubmed.ncbi.nlm.nih.gov/36690811/) | 2023 | Phase 1 | Nature Medicine | UNIVERSAL trial interim results: ALLO-715 allogeneic BCMA CAR-T + ALLO-647 ± **Fludarabine**/cyclophosphamide for R/R MM (n=43); ORR 56% with tolerable safety profile; validates **Flu**-based lymphodepletion in allogeneic CAR-T setting |
| [38659046](https://pubmed.ncbi.nlm.nih.gov/38659046/) | 2024 | Long-term Follow-up | J Hematol Oncol | 5-year follow-up of LEGEND-2 trial (LCAR-B38M CAR-T, now cilta-cel) in R/R MM; **Fludarabine**/cyclophosphamide used as lymphodepletion; sustained deep remissions in subset of patients at 5 years |
| [39365257](https://pubmed.ncbi.nlm.nih.gov/39365257/) | 2025 | Real-World Cohort | Blood | Real-world outcomes of cilta-cel in 236 R/R MM patients at 16 US academic centres; standard-of-care **Flu**/cyclophosphamide lymphodepletion confirms Fludarabine's central role in current myeloma CAR-T practice |
| [7781758](https://pubmed.ncbi.nlm.nih.gov/7781758/) | 1995 | Case Series | Eur J Haematol | Earliest clinical report of **Fludarabine** activity in plasma cell leukaemia — a closely related plasma cell malignancy — providing historical clinical evidence predating large trial series |

---

## Singapore Market Information

Fludarabine is currently **not registered** with the Health Sciences Authority (HSA) in Singapore and has no approved products on the Singapore market. No Singapore licence records are available.

For clinical use in Singapore, access would need to be arranged through compassionate use, unregistered medicinal product import under the HSA's regulatory framework, or through an institutional protocol pending regulatory approval.

---

## Cytotoxicity

Fludarabine meets the criteria for antineoplastic classification: it is a fluorinated purine nucleoside analogue used to treat CLL and B-cell malignancies, and belongs to the antimetabolite/cytotoxic chemotherapy category.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Purine nucleoside analogue (Antimetabolite class) |
| Myelosuppression Risk | **High** — neutropenia, thrombocytopenia, and anaemia are common and dose-limiting; prolonged CD4+ lymphopenia increases opportunistic infection risk for months after treatment |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count with differential (before each cycle and during recovery), renal function (CrCl — dose reduction required for CrCl < 30–50 mL/min), neurological assessment (high-dose neurotoxicity risk), infection surveillance (including PCP and CMV monitoring) |
| Handling Protection | Must follow cytotoxic drug handling regulations — appropriate PPE, closed-system drug-transfer devices, biohazard waste disposal |

---

## Safety Considerations

Detailed safety data (warnings, contraindications, drug interactions) specific to Singapore regulatory filings are not available in the current evidence pack.

Please refer to the package insert for complete safety information.

> **Known class-level safety signals** based on published literature: (1) severe and potentially fatal myelosuppression requiring haematological monitoring; (2) risk of severe opportunistic infections, including Pneumocystis jirovecii pneumonia and CMV reactivation, necessitating prophylaxis; (3) progressive multifocal leukoencephalopathy (PML) reported at higher doses; (4) significant renal dose adjustment requirement (CrCl-based dosing); (5) embryotoxicity and teratogenicity — contraindicated in pregnancy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Fludarabine is mechanistically plausible and clinically embedded in multiple myeloma management, with preclinical evidence of direct anti-myeloma cytotoxicity (PMID 17976186), a robust retrospective dataset for Flu+Mel/Flu+Bu allo-HSCT conditioning in MM patients, and an established role as the standard lymphodepletion regimen enabling BCMA-targeted CAR-T therapies. However, no dedicated completed Phase 2/3 RCT demonstrates fludarabine's single-agent direct efficacy in myeloma outside of the transplant conditioning context, holding the evidence at L3.

**To proceed, the following is needed:**

- Obtain Singapore HSA regulatory guidance on importation or compassionate use of unregistered fludarabine products
- Retrieve full package insert warnings, contraindications, and drug interaction data from a reference regulatory filing (FDA, EMA, or TFDA) to complete the S1 safety assessment
- Retrieve mechanism of action detail from DrugBank (DB01073) to formally document the mechanistic link for institutional review purposes
- Define the specific intended clinical role: **(a)** direct anti-myeloma therapy vs **(b)** conditioning/lymphodepletion backbone — these require different development and regulatory pathways
- If pursuing direct anti-myeloma use, design a Phase 1/2 trial in the Singapore/Asia Pacific context to generate local evidence
- Establish haematological monitoring and infection prophylaxis protocols before any clinical deployment given the high myelosuppression and immunosuppression risk in this patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

