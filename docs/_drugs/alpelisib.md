---
layout: default
title: Alpelisib
parent: Low Evidence (L5)
nav_order: 67
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Alpelisib: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not recorded in the Singapore licence data (the trials compiled point…"
monitor_inn: "Alpelisib"
predicted_indications: ["pulmonary hypertension"]
---

# Alpelisib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Alpelisib: From Breast Cancer (Indication Text Not Recorded in Local Licences) to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Alpelisib is an oral PI3K-alpha inhibitor marketed in Singapore as Piqray. The clinical trials in the data compiled for this report are all in breast or ovarian cancer.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are **0 clinical trials** and only **1 publication** (a case report of alpelisib-induced lung disease), so this prediction rests almost entirely on the model.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Singapore licence data (the trials compiled point to HR+/HER2- PIK3CA-mutated advanced breast cancer) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 0.9903 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 3 of 3) |
| Number of Registrations | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for alpelisib: "Alpelisib is an inhibitor of phosphatidylinositol-3-kinase (PI3K) with inhibitory activity predominantly against PI3Kα. Gain-of-function mutations in the gene encoding the catalytic α-subunit of PI3K (PIK3CA) lead to activation of PI3Kα and Akt-signaling, cellular transformation and the generation of tumors in in vitro and in vivo models." ([DailyMed: Piqray (alpelisib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b20b4e18-7a4b-4500-a08f-06c6dab0ee5b), label version 2026-10-28; accessed 2026-11-19.) Alpelisib is known to be a selective PI3K-alpha inhibitor. Its efficacy in PIK3CA-mutated advanced breast cancer was shown in the Phase 3 SOLAR-1 trial (NCT02437318).

PI3K/AKT signalling has been implicated in pulmonary vascular remodelling and smooth muscle proliferation. Inhibiting PI3K-alpha is therefore theoretically plausible for pulmonary hypertension.

However, the only publication linked to this prediction reports **alpelisib-induced interstitial lung disease**. That is a pulmonary safety signal, not evidence of benefit. The high model score is not backed by clinical data, and the pulmonary toxicity signal argues for caution.

## Clinical Trial Evidence

Currently no related clinical trials registered for pulmonary hypertension.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case report | J Oncol Pharm Pract | Alpelisib-induced interstitial lung disease in a patient with advanced breast cancer; a safety signal, not efficacy evidence |

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN15917P | PIQRAY 300MG DAILY DOSE PACK (150mg + 150mg) | TABLET, FILM COATED | Valid |
| SIN15918P | PIQRAY 200MG DAILY DOSE PACK | TABLET, FILM COATED | Valid |
| SIN15916P | PIQRAY 250MG DAILY DOSE PACK (200mg + 50mg) | TABLET, FILM COATED | Valid |

<!-- licenses:end -->

All three licences are held by Novartis Pharma Stein AG and are currently valid.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3K-alpha inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood glucose (hyperglycaemia is a recognised effect; a Phase 2 study, NCT04300790, tested metformin for prevention), plus respiratory symptoms given the reported interstitial lung disease |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found, and the 20 listed in the compiled data are all rated Moderate. Most involve antidiabetic drugs, including acarbose, metformin, pioglitazone, glimepiride, glipizide, alogliptin, and the SGLT2 inhibitors canagliflozin, dapagliflozin, empagliflozin and ertugliflozin. GLP-1 agonists (albiglutide, dulaglutide, exenatide) are also listed. Other interacting drugs include dexamethasone, bupropion, alosetron, dronabinol and fidaxomicin.
- **Pulmonary signal**: A published case report describes alpelisib-induced interstitial lung disease (PMID 35730191).

Please refer to the package insert for key warnings and contraindications, which were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (0.9903), but there are no clinical trials in pulmonary hypertension. The only linked publication is a case report of drug-induced lung disease, which is a safety concern. The mechanistic link through PI3K/AKT is plausible but unproven.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which block safety screening
- Mechanism of action data from DrugBank
- Preclinical evidence of PI3K-alpha inhibition in pulmonary vascular remodelling models
- An assessment of the interstitial lung disease risk in patients with pulmonary vascular disease
- The approved indication text for the Singapore licences

---

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Piqray (alpelisib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b20b4e18-7a4b-4500-a08f-06c6dab0ee5b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

