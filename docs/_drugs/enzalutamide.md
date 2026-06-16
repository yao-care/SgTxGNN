---
layout: default
title: Enzalutamide
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Enzalutamide
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

# Enzalutamide: From Prostate Cancer to Male Reproductive Organ Cancer

## One-Sentence Summary

Enzalutamide (Xtandi®) is a second-generation androgen receptor (AR) antagonist, originally approved internationally for the treatment of prostate cancer across multiple disease stages — from metastatic castration-sensitive prostate cancer (mCSPC) through metastatic castration-resistant prostate cancer (mCRPC).
The TxGNN model predicts with high confidence that it is effective for **Male Reproductive Organ Cancer**, supported by **over 50 clinical trials** and **20 publications**.
The most critical finding for Singapore is that Enzalutamide currently holds **zero HSA registrations**, making this a market access gap rather than an evidence gap.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (mCRPC / nmCRPC / mCSPC) — approved by FDA (2012–2019) and EMA |
| Predicted New Indication | Male Reproductive Organ Cancer |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Enzalutamide is a potent non-steroidal androgen receptor antagonist that directly targets the AR ligand-binding domain with approximately 5–8 fold higher binding affinity than first-generation anti-androgens such as bicalutamide. It simultaneously blocks three critical steps in androgen signalling: testosterone/DHT binding to AR, AR nuclear translocation, and AR–DNA/co-activator interactions. The net result is comprehensive suppression of androgen-driven gene transcription — the central driver of prostate tumour growth. Note: detailed MOA data was not available in this Evidence Pack; the above description is drawn from established clinical literature.

Male reproductive organ cancers, of which prostate adenocarcinoma is the dominant histotype, are paradigmatically dependent on AR signalling. Even in castration-resistant disease, AR remains the primary oncogenic driver through mechanisms such as AR gene amplification, ligand-binding domain mutations, and splice variants (e.g., AR-V7). This direct mechanistic alignment explains why Enzalutamide achieves clinical benefit across the full disease spectrum. The TxGNN model's 99.51% prediction confidence for male reproductive organ cancer essentially confirms the drug's established mechanism rather than proposing a novel indication.

