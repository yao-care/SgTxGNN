---
layout: default
title: Teriflunomide
parent: High Evidence (L1-L2)
nav_order: 968
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Teriflunomide: predicted new indication Relapsing-remitting multiple sclerosis (evidence level L1). Approved use: Multiple sclerosis"
monitor_inn: "Teriflunomide"
predicted_indications: ["relapsing-remitting multiple sclerosis", "marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "transient neonatal thrombocytopenia", "thrombocytopenia", "dense granule disease", "penile fibromatosis", "Ledderhose disease", "chronic hepatitis C virus infection", "palmar fibromatosis"]
---

# Teriflunomide
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Teriflunomide: From Multiple Sclerosis to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Teriflunomide is an oral immunomodulator originally used to treat multiple sclerosis.
The TxGNN model's top prediction is **relapsing-remitting multiple sclerosis (RRMS)**, which is effectively the original indication rather than a true repurposing case. It is supported by **12 clinical trials** (including 3 Phase 3 trials with direct relevance) and **20 publications**. A second, genuinely new direction is **thrombocytopenia** (immune thrombocytopenia, ITP), which has 4 early-phase trials and no efficacy results yet.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple sclerosis (the registration record has no indication text) |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, teriflunomide is the active metabolite of leflunomide. It inhibits the mitochondrial enzyme dihydroorotate dehydrogenase (DHODH), which limits de novo pyrimidine synthesis. Activated T and B lymphocytes depend heavily on this pathway to proliferate, so the result is a cytostatic, immunomodulatory effect.

RRMS is an autoimmune disease in which activated lymphocytes drive inflammatory demyelination. Reducing lymphocyte proliferation therefore fits the disease biology, and it is consistent with the established clinical use of teriflunomide. The high TxGNN score agrees with this. It is worth noting that this is the original approved indication, so the prediction mainly confirms existing knowledge.

The more interesting repurposing signal is **immune thrombocytopenia (ITP)**, ranked 5th with a score of 98.0%. Autoreactive T and B cells drive platelet destruction in ITP, so the same immunomodulatory mechanism is plausible. Several Phase 2 trials test teriflunomide with dexamethasone or danazol. One caution is a published case of leflunomide-induced thrombotic thrombocytopenic purpura. Leflunomide is the parent compound, so a haematological safety signal should be monitored.

The other eight predictions (for example hereditary thrombocytopenias, dense granule disease, fibromatoses and chronic hepatitis C) have no clinical or literature support and no clear mechanism. They are computational predictions only, and I would hold them.

## Clinical Trial Evidence

Trials for relapsing-remitting multiple sclerosis (the top prediction):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | Completed | 1088 | Pivotal placebo-controlled RCT of teriflunomide on relapse frequency and disability in relapsing MS |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | Completed | 324 | Teriflunomide (two doses) vs interferon beta-1a, rater-blinded, with long-term extension |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | Completed | 742 | Long-term extension documenting safety of teriflunomide 7 mg and 14 mg |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Phase 3 | Completed | 185 | Ofatumumab vs first-line DMT (physician's choice) in newly diagnosed relapsing MS |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | Completed | 147 | Extension of a Phase 2 study on long-term safety and efficacy |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | Completed | 106 | Observational real-world effectiveness study in RRMS |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | Completed | 30 | Mechanistic study of regulatory B lymphocytes in teriflunomide-treated RRMS |
| [NCT03561402](https://clinicaltrials.gov/study/NCT03561402) | N/A | Completed | 24 | Biomarkers associated with disease activity during teriflunomide treatment |

Trials for thrombocytopenia (ITP), the more notable repurposing direction:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06176911](https://clinicaltrials.gov/study/NCT06176911) | Phase 2 | Unknown | 124 | Teriflunomide plus danazol vs danazol in steroid-resistant/relapsed ITP |
| [NCT07065968](https://clinicaltrials.gov/study/NCT07065968) | Phase 2 | Recruiting | 132 | Teriflunomide plus high-dose dexamethasone vs dexamethasone alone, first-line ITP |
| [NCT06190145](https://clinicaltrials.gov/study/NCT06190145) | Phase 2 | Unknown | 40 | Single-arm safety and efficacy study in steroid-resistant/relapsed ITP |

A further ITP trial of the same design, NCT06176235, was withdrawn with 0 participants and provides no evidence. Several other MS trials in the compiled data (for example NCT06705608, NCT03500328, NCT07189325, NCT03535298 and NCT04260711) are strategy or other-drug studies with only indirect relevance to teriflunomide, so they are not listed.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network meta-analysis | Cochrane Database Syst Rev | Compares immunomodulators and immunosuppressants for RRMS |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | N Engl J Med | Tolebrutinib vs teriflunomide in relapsing MS |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | N Engl J Med | Ublituximab vs teriflunomide in relapsing MS |
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | N Engl J Med | Ofatumumab vs teriflunomide in MS |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | Lancet Neurol | Evobrutinib vs teriflunomide (evolutionRMS1 and 2) |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurol | Ponesimod vs teriflunomide (OPTIMUM) |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Teriflunomide review in RRMS: DHODH inhibition, effective and generally well tolerated |
| [40783682](https://pubmed.ncbi.nlm.nih.gov/40783682/) | 2025 | Systematic review / network meta-analysis | BMC Neurol | Comparative effectiveness of DMTs in highly active RRMS |
| [37578431](https://pubmed.ncbi.nlm.nih.gov/37578431/) | 2023 | Observational | Eur J Neurol | Real-world comparison of dimethyl fumarate and teriflunomide in RRMS |
| [34267852](https://pubmed.ncbi.nlm.nih.gov/34267852/) | 2021 | Case report | J Hematol | Leflunomide-induced thrombotic thrombocytopenic purpura (relevant to the ITP direction as a safety signal) |

In these head-to-head RCTs, teriflunomide mainly served as the active comparator for newer MS drugs.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14841P | AUBAGIO FILM-COATED TABLETS 14mg | Tablet, film coated | Not listed in the registration record |

The manufacturer is Opella Healthcare International SAS, the route is oral, and the licence status is valid.

## Cytotoxicity

Teriflunomide is an immunomodulator rather than an antineoplastic drug, so this section does not apply.

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screen. Of the 20 shown in the compiled data, most are Major:
  - Major examples include acarbose, pioglitazone, bupropion, acetylsalicylic acid, clarithromycin, minocycline, oxandrolone and oxymetholone.
  - Corticosteroids are also flagged as Major, including hydrocortisone, triamcinolone, dexamethasone, betamethasone and budesonide.
  - Moderate examples include alosetron, cimetidine, empagliflozin and sitagliptin.
  - Minor examples include zinc sulfate and zinc acetate.
- **Additional signals from the evidence reviewed**: Teriflunomide is teratogenic and carries a hepatotoxicity warning, which matters especially for neonatal or chronic liver disease indications. Leflunomide, the parent compound, has been linked to thrombotic thrombocytopenic purpura. These points come from general pharmacological knowledge and the evidence reviewed, not from the local package insert.

The warnings and contraindications from the Singapore package insert were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For RRMS, teriflunomide is already marketed in Singapore, and the evidence is strong, with multiple completed Phase 3 trials and many high-quality publications (L1). This is an existing indication, not a new repurposing opportunity. For ITP, the evidence is early (Phase 2, no results; L2), so it should be treated as a research question. The remaining predictions have no supporting evidence and should be held.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (a blocking gap for formal safety screening)
- Mechanism of action data from DrugBank to replace the general pharmacology summary
- The registered indication text for the Singapore licence
- Results from the ITP Phase 2 trials, with attention to haematological and hepatic safety
- A teratogenicity and liver-monitoring plan, and a review of the interactions with corticosteroids, since dexamethasone is used in the ITP trial combinations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

