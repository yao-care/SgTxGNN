---
layout: default
title: Gimeracil
parent: 僅模型預測 (L5)
nav_order: 321
evidence_level: L5
indication_count: 10
---

# Gimeracil
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

# Gimeracil: From Gastric Cancer (S-1 Component) to Colonic Neoplasm

## One-Sentence Summary

Gimeracil is a key component of the S-1 combination (tegafur/gimeracil/oteracil), which is clinically used as part of a fluoropyrimidine-based antineoplastic regimen primarily for gastric cancer treatment.
The TxGNN model predicts it may be effective for **Colonic Neoplasm**,
with **8 clinical trials** and **14 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric cancer (as S-1 component; no direct Singapore registration) |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Gimeracil (CDHP) is one of the three active components of S-1 (tegafur/gimeracil/oteracil potassium). Its specific role is to inhibit dihydropyrimidine dehydrogenase (DPD), the primary enzyme responsible for the catabolism of 5-fluorouracil (5-FU). By blocking DPD, gimeracil sustains elevated intratumoral concentrations of 5-FU generated from tegafur, thereby amplifying the antitumor effect of the S-1 combination. This mechanism of enhancing fluoropyrimidine availability is directly relevant to any 5-FU-sensitive tumour type.

Currently, detailed standalone mechanism of action data for gimeracil as an isolated agent is not available. Based on its pharmacological role within S-1, its efficacy against gastrointestinal malignancies has been well established. Gastric cancer and colonic neoplasm share overlapping molecular characteristics: both are gastrointestinal epithelial tumours with high expression of thymidylate synthase, sensitivity to fluoropyrimidine-based chemotherapy, and responsiveness to oxaliplatin-containing regimens (SOX, XELOX). The S-1 combination has obtained colorectal cancer indications in Japan and Taiwan, providing strong regulatory precedent and further supporting the TxGNN model's prediction.