The evidence base is exceptional. Landmark Phase 3 RCTs — AFFIRM (post-docetaxel mCRPC), PREVAIL (chemotherapy-naïve mCRPC), PROSPER (nmCRPC), ARCHES (mCSPC), and ENZAMET (mCSPC) — have each demonstrated statistically significant overall survival or metastasis-free survival benefits. It is worth noting that TxGNN's top five ranked predictions (ranks 1–4: genetic susceptibility loci, rare benign prostatic stromal tumours, Brenner tumour) all carry L5 evidence and "Hold" recommendations, reflecting knowledge-graph topological noise rather than true repurposing signals. The actionable signal sits squarely at ranks 6 and 9, where robust L1 evidence supports a Proceed with Guardrails decision.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01949337](https://clinicaltrials.gov/study/NCT01949337) | Phase 3 | Unknown | 1,311 | Randomized Phase III comparing Enzalutamide monotherapy vs. Enzalutamide + Abiraterone + Prednisone in castration-resistant metastatic prostate cancer — core high-level evidence for Enzalutamide efficacy |
| [NCT04821622](https://clinicaltrials.gov/study/NCT04821622) | Phase 3 | Active, not recruiting | 599 | TALAPRO-3: Talazoparib + Enzalutamide vs. Placebo + Enzalutamide in DDR gene-mutated mCSPC — evaluates PARP inhibitor + ARSI combination in a genomically selected population |
| [NCT05968599](https://clinicaltrials.gov/study/NCT05968599) | N/A (RWE) | Completed | 2,731 | Large real-world comparison of Enzalutamide vs. Abiraterone in chemotherapy-naïve mCRPC (Flatiron EHR database); n=2,731 strengthens external validity of Phase 3 trial findings |
| [NCT04179864](https://clinicaltrials.gov/study/NCT04179864) | Phase 1b/2 | Terminated | 102 | CELLO-1: Tazemetostat (EZH2 inhibitor) + Enzalutamide in mCRPC — exploratory epigenetic + AR dual-blockade strategy; terminated early, termination rationale unconfirmed |
| [NCT04557449](https://clinicaltrials.gov/study/NCT04557449) | Phase 1/2a | Active, not recruiting | 362 | PF-07220060 (CDK4/6 inhibitor) as single agent and in combination with Enzalutamide in advanced solid tumours including mCRPC — ongoing combination safety/efficacy study |
| [NCT02588001](https://clinicaltrials.gov/study/NCT02588001) | N/A | Completed | 60 | Japanese real-world study of Enzalutamide in nmCRPC over 5 years — provides East Asian safety and efficacy data directly relevant to Singapore clinical context |
| [NCT05914116](https://clinicaltrials.gov/study/NCT05914116) | Phase 1/2a | Recruiting | 862 | DB-1311/BNT324 (novel ADC) + Enzalutamide in advanced/metastatic solid tumours — first-in-human study expanding combination evidence in mCRPC |
| [NCT07230106](https://clinicaltrials.gov/study/NCT07230106) | Phase 2 | Recruiting | 218 | HS-20093 or SHR2554 + Novel Hormonal Agents (including Enzalutamide) in metastatic prostate cancer — assessing PK, tolerability and efficacy of novel combination |
| [NCT04033328](https://clinicaltrials.gov/study/NCT04033328) | Phase 1b | Terminated | 41 | ORIC-101 (glucocorticoid receptor antagonist) + Enzalutamide in mCRPC progressing on Enzalutamide — explores glucocorticoid-mediated resistance reversal; terminated early, limited data |
| [NCT03674814](https://clinicaltrials.gov/study/NCT03674814) | Phase 1 | Active, not recruiting | 35 | Relacorilant (glucocorticoid receptor antagonist) + Enzalutamide in mCRPC — mechanistic study addressing GR-mediated AR bypass resistance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28655021](https://pubmed.ncbi.nlm.nih.gov/28655021/) | 2017 | Review | JAMA | Comprehensive review of prostate cancer diagnosis and treatment; Enzalutamide positioned as a key second-generation AR inhibitor for advanced disease management |
| [32534790](https://pubmed.ncbi.nlm.nih.gov/32534790/) | 2020 | Review | Trends in Cancer | Rapidly evolving treatment landscape: summarises Phase 3 evidence for Enzalutamide, Abiraterone, Apalutamide, Darolutamide, Docetaxel and Radium-223; discusses optimal drug sequencing |
| [31614208](https://pubmed.ncbi.nlm.nih.gov/31614208/) | 2020 | Review | J Steroid Biochem Mol Biol | Intracrinology of androgen biosynthesis in prostate cancer; explains mechanistic basis for sustained AR signalling in CRPC and why AR-targeted therapies including Enzalutamide retain efficacy |
| [36842160](https://pubmed.ncbi.nlm.nih.gov/36842160/) | 2023 | Review | The Prostate | 3βHSD1 as a precision medicine target; 3βHSD1 activity increases after long-term Enzalutamide treatment, mediating resistance — identifies actionable co-treatment strategy |
| [37844613](https://pubmed.ncbi.nlm.nih.gov/37844613/) | 2023 | Basic Science | Nature | Inhibition of myeloid chemotaxis reverses therapy resistance in a subset of prostate cancer patients; demonstrates tumour microenvironment as a combination target alongside AR inhibition |
| [34489465](https://pubmed.ncbi.nlm.nih.gov/34489465/) | 2021 | Basic Science | Nature Communications | Single-cell ATAC + RNA sequencing identifies pre-existing resistant cell subpopulations before Enzalutamide treatment — major insight into primary resistance mechanisms and combination therapy rationale |
| [34752846](https://pubmed.ncbi.nlm.nih.gov/34752846/) | 2022 | Basic Science | Cancer Letters | Enzalutamide-induced PTH1R-mediated TGFBR2 degradation in osteoblasts confers bone microenvironment-dependent resistance in ~50% of bone-metastatic PCa — supports need for combination strategies |
| [33542074](https://pubmed.ncbi.nlm.nih.gov/33542074/) | 2021 | Basic Science | Clin Cancer Res | BCL-2 and IKKB dependencies emerge during acquired Enzalutamide resistance — identifies BCL-2 inhibition as a potential co-treatment to delay or overcome resistance |
| [33483372](https://pubmed.ncbi.nlm.nih.gov/33483372/) | 2021 | Basic Science | Cancer Research | Ferroptosis inducers (FINs) show therapeutic potential in advanced prostate cancer models; mediators SLC7A11, SLC3A2, GPX expressed in treatment-resistant disease — potential synergy with Enzalutamide |
| [32355025](https://pubmed.ncbi.nlm.nih.gov/32355025/) | 2020 | Basic Science | Science | Single-cell RNA sequencing reveals a rare Sca1+/Psca+ luminal stem-like prostate cell population surviving androgen deprivation — explains incomplete tumour elimination by AR inhibition and underpins combination strategy research |

---

## Singapore Market Information

Enzalutamide is currently **not registered** with Singapore's Health Sciences Authority (HSA). There are no product licences on record, and the drug is not commercially available through standard channels in Singapore.

For reference, Enzalutamide (Xtandi®, Astellas/Pfizer) holds the following international approvals:

| Market | Indication | Year Approved |
|--------|-----------|---------------|
| US FDA | mCRPC (post-docetaxel) | 2012 |
| US FDA | nmCRPC | 2018 |
| US FDA | mCSPC | 2019 |
| EMA | mCRPC, nmCRPC, mCSPC | 2013–2020 |
| Japan PMDA | mCRPC, nmCRPC, mCSPC | 2014–2020 |

A formal HSA registration application, potentially supported by a collaborative registration pathway leveraging existing FDA or EMA data packages, would be the most direct route to Singapore market access.

---

## Cytotoxicity

Enzalutamide is an antineoplastic agent used for the treatment of prostate cancer. It is classified as a targeted hormone therapy, not as a conventional cytotoxic chemotherapy drug.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation androgen receptor antagonist (non-steroidal; not cytotoxic) |
| Myelosuppression Risk | Low — Enzalutamide does not directly suppress bone marrow; clinically significant cytopenias are uncommon |
| Emetogenicity Classification | Low — nausea and vomiting rates in clinical trials were comparable to placebo |
| Monitoring Items | Liver function (ALT/AST), blood pressure, baseline seizure risk assessment, cognitive function and falls risk in elderly patients, PSA response |
| Handling Protection | Standard oncology medication precautions apply; not classified as a vesicant or highly hazardous cytotoxic requiring specialised chemotherapy-suite preparation |

---

## Safety Considerations

Safety data was not available in this Evidence Pack for local HSA/TFDA package insert warnings and contraindications.

Based on internationally recognised clinical trial data and regulatory labelling:

- **Seizure risk**: A known class effect; approximately 0.5% incidence in Phase 3 trials. Exercise caution or avoid in patients with a history of seizure disorder, prior brain injury, or concurrent use of seizure-threshold-lowering medications.
- **Drug-drug interactions**: Enzalutamide is a potent inducer of CYP3A4, CYP2C8, CYP2C9, and CYP2C19. Co-administered medications metabolised by these enzymes (including anticoagulants, opioids, and many cardiovascular drugs) may require dose adjustment or substitution.

Please refer to the FDA/EMA prescribing information and the future HSA-approved package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Enzalutamide carries one of the most robust oncology evidence profiles available — multiple completed Phase 3 RCTs confirming overall survival benefit across the full prostate cancer disease spectrum. The sole barrier to use in Singapore is the absence of HSA registration, not a lack of clinical evidence.

**To proceed, the following is needed:**
- Initiate HSA regulatory submission for Enzalutamide (Xtandi®), leveraging existing FDA/EMA approval dossiers via Singapore's collaborative registration pathway where applicable
- Obtain the complete local or reference-country package insert to formally document contraindications, boxed warnings, and drug interaction profile for HSA review
- Clarify reimbursability under Singapore's cancer drug list, MediShield Life, and/or Medisave framework
- Review CYP induction-mediated drug interaction risks in the intended patient population, particularly given common co-medications (anticoagulants, analgesics)
- Leverage existing East Asian safety data (Japanese nmCRPC study NCT02588001; n=60) as a pharmacovigilance reference while awaiting Singapore-specific post-marketing data
- Establish institutional seizure risk screening and monitoring protocols prior to formulary listing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

