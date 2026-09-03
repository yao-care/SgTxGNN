---
layout: default
title: Tenofovir Alafenamide
parent: 僅模型預測 (L5)
nav_order: 953
evidence_level: L5
indication_count: 10
---

# Tenofovir Alafenamide
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

# Tenofovir Alafenamide: From HIV/Hepatitis B Antiviral Therapy to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Tenofovir alafenamide (TAF) is a nucleotide reverse transcriptase inhibitor prodrug that forms the backbone of modern antiretroviral (HIV) and anti-hepatitis B regimens.
> In this evidence pack, the TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection**,
> but this is supported by only **1 clinical trial** (of doubtful relevance) and **9 preclinical macaque/animal-model publications** — evidence that does not translate into an actionable human indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (TAF is not registered/marketed in Singapore, so no local approved-indication text exists; regulatory `licenses` list is empty) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 (preclinical/mechanistic studies only) |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for TAF is not available in the structured drug record of this evidence pack (flagged as a High-severity data gap, DG002). Based on the mechanistic notes captured in the evidence review, TAF is a prodrug of tenofovir that inhibits the reverse transcriptase of retroviruses. Since both SIV and HIV are lentiviruses, there is a theoretical mechanistic rationale for antiviral activity against SIV.

However, SIV is, by definition, a **non-human primate pathogen** — it does not naturally infect humans and has no corresponding human clinical indication. All nine supporting publications are preclinical macaque/SHIV (simian-human immunodeficiency virus) chemoprophylaxis or PrEP models, used to inform *human* HIV prevention strategy rather than to treat SIV itself. The single associated clinical trial (NCT03577782) was independently graded **"C" relevance** by the evidence reviewer — it is actually a human HIV trial of vedolizumab plus antiretroviral therapy that appears to have been linked to this disease entity through keyword overlap, not a genuine SIV study.

In short, this is very likely a knowledge-graph embedding artifact: TAF's genuine, well-established mechanistic and clinical relationship is with **human HIV-1 and chronic hepatitis B**, and the model has generalized this relationship to a mechanistically adjacent but non-human disease entity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Human HIV trial of vedolizumab + antiretroviral therapy aiming for virological remission after ART interruption. Reviewer-graded "C" relevance: likely linked to SIV via keyword overlap rather than being a genuine SIV/animal study. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Animal model (SHIV remission) | Nature Communications | Early ART initiation with oral FTC/TAF plus long-acting cabotegravir/rilpivirine achieved SHIV remission in macaques |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Animal model | J Infect Dis | TAF/elvitegravir vaginal inserts gave extended post-exposure protection against SHIV in macaques |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Animal model (humanized mouse) | Frontiers in Immunology | Dual-purpose humanized mouse model proposed for testing antiviral strategies against SIV and HIV |
| [35913838](https://pubmed.ncbi.nlm.nih.gov/35913838/) | 2022 | Animal model (implant) | J Antimicrob Chemother | Biodegradable TAF-releasing implant provided vaginal protection against SHIV in macaques |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Animal model | J Infect Dis | Oral TAF alone or with emtricitabine protected macaques against vaginal SHIV infection |
| [31730629](https://pubmed.ncbi.nlm.nih.gov/31730629/) | 2019 | Methodology (animal) | PLoS ONE | Protocol for training rhesus macaques to reliably take daily oral ARVs for preclinical SHIV studies |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal model (chemoprophylaxis) | J Infect Dis | Oral FTC/TAF chemoprophylaxis protected macaques from rectal SHIV infection |
| [22740713](https://pubmed.ncbi.nlm.nih.gov/22740713/) | 2012 | Animal model | J Infect Dis | Oral PrEP reduced inflammation and CD4 loss in macaques with breakthrough acute SHIV infection |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Animal model | JAIDS | Oral TDF and topical TAF prodrug (GS-7340) protected infant macaques against repeated oral SIV challenge |

All nine publications are non-human primate (macaque) preclinical studies; none report treatment of established SIV infection in a clinical setting, and none are directly translatable to a human disease indication.

---

## Singapore Market Information

Currently no Singapore registrations exist for tenofovir alafenamide in this dataset (`market_status`: Not Marketed, `total_licenses`: 0).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not available in this evidence pack — flagged as a **Blocking** data gap, DG001, requiring TFDA/HSA package-insert retrieval before any S1 safety review can proceed.)

---

## Full List of Predicted Indications in This Evidence Pack (Reference)

This evidence pack is a multi-candidate report (`candidate_id: TW-DB09299-multi`). For transparency, all 10 TxGNN-predicted indications and their internal scoring are summarized below — several are of materially higher clinical interest than the rank-1 candidate discussed above:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|-------------|-----------------|-----------------|------|
| 1 | Simian immunodeficiency virus infection | 99.89% | L4 | Hold | Non-human disease; see analysis above |
| 2 | Feline acquired immunodeficiency syndrome | 99.89% | L5 | Hold | No trials/literature; veterinary, not human-applicable |
| 3 | Neurodevelopmental disorder (ataxic gait/absent speech) | 99.87% | L5 | Hold | No mechanistic link; likely embedding false positive |
| 4 | Chronic hepatitis C virus infection | 98.60% | L4 | Hold | HCV has no reverse-transcriptase step; TAF has no direct anti-HCV activity — trials are DDI/co-infection studies only |
| 5 | Familial combined hyperlipidaemia (obsolete term) | 97.80% | L5 | Hold | Obsolete disease term; no mechanistic or evidentiary link |
| 6 | Congenital human immunodeficiency virus | 97.06% | **L1** | **Proceed with Guardrails** | Reflects TAF's established role in perinatal HIV/PMTCT — not a novel indication |
| 7 | AIDS related complex | 97.06% | **L1** | **Proceed with Guardrails** | Older terminology for HIV/AIDS disease spectrum — not a novel indication |
| 8 | Hepatitis B virus infection | 96.14% | **L1** | **Proceed with Guardrails** | **Already an approved TAF indication (Vemlidy)** — confirms model validity, not a repurposing opportunity |
| 9 | Hepatitis C virus infection (duplicate entry) | 96.12% | L4 | Hold | Same limitation as rank 4 |
| 10 | Hepatitis E virus infection | 94.99% | L4 | Hold | HEV has no reverse-transcriptase step; supporting trials/literature are mislabeled HBV studies |

**Key pattern**: the highest-evidence candidates (ranks 6–8) are not genuinely *new* indications — they restate TAF's already-approved uses (HIV treatment/prevention, chronic hepatitis B) under different disease terminology. The nominally "novel" candidates (ranks 1–5, 9–10) either lack mechanistic plausibility, lack any supporting evidence, or rely on evidence that does not actually support the stated indication. **No genuinely actionable new indication was identified in this batch.**

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The rank-1 TxGNN prediction (SIV infection) is a non-human disease with no translatable clinical evidence; its sole associated trial is very likely a mislabeling artifact.
- Across the full candidate set, indications with strong (L1) evidence turn out to be restatements of TAF's already-approved uses (HIV, hepatitis B) rather than true repurposing opportunities, while genuinely novel candidates have no credible mechanistic or clinical support.

**To proceed, the following is needed:**
- Formal MOA documentation for TAF (DG002)
- TFDA/HSA package insert retrieval to resolve the Blocking safety data gap (DG001) before any S1 safety review
- If repurposing is still of interest, a targeted re-screen of TxGNN outputs excluding already-approved indications and non-human disease entities, to surface genuinely novel, human-relevant candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

