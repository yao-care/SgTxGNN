---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
---

# Clopidogrel
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

# Clopidogrel: From Atherothrombotic Event Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Clopidogrel is a thienopyridine-class antiplatelet agent, established for the prevention of atherothrombotic events including acute coronary syndrome, ischaemic stroke, and peripheral arterial disease.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**, with **0 dedicated clinical trials** and **16 publications** currently supporting this specific subtype — though the closely related indication of general migraine disorder has an additional **8 clinical trials** and **20 publications** providing indirect mechanistic and clinical support.
The biological rationale is plausible but clinical evidence remains at the observational level, and the drug is not currently registered in Singapore.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atherothrombotic event prevention (acute coronary syndrome, ischaemic stroke, peripheral arterial disease) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Clopidogrel irreversibly inhibits the P2Y12 ADP receptor on platelet surfaces, blocking ADP-mediated platelet activation and aggregation. This results in sustained antiplatelet effect for the lifetime of the platelet (~7–10 days). Detailed MOA data was not retrievable from the evidence pack; however, Clopidogrel's role as a P2Y12 antagonist is pharmacologically well-characterised, and this mechanism provides the biological bridge to migraine pathophysiology described below.

Migraine with brainstem aura (formerly basilar-type migraine) is distinguished by aura symptoms of brainstem origin — dysarthria, diplopia, tinnitus, ataxia, and altered consciousness — and is thought to share pathophysiology with posterior circulation microembolism. The central mechanistic hypothesis is that patent foramen ovale (PFO) or right-to-left shunts (RLS) allow platelet microaggregates to bypass pulmonary filtration and reach the posterior cerebral circulation, triggering cortical spreading depression (CSD) in the brainstem. Because brainstem aura is more closely linked to posterior circulation events than common migraine with aura, this subtype is mechanistically the most relevant population for antiplatelet intervention. Supporting literature (PMID 16103551, 30478066, 24770421) consistently demonstrates reduction in aura-type migraine with thienopyridines, including Clopidogrel, specifically in patients with confirmed PFO or RLS.

An additional non-vascular mechanism has been proposed: P2Y12 receptors are expressed on microglia within the trigeminal nucleus caudalis and, when activated via the RhoA/ROCK pathway, promote central sensitisation relevant to chronic migraine. Blocking P2Y12 in this central compartment could theoretically reduce trigeminovascular sensitisation independently of platelet effects. However, no clinical trial has yet enrolled patients specifically diagnosed with migraine with brainstem aura as a distinct phenotype; existing evidence is largely extrapolated from broader "migraine with aura + PFO/RLS" populations, which overlap substantially with this subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for migraine with brainstem aura.

