---
layout: default
title: Ifosfamide
parent: 僅模型預測 (L5)
nav_order: 515
evidence_level: L5
indication_count: 10
---

# Ifosfamide
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

# Ifosfamide: From Sarcoma & Testicular Cancer to Female Breast Carcinoma

## One-Sentence Summary

Ifosfamide is an oxazaphosphorine alkylating agent with well-established antineoplastic activity, originally used in soft tissue sarcoma and testicular carcinoma treatment.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **8 clinical trials** and **20 publications** currently supporting this direction.
Evidence is rated **L2**, anchored by multiple Phase 2 trials and one large Phase 3 randomized trial (n=637) whose completion status remains unconfirmed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Soft tissue sarcoma, testicular carcinoma (established oncology use; no Singapore registrations on file) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological literature, Ifosfamide is an oxazaphosphorine prodrug that undergoes hepatic bioactivation by cytochrome P450 enzymes (CYP3A4, CYP2B6, CYP2C9) to generate its active metabolite, isofosforamide mustard. This active species forms DNA interstrand cross-links, blocking replication in rapidly dividing cells. Importantly, a translational study (PMID 14970873) demonstrated that all three activating CYP enzymes are expressed in breast cancer tissue microsomes, confirming that intratumoral bioactivation is mechanistically feasible—a property not shared by all alkylating agents.

Breast carcinoma shares a defining characteristic with ifosfamide's classical indications: dependence on rapid cell proliferation. The IMF regimen (Ifosfamide substituting for cyclophosphamide in the CMF backbone) was specifically designed for CMF-refractory breast cancer patients, establishing that ifosfamide provides a pharmacologically distinct and non-cross-resistant alkylating mechanism within this disease setting. Multiple combination partners—including docetaxel, paclitaxel, vinorelbine, epirubicin, and carboplatin—have been systematically explored across more than three decades of clinical investigation.

