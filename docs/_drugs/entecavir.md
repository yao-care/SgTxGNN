---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir (ETV) is a guanosine nucleoside analogue approved globally since 2005 for the treatment of chronic hepatitis B virus (HBV) infection, though it is currently not registered in Singapore.
The TxGNN model predicts it may be effective for **Chronic Hepatitis C Virus Infection** with a score of **99.98%**, however this prediction is identified as a **computational false positive** — no clinical trials or publications provide direct evidence of ETV activity against HCV, and the mechanistic basis is absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Hepatitis B Virus Infection (globally approved in US/EU/Japan; **not registered in Singapore**) |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Entecavir belongs to the guanosine nucleoside analogue class. Once taken up by hepatocytes, it is phosphorylated to its active triphosphate form, which then competitively inhibits the HBV DNA polymerase across three distinct catalytic steps: (1) primer initiation of the pregenomic RNA template, (2) reverse transcription of the negative-strand DNA, and (3) synthesis of the positive-strand DNA. Its inhibitory constant (Ki) for HBV polymerase is orders of magnitude lower than for human DNA polymerases, conferring high selectivity — the pharmacological basis for its FDA approval in 2005.

Hepatitis C virus (HCV), however, belongs to the Flaviviridae family and is a positive-sense single-stranded RNA virus. Its replication relies entirely on the NS5B RNA-dependent RNA polymerase (RdRp), an enzyme that is structurally and mechanistically distinct from HBV's reverse-transcriptase-like DNA polymerase. ETV's triphosphate form has no known binding affinity or inhibitory activity against HCV NS5B. The two enzymes share neither substrate specificity nor active-site architecture relevant to nucleoside analogue inhibition.

The high TxGNN score (0.9998) most likely reflects **knowledge graph topology** rather than biological plausibility: HBV and HCV share numerous graph nodes related to viral hepatitis, liver disease, co-infection clinics, and shared patient populations. This creates strong topological connections between the ETV node and the HCV disease node without any underlying mechanistic support. All reviewed evidence confirms this is a **computational false positive**, and no further mechanistic or clinical pathway connects ETV to HCV efficacy.

---

## Clinical Trial Evidence

