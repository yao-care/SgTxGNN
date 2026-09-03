---
layout: default
title: Praziquantel
parent: 僅模型預測 (L5)
nav_order: 810
evidence_level: L5
indication_count: 10
---

# Praziquantel
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

# Praziquantel: From Schistosomiasis to *Plasmodium falciparum* Malaria

## One-Sentence Summary

> Praziquantel is a broad-spectrum antihelmintic, internationally established for treating schistosomiasis and other trematode/cestode infections, though it currently holds no market registration in Singapore.
> Among the ten indications the TxGNN model surfaced for this drug, **Plasmodium falciparum malaria** is the only one supported by real-world clinical evidence — including a 2025 Phase IIb RCT directly testing praziquantel's antimalarial activity —
> with **5 clinical trials** and **17 publications** currently touching on this direction, most concerning malaria–schistosomiasis co-infection populations.

*Note on candidate selection: the six highest-scoring TxGNN predictions (all uterine/soft-tissue sarcoma subtypes, e.g. uterine corpus leiomyosarcoma at 97.3%) carry zero supporting trials or literature and are explicitly flagged in the model's own rationale as likely reflecting sarcoma-node clustering in the embedding space rather than a drug-specific signal. This report therefore focuses on the highest-evidence candidate (rank 2) rather than the raw top-ranked score.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schistosomiasis and other trematode/cestode infections (established international indication; Singapore label data not on file) |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 97.22% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for praziquantel is not available in this evidence pack. Based on known pharmacology, praziquantel is a pyrazinoisoquinoline antihelmintic that increases calcium ion permeability in trematode/cestode cell membranes, causing tetanic paralysis and eventual death of the parasite. This mechanism is well established for schistosomiasis and other fluke/tapeworm infections but has no established biological link to *Plasmodium* (a protozoan, not a helminth).

Despite the lack of a validated shared mechanism, praziquantel and antimalarial control programs frequently overlap operationally: schistosomiasis and malaria are co-endemic across sub-Saharan Africa, and mass drug administration campaigns often deliver both interventions to the same populations. This operational overlap appears to be reflected in the TxGNN knowledge graph — most of the underlying evidence base consists of co-infection and epidemiological studies rather than direct antimalarial efficacy trials.

