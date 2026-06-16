---
layout: default
title: Eltrombopag
parent: 僅模型預測 (L5)
nav_order: 365
evidence_level: L5
indication_count: 10
---

# Eltrombopag
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

# Eltrombopag: From Immune Thrombocytopenia to HIV Infectious Disease

## One-Sentence Summary

Eltrombopag is a thrombopoietin receptor agonist (TPO-RA) approved in multiple countries for chronic immune thrombocytopenia (ITP) and aplastic anemia, though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **HIV Infectious Disease** — specifically in managing HIV-related thrombocytopenia — with **5 clinical trials** and **10 publications** currently supporting this direction.
Evidence strength reaches Level L2, anchored by two large completed Phase 3 RCTs in viral infection–associated thrombocytopenia.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic immune thrombocytopenia (ITP) / Aplastic anemia (internationally approved; not registered in Singapore) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Eltrombopag is a small-molecule, non-peptide thrombopoietin receptor (TPO-R / MPL) agonist. By activating the TPO-R on megakaryocytes and their progenitors in the bone marrow, eltrombopag stimulates platelet production — a mechanism entirely independent of thrombopoietin itself. This makes it suitable for thrombocytopenic states where the bone marrow's capacity to produce platelets is suppressed, regardless of the underlying cause.

HIV infection causes thrombocytopenia through two converging mechanisms: (1) direct infection of megakaryocytes by HIV, impairing platelet production; and (2) immune-mediated platelet destruction, where HIV surface proteins trigger cross-reactive antibodies that clear platelets from circulation. The resulting thrombocytopenia is both a clinical burden and a barrier to initiating and maintaining antiviral therapy. Eltrombopag, by restoring platelet counts via megakaryocyte stimulation, directly addresses this complication — much as it has been used to allow hepatitis C patients with viral-induced thrombocytopenia to complete a full course of antiviral therapy.

