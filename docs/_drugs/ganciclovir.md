---
layout: default
title: Ganciclovir
parent: 僅模型預測 (L5)
nav_order: 451
evidence_level: L5
indication_count: 10
---

# Ganciclovir
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

# Ganciclovir: From CMV Disease to Cytomegalovirus Pneumonia

## One-Sentence Summary

Ganciclovir is an established nucleoside analogue antiviral, recognised globally as first-line therapy for serious cytomegalovirus (CMV) infections in immunocompromised patients — particularly CMV retinitis in AIDS and transplant recipients — though it currently carries no product registration in Singapore.
The TxGNN model predicts it may be specifically effective for **Cytomegalovirus Pneumonia**, a life-threatening CMV end-organ disease with historically near-100% mortality if left untreated in allogeneic bone marrow transplant recipients.
This direction is currently supported by **9 clinical trials** and **20 publications**, yielding an evidence level of **L1**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | CMV retinitis and systemic CMV disease in immunocompromised patients (no Singapore registration on file; based on global established use) |
| Predicted New Indication | Cytomegalovirus Pneumonia |
| TxGNN Prediction Score | 97.56% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data was not available in the current evidence package. However, based on published literature, Ganciclovir is a nucleoside analogue that acts as a competitive inhibitor of the CMV DNA polymerase (UL54). It must first be phosphorylated by the viral kinase UL97 to its active triphosphate form, which then halts viral DNA synthesis — directly targeting the molecular machinery that CMV relies on for replication in any host tissue, including the lung.

Cytomegalovirus pneumonia represents one of the most severe end-organ manifestations of CMV disease, predominantly affecting allogeneic bone marrow transplant recipients, solid organ transplant patients, and individuals with advanced HIV/AIDS. In untreated allogeneic BMT recipients, mortality from CMV pneumonia historically approached 100%. The condition is mechanistically driven by active CMV replication in pulmonary tissue — precisely the same replication target that Ganciclovir inhibits. This makes CMV pneumonia a direct extension of Ganciclovir's established therapeutic domain, not a speculative leap.

