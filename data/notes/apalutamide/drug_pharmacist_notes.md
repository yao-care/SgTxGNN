# Apalutamide: From Prostate Cancer to Male Reproductive Organ Cancer

## One-Sentence Summary

Apalutamide (Erleada®) is a second-generation androgen receptor (AR) inhibitor globally established for prostate cancer treatment—having received FDA approval for non-metastatic castration-resistant prostate cancer (2018) and metastatic castration-sensitive prostate cancer (2019)—yet remains unregistered in Singapore.
The TxGNN model predicts it may be effective for **Male Reproductive Organ Cancer**, with **50 clinical trials** and **18 publications** currently supporting this direction.
This indication carries the strongest evidence level in the dataset (L1), driven by multiple completed Phase 3 RCTs, and the recommended decision is **Proceed with Guardrails** pending local regulatory authorization.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (globally approved; not registered in Singapore) |
| Predicted New Indication | Male Reproductive Organ Cancer |
| TxGNN Prediction Score | 97.41% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Singapore regulatory database. Based on the published scientific record, Apalutamide is a competitive androgen receptor (AR) inhibitor that binds directly to the ligand-binding domain of AR, preventing androgen binding, blocking AR nuclear translocation, and inhibiting downstream AR-mediated transcriptional activation. Originally developed as ARN-509, it was specifically engineered to overcome the partial agonist activity of first-generation antiandrogens such as bicalutamide—particularly relevant in the castration-resistant setting where AR is frequently overexpressed or constitutively activated.

Prostate cancer is fundamentally an androgen-driven malignancy. The androgen receptor remains the principal oncogenic driver even after systemic testosterone suppression, a phenomenon that underpins the transition to castration-resistant disease. Apalutamide targets this central oncogenic pathway by directly antagonising AR signalling, thereby suppressing tumour cell proliferation, DNA synthesis, and survival. This mechanism is active across multiple stages of the prostate cancer continuum: high-risk localised disease, non-metastatic castration-resistant disease (nmCRPC), and metastatic hormone-sensitive disease (mHSPC).

