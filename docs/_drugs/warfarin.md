---
layout: default
title: Warfarin
parent: Low Evidence (L5)
nav_order: 1079
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Warfarin: predicted new indication Top-ranked: heparin cofactor 2 deficiency. Best-supported: thrombophi… (evidence level L5). Approved use: Pulmonary embolism, thrombotic disease, intracranial embol…"
monitor_inn: "Warfarin"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "rheumatoid arthritis", "breast fibrocystic disease", "benign mammary dysplasia", "apocrine adenosis of breast", "blunt duct adenosis of breast", "migraine disorder"]
---

# Warfarin
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

# Warfarin: From Thrombotic Disease to Thrombophilia

## One-Sentence Summary

Warfarin is an oral vitamin K antagonist anticoagulant, originally used to treat pulmonary embolism, thrombotic disease and intracranial embolism.
The TxGNN model's top-ranked prediction is **heparin cofactor 2 deficiency**, but that prediction rests on only three case reports. The best-supported predicted indication is **thrombophilia** (rank 4), with **1 Phase 3 clinical trial** and **18 publications**, so this report evaluates thrombophilia as the primary candidate and covers the other predictions briefly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, thrombotic disease, intracranial embolism (from the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Top-ranked: heparin cofactor 2 deficiency. Best-supported: thrombophilia |
| TxGNN Prediction Score | 99.87% (heparin cofactor 2 deficiency); 99.75% (thrombophilia) |
| Evidence Level | L5 or L4 for most predictions; thrombophilia is rated L1 in the underlying data, but this is overstated (see below) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails (thrombophilia only); Hold or Research Question for the others |

> **Note on the evidence level:** The only trial for thrombophilia (NCT00895505) is a Phase 3 trial of unknown status. It tests a D-dimer-guided strategy for extending anticoagulation, not warfarin against placebo in thrombophilia. A conservative reading is therefore closer to L3, since the support is mainly reviews and management articles.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, warfarin inhibits vitamin K epoxide reductase and so reduces synthesis of the vitamin K-dependent clotting factors II, VII, IX and X. Its efficacy in venous thromboembolism is well established.

Thrombophilia is a hypercoagulable state, either inherited (antithrombin, protein C or protein S deficiency, factor V Leiden) or acquired (such as antiphospholipid syndrome). Patients with it have recurrent thrombosis, which is the same problem warfarin already treats. The link is to the thrombotic phenotype and not to correcting the underlying defect. Reviews support its use for long-term secondary prevention, usually after initial heparin.

The same logic applies to the other thrombosis-related predictions (heparin cofactor 2 deficiency, antithrombin deficiency type 2, factor 5 excess), but the supporting evidence is thin:

- **Heparin cofactor 2 deficiency:** three small case or family reports.
- **Antithrombin deficiency type 2:** one case report.
- **Factor 5 excess with spontaneous thrombosis:** no trials or literature. The high score probably reflects network proximity to thrombosis indications and is not independent evidence.

Several other predictions look like artifacts rather than real signals:

- **Rheumatoid arthritis:** all four trials are Phase 1 drug-interaction studies in which warfarin is only a probe substrate.
- **Breast fibrocystic disease, benign mammary dysplasia, apocrine adenosis and blunt duct adenosis:** these show no plausible mechanism. The only literature is a danazol–warfarin interaction report.
- **Migraine:** several case reports describe improvement on warfarin, likely confounded by underlying conditions such as patent foramen ovale or antiphospholipid syndrome. No controlled trial exists, and bleeding risk is a major barrier. This is hypothesis-generating only.

---

## Clinical Trial Evidence

