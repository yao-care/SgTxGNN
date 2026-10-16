---
layout: default
title: Ganciclovir
parent: High Evidence (L1-L2)
nav_order: 468
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Ganciclovir: predicted new indication Cytomegalovirus pneumonia (evidence level L2). Approved use: Cytomegalovirus retinitis"
---

# Ganciclovir
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Ganciclovir: From Cytomegalovirus Retinitis to Cytomegalovirus Pneumonia

## One-Sentence Summary

Ganciclovir is an antiviral drug originally used for cytomegalovirus (CMV) retinitis and herpes simplex virus keratitis.
The TxGNN model predicts it may be effective for **Cytomegalovirus Pneumonia**,
with **1 clinical trial** (Phase 4, completed) and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cytomegalovirus retinitis; herpes simplex virus keratitis (no approved indication text is available from the Singapore licences) |
| Predicted New Indication | Cytomegalovirus pneumonia |
| TxGNN Prediction Score | 97.56% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ganciclovir is a guanosine analogue. It is phosphorylated by the viral UL97 kinase and then inhibits CMV DNA polymerase, which stops the virus from replicating. Detailed mechanism of action data was not available in the structured drug record, but this mechanism is well established in the published literature and in the analysis compiled for this report.

The original indication (CMV retinitis) and the predicted indication (CMV pneumonia) are caused by the same pathogen. The prediction is therefore an extension to another organ site, not a new mechanism. Ganciclovir is already regarded as first-line therapy for life- or sight-threatening CMV disease in immunocompromised patients. Older studies in bone marrow transplant recipients also describe its use, often with intravenous immunoglobulin, for CMV pneumonia.

The high score is consistent with this biological logic. The main caveat is that the available trial tests preemptive treatment in ICU patients, not treatment of established CMV pneumonia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02152358](https://clinicaltrials.gov/study/NCT02152358) | Phase 4 | Completed | 317 | Randomised, double-blind trial of preemptive ganciclovir (CMV viraemia) or aciclovir (HSV) in ventilated ICU patients; the primary aim is to increase ventilator-free days at Day 60. Results are not summarised in the data compiled. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39774866](https://pubmed.ncbi.nlm.nih.gov/39774866/) | 2025 | Review | Intensive Care Medicine | Presentation, risk factors and management of CMV infection in immunocompromised ICU patients |
| [32134483](https://pubmed.ncbi.nlm.nih.gov/32134483/) | 2020 | Review | J Infect Dis | Ganciclovir and valganciclovir used for prevention and treatment of CMV in transplant patients; new therapies in development |
| [8668848](https://pubmed.ncbi.nlm.nih.gov/8668848/) | 1995 | Review | Semin Respir Infect | CMV pneumonia is severe in allogeneic bone marrow transplant recipients (almost 100% mortality if untreated); faster diagnosis allows earlier therapy |
| [8274605](https://pubmed.ncbi.nlm.nih.gov/8274605/) | 1993 | Review | Clin Infect Dis | Prevention and treatment of CMV pneumonia in transplant recipients; ganciclovir increasingly important for early prevention |
| [2161731](https://pubmed.ncbi.nlm.nih.gov/2161731/) | 1990 | Review | Drugs | Ganciclovir should be considered first-line for life- or sight-threatening CMV infection in immunocompromised patients |
| [2847610](https://pubmed.ncbi.nlm.nih.gov/2847610/) | 1988 | Cohort | Ann Intern Med | Ganciclovir plus intravenous CMV immunoglobulin for CMV pneumonia after bone marrow transplant |
| [2847609](https://pubmed.ncbi.nlm.nih.gov/2847609/) | 1988 | Case report | Ann Intern Med | CMV interstitial pneumonitis after allogeneic transplant treated with ganciclovir plus high-dose immune globulin |
| [2847292](https://pubmed.ncbi.nlm.nih.gov/2847292/) | 1988 | Clinical series | Rev Infect Dis | 28 of 39 (72%) life- or sight-threatening CMV infections improved on ganciclovir |
| [3035246](https://pubmed.ncbi.nlm.nih.gov/3035246/) | 1987 | Clinical series | JAMA | 31 immunocompromised patients with severe CMV disease treated with intravenous ganciclovir |
| [11477447](https://pubmed.ncbi.nlm.nih.gov/11477447/) | 2001 | Retrospective review | Bone Marrow Transplant | CMV pneumonia in 16 of 795 autologous transplant recipients (2%), more frequent in seropositive patients |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05051P | CYMEVENE FOR INJECTION 500 mg | Powder for solution for injection | Not stated in the data compiled |
| SIN11778P | VIRGAN EYE GEL 1.5 mg/g | Ointment (eye gel) | Not stated in the data compiled |

Note: The injectable form is the one relevant to CMV pneumonia. The eye gel is a topical ocular product and would not be suitable for lung disease.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antiviral nucleoside analogue, not a conventional anticancer drug. It acts on cellular DNA synthesis and is haematotoxic. |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The knowledge graph links ganciclovir to neutropenia, thrombocytopenia, anaemia and agranulocytosis as contraindicated conditions. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential and platelets; renal function |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Contraindicated conditions (knowledge graph, not label text)**:
  - Blood disorders: neutropenia, agranulocytosis, thrombocytopenia, anaemia, cyclic haematopoiesis
  - Kidney disease
  - Respiratory conditions: COPD, asthma, respiratory failure
  - Cardiovascular conditions: aortic stenosis and valve disease, acute coronary syndrome, hypotensive disorders, atrioventricular block
  - Eye conditions: uveitis, conjunctivitis, other inflammatory eye diseases

  These associations come from a knowledge graph and should be checked against the official package insert.

- **Drug Interactions**: 100 interactions were recorded. The Moderate-level ones are:
  - Amphotericin B (including the lipid complex, cholesteryl sulfate and liposomal forms)
  - Trospium
  - Nitisinone

  Other listed interactions (for example calcitriol, doxycycline, vancomycin, proton pump inhibitors, morphine, prednisone) have an unknown severity level.

Package insert warnings and contraindications could not be retrieved. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
CMV pneumonia is caused by the same virus as ganciclovir's established indication, and a completed randomised Phase 4 trial and decades of clinical reports support its use. Nevertheless, the trial tested a preemptive strategy in ICU patients, not treatment of established CMV pneumonia, and no pivotal Phase 3 trial exists for this indication. The safety data are also incomplete.

**To proceed, the following is needed:**
- The package insert (warnings and contraindications) from the Singapore Health Sciences Authority (HSA) to complete the safety screening
- Results of NCT02152358, and evidence specific to treatment of established CMV pneumonia
- Confirmation of the approved indication text for the Singapore injectable product (CYMEVENE)
- A haematological and renal monitoring plan, especially for transplant and other immunocompromised patients
- A DrugBank mechanism of action record to formally document the mechanistic link
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

