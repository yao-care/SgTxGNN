---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: From Chronic Myeloid Leukemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib (Sprycel®) is a second-generation tyrosine kinase inhibitor (TKI) originally approved for the treatment of chronic myeloid leukemia (CML) and Philadelphia chromosome-positive (Ph+) acute lymphoblastic leukemia, working by blocking the BCR-ABL fusion kinase that drives these blood cancers.

The TxGNN model predicts it may be effective for **Ewing Sarcoma**, with **3 clinical trials** and **9 publications** currently supporting this direction. However, most evidence remains at the preclinical stage, and the single completed sarcoma trial enrolled all advanced sarcoma subtypes rather than Ewing sarcoma exclusively.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Myeloid Leukemia (CML), Ph+ Acute Lymphoblastic Leukemia |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Registered |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on known pharmacological information, Dasatinib is a small-molecule, orally bioavailable multi-kinase inhibitor that potently blocks BCR-ABL, Src family kinases (SFKs), c-KIT, and PDGFR-β. Its primary clinical approval is built on BCR-ABL inhibition in CML, but its Src kinase inhibitory activity creates a compelling mechanistic bridge to Ewing sarcoma biology.

Ewing sarcoma is a highly aggressive bone and soft tissue malignancy predominantly driven by the EWS-FLI1 fusion oncoprotein, which dysregulates downstream signaling pathways including the Src/FAK axis. Multiple preclinical studies from 2007 to 2022 have demonstrated that Ewing sarcoma cells are heavily dependent on Src kinase activity for migration, invasion, and survival — particularly under tumor microenvironmental stress conditions such as hypoxia and nutrient deprivation. Dasatinib has been shown to block invadopodia formation, inhibit Src-dependent cell migration, reduce proliferation, and induce apoptosis in Ewing sarcoma cell lines. The EWS-FLI1 fusion protein may additionally upregulate Src signaling, further reinforcing this mechanistic rationale.

Although CML and Ewing sarcoma are fundamentally different diseases (hematologic vs. bone/soft tissue malignancy), their shared dependency on Src-family kinase signaling provides a biologically plausible basis for repurposing. The TxGNN model's high prediction score (99.90%) likely reflects this Src-axis convergence captured within the knowledge graph. Notably, the largest sarcoma-specific dasatinib trial (NCT00464620, n=366) included Ewing sarcoma patients as part of an advanced sarcoma cohort, and Ewing sarcoma-specific subgroup results have not been separately published — representing the key evidence gap to resolve.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Dasatinib monotherapy in advanced sarcomas (all subtypes including Ewing); evaluated response rate and 6-month progression-free survival — the largest single dasatinib sarcoma trial to date, but Ewing-specific subgroup data not separately reported |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Pediatric trial of dasatinib combined with ICE chemotherapy (ifosfamide/carboplatin/etoposide); terminated early with only 7 patients enrolled, yielding limited safety data for the combination and no efficacy conclusions |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Recruiting | 41 | B7-H3 CAR-T cell therapy in pediatric relapsed/refractory solid tumors including Ewing sarcoma; not a dasatinib trial — included to reflect the broader landscape of novel agents being tested in this indication |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclinical (In vitro/In vivo) | Oncology Reports | Direct demonstration of dasatinib antiproliferative and antimigratory activity in Ewing sarcoma cell lines; c-KIT and PDGFR identified as relevant molecular targets in this tumor type |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclinical (In vitro) | Cancer Research | Dasatinib inhibits migration and invasion across diverse human sarcoma cell lines and induces apoptosis specifically in bone sarcoma cells that are Src-kinase dependent for survival |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Preclinical (Translational) | Sarcoma | Targeting the FAK-Src complex in Ewing sarcoma and related round cell sarcomas; dasatinib single-agent activity was insufficient, supporting combination strategies as the next step |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical (In vitro) | Neoplasia | Tenascin C and Src kinase cooperate under microenvironmental stress to drive invadopodia formation and invasion in Ewing sarcoma — dasatinib-targetable mechanism |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical (In vitro) | Neoplasia | Microenvironmental stress (hypoxia, nutrient deprivation) induces Src-dependent invadopodia activation and cell migration in Ewing sarcoma, identifying a stress-response vulnerability |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | Comprehensive review of Src signaling biology in sarcoma subtypes; positions Src inhibition — and by extension dasatinib — as a rational therapeutic strategy |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | Preclinical (In vitro) | Cell Communication and Signaling | CXCR4 antagonist plerixafor activates receptor tyrosine kinase signaling in Ewing sarcoma cells, highlighting crosstalk between microenvironmental pathways and Src-related signaling axes |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Clinical Review | Current Treatment Options in Oncology | Review of systemic therapy approaches in sarcomas, including discussion of antiangiogenic and TKI strategies; provides contextual framing for dasatinib's role in the broader sarcoma landscape |

