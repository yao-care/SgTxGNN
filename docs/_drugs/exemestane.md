---
layout: default
title: Exemestane
parent: Medium Evidence (L3-L4)
nav_order: 414
evidence_level: L4
indication_count: 10
---

# Exemestane
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

# Exemestane: From Breast Cancer to Amenorrhea

## One-Sentence Summary

Exemestane is a steroidal aromatase inhibitor that lowers estrogen levels. It is marketed in Singapore as a 25 mg tablet, but the registered indication text is not available in the data compiled for this report.
The TxGNN model ranks **amenorrhea** as its second-highest prediction, but this is an expected pharmacological effect of estrogen suppression rather than a therapeutic goal.
Evidence is limited to **0 clinical trials** and **5 indirect publications**, so this is a weak repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the registration data (the drug is an aromatase inhibitor) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

The top-ranked prediction was antithrombin deficiency type 2 (99.83%). It has no supporting evidence and no plausible mechanism, so this report focuses on the second-ranked prediction, amenorrhea, which is the first with any literature. The other predictions are summarised at the end.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Exemestane is known to be a steroidal aromatase inhibitor. It blocks the conversion of androgens to estrogens, which lowers circulating estradiol.

Amenorrhea (absence of menstruation) can follow when estrogen is suppressed. In this sense the prediction reflects a real pharmacological effect of the drug. However, this is an expected or adverse effect, not a therapeutic benefit. Amenorrhea is a symptom of many underlying conditions, and inducing it is not a treatment goal. The prediction most likely reflects the drug's estrogen-lowering action rather than a true repurposing opportunity.

The retrieved papers concern ovarian suppression and recovery of ovarian function in breast cancer patients. They are indirect context only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23108951](https://pubmed.ncbi.nlm.nih.gov/23108951/) | 2013 | Cohort | Ann Oncol | Incidence and predictors of ovarian function recovery in breast cancer patients with chemotherapy-induced amenorrhea who switched from tamoxifen to exemestane |
| [26178334](https://pubmed.ncbi.nlm.nih.gov/26178334/) | 2015 | Review | Oncology (Williston Park) | Role of ovarian suppression in premenopausal women with hormone receptor-positive early breast cancer; chemotherapy-induced amenorrhea linked to better survival |
| [31379370](https://pubmed.ncbi.nlm.nih.gov/31379370/) | 2019 | Review | Recenti Prog Med | Current role of LHRH analogues in early and advanced breast cancer in premenopausal patients |
| [28118723](https://pubmed.ncbi.nlm.nih.gov/28118723/) | 2016 | Review | Klin Onkol | Aromatase inhibitor treatment in postmenopausal breast cancer and management of side effects; AIs are contraindicated in women with functional ovaries |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Review / clinical commentary | J Clin Oncol | Whether estradiol monitoring is needed in women receiving ovarian suppression for breast cancer |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11398P | AROMASIN TABLET 25mg (Pfizer Italia S.r.l.) | Tablet, sugar coated | Not available |
| SIN15232P | AROMASTAN F.C. TABLET 25MG (S.C. Sindan-Pharma S.R.L.) | Tablet, film coated | Not available |
| SIN14757P | EXEMESTANE STADA FILM COATED TABLET 25mg (EirGen Pharma Ltd.) | Tablet, film coated | Not available |
| SIN16646P | EXEDRAL 25 FILM-COATED TABLET 25MG (Remedica Ltd) | Tablet, film coated | Not available |
| SIN16062P | EXACCORD 25 FILM COATED TABLET 25 MG (Intas Pharmaceuticals Limited) | Tablet, film coated | Not available |

All five licences are valid single-ingredient oral products.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (steroidal aromatase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Low; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert warnings and precautions (bone density and lipids are commonly considered for aromatase inhibitors) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: A screen found 100 potential interactions. The only ones graded Moderate are **dexamethasone** and **troglitazone**. Other listed drugs, including pantoprazole, morphine, metformin, omeprazole, simvastatin, rosuvastatin and aspirin, have no assigned severity level.

For warnings and contraindications, please refer to the package insert, since this information was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The amenorrhea prediction has a high model score but no clinical trials, and the literature is indirect. Amenorrhea is an expected effect of estrogen suppression, not a treatable condition, so it is not a meaningful repurposing target. The other nine predictions have no evidence (L5). Several are thrombophilia-related genetic disorders with no plausible mechanistic link, such as antithrombin deficiency type 2, factor 5 excess and heparin cofactor 2 deficiency. Estrogen lowering could plausibly worsen migraine, and acne is a recognised side effect of the drug class.

**Other predictions in brief:**
- **Breast fibrocystic disease** (rank 10, 95.7%) is the most biologically plausible candidate because it is estrogen-responsive, but menopausal-range estrogen suppression is a poor fit for a benign condition. It is worth a literature review as a research question.
- **Thrombophilia** has only a theoretical link through estrogen and thrombotic risk.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Registered indication text for the Singapore licences
- A targeted literature review of aromatase inhibitors in fibrocystic breast disease
- Clinical rationale for any therapeutic use of amenorrhea, or confirmation that this prediction should be dismissed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

