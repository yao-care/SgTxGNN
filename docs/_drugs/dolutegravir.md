---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
---

# Dolutegravir
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

# Dolutegravir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Dolutegravir (DTG) is a second-generation integrase strand transfer inhibitor (INSTI), originally developed and globally approved for the treatment of HIV-1 infection in adults and children.
The TxGNN model ranks **Simian Immunodeficiency Virus (SIV) Infection** as its top predicted new indication (score: 99.85%), supported by **1 clinical trial** and **15 publications** — though this primarily reflects DTG's established use in SIV-based animal models rather than a genuinely novel repurposing.
Of note, two clinically meaningful HIV-spectrum indications further down the ranked list — **AIDS-Related Complex** (rank 5) and **Congenital HIV Infection** (rank 6) — both carry L1 evidence and a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (no Singapore registration; inferred from drug class — INSTI) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Dolutegravir inhibits HIV integrase, the enzyme responsible for inserting viral cDNA into the host cell genome — a step without which HIV cannot replicate. DTG binds tightly to the integrase–DNA complex, slowing dissociation and creating a high genetic barrier to resistance. This mechanism has made DTG the cornerstone of WHO-preferred first-line HIV treatment since 2019.

SIV (Simian Immunodeficiency Virus) belongs to the same Lentivirus genus as HIV and shares high structural homology at the integrase active site. In vitro studies have demonstrated that SIV is susceptible to all major INSTIs, and HIV integrase resistance mutations introduced into SIVmac239 produce phenotypically comparable effects. This conservation of the integrase target makes DTG's mechanism directly applicable to SIV biology.

