---
layout: default
title: Alprostadil
parent: Medium Evidence (L3-L4)
nav_order: 71
evidence_level: L3
indication_count: 10
---

# Alprostadil
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Alprostadil: From Registered Injectable Use to Aortic Malformation (Ductus-Dependent Lesions)

## One-Sentence Summary

Alprostadil (prostaglandin E1) is a vasodilator marketed in Singapore as injectable products, but the Singapore licence records do not state an approved indication.
The TxGNN model predicts it may be effective for **aortic malformation**, for example interrupted aortic arch and critical aortic stenosis, where it keeps the ductus arteriosus open until surgery.
Support consists of **2 clinical trials** (neither a pivotal efficacy trial) and **20 publications**, mostly reviews, cohorts and case reports.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Aortic malformation |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the input. Based on the retrieved literature, alprostadil (PGE1) relaxes ductal smooth muscle and keeps the ductus arteriosus open. In ductus-dependent systemic-flow lesions (interrupted aortic arch, critical aortic stenosis, aortic atresia or hypoplastic left heart), an open duct maintains systemic perfusion until surgery or intervention.

The review by Jonas (2015) states that introducing PGE1 in the late 1970s "revolutionized" the management of interrupted aortic arch. The mechanism is well established, and the prediction reflects long-standing neonatal practice rather than a novel pharmacology.

Whether this use is on the Singapore label could not be confirmed, because the licence records have no indication text. Label status should be checked separately. The prediction applies only to ductus-dependent lesions, not to every aortic malformation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04054115](https://clinicaltrials.gov/study/NCT04054115) | Phase 1 | Terminated | 10 | Acute effects of alprostadil on cerebral and pulmonary flow after bidirectional cavopulmonary connection (single-ventricle palliation). Small, underpowered, different lesion context. |
| [NCT02042092](https://clinicaltrials.gov/study/NCT02042092) | N/A | Completed | 39 | Cross-sectional comparison of Doppler ultrasonography and MR angiography in large-vessel vasculitis. Diagnostic imaging study that does not test alprostadil. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [26686446](https://pubmed.ncbi.nlm.nih.gov/26686446/) | 2015 | Review | Semin Thorac Cardiovasc Surg | PGE1 transformed management of interrupted aortic arch. Resuscitation precedes one-stage neonatal repair. |
| [25647388](https://pubmed.ncbi.nlm.nih.gov/25647388/) | 2014 | Review | Cardiol Young | Preoperative management of neonates with critical aortic valvar stenosis. |
| [30347623](https://pubmed.ncbi.nlm.nih.gov/30347623/) | 2019 | Review | J Neonatal Perinatal Med | Enteral feeding and necrotising enterocolitis risk in duct-dependent heart disease on PGE1. |
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | Cohort | Pharmacotherapy | Alprostadil dilates the ductus and increases pulmonary blood flow in infants with congenital heart malformations. |
| [7201134](https://pubmed.ncbi.nlm.nih.gov/7201134/) | 1982 | Case series | Pediatr Cardiol | PGE1 in 7 infants with hypoplastic left ventricle and aortic atresia. Transient improvement in 6, but high early mortality. |
| [6537955](https://pubmed.ncbi.nlm.nih.gov/6537955/) | 1984 | Case series | J Am Coll Cardiol | Long-term PGE1 infusion (mean 39 days) in 17 neonates, including aortic coarctation. |
| [32184038](https://pubmed.ncbi.nlm.nih.gov/32184038/) | 2020 | Cohort | Asian J Surg | Staged surgical repair outcomes for infants with interrupted aortic arch. |
| [16368373](https://pubmed.ncbi.nlm.nih.gov/16368373/) | 2006 | Cohort | Ann Thorac Surg | Outcomes of closed aortic valvotomy for critical aortic stenosis in neonates. |
| [25263728](https://pubmed.ncbi.nlm.nih.gov/25263728/) | 2014 | Case report | J Perinatol | Transient hypertrophic pyloric stenosis after PGE1 infusion (safety signal). |
| [28508920](https://pubmed.ncbi.nlm.nih.gov/28508920/) | 2017 | Case report | Pediatr Cardiol | Second- and third-degree AV block during prolonged low-dose PGE1 in a neonate with critical coarctation (safety signal). |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08097P | CAVERJECT POWDER FOR INJECTION 20 mcg/ml | Injection, powder, for solution | Not stated in the licence record |
| SIN02280P | PROSTIN VR PAEDIATRIC INJECTION 0.5 mg/ml | Injection | Not stated in the licence record |

## Safety Considerations

Package insert warnings, contraindications and drug interaction data were not available. Please refer to the package insert for safety information.

Signals from the retrieved literature on prolonged PGE1 infusion in neonates:
- Hypertrophic pyloric stenosis and gastric outlet changes (PMID 25263728).
- Atrioventricular block at low doses (PMID 28508920).
- Other known effects include apnea and fever, so use should be limited to a neonatal ICU with apnea monitoring and titration to the lowest effective dose.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is well established and the reviews and case series consistently describe PGE1 as a bridge in ductus-dependent aortic lesions. However, there are no completed randomized trials, the two registered trials are not efficacy studies of this use, and safety data for Singapore are missing.

**To proceed, the following is needed:**
- Download and parse the HSA package insert (warnings, contraindications, approved indications). This is a blocking gap.
- Verify whether ductal patency in neonates is already on the Singapore label for PROSTIN VR PAEDIATRIC.
- Retrieve mechanism-of-action data from DrugBank.
- Evaluate by lesion type, since only ductus-dependent lesions are plausible. Other predictions were weaker: congenital tricuspid stenosis, tricuspid valve agenesis and heart septal defect are research questions, and the remaining predictions (including non-specific valve anomalies and endemic goiter) are on hold.
- Define a neonatal ICU monitoring plan for apnea, gastric outlet changes and heart block.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