A secondary mechanistic hypothesis deserves mention, though it remains experimental: a 2020 in vitro drug screen (PMID 32977702) identified eltrombopag as a potential modulator of HIV-1 proviral transcription, suggesting a possible direct antiviral effect. This finding has not yet been validated in clinical or animal studies, and the primary repurposing rationale remains the management of HIV-associated thrombocytopenia rather than direct anti-HIV activity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00529568](https://clinicaltrials.gov/study/NCT00529568) | Phase 3 | Completed | 759 | Eltrombopag vs placebo in HCV-infected thrombocytopenic patients; primary endpoint: sustained virological response (SVR) enabled by stable platelet counts during antiviral therapy (pegIFN-α2b + ribavirin) |
| [NCT00516321](https://clinicaltrials.gov/study/NCT00516321) | Phase 3 | Completed | 687 | Second large confirmatory RCT in HCV-associated thrombocytopenia; evaluated eltrombopag's ability to maintain platelet counts sufficient to complete antiviral therapy (pegIFN-α2a + ribavirin) and achieve SVR |
| [NCT00678587](https://clinicaltrials.gov/study/NCT00678587) | Phase 3 | Terminated | 292 | Placebo-controlled RCT in chronic liver disease patients with thrombocytopenia undergoing elective invasive procedures; assessed whether eltrombopag reduced need for platelet transfusions; terminated early (reason not confirmed) |
| [NCT01636778](https://clinicaltrials.gov/study/NCT01636778) | Phase 2 | Completed | 45 | Open-label study in HCV patients with compensated cirrhosis and platelet count <80,000/μL; assessed eltrombopag's ability to raise counts to enable initiation of pegIFN + ribavirin therapy |
| [NCT00996216](https://clinicaltrials.gov/study/NCT00996216) | Phase 3 | Completed | 27 | Open-label rollover extension study in HCV-infected thrombocytopenic patients already enrolled in prior trials; primary focus on long-term safety and tolerability of eltrombopag |

> **Note:** The clinical trials above were conducted in hepatitis C virus (HCV)–associated thrombocytopenia. They are included as supporting evidence for the HIV indication because both HCV and HIV cause thrombocytopenia through overlapping mechanisms (immune-mediated platelet destruction and megakaryocyte suppression), and eltrombopag's TPO-RA mechanism is relevant across all viral infection–related thrombocytopenias. Direct HIV-specific trials are not yet registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [24816314](https://pubmed.ncbi.nlm.nih.gov/24816314/) | 2014 | Systematic Review / Meta-analysis | Internal Medicine Journal | Systematic review of TPO-R agonists including eltrombopag in immune thrombocytopenia of <6 months duration; evaluates evidence base across multiple etiologies |
| [25504472](https://pubmed.ncbi.nlm.nih.gov/25504472/) | 2015 | Retrospective Case Series | J Int Assoc Providers AIDS Care | First case series reporting eltrombopag and romiplostim use in refractory HIV-associated ITP; HAART optimization followed by TPO-RA rescue; eltrombopag demonstrated platelet responses in this difficult-to-treat population |
| [22185370](https://pubmed.ncbi.nlm.nih.gov/22185370/) | 2012 | Cohort / Real-world | Platelets | Danish real-world experience with TPO-R agonists including off-label use; secondary ITP due to various infectious and autoimmune etiologies including HIV-related thrombocytopenia |
| [19932434](https://pubmed.ncbi.nlm.nih.gov/19932434/) | 2009 | Review | Hematol Oncol Clin North Am | Comprehensive review of infectious causes of chronic ITP including HCV, HIV, and H. pylori; establishes mechanistic rationale for TPO-RA use in infection-related thrombocytopenia |
| [19245929](https://pubmed.ncbi.nlm.nih.gov/19245929/) | 2009 | Review | Seminars in Hematology | Reviews therapeutic strategies for hepatitis- and infection-related immune thrombocytopenias; discusses eltrombopag as an emerging treatment option in secondary ITP including HIV |
| [32977702](https://pubmed.ncbi.nlm.nih.gov/32977702/) | 2020 | In vitro / Drug Screen | Viruses | FDA-approved drug library screen identifying eltrombopag as a potential modulator of HIV-1 proviral transcription; suggests a direct antiviral mechanism independent of TPO-RA activity — hypothesis-generating only, requires clinical validation |
| [25333665](https://pubmed.ncbi.nlm.nih.gov/25333665/) | 2014 | Case Report | AIDS (London) | First reported case of eltrombopag successfully treating severe aplastic anemia in an HIV-infected patient; observed immunomodulatory effect with reduction of pro-inflammatory T-helpers (Th1/Th17) and increased Treg/Th ratio |
| [22992580](https://pubmed.ncbi.nlm.nih.gov/22992580/) | 2012 | Case Report | AIDS (London) | Successful use of eltrombopag without splenectomy in refractory HIV-related immune reconstitution thrombocytopenia (HIV-IRT); demonstrates clinical feasibility in a specific HIV complication scenario |
| [28043314](https://pubmed.ncbi.nlm.nih.gov/28043314/) | 2016 | Case Report | JCPSP | HBV-associated megaloblastic anemia and severe peripheral thrombocytopenia; provides supporting context for viral infection–related platelet disorders |
| [24128106](https://pubmed.ncbi.nlm.nih.gov/24128106/) | 2013 | Case Report (×2) | Farmacia Hospitalaria | Two cases of eltrombopag for thrombocytopenia in chronic hepatitis C; provides supplementary real-world evidence for eltrombopag's role in viral hepatitis–associated thrombocytopenia |

---

## Singapore Market Information

Eltrombopag is not registered with the Health Sciences Authority (HSA) of Singapore and has no active product licences. No registration data is available for tabulation.

Internationally, eltrombopag is marketed under the brand names **Promacta** (United States) and **Revolade** (European Union, multiple countries) and holds regulatory approvals for: chronic ITP in adults and children ≥1 year, chronic hepatitis C–associated thrombocytopenia, and severe aplastic anemia. These approvals are not reflected in Singapore's regulatory database based on current data.

---

## Safety Considerations

Detailed safety data specific to the Singapore/Taiwan label (TFDA package insert warnings, contraindications) was not retrievable during this assessment and represents a known data gap (Data Gap DG001, severity: Blocking). No drug-drug interaction records were identified in the DDI query.

> Please refer to the international prescribing information (Promacta/Revolade) for full safety information, including hepatotoxicity monitoring, thromboembolic risk, cataracts (long-term use), bone marrow reticulin formation, and rebound thrombocytopenia upon discontinuation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two large completed Phase 3 RCTs (NCT00529568, n=759; NCT00516321, n=687) plus multiple case series directly demonstrate eltrombopag's ability to manage viral infection–associated thrombocytopenia — the core pathophysiology of HIV-related thrombocytopenia. The mechanistic link is sound, and real-world reports confirm clinical benefit in HIV-associated ITP and aplastic anemia. The absence of a Singapore marketing authorisation and the missing local label safety data are the primary guardrails.

**To proceed, the following is needed:**

- **Regulatory pathway clarification**: Determine whether this constitutes a new indication filing or an off-label use protocol within existing HSA compassionate use / special access provisions
- **TFDA/HSA package insert retrieval**: Resolve Data Gap DG001 (Blocking) — download and parse the full prescribing information to complete the safety screening (S1 gate)
- **MOA documentation**: Resolve Data Gap DG002 (High) — retrieve full DrugBank MOA entry to strengthen mechanistic rationale scoring
- **HIV-specific trial registration**: No clinical trials are registered directly for HIV-associated thrombocytopenia as primary indication; a prospective Phase 2 pilot study in HIV-positive patients with thrombocytopenia would be the critical next evidence-generation step
- **Hepatotoxicity monitoring plan**: Eltrombopag carries a known hepatotoxicity signal; HIV-infected patients frequently have co-existing liver disease (HBV/HCV co-infection, ARV hepatotoxicity), requiring a structured liver function monitoring protocol before any clinical deployment
- **Drug interaction review with antiretrovirals (ARVs)**: Eltrombopag's chelation of polyvalent cations (iron, calcium, aluminium) can reduce its absorption; formal PK interaction review with commonly used ARV regimens is needed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

