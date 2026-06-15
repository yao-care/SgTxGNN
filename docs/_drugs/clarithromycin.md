---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Clarithromycin
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

# Clarithromycin: From Bacterial Infections to Monoclonal Gammopathy

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic widely used for respiratory tract infections, *Helicobacter pylori* eradication, and *Mycobacterium avium* complex (MAC) infections.
The TxGNN model predicts it may be effective for **Monoclonal Gammopathy** (including MGUS and multiple myeloma),
with **1 completed Phase 2 clinical trial** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (respiratory tract, *H. pylori* eradication, MAC) |
| Predicted New Indication | Monoclonal Gammopathy |
| TxGNN Prediction Score | 98.81% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacology, Clarithromycin is a macrolide antibiotic that inhibits bacterial protein synthesis via binding to the 50S ribosomal subunit. Beyond its antibacterial properties, it is a potent **CYP3A4 inhibitor** and exerts significant immunomodulatory effects — including inhibition of NF-κB signalling and downregulation of pro-inflammatory cytokines such as TNF-α and IL-6.

Monoclonal gammopathy encompasses a spectrum of clonal plasma cell disorders, from the indolent pre-malignant state of MGUS (monoclonal gammopathy of undetermined significance) to symptomatic multiple myeloma. The mechanistic rationale for Clarithromycin in this disease spectrum operates on multiple levels: (1) **CYP3A4 inhibition** increases systemic drug exposure of immunomodulatory agents (IMiDs: thalidomide, lenalidomide, pomalidomide) and dexamethasone, effectively potentiating standard backbone regimens; (2) **direct NF-κB inhibition and cytokine downregulation** exert anti-myeloma effects independent of combination partners; and (3) **preclinical evidence** demonstrates synergistic cytotoxicity against myeloma cells when Clarithromycin is combined with IMiDs (PMID 26505646).

The clinical translation of these mechanisms is supported by multiple established combination regimens: BiRD (clarithromycin + lenalidomide + dexamethasone), BLT-D (clarithromycin + thalidomide + dexamethasone), and ClaPd (clarithromycin + pomalidomide + dexamethasone). A completed Phase 2 trial specifically targeting MGUS (NCT00006219) further validates the TxGNN prediction, and a Phase 3 RCT (Puig et al., 2021) was also conducted — lending this indication an unusually high level of clinical investigation for a repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00006219](https://clinicaltrials.gov/study/NCT00006219) | Phase 2 | Completed | N/A | Randomized Phase 2 comparing DHEA vs clarithromycin as chemoprevention in MGUS patients at high risk of progressing to multiple myeloma; completed December 2006 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34021118](https://pubmed.ncbi.nlm.nih.gov/34021118/) | 2021 | Randomized Clinical Trial | Blood Cancer Journal | Phase 3 RCT (286 patients): continuous Rd ± clarithromycin in transplant-ineligible MM; no significant PFS difference at median 19 months follow-up — raises questions about the added benefit of clarithromycin over standard Rd |
| [36394758](https://pubmed.ncbi.nlm.nih.gov/36394758/) | 2022 | Systematic Review / Meta-analysis | European Review for Medical and Pharmacological Sciences | Meta-analysis of pomalidomide + dexamethasone triplets in relapsed/refractory MM; contextualises clarithromycin-containing regimen (ClaPd) efficacy relative to other triplet options |
| [17989313](https://pubmed.ncbi.nlm.nih.gov/17989313/) | 2008 | Clinical Trial | Blood | BiRD regimen as first-line therapy in treatment-naive symptomatic MM: high complete and overall response rates established; served as the pivotal proof-of-concept for the clarithromycin + IMiD strategy |
| [30792190](https://pubmed.ncbi.nlm.nih.gov/30792190/) | 2019 | Phase 2 Clinical Trial | Blood Advances | ClaPd (clarithromycin + pomalidomide + dexamethasone) in 120 RRMM patients with prior lenalidomide exposure; evaluated safety and efficacy in a heavily pretreated population (median 5 prior lines) |
| [24723438](https://pubmed.ncbi.nlm.nih.gov/24723438/) | 2014 | Clinical Study | American Journal of Hematology | Retrospective analysis (24 patients): adding clarithromycin to lenalidomide/dexamethasone at disease progression reversed IMiD resistance; supports a resistance-reversal mechanism |
| [24576165](https://pubmed.ncbi.nlm.nih.gov/24576165/) | 2014 | Phase 2 Clinical Trial | Leukemia & Lymphoma | T-BiRD (thalidomide + clarithromycin + lenalidomide + dexamethasone) in 26 newly diagnosed MM patients; evaluated response and tolerability of this quadruplet oral regimen |
| [34424561](https://pubmed.ncbi.nlm.nih.gov/34424561/) | 2021 | Phase 2 Clinical Trial | American Journal of Hematology | Car-BiRd (carfilzomib → clarithromycin + lenalidomide + dexamethasone consolidation) sequential strategy in newly diagnosed MM; achieved deep responses with reduced corticosteroid toxicity |
| [12685831](https://pubmed.ncbi.nlm.nih.gov/12685831/) | 2002 | Phase 2 Clinical Trial | Leukemia & Lymphoma | BLT-D (clarithromycin + low-dose thalidomide + dexamethasone) in previously treated and untreated MM and Waldenström's macroglobulinemia; established clarithromycin's role as a non-myelosuppressive oral partner |
| [26505646](https://pubmed.ncbi.nlm.nih.gov/26505646/) | 2016 | Preclinical / Translational | Acta Haematologica | Clarithromycin synergistically enhances thalidomide cytotoxicity in myeloma cells in vitro; provides the mechanistic underpinning for IMiD potentiation across combination regimens |
| [12720150](https://pubmed.ncbi.nlm.nih.gov/12720150/) | 2003 | Clinical Study | Seminars in Oncology | Clarithromycin + thalidomide + dexamethasone in Waldenström's macroglobulinemia (a monoclonal IgM disorder closely related to MGUS); demonstrated improved activity over thalidomide monotherapy |

---

## Singapore Market Information

Clarithromycin is currently **not registered** in Singapore. No active product licences were identified in the regulatory database (0 registrations).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2 clinical trials and one completed Phase 3 RCT document Clarithromycin's use within combination regimens for monoclonal gammopathy and multiple myeloma. The mechanistic basis — CYP3A4-mediated IMiD potentiation combined with direct immunomodulatory and anti-tumour effects — is well characterised, and established regimens (BiRD, BLT-D, ClaPd) are already used in clinical practice. However, the Phase 3 RCT result (no significant PFS benefit when added to standard Rd) signals that the benefit may be context-dependent, indicating guardrails are necessary before broader adoption.

**To proceed, the following is needed:**
- Retrieve detailed MOA data from DrugBank API (CYP3A4 interaction profile, direct anti-tumour pathways) to complete the mechanistic analysis
- Obtain Singapore HSA package insert and label for key warnings, contraindications, and drug interaction data (currently all data gaps)
- Define the specific target subpopulation: MGUS chemoprevention vs. active MM (which line of therapy, which combination backbone)
- Conduct Singapore-specific regulatory pathway assessment for the "repurposed" oncology indication, given current zero-registration status
- Review the Phase 3 RCT (PMID 34021118) results in full to understand which patient subgroups may still derive benefit from clarithromycin addition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