All 40 clinical trials retrieved for this indication target **HBV, not HCV**. They appeared in the evidence search because Entecavir and HCV co-occur in trials involving HBV/HCV co-infected patients (where ETV manages the HBV component while DAAs address HCV) or in background/comparator contexts. No trial has evaluated Entecavir as a treatment for HCV infection.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | N/A | Unknown | 420 | Prospective ETV trial in HBV+HCC patients undergoing radiofrequency ablation — targets HBV viral load, not HCV |
| [NCT00371150](https://clinicaltrials.gov/study/NCT00371150) | Phase 4 | Completed | 131 | Antiviral effect of ETV in Black/Hispanic patients with chronic HBV — HBV focus only |
| [NCT00096785](https://clinicaltrials.gov/study/NCT00096785) | Phase 3 | Completed | 69 | ETV vs. adefovir for early viral load reduction in nucleoside-naive chronic HBV — HBV only |
| [NCT02532413](https://clinicaltrials.gov/study/NCT02532413) | Phase 4 | Unknown | 180 | ETV monotherapy vs. ETV + Poly IC in chronic HBV — HBV focus |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | DAA therapy in HCV/HBV co-infected patients; ETV used prophylactically to prevent **HBV reactivation** during HCV treatment, not to treat HCV |
| [NCT00597259](https://clinicaltrials.gov/study/NCT00597259) | Phase 4 | Unknown | 294 | Pegasys + ETV vs. ETV alone in HBeAg-positive chronic HBV — HBV focus |
| [NCT07267208](https://clinicaltrials.gov/study/NCT07267208) | Phase 2 | Not yet recruiting | 82 | ETV orally disintegrating tablet in stable liver transplant recipients with chronic HBV — HBV focus |
| [NCT05484466](https://clinicaltrials.gov/study/NCT05484466) | Phase 2 | Unknown | 90 | ZM-H1505R + ETV vs. ETV monotherapy in CHB patients on long-term ETV — HBV focus |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Unknown | 60 | Role of nucleoside analogues (incl. ETV) in preventing HBV reactivation during DAA therapy for chronic HCV — ETV used for HBV protection, not HCV treatment |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | Completed | 130 | Arabinoxylan rice bran for HCC, HBV and HCV infection — ETV is a background agent for HBV; no ETV HCV efficacy data |

**None of the above trials assess Entecavir's efficacy against HCV.**

---

## Literature Evidence

The 20 publications retrieved co-mention Entecavir and hepatitis C primarily in the context of: (1) HBV/HCV co-infection management where ETV controls the HBV component; (2) HCV reactivation risk during anti-HBV nucleoside therapy; or (3) general reviews of viral hepatitis treatment landscapes. None provide data on ETV inhibiting HCV replication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | HCV reactivation in anti-HCV antibody-positive CHB patients on nucleoside analogues — ETV used to treat HBV; HCV reactivated rather than being suppressed |
| [28538267](https://pubmed.ncbi.nlm.nih.gov/28538267/) | 2017 | Cohort | Eur J Gastroenterol Hepatol | Cirrhosis does not impair ETV efficacy in CHB; notes contrast with HCV where cirrhosis complicates DAA response — HBV focus |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral medications for HBV and HCV and renal effects — ETV cited as HBV agent only; no HCV efficacy claim |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | HBV/HCV co-infection management — ETV role is HBV suppression while HCV is treated with interferon/DAA combinations |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Review | Biomedicines | Chronic viral hepatitis therapy overview — ETV and tenofovir highlighted as HBV nucleoside analogues; HCV treated with DAAs |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clin Res Hepatol Gastroenterol | Management of HBV and HCV in children — ETV for HBV; pediatric HCV treated with sofosbuvir-based DAAs |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Review | World J Hepatology | HBV and HCV management before and after transplantation — ETV prevents HBV recurrence post-transplant |
| [21497740](https://pubmed.ncbi.nlm.nih.gov/21497740/) | 2011 | Review | Best Pract Res Clin Gastroenterol | Fibrosis in chronic viral hepatitis — ETV improves liver histology in HBV; distinct from HCV treatment |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Chronic HBV and HCV treatment landscape overview — ETV noted as emerging HBV therapy; peginterferon + ribavirin for HCV |
| [28487602](https://pubmed.ncbi.nlm.nih.gov/28487602/) | 2017 | Review | World J Gastroenterology | HBV and alcohol; HCC epidemiology; notes HCV now curable with DAAs, making HBV a future dominant cause — ETV cited for HBV |

**None of the above publications demonstrate Entecavir efficacy against HCV.**

---

## Singapore Market Information

Entecavir is currently **not registered in Singapore**. No product authorizations were identified.

> Entecavir (brand name Baraclude®, Bristol-Myers Squibb; multiple generics also available) is approved and widely used in the United States (FDA, 2005), European Union, Japan, China, South Korea, Taiwan, and many other jurisdictions for the treatment of chronic HBV infection. Clinicians in Singapore requiring Entecavir would need to access it through the Health Sciences Authority's special access or import pathways.

---

## Safety Considerations

Formal safety data from Singapore/HSA-registered product inserts is unavailable as Entecavir is not marketed locally.

> Please refer to the package insert (Baraclude® or equivalent generic) for complete safety information.

Two safety points from the drug's known international regulatory profile are particularly important for clinical awareness:

- **Black Box Warning — HIV/HBV co-infection**: The FDA mandates that Entecavir must **not** be used as monotherapy in HIV/HBV co-infected patients who are not on a fully suppressive antiretroviral regimen. Sub-therapeutic Entecavir concentrations against HIV-1 can select for the RT M184V resistance mutation, conferring cross-resistance to lamivudine and emtricitabine (see Rank 3 rationale in this evidence pack).
- **Class warning — Lactic acidosis and hepatomegaly**: As a nucleoside analogue, Entecavir carries a class warning for potentially fatal lactic acidosis and severe hepatomegaly with steatosis. Risk increases with hepatic dysfunction.
- **Renal adjustment**: Dose modification is required for creatinine clearance < 50 mL/min.
- **Post-treatment hepatitis flare**: Abrupt discontinuation can cause severe exacerbations of HBV.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Entecavir's mechanism of action — inhibition of HBV DNA polymerase (reverse transcriptase) — is fundamentally incompatible with HCV treatment, which requires inhibition of the structurally and enzymatically distinct NS5B RNA-dependent RNA polymerase. The TxGNN prediction score of 99.98% reflects knowledge graph co-occurrence between hepatitis disease nodes rather than any true pharmacological connection. Every clinical trial and every publication in the evidence pack confirms this: Entecavir has been studied extensively alongside HCV only in the context of managing the HBV component in co-infected patients.

**No further development is warranted for this specific predicted indication.**

**Higher-priority observations from this evidence pack:**

- **Hepatitis B virus infection** (Rank 2, L1 evidence, Proceed with Guardrails) — This is the drug's established global indication, backed by multiple completed Phase 3 RCTs including NCT01063036 (ETV + tenofovir, n=144) and NCT01438424 (open-label ETV, n=1,053). Pursuing Singapore registration should be prioritized if local clinical demand exists.
- **HIV infectious disease** (Rank 3, L3 evidence) — Published data (PMID 17582071, PMID 18453854) confirm measurable anti-HIV-1 activity in vitro and in patients, but the FDA black box warning on resistance selection means this requires careful safety evaluation before any repurposing investigation.
- **Animal viral hepatitis** (Rank 8, L3 evidence) — ETV's development history is deeply rooted in woodchuck hepatitis virus and duck HBV animal models, where substantial efficacy data exist. This is scientifically valid but not a human medical repurposing opportunity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

