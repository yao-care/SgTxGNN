---
layout: default
title: Capecitabine
parent: Low Evidence (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: From Cancer Chemotherapy to Gastric Adenocarcinoma and Proximal Polyposis of the Stomach

## One-Sentence Summary

Capecitabine is an oral chemotherapy drug that the body converts into 5-FU, and it is marketed in Singapore as an anticancer medicine. The TxGNN model predicts it may be effective for **gastric adenocarcinoma and proximal polyposis of the stomach**, a rare hereditary syndrome. **No clinical trials and no publications** were retrieved for this specific disease, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Gastric adenocarcinoma and proximal polyposis of the stomach |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not currently available. The evidence pack describes capecitabine as a prodrug that is converted to 5-FU in tumour tissue, where the activating enzyme thymidylate phosphorylase is enriched. 5-FU inhibits thymidylate synthase and is incorporated into RNA and DNA, which suppresses DNA synthesis.

That mechanism applies to gastric adenocarcinoma in general, which is why the model links the drug to this condition. However, this prediction concerns a rare hereditary syndrome, and no disease-specific data support it. The high score reflects the model's association with gastric adenocarcinoma, not evidence for this syndrome.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

The record lists 10 registrations in total. Five are shown below. The approved-indication text is not provided in the records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15464P | Intacape Film Coated Tablet 500 mg | Tablet, film coated | — |
| SIN15369P | Kapetral Film-Coated Tablet 500 mg | Tablet, film coated | — |
| SIN10678P | Xeloda Tablets 150 mg | Tablet, film coated | — |
| SIN15368P | Kapetral Film-Coated Tablet 150 mg | Tablet, film coated | — |
| SIN10677P | Xeloda Tablets 500 mg | Tablet, film coated | — |

## Cytotoxicity

This section is included because capecitabine is a fluoropyrimidine chemotherapy drug. The entries below reflect its drug class. The evidence pack contains no DrugBank toxicity data.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class) |
| Myelosuppression Risk | Medium |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for full details.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trials or publications support capecitabine in this rare hereditary syndrome, so the high TxGNN score is prediction only (L5). The mechanism is plausible for gastric adenocarcinoma as a whole, but it has not been shown for this specific disease.

**To proceed, the following is needed:**
- Disease-specific clinical or observational evidence for this syndrome
- The Singapore package insert, including approved indications and safety information
- Mechanism of action data from DrugBank
- Confirmation of whether capecitabine's existing gastric cancer use already covers this population

**Note on other predictions:** In the same evidence pack, the broader term *gastric tubular adenocarcinoma* (rank 2) is supported by multiple Phase 3 RCTs, such as CLASSIC and RESOLVE, and is rated L1 with a "Proceed with Guardrails" recommendation. Capecitabine may already be labelled for gastric cancer in some jurisdictions, so that finding may confirm an existing use rather than a new one. It would be the more productive direction to review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

