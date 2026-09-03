---
layout: default
title: Valaciclovir
parent: 僅模型預測 (L5)
nav_order: 1039
evidence_level: L5
indication_count: 10
---

# Valaciclovir
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

# Valaciclovir: From Herpesvirus Infections to Rheumatoid Arthritis

## One-Sentence Summary

Valaciclovir is an antiviral prodrug of acyclovir, established for treating herpes simplex (HSV) and varicella-zoster virus (VZV) infections such as shingles and genital herpes. The TxGNN model predicts a possible link to **Rheumatoid Arthritis**, but this is currently supported only by **2 low-relevance clinical trials** and **15 case-report-level publications**, most of which describe valaciclovir treating viral complications *in* RA patients rather than treating RA itself. Overall evidence strength is weak and likely reflects confounding rather than a genuine repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes simplex virus (HSV) and varicella-zoster virus (VZV) infections (antiviral therapy) — not present in the Singapore regulatory record because the drug is unregistered locally |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.95% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the evidence pack. Based on general pharmacological knowledge, valaciclovir is the L-valyl ester prodrug of acyclovir; after oral absorption it is converted to acyclovir, which is selectively phosphorylated by viral thymidine kinase in HSV/VZV-infected cells and then inhibits viral DNA polymerase, blocking viral replication. Its established clinical use is limited to treating HSV and VZV infections.

There is no known pharmacological connection between this antiviral mechanism and the autoimmune/inflammatory pathways that drive rheumatoid arthritis (TNF-α, IL-6, RANKL signalling). The TxGNN association appears to be driven largely by **confounding by indication**: RA patients treated with immunosuppressive or biologic therapies (TNF-α inhibitors, tofacitinib, methotrexate) have an elevated risk of HSV/VZV reactivation, and valaciclovir is the standard treatment for that viral complication — not for RA itself. Every case identified in the evidence pack describes valaciclovir being used to treat a viral infection that arose *in* an RA patient, rather than any direct effect on RA disease activity.

Given the absence of any mechanistic rationale or interventional trial testing valaciclovir as an RA therapy, this prediction should be treated as a data-linkage artifact rather than a genuine repurposing candidate at this stage.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05111743](https://clinicaltrials.gov/study/NCT05111743) | N/A | Completed | 9,261 | Real-world safety study of brolucizumab in wet age-related macular degeneration; unrelated to valaciclovir or RA — flagged as a noise pairing during evidence review |
| [NCT00195624](https://clinicaltrials.gov/study/NCT00195624) | Phase 2 | Completed | 47 | Pilot study of alemtuzumab for relapsed/refractory severe aplastic anemia; unrelated to valaciclovir or RA — flagged as a noise pairing |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34579250](https://pubmed.ncbi.nlm.nih.gov/34579250/) | 2021 | Systematic Review | Vaccines | Reviewed 12 case reports of VZV reactivation after COVID-19 vaccination; not RA- or valaciclovir-efficacy evidence |
| [18674945](https://pubmed.ncbi.nlm.nih.gov/18674945/) | 2008 | Case Series/Review | Joint Bone Spine | Herpes zoster occurrence in patients on TNF-α antagonists for chronic inflammatory joint disease (incl. RA); documents infection risk during biologic therapy |
| [35249916](https://pubmed.ncbi.nlm.nih.gov/35249916/) | 2022 | Case Report | Intern Med | RA patient on methotrexate + iguratimod developed VZV reinfection and EBV reactivation; despite oral valacyclovir, developed varicella pneumonia and meningoencephalitis |
| [24660085](https://pubmed.ncbi.nlm.nih.gov/24660085/) | 2014 | Case Report | Case Rep Rheumatol | RA patient developed Ramsay Hunt syndrome (VZV reactivation) after infliximab; treated with valaciclovir + hydrocortisone, full recovery at 6 months |
| [35236687](https://pubmed.ncbi.nlm.nih.gov/35236687/) | 2022 | Case Report | BMJ Case Rep | RA patient on tofacitinib developed herpes zoster meningitis; tofacitinib discontinued, antiviral treatment given |
| [19648728](https://pubmed.ncbi.nlm.nih.gov/19648728/) | 2009 | Case Report | Dermatology | RA patient on etanercept developed disseminated herpes zoster mimicking rheumatoid vasculitis — diagnostic pitfall during biologic therapy |
| [32274443](https://pubmed.ncbi.nlm.nih.gov/32274443/) | 2020 | Case Series | Am J Ophthalmol Case Rep | Four RA patients with concomitant herpes simplex keratitis and autoimmune ulcerative keratitis |
| [34540433](https://pubmed.ncbi.nlm.nih.gov/34540433/) | 2021 | Case Report | Cureus | RA patient presenting as Felty syndrome (neutropenia, splenomegaly) with concurrent genital herpes; unrelated to any RA-directed effect of valaciclovir |
| [14600805](https://pubmed.ncbi.nlm.nih.gov/14600805/) | 2003 | Case Report | Intensive Care Med | Patient with mild RA on infliximab + methotrexate developed disseminated TB, pulmonary aspergillosis, and cutaneous HSV infection |
| [21299443](https://pubmed.ncbi.nlm.nih.gov/21299443/) | 2011 | Case Report | Cutan Ocul Toxicol | Herpes zoster occurring at the infliximab infusion site in a patient treated for inflammatory arthritis |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but all supporting evidence is low-quality (case reports/case series, no RCTs) and appears explained by confounding by indication — valaciclovir treats viral infections that occur *in* immunosuppressed RA patients, not RA itself. There is no mechanistic basis linking an antiviral drug to autoimmune joint disease, and the two associated clinical trials are unrelated noise pairings.

**To proceed, the following is needed:**
- A confirmed mechanistic hypothesis linking acyclovir/valaciclovir activity to RA-relevant pathways (currently none identified)
- At minimum, a controlled or interventional study testing valaciclovir specifically for RA disease activity (not just antiviral treatment in RA patients)
- Singapore/HSA regulatory and safety data (drug is currently unregistered — 0 licenses), including package insert warnings, contraindications, and drug interactions
- Confirmed drug MOA data from DrugBank to close data gap DG002
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

