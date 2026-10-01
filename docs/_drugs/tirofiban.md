---
layout: default
title: Tirofiban
parent: Medium Evidence (L3-L4)
nav_order: 985
evidence_level: L4
indication_count: 10
---

# Tirofiban
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

# Tirofiban: From Acute Coronary Syndrome to Primary Release Disorder of Platelets

## One-Sentence Summary

Tirofiban is an intravenous antiplatelet drug that blocks the platelet GPIIb/IIIa receptor. The HSA record does not state its approved indication, but the retrieved literature places it in acute coronary syndrome and percutaneous coronary intervention (PCI).
The TxGNN model predicts it for **primary release disorder of platelets**, but the evidence is weak: **2 clinical trials** and **3 publications** were retrieved, and none shows therapeutic benefit.
The proposed direction also looks mechanistically backwards, because tirofiban further suppresses platelet function in a condition where platelet function is already impaired.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA record. The literature context points to acute coronary syndrome and PCI (inferred, not from the label). |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 96.27% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank for this record. The Evidence Pack's own analysis describes tirofiban as an antagonist of the GPIIb/IIIa receptor (integrin alphaIIb-beta3). It blocks fibrinogen binding and therefore platelet aggregation, which is why it is used to prevent clotting in coronary disease.

The predicted disease is a platelet release (granule secretion) disorder, a state of platelet hypofunction. Further suppressing platelet function would work against the patient and increase bleeding risk. The high TxGNN score most likely reflects a knowledge-graph association between platelet-function targets and the disease, not a therapeutic rationale. One in vitro study in the pack (PMID 16820939) found that inhibiting GPIIb/IIIa impairs platelet delta-granule release. That suggests the drug could mimic the disorder, not treat it.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03691727](https://clinicaltrials.gov/study/NCT03691727) | Phase 1/2 | Completed | 30 | Randomized, double-blind study of standard care with or without Aggrastat (tirofiban's brand name) in aneurysmal subarachnoid hemorrhage. It addresses a different disease and gives no efficacy evidence for platelet release disorders. |
| [NCT01863134](https://clinicaltrials.gov/study/NCT01863134) | Phase 4 | Completed | 140 | Eptifibatide, a different GPIIb/IIIa inhibitor, in high-risk NSTE-ACS patients needing urgent bypass surgery. The drug and the disease are both different from the prediction. |

Both trials were graded C for relevance, meaning neither supports the predicted indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16287613](https://pubmed.ncbi.nlm.nih.gov/16287613/) | 2005 | Laboratory/case series | Platelets | Tirofiban-associated thrombocytopenia is caused by drug-dependent antibodies against GPIIb/IIIa. A higher incidence of myocardial infarction and mortality has been reported in such cases. |
| [12204495](https://pubmed.ncbi.nlm.nih.gov/12204495/) | 2002 | Clinical study (TOPSTAR) | J Am Coll Cardiol | Examined troponin T release after elective PCI, and the effect of adding tirofiban on top of aspirin and clopidogrel. The setting is cardiac, not platelet disorders. |
| [16682384](https://pubmed.ncbi.nlm.nih.gov/16682384/) | 2006 | Clinical trial (ELISA-2) | Eur Heart J | Compared dual with triple antiplatelet pre-treatment in NSTE-ACS patients planned for early catheterization. It is not relevant to platelet release disorders. |

All three publications concern cardiology or drug safety. None tests tirofiban as a treatment for a platelet release disorder.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10931P | AGGRASTAT CONCENTRATE FOR INFUSION 0.25 mg/ml | Injection | Not stated in the record |

The manufacturer is Patheon Manufacturing Services LLC.

## Safety Considerations

- **Thrombocytopenia:** The retrieved literature (PMID 16287613) reports tirofiban-induced thrombocytopenia caused by drug-dependent antibodies, with a higher incidence of myocardial infarction and mortality in affected patients.
- **Bleeding risk:** The pack's mechanistic analysis notes that further platelet suppression in a platelet hypofunction state would raise bleeding risk.

No drug-interaction records were found. For other warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. The two retrieved trials and three publications do not test tirofiban in platelet release disorders. The proposed direction also appears inverted: a GPIIb/IIIa antagonist would suppress platelet function further and increase bleeding risk. The other top predictions share the problem, since Glanzmann thrombasthenia and pseudo-von Willebrand disease are both bleeding disorders where the effect would also be harmful.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications and approved indication), which is currently missing and blocks safety screening.
- DrugBank mechanism-of-action data to complete the mechanistic analysis.
- Expert review to confirm that the direction of effect is inverted, and to decide whether to retire this candidate.
- Any direct clinical or preclinical evidence of benefit in platelet release disorders. None was found.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