Given that gimeracil's function is specifically tied to maximising 5-FU activity — and that 5-FU has been a cornerstone of colorectal cancer treatment for decades — the mechanistic link between gimeracil's contribution and colonic neoplasm is biologically sound and clinically credible.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1,191 | SOX (S-1 + Oxaliplatin) vs. XELOX (Capecitabine + Oxaliplatin) as adjuvant chemotherapy for Stage III colorectal cancer; head-to-head comparison addressing hand-foot syndrome burden of capecitabine |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO trial: S-1 vs. Capecitabine ± Bevacizumab as first-line treatment for metastatic colorectal cancer; safety evaluation of oral fluoropyrimidines |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1,535 | UFT + Leucovorin vs. S-1 (TS-1) as adjuvant treatment for Stage III colon cancer; includes gene expression analysis for predictive factors |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | Unknown | 42 | S-1 + Oral Leucovorin + Oxaliplatin (SOL) as first-line therapy for untreated metastatic colorectal cancer; established S-1 equivalence to 5-FU/LV |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | S-1 vs. Capecitabine + Oxaliplatin in metastatic GI adenocarcinoma; evaluated cardiac microvascular toxicity (coronary flow reserve); terminated early |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + Bevacizumab in unresectable or recurrent colorectal cancer after irinotecan- and oxaliplatin-containing regimen failure |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | Raltitrexed + S-1 for metastatic colorectal cancer following failure of standard chemotherapy; primary endpoint: median progression-free survival |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not Yet Recruiting | 52 | Fuquinitinib + Tegafur/Gimeracil/Oteracil (S-1) as third-line treatment for advanced metastatic colorectal cancer (CRC); open-label, single-arm, multicentre |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21875473](https://pubmed.ncbi.nlm.nih.gov/21875473/) | 2011 | Clinical Study | Chinese Journal of Oncology | Evaluated efficacy and safety of oxaliplatin + S-1 combination for postoperative colorectal cancer; supports SOX regimen in CRC |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Preclinical | Oncology Reports | CPT-11 and oxaliplatin combined with S-1 in 5-FU-sensitive/-resistant colon cancer xenografts; CPT-11 + S-1 significantly augmented antitumour activity |
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Retrospective Cohort | Gan to Kagaku Ryoho | Risk factor analysis for Grade 3–4 haematological toxicity in 87 patients with unresectable/recurrent colon cancer receiving S-1 + irinotecan; toxicity rate 16.1% |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Case Report | Anticancer Research | Complete response achieved and maintained with S-1 + CPT-11 for hepatic metastases of colon cancer; confirms S-1's activity in CRC |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Case Report | Gan to Kagaku Ryoho | Ascending colon cancer with multiple bilobar liver metastases successfully downstaged using SOX + panitumumab, enabling curative two-stage hepatectomy |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Case Report | Journal of Oncology Pharmacy Practice | Novel adverse effect: predominant hypertriglyceridaemia following S-1 administration in a CRC patient; confirms S-1 as effective agent for colorectal cancer |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | Pharmacokinetic Study | Gan to Kagaku Ryoho | Pharmacokinetics of S-1 for peritoneal metastasis from colon cancer in mouse model; investigated route-specific drug distribution |
| [41253353](https://pubmed.ncbi.nlm.nih.gov/41253353/) | 2025 | Case Report | Gan to Kagaku Ryoho | Sigmoid colon cancer with liver metastases treated sequentially with FOLFOX → tegafur/uracil → tegafur/gimeracil/oteracil; documents real-world S-1 use in CRC progression |
| [29483452](https://pubmed.ncbi.nlm.nih.gov/29483452/) | 2018 | Case Report | Gan to Kagaku Ryoho | Advanced transverse colon cancer with liver metastasis and portal vein tumour thrombosis; switched from CapeOX to S-1 + Bevacizumab after tumour perforation |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | Case Report | Gan to Kagaku Ryoho | Ascending colon cancer Stage IIIb; postoperative adjuvant chemotherapy with UFT/Leucovorin followed by repeated laparoscopic resection for peritoneal recurrence |

---

## Singapore Market Information

Gimeracil (as a standalone registered product or as part of an S-1 combination product) is currently **not registered in Singapore**. No marketing authorisation records were identified in the Singapore regulatory database.

Note: S-1 combination products (Teysuno, TS-One) are approved in Japan, the EU, and Taiwan for gastrointestinal cancers. A Singapore registration application may be feasible given the available Phase 3 evidence.

---

## Cytotoxicity

Gimeracil is a component of S-1, a cytotoxic antineoplastic regimen of the fluoropyrimidine class.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine class (DPD inhibitor component of S-1) |
| Myelosuppression Risk | Moderate — Grade 3–4 haematological toxicity reported at 16.1% in S-1 + irinotecan cohort (PMID 21084813); neutropenia and thrombocytopenia are the main concerns |
| Emetogenicity Classification | Low to moderate (consistent with oral fluoropyrimidine class) |
| Monitoring Items | Complete blood count with differential (CBC-DC), liver function tests (AST/ALT/bilirubin), renal function (serum creatinine, eGFR), serum triglycerides (hypertriglyceridaemia reported), and assessment for hand-foot syndrome |
| Handling Protection | Must follow institutional cytotoxic drug handling and disposal regulations; oral formulation handling precautions apply |

---

## Safety Considerations

No specific safety data (key warnings, contraindications, or drug–drug interactions) for gimeracil was identified in the current evidence pack. Please refer to the S-1 (tegafur/gimeracil/oteracil potassium) package insert for full safety information, including warnings regarding DPD-deficient patients, concomitant fluoropyrimidine use, and renal/hepatic impairment dose adjustments.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 3 clinical trials — including two completed studies (NCT01918852, NCT00660894) — support the clinical efficacy of S-1 in colorectal cancer, and the S-1 combination is approved for CRC indications in Japan and Taiwan. The mechanistic basis (DPD inhibition enhancing 5-FU activity in GI tumours) is well established, making this prediction both biologically and clinically credible. However, gimeracil itself is not independently registered in Singapore, and standalone safety data is absent.

**To proceed, the following is needed:**
- Regulatory feasibility assessment for registering S-1 (as a combination product) in Singapore for colorectal cancer indication
- Retrieval and review of the S-1 package insert (Japanese PMDA or EU SmPC) to fill the TFDA/HSA label gap for warnings and contraindications (Data Gap DG001)
- Pharmacogenomic screening protocol for DPD deficiency (DPYD polymorphism), which is a critical safety consideration for fluoropyrimidine-containing regimens
- Population-specific pharmacokinetic data for Singapore/Asian patients (particularly regarding renal dose adjustment)
- MOA documentation from DrugBank or primary literature to formally complete the mechanistic rationale analysis (Data Gap DG002)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

