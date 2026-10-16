---
layout: default
title: Eltrombopag
parent: Low Evidence (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Eltrombopag: predicted new indication HIV infectious disease (evidence level L5). Approved use: Autoimmune thrombocytopenia"
monitor_inn: "Eltrombopag"
predicted_indications: ["HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "female breast carcinoma", "obsolete familial combined hyperlipidemia", "homozygous familial hypercholesterolemia", "AIDS", "rheumatoid arthritis", "cholecystolithiasis"]
---

# Eltrombopag
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

# Eltrombopag: From Autoimmune Thrombocytopenia to HIV Infectious Disease

## One-Sentence Summary

Eltrombopag is an oral thrombopoietin (TPO) receptor agonist, originally used to treat autoimmune thrombocytopenia.
The TxGNN model predicts it may be useful for **HIV infectious disease**, with **1 clinical trial** (a terminated Phase 3 study in a related thrombocytopenia setting) and **8 publications** (mostly case reports and reviews) currently supporting this direction.
The likely benefit is supportive, treating HIV-associated low platelet counts rather than the virus itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Autoimmune thrombocytopenia (from the knowledge graph; no approved indication text is available in the Singapore licence records) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 per the data compiled for this report; in practice weaker (see below) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, eltrombopag is a TPO receptor agonist. It stimulates platelet production in the bone marrow, and its efficacy in autoimmune thrombocytopenia is established.

HIV infection can cause persistent thrombocytopenia, including immune thrombocytopenia (ITP)-like forms and immune reconstitution-related forms. Because eltrombopag raises platelet counts regardless of the underlying cause, it may be applicable here. Case reports describe platelet responses in refractory HIV-related thrombocytopenia, and one report describes a response in HIV-associated aplastic anaemia, with a possible immunomodulatory effect.

The benefit is **supportive, not antiviral**. A 2020 in vitro screening study (PMID 32977702) suggests eltrombopag may modulate HIV-1 proviral transcription, but this is preclinical and only hypothesis-generating.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00678587](https://clinicaltrials.gov/study/NCT00678587) | Phase 3 | Terminated | 292 | Randomised, double-blind, placebo-controlled study of eltrombopag to reduce platelet transfusions in thrombocytopenic patients with chronic liver disease undergoing elective invasive procedures (2008-06 to 2009-10) |

**Caveat:** this trial studied chronic liver disease, not HIV directly. It was terminated early, and its population relevance to HIV should be verified. The L1 level therefore rests on a single terminated trial and should be read cautiously.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25504472](https://pubmed.ncbi.nlm.nih.gov/25504472/) | 2015 | Case series | J Int Assoc Providers AIDS Care | Thrombopoietin receptor agonists in refractory HIV-associated ITP |
| [22992580](https://pubmed.ncbi.nlm.nih.gov/22992580/) | 2012 | Case report | AIDS | Eltrombopag used successfully without splenectomy in refractory HIV-related immune reconstitution thrombocytopenia |
| [25333665](https://pubmed.ncbi.nlm.nih.gov/25333665/) | 2014 | Case report | AIDS | Eltrombopag treated HIV-associated severe aplastic anaemia with a trilineage response and signs of immunomodulation |
| [19932434](https://pubmed.ncbi.nlm.nih.gov/19932434/) | 2009 | Review | Hematol Oncol Clin North Am | Infectious causes (HCV, HIV, H. pylori) of chronic immune thrombocytopenia |
| [19245929](https://pubmed.ncbi.nlm.nih.gov/19245929/) | 2009 | Review | Semin Hematol | Therapeutic strategies for hepatitis- and other infection-related immune thrombocytopenias |
| [32977702](https://pubmed.ncbi.nlm.nih.gov/32977702/) | 2020 | In vitro screening | Viruses | FDA-approved drug library screened for modulators of HIV-1 proviral transcription |
| [28043314](https://pubmed.ncbi.nlm.nih.gov/28043314/) | 2016 | Case report | J Coll Physicians Surg Pak | Hepatitis B leading to megaloblastic anaemia and severe thrombocytopenia (indirectly related) |
| [24128106](https://pubmed.ncbi.nlm.nih.gov/24128106/) | 2013 | Case report | Farm Hosp | Eltrombopag for thrombocytopenia in chronic hepatitis C (two cases; indirectly related) |

No randomised controlled trial in HIV was found.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13909P | Revolade Tablet 25mg | Film-coated tablet | Not stated in the licence record |
| SIN13910P | Revolade Tablet 50mg | Film-coated tablet | Not stated in the licence record |

Both licences are valid single-ingredient oral products, with no cancelled registrations.

## Safety Considerations

- **Drug Interactions:** 100 interactions were found in total. Most are Moderate and involve polyvalent cation products, such as calcium salts (carbonate, acetate, citrate, gluconate, lactate), magnesium salts, aluminium hydroxide, iron, kaolin, attapulgite and magaldrate. Eluxadoline is a **Major** interaction. Glyburide is a Moderate interaction.
- **Disease-level contraindication signals (knowledge graph, not label text):** kidney disease, liver disease (including acute liver failure, hepatitis, hepatic vein thrombosis and Budd-Chiari syndrome), gallbladder disease, hyperbilirubinaemia (including Gilbert syndrome), anaemia, leukopenia, myelodysplastic syndrome and thrombocytosis. These come from graph edges and need confirmation against the package insert.

Please refer to the package insert for authoritative warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence supports eltrombopag as supportive treatment for HIV-associated thrombocytopenia, based on consistent case-level reports and its established platelet-raising effect. There is no evidence of antiviral activity in humans. The single Phase 3 trial was terminated and studied chronic liver disease, so the L1 label overstates the strength of the HIV-specific evidence.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications and approved indications), a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- HIV-specific controlled data, or a confirmed HIV subgroup from the Phase 3 trial
- A hepatic monitoring plan, since the knowledge graph flags liver disease, and a plan for cation-containing co-medications
- A clear framing of the indication as thrombocytopenia in HIV rather than HIV treatment

**Other predictions in the list:**
- **AIDS** (score 97.1%) largely duplicates the HIV entry and should be evaluated together with it.
- **Female breast carcinoma** (98.6%) has preclinical evidence only (HuR targeting, apoptosis in cell lines) and is a research question, not a clinical candidate.
- **Rheumatoid arthritis** (96.8%) has evidence only for secondary thrombocytopenia in autoimmune disease, not disease-modifying activity, so it is also a research question.
- The remaining predictions (veterinary and animal-model immunodeficiency conditions, a rare neurodevelopmental disorder, familial hyperlipidaemia terms, cholecystolithiasis) have no supporting evidence and should be held.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

