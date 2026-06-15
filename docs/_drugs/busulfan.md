---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan: From Chronic Myeloid Leukemia to Myelodysplastic Syndrome

## One-Sentence Summary

Busulfan is a bifunctional alkylating agent classically used for chronic myeloid leukemia (CML) and now widely adopted internationally as the backbone conditioning agent before allogeneic hematopoietic stem cell transplantation (allo-HSCT).
The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)**, supported by **multiple completed Phase 3 RCTs** and **20 publications** — including two landmark trials published in *The Lancet Haematology* — establishing the highest evidence level (L1) for this indication.
Despite strong international evidence, busulfan is currently not registered in Singapore, representing a critical access gap for eligible patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic myeloid leukemia (CML); HSCT conditioning (not registered in Singapore) |
| Predicted New Indication | Myelodysplastic Syndrome (MDS) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Busulfan is a bifunctional bis-alkylsulfonate that covalently cross-links DNA strands by alkylating the N7 position of guanine. This mechanism selectively destroys rapidly dividing haematopoietic progenitor cells — including the abnormal clonal stem cells that define MDS — while sparing most non-haematopoietic tissues at conditioning doses. The drug can be calibrated across a spectrum: myeloablative conditioning (MAC, typically Flu/Bu4 or BuCy) eradicates the MDS clone completely, while reduced-intensity conditioning (RIC, Flu/Bu2) achieves sufficient immunosuppression for donor engraftment in older or comorbid patients who cannot tolerate full myeloablation.

MDS and CML share a common denominator: both originate from clonal haematopoietic stem cell dysfunction. In CML, the BCR-ABL fusion drives proliferation; in MDS, somatic mutations in genes such as *SF3B1*, *TET2*, *ASXL1*, and *TP53* cause dysplastic, ineffective haematopoiesis and risk of leukaemic transformation. Allo-HSCT with busulfan-based conditioning addresses MDS by simultaneously clearing the abnormal clone, creating marrow space, and enabling a donor graft-versus-MDS immune effect. This mechanistic logic is identical to busulfan's established role in CML transplantation, making the TxGNN prediction biologically coherent rather than speculative.

