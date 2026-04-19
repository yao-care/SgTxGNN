# Arsenic Trioxide: From Acute Promyelocytic Leukemia to Myelodysplastic Syndrome Spectrum

## One-Sentence Summary

Arsenic trioxide (ATO) is an established antineoplastic agent approved internationally for Acute Promyelocytic Leukemia (APL), exerting its effects through pro-apoptotic, differentiating, and anti-angiogenic mechanisms.
The TxGNN model predicts it may be effective across a **spectrum of myelodysplastic and bone marrow failure conditions**, with the top prediction by score being **unclassified myelodysplastic syndrome** (99.93%), while the best-supported prediction is **myelodysplastic syndrome** (rank 6), backed by **24 clinical trials** and **20 publications** including a 2025 RCT and a 2023 systematic review.
Additional predictions spanning aplastic anemia, Ewing sarcoma, and rare bone marrow failure syndromes are also evaluated, with evidence levels ranging from L2 to L5 across the 10 predicted indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Promyelocytic Leukemia (APL) |
| Top TxGNN Prediction (Rank 1) | Unclassified Myelodysplastic Syndrome |
| Best-Supported Prediction | Myelodysplastic Syndrome (Rank 6) |
| TxGNN Score (Rank 1) | 99.93% |
| Evidence Level (Best-Supported Prediction) | L2 — Myelodysplastic Syndrome |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** (MDS, Aplastic Anemia) / Research Question (MDS subtypes, Ewing Sarcoma) / Hold (3 indications) |

---

## All Predicted Indications Summary

| Rank | Disease | TxGNN Score | Evidence Level | Trials | Literature | Recommendation |
|------|---------|-------------|----------------|--------|------------|----------------|
| 1 | Unclassified Myelodysplastic Syndrome | 99.93% | L4 | 0 | 0 | Research Question |
| 2 | Refractory Cytopenia of Childhood | 99.93% | L3 | 1 | 0 | Research Question |
| 3 | Severe Congenital Hypochromic Anemia with Ringed Sideroblasts | 99.93% | L5 | 0 | 0 | Hold |
| 4 | Aregenerative Anemia (Aplastic Anemia) | 99.92% | L3 | 6† | 12† | Proceed with Guardrails |
| 5 | 5q- Syndrome (Partial del(5q)) | 99.92% | L4 | 0 | 0 | Research Question |
| 6 | Myelodysplastic Syndrome | 99.91% | L2 | 24 | 20 | Proceed with Guardrails |
| 7 | Ewing Sarcoma | 99.89% | L3 | 1 | 10 | Research Question |
| 8 | Dermatofibrosarcoma Protuberans | 99.77% | L5 | 0 | 0 | Hold |
| 9 | Liposarcoma | 99.75% | L5 | 0 | 0 | Hold |
| 10 | Ovarian Myxoid Liposarcoma | 99.70% | L5 | 0 | 0 | Hold |

*† Trials and literature for rank 4 are predominantly MDS-related with indirect relevance to aplastic anemia; directly aplastic-anemia-specific literature: 4 papers.*

---

## Why is This Prediction Reasonable?

Arsenic trioxide (ATO, As₂O₃) has been used medicinally for centuries and received FDA approval for APL in 2000. Its established mechanism in APL — degradation of the PML-RAR oncofusion protein, induction of differentiation, and apoptosis of malignant promyelocytes — represents only part of its broader biological activity. ATO also possesses multiple independent mechanisms that extend its therapeutic potential beyond APL.

For **myelodysplastic syndrome**, the mechanistic links are robust and multi-layered: (1) ATO induces mitochondria-dependent apoptosis specifically in abnormal clonal myeloid progenitors; (2) it inhibits NF-κB, which is pathologically upregulated in advanced MDS and drives pro-survival signalling; (3) it downregulates BCL2 and BCL-XL anti-apoptotic proteins; (4) it demonstrates synergistic epigenetic effects when combined with hypomethylating agents (Decitabine, Azacitidine); and (5) ROS-mediated DNA damage preferentially targets dysplastic cells. A 2023 network meta-analysis and a 2025 RCT confirm that these mechanisms translate directly to clinical benefit.

