---
layout: default
title: Moroctocog Alfa
parent: Low Evidence (L5)
nav_order: 680
evidence_level: L5
indication_count: 10
---

# Moroctocog Alfa
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

# Moroctocog alfa: From Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Moroctocog alfa is a B-domain-deleted recombinant factor VIII (FVIII), marketed in Singapore as Xyntha. It replaces the missing clotting factor in hemophilia A, although the Singapore registry records give no indication text.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but the evidence is very weak: **7 loosely related clinical trials** (none tests this drug in this disease) and **0 publications**.
The high score most likely reflects proximity in the knowledge graph to bleeding-disorder concepts, not a pharmacological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registry records. As a recombinant FVIII product, it is used for hemophilia A (general knowledge, not from the Evidence Pack) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no relevant studies) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, moroctocog alfa supplies FVIII, a plasma coagulation factor. FVIII works together with activated factor IX on the platelet surface to generate thrombin.

Platelet release (secretion) disorders are different. They are intrinsic defects of platelet granules or signalling, so the platelets themselves fail to release their contents. Giving more FVIII does not correct this, so **no credible mechanistic link** could be identified. The score of about 99.97% likely reflects the drug's position near coagulation and bleeding-disorder nodes in the knowledge graph. It should not be read as evidence of efficacy.

The same weakness applies to the other top-ranked predictions:
- Pseudo-von Willebrand disease (99.97%): the defect is in the platelet GPIbα receptor. FVIII binds von Willebrand factor (VWF) but does not fix the receptor.
- Glanzmann thrombasthenia (99.96%): the defect is in the GPIIb/IIIa integrin. Standard care is platelet transfusion and recombinant FVIIa.
- Acquired coagulation factor deficiency (99.88%): this is the most biologically plausible prediction. It is limited by neutralising autoantibodies against FVIII in acquired hemophilia A, and the standard options are bypassing agents or porcine FVIII.

---

## Clinical Trial Evidence

None of these trials tests moroctocog alfa in platelet release disorders. All were graded C (low relevance).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | Recruiting | 200 | Laboratory and symptom study in post-COVID-19-vaccination syndrome; unrelated to FVIII or platelet release disorders |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Not yet recruiting | 80 | Coagulation profiles in newly diagnosed AML patients on induction chemotherapy; not about this drug or indication |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | Recruiting | 25 | Artificial liver support (DPMAS + plasma exchange) in acute-on-chronic liver failure; unrelated population and intervention |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Completed | 30 | PEGylated rFVIII (BAX 855) in severe hemophilia A patients undergoing surgery; supports the FVIII class in hemophilia A only |
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Completed | 159 | BIVV001 (rFVIIIFc-VWF-XTEN) in previously treated patients ≥12 years with severe hemophilia A; not tied to platelet release disorders |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | Completed | 74 | BIVV001 in previously treated children <12 years with severe hemophilia A; same limitation |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | Recruiting | 45 | Systemic and portal hemostasis in patients undergoing TIPS placement; unrelated |

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13791P | Xyntha Powder and Solvent for Solution for Injection 250iu | Injection, powder, for solution | Not listed in registry record |
| SIN13792P | Xyntha Powder and Solvent for Solution for Injection 500iu | Injection, powder, for solution | Not listed in registry record |
| SIN13794P | Xyntha Powder and Solvent for Solution for Injection 1000iu | Injection, powder, for solution | Not listed in registry record |
| SIN13793P | Xyntha Powder and Solvent for Solution for Injection 2000iu | Injection, powder, for solution | Not listed in registry record |

Manufacturer: Wyeth Farma S.A, with Vetter Pharma-Fertigung GmbH & Co. KG (pre-filled syringe diluent).

---

## Safety Considerations

Please refer to the package insert for safety information.

The following points come from the mechanistic analysis in the Evidence Pack, not from labelling:
- Moroctocog alfa is a procoagulant product. It could add thrombotic risk in conditions that already tend toward thrombosis, such as thrombocytosis or thrombomodulin defects (predicted ranks 9 and 10).
- In acquired hemophilia A, autoantibodies against FVIII are expected to neutralise human rFVIII, which limits its usefulness.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.97%), but there is no credible mechanistic link between FVIII replacement and platelet release disorders. No trial or publication tests the drug for this indication, and the evidence level is L5. The prediction does not justify further investment as it stands.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, currently missing and blocking any safety screening
- Mechanism of action data from DrugBank, to support a proper mechanistic review
- The approved indication text for the Singapore registrations, which is empty in all four records
- A mechanistic or preclinical rationale showing how FVIII could benefit platelet function defects
- Consideration of "acquired coagulation factor deficiency" (rank 4) as a more plausible research question, with a specific focus on low-titre inhibitor cases, since standard care there uses bypassing agents or porcine FVIII

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

