---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Clofarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Clofarabine: From Relapsed/Refractory Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Clofarabine is a second-generation purine nucleoside analog, granted accelerated FDA approval in 2004 for pediatric patients (ages 1–21) with relapsed or refractory acute lymphoblastic leukemia (ALL) after at least two prior treatment regimens.
The TxGNN model predicts it may be effective for **Myeloid Leukemia** (including acute myeloid leukemia, AML), with a prediction score of **99.88%**.
The current evidence base includes **multiple completed Phase 2/3 clinical trials** — anchored by a landmark Phase 3 RCT — and **20 publications** directly supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed/refractory acute lymphoblastic leukemia (pediatric; FDA-approved 2004) |
| Predicted New Indication | Myeloid Leukemia (AML and related myeloid malignancies) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Clofarabine was designed to combine the best pharmacological properties of fludarabine and cladribine while overcoming their respective limitations — chiefly susceptibility to deamination and phosphorolysis. After cellular uptake, it is phosphorylated by deoxycytidine kinase (dCK) to its active triphosphate form, which then operates through two simultaneous cytotoxic mechanisms: competitively inhibiting DNA polymerase α to block DNA replication, and depleting the intracellular dATP pool by inhibiting ribonucleotide reductase. In parallel, the drug directly disrupts mitochondrial membrane integrity to trigger caspase-dependent apoptosis. This multi-pronged mechanism makes clofarabine considerably more potent than its predecessors against treatment-resistant leukemic blasts.

The biological link between pediatric ALL and myeloid leukemia is direct and mechanistically coherent. Both diseases arise from immature hematopoietic precursors characterized by rapid proliferation and deficient DNA repair — the precise cellular context that maximizes vulnerability to clofarabine's mechanism. Critically, myeloid leukemia cells (especially AML blasts) highly express dCK, the rate-limiting activating enzyme, making them at least as sensitive to clofarabine as lymphoblasts. This shared molecular biology explains why the same drug class has been actively explored across both lineages.

