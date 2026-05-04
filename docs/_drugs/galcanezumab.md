---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 250
evidence_level: L5
indication_count: 10
---

# Galcanezumab
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

# Galcanezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Galcanezumab (Emgality®) is a humanized monoclonal antibody targeting calcitonin gene-related peptide (CGRP), approved in the US, EU, and Japan for preventive treatment of episodic and chronic migraine, as well as episodic cluster headache.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** — a rare migraine subtype historically excluded from triptan trials due to vasoconstriction concerns — with strong mechanistic plausibility and **20 supporting publications**.
Although no clinical trials are dedicated to this specific subtype, the mechanistic rationale is strong and indirect evidence from hemiplegic migraine studies is accumulating.

> **Analyst Note on TxGNN Rankings**: The top-ranked TxGNN predictions (ranks 1–4: heparin cofactor 2 deficiency, antithrombin deficiency, factor 5 excess, thrombophilia) receive very high scores (0.990–0.995) but are assessed as likely false positives driven by shared vascular-regulatory nodes in the knowledge graph. No mechanistic link or supporting evidence exists between CGRP antagonism and coagulation disorders. **Migraine with brainstem aura (rank 5)** is the highest-ranked indication with both mechanistic plausibility and supporting literature, and is therefore selected as the primary focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Migraine prevention (episodic/chronic migraine; episodic cluster headache) — globally approved, not yet registered in Singapore |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 98.33% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Galcanezumab is a humanized IgG4 monoclonal antibody that selectively binds free CGRP, preventing it from activating the CGRP receptor on trigeminal nerve terminals and cranial blood vessels. During migraine attacks, CGRP is released from trigeminal ganglia and its circulating levels rise sharply — this rise has been documented not only in common migraine but across all major migraine subtypes, including those with aura. By blocking this release-triggered cascade peripherally, galcanezumab reduces the frequency and severity of attacks without causing vasoconstriction.

Migraine with brainstem aura (MBA), formerly called basilar-type migraine, is characterized by fully reversible aura symptoms originating from the brainstem — including dysarthria, vertigo, tinnitus, diplopia, ataxia, or decreased level of consciousness — followed by headache. Historically, MBA was listed as a relative contraindication for triptans due to theoretical concerns about basilar artery vasoconstriction. Anti-CGRP monoclonal antibodies carry no such risk: they do not affect vascular tone directly and have shown no vasoconstriction signal in cardiovascular safety studies. This makes galcanezumab a mechanistically well-suited and potentially safer preventive option for MBA patients who currently have limited pharmacological choices.

Indirect support comes from the growing body of evidence in hemiplegic migraine — another "complicated" aura subtype previously thought unsuitable for standard migraine biologics. Multiple case series and a pooled individual-patient analysis (2026) now document meaningful reduction in attack frequency with anti-CGRP mAbs in hemiplegic migraine. Since MBA and hemiplegic migraine share similar pathophysiology (cortical spreading depression propagating to brainstem or motor cortex) and both involve CGRP-mediated trigeminovascular activation, positive results in hemiplegic migraine provide meaningful biological plausibility for MBA.

---

## Clinical Trial Evidence

Currently no dedicated clinical trials for galcanezumab specifically in migraine with brainstem aura are registered on ClinicalTrials.gov or ICTRP.

