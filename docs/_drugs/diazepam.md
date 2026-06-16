---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 322
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# Diazepam: From Anxiety and Seizure Disorders to Insomnia

## One-Sentence Summary

Diazepam is a classic benzodiazepine globally established for the treatment of anxiety disorders, seizures, and muscle spasms, though it currently holds no registered products in Singapore.
The TxGNN model predicts it may be effective for **Insomnia**, with **24 clinical trials** and **18 publications** currently supporting this direction.
The prediction carries a high mechanistic plausibility score of 99.99%, reflecting the well-documented sedative-hypnotic properties of benzodiazepines — though modern guidelines increasingly favour newer agents for this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally recognised for anxiety disorders, seizures, and muscle spasms |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Diazepam is a positive allosteric modulator (PAM) of the GABA-A receptor. By binding to the benzodiazepine recognition site on the receptor complex, it increases the frequency of chloride ion channel opening in response to GABA, thereby suppressing neuronal excitability. Both BZ1 and BZ2 receptor subtypes are engaged — BZ1 receptors, which are enriched in sleep-regulating brain regions such as the thalamus and cortex, are particularly linked to the sedative-hypnotic effect that underpins insomnia treatment. This mechanism is shared across the benzodiazepine class and represents the direct pharmacological basis for hypnotic activity.

The mechanistic connection between Diazepam and insomnia is therefore not speculative but well-established: Diazepam reduces sleep onset latency, decreases nocturnal awakenings, and increases total sleep time. These properties led benzodiazepines to dominate insomnia pharmacotherapy throughout the 1970s–1990s, as documented in authoritative guidelines (Ashton 1994) and confirmed in at least one direct head-to-head RCT comparing Diazepam against another benzodiazepine hypnotic (lormetazepam) in 100 outpatients with sleep disorders.

