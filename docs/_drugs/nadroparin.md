---
layout: default
title: Nadroparin
parent: Low Evidence (L5)
nav_order: 694
evidence_level: L5
indication_count: 10
---

# Nadroparin
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

# Nadroparin: From Thromboembolic Disorders to Pulmonary Embolism

## One-Sentence Summary

Nadroparin is a low-molecular-weight heparin (LMWH) anticoagulant marketed in Singapore as Fraxiparine. The TxGNN model's top-ranked prediction is **primary release disorder of platelets**, but this is a bleeding disorder and the prediction is not credible. The best-supported prediction in the list is **pulmonary embolism**, with **11 clinical trials** and **20 publications**. The mechanism-based, partly evidenced alternative is **thrombophilia**, with **2 clinical trials** and **20 publications**.

> **Note on selecting the lead indication:** The highest-scoring prediction (rank 1, score 98.15%) has no clinical or literature evidence and a biologically opposed mechanism. This report therefore presents the top prediction in the overview and also highlights the best-supported candidates (pulmonary embolism and thrombophilia) so the decision is not misleading.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the registration data) |
| Predicted New Indication | Primary release disorder of platelets (rank 1). Best-supported: pulmonary embolism (rank 8) and thrombophilia (rank 4) |
| TxGNN Prediction Score | 98.15% (rank 1); 96.98% (pulmonary embolism); 97.28% (thrombophilia) |
| Evidence Level | L5 (rank 1); L1 (pulmonary embolism); L1 (thrombophilia) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold (rank 1); Proceed with Guardrails (pulmonary embolism, thrombophilia) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, nadroparin is a low-molecular-weight heparin that potentiates antithrombin, thereby inhibiting factor Xa and, to a lesser degree, thrombin. This is an anticoagulant action.

**Rank 1 (primary release disorder of platelets) is not plausible.** A platelet release defect is a bleeding disorder, so an anticoagulant is mechanistically opposed and may worsen bleeding. The same concern applies to the other bleeding-disorder predictions, Glanzmann thrombasthenia (rank 2) and pseudo-von Willebrand disease (rank 3). The high scores likely reflect network proximity in the knowledge graph (coagulation and platelet terms) rather than therapeutic benefit. Amenorrhea (rank 9) also has no plausible mechanistic link.

**Pulmonary embolism (rank 8) and thrombophilia (rank 4) are mechanistically sound.** Inhibiting Xa and thrombin generation is the established basis for preventing and treating venous thromboembolism. In thrombophilia, it directly addresses the hypercoagulable state, especially in pregnancy. Note that VTE treatment is likely already a labelled use in many regions, so pulmonary embolism is not truly novel repurposing.

Other predictions are plausible but unvalidated: factor 5 excess with spontaneous thrombosis (rank 6), heparin cofactor 2 deficiency (rank 7; heparin acts mainly through antithrombin, which remains intact), and antithrombin deficiency type 2 (rank 5; efficacy depends on whether the variant affects the heparin-binding site). Hemoglobinopathy (rank 10) has only an indirect thrombosis-prevention rationale.

---

## Clinical Trial Evidence

The rank 1 prediction has no registered trials. The tables below cover the two best-supported predictions.