For **aplastic anemia (aregenerative anemia)**, a distinct pathway applies: ATO attenuates T-cell-mediated immune destruction of haematopoietic progenitors by enhancing regulatory T cells (Tregs), suppressing pro-inflammatory IFN-γ and IL-17, and upregulating TGF-β1 to restore immune tolerance. This immunomodulatory rationale is mechanistically independent of the MDS apoptotic pathway and is supported by dedicated prospective clinical studies. However, conflicting results across trials indicate that patient selection and treatment sequencing are critical.

Detailed mechanism of action data from DrugBank is not available in this evidence pack. The mechanistic rationale above is drawn from published peer-reviewed literature.

---

## Clinical Trial Evidence

### Myelodysplastic Syndrome (Rank 6 — Highest Evidence)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00195104](https://clinicaltrials.gov/study/NCT00195104) | Phase 1/2 | Completed | 87 | ATO + low-dose Cytarabine for high-risk MDS and poor-prognosis AML; 17% complete remission rate, tolerable safety |
| [NCT02190695](https://clinicaltrials.gov/study/NCT02190695) | Phase 2 | Completed | 92 | Randomised Leukemia SPORE study: Decitabine vs Decitabine + Carboplatin vs Decitabine + ATO in relapsed/refractory AML and MDS |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Completed | 2,000 | Large treatment development programme for older AML/high-risk MDS patients; highest enrolment trial, provides broad safety data |
| [NCT00093366](https://clinicaltrials.gov/study/NCT00093366) | Phase 1/2 | Completed | 32 | ATO + Etanercept for advanced MDS; completed with directly relevant MDS-specific efficacy data |
| [NCT00274781](https://clinicaltrials.gov/study/NCT00274781) | Phase 2 | Completed | 30 | ATO + Gemtuzumab Ozogamicin for advanced MDS; completed with response data |
| [NCT00671697](https://clinicaltrials.gov/study/NCT00671697) | Phase 1 | Completed | 13 | IV Decitabine + ATO + Ascorbic Acid in MDS and AML; safety and dose-finding study |
| [NCT00621023](https://clinicaltrials.gov/study/NCT00621023) | Phase 2 | Completed | 7 | Decitabine + ATO + Ascorbic Acid for MDS; safety pilot with positive completion |
| [NCT06778187](https://clinicaltrials.gov/study/NCT06778187) | Phase 2 | Recruiting | 30 | Oral ATO (Arsenol®) + ascorbic acid + investigator-choice low-intensity therapy for TP53-mutated myeloid malignancies including MDS; ongoing 2025–2028 |
| [NCT06670222](https://clinicaltrials.gov/study/NCT06670222) | Phase 1 | Recruiting | 24 | Oral ATO for low-risk MDS failing ESA and Luspatercept; dose-escalation study launched July 2025 |
| [NCT00803530](https://clinicaltrials.gov/study/NCT00803530) | Phase 2 | Terminated | 55 | ATO + Ascorbic Acid for MDS; prospective multicentre trial, terminated — provides partial efficacy and safety data |

### Refractory Cytopenia of Childhood (Rank 2)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00104806](https://clinicaltrials.gov/study/NCT00104806) | Phase 2 | Terminated | 5 | ATO + Cholecalciferol for MDS (includes paediatric context); terminated early — indirect evidence for paediatric MDS |

### Ewing Sarcoma (Rank 7)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00024258](https://clinicaltrials.gov/study/NCT00024258) | Phase 2 | Completed | 22 | ATO for paediatric neuroblastoma and other solid tumours including Ewing sarcoma subgroup; completed — provides safety and initial efficacy data in paediatric solid tumours |

---

## Literature Evidence

### Myelodysplastic Syndrome (Rank 6)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37908176](https://pubmed.ncbi.nlm.nih.gov/37908176/) | 2023 | Systematic Review / Meta-analysis | Hematology | Network meta-analysis confirming ATO efficacy in MDS via apoptosis and demethylation; identifies optimal ATO-containing combination regimens |
| [40167011](https://pubmed.ncbi.nlm.nih.gov/40167011/) | 2025 | RCT | Hematology | Decitabine + ATO vs Decitabine alone in elderly high-risk MDS; combination demonstrates superior efficacy with manageable safety |
| [38816179](https://pubmed.ncbi.nlm.nih.gov/38816179/) | 2024 | Comparative Study | Immunopharmacology & Immunotoxicology | Realgar vs ATO immunological comparison in murine MDS model; confirms ATO modulates immune-mediated disease pathogenesis |
| [20956016](https://pubmed.ncbi.nlm.nih.gov/20956016/) | 2011 | Phase 1/2 Clinical Study | Leukemia Research | ATO + low-dose Cytarabine in 49 intermediate-2/high-risk MDS patients; 17% CR, 8% 4-week mortality |
| [22964015](https://pubmed.ncbi.nlm.nih.gov/22964015/) | 2012 | Clinical/Molecular Study | J Hematol Oncol | ATO + Ascorbic Acid modulates BCL2 family gene expression in MDS patients; ex vivo confirmation of apoptotic mechanism |
| [16105982](https://pubmed.ncbi.nlm.nih.gov/16105982/) | 2005 | Molecular Study | Blood | NF-κB and FLIP in ATO-induced apoptosis in MDS; mechanistic basis for differential ATO activity across MDS subtypes |
| [17920679](https://pubmed.ncbi.nlm.nih.gov/17920679/) | 2008 | Clinical Study | Leukemia Research | ATO + retinoic acid + thalidomide combination in higher-risk MDS; efficacy and safety evaluation |
| [20425329](https://pubmed.ncbi.nlm.nih.gov/20425329/) | 2006 | Review | Curr Hematol Malignancy Reports | Comprehensive review of ATO as MDS treatment: pro-apoptotic, antiproliferative, and anti-angiogenic mechanisms; clinical trial results |
| [30898879](https://pubmed.ncbi.nlm.nih.gov/30898879/) | 2019 | Preclinical Study | J Investig Med | Decitabine + ATO synergistic activity via ER stress-related apoptosis in MUTZ-1 and SKM-1 MDS cell lines |
| [27665715](https://pubmed.ncbi.nlm.nih.gov/27665715/) | 2016 | In Vitro Study | Mol Med Reports | ATO + Triptolide synergistic apoptosis induction in SKM-1 MDS cell line via NF-κB pathway inhibition |

### Aplastic Anemia / Aregenerative Anemia (Rank 4)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32590737](https://pubmed.ncbi.nlm.nih.gov/32590737/) | 2020 | Prospective Clinical Study | Medicine | ATO increases Treg frequency and modulates IFN-γ, IL-4, IL-17, TGF-β1 in severe aplastic anemia patients; immunological mechanism confirmed in vivo |
| [23044093](https://pubmed.ncbi.nlm.nih.gov/23044093/) | 2012 | Clinical Study | J Hematol Oncol | ATO 0.15 mg/kg IV in 5 refractory severe aplastic anemia patients; 60% complete response, 100% overall response rate at 17 weeks |
| [23064943](https://pubmed.ncbi.nlm.nih.gov/23064943/) | 2013 | Clinical Trial / Case Series | Ann Hematol | ATO for refractory aplastic anemia; supporting case series data from same research group |
| [29075064](https://pubmed.ncbi.nlm.nih.gov/29075064/) | 2017 | Phase II Trial | Indian J Hematol Blood Transfus | Open-label Phase II of ATO in ATG-refractory aplastic anemia; 0% response in all patients, terminated at 8 weeks — critical negative data |

### Ewing Sarcoma (Rank 7)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31746397](https://pubmed.ncbi.nlm.nih.gov/31746397/) | 2020 | In Vitro Study | Oncology Reports | ATO + Etoposide synergistic interaction in Ewing sarcoma cell lines; ATO enhances etoposide-induced cell death |
| [27665785](https://pubmed.ncbi.nlm.nih.gov/27665785/) | 2016 | In Vitro / Preclinical | Int J Oncology | ATO potentiates etoposide in Ewing sarcoma cells while sparing normal mesenchymal stem cells |
| [16646077](https://pubmed.ncbi.nlm.nih.gov/16646077/) | 2006 | Preclinical Study | Int J Cancer | Clinically tolerable ATO concentrations induce p53-independent apoptosis and suppress NF-κB in Ewing sarcoma |
| [21946058](https://pubmed.ncbi.nlm.nih.gov/21946058/) | 2012 | In Vitro Study | Anti-Cancer Drugs | ATO inhibits Ewing sarcoma cell invasiveness via p38-MAPK and JNK pathway suppression |
| [22315235](https://pubmed.ncbi.nlm.nih.gov/22315235/) | 2012 | Preclinical (PPTP) | Pediatr Blood Cancer | PPTP programme evaluation of ATO focused on Ewing sarcoma in vivo; modest activity, IC₅₀ values comparable to other PPTP cell lines |

---

## Singapore Market Information

Arsenic trioxide is currently **not registered** in Singapore. No HSA marketing authorisations have been identified.

| Item | Details |
|------|---------|
| HSA Registration Status | Not registered |
| Active Registrations | 0 |
| Available Local Dosage Forms | None |
| Regulatory Pathway if Pursuing Use | HSA Special Access Route (SAR) — Compassionate Use or Unregistered Drug Import |

For reference, ATO is available internationally as **Trisenox®** (Jazz Pharmaceuticals) as an intravenous formulation (1 mg/mL, 10 mg/10 mL ampoule), approved in the US, EU, and several Asia-Pacific markets. An oral formulation, **Arsenol®**, is under Phase 2 investigation (NCT06778187). Clinical procurement via HSA's Special Access Route would be required before any use in Singapore.

---

## Cytotoxicity

Arsenic trioxide is classified as an antineoplastic agent, indicated for a haematological malignancy (APL) and under investigation for multiple haematological disorders.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic with differentiating properties — inorganic arsenic compound (not a classical alkylating agent or antimetabolite; unique mechanism class) |
| Myelosuppression Risk | Moderate — leukocytosis and differentiation syndrome risk in APL context; cytopenias possible in MDS/aplastic anemia setting; monitor closely |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (baseline and weekly); 12-lead ECG with QTc measurement (baseline, then at minimum weekly); serum electrolytes (K⁺, Mg²⁺, Ca²⁺) before each dose; liver function tests; renal function; blood glucose |
| Handling Protection | Standard cytotoxic drug handling regulations apply for IV preparation and administration; appropriate containment and PPE required |

> **Critical Warning — QTc Prolongation**: ATO is a known QT-prolonging drug. Torsades de pointes and fatal arrhythmias have been reported. Electrolyte correction (K⁺ ≥4.0 mEq/L; Mg²⁺ ≥1.8 mg/dL) before and throughout treatment is mandatory. Avoid concurrent QT-prolonging medications.

> **Carcinogenicity Note**: Arsenic is classified as an IARC Group 1 human carcinogen. Long-term cancer risk must be weighed against benefit, particularly for non-malignant indications or in younger patients.

---

## Safety Considerations

Complete package insert warnings and contraindications are not yet available in this evidence pack. The full prescribing information for Trisenox® or an equivalent registered product must be reviewed before any clinical use.

Based on published literature and internationally available prescribing information:

- **QTc Prolongation and Cardiac Arrhythmia**: Mandatory baseline ECG; electrolyte optimisation required before and during each treatment cycle; avoid concomitant QT-prolonging drugs (common examples in haematology patients: fluoroquinolones, azole antifungals, ondansetron)
- **Hepatotoxicity**: Transaminase elevations are commonly reported across trials; monitor LFTs at baseline and periodically
- **Peripheral Neuropathy**: Cumulative and dose-dependent; monitor for sensory symptoms and assess motor function
- **APL Differentiation Syndrome**: A risk primarily in APL treatment context; less likely in MDS/aplastic anemia use but should be monitored
- **Renal Toxicity**: Arsenic is renally excreted; dose adjustment considerations may apply in renal impairment

Please refer to the official Trisenox® prescribing information for complete drug interaction and contraindication data.

---

## Conclusion and Next Steps

---

### Myelodysplastic Syndrome (Rank 6)

**Decision: Proceed with Guardrails**

**Rationale:**
A 2023 systematic review and network meta-analysis, combined with a 2025 RCT (Decitabine + ATO), directly confirm clinical efficacy in MDS. The mechanistic rationale is multi-layered and well-validated. Although ATO is not registered in Singapore, the evidence base is sufficiently mature to support a structured investigational programme or compassionate use protocol.

**To proceed, the following is needed:**
- Obtain Trisenox® prescribing information for full safety review (addresses Data Gap DG001)
- Retrieve ATO mechanistic profile from DrugBank (addresses Data Gap DG002)
- Define target patient population: IPSS risk score, TP53 mutation status, prior therapy history
- Establish mandatory cardiac monitoring protocol with pre-treatment electrolyte optimisation
- Apply for HSA Special Access Route for drug importation
- Consider Decitabine + ATO combination based on the 2025 RCT evidence as preferred regimen

---

### Aregenerative Anemia / Aplastic Anemia (Rank 4)

**Decision: Proceed with Guardrails**

**Rationale:**
Prospective Chinese clinical studies confirm ATO's immunomodulatory mechanism in aplastic anemia, with a 100% overall response rate in a small refractory series. However, a separate Phase II trial reported 0% response and was terminated early, indicating strong patient selection dependency. This indication warrants a carefully designed investigational study before clinical adoption.

**To proceed, the following is needed:**
- Identify predictive biomarkers for response (baseline Treg levels, IFN-γ, IL-17)
- Standardise dosing protocol (0.15 mg/kg IV appears most studied)
- Design a prospective study with pre-specified response criteria (IWG 2006 or equivalent)
- Rule out competing diagnoses (e.g., hypoplastic MDS) before enrolment

---

### MDS Subtypes and Ewing Sarcoma (Ranks 1, 2, 5, 7)

**Decision: Research Question**

**To proceed, the following is needed:**
- For unclassified MDS (rank 1) and 5q- syndrome (rank 5): leverage broader MDS trial data; design retrospective sub-analyses or registry studies
- For refractory cytopenia of childhood (rank 2): develop paediatric PK/PD data; establish dosing guidance for the paediatric population; assess growth and developmental safety
- For Ewing sarcoma (rank 7): confirm in vivo activity in standard preclinical models; design a Phase 1/2 combination study (ATO + Etoposide) in recurrent/refractory disease based on the convergent in vitro evidence

---

### Ranks 3, 8, 9, 10

**Decision: Hold**

Severe congenital hypochromic anemia with ringed sideroblasts (rank 3), dermatofibrosarcoma protuberans (rank 8), liposarcoma (rank 9), and ovarian myxoid liposarcoma (rank 10) lack any supporting clinical or preclinical evidence. For rank 3, ATO's mitochondrial toxicity may potentially worsen iron metabolism dysregulation, representing a possible safety concern. No further action is recommended at this stage for these four indications.

---

> **Disclaimer**: This report is intended for research reference only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before any therapeutic application. All pages should include appropriate YMYL disclaimers.