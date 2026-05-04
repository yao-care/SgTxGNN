---
layout: default
title: Capmatinib
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
---

# Capmatinib
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

# Capmatinib: From NSCLC (METex14) to Rheumatoid Arthritis

## One-Sentence Summary

Capmatinib (Tabrecta) is a selective c-MET/HGFR inhibitor approved by the FDA for the treatment of non-small cell lung cancer (NSCLC) harbouring MET exon 14 (METex14) skipping mutations.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
with **0 clinical trials** and **1 publication** (a general narrative review) currently providing only indirect mechanistic support for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | NSCLC with MET exon 14 skipping mutations |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Capmatinib is a highly selective, orally bioavailable inhibitor of the c-MET receptor tyrosine kinase (also known as HGFR, hepatocyte growth factor receptor). By blocking MET phosphorylation, capmatinib suppresses downstream pro-survival and pro-migratory signalling cascades including PI3K/AKT, RAS/MAPK, and STAT3. Its original oncology indication exploits the fact that METex14 mutations abolish the receptor's self-degradation signal, leading to constitutive kinase activation and tumour growth.

In rheumatoid arthritis (RA), the HGF/c-MET axis is aberrantly upregulated within the inflamed synovium. Synovial fibroblasts (FLS) from RA patients overexpress c-MET, and HGF stimulation drives FLS proliferation, invasion into cartilage, and secretion of matrix metalloproteinases. Additionally, MET-mediated signalling promotes VEGF-driven pannus (inflammatory tissue) formation and neovascularisation, processes that sustain chronic joint destruction. Mechanistically, therefore, blocking MET could theoretically restrain FLS invasiveness and synovial angiogenesis — two hallmarks of RA pathology.

However, the mechanistic link currently rests on indirect inference only. The sole retrieved publication (PMID 33513356) is a broad narrative review of FDA-approved kinase inhibitors and does not present any RA-specific data for capmatinib. No dedicated in vitro, animal-model, or clinical studies have been published examining capmatinib in an RA context. This means the biological plausibility, while conceptually coherent, lacks empirical validation and the prediction should be treated as an early-stage hypothesis requiring dedicated experimental work.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Capmatinib in Rheumatoid Arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Narrative Review | Pharmacological Research | Comprehensive overview of properties of all FDA-approved small molecule kinase inhibitors as of 2021, including capmatinib; no RA-specific data presented |

---

## Singapore Market Information

Capmatinib currently holds **no registered product licences** in Singapore. The drug is therefore not commercially available in this market.

For reference, capmatinib (Tabrecta®) has received regulatory approval in the following major jurisdictions outside Singapore:

| Jurisdiction | Approval Year | Approved Indication |
|-------------|--------------|---------------------|
| USA (FDA) | 2020 | Adult patients with metastatic NSCLC whose tumours have a METex14 skipping mutation |
| EU (EMA) | 2022 | Adult patients with advanced NSCLC with METex14 skipping mutations |
| Japan (PMDA) | 2021 | Unresectable, advanced/recurrent NSCLC with MET gene alterations |

Any future regulatory pathway in Singapore would require local registration prior to clinical use.

---

## Cytotoxicity

Capmatinib is an antineoplastic targeted therapy (kinase inhibitor class).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective MET receptor tyrosine kinase inhibitor |
| Myelosuppression Risk | Low to moderate; peripheral oedema, nausea, and fatigue are more common dose-limiting effects; haematologic toxicity is uncommon but monitor baseline CBC |
| Emetogenicity Classification | Low (consistent with most oral targeted kinase inhibitors) |
| Monitoring Items | CBC with differential; liver function tests (ALT/AST — interstitial lung disease and hepatotoxicity reported); renal function; QTc interval at baseline and during dose escalation |
| Handling Protection | Oral solid dosage form; standard precautions for handling cytotoxic oral agents apply (avoid crushing tablets, use gloves) |

---

## Safety Considerations

Detailed TFDA package insert warnings and contraindications are not available in the current data set (Data Gap DG001). Please refer to the FDA/EMA-approved Tabrecta® prescribing information for complete safety details.

Key safety signals from the approved oncology indication that remain relevant in any new indication:

- **Interstitial Lung Disease (ILD) / Pneumonitis**: Reported in ~5% of patients in the GEOMETRY mono-1 trial; any new or worsening respiratory symptoms require prompt evaluation and treatment interruption.
- **Photosensitivity**: Patients should be counselled to limit sun exposure and use broad-spectrum sunscreen.
- **Embryo-Foetal Toxicity**: Capmatinib can cause foetal harm; effective contraception required in women of childbearing potential.
- **Drug Interactions**: No DDI data were retrieved in this evidence pack. Note that capmatinib is a substrate of CYP3A4 and P-glycoprotein, and co-administration with strong CYP3A4 inducers or inhibitors warrants caution.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score (99.45%) to the capmatinib → rheumatoid arthritis pairing, and the HGF/c-MET mechanistic hypothesis in RA synovial biology is conceptually coherent. However, the evidence base is at L4 — no dedicated pre-clinical RA models, no clinical trials, and no direct publications — making this a hypothesis-only prediction unsuitable for clinical advancement at this stage.

**To proceed, the following is needed:**

- **Preclinical validation**: In vitro experiments using RA-FLS cell lines treated with capmatinib (proliferation, invasion, cytokine secretion assays); collagen-induced arthritis (CIA) mouse model studies to assess joint protection endpoints
- **MOA data**: Full DrugBank mechanistic annotation for capmatinib (Data Gap DG002) to strengthen the mechanistic rationale
- **Safety data**: Retrieve and review TFDA/FDA package insert warnings and contraindications (Data Gap DG001) before any clinical hypothesis development
- **RA-specific literature search**: Conduct a targeted systematic search for HGF/MET inhibition in RA across PubMed, EMBASE, and bioRxiv to identify any unpublished or grey literature evidence
- **Comparator analysis**: Review whether other MET inhibitors (crizotinib, tepotinib, savolitinib) have been studied in RA, as class-level evidence could inform capmatinib's potential
- **Registration pathway assessment**: If preclinical evidence emerges, a Singapore HSA registration strategy would be required de novo given current zero-licence status

> ⚠️ **Disclaimer**: This report is intended for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