That said, a small but growing body of direct evidence exists. A 1998 open-label study reported that oral praziquantel cleared *P. falciparum* parasitaemia in several treated patients, and a 2025 double-blind, placebo-controlled Phase IIb trial in asymptomatic Gabonese adults specifically re-examined praziquantel's antimalarial efficacy. The mechanism behind this activity remains unclear — proposed hypotheses include host immune modulation following anthelminthic treatment or off-target effects on parasite ion channels — and requires further mechanistic study before this signal can be considered pharmacologically established.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01722539](https://clinicaltrials.gov/study/NCT01722539) | Phase 3 | Completed | 616 | Tested SP ± piperaquine intermittent preventive treatment in Congolese schoolchildren; did not use praziquantel (Grade C — low relevance) |
| [NCT00347113](https://clinicaltrials.gov/study/NCT00347113) | N/A | Completed | 620 | Examined effect of schistosome/STH infection and anthelminthic intervention (likely including PZQ) on malaria burden in Tanzanian children (Grade B — indirect) |
| [NCT03893097](https://clinicaltrials.gov/study/NCT03893097) | Phase 3 | Completed | 726 | Compared artesunate-mefloquine vs. standard praziquantel for schistosomiasis; not an antimalarial efficacy trial for PZQ (Grade C) |
| [NCT02769013](https://clinicaltrials.gov/study/NCT02769013) | N/A | Completed | 380 | Assessed effect of neglected tropical diseases (including PZQ-treated schistosomiasis) on *P. falciparum* transmission (Grade B — indirect) |
| [NCT03640403](https://clinicaltrials.gov/study/NCT03640403) | Phase 3 | Completed | 1555 | Compared dihydroartemisinin-piperaquine vs. artesunate-amodiaquine for IPT in Tanzanian schoolchildren; did not test PZQ (Grade C) |

**Note:** None of the five registered trials directly tested praziquantel as an antimalarial monotherapy; the strongest direct clinical evidence for this indication comes from the literature (see below), not from registered trials.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41159886](https://pubmed.ncbi.nlm.nih.gov/41159886/) | 2025 | RCT (Phase IIb, double-blind, placebo-controlled) | The Journal of Infectious Diseases | Direct test of praziquantel efficacy against *P. falciparum* infection in asymptomatic Gabonese adults; preliminary evidence of clinically important antimalarial effect from certain anthelminthics |
| [37957702](https://pubmed.ncbi.nlm.nih.gov/37957702/) | 2023 | RCT (observer-blind) | Malaria Journal | Randomized trial assessing feasibility/safety of combining helminth MDA (praziquantel) with seasonal malaria chemoprevention in Senegalese children |
| [10531774](https://pubmed.ncbi.nlm.nih.gov/10531774/) | 1998 | Clinical Study | JPMA | Oral praziquantel (30 mg/kg/day) produced complete parasitological cure in 8/10 patients with *P. falciparum*/*P. vivax* malaria within 4–6 days |
| [38265982](https://pubmed.ncbi.nlm.nih.gov/38265982/) | 2024 | Scoping Review | PLoS Neglected Tropical Diseases | Reviewed integration efforts between malaria and schistosomiasis control programs, both reliant on mass drug delivery (praziquantel for schisto) |
| [17568947](https://pubmed.ncbi.nlm.nih.gov/17568947/) | 2007 | Cohort | Memórias do Instituto Oswaldo Cruz | Studied anti-malaria antibody responses in children with *S. haematobium*/*P. falciparum* co-infection before chemotherapeutic (PZQ) treatment |
| [21696629](https://pubmed.ncbi.nlm.nih.gov/21696629/) | 2011 | Cohort/Intervention | BMC Int Health Hum Rights | 33-month follow-up on integrated school-based deworming (PZQ) plus prompt malaria treatment on helminth–*P. falciparum* co-infection |
| [37808169](https://pubmed.ncbi.nlm.nih.gov/37808169/) | 2023 | Cohort | J Parasitology Research | Investigated *P. falciparum* and *S. haematobium* co-infection and association with anaemia in pregnant Ghanaian women |
| [20353134](https://pubmed.ncbi.nlm.nih.gov/20353134/) | 2006 | Cohort | Central African J Medicine | Examined humoral immune response changes after chemotherapy in single/co-infected *S. haematobium*/*P. falciparum* patients |
| [25210876](https://pubmed.ncbi.nlm.nih.gov/25210876/) | 2014 | Cohort | PLoS Neglected Tropical Diseases | Long-term *P. falciparum* carriers co-infected with *S. haematobium* (PZQ-treated) showed enhanced protection from febrile malaria in Mali |
| [30080853](https://pubmed.ncbi.nlm.nih.gov/30080853/) | 2018 | Cohort | PLoS Neglected Tropical Diseases | *S. haematobium* infection modified *P. falciparum* prevalence/incidence in Gabonese school-age children |

---

## Singapore Market Information

Praziquantel currently has **no registered product license in Singapore** (`taiwan_regulatory.total_licenses = 0`, market status: Not Marketed). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction, contraindication, or warning data are currently available in this evidence pack (flagged as a **Blocking** data gap — TFDA/regulatory label warnings must be sourced before any safety pre-screen can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The strongest direct evidence for antimalarial activity is a single 2025 Phase IIb RCT and a decades-old open-label study of ten patients — insufficient to establish efficacy, and the underlying mechanism is undefined. The drug is unregistered in Singapore, and safety/contraindication data (a Blocking-severity gap) is completely unavailable, precluding any safety pre-screen.

**To proceed, the following is needed:**
- Full-text review and independent validation of the 2025 Phase IIb RCT (PMID 41159886) efficacy results
- Praziquantel mechanism of action (MOA) data from DrugBank to assess biological plausibility against *Plasmodium*
- TFDA/regulatory-equivalent package insert data (warnings, contraindications, DDI) — currently a Blocking gap
- A defined regulatory pathway assessment, since the drug is not currently marketed in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