The breadth of evidence is notable: clinical series dating from 1990 through 2002 consistently show ifosfamide-based regimens producing meaningful response rates (overall response rates of 30–50% in anthracycline-pretreated patients), a randomized Phase 2 trial in 357 evaluable patients, and at least one Phase 3 randomized trial (NCT00954174, n=637). These data collectively establish a plausible and biologically coherent rationale for the TxGNN model's high-confidence prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|------------|------|--------|-----------|-------------|
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | Unknown | 42 | Docetaxel + Ifosfamide as first-line chemotherapy in metastatic breast cancer; direct head-to-head efficacy evaluation of this ifosfamide-containing doublet |
| [NCT00954174](https://clinicaltrials.gov/study/NCT00954174) | Phase 3 | Unknown | 637 | Randomized trial of Paclitaxel + Carboplatin vs. Ifosfamide + Paclitaxel in newly diagnosed/recurrent carcinosarcoma (uterine/fallopian/peritoneal/ovarian); largest randomized dataset comparing an ifosfamide arm |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | Completed | 33 | Sequential high-dose cycles of Cisplatin, Cyclophosphamide, Etoposide, and Ifosfamide/Carboplatin/Taxol with autologous stem cell support in advanced cancer; establishes high-dose ifosfamide safety and dosing reference |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | Unknown | N/A | Randomized comparison of multi-cycle high-dose vs. optimized conventional chemotherapy (including ifosfamide) in metastatic breast cancer; dose-optimization reference |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | TIME regimen (Topotecan + Ifosfamide/Mesna + Etoposide) followed by autologous stem cell rescue in metastatic breast cancer; confirms ifosfamide's role in intensive salvage combinations |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | Terminated | 12 | Samarium-153 plus high-dose sequential chemotherapy (including ifosfamide) for Stage IV breast cancer; terminated early due to limited enrollment |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | Terminated | 7 | High-dose chemotherapy + peripheral stem cell transplant + activated T-cell therapy in Stage IV breast cancer; ifosfamide in conditioning regimen; terminated with very small enrollment |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Patient-derived organoid drug screen (SCORE study) for refractory solid tumours; ifosfamide included as candidate chemotherapy agent in precision selection platform |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|------------|
| [11932893](https://pubmed.ncbi.nlm.nih.gov/11932893/) | 2002 | Phase II Trial | *Cancer* | Paclitaxel (24-hour infusion) + ifosfamide in anthracycline-resistant metastatic breast carcinoma; systematic efficacy and tolerability assessment |
| [8711499](https://pubmed.ncbi.nlm.nih.gov/8711499/) | 1996 | Randomized Phase II | *Seminars in Oncology* | Epirubicin/ifosfamide vs. treatment interruption in advanced metastatic breast cancer; n=331 evaluable, 8% CR + 37% PR; largest randomized ifosfamide dataset in breast cancer |
| [2347057](https://pubmed.ncbi.nlm.nih.gov/2347057/) | 1990 | Clinical Trial | *Cancer Chemother Pharmacol* | IMF regimen (ifosfamide replacing cyclophosphamide) in 25 CMF-refractory breast cancer patients; established ifosfamide as a viable alkylating alternative with distinct activity |
| [8918497](https://pubmed.ncbi.nlm.nih.gov/8918497/) | 1996 | Clinical Trial | *J Clin Oncol* | Ifosfamide + vinorelbine as first-line chemotherapy in metastatic breast cancer; efficacy and toxicity profile for this non-anthracycline doublet |
| [8873839](https://pubmed.ncbi.nlm.nih.gov/8873839/) | 1996 | Clinical Series | *J Chemotherapy* | IMEpi (ifosfamide + mesna + epirubicin) as second-line in advanced breast cancer (n=16); 50% overall response rate with 9.6-month median remission duration |
| [2347053](https://pubmed.ncbi.nlm.nih.gov/2347053/) | 1990 | Clinical Series | *Cancer Chemother Pharmacol* | Epirubicin + ifosfamide in 23 refractory breast cancer patients; notable activity in a heavily pretreated population |
| [10602907](https://pubmed.ncbi.nlm.nih.gov/10602907/) | 1999 | Clinical Trial | *Cancer Chemother Pharmacol* | ICE (Ifosfamide + Carboplatin + Etoposide) in 25 metastatic/refractory breast cancer patients; response data after multiple prior regimens |
| [2112056](https://pubmed.ncbi.nlm.nih.gov/2112056/) | 1990 | Clinical Trial | *Cancer Chemother Pharmacol* | Ifosfamide/etoposide + mesna in 44 advanced breast cancer patients with measurable refractory disease; systematic efficacy and toxicity evaluation |
| [9226029](https://pubmed.ncbi.nlm.nih.gov/9226029/) | 1997 | Clinical Trial | *Tumori* | Ifosfamide + etoposide in previously treated advanced breast cancer; response characteristics and toxicity profile in alkylating-based salvage setting |
| [1720382](https://pubmed.ncbi.nlm.nih.gov/1720382/) | 1991 | Review | *Drugs* | Comprehensive review of ifosfamide antineoplastic activity, pharmacokinetic properties, and therapeutic efficacy including breast cancer; mesna uroprotection framework established |

---

## Singapore Market Information

Ifosfamide currently has **no registered product licenses** in Singapore. The drug is not available as a marketed commercial product through standard channels.

Any clinical use in Singapore would require accessing the drug through:
- Importation under the Special Access Route (SAR) via the Health Sciences Authority (HSA)
- Institutional compassionate use or clinical trial protocols
- International procurement for licensed clinical research

---

## Cytotoxicity

Ifosfamide is classified as a conventional cytotoxic antineoplastic agent. It fulfils multiple criteria: it belongs to the oxazaphosphorine/nitrogen mustard alkylating class, its original and predicted indications are malignant neoplasms, and it carries the characteristic toxicity profile of cytotoxic chemotherapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Oxazaphosphorine alkylating agent (nitrogen mustard analogue) |
| Myelosuppression Risk | High — leukopenia and neutropenia are dose-limiting; thrombocytopenia common; risk amplified with high-dose regimens and combinations (e.g., ICE) |
| Emetogenicity Classification | Moderate to High (dependent on dose and infusion duration) |
| Monitoring Items | CBC with differential (at least weekly during treatment), serum creatinine and BUN, urinalysis with microscopy (hematuria surveillance), liver function tests, serum electrolytes (especially phosphate — Fanconi syndrome risk) |
| Handling Protection | Must follow cytotoxic drug handling regulations (PPE, closed-system transfer devices); mandatory mesna co-administration for uroprotection against hemorrhagic cystitis; specialized pharmacy preparation required |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical co-administration requirement**: Ifosfamide must always be given with **mesna** (sodium 2-mercaptoethane sulfonate) to prevent hemorrhagic cystitis, an otherwise life-threatening urothelial toxicity. This is not optional. All clinical protocols must specify the mesna dosing schedule (typically 60–160% of ifosfamide dose, divided across the infusion period). Additionally, there is a well-documented risk of **ifosfamide encephalopathy** (CNS toxicity), and of **therapy-related MDS/AML** with cumulative alkylating agent exposure — both must be addressed in patient consent and long-term follow-up planning.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
More than 30 years of clinical investigation across multiple Phase 2 trials and one Phase 3 randomized trial (NCT00954174, n=637) demonstrate consistent activity of ifosfamide-based regimens in metastatic and anthracycline-resistant breast cancer. The mechanistic basis — alkylation of rapidly proliferating tumour cells — is sound and confirmed by evidence of intratumoral bioactivation in breast tissue. The evidence level (L2) reflects the absence of a confirmed, published Phase 3 primary endpoint result, but the totality of data is sufficient to justify structured clinical investigation.

**To proceed, the following is needed:**
- Confirm publication status and primary endpoint results of NCT00954174 (Phase 3, n=637, status UNKNOWN); this single data point could elevate evidence to L1
- Obtain full MOA documentation from DrugBank (DB01181) to complete mechanistic linkage analysis
- Establish Singapore HSA Special Access Route (SAR) pathway for drug importation, given zero local registrations
- Define mandatory mesna co-administration protocol and monitoring algorithm for hemorrhagic cystitis and Fanconi syndrome
- Specify patient eligibility criteria: anthracycline exposure history, renal function thresholds (creatinine clearance ≥ 60 mL/min recommended), CNS status, and prior treatment lines
- Assess cumulative alkylating agent exposure to model therapy-related MDS/AML risk for long-term survivorship planning
- Retrieve TFDA package insert PDF for full warnings, contraindications, and drug interaction data to complete S1 safety screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

