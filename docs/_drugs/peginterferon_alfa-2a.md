---
layout: default
title: Peginterferon Alfa-2A
parent: High Evidence (L1-L2)
nav_order: 762
evidence_level: L1
indication_count: 10
---

# Peginterferon Alfa-2A
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Peginterferon alfa-2a: From Unrecorded Original Indication to Hepatitis B Virus Infection

## One-Sentence Summary

Peginterferon alfa-2a is a long-acting type I interferon injection. The Singapore registration data do not record its original indication.
The TxGNN model predicts it may be effective for **hepatitis B virus infection**, and the evidence pack lists **50 clinical trials** (many are hepatitis C studies) and **20 publications**, including Phase 3 randomised trials.
This is probably a gap in the record rather than true repurposing, because the drug is an established hepatitis B therapy. The label status should be verified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (the approved indication text in both Singapore registrations is blank) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the DrugBank record. Based on the evaluation notes, peginterferon alfa-2a is an immunomodulatory and antiviral type I interferon. It induces interferon-stimulated genes and enhances natural killer (NK) and T-cell responses. These effects support the outcomes seen in hepatitis B: HBeAg seroconversion and a decline in HBsAg.

Because the original indication is not recorded, the link between the "original" and "new" indication cannot be assessed. The drug is widely known for treating chronic viral hepatitis, and the evidence pack contains hepatitis B trials dating back to 2004 and Phase 3 RCTs in the literature (for example, HBeAg-negative hepatitis B, PMID 15371578). This suggests the prediction reflects a known use rather than a new one.

Response depends on HBV genotype, baseline HBsAg level and early on-treatment kinetics. Published stopping rules exist (PMID 30865588).

---

## Clinical Trial Evidence

