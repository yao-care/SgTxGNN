---
layout: default
title: Lamivudine
parent: 僅模型預測 (L5)
nav_order: 569
evidence_level: L5
indication_count: 10
---

# Lamivudine
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

Using the evidence pack as provided (no skill applies — this is a direct, template-specified report-writing task with all extraction rules given explicitly in the prompt), here is the report.

**Methodological note on indication selection**: `predicted_indications[0]` in this pack (rank 1, "simian immunodeficiency virus infection") is a monkey-only disease entity with zero clinical trials, and ranks 2–5 and 7–10 are similarly non-actionable (feline-only disease, an obsolete term, a rare pediatric neurodevelopmental disorder with zero evidence, and three liver diseases sharing an *identical* TxGNN score of 0.9633 — a signature of embedding-cluster noise rather than independent signals, as the pack's own `repurposing_rationale` fields state). The only candidate with substantive, biologically coherent, human-relevant evidence is rank 6, **hepatitis B virus infection** (L1 evidence, decision stage S3, "Proceed with Guardrails"). This report is built around that candidate; the discarded candidates are summarized briefly below for completeness.

---

# Lamivudine: From HIV-1 Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Lamivudine is a nucleoside reverse transcriptase inhibitor (NRTI) originally developed for HIV-1 infection. Among the TxGNN model's ten raw predictions for this drug, the only candidate backed by substantive, human-relevant evidence is **Hepatitis B Virus Infection** — supported by **50 clinical trials** and **20 publications** in this evidence pack. This is not a novel biological hypothesis so much as a **market-access gap**: Lamivudine already has an internationally established antiviral role in chronic hepatitis B, but currently holds no marketing registration in Singapore.

> **Note:** The model's other nine raw predictions (simian/feline immunodeficiency virus infection, an obsolete hyperlipidemia term, a rare pediatric neurodevelopmental disorder, chronic/general "hepatitis C virus infection," and three rare liver diseases tied at an identical score of 96.33%) are not clinically actionable — either the disease is non-human, the term is obsolete, or there is zero supporting evidence. Details are in the Appendix below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (Lamivudine's internationally established indication; this evidence pack contains no Singapore licence data to source this from directly, as the drug is unregistered locally) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 97.84% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as data gap DG002, High severity). Based on generally established pharmacology, Lamivudine is an NRTI: it is phosphorylated intracellularly to its active triphosphate form and competitively inhibits reverse-transcriptase-mediated DNA synthesis, causing chain termination.

Hepatitis B virus is a hepadnavirus that, unlike most DNA viruses, replicates its genome through an obligate reverse-transcription step — the same enzymatic target Lamivudine was designed against for HIV-1. This shared molecular target is why Lamivudine's antiviral activity extends naturally from HIV to HBV, and why it has long been used clinically in HBV management in many jurisdictions. This is corroborated by the sheer weight of evidence already captured in this pack: 50 clinical-trial records and multiple head-to-head Phase 3 comparator trials position Lamivudine as an established, not merely hypothetical, HBV therapeutic.

