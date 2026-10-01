---
layout: default
title: Abacavir
parent: Medium Evidence (L3-L4)
nav_order: 19
evidence_level: L4
indication_count: 10
---

# Abacavir
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

# Abacavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor (NRTI) used against HIV-1 infection. The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but there are **0 clinical trials** and only **1 publication** (an in vitro susceptibility study) behind this prediction. SIV is a non-human viral model, so this is not a human repurposing target.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from the drug class and the evidence pack; the registration records list no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Abacavir is an NRTI, a class of drugs that blocks the reverse transcriptase enzyme HIV uses to copy its genome. SIV reverse transcriptase is closely related to HIV-1 reverse transcriptase, so activity against SIV is biologically plausible. That is the likely reason the model scored this link so highly.

Detailed mechanism-of-action data is not available in the source record. The link rests on class knowledge: abacavir is an established antiretroviral, and its target enzyme is similar in the two viruses.

The only supporting evidence is a laboratory comparison of how susceptible HIV-2, SIV and SHIV strains are to anti-HIV drugs. There are no animal efficacy data, no human data and no trials. SIV infects non-human primates, so it is not a disease that would be treated in patients in Singapore. In practice, this prediction mainly confirms that abacavir's known antiretroviral mechanism has a plausible reach into related lentiviruses.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility study | Antiviral Therapy | Tested 16 approved anti-HIV drugs plus one experimental drug (AMD3100) against two HIV-2 isolates, two SIV strains and two SHIV strains. The abstract available in the evidence pack is truncated, so abacavir-specific results could not be confirmed. |

## Singapore Market Information

Five authorizations are on record. The registration data does not include approved indication text.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16114P | ABACAR Abacavir Tablets USP 300 mg | Film-coated tablet |
| SIN11098P | ZIAGEN Tablets 300 mg | Film-coated tablet |
| SIN15864P | ABALAM Abacavir Sulfate & Lamivudine Tablets 600/300 mg | Film-coated tablet |
| SIN13230P | Kivexa | Tablet |
| SIN15100P | TRIUMEQ Film Coated Tablet 50 mg/600 mg/300 mg | Film-coated tablet |

## Safety Considerations

Please refer to the package insert for safety information.

Other abacavir predictions in this evidence pack note a hypersensitivity risk in carriers of HLA-B*5701. HLA-B*5701 screening is therefore a standard precaution before use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on a single in vitro study, giving an L4 evidence level. SIV is a non-human viral model, so it is not a viable human repurposing target.
- The package insert safety data are missing, and the pack flags this as a blocking gap.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, downloaded and parsed.
- Mechanism-of-action data from DrugBank.
- The full text of PMID 15040537, to confirm abacavir-specific susceptibility results.
- Redirection of review effort to the human HIV-related predictions in the same pack. These include congenital HIV, where evidence is L1 with a "Proceed with Guardrails" recommendation, and AIDS related complex. Both largely overlap with abacavir's established use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