### Pulmonary embolism (rank 8)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00796692](https://clinicaltrials.gov/study/NCT00796692) | Phase 4 | Completed | 274 | Weight-adjusted nadroparin vs unfractionated heparin for initial treatment of pulmonary thromboembolism in China |
| [NCT01828697](https://clinicaltrials.gov/study/NCT01828697) | Phase 4 | Completed | 1110 | Two LMWH doses to prevent recurrent VTE in pregnancy |
| [NCT01164046](https://clinicaltrials.gov/study/NCT01164046) | Phase 3 | Terminated | 56 | Long-term treatment of cancer patients with DVT or PE; terminated early |
| [NCT00312013](https://clinicaltrials.gov/study/NCT00312013) | Phase 3 | Completed | 503 | Nadroparin effect on survival and progression in advanced lung, pancreatic or prostate cancer (oncologic endpoint) |
| [NCT00881088](https://clinicaltrials.gov/study/NCT00881088) | Phase 2/3 | Unknown | 669 | Nadroparin vs fondaparinux for VTE prophylaxis in lower-limb fracture with cast |
| [NCT04373707](https://clinicaltrials.gov/study/NCT04373707) | Phase 4 | Completed | 1000 | Weight-adjusted vs fixed prophylactic LMWH dosing in COVID-19 |
| [NCT01531829](https://clinicaltrials.gov/study/NCT01531829) | Phase 4 | Unknown | 460 | Low-dose rt-PA plus LMWH vs LMWH alone in normotensive PE with RV dysfunction |
| [NCT01727427](https://clinicaltrials.gov/study/NCT01727427) | N/A | Completed | 695 | Prospective study of treating unsuspected PE in cancer patients |
| [NCT01267305](https://clinicaltrials.gov/study/NCT01267305) | N/A | Completed | 362 | LMWH doses vs fondaparinux for thromboprophylaxis after thoracic surgery |
| [NCT05621915](https://clinicaltrials.gov/study/NCT05621915) | N/A | Completed | 43 | Nadroparin pharmacokinetics across COVID-19 stages (no efficacy endpoint) |

### Thrombophilia (rank 4)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01019655](https://clinicaltrials.gov/study/NCT01019655) | Phase 3 | Unknown | 300 | LMWH in pregnant women with thrombophilia; results unconfirmed |
| [NCT06494878](https://clinicaltrials.gov/study/NCT06494878) | Phase 3 | Recruiting | 8805 | PARTUM: postpartum aspirin vs LMWH for VTE prevention (aspirin is the test drug, so only indirectly relevant) |

---

## Literature Evidence

### Pulmonary embolism (rank 8)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27836513](https://pubmed.ncbi.nlm.nih.gov/27836513/) | 2016 | RCT | Lancet Haematol | CACTUS: placebo-controlled trial of anticoagulation for symptomatic calf DVT |
| [9108990](https://pubmed.ncbi.nlm.nih.gov/9108990/) | 1997 | Review | Drugs & Aging | Nadroparin pharmacology and use in preventing and treating thromboembolic disorders |
| [31030749](https://pubmed.ncbi.nlm.nih.gov/31030749/) | 2019 | Review | Prog Mol Biol Transl Sci | Overview of LMWHs and their clinical applications |
| [16358378](https://pubmed.ncbi.nlm.nih.gov/16358378/) | 2005 | Clinical comparison | J Zhejiang Univ Sci B | LMWH vs unfractionated heparin for acute non-massive PTE: efficacy, adverse effects, cost |
| [32639644](https://pubmed.ncbi.nlm.nih.gov/32639644/) | 2020 | Cohort | J Clin Pharmacol | Liver function effects of LMWH vs fondaparinux in 463 PE patients; liver dysfunction in 17.1% |
| [20015933](https://pubmed.ncbi.nlm.nih.gov/20015933/) | 2011 | Clinical study | J Oncol Pharm Pract | Low-dose nadroparin in PE with brain metastases |

### Thrombophilia (rank 4)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38233773](https://pubmed.ncbi.nlm.nih.gov/38233773/) | 2024 | Meta-analysis | BMC Pregnancy Childbirth | LMWH for preventing preeclampsia in high-risk pregnancies without thrombophilia |
| [20229677](https://pubmed.ncbi.nlm.nih.gov/20229677/) | 2010 | RCT | Srp Arh Celok Lek | Nadroparin vs unfractionated heparin for VTE in pregnancy and puerperium |
| [24995856](https://pubmed.ncbi.nlm.nih.gov/24995856/) | 2014 | Review | Cochrane Database Syst Rev | Aspirin and/or heparin for unexplained recurrent miscarriage, with or without inherited thrombophilia |
| [23262970](https://pubmed.ncbi.nlm.nih.gov/23262970/) | 2014 | Prospective study | Clin Appl Thromb Hemost | Prophylactic nadroparin in 85 pregnant women with thrombophilia and recurrent fetal loss |
| [16601339](https://pubmed.ncbi.nlm.nih.gov/16601339/) | 2006 | Review | Fetal Diagn Ther | Pregnancy outcome in inherited thrombophilia treated with LMWH |
| [30660948](https://pubmed.ncbi.nlm.nih.gov/30660948/) | 2019 | Review | Thromb Res | Anti-Xa monitoring of heparins in antithrombin-deficient patients |

### Antithrombin deficiency type 2 (rank 5)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37703851](https://pubmed.ncbi.nlm.nih.gov/37703851/) | 2023 | Case report | Med Princ Pract | Reduced thrombin generation after heparin in a homozygous type II heparin-binding-site deficient pregnant woman |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15473P | Fraxiparine Injection 7600 IU AXA/0.8 mL | Injection | Not available |
| SIN15472P | Fraxiparine Injection 1900 IU AXA/0.2 mL | Injection | Not available |
| SIN14223P | Fraxiparine Injection 3800 IU AXA/0.4 mL | Injection | Not available |
| SIN14222P | Fraxiparine Injection 5700 IU AXA/0.6 mL | Injection | Not available |
| SIN15474P | Fraxiparine Injection 9500 IU AXA/1.0 mL | Injection | Not available |

Three further single-ingredient licences are also valid (8 in total): SIN11872P (Fraxiparine Multidose), SIN11292P (Fraxiparine Forte) and SIN02147P (Fraxiparine 2850 IU AXA/0.3 mL). All are injections from Aspen Notre Dame de Bondeville.

---

## Safety Considerations

Package insert warnings and contraindications were not available for this report, so please refer to the package insert for safety information.

Points drawn from the evidence reviewed:
- **Bleeding risk**: Nadroparin is an anticoagulant and may worsen bleeding, which is the main reason the platelet and von Willebrand disease predictions should not proceed.
- **Heparin-induced thrombocytopenia**: Reported with nadroparin, including a case complicated by pulmonary embolism and disseminated intravascular coagulation (PMID 12544086).
- **Liver function**: Liver dysfunction was seen in 17.1% of PE patients treated with LMWH or fondaparinux (PMID 32639644).
- **Antithrombin deficiency**: Anti-Xa monitoring and individualized dosing may be needed.
- **Dosing adjustments**: Renal impairment, body weight and pregnancy.

---

## Conclusion and Next Steps

**Decision: Hold for the rank 1 prediction (primary release disorder of platelets); Proceed with Guardrails for pulmonary embolism and thrombophilia.**

**Rationale:**
- The rank 1 prediction has no clinical or literature support, and its mechanism is biologically opposed to nadroparin's, so the high score reflects knowledge-graph proximity only.
- Pulmonary embolism and thrombophilia are supported by Phase 3/4 trials and reviews (L1), but pulmonary embolism is likely already an established use, so it is not truly novel repurposing. Evidence for pregnancy-outcome benefit in thrombophilia is mixed, and the key thrombophilia trial status is unknown.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the approved indications for the Singapore licences, to establish what is new versus already labelled
- For thrombophilia: confirmation of the thrombophilia type, with anti-Xa monitoring for antithrombin deficiency, and a bleeding-risk assessment
- Updated status of NCT01019655 and the results of the ongoing PARTUM trial
- Route compatibility check (currently pending); only injectable forms are registered in Singapore
- Specific hypotheses, if any, before further work on the antithrombin type 2, factor 5 excess, heparin cofactor 2 deficiency and hemoglobinopathy predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