The pack lists 50 trials matched to this drug. Many are hepatitis C studies and most have not been formally relevance-graded. The table shows the 10 that are most clearly hepatitis B-focused.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01464281](https://clinicaltrials.gov/study/NCT01464281) | Not labelled | Unknown | 300 | Randomised study of switching to peginterferon alfa-2a for 48 or 96 weeks in patients on nucleotide analogues to achieve HBsAg clearance |
| [NCT00964665](https://clinicaltrials.gov/study/NCT00964665) | Phase 1/2 | Terminated | 141 | PK/PD and dose-response study of an investigational formulation (ABF656) in HBeAg-positive hepatitis B |
| [NCT02598063](https://clinicaltrials.gov/study/NCT02598063) | Phase 4 | Completed | 255 | Peginterferon alfa-2a vs adefovir in lamivudine-resistant HBeAg-positive hepatitis B |
| [NCT00435825](https://clinicaltrials.gov/study/NCT00435825) | Phase 4 | Completed | 551 | Randomised double-blind comparison of 24 vs 48 weeks and 90 vs 180 µg doses for HBeAg seroconversion |
| [NCT00877760](https://clinicaltrials.gov/study/NCT00877760) | Phase 4 | Completed | 184 | Temporary peginterferon add-on to entecavir in HBeAg-positive hepatitis B |
| [NCT01368497](https://clinicaltrials.gov/study/NCT01368497) | Phase 3 | Completed | 60 | Entecavir plus peginterferon in immune-tolerant children with chronic hepatitis B |
| [NCT00412750](https://clinicaltrials.gov/study/NCT00412750) | Phase 3 | Terminated | 159 | Telbivudine plus peginterferon alfa-2a vs peginterferon monotherapy in HBeAg-positive hepatitis B |
| [NCT02644538](https://clinicaltrials.gov/study/NCT02644538) | Phase 4 | Unknown | 196 | Adding peginterferon to nucleos(t)ide treatment to improve HBsAg clearance |
| [NCT01906580](https://clinicaltrials.gov/study/NCT01906580) | Phase 4 | Unknown | 105 | Combination vs sequential peginterferon alfa-2a and entecavir in HBeAg-positive patients |
| [NCT01531166](https://clinicaltrials.gov/study/NCT01531166) | N/A (observational) | Completed | 500 | Real-world antiviral efficacy and safety in Korean patients with chronic hepatitis B |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15371578](https://pubmed.ncbi.nlm.nih.gov/15371578/) | 2004 | RCT | N Engl J Med | Peginterferon alfa-2a alone, lamivudine alone, and the combination in HBeAg-negative chronic hepatitis B |
| [15987917](https://pubmed.ncbi.nlm.nih.gov/15987917/) | 2005 | Comparative trial (not classified in pack) | N Engl J Med | Peginterferon alfa-2a with or without lamivudine vs lamivudine alone in HBeAg-positive chronic hepatitis B |
| [30549279](https://pubmed.ncbi.nlm.nih.gov/30549279/) | 2019 | RCT | Hepatology | Entecavir plus peginterferon alfa-2a in adults with HBeAg-positive immune-tolerant infection |
| [30318613](https://pubmed.ncbi.nlm.nih.gov/30318613/) | 2019 | RCT | Hepatology | Entecavir plus peginterferon alfa-2a in children with immune-tolerant chronic hepatitis B |
| [33720089](https://pubmed.ncbi.nlm.nih.gov/33720089/) | 2021 | Randomised controlled study | J Pediatr Gastroenterol Nutr | Peginterferon alfa-2a plus lamivudine or entecavir in children with immune-tolerant hepatitis B |
| [29689122](https://pubmed.ncbi.nlm.nih.gov/29689122/) | 2018 | Phase 3 trial | Hepatology | PEG-B-ACTIVE: efficacy and safety of peginterferon alfa-2a in children with chronic hepatitis B |
| [22045673](https://pubmed.ncbi.nlm.nih.gov/22045673/) | 2011 | Post-hoc analysis of RCT | Hepatology | Shorter durations and lower doses gave inferior HBeAg seroconversion in genotypes B or C |
| [30865588](https://pubmed.ncbi.nlm.nih.gov/30865588/) | 2019 | Systematic review / meta-analysis | Antivir Ther | Individual-participant meta-analysis to identify peginterferon stopping rules |
| [26700861](https://pubmed.ncbi.nlm.nih.gov/26700861/) | 2015 | Randomised double-blind trial | Virol J | Long-term effects of peginterferon alfa-2a in Japanese patients |
| [29715359](https://pubmed.ncbi.nlm.nih.gov/29715359/) | 2018 | Review | JAMA | Review of chronic hepatitis B, including prevalence and progression risk |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN12313P | PEGASYS PRE-FILLED SYRINGE FOR INJECTION 180 mcg/0.5 ml | Injection |
| SIN12314P | PEGASYS PRE-FILLED SYRINGE FOR INJECTION 135 mcg/0.5 ml | Injection |

Both products are made by F. Hoffmann-La Roche Ltd. The registry data provided contain no approved indication text for either authorization.

---

## Safety Considerations

Please refer to the package insert for safety information. The HSA package insert has not yet been retrieved, and no drug interaction data were found.

Interferon toxicity must be screened before use. Patient groups needing particular caution include those with decompensated cirrhosis, autoimmune disease or psychiatric illness.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Phase 3 randomised evidence supports peginterferon alfa-2a in hepatitis B, and the drug is already marketed in Singapore. However, the original indication is unrecorded and the safety data are missing. Treat this as confirming an established use rather than a new repurposing opportunity.

**To proceed, the following is needed:**
- Download and parse the HSA package insert to confirm whether hepatitis B is already a labelled indication, and to obtain warnings and contraindications.
- Obtain mechanism-of-action data from DrugBank.
- Define patient-selection and monitoring rules: genotype, baseline HBsAg, early on-treatment kinetics and stopping rules.
- Screen for interferon-related contraindications such as decompensated cirrhosis, autoimmune disease and psychiatric illness.

The other predicted indications rank lower. Hepatitis E is an L3 research question supported only by case series and a systematic review. All the remaining predictions are on hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