The prediction is strongly validated by clinical practice. The Phase 3 MC11 trial (*Lancet Haematology*, PMID 31606445, n=476) used busulfan+fludarabine as the **standard-of-care comparator arm** in older/comorbid AML and MDS patients undergoing allo-HSCT — confirming its reference status. A second Phase 3 RCT (*Lancet Haematology*, PMID 36702138) demonstrated that adding G-CSF and decitabine to the BUCY backbone significantly reduced MDS relapse rates, further cementing busulfan as the conditioning foundation. The 99.62% TxGNN score is therefore not a novel discovery but a correct identification of an already well-established, internationally-accepted application that simply lacks regulatory approval in Singapore.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05823714](https://clinicaltrials.gov/study/NCT05823714) | Phase 2 | Unknown | 70 | Venetoclax + Azacytidine bridge therapy followed by modified BUCY (busulfan + cyclophosphamide) conditioning for high-risk MDS and R/R AML undergoing allo-HSCT; evaluates the complete bridging-to-conditioning clinical pathway |
| [NCT07183878](https://clinicaltrials.gov/study/NCT07183878) | Randomized | Recruiting | 138 | Prospective multicenter RCT comparing Venetoclax-enhanced BUCY versus standard BUCY conditioning in high-risk AML/MDS before allo-HSCT; 1:1 randomization, primary endpoint OS |
| [NCT00629798](https://clinicaltrials.gov/study/NCT00629798) | Phase 2 | Completed | 64 | Busulfan + Melphalan + Fludarabine with peri-transplant palifermin (mucosal protection) followed by T-cell depleted allo-HSCT for advanced MDS and AML; directly tests busulfan-containing conditioning with adequate sample and complete follow-up |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | Completed | 80 | Multi-centre HLA-mismatched unrelated donor BMT with post-transplant cyclophosphamide (PTCy) for haematologic malignancies including MDS; demonstrates busulfan conditioning feasibility in mismatched-donor setting |
| [NCT00301834](https://clinicaltrials.gov/study/NCT00301834) | Phase 2 | Completed | 35 | Fludarabine + Busulfan + Alemtuzumab reduced-toxicity ablative regimen for paediatric patients with MDS and marrow failure syndromes; specifically evaluates busulfan in the paediatric MDS transplant context |
| [NCT03412409](https://clinicaltrials.gov/study/NCT03412409) | Phase 2 | Recruiting | 50 | RIC regimen for elderly or high-comorbidity burden patients receiving haploidentical HSCT; targets the population with greatest clinical unmet need where transplant-related mortality is the primary concern |
| [NCT00469144](https://clinicaltrials.gov/study/NCT00469144) | Phase 3 | Completed | 233 | Randomized Phase 3 comparing PK-guided (AUC-targeted) once-daily IV busulfan versus fixed-dose busulfan combined with fludarabine for AML/MDS; establishes therapeutic drug monitoring (TDM) as the standard approach to optimize efficacy and reduce toxicity |
| [NCT06829472](https://clinicaltrials.gov/study/NCT06829472) | Phase 3 | Recruiting | 120 | Randomized Phase 3 comparing Melphalan 100 mg/m² versus 140 mg/m² within the Melphalan-Busulfan-Fludarabine (MBF) conditioning platform for AML/MDS; refines dosing to reduce toxicity without compromising disease control |
| [NCT04713956](https://clinicaltrials.gov/study/NCT04713956) | Phase 2/3 | Unknown | 242 | Prospective study evaluating G-CSF + Decitabine + BUCY versus G-CSF + Decitabine + BF conditioning specifically in RAEB-1, RAEB-2 and secondary AML evolving from MDS; large sample, MDS-specific design |
| [NCT05453552](https://clinicaltrials.gov/study/NCT05453552) | Phase 2/3 | Unknown | 242 | Parallel prospective study evaluating the same G-CSF + Decitabine + BUCY versus G-CSF + Decitabine + BF comparison focused on high-risk MDS; complements NCT04713956 with expanded MDS scope |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | RCT | The Lancet Haematology | Phase 3 open-label multicentre RCT: G-CSF + decitabine + BUCY significantly reduced relapse vs. BUCY alone in MDS-RAEB and secondary AML patients undergoing allo-HSCT; establishes enhanced BUCY as superior conditioning platform |
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | Phase 3 RCT | The Lancet Haematology | MC11 Trial (n=476): treosulfan non-inferior to busulfan + fludarabine in older/comorbid AML and MDS patients; formally validates busulfan+fludarabine as the international reference standard for RIC conditioning in this population |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | RCT Final Analysis | American Journal of Hematology | Final analysis of the Phase 3 MC11 trial: treosulfan-based conditioning improves event-free survival versus RIC busulfan in older AML/MDS; reinforces busulfan benchmark while defining its performance ceiling |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | Prospective Phase 2 | Transplantation and Cellular Therapy | Myeloablative busulfan + fludarabine with in vivo T-cell depletion is safe and effective for AML/MDS across age groups when guided by HCT-CI comorbidity scoring; supports extension of MAC to older, fit patients |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | Phase 3 RCT | Journal of Clinical Oncology | Phase 3 RCT comparing MAC vs. RIC before allo-HCT in AML/MDS: lower TRM with RIC, lower relapse with MAC; foundational data for conditioning intensity decision-making |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Registry Cohort | Bone Marrow Transplantation | Japanese national registry propensity-matched analysis: Flu/Bu4 superior to Bu4/Cy as myeloablative conditioning for MDS; supports fludarabine-busulfan as the preferred MAC backbone |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Registry Cohort | Transplantation and Cellular Therapy | Japanese national registry propensity-matched analysis comparing MAC Flu/Bu4 versus RIC Flu/Bu2 for MDS; provides real-world guidance on dose-intensity selection based on patient risk profile |
| [33471943](https://pubmed.ncbi.nlm.nih.gov/33471943/) | 2021 | Retrospective Cohort | Cancer | Fractionated IV busulfan myeloablative conditioning can be safely administered to older AML/MDS patients without increasing non-relapse mortality; extends MAC eligibility beyond the traditional age cutoff of 55 |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Retrospective Cohort | Transplantation and Cellular Therapy | Propensity score-matched single-centre study (n=138 MDS patients): treosulfan vs. busulfan conditioning for MDS allo-HCT; provides contemporary comparative effectiveness data in a real-world MDS transplant population |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Narrative Review | American Journal of Hematology | Contemporary review of allo-HSCT for MDS and myelofibrosis: covers genomic-informed patient selection, conditioning intensity optimisation, novel pre-transplant therapies, and outcomes benchmarks for clinical practice |

---

## Singapore Market Information

Busulfan is currently not registered or marketed in Singapore. No product authorizations are on record with HSA.

Busulfan IV (Busulfex®) and oral formulations (Myleran®) are approved in the US (FDA), EU (EMA), Japan (PMDA), and multiple other major markets for haematopoietic conditioning and/or CML. Any clinical use in Singapore would require an import exemption under the Medicines Act or access through an institutional compassionate use / named patient programme.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Alkylating agent (bifunctional bis-alkylsulfonate; busulfan class) |
| Myelosuppression Risk | **High** — severe, prolonged pancytopenia is the intended therapeutic effect at conditioning doses; myeloablation at MAC doses, significant cytopenia at RIC doses |
| Emetogenicity Classification | Moderate to High — IV formulation at myeloablative doses is considered highly emetogenic; prophylactic antiemetic regimen (5-HT3 antagonist ± NK1 antagonist) required |
| Monitoring Items | Complete blood count with differential (daily during conditioning); liver function tests and bilirubin (sinusoidal obstruction syndrome/VOD surveillance); serum creatinine and BUN; busulfan pharmacokinetics (AUC-guided TDM is the standard of care — target AUC 900–1350 µmol·min); neurological status assessment (seizure risk) |
| Handling Protection | Must follow cytotoxic drug handling regulations; IV formulation (Busulfex®) requires preparation in a biological safety cabinet by trained pharmacy staff; closed-system drug transfer devices recommended |

---

## Safety Considerations

Formal warning and contraindication data specific to Singapore regulatory filings are not available for this review, as busulfan is not registered locally.

Based on internationally established class-level safety information for clinical awareness:

- **Seizure risk**: Prophylactic antiepileptic therapy (levetiracetam or phenytoin) is mandatory during busulfan conditioning due to dose-dependent CNS toxicity
- **Hepatotoxicity / Sinusoidal Obstruction Syndrome (SOS/VOD)**: A serious, potentially fatal complication occurring in 5–40% of patients depending on risk factors; ursodiol prophylaxis is standard; defibrotide is used for established severe SOS
- **Secondary malignancy**: Long-term leukemogenic risk with extended oral use (historical context: oral Myleran for CML); risk profile of conditioning-dose IV busulfan differs and is considered acceptable given transplant intent
- **Pulmonary toxicity**: "Busulfan lung" (interstitial pneumonitis) reported with prolonged oral use; less common with short-course IV conditioning regimens

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Busulfan-based conditioning for allo-HSCT in MDS is supported by two completed Phase 3 RCTs in *The Lancet Haematology* using busulfan+fludarabine as the international standard-of-care comparator, numerous Phase 2 trials, and a large body of registry data — meeting the L1 evidence threshold. The mechanistic basis is clear, clinical practice is mature, and the drug is considered standard of care in international transplant guidelines (EBMT, NCCN). The critical barrier is not efficacy or safety, but the absence of regulatory registration in Singapore, which must be resolved before institutional adoption.

**To proceed, the following is needed:**

- **Regulatory access pathway**: Initiate HSA import licence application or Named Patient Programme for IV busulfan (Busulfex®); identify a licensed Singapore distributor or international supplier
- **Safety data package**: Obtain and review the full SmPC/package insert (US FDA label or EMA SPC) to complete the blocking safety assessment (warnings, contraindications, DDI) identified as a data gap in this evidence pack
- **MOA documentation**: Retrieve DrugBank DB01008 full drug profile to complete mechanism-of-action documentation for clinical reference materials
- **Pharmacokinetic monitoring protocol**: Establish AUC-guided TDM service capacity at the transplant centre (target AUC 900–1350 µmol·min/dose); requires access to busulfan plasma assay
- **Toxicity management protocols**: Formalize institutional SOPs for seizure prophylaxis, VOD/SOS surveillance and treatment (including defibrotide access), and hepatotoxicity monitoring
- **Patient population definition**: Identify eligible MDS patients (IPSS-R intermediate-high/very high risk) who are allo-HSCT candidates and for whom busulfan-based conditioning would be selected over alternatives (e.g., treosulfan, when available)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