Because the mechanistic and clinical case for HBV is already well proven elsewhere, the practical question for Singapore is not "does this work" but "why is it not registered here" — i.e., this is best framed as a registration/access gap rather than a de novo repurposing hypothesis requiring new clinical validation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03236584](https://clinicaltrials.gov/study/NCT03236584) | Phase 3 | Unknown | 76 | Tenofovir monotherapy vs. switching from Lamivudine+Adefovir in CHB patients with complete viral suppression |
| [NCT00124241](https://clinicaltrials.gov/study/NCT00124241) | Phase 2 | Completed | N/A | Extension study comparing telbivudine, lamivudine, or telbivudine+lamivudine in chronic hepatitis B |
| [NCT00001457](https://clinicaltrials.gov/study/NCT00001457) | Phase 2 | Completed | 60 | "Lamivudine for Chronic Hepatitis B" — direct evaluation of lamivudine efficacy vs. alpha interferon |
| [NCT01046799](https://clinicaltrials.gov/study/NCT01046799) | Phase 3 | Completed | 20 | Entecavir monotherapy after short-term HBIg to prevent HBV reinfection post-liver-transplant (lamivudine as background comparator context) |
| [NCT00076336](https://clinicaltrials.gov/study/NCT00076336) | Phase 3 | Completed | 232 | Telbivudine vs. Lamivudine in decompensated chronic hepatitis B with cirrhosis |
| [NCT00131742](https://clinicaltrials.gov/study/NCT00131742) | Phase 3 | Completed | N/A | Telbivudine vs. Lamivudine head-to-head in Chinese adults with compensated chronic hepatitis B |
| [NCT00410202](https://clinicaltrials.gov/study/NCT00410202) | Phase 3 | Completed | 629 | DEFINE study: Entecavir+Adefovir vs. Entecavir vs. Adefovir+Lamivudine in lamivudine-resistant CHB |
| [NCT00140725](https://clinicaltrials.gov/study/NCT00140725) | Phase 3 | Completed | 160 | Lamivudine+Interferon vs. Lamivudine alone in HBeAg-positive chronic hepatitis B |
| [NCT01580202](https://clinicaltrials.gov/study/NCT01580202) | Phase 3 | Completed | 180 | Entecavir vs. Lamivudine as antiviral prophylaxis in HBV-positive patients undergoing cytotoxic chemotherapy for malignant tumors |
| [NCT02598063](https://clinicaltrials.gov/study/NCT02598063) | Phase 4 | Completed | 255 | Peginterferon alfa-2a vs. Adefovir in lamivudine-resistant HBeAg-positive chronic hepatitis B |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19207972](https://pubmed.ncbi.nlm.nih.gov/19207972/) | 2009 | Cohort | Liver International | Natural history of chronic HBV infection and long-term outcomes under antiviral treatment |
| [12269843](https://pubmed.ncbi.nlm.nih.gov/12269843/) | 2002 | Review | Paediatric Drugs | Lamivudine's efficacy/tolerability profile in children and adolescents with chronic HBV |
| [35499182](https://pubmed.ncbi.nlm.nih.gov/35499182/) | 2022 | Review | Antiviral Therapy | Adefovir developed as a response to lamivudine resistance in chronic hepatitis B treatment |
| [22077578](https://pubmed.ncbi.nlm.nih.gov/22077578/) | 2011 | Cohort | PharmacoEconomics | Cost-effectiveness of prophylactic lamivudine in preventing mother-to-child HBV transmission |
| [31272463](https://pubmed.ncbi.nlm.nih.gov/31272463/) | 2019 | Meta-analysis | Virology Journal | Meta-analysis of lamivudine therapy for chronic hepatitis B in children |
| [27818588](https://pubmed.ncbi.nlm.nih.gov/27818588/) | 2016 | Review | World J Gastroenterology | Update on occult HBV infection, including antiviral management context |
| [16980024](https://pubmed.ncbi.nlm.nih.gov/16980024/) | 2006 | Case series | Transplantation Proceedings | Successful treatment of HBV infection with Lamivudine after heart transplantation |
| [12702032](https://pubmed.ncbi.nlm.nih.gov/12702032/) | 2003 | Review | Journal of Internal Medicine | Lamivudine therapy for HBV before and after liver transplantation |
| [15134176](https://pubmed.ncbi.nlm.nih.gov/15134176/) | 2004 | Commentary | Antiviral Therapy | Discussion of lamivudine-resistant HBV and implications for ongoing therapy |
| [11231955](https://pubmed.ncbi.nlm.nih.gov/11231955/) | 2001 | Review | Gastroenterology | Molecular basis of HBV drug resistance, including lamivudine resistance mutations |

## Singapore Market Information

Lamivudine currently holds **no marketing authorisation in Singapore** (0 registered products). Realizing this indication locally would require pursuing a new drug registration (or applicable named-patient/import pathway) rather than an indication extension of an existing local licence.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are flagged as data gaps in this evidence pack — notably DG001, a Blocking-severity gap on TFDA/HSA label warnings and contraindications, which must be resolved before any safety-stage review can proceed.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Hepatitis B virus infection is supported by L1-grade evidence (multiple completed Phase 3 head-to-head trials) and a well-established, mechanistically coherent rationale — this is a registration/access gap for an already-validated antiviral role, not an unproven hypothesis. However, a Blocking-severity safety data gap (local label warnings/contraindications) currently prevents this candidate from clearing the initial safety screening stage.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert (warnings and contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation via DrugBank API — currently a High-severity data gap (DG002)
- Drug-drug interaction data (current DDI query returned no results)
- Formal exclusion review of the other nine model-predicted indications (species-mismatched, obsolete, or zero-evidence entries) to prevent them from being mistaken for independent repurposing signals in downstream reporting

---

### Appendix: Other Model-Predicted Candidates (Not Actionable)

| Disease | Score | Evidence Level | Reason Excluded |
|---|---|---|---|
| Simian immunodeficiency virus infection | 99.93% | L4 | Non-human (macaque) disease entity; no clinical relevance to human indications |
| Feline acquired immunodeficiency syndrome | 99.93% | L4 | Non-human (feline) disease entity; associated clinical trials are mislabeled human HIV studies |
| Neurodevelopmental disorder with ataxic gait... | 99.93% | L5 | Rare pediatric genetic disorder; zero mechanistic link, zero evidence |
| Obsolete familial combined hyperlipidemia | 99.63% | L5 | Deprecated disease ontology term; no mechanistic plausibility |
| Chronic hepatitis C virus infection | 99.11% | L4 | HCV does not use reverse transcriptase; associated trials are HBV-drug studies mislabeled |
| Hepatitis C virus infection | 96.96% | L4 | Duplicate ontology entry of the above; same mechanistic disqualification |
| Early-onset familial noncirrhotic portal hypertension | 96.33% | L5 | Rare vascular liver disease; zero evidence; identical score to next two entries suggests embedding-cluster artifact |
| Hepatoportal sclerosis | 96.33% | L5 | Same as above |
| Idiopathic copper-associated cirrhosis | 96.33% | L5 | Same as above |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