The clinical translation of this rationale is well-documented. The AML08 Phase 3 randomized controlled trial (NCT00703820, n=324) demonstrated that clofarabine can replace anthracyclines and etoposide in pediatric AML induction therapy without inferior outcomes — a landmark finding published in the *Journal of Clinical Oncology* (PMID 31246522). A large Phase 2/3 programme (NCT00454480, n=2,000) further established the evidence base in older adult AML patients. Together with multiple completed Phase 2 trials across adult salvage, transplant conditioning, and frontline settings, the mechanistic prediction from TxGNN aligns squarely with extensive clinical validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00098033](https://clinicaltrials.gov/study/NCT00098033) | Phase 2 | Completed | 64 | Pivotal pharmacodynamic and efficacy study of clofarabine in AML, ALL, and CML blast/accelerated phases; evaluated antileukemic activity across acute leukemia subtypes and established foundational pharmacodynamic data. |
| [NCT00703820](https://clinicaltrials.gov/study/NCT00703820) | Phase 3 | Completed | 324 | AML08 Phase 3 RCT: compared clofarabine + cytarabine versus conventional daunorubicin/etoposide induction in newly diagnosed paediatric AML; demonstrated non-inferiority of the clofarabine arm with potential to reduce cardiotoxicity exposure. |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Completed | 2,000 | Large treatment development programme for older AML and high-risk MDS patients (NCRI AML16 framework); evaluated multiple novel agents including clofarabine-based regimens vs. established chemotherapy backbones. |
| [NCT01794702](https://clinicaltrials.gov/study/NCT01794702) | Phase 1/2 | Completed | 65 | Evaluated decitabine priming followed by clofarabine + idarubicin + cytarabine (CIA) in acute leukemia; defined optimal dosing of the combination and provided efficacy and safety data in AML. |
| [NCT05917405](https://clinicaltrials.gov/study/NCT05917405) | Phase 2/3 | Recruiting | 302 | FLUCLORIC: ongoing randomised multicentre trial comparing clofarabine/busulfan vs. fludarabine/busulfan as reduced-intensity conditioning prior to allogeneic transplant in AML; designed to confirm retrospective advantages of clofarabine-based conditioning. |
| [NCT01025154](https://clinicaltrials.gov/study/NCT01025154) | Phase 2 | Completed | 63 | Clofarabine + cytarabine + idarubicin (CIA) as induction therapy in younger AML patients (18–60 years); demonstrated meaningful complete remission rates and manageable toxicity profile. |
| [NCT00924443](https://clinicaltrials.gov/study/NCT00924443) | Phase 2 | Completed | 69 | Clofarabine monotherapy in older untreated AML patients unsuitable for intensive chemotherapy; established clinically relevant single-agent activity and informed subsequent combination development. |
| [NCT00067028](https://clinicaltrials.gov/study/NCT00067028) | Phase 2 | Completed | 116 | Prospective randomized comparison of three clofarabine-based combinations (with idarubicin and/or Ara-C) in first relapse or primary refractory AML and high-grade MDS; key data informing optimal salvage backbone selection. |
| [NCT00602225](https://clinicaltrials.gov/study/NCT00602225) | Phase 1/2 | Completed | 50 | Dose-escalation study of clofarabine + cytarabine + G-CSF priming in relapsed/refractory AML; defined MTD and demonstrated synergistic cytotoxic activity with acceptable tolerability. |
| [NCT01193400](https://clinicaltrials.gov/study/NCT01193400) | Phase 2 | Terminated | 75 | Multicenter trial of clofarabine + low-dose cytarabine induction and consolidation in AML patients ≥60 years; terminated early but contributed remission rate and toxicity data relevant to elderly patients. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | Phase 3 RCT | J Clin Oncol | AML08 trial: clofarabine successfully replaced anthracyclines and etoposide in paediatric AML induction without sacrificing remission rates; primary Phase 3 evidence supporting this repurposing direction. |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Phase 2 Study | Cancer Medicine | CLAM regimen (clofarabine 30 mg/m²/d + cytarabine 750 mg/m²/d + mitoxantrone) in r/r AML aged 18–65: high composite response rate with effective bridge to allogeneic HSCT. |
| [29773602](https://pubmed.ncbi.nlm.nih.gov/29773602/) | 2018 | Phase IB | Haematologica | Clofarabine replacing fludarabine alongside high-dose cytarabine and liposomal daunorubicin in paediatric r/r AML (ITCC 020/I-BFM 2009-02); established recommended Phase 2 dose and confirmed activity in heavily pre-treated children. |
| [31905904](https://pubmed.ncbi.nlm.nih.gov/31905904/) | 2019 | Retrospective Cohort | Cancers | Clofarabine-based consolidation (CLARA regimen) significantly improved relapse-free survival over standard high-dose cytarabine in younger AML patients with micro-complex karyotype — clinically actionable subgroup finding. |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | Retrospective Cohort | Transplant Cell Ther | Clofarabine + busulfan myeloablative conditioning (Clo/Bu4) in active myeloid malignancies undergoing allogeneic HCT: demonstrated antileukemic activity with acceptable non-relapse mortality in patients ≤70 years. |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Review | Leukemia & Lymphoma | Comprehensive review of clofarabine's role in AML: covers single-agent activity, CIA/CLAM combination development, transplant conditioning use, and clinical positioning in first-line vs. salvage settings. |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Review | Crit Rev Oncol Hematol | In-depth review of clofarabine across adult AML: summarises Phase 1–3 data, combination strategies, and identifies optimal patient populations for further study. |
| [18756533](https://pubmed.ncbi.nlm.nih.gov/18756533/) | 2008 | Clinical Study | Cancer | Early Phase 2 data establishing clofarabine + idarubicin (CI) and clofarabine + cytarabine + idarubicin (CIA) as effective salvage combinations in relapsed AML; foundational data for combination backbone development. |
| [21182488](https://pubmed.ncbi.nlm.nih.gov/21182488/) | 2011 | Review | Curr Med Chem | Comprehensive survey of novel agents for AML including clofarabine; discusses mechanism of action in the context of AML biology and reviews early clinical efficacy and safety data. |
| [19852733](https://pubmed.ncbi.nlm.nih.gov/19852733/) | 2009 | Review | Future Oncol | Forward-looking analysis of clofarabine's positioning in adult AML; argues for its integration into both induction and consolidation regimens based on activity data available at the time. |

---

## Singapore Market Information

Clofarabine currently has **no registered products with the Health Sciences Authority (HSA) of Singapore**. The drug is commercially available as Clolar® (USA) and Evoltra® (Europe/Japan) via country-specific regulatory approvals, but has not been submitted for or granted HSA registration.

Any clinical use in Singapore would require either a Named Patient Supply arrangement or Compassionate Use Authorisation under the HSA Special Access Route (SAR) framework.

---

## Cytotoxicity

Clofarabine is a conventional cytotoxic antineoplastic agent belonging to the purine nucleoside analog class; this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Purine nucleoside analog (antimetabolite); second-generation deoxyadenosine analog |
| Myelosuppression Risk | **High** — neutropenia, thrombocytopenia, and anaemia are the primary and dose-limiting toxicities; febrile neutropenia and prolonged aplasia are expected at therapeutic doses |
| Emetogenicity Classification | Low to moderate (consistent with purine nucleoside analog class; less emetogenic than platinum agents or high-dose alkylators) |
| Monitoring Items | CBC with differential and platelet count (before each cycle and at least twice weekly during treatment); liver function tests (ALT, AST, bilirubin — clofarabine has known hepatotoxicity potential); renal function (serum creatinine, BUN); signs/symptoms of systemic inflammatory response syndrome (SIRS) and capillary leak |
| Handling Protection | Must comply with institutional cytotoxic drug handling regulations; appropriate PPE required during preparation, administration, and disposal; waste to be managed per cytotoxic chemotherapy guidelines |

---

## Safety Considerations

Please refer to the package insert for safety information.

> No safety data (key warnings, contraindications, or drug-drug interactions) was retrievable from the current Singapore data sources, as the drug is unregistered locally. Clinicians should consult the full Clolar® FDA prescribing information or Evoltra® EMA Summary of Product Characteristics prior to use. Known class-level and drug-specific safety concerns include: significant myelosuppression with risk of fatal infections, hepatotoxicity (including sinusoidal obstruction syndrome in transplant settings), systemic inflammatory response syndrome (SIRS), capillary leak syndrome, and tumour lysis syndrome.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clofarabine carries robust Level 1 evidence in myeloid leukemia, underpinned by at least one completed Phase 3 RCT (AML08, n=324) and a large Phase 2/3 programme (n=2,000), alongside multiple Phase 2 trials spanning paediatric and adult AML, induction, salvage, and transplant conditioning contexts. The mechanistic basis — high dCK expression in myeloid blasts enabling efficient drug activation — is well-validated, and the prediction aligns with an already extensively studied clinical use case. The primary barrier to implementation in Singapore is regulatory (no HSA registration), not evidential.

**To proceed, the following is needed:**

- **Regulatory access pathway:** Initiate HSA Special Access Route (Named Patient Supply or Compassionate Use) application, or commence formal product registration with HSA, as the drug is currently unavailable through standard Singapore channels
- **Full safety documentation:** Obtain the complete Clolar® prescribing information (FDA label) or Evoltra® SmPC and conduct a formal pharmacist-led safety review covering warnings, contraindications, hepatotoxicity monitoring, and SIRS/capillary leak management protocols
- **Drug interaction assessment:** Conduct a prospective DDI review with institutional pharmacist, given the current data gap; particular attention to concurrent nephrotoxic or hepatotoxic agents
- **Institutional capability assessment:** Confirm that administration is conducted within a tertiary haematology centre equipped for intensive chemotherapy, haematological emergency management, and allogeneic transplant support
- **Subgroup clarification:** Define target population clearly — paediatric AML evidence (Phase 3) is strongest; adult AML evidence, while substantial, is predominantly Phase 2; this distinction should inform protocol design and consent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

