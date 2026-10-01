---
layout: default
title: Nitrofurantoin
parent: Low Evidence (L5)
nav_order: 709
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is an oral antibacterial marketed in Singapore as 50 mg and 100 mg tablets. It is generally used for urinary tract infections, though the registration records here do not state an indication.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but there are **0 clinical trials** and no publications showing a benefit.
The retrieved literature describes nitrofurantoin as a source of harm in patients with rheumatoid arthritis, mainly lung toxicity and a drug interaction with methotrexate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records (nitrofurantoin is generally used for urinary tract infections) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 (no supporting efficacy evidence; see the note below) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

The L4 grade follows the Evidence Pack scoring. There are no trials, and the only observational study concerns antibiotics and RA flares, not nitrofurantoin as a treatment. In practice the prediction rests on the model score alone.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nitrofurantoin is a urinary antibacterial, and its use in urinary tract infection is well established. There is no known mechanistic link to the joint inflammation of rheumatoid arthritis, so no bridge between the two conditions can be assessed.

The TxGNN score (99.89%) comes from a knowledge-graph association, not from any demonstrated therapeutic effect. The retrieved papers show that the link between nitrofurantoin and rheumatoid arthritis appears mostly through adverse effects and co-occurring conditions:
- Rheumatoid arthritis patients are prone to lung disease, and nitrofurantoin is a known cause of drug-induced pulmonary fibrosis.
- One case report describes irreversible lung fibrosis in a patient given methotrexate and then nitrofurantoin.

The prediction is therefore best read as a graph artefact, not as a repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Ten of the 12 retrieved items were provided. No item tests nitrofurantoin as a treatment for rheumatoid arthritis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort (self-controlled case series) | Scientific Reports | Studied the association between antibiotic use and RA flares in about 32,000 newly diagnosed RA patients. It concerns antibiotics as a class, not nitrofurantoin as a treatment. |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Lists nitrofurantoin among drugs that cause pulmonary fibrosis. Notes that RA also predisposes to it. |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | Review of drug-induced interstitial lung disease. Names nitrofurantoin among the implicated antibiotics. |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Review | Revue de Pneumologie Clinique | Gold salt-induced lung disease with lymphocytic alveolitis. Not about nitrofurantoin as a treatment. |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Review | Der Internist | Overview of alveolitis and pulmonary fibrosis. No abstract available. |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | 57 RA patients hospitalised for interstitial lung fibrosis, with poor prognosis. Not about nitrofurantoin as a treatment. |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Cohort | Acta Medica Scandinavica | Bacteriuria treatment with short-term nitrofurantoin in middle-aged women. Concerns urinary infection, not RA. |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | A 94-year-old woman on long-term methotrexate developed irreversible pulmonary fibrosis after nitrofurantoin. |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | Autoimmune hepatitis versus drug-induced liver injury. Nitrofurantoin is listed as a possible cause. |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Annales de Dermatologie et de Vénéréologie | Phenylbutazone-induced sialadenitis. Nitrofurantoin is only mentioned as another reported cause. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00439P | AA PHARMA NITROFURANTOIN TABLET 50 mg (Apotex Inc) | Tablet | Not stated in the registration record |
| SIN00290P | AA PHARMA NITROFURANTOIN TABLET 100 mg (Apotex Inc) | Tablet | Not stated in the registration record |

Only oral tablets are registered.

## Safety Considerations

Please refer to the package insert for safety information. Package insert warnings and contraindications were not available in the Evidence Pack. No drug interaction records were found.

The retrieved literature raises these signals:
- **Pulmonary toxicity**: nitrofurantoin is repeatedly named as a cause of drug-induced pulmonary fibrosis and interstitial lung disease. This matters because RA itself affects the lungs.
- **Methotrexate interaction**: one case report describes irreversible pulmonary fibrosis after nitrofurantoin was given to an RA patient on long-term methotrexate. Methotrexate is a standard RA drug.
- **Liver injury**: nitrofurantoin is listed among drugs that can cause autoimmune-like hepatitis.
- **Methemoglobinemia and hemolysis**: an animal study and two neonatal case reports link nitrofurantoin to methemoglobin formation and hemolytic anaemia.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials and no literature showing benefit. The retrieved papers point mainly to harm in RA patients, including lung toxicity and a methotrexate interaction. Mechanism of action data is also missing, so no rationale for use in rheumatoid arthritis can be built.

The other nine predicted indications are also on Hold, and none has trial evidence:
- Methemoglobinemia (rank 10) has evidence that runs in the opposite direction, because nitrofurantoin causes methemoglobin formation.
- Sclerosing cholangitis (rank 7) conflicts with the drug's known hepatotoxicity.
- Diabetic nephropathy (rank 4) is limited by reduced renal function.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank)
- The HSA package insert (warnings and contraindications) for a safety screen
- Any preclinical or clinical evidence that nitrofurantoin has an anti-inflammatory effect relevant to RA
- The 2 retrieved literature items not provided in this Evidence Pack, for review
- Evidence that the lung, liver and methotrexate-interaction risks are acceptable in RA patients

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