Trials for the best-supported prediction, thrombophilia:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00895505](https://clinicaltrials.gov/study/NCT00895505) | Phase 3 | Unknown | 300 | Tests whether D-dimer testing can tailor the duration of oral anticoagulation after an unprovoked deep vein thrombosis, in a randomised controlled design. It is relevant to anticoagulation, but is not a head-to-head test of warfarin in a defined thrombophilia population. |

Trials for other predictions (none test warfarin as a treatment):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01311622](https://clinicaltrials.gov/study/NCT01311622) | Phase 1 | Completed | 15 | Fostamatinib–warfarin pharmacokinetic and pharmacodynamic interaction in healthy subjects (rheumatoid arthritis) |
| [NCT04246762](https://clinicaltrials.gov/study/NCT04246762) | Phase 1 | Completed | 17 | Effect of olokizumab on CYP probe substrates, including S-warfarin, in rheumatoid arthritis |
| [NCT01636557](https://clinicaltrials.gov/study/NCT01636557) | Phase 1 | Completed | 12 | Effect of sirukumab on CYP enzyme activity, with warfarin as a probe (rheumatoid arthritis) |
| [NCT05392127](https://clinicaltrials.gov/study/NCT05392127) | Phase 1 | Completed | 24 | Effect of SHR0302 on CYP substrates, including S-warfarin, in healthy volunteers (rheumatoid arthritis) |
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3,520 | Pediatric pharmacokinetics of understudied drugs given as standard of care (migraine); not designed to test warfarin for migraine |

---

## Literature Evidence

Thrombophilia (reviews and management articles):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39233011](https://pubmed.ncbi.nlm.nih.gov/39233011/) | 2024 | Review | J Thromb Haemost | ISTH communication on DOACs for secondary VTE prevention in severe thrombophilia; evidence comes only from cohort or single-centre studies |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Diagnosis and treatment of lower extremity VTE; recurrence rates of 20–36% over 10 years |
| [15706484](https://pubmed.ncbi.nlm.nih.gov/15706484/) | 2005 | Review | Semin Thromb Hemost | Management options for thrombophilias; inherited thrombophilia should not alter anticoagulant intensity |
| [12871277](https://pubmed.ncbi.nlm.nih.gov/12871277/) | 2003 | Review | J Thromb Haemost | Management of thrombophilia and uncertainty about how genetic test results should guide care |
| [12787539](https://pubmed.ncbi.nlm.nih.gov/12787539/) | 2003 | Review | Best Pract Res Clin Obstet Gynaecol | Anticoagulation in pregnancy for inherited thrombophilias; treatment-dose LMWH is favoured for high-risk women |
| [10718793](https://pubmed.ncbi.nlm.nih.gov/10718793/) | 2000 | Case report/Review (safety) | Br J Surg | Warfarin-induced skin necrosis, a rare complication (0.01–0.1%) |

Other predictions (case-level evidence only):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Case report | Kyobu Geka | Right ventricular thrombosis due to familial heparin cofactor II deficiency |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Case report | Nihon Kyobu Shikkan Gakkai Zasshi | Congenital antithrombin deficiency with pulmonary infarction, treated with warfarin for 7 years |
| [29582922](https://pubmed.ncbi.nlm.nih.gov/29582922/) | 2017 | Case report | Hamostaseologie | Unprovoked VTE in a young patient with antithrombin type IIB deficiency |
| [22222938](https://pubmed.ncbi.nlm.nih.gov/22222938/) | 2012 | Review/Case series | Neurol Sci | Migraine remission on warfarin; discusses anticoagulants for migraine prophylaxis |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case report | Headache | Migraine with aura resolved on warfarin but not on apixaban |
| [16716139](https://pubmed.ncbi.nlm.nih.gov/16716139/) | 2006 | Case report/Review | Pharmacotherapy | Leflunomide–warfarin interaction (a 22% warfarin dose reduction was needed) |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13517P | Apo-Warfarin 5mg Tablet | Tablet | Not listed in the data |
| SIN13515P | Apo-Warfarin 1mg Tablet | Tablet | Not listed in the data |
| SIN13516P | Apo-Warfarin 2mg Tablet | Tablet | Not listed in the data |
| SIN08146P | Marevan Tablet 1 mg (New Zealand) | Tablet | Not listed in the data |
| SIN08147P | Marevan Tablet 5 mg (New Zealand) | Tablet | Not listed in the data |

Six single-ingredient oral tablet licences are valid in total; the Marevan 3 mg tablet (SIN08019P) is the one not shown above.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from drug-disease relationships, not from label text): hypertension, liver failure and liver disease, congestive heart failure, hypothyroidism, nephrotic syndrome, impaired renal function, blood coagulation disease, psychotic and mental disorders, anaemia, cholestasis, hyperlipidaemia, chronic diarrhoeal disease, bone and connective tissue disease, and substance abuse/dependence. They should be checked against the actual package insert.
- **Drug Interactions:** 100 interactions were recorded. The most significant are the **Major** interactions with **acetylsalicylic acid (aspirin)** and **metronidazole**. Many **Moderate** interactions are also listed, including ranitidine, rabeprazole, doxycycline, amoxicillin, metformin, bupropion, aprepitant, mesalazine, chenodeoxycholic acid and several corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide).
- **Skin necrosis:** warfarin-induced skin necrosis has been reported, particularly in protein C deficiency, which is relevant in thrombophilia.
- **Pregnancy:** warfarin is generally avoided because of teratogenicity; LMWH is preferred.
- **Bleeding risk** is a major barrier to any prophylactic or off-label use.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (thrombophilia only). **Hold** for rheumatoid arthritis, factor 5 excess and the breast-related predictions. **Research Question** for heparin cofactor 2 deficiency, antithrombin deficiency type 2 and migraine.

**Rationale:**
- Thrombophilia is the only prediction where the mechanism, an established anticoagulant role in VTE secondary prevention, and a Phase 3 trial all point the same way. However, the trial is indirect and its status is unknown, so the evidence is partial.
- Rheumatoid arthritis and the breast-related predictions look like false positives driven by drug-interaction literature or graph propagation. Migraine and the rare deficiencies rest only on case reports.

**To proceed, the following is needed:**
- The package insert warnings and contraindications from the HSA website; this is a blocking gap for safety screening.
- Detailed mechanism of action data from DrugBank.
- Direct comparative evidence for warfarin versus DOACs or LMWH in defined thrombophilia subgroups (for example antithrombin, protein C or protein S deficiency, and antiphospholipid syndrome).
- A bleeding and INR monitoring plan, with special attention to pregnancy, protein C deficiency (skin necrosis) and the major interactions with aspirin and metronidazole.
- Confirmation of the approved indication text on the Singapore licences.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

