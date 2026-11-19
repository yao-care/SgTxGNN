---
layout: default
title: Vasopressin
parent: Low Evidence (L5)
nav_order: 1057
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Vasopressin: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Not stated in the available licence data"
monitor_inn: "Vasopressin"
predicted_indications: ["congenital prothrombin deficiency", "drug-induced osteoporosis"]
---

# Vasopressin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Vasopressin: From an Unspecified Original Indication to Congenital Prothrombin Deficiency
{: .text-alpha }

## One-Sentence Summary

Vasopressin is a peptide hormone marketed in Singapore as an injection, but the data compiled for this report do not specify an approved indication.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but **no clinical trials** and only **3 publications** exist, and none of them study vasopressin in this condition.
The prediction rests essentially on model output alone, so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for vasopressin: "Vasopressin causes vasoconstriction by binding to V 1 receptors on vascular smooth muscle coupled to the Gq/11-phospholipase C-phosphatidyl-inositol-triphosphate pathway, resulting in the release of intracellular calcium. In addition, vasopressin stimulates antidiuresis via stimulation of V 2 receptors which are coupled to adenyl cyclase." ([DailyMed: Vasostrict (vasopressin) prescribing information, Par Health USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b1147beb-743e-4c62-8927-91192447f8b8), label version 2026-04-21; accessed 2026-11-19.) Vasopressin is known to act through V1 (vasoconstrictor) and V2 (antidiuretic) receptors, but the original indication could not be confirmed from the licence data.

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

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN08350P | VASOPRESSIN INJECTION USP 20 u/ml | INJECTION | Valid |

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data for vasopressin is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vasostrict (vasopressin) prescribing information, Par Health USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b1147beb-743e-4c62-8927-91192447f8b8) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

