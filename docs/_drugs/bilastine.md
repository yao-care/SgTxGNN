---
layout: default
title: Bilastine
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Bilastine
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

# Bilastine: From Allergic Rhinitis to Cold Urticaria

## One-Sentence Summary

Bilastine is a second-generation, non-sedating H1-antihistamine with established international approval for allergic rhinitis/rhinoconjunctivitis, but currently not registered in Singapore.
The TxGNN model identifies **Cold Urticaria** as the highest-confidence, mechanistically plausible new indication (rank #7, score 90.15%), supported by **2 completed clinical trials** and **1 RCT-level publication**; the closely related indication **Allergic Urticaria** (rank #9) is additionally backed by **6 clinical trials** and **20 publications**, reaching L1 evidence level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis / rhinoconjunctivitis (international approval; not registered in Singapore) |
| Predicted New Indication | Cold Urticaria |
| TxGNN Prediction Score | 90.15% (Cold Urticaria, overall rank #7) |
| Evidence Level | L2 (Cold Urticaria) · L1 (Allergic Urticaria) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on TxGNN ranking:** The six highest-scoring TxGNN predictions (ranks #1–#6: duodenal obstruction, duodenal ulcer, duodenogastric reflux, gastric ulcer, linitis plastica, duodenitis) all carry a **Hold** recommendation due to mechanistic implausibility — H1 receptor blockade has no established role in upper GI structural or acid-mediated pathology. These are assessed as knowledge-graph false positives. The meaningful predictions begin at rank #7 (Cold Urticaria).

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not captured in this Evidence Pack. Based on well-established pharmacological knowledge, Bilastine is a highly selective H1-receptor inverse agonist: it binds to H1 receptors and stabilises them in an inactive state, blocking histamine-mediated downstream signalling. Key pharmacological characteristics include non-CNS penetration (non-sedating profile), absence of significant CYP450 metabolism (low drug-drug interaction potential), rapid onset of action (~1 hour), and prolonged effect duration (~24 hours). These properties distinguish it from older first-generation antihistamines and place it among the most selective second-generation agents.

Cold Urticaria (cold contact urticaria, CCU) is a physical urticaria subtype in which cold stimulus directly activates mast cells, triggering degranulation and histamine release. The resulting wheal-and-flare reaction is histamine-mediated via H1 receptors — making H1-antihistamines the recommended first-line treatment in international guidelines (EAACI/GA²LEN/EDF/WAO). Bilastine's high H1 selectivity is mechanistically well-matched to this pathophysiology. Published clinical evidence further shows that dose escalation to 40–80 mg (2–4× standard dose) yields dose-dependent improvements in cold stimulation thresholds, addressing the common clinical scenario where standard doses provide insufficient control in CCU patients.

The same H1-mediated mechanism applies to Allergic Urticaria, where allergen exposure — rather than cold — triggers mast cell activation. Bilastine has been evaluated in large pivotal Phase 3 RCTs for this indication and achieved EU regulatory approval. The convergence of strong mechanistic alignment and high-quality clinical evidence across both urticaria subtypes makes this one of the most well-supported predictions in the dataset. By contrast, C1 inhibitor deficiency (rank #8, hereditary angioedema) is bradykinin-mediated rather than histamine-mediated; antihistamines are ineffective for acute HAE attacks and that prediction should be disregarded entirely.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01271075](https://clinicaltrials.gov/study/NCT01271075) | Phase 2/3 | Completed | 20 | Double-blind triple crossover RCT in cold contact urticaria: Bilastine 20/40/80 mg vs placebo; primary endpoints were critical stimulation time threshold (CSTT) and critical temperature threshold (CTT); direct mechanistic and efficacy assessment |
| [NCT00421109](https://clinicaltrials.gov/study/NCT00421109) | Phase 3 | Completed | 522 | Pivotal RCT: Bilastine 20 mg QD vs levocetirizine 5 mg QD vs placebo for chronic idiopathic urticaria; key trial supporting EU marketing authorisation |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Completed | 150 | Comparative study of 5 antihistamines in urticaria (including cold urticaria subgroup) in a Latin American tropical population; pharmacokinetic and pharmacodynamic comparison |
| [NCT01081574](https://clinicaltrials.gov/study/NCT01081574) | Phase 1/2 | Completed | 36 | Multicentre adaptive PK study in children aged 2–<12 years with allergic rhinoconjunctivitis or chronic urticaria; established paediatric dosing regimen |
| [NCT07042828](https://clinicaltrials.gov/study/NCT07042828) | Phase 1 | Completed | 42 | Full replicate crossover bioequivalence study for generic bilastine tablet formulation under fasting conditions; confirms manufacturing equivalence |
| [NCT00419783](https://clinicaltrials.gov/study/NCT00419783) | Phase 1 | Completed | 30 | QTc cardiac safety study: bilastine 20 mg and 100 mg (5× standard) vs moxifloxacin 400 mg and placebo over 4 days; cardiac safety confirmed at therapeutic doses |
| [NCT04967092](https://clinicaltrials.gov/study/NCT04967092) | Phase 2 | Unknown | 58 | Double-blind RCT for Xiao-Feng Powder (Chinese herbal formula) in chronic urticaria; bilastine used as active control only — not the investigational agent; status uncertain |
| [NCT02576041](https://clinicaltrials.gov/study/NCT02576041) | Phase 4 | Completed | 19 | CNS safety: assessment of bilastine's effects on attention and reaction time using an F1 high-speed simulator in rhinitis/urticaria patients; confirms non-sedating profile |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [35593100](https://pubmed.ncbi.nlm.nih.gov/35593100/) | 2022 | Systematic Review + Meta-Analysis | Am J Rhinology & Allergy | Meta-analysis of RCTs: bilastine significantly reduces total nasal/ocular symptom scores in allergic rhinitis and wheal/flare scores in chronic urticaria vs placebo |
| [36380619](https://pubmed.ncbi.nlm.nih.gov/36380619/) | 2023 | Systematic Review + Meta-Analysis | Int Archives Allergy Immunol | Meta-analysis specific to chronic urticaria: bilastine superior to placebo in reducing wheal size and erythema; evidence-based reference for clinical use |
| [23742030](https://pubmed.ncbi.nlm.nih.gov/23742030/) | 2013 | RCT / Dose-escalation study | Allergy | Up-dosing bilastine (20→40→80 mg) in cold contact urticaria: dose-dependent improvement in CSTT and CTT; first clinical evidence for dose escalation in CCU |
| [33030434](https://pubmed.ncbi.nlm.nih.gov/33030434/) | 2021 | Systematic Review | J Investig Allergol Clin Immunol | Systematic review of antihistamine up-dosing (up to 4× licensed dose) in chronic spontaneous urticaria; supports guideline recommendation for dose escalation including bilastine |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Drug Review | Drugs | Comprehensive review of bilastine Phase 3 RCT data; summarises efficacy vs placebo and levocetirizine in seasonal allergic rhinitis and chronic urticaria |
| [26844221](https://pubmed.ncbi.nlm.nih.gov/26844221/) | 2016 | Consensus Statement | Asia Pacific Allergy | Asia-Pacific regional consensus on bilastine for allergic rhinitis and chronic urticaria; directly relevant to Singapore patient population and prescribing context |
| [36382168](https://pubmed.ncbi.nlm.nih.gov/36382168/) | 2022 | Drug Review / Guideline | Australian Prescriber | Regulatory prescribing summary issued in the Asia-Pacific context for bilastine in allergic rhinoconjunctivitis and urticaria |
| [28210286](https://pubmed.ncbi.nlm.nih.gov/28210286/) | 2017 | Practice Guideline / Review | Drugs in Context | Clinical decision guide covering bilastine use in co-morbid patients, concomitant medications, and special populations; based on Medical Information Department queries |
| [34850647](https://pubmed.ncbi.nlm.nih.gov/34850647/) | 2022 | Pediatric Review | Immunotherapy | Bilastine paediatric development summary (2–<12 years); EMA-authorised pharmacokinetic modelling and Phase 3 trial in children with rhinoconjunctivitis and urticaria |
| [38742145](https://pubmed.ncbi.nlm.nih.gov/38742145/) | 2024 | Delphi Expert Consensus | Drugs in Context | International Delphi study from EU/Asia experts defining bilastine's positioning among second-generation antihistamines for rhinitis and urticaria across age groups |

---

## Singapore Market Information

Bilastine is **not currently registered in Singapore**. There are no recorded product authorizations (0 licenses).

For reference, bilastine holds regulatory approval in the following major jurisdictions:

| Region | Brand Name | Approved Indications |
|--------|-----------|---------------------|
| European Union (EMA) | Bilaxten / Ilaxten | Allergic rhinoconjunctivitis, urticaria (adults, adolescents, children ≥2 years) |
| Japan (PMDA) | Bilanoa | Allergic rhinitis, urticaria |
| South Korea (MFDS) | Bilaxten | Allergic rhinitis, urticaria |
| Australia (TGA) | Bilaxten | Allergic rhinoconjunctivitis, urticaria |

The absence of Singapore registration represents a directly addressable regulatory gap for a drug with a well-established international safety and efficacy profile.

---

## Safety Considerations

No Singapore-specific package insert data is available as bilastine is unregistered locally. Based on international clinical development data:

- **Sedation**: Does not penetrate the blood-brain barrier at therapeutic doses; no psychomotor impairment at 20 mg (confirmed by driving simulator study NCT02576041)
- **Cardiac safety**: No clinically significant QTc prolongation at 20 mg standard dose; minor effects observed only at supratherapeutic doses (100 mg) in combination with the P-gp/CYP3A4 inhibitor ketoconazole
- **Drug interactions**: No significant CYP450 metabolism; low inherent DDI risk; however, concomitant use with P-glycoprotein inhibitors (e.g., ketoconazole, erythromycin) can increase bilastine plasma exposure — caution advised
- **Food interaction**: Bioavailability reduced when taken with food or grapefruit juice; should be taken on an empty stomach

Please refer to the EU Summary of Product Characteristics (EU SmPC) or Japanese prescribing information for the complete, authoritative safety profile.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bilastine's H1-selective inverse agonism is directly mechanistically matched to histamine-driven urticaria. Allergic Urticaria is supported by a pivotal Phase 3 RCT (n=522, L1 evidence) and two meta-analyses; Cold Urticaria by a dedicated Phase 2/3 crossover RCT and a dose-escalation publication (L2 evidence). The drug is approved in the EU, Japan, Australia, and South Korea. Singapore's current absence of any bilastine registration is a clear market gap for a mature, well-characterised antihistamine with a favourable safety profile.

**To proceed, the following is needed:**
- Initiate an HSA Singapore registration application using the EU SmPC or Japanese package insert as reference dossier (abridged approval pathway may apply)
- Obtain and review the full EU SmPC for safety label localisation and YMYL compliance
- Confirm that both allergic urticaria and cold urticaria are captured within the proposed Singapore label, or plan for separate indication extension
- Clarify the regulatory position on dose escalation (40–80 mg) for cold urticaria — whether a separate dosing section is required in the local label
- Review the P-gp interaction warning in the context of commonly co-prescribed drugs in Singapore (e.g., macrolide antibiotics)
- Prepare a pharmacovigilance plan aligned with HSA post-market surveillance requirements
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

