---
layout: default
title: Albendazole
parent: High Evidence (L1-L2)
nav_order: 47
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Albendazole: predicted new indication Alveolar echinococcosis (evidence level L2). Approved use: Cystic echinococcosis, cysticercosis"
---

# Albendazole
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Albendazole: From Cystic Echinococcosis and Cysticercosis to Alveolar Echinococcosis

## One-Sentence Summary

Albendazole is a benzimidazole anthelmintic, originally used to treat cystic echinococcosis (hydatid disease) and cysticercosis.
The TxGNN model predicts it may be effective for **alveolar echinococcosis**, with **3 clinical trials** and **20 publications** compiled for this direction (1 completed Phase 2 trial in early-stage disease, 194 patients).
Albendazole is already the guideline-recommended parasitostatic standard of care for this disease, so this is largely an extension of existing practice.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic echinococcosis, cysticercosis (the Singapore licence records contain no approved-indication text, so these are taken from the knowledge-graph indication data) |
| Predicted New Indication | Alveolar echinococcosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the structured drug record. Based on the literature compiled for this report, albendazole is a benzimidazole that binds parasite beta-tubulin and inhibits microtubule polymerization. This impairs glucose uptake and energy metabolism in the larval (metacestode) stage of the parasite.

Alveolar echinococcosis is caused by *Echinococcus multilocularis*, a close relative of *E. granulosus*, which causes cystic echinococcosis, a labeled indication. The mechanism therefore carries over directly. Reviews describe albendazole as the long-term antiparasitic backbone for alveolar echinococcosis, usually given alongside surgery or when surgery is not possible.

One caveat: several reviews note that albendazole is **parasitostatic rather than parasiticidal** in alveolar echinococcosis, and that it can cause significant adverse effects. This is why new alternatives (e.g., pyronaridine) are being explored.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Completed | 194 | Albendazole treatment of early-stage alveolar echinococcosis found by ultrasound screening in Kyrgyzstan; directly relevant |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | NA | Completed | 50 | EchinoVISTA: markers of parasite viability to guide follow-up and treatment withdrawal in albendazole-treated hepatic AE; supports monitoring, not efficacy |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | NA | Unknown | 24 | Randomised trial of adjuvant albendazole versus placebo after pulmonary hydatid cyst resection; cystic rather than alveolar disease, small |

## Literature Evidence

Most items are reviews; no RCTs were identified in the compiled literature for this indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Review | Acta Tropica | Expert consensus on diagnosis and treatment of cystic and alveolar echinococcosis |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Review | Tidsskr Nor Legeforen | Alveolar echinococcosis: surgery plus prolonged antiparasitic treatment |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | World J Gastroenterol | Current management of liver echinococcosis; surgery is the cornerstone |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Review | Clin Microbiol Rev | 21st-century advances in echinococcosis diagnosis and treatment |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Review | Semin Liver Dis | Hepatic alveolar echinococcosis overview |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | Acta Tropica | No non-surgical option yet replaces albendazole or mebendazole |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Review | Parasite | Albendazole and mebendazole, and the search for alternatives |
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Observational study | J Antimicrob Chemother | 35 patients followed about 39 months on mebendazole or albendazole; long-term treatment outcomes |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | Review | Parasitology | Albendazole is not parasiticidal and can cause severe adverse effects; pyronaridine proposed as an alternative |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Preclinical | Antimicrob Agents Chemother | Solubilizing formulations to improve albendazole bioavailability in an AE rat model |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07903P | ALZENTAL TABLET 400 mg | Film-coated tablet | Not stated in the compiled record |
| SIN09954P | ALBENDOL-400 TABLET 400 mg | Tablet | Not stated in the compiled record |
| SIN14030P | Zentel Tablet 400mg | Chewable tablet | Not stated in the compiled record |

All three authorizations are valid single-ingredient oral products.

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: liver disease, gallbladder disease, neutropenia, agranulocytosis, anaemia (including macrocytic and aplastic anaemia), and pancytopenia. These suggest that liver function and blood counts need monitoring, especially in the prolonged treatment used for alveolar echinococcosis.
- **Drug Interactions**: 96 interactions were identified. Examples include moderate-level interactions with aprepitant, cobicistat, deferasirox, alemtuzumab, amprenavir, apalutamide, bendamustine, bosentan and others, and minor-level interactions with cimetidine, dexamethasone and lidocaine. Several of these (e.g., alemtuzumab, bendamustine, deferasirox) overlap with the blood-count concerns above.

Please refer to the package insert for the full warnings and precautions.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Albendazole is already the guideline-recommended parasitostatic therapy for alveolar echinococcosis, supported by a completed Phase 2 trial (194 patients) and consistent review literature. Evidence is graded L2 because it is based on one Phase 2 trial plus reviews and observational data, not multiple Phase 3 RCTs. The drug does not kill the parasite in this disease and requires long-term use, so safety monitoring is essential.

**To proceed, the following is needed:**
- The Singapore package-insert warnings and contraindications (not available in the data compiled for this report); the current licence records also lack approved-indication text
- Detailed mechanism-of-action data from DrugBank
- A monitoring plan for liver function and blood counts during long-term therapy
- Results from NCT07182305, to confirm efficacy and the dosing regimen (continuous versus cyclic)
- Review of the interaction list against typical co-medications in this patient group

---

**Other predicted indications (for reference):**
- **Coenurosis** and **Cestode infectious disease** (L1): supported by neurocysticercosis trials, a labeled-type disease. Evidence for coenurosis itself is limited to one case report. Proceed with Guardrails.
- **Intestinal helminthiasis** (L1): an established use, with many Phase 2/3 trials and mass-treatment programs. Efficacy against *Trichuris* with a single dose is lower, and resistance has been documented. Proceed with Guardrails.
- **Dermatofibrosarcoma protuberans, lung hilum carcinoma, fibroma of lung, inclusion body myopathy with Paget disease/FTD** (L5): prediction only, with no supporting trials or literature. Hold.
- **Lung benign neoplasm** (L4) and **hamartoma of lung** (L5): the literature retrieved is about parasitic cysts that mimic lung masses or about preclinical lung cancer studies. It does not support the predicted indications. Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

