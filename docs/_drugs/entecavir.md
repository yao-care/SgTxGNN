---
layout: default
title: Entecavir
parent: Low Evidence (L5)
nav_order: 375
evidence_level: L5
indication_count: 10
---

# Entecavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is an oral nucleoside analogue whose established use is chronic hepatitis B (HBV) treatment.
The TxGNN model predicts it may be effective for **chronic hepatitis C virus (HCV) infection**, with a very high score (99.98%).
However, none of the retrieved clinical trials or publications tests entecavir as an HCV treatment, so this prediction is **not supported by direct evidence** and is most likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B (the Singapore registration records provided contain no indication text, so this reflects the drug's known use) |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% (model rank 675) |
| Evidence Level | L5 (model prediction only; no HCV-specific studies. The upstream pack labelled this L4, but no preclinical or mechanistic HCV data were found) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 17 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Entecavir is a guanosine nucleoside analogue that inhibits HBV polymerase (priming, reverse transcription and DNA synthesis). Its efficacy in chronic hepatitis B is well established.

The prediction is difficult to justify mechanistically. HCV is an RNA virus that replicates through the NS5B RNA-dependent RNA polymerase, and entecavir has no documented activity against it. The high score most likely reflects graph proximity, since HBV and HCV share viral hepatitis and nucleoside analogue neighbours in the knowledge graph.

The retrieved evidence is consistent with this. All the trials are HBV studies. The literature is mostly about HBV/HCV co-infection, such as HBV reactivation during direct-acting antiviral (DAA) treatment for HCV. In those settings entecavir treats or prevents HBV, not HCV.

## Clinical Trial Evidence

No retrieved trial evaluates entecavir for HCV. The closest are HBV/HCV co-infection studies (first two rows) and HBV studies that mention HCV only in the background text.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Unknown | 60 | Tests whether prophylactic nucleos(t)ide analogue (NUC) prevents HBV reactivation in HBV/HCV co-infected patients receiving DAA therapy (12 vs 24 weeks). Targets HBV, not HCV. |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Studies HBV reactivation during DAA treatment of HCV/HBV co-infection. |
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | N/A | Unknown | 420 | Entecavir for chronic hepatitis B in HCC patients after radiofrequency ablation. HBV endpoint only. |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | Completed | 130 | Arabinoxylan rice bran (MGN-3/Biobran) in HCC with hepatitis B and C. Does not test entecavir. |
| [NCT00597259](https://clinicaltrials.gov/study/NCT00597259) | Phase 4 | Unknown | 294 | Peginterferon plus entecavir vs entecavir alone in HBeAg-positive chronic hepatitis B. Not an HCV study. |
| [NCT00371150](https://clinicaltrials.gov/study/NCT00371150) | Phase 4 | Completed | 131 | Entecavir antiviral effect in Black/African American and Hispanic patients with HBV. |
| [NCT02532413](https://clinicaltrials.gov/study/NCT02532413) | Phase 4 | Unknown | 180 | Entecavir monotherapy vs entecavir plus Poly IC in chronic hepatitis B. |
| [NCT00096785](https://clinicaltrials.gov/study/NCT00096785) | Phase 3 | Completed | 69 | Entecavir vs adefovir, early viral load reduction in nucleoside-naive HBV patients. |
| [NCT00065507](https://clinicaltrials.gov/study/NCT00065507) | Phase 3 | Completed | 195 | Entecavir vs adefovir in HBV with hepatic decompensation. |
| [NCT06566248](https://clinicaltrials.gov/study/NCT06566248) | Phase 2 | Recruiting | 90 | Nucleoside (acid) analogues combined with TQA3810 in chronic hepatitis B. |

## Literature Evidence

No publication reports entecavir efficacy against HCV. Most articles address HBV/HCV co-infection or HBV treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | 66 anti-HCV-positive chronic hepatitis B patients on nucleos(t)ide analogue therapy were followed for HCV reactivation and viral load changes. |
| [28538267](https://pubmed.ncbi.nlm.nih.gov/28538267/) | 2017 | Cohort | Eur J Gastroenterol Hepatol | Cirrhosis had no impact on entecavir response in chronic hepatitis B. The HCV comparison appears only as background. |
| [29194858](https://pubmed.ncbi.nlm.nih.gov/29194858/) | 2018 | Not classified | J Viral Hepat | Low incidence of HBV reactivation in HCV patients receiving DAA therapy. |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Not classified | J Gastroenterol Hepatol | Assessed the risk of HBV reactivation in HCV patients treated with DAAs. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Advances in treating HBV/HCV coinfection. |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Review / case report | Clin Res Hepatol Gastroenterol | HBV/HCV co-infection as a therapeutic challenge. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral drugs for hepatitis B and C and their effects on kidney function. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Current treatment and prospects for chronic hepatitis B and C. |
| [32527114](https://pubmed.ncbi.nlm.nih.gov/32527114/) | 2021 | Not classified | Chin Clin Oncol | Timing and management of hepatitis B and C in HCC patients. |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Not classified | World J Hepatol | Management of hepatitis B and C around liver and kidney transplantation. Entecavir is used against HBV recurrence. |

## Singapore Market Information

There are 17 registrations in total; five are shown. The approved indication text is not included in the registration records provided.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16092P | ENTECAVIR-TEVA FC TABLETS 0.5MG | Film-coated tablet | Remedica Ltd. |
| SIN16612P | ALMACAVIR (ENTECAVIR) FILM COATED TABLETS 0.5MG | Film-coated tablet | GENUONE Sciences Inc. |
| SIN16619P | BEATECAVIR FILM COATED TABLET 1MG | Film-coated tablet | Remedica Ltd |
| SIN16090P | HEPURI F.C. TABLETS 0.5 MG | Film-coated tablet | Standard Chem. & Pharm. Co. Ltd., 2nd Plant |
| SIN13167P | BARACLUDE TABLET 1mg | Film-coated tablet | AstraZeneca Pharmaceuticals LP; Catalent Anagni S.R.L.; Patheon Inc. |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data were available in the input.

For the established HBV use, the evidence pack notes these points, all of which need confirmation from the package insert:
- **Renal function**: dose adjustment is needed in renal impairment.
- **Lactic acidosis and hepatic flare on discontinuation**.
- **HBV resistance monitoring**.
- **HIV co-infection**: screen before use. Entecavir has partial anti-HIV-1 activity and can select the M184V mutation, which may compromise later lamivudine/emtricitabine options.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HCV prediction has a high model score but no direct evidence and no plausible mechanism. The trials are HBV studies, and the literature only concerns HBV/HCV co-infection. HCV is also now curable with direct-acting antivirals, so there is little unmet need for a nucleoside analogue with no known anti-HCV activity.

**To proceed, the following is needed:**
- Any in vitro evidence of entecavir activity against HCV (for example a replicon assay).
- Detailed mechanism of action data (MOA).
- Warnings and contraindications from the HSA package insert.
- Consideration of the rank-2 prediction (hepatitis B virus infection, L1, "Proceed with Guardrails"). It is the drug's established indication, so it is not true repurposing. Any new-indication work should focus on the HBV/HCV co-infection setting, where entecavir treats the HBV component.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

