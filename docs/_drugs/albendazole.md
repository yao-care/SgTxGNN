---
layout: default
title: Albendazole
parent: High Evidence (L1-L2)
nav_order: 47
evidence_level: L2
indication_count: 10
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

# Albendazole: From Anthelmintic Use to Alveolar Echinococcosis

## One-Sentence Summary

Albendazole is a broad-spectrum anthelmintic (anti-worm) drug marketed in Singapore under 3 registrations; the registration data do not state its approved indication.
The TxGNN model predicts it may be effective for **alveolar echinococcosis**, a severe parasitic liver disease caused by *Echinococcus multilocularis*.
Currently **5 clinical trials** (only 1 directly tests albendazole in this disease) and **20 publications** support this direction. Albendazole is already the standard drug therapy for this disease, so this is closer to confirming an established use than discovering a new one.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration data (albendazole is an anthelmintic) |
| Predicted New Indication | Alveolar echinococcosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the drug record. Albendazole is a benzimidazole that binds parasite beta-tubulin, disrupting microtubule-dependent glucose uptake in *Echinococcus* larvae. It is **parasitostatic rather than parasiticidal**: it slows parasite growth but does not kill it. This fits its role as long-term suppressive therapy and as an adjunct to surgery.

Alveolar echinococcosis is a tapeworm-larva disease. It behaves like a slow-growing liver tumour and is close to universally fatal without treatment. Albendazole is used against intestinal worms and other tapeworm diseases, so its activity against *Echinococcus* larvae is mechanistically plausible. Reviews and consensus guidance in the evidence set describe benzimidazoles (albendazole or mebendazole) as the only recommended drug treatment.

The high TxGNN score is consistent with this. Because the original indication is missing from the record, this may already be an established or guideline-endorsed use rather than true repurposing. That should be checked against the local label.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Completed | 194 | Albendazole treatment in early-stage alveolar echinococcosis found by ultrasound screening in Kyrgyzstan. This is the only direct treatment trial. Randomization and endpoints are not stated in the provided data. |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | N/A | Completed | 50 | Observational study of parasite viability and follow-up markers in albendazole-treated patients, to guide when to stop treatment. |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | N/A | Unknown | 24 | Randomized trial of adjuvant albendazole vs placebo after pulmonary hydatid cyst resection. This is the cystic form of the disease, but the parasite genus and drug question are closely related. |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | N/A | Recruiting | 43 | Diagnostic multiplex qPCR evaluation. It does not test a treatment. |
| [NCT07176598](https://clinicaltrials.gov/study/NCT07176598) | N/A | Completed | 1 | Single case report of an intramuscular hydatid cyst. No efficacy signal. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Expert consensus | Acta Trop | WHO-IWGE consensus on diagnosis, treatment and follow-up of cystic and alveolar echinococcosis. |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | Parasite | Benzimidazoles are the only recommended drugs for AE. They are parasitostatic, the parasite can resume growth when treatment stops, and they can cause liver dysfunction. |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Review | Tidsskr Nor Legeforen | AE mainly attacks the liver. Treatment is often extensive surgical resection plus prolonged albendazole. |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Review | Zhongguo Xue Xi Chong Bing Fang Zhi Za Zhi | Albendazole can delay progression in patients who cannot or will not have surgery. |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Review | Clin Microbiol Rev | 21st-century advances in echinococcosis genetics, diagnostics and treatment. |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Review | Semin Liver Dis | Overview of hepatic AE, a rare but severe zoonosis with resurgence in endemic areas. |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | World J Gastroenterol | Surgery is the cornerstone of management. Hepatic AE resembles carcinoma and can be fatal untreated. |
| [12667231](https://pubmed.ncbi.nlm.nih.gov/12667231/) | 2003 | Review | Fundam Clin Pharmacol | Albendazole is an important component of management for both cystic and alveolar echinococcosis. |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Preclinical (rat) | Antimicrob Agents Chemother | Solubilized albendazole formulations were developed to overcome poor oral bioavailability in a hepatic AE rat model. |
| [34688631](https://pubmed.ncbi.nlm.nih.gov/34688631/) | 2022 | Preclinical (animal) | Acta Trop | Carvacrol plus albendazole enhanced efficacy over monotherapy in experimental AE. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07903P | ALZENTAL TABLET 400 mg (Shin Poong Pharmaceutical) | Tablet, film coated | Not stated in provided data |
| SIN09954P | ALBENDOL-400 TABLET 400 mg (Micro Labs) | Tablet | Not stated in provided data |
| SIN14030P | Zentel Tablet 400mg (Haleon South Africa) | Tablet, chewable | Not stated in provided data |

All three products are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were retrieved.

One point from the literature: reviews note that benzimidazole therapy for AE is long-term and can cause liver dysfunction (PMID 39311470), so liver monitoring is expected during prolonged use.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Albendazole has a plausible mechanism, consensus guidance and reviews supporting its use in alveolar echinococcosis, and one completed Phase 2 treatment trial (n=194). There is no confirmed randomized comparative efficacy data, and the drug is parasitostatic, so evidence sits at L2.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (currently a blocking gap for safety screening)
- Confirmation of the approved indications on the Singapore labels, to establish whether AE is already covered
- Mechanism-of-action data from DrugBank
- Results and design details (randomization, endpoints) of NCT07182305
- A long-term monitoring plan (liver function, blood counts) and a treatment-duration or withdrawal strategy, given the parasitostatic action

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

