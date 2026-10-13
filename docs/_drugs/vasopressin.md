---
layout: default
title: Vasopressin
parent: Medium Evidence (L3-L4)
nav_order: 1057
evidence_level: L4
indication_count: 10
---

# Vasopressin
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

# Vasopressin: From an Unspecified Original Indication to Congenital Prothrombin Deficiency

## One-Sentence Summary

Vasopressin is a peptide hormone marketed in Singapore as an injection, but the data compiled for this report do not specify an approved indication.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but **no clinical trials** and only **3 publications** exist, and none of them study vasopressin in this condition.
The prediction rests essentially on model output alone, so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for vasopressin is not available. Vasopressin is known to act through V1 (vasoconstrictor) and V2 (antidiuretic) receptors, but the original indication could not be confirmed from the licence data.

The literature found relates to **desmopressin (DDAVP)**, a V2-selective vasopressin analogue. It raises plasma factor VIII and von Willebrand factor by releasing them from endothelial cells. This is plausible for factor VIII or vWF deficiencies. However, there is **no established mechanism for prothrombin (factor II) deficiency**, and vasopressin itself (a V1 agonist) is not the agent in these reports.

The very high TxGNN score most likely reflects network proximity to coagulation-factor disorders, not a prothrombin-specific mechanism. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Acquired hemophilia A (factor VIII autoantibodies): diagnosis, causes and treatment options. It does not address prothrombin deficiency. |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case report | Rinsho Ketsueki | DDAVP given to a patient with congenital combined factor V and factor VIII deficiency. The agent is desmopressin, not vasopressin. |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case report | Rinsho Ketsueki | Cesarean section managed with factor VIII replacement in a pregnant woman with combined factor V and VIII deficiency. |

None of these studies involves vasopressin in prothrombin deficiency.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08350P | Vasopressin Injection USP 20 u/ml (Fresenius Kabi USA, LLC) | Injection | Not stated in available data |

## Safety Considerations

**Drug Interactions:** The interaction screen returned 100 interacting drugs in total. The 20 listed in the data compiled for this report include:
- **Major:** dolasetron, cisapride, papaverine, macimorelin
- **Moderate:** famotidine, epinephrine, loperamide, chlorpropamide, clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron, promethazine, cilostazol, heparin, picosulfuric acid, sodium sulfate, and polyethylene glycol (3350 with electrolytes)
- **Minor:** metronidazole

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist, the literature concerns desmopressin in factor VIII/V disorders rather than vasopressin in prothrombin deficiency, and no mechanism links vasopressin to factor II deficiency. The high model score is not backed by evidence.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication from the HSA record (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Evidence that vasopressin, rather than desmopressin, affects prothrombin or other coagulation factors
- Evaluation of the other predicted indications, which currently have even weaker support (mostly L5)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