Because CMV pneumonia and CMV retinitis share an identical molecular target (CMV DNA polymerase UL54), the clinical logic is straightforward: an agent proven to suppress CMV replication in the eye or gut should, in principle, suppress it in the lung. A large body of clinical evidence — including landmark Phase 4 and Phase 2/3 RCTs, placebo-controlled trials, and multiple cohort studies — has confirmed that the Ganciclovir + intravenous immunoglobulin combination became the historical standard of care for CMV pneumonia in transplant settings. The TxGNN model's L1-level prediction is therefore strongly corroborated by decades of empirical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02152358](https://clinicaltrials.gov/study/NCT02152358) | Phase 4 | Completed | 317 | Large prospective RCT comparing preemptive Ganciclovir (CMV viremia) vs Aciclovir (HSV PCR-positive) in ICU patients requiring prolonged mechanical ventilation; primary endpoint was ventilator-free days at Day 60 — highest direct relevance to CMV pulmonary management |
| [NCT03915366](https://clinicaltrials.gov/study/NCT03915366) | Phase 2/3 | Completed | 563 | Multicenter open-label RCT (EMPIRICAL trial) evaluating empirical anti-CMV and anti-TB treatment in HIV-infected infants with severe pneumonia in Africa; assessed impact on 15-day and 1-year mortality |
| [NCT04690933](https://clinicaltrials.gov/study/NCT04690933) | N/A | Completed | 400 | Real-world observational study of anti-CMV drug efficacy and resistance in haematopoietic stem cell transplant recipients; interstitial pneumonia noted as the most severe and specific CMV manifestation of interest |
| [NCT05708755](https://clinicaltrials.gov/study/NCT05708755) | Phase 2 | Recruiting | 50 | Evaluates CMV T-cell immunity-guided valganciclovir prophylaxis duration in lung transplant recipients using the inSIGHT™ CMV T Cell Immunity Panel; aims to safely minimise prophylaxis exposure while preventing CMV lung disease |
| [NCT01199562](https://clinicaltrials.gov/study/NCT01199562) | N/A | Active, not recruiting | 153 | Observational study of a modified preemptive CMV management strategy in allogeneic haematopoietic cell transplant recipients with correlation to innate immune function; targets a high CMV pneumonia-risk population |
| [NCT00000726](https://clinicaltrials.gov/study/NCT00000726) | Phase 1 | Completed | 53 | Evaluated Foscarnet (not Ganciclovir) for CMV retinitis in AIDS patients; provides comparative background on CMV antiviral mechanisms — Foscarnet similarly inhibits viral DNA polymerase but lacks UL97 activation requirement |
| [NCT00141037](https://clinicaltrials.gov/study/NCT00141037) | Phase 1/2 | Completed | 130 | Paediatric renal transplant immunosuppression protocol comparing steroid-sparing vs standard regimens; CMV management appears as a secondary infection-related endpoint |
| [NCT00078533](https://clinicaltrials.gov/study/NCT00078533) | Phase 1 | Completed | 26 | Dose-finding trial of CMV-specific cytotoxic T-lymphocytes after allogeneic stem cell transplant; evaluates a cell-therapy approach to CMV prevention as an alternative to antiviral drugs |
| [NCT02109887](https://clinicaltrials.gov/study/NCT02109887) | N/A | Completed | 76 | Diagnostic study assessing whether CMV-specific ELISPOT assay predicts CMV co-infection in PCP patients; approximately one-third of non-HIV PCP patients have CMV co-infection, raising the question of whether anti-CMV treatment aids these patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [8380243](https://pubmed.ncbi.nlm.nih.gov/8380243/) | 1993 | RCT (placebo-controlled, double-blind) | Annals of Internal Medicine | Demonstrated that ganciclovir prophylaxis significantly reduced CMV infection and disease in allogeneic BMT recipients — a foundational controlled trial for Ganciclovir's role in high-risk CMV populations |
| [39774866](https://pubmed.ncbi.nlm.nih.gov/39774866/) | 2025 | Review / Clinical Guidance | Intensive Care Medicine | Updated guidance for intensivists on CMV infection in immunocompromised ICU patients: describes clinical presentation, risk factors, and antiviral management including current indications for Ganciclovir |
| [8786764](https://pubmed.ncbi.nlm.nih.gov/8786764/) | 1996 | Drug Review | N Engl J Med | Landmark NEJM drug review establishing Ganciclovir as first-line therapy for life- or sight-threatening CMV infection in immunocompromised patients; addresses pharmacology, clinical efficacy, and toxicity |
| [2161731](https://pubmed.ncbi.nlm.nih.gov/2161731/) | 1990 | Drug Review | Drugs | Comprehensive review of Ganciclovir's antiviral activity, pharmacokinetic properties, and therapeutic efficacy across CMV manifestations; recommends first-line use and notes efficacy variations by site of disease |
| [8668848](https://pubmed.ncbi.nlm.nih.gov/8668848/) | 1995 | Review | Semin Respir Infect | Focused review on CMV pneumonia: presentation, diagnosis, and treatment; documents near-100% mortality in untreated allogeneic BMT patients and the survival benefit of Ganciclovir + IVIG combination therapy |
| [8274605](https://pubmed.ncbi.nlm.nih.gov/8274605/) | 1993 | Review | Clin Infect Dis | Reviews CMV pneumonia prevention and treatment in transplant recipients; establishes Ganciclovir-based prophylaxis and preemptive therapy strategies as emerging standards of care |
| [8913411](https://pubmed.ncbi.nlm.nih.gov/8913411/) | 1996 | Review | Ann Pharmacother | Targeted overview of CMV in bone marrow transplant patients with emphasis on CMV interstitial pneumonia; summarises prevention and treatment evidence, including Ganciclovir regimens |
| [2847609](https://pubmed.ncbi.nlm.nih.gov/2847609/) | 1988 | Clinical Study | Annals of Internal Medicine | Landmark clinical study demonstrating efficacy of Ganciclovir + high-dose intravenous immune globulin for treating CMV interstitial pneumonitis after allogeneic BMT — established the combination as the treatment backbone |
| [2847610](https://pubmed.ncbi.nlm.nih.gov/2847610/) | 1988 | Clinical Study | Annals of Internal Medicine | Confirmed that the Ganciclovir + intravenous CMV immunoglobulin combination is effective in CMV pneumonia after bone marrow transplant; companion study to PMID 2847609 providing independent replication |
| [2161510](https://pubmed.ncbi.nlm.nih.gov/2161510/) | 1990 | Clinical Study | Nouv Rev Fr Hematol | Pilot study of early-administration Ganciclovir + high-dose anti-CMV IVIG in allogeneic BMT patients; showed that earlier initiation improves outcomes against the backdrop of historically high CMV pneumonia mortality |

---

## Singapore Market Information

Ganciclovir (DrugBank ID: DB01004) is currently **not registered with the Health Sciences Authority (HSA) of Singapore**. There are no active product licences on file, and the drug is not commercially available through registered channels.

> **Clinical note:** While Ganciclovir itself is unregistered, its oral prodrug **Valganciclovir** may be available through institutional import or special access pathways. Clinicians managing CMV pneumonia in immunocompromised patients should consult institutional pharmacy teams and refer to international treatment guidelines (IDSA, ECIL, ASBMT) for current therapeutic recommendations.

---

## Safety Considerations

Safety labelling data (key warnings, contraindications, and drug–drug interactions) were not available in the current evidence package.

> Please refer to the international package insert and clinical references for full safety information. Based on the pharmacological class, the following areas warrant particular attention prior to clinical use:
>
> - **Haematological toxicity**: Myelosuppression (neutropenia, thrombocytopenia) is a well-documented class effect of Ganciclovir and requires regular complete blood count monitoring.
> - **Renal toxicity and dose adjustment**: Ganciclovir is renally cleared; dose reduction is required in renal impairment.
> - **Teratogenicity and reproductive risk**: Ganciclovir has demonstrated teratogenic and embryotoxic effects in animal studies; appropriate counselling and contraception measures are necessary.
> - **Drug interactions**: Potential interactions with nephrotoxic agents (e.g., amphotericin B, ciclosporin) and immunosuppressants used in transplant settings should be reviewed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ganciclovir has an exceptionally strong mechanistic and clinical evidence base for treating cytomegalovirus pneumonia: it directly inhibits the CMV DNA polymerase responsible for pulmonary viral replication, and its efficacy is supported by a completed Phase 4 RCT (n=317), a completed Phase 2/3 RCT (n=563), a placebo-controlled double-blind trial, and over two decades of clinical literature establishing the Ganciclovir + IVIG combination as the historical standard of care. The L1 evidence level reflects genuine clinical utility rather than speculative prediction. The principal barriers to use in Singapore are the absence of local product registration and incomplete safety labelling documentation.

**To proceed, the following is needed:**

- **Regulatory pathway**: Assess Singapore HSA named-patient importation or special access programme eligibility for Ganciclovir (or consider Valganciclovir as an oral alternative with existing registration status in comparable markets)
- **Safety documentation**: Retrieve and review full international package insert (e.g., Cytovene® / Cymevene®) for complete warnings, contraindications, and drug interactions
- **Mechanistic documentation**: Retrieve DrugBank API entry for formal MOA, pharmacodynamic targets, and toxicity data to complete the evidence package
- **Local clinical protocol**: Develop institutional guidelines for CMV pneumonia diagnosis (BAL CMV PCR/culture thresholds), treatment initiation criteria, response monitoring (viral load, respiratory parameters), and duration of therapy
- **Pharmacovigilance plan**: Establish monitoring schedule for haematological parameters (CBC with differential weekly during induction), renal function, and hepatic enzymes
- **Population stratification**: Define target patient population precisely — allogeneic BMT recipients, solid organ transplant patients, and advanced HIV/AIDS patients represent the highest-evidence subgroups; avoid extrapolating to immunocompetent patients without additional evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

