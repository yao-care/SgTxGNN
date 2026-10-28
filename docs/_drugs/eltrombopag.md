---
layout: default
title: Eltrombopag
parent: High Evidence (L1-L2)
nav_order: 369
evidence_level: L1
indication_count: 1
last_modified_at: 2026-10-14
monitor_inn: "Eltrombopag"
predicted_indications: ["HIV infectious disease"]
description: "Eltrombopag: predicted new indication HIV infectious disease (evidence level L1). Approved use: Not recorded in the local data"
---

# Eltrombopag
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **1** 
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

## Eltrombopag: HIV infectious disease
{: .text-alpha }

## One-Sentence Summary

Eltrombopag is an oral thrombopoietin (TPO) receptor agonist, originally used to treat autoimmune thrombocytopenia.
The TxGNN model predicts it may be useful for **HIV infectious disease**, with **1 clinical trial** (a terminated Phase 3 study in a related thrombocytopenia setting) and **8 publications** (mostly case reports and reviews) currently supporting this direction.
The likely benefit is supportive, treating HIV-associated low platelet counts rather than the virus itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L1 per the data compiled for this report; in practice weaker (see below) |
| Singapore Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
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
- A clear framing of the indication as thrombocytopenia in HIV rather than HIV treatment

**Other predictions in the list:**
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

