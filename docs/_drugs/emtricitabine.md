---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 368
evidence_level: L5
indication_count: 10
---

# Emtricitabine
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

# Emtricitabine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Emtricitabine (FTC) is a nucleoside reverse transcriptase inhibitor (NRTI) globally established for HIV-1 treatment and pre-exposure prophylaxis (PrEP), though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with **2 clinical trials** (both of limited relevance) and **20 publications** (predominantly non-human primate animal studies) supporting this direction.
Importantly, SIV infection serves as the standard bridging animal model for HIV drug development — this prediction reflects mechanistic validation rather than a conventional new therapeutic indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally used for HIV-1 treatment and PrEP |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Emtricitabine is a fluorinated cytidine analogue that competitively inhibits the HIV-1 reverse transcriptase enzyme and is incorporated into nascent viral DNA, causing chain termination. As a core NRTI, FTC is the backbone of many first-line antiretroviral regimens — including Truvada® (FTC/TDF) and Descovy® (FTC/TAF) — and is FDA-approved for both HIV treatment and PrEP.

The mechanistic basis for this prediction lies in the high sequence homology between SIV reverse transcriptase and HIV-1 RT, estimated at approximately 60–70%. Non-human primate (NHP) models — using rhesus macaques infected with SIV or chimeric SHIV strains — are the accepted preclinical platform for evaluating antiretroviral pharmacokinetics, PrEP efficacy, viral reservoir dynamics, and drug resistance. FTC alone and in combination with TDF or TAF has been extensively validated in these systems across more than two decades of research.

It is important to interpret this prediction in context: SIV infection in macaques is a mechanistic validation platform and translational research tool, not a standalone clinical indication. The TxGNN model's high score almost certainly reflects the structural and functional parallels between HIV-1 and SIV lentiviruses, and FTC's well-characterized activity against reverse transcriptases of this virus family broadly — rather than signalling an untested new therapeutic use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Investigates Vedolizumab + ART for sustained HIV virological remission. FTC is a background ART component, not the primary study drug. Study concerns human HIV, not SIV; status is Unknown. |
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Withdrawn | 0 | Designed to study raltegravir decay kinetics in HIV; referenced SIV macaque data for comparison. Never enrolled any participants — not applicable. |

> Neither trial is directly designed to evaluate Emtricitabine in SIV infection as a primary endpoint. Both have significant limitations (off-target drug, withdrawn/unknown status). No clinical trials specifically targeting SIV infection as a human therapeutic indication are registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Animal study | *Nature Communications* | Oral FTC/TAF combined with long-acting cabotegravir/rilpivirine achieved SHIV remission in macaques with early ART initiation; explored immune adjuvants for viral reservoir clearance. |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Animal study (NHP PrEP) | *J Infectious Diseases* | TAF alone or TAF/FTC combination prevented vaginal SHIV acquisition in macaques; combination showed additive protection over monotherapy. |
| [29788316](https://pubmed.ncbi.nlm.nih.gov/29788316/) | 2018 | Animal study (NHP PrEP) | *J Infectious Diseases* | Intravaginal FTC/TFV gel provided dual rectal and vaginal compartment protection against SHIV in macaques, supporting a cross-compartment PrEP concept. |
| [29466356](https://pubmed.ncbi.nlm.nih.gov/29466356/) | 2018 | Virology study | *PloS ONE* | RT and integrase resistance mutations emerged in SIV-infected macaques on non-suppressive TDF/FTC + raltegravir, mirroring resistance patterns seen in human HIV. |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal study (NHP PrEP) | *J Infectious Diseases* | Oral FTC/TAF fully protected macaques from rectal SHIV over 19 weekly exposures; high intracellular drug concentrations in lymphoid tissue confirmed. |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal study (NHP PrEP) | *J Infectious Diseases* | Oral FTC/TDF maintained prophylactic efficacy in macaques coinfected with *Chlamydia trachomatis* and *Trichomonas vaginalis*, despite local genital inflammation. |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | Animal study (NHP vaccine+PrEP) | *AIDS Res Human Retroviruses* | Combined VLP HIV vaccine with partial oral FTC/TDF PrEP prevented SHIV infection in macaques and primed virus-amplified immunity — supporting combined biomedical prevention strategies. |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Animal study (NHP PrEP) | *J Infectious Diseases* | FTC/TDF provided partial protection against a TDF-resistant SHIV carrying the K65R mutation; the FTC component contributed independent antiviral activity. |
| [18216122](https://pubmed.ncbi.nlm.nih.gov/18216122/) | 2008 | Animal study (SIVagm) | *Journal of Virology* | ART (tenofovir + FTC) suppressed SIVagm in African green monkeys; study revealed that long-lived infected cells, not rapid replication, sustain the reservoir in natural SIV hosts. |
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | Virology study | *Journal of Virology* | M184V resistance mutation emerged within 5 weeks in SIVmac251-infected macaque neonates receiving FTC or 3TC, directly mirroring rapid M184V emergence seen in human HIV-1 during 3TC therapy. |

---

## Singapore Market Information

Emtricitabine is **not currently registered or marketed in Singapore**. No Health Sciences Authority (HSA) product authorizations exist for any emtricitabine-containing product based on the current dataset.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | No registered products | — | — |

> While combination products containing Emtricitabine (e.g., Truvada®, Descovy®, Biktarvy®) may be accessible in Singapore through special channels (e.g., Special Access Route, private importation), no HSA product licenses are on record in this dataset. Any clinical use would require regulatory pathway evaluation.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The TxGNN model's top prediction of Emtricitabine for SIV infection reflects an expected pharmacological relationship rather than a clinically novel repurposing opportunity. SIV-infected NHP models are the established preclinical platform for HIV drug development, and FTC's activity in these models is already well-documented as part of its core translational research role. The 20 supporting publications are exclusively animal studies, and the 2 matched clinical trials are not designed to evaluate SIV infection as a clinical endpoint. This is not a new indication in the conventional sense — it is the drug's existing mechanism operating in a parallel viral context used for research purposes.

Of note, two higher-ranked clinical predictions from this same Evidence Pack carry substantially stronger clinical evidence and may represent more actionable drug repurposing opportunities:

- **AIDS-related Complex** (Rank #5, L1 evidence, "Proceed with Guardrails") — with multiple Phase 2/3 trials and FTC's established role as an NRTI core drug for HIV spectrum disease
- **Congenital HIV Infection** (Rank #6, L1 evidence, "Proceed with Guardrails") — supported by FTC/TDF use in PMTCT protocols, maternal pharmacokinetic data, and Phase 3 RCTs in pregnant women

**To proceed, the following is needed:**
- Clarify the research objective: if the aim is translational HIV research using NHP models, current animal study evidence is sufficient; if a formal new clinical indication is sought, SIV infection is not applicable to human medicine
- Obtain formal MOA documentation from DrugBank (currently a data gap)
- Pursue HSA Singapore registration for FTC-containing products if clinical deployment is planned
- Review the full prescribing information / package insert for complete safety profiling
- Prioritise evaluation of **AIDS-related Complex (Rank #5)** and **Congenital HIV (Rank #6)** as the most clinically actionable repurposing candidates from this dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