> **Context from rank-2 indication (migraine disorder):** The completed Phase 4 CANOA trial (NCT00799045, n=220) directly tested Clopidogrel + Aspirin vs Aspirin alone for post-ASD-closure migraine prevention (published in *JAMA* 2015 and *JAMA Cardiology* 2021). An ongoing large Phase 4 head-to-head trial (NCT05546320, n=1,000) is comparing anticoagulation, antiplatelet (including Clopidogrel), and standard migraine medications in PFO-associated migraine. These trials, while not specific to brainstem aura, provide the closest available controlled evidence for translating to this subtype.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Comprehensive review of antithrombotic drugs as migraine preventive medications; provides most current synthesis of evidence for this drug class in migraine |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | European Heart Journal | PRIMA trial: multicentre RCT of percutaneous PFO closure vs medical therapy (including antiplatelet) in refractory migraine with aura; establishes the PFO–migraine-with-aura mechanistic framework |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | Pilot RCT | Cephalalgia | Direct pilot randomised controlled study of Clopidogrel as prophylactic monotherapy for migraine; first controlled evidence of Clopidogrel's anti-migraine potential independent of cardiac procedure context |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Observational | Heart | Landmark report: Clopidogrel reduced migraine with aura after transcatheter closure of PFO and ASD; initiated the clinical interest in thienopyridines for aura-type migraine |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Observational | J Investig Med | Clopidogrel 75 mg/day added for 3–6 months reduced migraine frequency in patients with drug-refractory migraine and confirmed PFO; PFO prevalence 56.8% in the migraine cohort |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label Pilot | Neurology | TRACTOR study: evaluated ticagrelor in refractory migraine/PFO after observing that thienopyridines (clopidogrel, prasugrel) reduced migraine headache in PFO patients; supports P2Y12-class effect |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective Cohort | Neurology | Retrospective review of thienopyridine therapy in migraineurs with PFO; characterised responder profiles and duration of benefit with Clopidogrel and Prasugrel |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospective Cohort | Cephalalgia | Clopidogrel as primary therapy for migraineurs with right-to-left shunt; directly links platelet activation and paradoxical embolisation to migraine-with-aura trigger mechanism |
| [22992406](https://pubmed.ncbi.nlm.nih.gov/22992406/) | 2012 | Case Series | Cephalalgia | De novo migraine onset after ASD closure; antiplatelet drugs including clopidogrel associated with migraine amelioration, while de novo onset occurred without antiplatelet cover |
| [15966922](https://pubmed.ncbi.nlm.nih.gov/15966922/) | 2005 | Case Series | J Interv Cardiol | Intense migraine developed after percutaneous ASD closure in 5/13 patients; administration of 300 mg clopidogrel produced near-instantaneous pain relief, suggesting direct platelet-mediated mechanism |

---

## Singapore Market Information

Clopidogrel is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No product licences are on record.

> For context, Clopidogrel (e.g., Plavix®) is widely marketed globally and is included on the WHO Essential Medicines List for its established cardiovascular indications. A full HSA registration review would be required before any clinical or research use in Singapore. International prescribing information (SmPC/US PI) should be consulted for reference safety data.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (TFDA warnings, contraindications, and drug-drug interaction records) were not available in this evidence pack. The following gaps have been identified for remediation:
> - **Warnings/Contraindications (DG001, Blocking):** TFDA package insert not yet retrieved; source: TFDA official website (PDF parsing required)
> - **MOA data (DG002, High):** DrugBank API query pending
>
> Based on general pharmacological knowledge, key safety considerations relevant to this evaluation include: haemorrhagic risk (particularly intracranial and GI bleeding), CYP2C19 pharmacogenomic variability (poor metabolisers have markedly reduced antiplatelet effect), and clinically significant interactions with PPIs (particularly omeprazole) and anticoagulants.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis linking Clopidogrel's P2Y12 inhibition to migraine with brainstem aura via PFO-mediated posterior circulation microembolism is biologically coherent and supported by a consistent body of observational data and indirect RCT evidence in the broader migraine-with-aura-plus-PFO population (L3). However, no clinical trial has specifically enrolled patients with the migraine with brainstem aura phenotype, the drug is unregistered in Singapore, and critical safety data (package insert warnings, DDI profile) have not been retrieved — precluding a full safety review at this stage.

**To proceed, the following is needed:**
- Retrieve TFDA/HSA package insert to complete safety review (DG001 — Blocking)
- Query DrugBank API for full MOA and pharmacogenomic data (DG002 — High priority)
- Confirm HSA registration pathway requirements for an investigational or compassionate use scenario
- Conduct a sub-group analysis of PRIMA and CANOA trial datasets to identify whether any enrolled patients had brainstem aura specifically, as a proxy efficacy signal
- Assess feasibility of a prospective observational registry in PFO-confirmed patients presenting with migraine with brainstem aura, using Clopidogrel as an add-on therapy
- Include CYP2C19 genotyping protocol in any future study design, given known pharmacogenomic variability in Clopidogrel bioactivation
- Await results of NCT04946734 (SPRING, Phase 3, n=440, expected completion Sep 2025) and NCT05546320 (COMPETE, Phase 4, n=1,000), which will materially upgrade the evidence base for the broader migraine-with-PFO indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