The TxGNN model's prediction of "male reproductive organ cancer" as a high-confidence indication (score 97.41%) is entirely consistent with Apalutamide's established clinical profile. The landmark Phase 3 SPARTAN trial demonstrated an approximately 24-month improvement in metastasis-free survival for nmCRPC, and the Phase 3 TITAN trial confirmed superior overall survival when apalutamide was added to androgen deprivation therapy in mHSPC. The drug's absence from the Singapore market reflects a regulatory gap rather than an evidence gap.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03767244](https://clinicaltrials.gov/study/NCT03767244) | Phase 3 | Active, Not Recruiting | 2,517 | Double-blind RCT of apalutamide + ADT vs placebo + ADT before and after radical prostatectomy in high-risk localised/locally advanced PCa; primary endpoints: pathological complete response rate and metastasis-free survival |
| [NCT02489318](https://clinicaltrials.gov/study/NCT02489318) | Phase 3 | Active, Not Recruiting | 1,052 | TITAN study: apalutamide + ADT vs ADT alone in metastatic hormone-sensitive PCa; final analysis confirmed significant improvement in both radiographic PFS and overall survival |
| [NCT04557059](https://clinicaltrials.gov/study/NCT04557059) | Phase 3 | Active, Not Recruiting | 694 | Apalutamide added to radiotherapy + LHRHa in high-risk hormone-sensitive PCa; evaluating PSMA-PET-based metastatic progression delay vs RT + LHRHa alone |
| [NCT06592924](https://clinicaltrials.gov/study/NCT06592924) | Phase 3 | Recruiting | 830 | Docetaxel addition to ARPI in mCSPC patients with suboptimal PSA response; tests treatment escalation in poor first-line responders |
| [NCT03124433](https://clinicaltrials.gov/study/NCT03124433) | Phase 2 | Completed | 30 | NEAR trial: neoadjuvant apalutamide monotherapy + radical prostatectomy in D'Amico intermediate/high-risk PCa; demonstrated tumour downstaging and pathological responses |
| [NCT01171898](https://clinicaltrials.gov/study/NCT01171898) | Phase 1/2 | Completed | 127 | Original proof-of-concept study of ARN-509 (apalutamide) in advanced CRPC; established dose selection and initial efficacy across three patient cohorts, forming the basis for Phase 3 development |
| [NCT03436654](https://clinicaltrials.gov/study/NCT03436654) | Phase 2 | Active, Not Recruiting | 102 | Multi-arm neoadjuvant study combining apalutamide + abiraterone + prednisone + ADT before surgery in very high-risk localised and low-volume metastatic PCa |
| [NCT04295447](https://clinicaltrials.gov/study/NCT04295447) | Phase 2 | Active, Not Recruiting | 190 | Adjuvant apalutamide vs standard of care after radical prostatectomy in high-risk PCa; primary endpoint: biochemically recurrence-free survival |
| [NCT02867020](https://clinicaltrials.gov/study/NCT02867020) | Phase 2 | Completed | 128 | Three-arm randomised comparison of abiraterone + ADT, apalutamide alone, and abiraterone + apalutamide in hormone-naïve locally advanced or metastatic PCa |
| [NCT05202301](https://clinicaltrials.gov/study/NCT05202301) | Observational | Completed | 13,779 | Large real-world study on medication adherence and discontinuation patterns among prostate cancer patients initiating second-generation AR inhibitors including apalutamide |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33914595](https://pubmed.ncbi.nlm.nih.gov/33914595/) | 2021 | Phase 3 RCT | J Clin Oncol | TITAN final analysis: apalutamide + ADT significantly improved OS and rPFS in mCSPC; survival benefit maintained after placebo-to-apalutamide crossover |
| [31150574](https://pubmed.ncbi.nlm.nih.gov/31150574/) | 2019 | Phase 3 RCT | N Engl J Med | TITAN primary analysis: apalutamide + ADT vs placebo + ADT in metastatic castration-sensitive PCa; significant rPFS and OS advantage at first interim analysis |
| [29420164](https://pubmed.ncbi.nlm.nih.gov/29420164/) | 2018 | Phase 3 RCT | N Engl J Med | SPARTAN study: apalutamide extended median metastasis-free survival by approximately 24 months vs placebo in high-risk non-metastatic CRPC |
| [32907777](https://pubmed.ncbi.nlm.nih.gov/32907777/) | 2021 | Phase 3 RCT | Eur Urol | SPARTAN final OS analysis: apalutamide improved overall survival in nmCRPC; validated MFS as a surrogate endpoint for OS in this disease setting |
| [36858151](https://pubmed.ncbi.nlm.nih.gov/36858151/) | 2023 | Phase 3 Analysis | Ann Oncol | TITAN PSA kinetics sub-analysis: deep and rapid PSA decline with apalutamide + ADT independently associated with improved OS; ultralow PSA identified as a prognostic marker in mCSPC |
| [38261983](https://pubmed.ncbi.nlm.nih.gov/38261983/) | 2024 | Phase 3 RCT | J Clin Oncol | PRESTO (AFT-19): androgen blockade intensification with apalutamide in high-risk biochemically relapsed castration-sensitive PCa following radical prostatectomy; assessed whether intensification improves outcomes |
| [39417629](https://pubmed.ncbi.nlm.nih.gov/39417629/) | 2025 | Comparative Cohort | The Prostate | Real-world multicenter comparison of abiraterone, enzalutamide, and apalutamide differential efficacy and safety in metastatic hormone-sensitive PCa |
| [36167599](https://pubmed.ncbi.nlm.nih.gov/36167599/) | 2023 | Phase 2 RCT | Eur Urol | ARNEO trial: randomised neoadjuvant degarelix ± apalutamide prior to radical prostatectomy; assessed pathological downstaging and biomarker response in high-risk PCa |
| [35091711](https://pubmed.ncbi.nlm.nih.gov/35091711/) | 2022 | Phase 2 | Prostate Cancer Prostatic Dis | NEAR trial results: single-arm Phase II of neoadjuvant apalutamide monotherapy + radical prostatectomy in D'Amico intermediate-/high-risk PCa; pathological efficacy and downstaging outcomes |
| [32930958](https://pubmed.ncbi.nlm.nih.gov/32930958/) | 2020 | Review | Drugs | Comprehensive drug review: apalutamide mechanism of action, Phase 3 clinical evidence (TITAN), pharmacokinetics, and safety profile in metastatic castration-sensitive PCa |

---

## Singapore Market Information

Apalutamide is currently **not registered** in Singapore. No product authorisations are on file with the Health Sciences Authority (HSA), and no apalutamide-containing products are commercially available locally. Regulatory authorisation is required before the drug can be prescribed or distributed in Singapore.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Second-generation Androgen Receptor Inhibitor (non-cytotoxic, non-myelosuppressive mechanism of action) |
| Myelosuppression Risk | Low (AR inhibitors do not suppress bone marrow; standard haematological monitoring recommended as part of routine oncology follow-up) |
| Emetogenicity Classification | Low (oral agent; nausea is infrequent in clinical trials; routine antiemetic prophylaxis is not required) |
| Monitoring Items | Thyroid function (TSH), liver function tests, blood pressure, fasting lipid profile, bone mineral density (with long-term ADT co-administration); ECG if QT-prolonging agents are co-prescribed |
| Handling Protection | Standard oral anticancer agent handling guidelines apply; dedicated cytotoxic compounding facilities are generally not required; follow local institutional SOPs |

---

## Safety Considerations

- **Drug Interactions**: Apalutamide is a potent inducer of CYP3A4 and may substantially reduce plasma concentrations of co-administered CYP3A4-sensitive substrates, including tyrosine kinase inhibitors, anticoagulants, immunosuppressants, and certain statins. A comprehensive medication reconciliation is essential prior to initiation and at each review.
- **Key Adverse Events to Monitor**: Skin reactions and rash (reported in approximately 24% of patients in the TITAN trial), fatigue, hypothyroidism, falls and fractures (associated with concurrent ADT use), and cardiovascular events require proactive monitoring and patient counselling.

> Complete prescribing information—including boxed warnings, full contraindications, and a comprehensive drug interaction table—is not available in the current dataset. Please refer to the approved package insert (e.g., FDA-approved Erleada® Prescribing Information or the most current EMA-approved SmPC) for complete safety guidance.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Apalutamide has established L1 evidence from multiple completed Phase 3 RCTs—SPARTAN for nmCRPC and TITAN for mCSPC—demonstrating clinically meaningful and statistically significant improvements in both metastasis-free survival and overall survival. The drug is approved in the US, EU, Japan, and other major markets, yet remains unavailable to Singapore patients with prostate cancer, one of the most prevalent male malignancies in the region. The evidence base is robust; the primary barrier is regulatory.

**To proceed, the following is needed:**

- **HSA Regulatory Submission**: Prepare and submit a New Drug Application (NDA) or abridged application to the Health Sciences Authority (HSA) Singapore, leveraging existing FDA/EMA approval dossiers to expedite review
- **Complete Safety Documentation**: Obtain the full prescribing information including boxed warnings, contraindications, and a comprehensive DDI table, which are currently absent from the local regulatory dataset
- **CYP3A4 DDI Risk Management Protocol**: Develop institutional guidance for managing strong CYP3A4 induction interactions in the Singapore patient population, with particular attention to polypharmacy settings common in elderly oncology patients
- **Risk Management Plan (RMP)**: Prepare a Singapore-specific RMP addressing key identified risks: falls and fractures, cardiovascular events, hypothyroidism, and skin reactions
- **Asian Subgroup Data Review**: Evaluate available Asian patient subgroup data from TITAN and SPARTAN to confirm appropriateness for the Singapore population and determine whether additional bridging studies are required
- **Formulary and Reimbursement Strategy**: Assess cost-effectiveness for potential inclusion in national subsidy schemes (e.g., Medication Assistance Fund) or institutional hospital drug formularies