> **Context**: The pivotal Phase 3 trials (EVOLVE-1, EVOLVE-2, REGAIN) excluded patients with brainstem aura per legacy triptan-era safety criteria — this represents a protocol exclusion gap, not evidence of clinical failure. Prospective studies specifically enrolling MBA patients are needed.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29813147](https://pubmed.ncbi.nlm.nih.gov/29813147/) | 2018 | Phase 3 RCT | JAMA Neurology | EVOLVE-1: Galcanezumab significantly reduced monthly migraine headache days vs placebo in episodic migraine over 6 months |
| [33549036](https://pubmed.ncbi.nlm.nih.gov/33549036/) | 2021 | Phase 3 Pooled Analysis | J Headache Pain | Pooled EVOLVE-1, EVOLVE-2, REGAIN data: galcanezumab reduced headache severity and accompanying symptoms (nausea, photophobia, phonophobia) across episodic and chronic migraine |
| [32504377](https://pubmed.ncbi.nlm.nih.gov/32504377/) | 2020 | Systematic Review | Drugs | Comprehensive review of galcanezumab efficacy and safety for episodic/chronic migraine and cluster headache; confirms well-established CGRP-blocking mechanism |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Individual Patient Quantitative Analysis | J Headache Pain | Anti-CGRP mAbs effective and generally safe in hemiplegic migraine — the most closely related "complicated aura" subtype to brainstem aura |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case Reports & Review | J Clin Medicine | Anti-CGRP mAbs (including galcanezumab) may reduce migraine aura frequency; emerging case evidence reviewed with mechanistic discussion |
| [37366160](https://pubmed.ncbi.nlm.nih.gov/37366160/) | 2023 | Case Series | Headache | Tertiary headache center experience: anti-CGRP mAbs showed promising efficacy in hemiplegic migraine patients with no adequate prior treatment options |
| [39345003](https://pubmed.ncbi.nlm.nih.gov/39345003/) | 2025 | Case Series | Headache | Galcanezumab effective in PRRT2-associated familial hemiplegic migraine — demonstrates efficacy extends to genetically defined rare aura subtypes |
| [40341526](https://pubmed.ncbi.nlm.nih.gov/40341526/) | 2025 | Genetic/Subtype Analysis | Headache | CGRP antagonist therapy responsive in two genetic migraine disorders (including one with brainstem-predominant features); supports CGRP pathway relevance across migraine genotypes |
| [36927366](https://pubmed.ncbi.nlm.nih.gov/36927366/) | 2023 | Secondary RCT Analysis | J Headache Pain | Galcanezumab altered incidence of aura episodes and premonitory symptoms in responders; relevant to understanding aura-modifying potential |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Mechanistic Review | Handbook Exp Pharmacol | Foundational review of CGRP's role in migraine pathophysiology, including trigeminal activation, aura, and brainstem-level involvement |

---

## Singapore Market Information

Galcanezumab is **not currently registered in Singapore**. No Health Sciences Authority (HSA) authorizations are on record.

> Galcanezumab is approved by the US FDA (August 2018), EMA (November 2018), PMDA Japan (April 2021), and several other regulatory authorities for migraine prevention. A Singapore registration submission would be a prerequisite for any formal clinical use in this market.

---

## Safety Considerations

Formal package insert data for Singapore is unavailable as the drug is unregistered. Based on published literature and global regulatory labels:

- **Injection site reactions**: The most commonly reported adverse effect in Phase 3 trials; generally mild and transient
- **Rare cerebrovascular risk**: At least one case of reversible cerebral vasoconstriction syndrome (RCVS) has been reported following a loading dose ([PMID 39365416](https://pubmed.ncbi.nlm.nih.gov/39365416/)); requires clinical vigilance especially in aura-predominant patients
- **Pregnancy exposure**: Limited data; two cases of normal delivery following first- and second-trimester galcanezumab exposure have been reported ([PMID 41760025](https://pubmed.ncbi.nlm.nih.gov/41760025/)), but routine use in pregnancy cannot be recommended
- **Drug interactions**: No significant pharmacokinetic drug-drug interactions identified; as a monoclonal antibody, galcanezumab is not metabolized by CYP enzymes

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Galcanezumab has strong mechanistic plausibility for migraine with brainstem aura — CGRP elevation is a consistent finding across all migraine subtypes, and the absence of vasoconstriction removes the primary historical safety concern that blocked triptan use in this population. Phase 3 RCT data firmly establishes the drug class's efficacy in migraine broadly, and case series in hemiplegic migraine (a closely related aura subtype) are increasingly supportive. The evidence gap is subtype-specific rather than drug-class-specific.

**To proceed, the following is needed:**

- **Dedicated clinical evidence**: Prospective observational study or registry specifically enrolling migraine with brainstem aura patients treated with anti-CGRP mAbs; could be initiated without a formal RCT as a first step
- **Singapore regulatory pathway**: HSA registration for the core migraine indication must be completed before any local use is possible; this should be treated as a prerequisite
- **MOA data completion**: Retrieve full mechanism-of-action and pharmacology data from DrugBank API (DB14042)
- **Local package insert review**: Obtain Singapore-jurisdiction-approved prescribing information once registered, or reference the most current US/EU label in the interim
- **Safety monitoring plan**: Define a monitoring protocol for RCVS risk signal in aura-prominent patients, given the brainstem aura context and the isolated RCVS case report
- **Patient selection criteria**: Define inclusion/exclusion criteria for any compassionate use or study protocol, particularly regarding cardiovascular risk factors
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

