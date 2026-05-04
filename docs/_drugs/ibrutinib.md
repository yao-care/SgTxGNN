---
layout: default
title: Ibrutinib
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
---

# Ibrutinib
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

# Ibrutinib: From B-Cell Malignancy to Monoclonal Paraproteinemia Disease

## One-Sentence Summary

Ibrutinib is a first-generation, irreversible BTK (Bruton's Tyrosine Kinase) inhibitor with established global approvals for multiple B-cell malignancies — including CLL, MCL, and Waldenström's Macroglobulinemia — but currently holds no Singapore market authorization.
The TxGNN model's highest-scored prediction is polyclonal hypergammaglobulinemia (91.75%), but with no supporting evidence (L5); the most clinically actionable prediction is **Monoclonal Paraproteinemia Disease** (principally Waldenström's Macroglobulinemia, 91.16%), backed by **13 clinical trials** including **2 completed Phase 3 RCTs** and **20 publications**.
This constitutes one of the strongest evidence bases in this repurposing dataset, with an L1 evidence level and a clear **Proceed with Guardrails** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Singapore-registered indication (drug not marketed in Singapore) |
| Predicted New Indication | Monoclonal Paraproteinemia Disease (Waldenström's Macroglobulinemia) |
| TxGNN Prediction Score | 91.16% |
| Evidence Level | L1 (2 completed Phase 3 RCTs: iNNOVATE and ASPEN) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ibrutinib is a small-molecule, covalent, irreversible inhibitor of Bruton's Tyrosine Kinase (BTK) — a non-receptor tyrosine kinase that acts as a critical signal hub downstream of the B-cell receptor (BCR). By permanently binding to the C481 cysteine residue within BTK's ATP-binding pocket, ibrutinib blocks multiple downstream survival cascades including NF-κB, PI3K/AKT, and ERK, all of which are essential for the proliferation and survival of malignant B cells. Although detailed DrugBank MOA data was not retrieved in this evidence pack, ibrutinib's mechanism is extensively characterized in over 20 peer-reviewed publications identified in this dataset and underpins its multiple global regulatory approvals.

Waldenström's Macroglobulinemia (WM), the dominant disease entity within the "monoclonal paraproteinemia disease" classification, offers an exceptionally strong mechanistic justification for ibrutinib. Over 90% of WM tumor cells carry the MYD88 L265P somatic mutation, which constitutively activates the IRAK1/4 → BTK → NF-κB signaling axis, driving both tumor survival and pathological monoclonal IgM hypersecretion. An additional 35–40% of WM patients harbor CXCR4 WHIM-type mutations that modulate disease trafficking and alter BTK inhibitor response profiles. By targeting BTK — the convergence point of both BCR-dependent and MYD88-dependent pathways — ibrutinib achieves dual blockade highly specific to WM's molecular pathogenesis.

This mechanistic rationale is fully validated by clinical evidence. The iNNOVATE Phase 3 RCT demonstrated superior progression-free survival with ibrutinib plus rituximab versus rituximab alone, and ibrutinib subsequently received FDA approval for WM in 2015 (relapsed/refractory) and 2018 (treatment-naïve). The ASPEN Phase 3 head-to-head comparison further confirmed ibrutinib as the efficacy benchmark for the BTK inhibitor class in WM. For Singapore, ibrutinib's absence from the local market represents a regulatory gap rather than any scientific or clinical uncertainty, and a submission to the Health Sciences Authority could draw directly on this internationally accepted evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02165397](https://clinicaltrials.gov/study/NCT02165397) | Phase 3 | Completed | 181 | iNNOVATE: Randomized double-blind RCT of ibrutinib + rituximab vs placebo + rituximab in WM; pivotal trial establishing ibrutinib as standard of care |
| [NCT03053440](https://clinicaltrials.gov/study/NCT03053440) | Phase 3 | Completed | 201 | ASPEN: Zanubrutinib vs ibrutinib head-to-head in MYD88-mutated WM; confirms ibrutinib efficacy benchmark while showing zanubrutinib's improved safety profile |
| [NCT04061512](https://clinicaltrials.gov/study/NCT04061512) | Phase 2/3 | Recruiting | 148 | RAINBOW: Ibrutinib + rituximab vs DRC (dexamethasone, rituximab, cyclophosphamide) as initial therapy for WM; evaluating chemotherapy-free first-line strategy |
| [NCT04840602](https://clinicaltrials.gov/study/NCT04840602) | Phase 2 | Recruiting | 92 | Three-arm study comparing ibrutinib + rituximab vs zanubrutinib alone vs venetoclax + rituximab in previously untreated WM/LPL |
| [NCT03620903](https://clinicaltrials.gov/study/NCT03620903) | Phase 2 | Active, not recruiting | 53 | BRI triple regimen (Bortezomib + Rituximab + Ibrutinib) as first-line therapy in treatment-naïve WM; evaluating a highly active combination approach |
| [NCT04062448](https://clinicaltrials.gov/study/NCT04062448) | Phase 2 | Completed | 16 | Ibrutinib + rituximab in Japanese WM patients (treatment-naïve and relapsed/refractory); ORR assessed by Independent Review Committee — Asia-specific safety and efficacy data |
| [NCT07169565](https://clinicaltrials.gov/study/NCT07169565) | Phase 1 | Not yet recruiting | 21 | Time-limited therapy: Ibrutinib induction followed by bendamustine + rituximab (BR) in WM; 3+3 dose-escalation to identify MTD and explore fixed-duration strategies |
| [NCT01479842](https://clinicaltrials.gov/study/NCT01479842) | Phase 1 | Active, not recruiting | 48 | Rituximab + bendamustine + ibrutinib (RBI) in relapsed B-cell NHL including WM; dose-escalation study establishing combination safety and optimal dosing |
| [NCT02332980](https://clinicaltrials.gov/study/NCT02332980) | Phase 2 | Completed | 65 | Pembrolizumab ± idelalisib or ibrutinib in relapsed/refractory CLL and low-grade B-cell NHL; exploratory combination immunotherapy study, ibrutinib as adjunct arm |
| [NCT02950220](https://clinicaltrials.gov/study/NCT02950220) | Phase 1 | Completed | 2 | Pembrolizumab + ibrutinib in relapsed/refractory NHL; early-phase safety signal generation for checkpoint inhibitor + BTK inhibitor combination |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [32731259](https://pubmed.ncbi.nlm.nih.gov/32731259/) | 2020 | RCT (Phase 3, ASPEN) | Blood | ASPEN trial: Zanubrutinib vs ibrutinib in MYD88-mutated WM; ibrutinib achieves robust responses; zanubrutinib shows higher VGPR rate and better cardiac safety — establishes ibrutinib's efficacy baseline |
| [38315878](https://pubmed.ncbi.nlm.nih.gov/38315878/) | 2024 | Post-hoc Analysis | Blood Advances | ASPEN biomarker analysis: MYD88/CXCR4/BTK mutation profiling from 190 bone marrow samples; identifies molecular predictors of differential response to ibrutinib vs zanubrutinib |
| [34911327](https://pubmed.ncbi.nlm.nih.gov/34911327/) | 2021 | Review | Klinicka Onkologie | WM disease overview: lymphoplasmacytic infiltration, IgM-related complications (hyperviscosity, neuropathy, cryoglobulinemia), and BTK inhibitor-based modern therapy |
| [29169431](https://pubmed.ncbi.nlm.nih.gov/29169431/) | 2017 | Review | Deutsches Ärzteblatt Int | Systematic differential diagnosis of IgM monoclonal gammopathy (3.2–3.5% of adults >50); distinguishing WM from MGUS and other IgM-secreting conditions with different therapeutic implications |
| [34674984](https://pubmed.ncbi.nlm.nih.gov/34674984/) | 2022 | Clinical Review | Clin Lymphoma Myeloma Leuk | Bing-Neel syndrome (CNS manifestation of WM): diagnostic approach via CSF MYD88 analysis; ibrutinib's CNS penetration makes it the preferred treatment for this rare extramedullary complication |
| [34610502](https://pubmed.ncbi.nlm.nih.gov/34610502/) | 2021 | Review | J Neuroimmunology | Anti-MAG neuropathy: acquired demyelinating neuropathy driven by IgM paraprotein; BTK inhibition emerging as therapeutic strategy targeting the underlying B-cell clone |
| [25679974](https://pubmed.ncbi.nlm.nih.gov/25679974/) | 2015 | Review | Clin Adv Hematol Oncol | Pre-ibrutinib era WM survival data (5-year OS: 87%/68%/36% by risk group) and treatment landscape; provides baseline context for quantifying the ibrutinib era improvement |
| [27825468](https://pubmed.ncbi.nlm.nih.gov/27825468/) | 2016 | Review | Best Pract Res Clin Haematol | Novel therapeutic targets in WM: MYD88 signaling, BCR pathway, CXCR4 axis; mechanistic rationale for ibrutinib and emerging targeted combinations in WM |
| [39859314](https://pubmed.ncbi.nlm.nih.gov/39859314/) | 2025 | Review | Int J Mol Sci | Schnitzler syndrome (urticaria + monoclonal IgM + systemic inflammation): NLRP3-driven autoinflammatory condition associated with IgM paraproteinemia; BTK role in sustaining the secreting B-cell clone |
| [33297772](https://pubmed.ncbi.nlm.nih.gov/33297772/) | 2020 | Review | Expert Rev Hematol | Zanubrutinib for WM: comparative review of BTK inhibitor selectivity and toxicity profiles; contextualizes ibrutinib's established position vs next-generation alternatives |

---

## Singapore Market Information

Ibrutinib is currently **not registered** in Singapore. There are no Health Sciences Authority (HSA) drug authorizations on file.

> Ibrutinib holds regulatory approval in major international markets including FDA (USA) for WM (2015 relapsed/refractory; 2018 treatment-naïve), CLL/SLL, MCL, and MZL, and EMA approval for the same indications in the European Union. An HSA submission could leverage these established international dossiers through an abbreviated or reference-product regulatory pathway.

---

## Cytotoxicity

Ibrutinib is classified as an antineoplastic agent (targeted oral kinase inhibitor for B-cell malignancies). Classification criteria met: the drug targets oncogenic signaling in lymphoid cancers and is approved under antineoplastic drug frameworks globally.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — covalent, irreversible small molecule BTK kinase inhibitor (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low to moderate; neutropenia and thrombocytopenia are reported but less severe than traditional chemotherapy; Grade 3+ cytopenias occur in approximately 10–20% of patients on long-term therapy |
| Emetogenicity Classification | Low (oral formulation; ibrutinib carries minimal emetogenic potential per MASCC/ESMO classification) |
| Monitoring Items | Complete blood count with differential (for cytopenias); liver function tests; renal function; cardiac monitoring including ECG and blood pressure for atrial fibrillation and hypertension; bleeding risk assessment at each visit |
| Handling Protection | Standard oral antineoplastic precautions apply; no inhalation or dermal hazard from intact capsule/tablet; caregivers should avoid crushing, breaking, or opening capsules without protective equipment |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (iNNOVATE and ASPEN) provide robust L1-level evidence for ibrutinib's efficacy in Waldenström's Macroglobulinemia, and existing FDA/EMA approvals confirm its clinical validity at the international level; the primary barrier for Singapore patients is the absence of an HSA registration rather than any scientific uncertainty.

**To proceed, the following is needed:**
- **Regulatory submission**: Prepare an HSA marketing authorization application for ibrutinib for WM, drawing on the established FDA/EMA data package; evaluate eligibility for an abridged or reference-product dossier pathway
- **Safety documentation**: Retrieve the full prescribing information / package insert to document approved warnings, contraindications, and drug interactions — this is currently the sole blocking data gap
- **Patient stratification plan**: Confirm availability of MYD88 L265P and CXCR4 mutation testing in Singapore diagnostic laboratories for appropriate patient selection and response prediction
- **Cardiac risk management protocol**: Develop a monitoring and management framework for atrial fibrillation (estimated 2-year incidence ~16%) and major bleeding risk, which are the two primary safety guardrails for ibrutinib therapy
- **Indication scope decision**: Determine whether to submit for WM alone or pursue a combined portfolio application covering CLL/SLL, MCL, and MZL — all with existing L1 global evidence — to maximize patient access in a single regulatory cycle
- **Health technology assessment**: Evaluate cost-effectiveness within the Singapore healthcare context and potential inclusion in national cancer drug lists or formulary, particularly given the high treatment cost associated with continuous BTK inhibitor therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