Crucially, this prediction captures an established research paradigm rather than a novel clinical opportunity. SIV-infected non-human primate (NHP) models — particularly rhesus macaques infected with SIVmac239 or SIVmac251 — serve as the standard pre-clinical platform for HIV eradication research, CNS reservoir studies, long-acting ART evaluation, and resistance profiling. DTG-containing regimens are routinely employed in these models. The TxGNN score of 99.85% most likely reflects the deep biological co-occurrence of DTG and SIV in the knowledge graph, rather than a prediction of a previously unexplored therapeutic axis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Evaluated vedolizumab + ART to achieve virological remission in HIV-infected subjects without prior ART. DTG was used as background ART, not as the primary investigational agent. Relevance to SIV is indirect (HIV/ART context only). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30381490](https://pubmed.ncbi.nlm.nih.gov/30381490/) | 2019 | Preclinical animal study | Journal of Virology | DTG monotherapy in SIV-infected macaques selects for resistance mutations with variable virological outcomes; confirms in vivo INSTI–SIV interaction |
| [36365101](https://pubmed.ncbi.nlm.nih.gov/36365101/) | 2022 | Preclinical PK validation | Pharmaceutics | Pharmacological validation of long-term DTG-containing ART (TDF+FTC+DTG) in SIVmac251-infected macaques; confirms adequate drug exposure and viral suppression |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Comparative preclinical | AIDS Research and Human Retroviruses | Compared novel coformulated cART regimens including DTG in SIVmac239-infected rhesus macaques; demonstrated clinically relevant viral suppression |
| [40093003](https://pubmed.ncbi.nlm.nih.gov/40093003/) | 2025 | Preclinical neuroimaging | Frontiers in Immunology | DTG-containing cART modulates extracellular water distribution and white matter tract integrity in SIV-infected macaques; insights into CNS reservoir and neurorepair |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Preclinical | mBio | Lentiviral persistence in brain despite ART including DTG; parallel findings across HIV-1, HIV-2, and SIV brain reservoir models |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | Preclinical resistance profiling | Journal of Virology | Characterized INSTI resistance profiles including DTG in SIVmac239; tissue culture selection yielded mutations paralleling those in HIV |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | Preclinical resistance | Journal of Virology | HIV integrase resistance mutations (RAL, EVG, DTG) introduced into SIVmac239 show comparable susceptibility changes; validates SIV as resistance model |
| [25583721](https://pubmed.ncbi.nlm.nih.gov/25583721/) | 2015 | Preclinical | Antimicrobial Agents and Chemotherapy | Simian-tropic HIV as a model for studying INSTI resistance including DTG; bridges HIV and SIV resistance research |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Structural review | FEBS Journal | HIV/SIV intasome crystal structures illuminate how DTG binds integrase and how resistance mutations impair binding; mechanistic foundation for both viruses |
| [28576126](https://pubmed.ncbi.nlm.nih.gov/28576126/) | 2017 | Veterinary case report | Retrovirology | Effective treatment of SIVcpz-induced immunodeficiency in a captive western chimpanzee; demonstrates real-world INSTI efficacy against SIV-related disease |

---

## Singapore Market Information

Dolutegravir is **not currently registered in Singapore**. No product authorizations were identified in the Health Sciences Authority (HSA) database.

For international context, DTG is widely marketed under the following product names and has received approval from the FDA, EMA, and WHO prequalification:

| Product | Combination | Primary Indication |
|---------|------------|-------------------|
| Tivicay® | DTG 50 mg (monotherapy) | HIV-1 infection, adults and pediatric ≥4 weeks |
| Triumeq® | DTG/abacavir/lamivudine | HIV-1 infection, adults and children ≥25 kg |
| Dovato® | DTG/lamivudine | HIV-1 infection, adults (2-drug regimen) |
| Juluca® | DTG/rilpivirine | HIV-1 infection, virologically suppressed adults |

Any future Singapore registration would require submission of a full dossier to HSA under the Drug Registration Framework.

---

## Safety Considerations

Please refer to the package insert for safety information.

Formal Singapore-specific warning and contraindication data is unavailable (Dolutegravir is not registered locally). Internationally recognized safety considerations from regulatory authorities include:

- **Neuropsychiatric effects**: Insomnia, depression, suicidality — particularly in patients with pre-existing psychiatric conditions
- **Weight gain**: Clinically significant weight increase reported, especially with TAF-based combinations
- **Neural tube defect signal**: A 2018 Botswana signal raised concern about neural tube defects with periconceptional DTG exposure. Subsequent large studies (including Tsepamo follow-up) showed a low absolute risk (~0.1–0.3%) comparable to background rates, but informed consent for women of reproductive potential remains recommended
- **Hepatotoxicity**: Rare; caution in patients with hepatitis B or C co-infection
- **Drug interactions**: DTG is affected by polyvalent cation-containing products (antacids, iron, calcium supplements) which reduce absorption; must be separated by at least 2–6 hours

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The top TxGNN prediction (SIV infection, L3) represents an established animal model application, not a novel therapeutic repurposing. DTG's use in SIV-infected NHP models is already standard practice in HIV research and requires no further regulatory or clinical development framing. The more actionable clinical signals in this pipeline are **AIDS-Related Complex** (rank 5, L1) and **Congenital HIV Infection / Vertical Transmission Prevention** (rank 6, L1), both of which represent extensions of DTG's existing HIV indication with well-established evidence bases and "Proceed with Guardrails" recommendations.

**To proceed, the following is needed:**

- **Regulatory gap**: Submit Singapore HSA registration dossier if local market entry is intended; Dolutegravir has no current HSA registration
- **Data gap — MOA**: Retrieve DTG mechanism of action documentation from DrugBank (DG002, high severity)
- **Data gap — Safety**: Obtain TFDA or reference-country package insert to resolve blocking DG001 (warnings, contraindications)
- **For SIV research use**: No additional development required; SIV-NHP model applications are already active in the literature
- **For AIDS-Related Complex / Congenital HIV (the stronger repurposing signals)**:
  - Confirm Singapore patient population need and current treatment gaps
  - Develop local safety monitoring protocol for neuropsychiatric effects and weight gain
  - For maternal/pediatric use: implement neural tube defect risk counselling and folic acid supplementation protocols
  - Engage HSA for accelerated review given WHO-preferred status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