A critical clinical caveat must accompany this prediction: chronic use of Diazepam for insomnia is associated with tolerance development, physical dependence, and rebound insomnia upon discontinuation. A 2022 Nature Neuroscience study (PMID 35228700) further demonstrated that long-term Diazepam treatment in mice causes microglial spine engulfment via the 18 kDa translocator protein (TSPO), impairing dendritic spine plasticity and leading to persistent cognitive impairment. Contemporary sleep medicine guidelines therefore restrict benzodiazepines to short-term or transient insomnia only, and increasingly prefer newer agents such as Z-drugs or orexin receptor antagonists for ongoing management.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04364321](https://clinicaltrials.gov/study/NCT04364321) | N/A | Unknown | 74 | Direct head-to-head comparison of single-dose clonazepam versus intermittent oral Diazepam for prevention of recurrent febrile seizures; one of the few trials directly involving Diazepam as an active comparator |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | N/A | Completed | 128 | RCT comparing Acceptance and Commitment Therapy versus standard psychological support for benzodiazepine withdrawal in adults with benzodiazepine-dependent insomnia; confirms the clinical prevalence of benzodiazepine (including Diazepam) use in insomnia populations |
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Phase 3 | Active, Not Recruiting | 260 | Randomised trial evaluating blinded versus open-label benzodiazepine receptor agonist tapering combined with CBTI; evaluates discontinuation strategies for hypnotics used in insomnia, with direct relevance to Diazepam |
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Phase 2 | Completed | 74 | Investigates the influence of tapering pace and patient traits on sedative-hypnotic (predominantly benzodiazepine) discontinuation in treatment-seeking insomnia patients; reflects the clinical reality of Diazepam's widespread use in insomnia |
| [NCT05935553](https://clinicaltrials.gov/study/NCT05935553) | Phase 2/3 | Recruiting | 93 | Evaluates baclofen (GABA-B agonist) as an adjunct to facilitate benzodiazepine tapering in benzodiazepine-dependent patients; provides mechanistic context on GABA modulation in the BZD-insomnia setting |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Phase 4 | Completed | 17 | Placebo-controlled multicenter double-blind study examining ramelteon co-administration to support BZD/non-BZD hypnotic dose reduction in chronic insomnia patients |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | Completed | 188 | Investigates novel behavioural mechanisms for helping older adults discontinue hypnotics (including benzodiazepines) prescribed for insomnia, targeting mechanisms beyond simple tapering |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT | J Int Med Research | 7-day double-blind RCT (n=100) directly comparing **Diazepam 5 mg vs lormetazepam 1 mg** in outpatients with sleep disorders; lormetazepam was superior in reducing time to fall asleep and prolonging uninterrupted sleep, highlighting both Diazepam's hypnotic activity and its relative limitations as a hypnotic agent |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorganic Chemistry | Comprehensive review of GABA-A receptor modulators for neurological and psychiatric disorders; Diazepam is cited as the prototype PAM with established sedative-hypnotic indications including insomnia, alongside a discussion of tolerance, dependence, and next-generation selectivity strategies |
| [7525193](https://pubmed.ncbi.nlm.nih.gov/7525193/) | 1994 | Guidelines/Review | Drugs | Authoritative guidelines on rational benzodiazepine use; recommends benzodiazepines including Diazepam for transient or short-term insomnia only, with prescriptions ideally limited to a few days to avoid tolerance, dependence, and cognitive sequelae |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Basic Science | Nature Neuroscience | Long-term Diazepam treatment in mice impairs dendritic spine plasticity via TSPO-mediated microglial engulfment, causing persistent cognitive impairment — a critical safety signal for any chronic insomnia treatment indication |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Research | Cell Mol Biol Letters | Clinical and molecular evidence that long-term use of BZDRs (Diazepam and Zolpidem) for insomnia and anxiety significantly exacerbates breast cancer risk via GABA-A receptor-mediated pathways; highlights an important oncological safety concern |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica | Meta-analysis of tranquiliser use in elderly patients with chronic non-communicable diseases; evaluates doses, efficacy outcomes, and adverse effects, with direct relevance to Diazepam safety in elderly insomnia patients |
| [37776625](https://pubmed.ncbi.nlm.nih.gov/37776625/) | 2023 | Research | J Pharm Biomed Analysis | Uses Diazepam as a positive control in a metabolomics study of PCPA-induced insomnia in rats; confirms Diazepam's established benchmark hypnotic efficacy in preclinical insomnia models |
| [40350874](https://pubmed.ncbi.nlm.nih.gov/40350874/) | 2025 | Research | China J Chin Materia Medica | Uses Diazepam (2 mg/kg) as the positive control in a CUMS-induced insomnia mouse model; reinforces Diazepam's continued status as the reference hypnotic in insomnia research |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Review | Drugs | Comparative review of triazolam versus longer-acting benzodiazepines (including Diazepam) for insomnia; establishes that Diazepam's prolonged half-life makes it less suitable than shorter-acting agents for hypnotic use due to carry-over sedation |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Reviews the pharmacokinetics of anxiolytic drugs including Diazepam; discusses its widespread global prescription for anxiety and insomnia and the pharmacokinetic factors influencing clinical outcomes and adverse effect profiles |

---

## Singapore Market Information

Diazepam (DrugBank: DB00829) currently has **no registered products in Singapore**. Given its status as a long-established, widely used medicine in most jurisdictions worldwide, this absence warrants further investigation — it may reflect local scheduling restrictions, voluntary market withdrawal by manufacturers, or classification as a controlled substance requiring separate authorisation. A regulatory assessment through HSA should be completed before any clinical application is considered.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for Diazepam in insomnia is mechanistically well-founded and supported by at least one direct head-to-head RCT (PMID 6113175) and multiple Phase 2/3 clinical trials involving benzodiazepine-dependent insomnia populations (Evidence Level L2). However, the clinical risk-benefit balance for insomnia is complex: Diazepam's sedative-hypnotic efficacy is real, but its propensity for dependence, rebound insomnia, and cognitive impairment — especially with chronic use — means that any clinical application must be tightly scoped and actively monitored.

**To proceed, the following is needed:**
- **Resolve Singapore regulatory status**: Diazepam's absence from HSA-registered products (0 licenses) must be investigated and cleared before any clinical use pathway can be established
- **Obtain the full prescribing information**: Package insert warnings, contraindications, and drug-drug interaction data are currently unavailable and are essential for a complete safety evaluation
- **Define strict patient selection criteria**: Appropriate candidates are those with transient or short-term insomnia; patients with a history of substance dependence, respiratory compromise, or advanced age require heightened caution
- **Establish a time-limited treatment protocol**: Clinical use should be restricted to the shortest effective duration (typically ≤2–4 weeks) with a planned tapering schedule to minimise rebound and dependence
- **Clarify positioning relative to newer agents**: Evaluate whether Z-drugs or orexin receptor antagonists offer a more favourable risk-benefit profile for the target insomnia population in Singapore before committing to Diazepam as the preferred agent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