---

## Singapore Market Information

Dasatinib is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No product authorizations or approved indications are on record.

> Dasatinib (Sprycel®, Bristol-Myers Squibb) is approved in major markets globally — including the US (FDA, 2006), EU (EMA), and Japan (PMDA) — for CML and Ph+ ALL. Access in Singapore would require an HSA Special Access Route (SAR) application under the Therapeutic Products Act for unregistered medicinal products.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — BCR-ABL / Src family kinase inhibitor (second-generation TKI); not a conventional cytotoxic agent |
| Myelosuppression Risk | Moderate — cytopenias (neutropenia, thrombocytopenia, anemia) are common class effects; Grade 3/4 neutropenia reported in approximately 21–36% of CML patients in pivotal trials |
| Emetogenicity Classification | Low — oral TKI with minimal intrinsic emetogenic potential; nausea is typically mild and manageable without prophylactic antiemetics |
| Monitoring Items | Complete blood count with differential (weekly for the first 2 months, then monthly thereafter), liver function tests, renal function, serum electrolytes, ECG for QTc assessment, and chest imaging for pleural effusion surveillance |
| Handling Protection | Standard oral cytotoxic handling precautions apply; closed-system transfer devices recommended if tablets require manipulation; disposal according to local cytotoxic waste regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

> No Singapore/Taiwan regulatory package insert data, contraindications, or drug interaction records were available in this Evidence Pack. Known class-associated concerns for dasatinib — based on global regulatory labels — include pleural effusion (occurring in approximately 20–35% of patients), pulmonary arterial hypertension, QTc prolongation, hepatotoxicity, and embryofetal toxicity (Pregnancy Category D). Consultation of the FDA-approved Sprycel® Prescribing Information or EMA Summary of Product Characteristics is strongly recommended prior to any clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for dasatinib in Ewing sarcoma is mechanistically coherent and supported by a consistent body of preclinical evidence spanning 15 years (2007–2022), all pointing to Src/FAK-axis dependency as a therapeutically exploitable vulnerability. A completed Phase 2 trial (n=366) has evaluated dasatinib in advanced sarcomas including Ewing patients, reaching L2 evidence level — but Ewing sarcoma-specific efficacy outcomes have not been separately reported, which represents the primary bottleneck before any clinical translation decision can be made.

**To proceed, the following is needed:**
- Obtain subgroup efficacy data from NCT00464620 specifically for the Ewing sarcoma patient cohort (contact investigators or review conference abstracts)
- Retrieve the full Sprycel® prescribing information (FDA USPI or EMA SmPC) for complete contraindications, black box warnings, and drug interaction profile
- Query DrugBank API to formally confirm mechanism of action and target binding profile (flagged as a high-severity data gap)
- Evaluate HSA Singapore Special Access Route eligibility if clinical use is contemplated
- Consider designing a Ewing sarcoma-specific biomarker-selected pilot study or basket trial incorporating Src phosphorylation status and EWS-FLI1 fusion confirmation as stratification criteria
- Assess potential combination partners — preclinical data suggest dasatinib as monotherapy may be insufficient; synergistic combinations with standard-of-care VDC/IE backbone or emerging agents warrant exploration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

