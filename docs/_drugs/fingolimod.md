---
layout: default
title: Fingolimod
parent: 僅模型預測 (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
---

# Fingolimod
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

# Fingolimod: From Multiple Sclerosis to Borderline Ovarian Serous Tumor

## One-Sentence Summary

Fingolimod (FTY720, brand name Gilenya) is a sphingosine-1-phosphate (S1P) receptor modulator internationally approved for relapsing-remitting multiple sclerosis, though it holds no Singapore registration.
The TxGNN model predicts it may be effective for **Borderline Ovarian Serous Tumor** (top-ranked prediction, score 94.9%),
with **no clinical trials** and **no direct literature** supporting this specific indication — though related preclinical evidence for epithelial ovarian cancer exists under adjacent disease labels in the knowledge graph.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; internationally approved for relapsing-remitting Multiple Sclerosis |
| Predicted New Indication | Borderline Ovarian Serous Tumor |
| TxGNN Prediction Score | 94.9% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on information surfaced in the retrieved literature, Fingolimod (FTY720) is a synthetic sphingosine analogue that functions as an S1P receptor modulator. In its approved indication — relapsing-remitting multiple sclerosis — it sequesters lymphocytes within lymph nodes by acting as a functional antagonist at S1P receptors on lymphocyte surfaces, thereby reducing autoreactive immune cell trafficking into the CNS.

The TxGNN knowledge graph infers a connection between the S1P signaling pathway and ovarian serous pathology through shared gene nodes. Sphingosine kinase 1 (SphK1), the enzyme producing S1P, is over-expressed in epithelial ovarian carcinoma (EOC). FTY720 — as a functional S1P antagonist — may suppress tumor cell survival by activating protein phosphatase 2A (PP2A), which dephosphorylates and inactivates pro-survival Akt/ERK signaling. Preclinical data also show FTY720 induces necroptosis and modulates autophagy in ovarian cancer cell lines.

However, **"borderline ovarian serous tumor"** (low malignant potential tumor) is a clinically distinct entity from invasive EOC. These tumors carry a favorable prognosis and are managed primarily with surgery alone. The rationale for systemic immunomodulatory or cytotoxic intervention in this specific subtype is clinically weak, and no preclinical data specifically addresses borderline tumors. The KG prediction derives entirely from structural graph proximity between the S1P pathway and the broader ovarian serous ontology node — not from direct biological evidence in borderline histology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Fingolimod in borderline ovarian serous tumor or any of the 10 predicted ovarian/haematological indications in this evidence pack.

---

## Literature Evidence

No literature is available for Fingolimod specifically in **borderline ovarian serous tumor** (Rank 1).

The table below presents all retrievable preclinical evidence aggregated under adjacent KG nodes (**serous neoplasm**, Rank 5; **ovarian benign neoplasm**, Rank 8), which collectively constitute the strongest available mechanistic signal:

> ⚠️ **Label Mismatch Notice**: All 8 publications retrieved under "ovarian benign neoplasm" actually address malignant epithelial ovarian carcinoma (EOC). This reflects a KG ontology artifact where ovarian cancer research is indexed under the broader ovarian neoplasm node. Evidence applies to invasive EOC, not benign tumors.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30120964](https://pubmed.ncbi.nlm.nih.gov/30120964/) | 2018 | PDX (in vivo) | Cancer Letters | FTY720 sensitizes drug-resistant ovarian cancer cells (A2780-cp20, HeyA8-MDR) to carboplatin and tamoxifen; efficacy confirmed in patient-derived xenograft models |
| [25429856](https://pubmed.ncbi.nlm.nih.gov/25429856/) | 2015 | Target validation | Int J Cancer | SphK1 over-expressed in EOC; FTY720 inhibits proliferation, induces apoptosis, reduces angiogenesis and invasion across multiple EOC cell lines |
| [20935520](https://pubmed.ncbi.nlm.nih.gov/20935520/) | 2010 | In vitro | Autophagy | FTY720 induces necrotic cell death in human ovarian cancer cells; autophagy activated concurrently and may function as a protective resistance mechanism |
| [23592281](https://pubmed.ncbi.nlm.nih.gov/23592281/) | 2013 | In vitro | Int J Oncology | ⚠️ FTY720 + cisplatin exhibits **antagonistic** cytotoxicity in ovarian cancer cells — critical conflict with carboplatin synergy finding above |
| [30388910](https://pubmed.ncbi.nlm.nih.gov/30388910/) | 2019 | In vitro | Cancer Biol Therapy | FTY720 synergizes with pemetrexed to kill NSCLC and ovarian cancer cells; overcomes resistance in K-RAS mutant and ERBB-inhibitor-resistant models |

> **Critical Platinum Interaction Conflict**: FTY720 is **synergistic** with carboplatin/tamoxifen but **antagonistic** with cisplatin in ovarian cancer models. Any future combination design must specify carboplatin, not cisplatin.

---

## Singapore Market Information

Fingolimod is **not registered in Singapore**. No authorization records are available.

Internationally, Fingolimod is marketed as **Gilenya** (Novartis) with approvals in the US (FDA, 2010), EU (EMA, 2011), and numerous other jurisdictions for relapsing-remitting multiple sclerosis.

---

## Safety Considerations

Please refer to the package insert for safety information. No Singapore-specific safety data is available in the current dataset (warnings, contraindications, and drug interaction records all returned as data gaps).

**Note from preclinical literature**: A mechanistically important drug interaction conflict has been identified:
- FTY720 is **synergistic** with carboplatin and tamoxifen in ovarian cancer PDX models
- FTY720 is **antagonistic** with cisplatin in ovarian cancer cell lines (autophagy-mediated resistance)

Platinum compound selection would be a critical safety and efficacy variable in any future clinical protocol design.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (borderline ovarian serous tumor) has zero direct supporting evidence, and the clinical logic for systemic drug intervention in low-malignant-potential ovarian tumors is weak — these lesions are typically curative with surgery alone. The broader preclinical evidence for FTY720 in malignant epithelial ovarian cancer is mechanistically coherent but remains confined to in vitro and one PDX study, far below the threshold for clinical translation. Singapore has no regulatory registration for this drug, and foundational safety data (package insert warnings, contraindications) is currently unavailable.

**To proceed, the following is needed:**
- **Clarify the intended repurposing target**: if the oncology signal of interest is invasive epithelial ovarian carcinoma (EOC), re-run evidence collection under that indication label rather than borderline/benign tumor nodes
- **Resolve DG002**: Obtain Fingolimod MOA from DrugBank API to enable mechanistic rationale scoring
- **Resolve DG001**: Obtain HSA/TFDA package insert warnings and contraindications to support S1 safety evaluation
- **Conduct a focused systematic review** of FTY720 in EOC, explicitly addressing the platinum-type interaction conflict (carboplatin synergy vs. cisplatin antagonism) before any combination protocol design
- **Generate EOC-specific preclinical data** (if not found in literature): in vivo models with carboplatin-based combinations to replicate and extend the 2018 PDX findings
- **Assess regulatory pathway**: Fingolimod would require Singapore NDA submission from scratch; consider whether a Phase 1 oncology IND/CTA is the appropriate next step given current evidence depth
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

