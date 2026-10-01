---
layout: default
title: Calfactant
parent: Low Evidence (L5)
nav_order: 197
evidence_level: L5
indication_count: 10
---

# Calfactant
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

# Calfactant: From Neonatal Respiratory Distress Syndrome to Adult Acute Respiratory Distress Syndrome

## One-Sentence Summary

Calfactant is a natural calf-lung surfactant, marketed in Singapore as Infasurf, and used for respiratory distress syndrome in neonates.
The TxGNN model predicts it may be effective for **adult acute respiratory distress syndrome (ARDS)**.
Support so far is **1 Phase 3 trial (terminated early)** and **7 publications**, and adult efficacy has not been established.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neonatal respiratory distress syndrome (not stated in the Singapore registration record) |
| Predicted New Indication | Adult acute respiratory distress syndrome |
| TxGNN Prediction Score | 95.78% |
| Evidence Level | L2 (see note below) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

*Evidence level note: the input labelled this L1. Under the L1-L5 rules, L1 needs at least two completed Phase 3 RCTs. The only registered Phase 3 trial was terminated, so this report rates it L2 on the strength of the published RCTs (adult and pediatric).*

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for calfactant is not available in the input. Based on known information, calfactant is a natural bovine-derived lung surfactant that directly replaces the body's own surfactant. Its efficacy in neonatal respiratory distress syndrome is established, and mechanistically it may be applicable to ARDS.

ARDS involves inactivation and dysfunction of the lung's own surfactant. Replacing it is therefore biologically plausible, and it is the same principle that works in neonates. A pediatric acute lung injury RCT (JAMA 2005) and its secondary analysis support this direction in children.

Adult efficacy remains unproven. The adult Phase 3 trial was terminated early, so its outcome should be checked against the primary publication (PMID 25855884) before any recommendation is made.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00682500](https://clinicaltrials.gov/study/NCT00682500) | Phase 3 | Terminated | 332 | Intratracheal calfactant in adults and children with direct ARDS or direct acute lung injury, started within 48 hours of mechanical ventilation. It tested whether calfactant lowers mortality and shortens respiratory failure. Early termination limits the strength of any conclusion. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25855884](https://pubmed.ncbi.nlm.nih.gov/25855884/) | 2015 | RCT | Chest | Adult Calfactant in ARDS trial. A multicentre, randomized, masked trial of calfactant in adults and children with ALI/ARDS, based on positive pediatric results. The abstract provided is truncated, so the outcome is not confirmed here. |
| [15671432](https://pubmed.ncbi.nlm.nih.gov/15671432/) | 2005 | RCT (pediatric) | JAMA | Randomized trial of calfactant in pediatric acute lung injury. Earlier adult surfactant trials had been unsuccessful, while preliminary pediatric data suggested benefit. |
| [23925143](https://pubmed.ncbi.nlm.nih.gov/23925143/) | 2013 | Secondary analysis of RCT (pediatric) | Pediatr Crit Care Med | Post hoc analysis of the pediatric calfactant trial examining how fluid balance relates to in-hospital outcomes. |
| [21048239](https://pubmed.ncbi.nlm.nih.gov/21048239/) | 2010 | Review | Indian Pediatrics | Review of pediatric ARDS causes, mortality risk and supportive therapies. |
| [17198050](https://pubmed.ncbi.nlm.nih.gov/17198050/) | 2007 | Review | Curr Opin Crit Care | Review of pediatric mechanical ventilation, which is largely guided by a few pediatric trials plus adult data. |
| [20335386](https://pubmed.ncbi.nlm.nih.gov/20335386/) | 2010 | Review/Commentary | Am J Respir Crit Care Med | Commentary arguing that surfactant composition and biophysical properties matter in clinical studies. |
| [33493441](https://pubmed.ncbi.nlm.nih.gov/33493441/) | 2021 | Case report | Chest | Exogenous surfactant used in one COVID-19 patient with ARDS. COVID-19 hypoxemia resembles surfactant-deficiency respiratory distress. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14333P | Infasurf Intratracheal Suspension 35mg/mL (ONY Biotech Inc., parametric release) | Suspension, sterile | Not listed in the registration record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the model score is high (95.78%). However, the only Phase 3 trial in adults was terminated early, and adult efficacy is not established. The pediatric RCT evidence does not transfer directly to adults. Safety information is also missing from the input.

**To proceed, the following is needed:**
- The package insert from HSA (warnings and contraindications), before any safety screening
- Detailed mechanism-of-action data from DrugBank
- The primary results of NCT00682500 and the Chest 2015 publication (PMID 25855884), including mortality and the reason for early termination
- Confirmation of the approved indication text for SIN14333P and of intratracheal route suitability for adult ARDS

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

