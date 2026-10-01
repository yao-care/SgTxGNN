---
layout: default
title: Enfortumab Vedotin
parent: Low Evidence (L5)
nav_order: 372
evidence_level: L5
indication_count: 10
---

# Enfortumab Vedotin
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

# Enfortumab Vedotin: From Urothelial Cancer to Leprosy

## One-Sentence Summary

Enfortumab vedotin is a Nectin-4-directed antibody-drug conjugate (ADC) used in oncology. The HSA record supplied does not state its approved indication, so urothelial cancer here comes from general knowledge of the drug. The TxGNN model predicts it may be effective for **leprosy**, but **no clinical trials and no publications** support this, and the score most likely reflects a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urothelial cancer (not listed in the HSA record; based on the drug's known use) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. From what is known, enfortumab vedotin is an ADC that targets Nectin-4 on tumour cells and delivers the cytotoxic payload MMAE. Its activity is designed for Nectin-4-expressing cancers.

Leprosy is a bacterial infection caused by *Mycobacterium leprae*. There is no plausible mechanistic link between a Nectin-4-directed cytotoxic ADC and treating this infection. The high score therefore looks like an artifact of the knowledge graph rather than a real repurposing signal. This prediction should not be treated as a credible candidate without independent supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16502P | PADCEV® 20 mg/vial, powder for concentrate for solution for infusion | Lyophilised powder for injection |
| SIN16503P | PADCEV® 30 mg/vial, powder for concentrate for solution for infusion | Lyophilised powder for injection |

Both products are manufactured by Baxter Oncology GmbH. The approved indication text is not listed in the supplied record.

## Cytotoxicity

This section reflects general knowledge of the drug class, not data in the supplied record. Please verify it against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy: antibody-drug conjugate with an MMAE (microtubule-disrupting) payload |
| Myelosuppression Risk | Medium (neutropenia is the main concern) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function, blood glucose, skin reactions, peripheral neuropathy |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

For the infection-related predictions (leprosy, cytomegalovirus infection, candidiasis, HIV), myelosuppression and immune effects from a cytotoxic ADC could worsen infection risk rather than help.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trial or literature support, and no mechanistic link between a Nectin-4-directed ADC and leprosy. The evidence level is L5 (model prediction only).

Among the 10 predicted indications, only **HER2-positive breast carcinoma** (rank 10, score 98.99%, L4) has any supporting material. It is indirect: the EV-202 basket study [NCT04225117](https://clinicaltrials.gov/study/NCT04225117) tests enfortumab vedotin in solid tumours, but it is single-arm Phase 2, and its breast cohorts appear to be HER2-negative or triple-negative. This is a research question, not a recommendation, and it needs verification.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (currently blocking for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text from the HSA record
- If pursuing the breast cancer direction, confirmation of the EV-202 cohort details and of Nectin-4/HER2 co-expression
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

