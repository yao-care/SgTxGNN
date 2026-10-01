---
layout: default
title: Fenofibrate
parent: Medium Evidence (L3-L4)
nav_order: 418
evidence_level: L4
indication_count: 10
---

# Fenofibrate
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Fenofibrate: From Dyslipidaemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a fibrate lipid-lowering drug that acts mainly on triglycerides. The Singapore registry text for its licences is blank, so the original indication is inferred from its known pharmacology.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)**. Only **1 clinical trial** was retrieved, and it tests a different drug (alirocumab). **Literature** is limited to 1 small older cohort that touches HoFH, plus guidelines and reviews of other lipid-lowering drugs.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registry records (inferred: dyslipidaemia, based on fenofibrate's class and the literature) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Fenofibrate is a PPARα agonist. It mainly lowers triglycerides and raises HDL-C, with a modest LDL-C effect.

HoFH is caused by absent or defective LDL receptors. A drug that acts through PPARα is therefore unlikely to lower LDL-C meaningfully in these patients. A 1984 study reported that one HoFH patient in a type II hyperlipoproteinemia cohort had the largest fall in cholesterol, but a single case is far too little to build on. The high TxGNN score most likely reflects graph proximity to the lipid-disorder cluster rather than a true mechanistic fit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab (PCSK9 inhibitor) in children and adolescents aged 8–17 with HoFH, with LDL-C at Week 12 as the primary outcome. Fenofibrate is not tested, so this gives no direct evidence. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohort | Pharmacol Res Commun | In 22 type II hyperlipoproteinemia patients on fenofibrate 300 mg/day, LDL-C fell about 24%. The single HoFH patient had the greatest fall in cholesterol and LDL-C. This is the only fenofibrate-specific paper. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidaemia management and cardiovascular prevention. No fenofibrate-specific HoFH data. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Review of non-statin lipid-lowering drugs. The clearest indication for fenofibrate monotherapy is fasting triglycerides above 500 mg/dl, to reduce pancreatitis risk. |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review / case report | Intern Med J | Liver transplantation for adult HoFH when drugs and apheresis are insufficient. Fenofibrate is not the focus. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Ann N Y Acad Sci | Drug and surgical treatment of dyslipidaemic children. Fenofibrate is among the agents that lowered lipids in familial hypercholesterolemia. |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart J | LDL-C, statins and PCSK9 inhibitors. Does not evaluate fenofibrate. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Pharmacokinetic study | Pharmacotherapy | Lomitapide, an approved HoFH drug, was tested for drug interactions with several lipid drugs, including fenofibrate. |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Curr Atheroscler Rep | Dyslipidaemia management in pregnancy. Not specific to fenofibrate or HoFH. |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Ezetimibe review. Not about fenofibrate. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Atorvastatin review. Not about fenofibrate. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13351P | Fenosup Lidose 160mg Capsule | Capsule | Not stated in registry record |
| SIN13615P | LIPANTHYL PENTA FILM COATED TABLET 145 mg | Tablet, film coated | Not stated in registry record |
| SIN10668P | TROLIP 300 CAPSULES 300 mg | Capsule | Not stated in registry record |
| SIN17013P | TRICOR TABLET 160 MG | Tablet, film coated | Not stated in registry record |
| SIN16947P | TROLATE CAPSULE 100mg | Capsule | Not stated in registry record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism does not fit HoFH, which stems from defective LDL receptors. The only trial retrieved tests alirocumab, not fenofibrate. The fenofibrate-specific literature is one small 1984 cohort with a single HoFH patient. The high TxGNN score alone is not enough to support advancing this indication.

**To proceed, the following is needed:**
- The approved indications from the Singapore package insert, which would confirm the original indication and its safety information.
- Mechanism of action data, from DrugBank.
- A dedicated controlled study of fenofibrate in HoFH, as an adjunct to standard therapy such as PCSK9 inhibitors or lomitapide.

Two other predictions in the pack look stronger. Hyperlipoproteinemia (rank 2) has Phase 3/4 RCTs with fenofibrate arms and was scored L1. However, it appears to be an established lipid-lowering use rather than true repurposing, so it should be checked against the approved label. Familial hypercholesterolemia and autosomal dominant hypercholesterolemia (ranks 3 and 7) have only small older studies (L3), and fenofibrate would at best be an adjunct there.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

