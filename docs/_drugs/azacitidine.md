---
layout: default
title: Azacitidine
parent: Low Evidence (L5)
nav_order: 127
evidence_level: L5
indication_count: 10
---

# Azacitidine
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

# Azacitidine: From an Established Hypomethylating Agent to Bulbar Polio (Top-Ranked Prediction)

## One-Sentence Summary

Azacitidine is a hypomethylating nucleoside analog that is already marketed in Singapore in injectable and oral forms. The TxGNN model ranks **bulbar polio** as its top predicted new indication, but this prediction has **0 clinical trials** and **0 publications** behind it. It is most likely a knowledge-graph artifact rather than a real biological signal.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Bulbar polio |
| TxGNN Prediction Score | 98.59% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Azacitidine is a DNA hypomethylating nucleoside analog, and its use is centred on blood cancers and related bone marrow disorders.

Bulbar polio is a viral infection of the motor neurons in the brainstem. Azacitidine has no known antiviral or neuroprotective activity against poliovirus, so there is no plausible mechanistic bridge from its known biology to this disease. The high score (0.986) is most likely a knowledge-graph association artifact.

Other indications from the same run (see the Conclusion) have a much more credible link, mainly in myelodysplastic disorders.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

The approved indication text is not available in the supplied registration records, so it is omitted from the table.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| SIN13801P | Vidaza powder for suspension for injection 100mg/vial | Injection, powder, for suspension | Baxter Oncology GmbH |
| SIN15875P | Avoxred powder for suspension for injection 100mg/vial | Injection, powder, lyophilized, for suspension | Dr. Reddy's Laboratories Limited |
| SIN16573P | Onureg film-coated tablets 300 mg | Tablet, film coated | Excella GmbH & Co. KG |
| SIN16572P | Onureg film-coated tablets 200 mg | Tablet, film coated | Excella GmbH & Co. KG |
| SIN15118P | Xpreza 100 injection 100 mg/vial | Injection | Natco Pharma Limited / Panacea Biotec Pharma Ltd. |

Two more registrations exist beyond the five listed. Both injectable and oral routes are available.

## Cytotoxicity

The classification below is based on the drug class, not on DrugBank toxicity data. Please confirm against the HSA package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (hypomethylating nucleoside analog) |
| Myelosuppression Risk | High (neutropenia and thrombocytopenia are expected) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Bulbar polio has no trials and no literature, and there is no biological rationale for azacitidine in poliovirus infection. This candidate should not advance.

**Other candidates from the same run:**

| Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|
| Refractory cytopenia of childhood | 98.20% | L3 | Retrospective pediatric MDS series (EWOG-MDS) and one Phase 2 trial terminated with 3 patients; worth a research question |
| Unclassified myelodysplastic syndrome | 98.10% | L3 | Registry and retrospective evidence only; the one linked trial is a colorectal cancer study and is irrelevant |
| Aregenerative anemia | 97.88% | L2 | Many azacitidine combination trials in MDS/AML, but few with anemia-specific endpoints; disease-term mapping needs confirmation |
| Partial deletion of the long arm of chromosome 5; severe congenital hypochromic anemia with ringed sideroblasts; 5q35 microduplication syndrome; neuralgic amyotrophy; amyotrophic neuralgia; familial thrombocytosis | 93.09–97.88% | L5 | No trials or literature; hold. Neuralgic amyotrophy and amyotrophic neuralgia appear to be duplicate nodes and should be merged |

**To proceed, the following is needed:**
- HSA package insert warnings, contraindications, and labeled indications (currently blocking any safety screening)
- Detailed mechanism of action data from DrugBank
- Confirmation of the labeled MDS subtypes before treating any myelodysplastic entry as a new indication
- Dedicated evidence review of the myelodysplastic and anemia entries, which are the only credible repurposing directions in this set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

