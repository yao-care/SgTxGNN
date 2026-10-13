---
layout: default
title: Lopinavir
parent: Medium Evidence (L3-L4)
nav_order: 613
evidence_level: L4
indication_count: 10
---

# Lopinavir
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

# Lopinavir: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Lopinavir is an HIV protease inhibitor, marketed in combination with ritonavir (Kaletra), and originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, a primate model of HIV.
The data compiled for this report contain **no clinical trials** and **3 preclinical animal publications** for this prediction, so it is a model prediction with only preclinical support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection and AIDS (the Singapore licence records contain no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, lopinavir is an HIV-1 protease inhibitor used with ritonavir as a pharmacokinetic booster. Its efficacy in HIV infection is established, and mechanistically it may be applicable to related lentiviruses.

Simian immunodeficiency virus (SIV) is the primate counterpart of HIV-1, and its protease is closely related. This makes protease inhibition plausible. The supporting studies are macaque experiments: antiretroviral combination regimens and a chimeric SHIV carrying an HIV-1 protease gene. These serve mainly as models of the approved HIV indication, so this is **not a true human repurposing opportunity**.

Other predictions from the same model are more clinically relevant:
- **Congenital HIV** (score 98.2%, evidence level L1): a Phase 3 trial and cohort studies exist. This largely extends the existing HIV label, and the trial's lopinavir arm is unconfirmed.
- **Hepatitis B virus infection** (score 93.2%, evidence level L2): the evidence concerns HIV/HBV co-infected patients. Any anti-HBV effect comes from tenofovir, not lopinavir.
- **HPV-related benign reproductive system neoplasm** (score 86.2%, evidence level L3): one single-arm proof-of-concept study of lopinavir/ritonavir in HPV-related pre-invasive cervical disease. This is a biologically plausible early signal that needs a controlled trial.

## Clinical Trial Evidence

Currently no related clinical trials registered for simian immunodeficiency virus infection.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal study | Journal of Virology | Four cynomolgus macaques infected with SIVmac251 received a 7-day course of quadruple antiretroviral therapy. The study examined rapid viral decay and viral dynamics. |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal study | Microbes and Infection | Built a SHIV with an HIV-1 protease gene. Protease inhibitor blocked its growth in cell culture. Infection in rhesus macaques was weak but long-lasting, making it a tool for testing protease inhibitors in vivo. |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal study | Journal of Virological Methods | Two SHIV89.6P-infected rhesus macaques received oral AZT, 3TC and lopinavir/ritonavir for 28 days. The study assessed the effect on the CD8 T-cell subset. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13250P | Kaletra Tablet 200mg/50mg | Film-coated tablet | Not stated in the licence record |
| SIN11492P | Kaletra Oral Solution | Syrup | Not stated in the licence record |

## Safety Considerations

The knowledge graph links lopinavir to the following conditions as contraindications or cautions. These come from graph relationships, not from label text:
- **Cardiac and conduction:** long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, cardiomyopathy, myocardial ischaemia, coronary artery disease
- **Liver and biliary:** liver disease, cirrhosis, chronic hepatitis B and C infection, gallbladder disease, hyperbilirubinaemia, Gilbert syndrome
- **Metabolic:** pancreatitis, diabetes mellitus, hyperglycaemia, diabetic ketoacidosis, hypertriglyceridaemia, familial combined hyperlipidaemia, potassium deficiency
- **Other:** haemophilia

**Drug interactions:** 65 interactions were recorded. The listed examples include:
- **Major:** dolasetron, papaverine
- **Moderate:** acarbose, dapagliflozin, metformin, levofloxacin, ondansetron, palonosetron, famotidine, and several laxatives (bisacodyl, castor oil, lactulose, lactitol, glycerin, magnesium citrate, magnesium hydroxide, mineral oil, phenolphthalein)
- **Minor:** cimetidine, clotrimazole

Cohort literature on in utero exposure also reports transient adrenal dysfunction in uninfected infants exposed to lopinavir/ritonavir. For full details, refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The simian immunodeficiency virus prediction rests only on macaque studies, with no registered trials and no human efficacy data. These studies model the already-approved HIV indication, so they offer no new human repurposing opportunity. The label warnings and contraindications could not be verified.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Reconsideration of higher-value candidates: HPV-related neoplasia (a controlled trial), and congenital HIV (confirm the lopinavir arm in NCT00102960)
- Cardiac (QT) and hepatic safety assessment, given the knowledge graph contraindication signals and the DDI burden
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

