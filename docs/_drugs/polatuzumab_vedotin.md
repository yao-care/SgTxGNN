---
layout: default
title: Polatuzumab Vedotin
parent: Low Evidence (L5)
nav_order: 804
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Polatuzumab Vedotin: predicted new indication HER2 positive breast carcinoma (evidence level L5). Approved use: Not stated in the Singapore licence records. Literature indicates dif…"
monitor_inn: "Polatuzumab vedotin"
predicted_indications: ["HER2 positive breast carcinoma", "progesterone-receptor positive breast cancer", "normal breast-like subtype of breast carcinoma", "breast tumor luminal A or B", "progesterone-receptor negative breast cancer", "drug-induced osteoporosis", "acne (disease)", "antithrombin deficiency type 2", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis"]
---

# Polatuzumab Vedotin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Polatuzumab vedotin: From B-Cell Lymphoma to HER2-Positive Breast Carcinoma
{: .text-alpha }

## One-Sentence Summary

Polatuzumab vedotin is an anti-CD79b antibody-drug conjugate carrying the microtubule inhibitor MMAE, and it is marketed in Singapore as Polivy. The TxGNN model predicts it may be effective for **HER2-positive breast carcinoma**, but **no clinical trials and no relevant publications** support this prediction, so it rests on a computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records. Literature indicates diffuse large B-cell lymphoma (DLBCL) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From the published literature, polatuzumab vedotin is an antibody-drug conjugate. Its antibody targets CD79b, a component of the B-cell receptor. After binding, it is internalised and releases MMAE, which blocks cell division and induces apoptosis. Its established use is in diffuse large B-cell lymphoma.

CD79b is a B-cell marker and is not a recognised target in HER2-positive breast carcinoma. The only plausible link is the general cytotoxic activity of MMAE, which is already used in other breast cancer antibody-drug conjugates. That activity does not depend on CD79b. The high TxGNN score is therefore a computational prediction without a demonstrated mechanistic basis.

The other top predictions are other breast cancer subtypes, drug-induced osteoporosis, acne, and several hereditary coagulation disorders. For these, no mechanistic rationale exists, and the scores are likely knowledge-graph artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for HER2-positive breast carcinoma.

Nineteen publications were matched to a lower-ranked breast prediction (luminal A or B breast tumour). They concern DLBCL, not breast cancer, and appear to have been matched spuriously. Examples are the POLARIX trial (PMID [34904799](https://pubmed.ncbi.nlm.nih.gov/34904799/)) and the GO29365 update (PMID [34749395](https://pubmed.ncbi.nlm.nih.gov/34749395/)). They should not be counted as support for any breast cancer indication. They do show that the approved lymphoma use of the drug is well documented.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16345P | POLIVY Powder for Concentrate for Solution for Infusion 30mg | Injection, powder, lyophilised, for solution | Not stated in the licence data |
| SIN16007P | POLIVY Powder for Concentrate for Solution for Infusion 140mg | Injection, powder, lyophilised, for solution | Not stated in the licence data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic payload (MMAE, microtubule inhibitor) |
| Myelosuppression Risk | Medium to high (myelosuppression is a recognised risk with this class; please refer to the package insert) |
| Emetogenicity Classification | Low to moderate (please refer to the package insert) |
| Monitoring Items | CBC with differential, liver function, signs of peripheral neuropathy and infection |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 entries, all from DDInter. Examples of those listed as **Major** are clarithromycin, cobicistat, deferiprone and samarium (153Sm) lexidronam. Many others are **Moderate**, such as aprepitant, cimetidine, simvastatin, rosuvastatin, ticagrelor, metronidazole, chloroquine and hydroxychloroquine. Interactions involving strong CYP3A inhibitors should be reviewed carefully, because MMAE exposure may rise.
- **Other considerations**: Peripheral neuropathy, myelosuppression and infection are known concerns for this drug class. This is a risk-benefit issue for any non-lymphoma use.

Please refer to the package insert for key warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no trials or relevant publications, and no recognised mechanism, because CD79b is specific to B-cell malignancies. The drug has a significant toxicity profile, so the risk-benefit balance is unproven.

**To proceed, the following is needed:**
- Evidence of target expression or a rationale independent of CD79b, for example preclinical data in HER2-positive breast cancer models
- Mechanism of action data confirmed from DrugBank
- Warnings and contraindications from the HSA package insert, and approved indication text for the Singapore licences
- A systematic literature and trial search specific to breast cancer, since the retrieved publications are all lymphoma-related
- A safety assessment of the drug interactions, especially the Major-level ones
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

