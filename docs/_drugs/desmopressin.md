---
layout: default
title: Desmopressin
parent: Medium Evidence (L3-L4)
nav_order: 312
evidence_level: L4
indication_count: 10
---

# Desmopressin
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

# Desmopressin: From Antidiuretic Uses to Congenital Prothrombin Deficiency

## One-Sentence Summary

Desmopressin is a synthetic vasopressin analogue marketed in Singapore as Minirin and Nocdurna, and it is also widely used to release von Willebrand factor (VWF) and factor VIII (FVIII) in some bleeding disorders.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but only **1 clinical trial** (unrelated to desmopressin) and **4 publications** (reviews and case reports, none showing benefit for this disease) are linked to this prediction.
The evidence is weak, and the mechanistic link is doubtful.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA registry text. Desmopressin is generally used for diabetes insipidus, nocturnal enuresis and nocturia, and mild hemophilia A/von Willebrand disease. |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Desmopressin acts on V2 receptors to release VWF and FVIII from endothelial stores. This is why it is used in mild hemophilia A and some types of von Willebrand disease. Detailed mechanism-of-action data from DrugBank is not available in this evidence pack, so the description here relies on the pack's mechanistic assessment.

Prothrombin (factor II) deficiency is a different problem. Desmopressin does not raise prothrombin, so the mechanistic link is weak. The high graph score most likely reflects the drug's many associations with other congenital coagulation factor disorders, which sit close to this disease in the knowledge graph. In short, the prediction looks like a graph-proximity effect rather than a true biological rationale.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04567511](https://clinicaltrials.gov/study/NCT04567511) | Phase 4 | Recruiting | 20 | Single-arm study of emicizumab (Hemlibra) in mild hemophilia A. It does not involve desmopressin or prothrombin deficiency (relevance grade C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Review | Drugs | Rational treatment options for inherited bleeding disorders, mainly haemophilia A and von Willebrand disease. |
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Diagnosis, aetiology and treatment of acquired hemophilia A. |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case report | Rinsho Ketsueki | DDAVP given to a patient with congenital combined factor V and VIII deficiency. |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case report | Rinsho Ketsueki | Cesarean section managed with factor VIII concentrate in a pregnant woman with combined factor V and VIII deficiency. |

None of these papers directly studies desmopressin in prothrombin deficiency.

## Singapore Market Information

Seven registrations exist in total. Five are shown below. The registry text has no approved-indication wording for these products, so that column is omitted. Other forms on record include spray and injection.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15461P | NOCDURNA ORAL LYOPHILISATE 25MCG | Orally disintegrating tablet |
| SIN14261P | MINIRIN Oral Lyophilisate 120 mcg | Orally disintegrating tablet |
| SIN11656P | MINIRIN TABLET 0.1 mg (Oval) | Tablet |
| SIN14260P | MINIRIN Oral Lyophilisate 60 mcg | Orally disintegrating tablet |
| SIN15462P | NOCDURNA ORAL LYOPHILISATE 50MCG | Orally disintegrating tablet |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The link to prothrombin deficiency is mechanistically weak, and the only trial found tests a different drug. The literature has no supporting efficacy data (evidence level L4). A high model score alone does not justify advancing this candidate.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Direct clinical data on desmopressin in prothrombin deficiency, if any exists
- A review of the other predictions from this run:
  - Primary release disorder of platelets is the most plausible (L3, Research Question), since desmopressin can shorten bleeding time in some platelet release defects.
  - Thrombotic thrombocytopenic purpura, inherited thrombophilia and pseudo-von Willebrand disease carry harm signals and should be treated as contraindication warnings, not opportunities.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

