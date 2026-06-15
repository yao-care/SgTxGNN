---
layout: default
title: Calfactant
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 10
---

# Calfactant
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

# Calfactant: From Neonatal Respiratory Distress Syndrome to Adult Acute Respiratory Distress Syndrome

## One-Sentence Summary

Calfactant (Infasurf) is a natural calf lung surfactant, originally proven effective in neonatal and pediatric respiratory distress syndrome (RDS/ALI), where exogenous surfactant replacement directly addresses alveolar surface tension dysfunction.
The TxGNN model predicts it may be effective for **Adult Acute Respiratory Distress Syndrome (ARDS)**,
with **1 Phase 3 clinical trial** and **7 publications** currently examined — however, the pivotal Phase 3 RCT was terminated early due to futility, making this a cautionary evidence package rather than a supportive one.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neonatal / Pediatric Respiratory Distress Syndrome (RDS / ALI) |
| Predicted New Indication | Adult Acute Respiratory Distress Syndrome (ARDS) |
| TxGNN Prediction Score | 95.78% |
| Evidence Level | L1 (Phase 3 RCT exists, but terminated for futility) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, Calfactant is a natural bovine lung surfactant extract containing phospholipids (predominantly dipalmitoylphosphatidylcholine) and surfactant-associated proteins SP-B and SP-C. Its core mechanism is the restoration of alveolar surface tension at the air-liquid interface, which is the same pathological defect that defines neonatal RDS. The extension to ARDS is therefore mechanistically coherent at first glance.

The rational link between neonatal RDS and adult ARDS rests on a shared pathophysiological feature: surfactant dysfunction. In ARDS, plasma proteins leaking across the damaged alveolar-capillary membrane competitively inhibit endogenous surfactant activity, collapsing alveoli and worsening hypoxemia. Replacing this dysfunctional surfactant pool with exogenous Calfactant — which is particularly rich in SP-B, the protein associated with superior surface tension reduction — was hypothesised to partially restore alveolar stability and improve gas exchange, directly extending the mechanism proven in neonates.

However, the translation fails at scale. Adult ARDS involves a far greater degree of inflammatory injury, protein flooding, and surfactant inactivation than neonatal RDS. The pivotal Phase 3 RCT (NCT00682500, n = 332) was stopped early by the Data Safety Monitoring Board for futility: Calfactant did not improve mortality or the course of respiratory failure in adults. Positive results from the paediatric ARDS RCT (JAMA 2005) cannot be directly extrapolated to adults, as was confirmed by the negative adult trial. The prediction is mechanistically plausible but clinically falsified for the adult population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00682500](https://clinicaltrials.gov/study/NCT00682500) | Phase 3 | Terminated | 332 | Multicentre RCT of intratracheal Calfactant within 48 h of mechanical ventilation in adults and children with Direct ARDS/ALI. Stopped early — Calfactant did not reduce mortality or shorten the course of respiratory failure in adults. This is the decisive negative evidence against adult repurposing. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [25855884](https://pubmed.ncbi.nlm.nih.gov/25855884/) | 2015 | RCT Primary Report | Chest | Adult Calfactant in ARDS Trial: exogenous surfactant (including SP-B–containing preparations) failed to improve primary endpoints in adults with ALI/ARDS; terminates the hypothesis of adult benefit. |
| [15671432](https://pubmed.ncbi.nlm.nih.gov/15671432/) | 2005 | RCT | JAMA | Paediatric ALI RCT (n = 153): intratracheal Calfactant significantly improved oxygenation and reduced mortality vs. placebo in children — the key positive paediatric signal that motivated the adult trial. |
| [23925143](https://pubmed.ncbi.nlm.nih.gov/23925143/) | 2013 | Retrospective Cohort Analysis | Pediatric Critical Care Medicine | Post-hoc analysis of the paediatric Calfactant ARDS trial: fluid overload was independently associated with worse outcomes, underscoring that surfactant benefit in children occurs in the context of conservative fluid management. |
| [33493441](https://pubmed.ncbi.nlm.nih.gov/33493441/) | 2021 | Case Report | Chest | Single-patient experience: exogenous surfactant administered to a COVID-19 ARDS patient with atypical physiology resembling neonatal RDS showed temporary oxygenation improvement; highlights a potential subgroup hypothesis but cannot support efficacy conclusions. |
| [21048239](https://pubmed.ncbi.nlm.nih.gov/21048239/) | 2010 | Review | Indian Pediatrics | Comprehensive review of paediatric ARDS management; contextualises surfactant therapy within the broader paediatric ICU evidence base and supportive care strategies. |
| [17198050](https://pubmed.ncbi.nlm.nih.gov/17198050/) | 2007 | Review | Current Opinion in Critical Care | Review of paediatric ventilation strategies and timing; surfactant use discussed as one component of lung-protective care in children, highlighting differences from adult practice. |
| [20335386](https://pubmed.ncbi.nlm.nih.gov/20335386/) | 2010 | Basic Science / Methodology | American Journal of Respiratory and Critical Care Medicine | Commentary on surfactant composition and biophysical properties; argues that SP-B content and phospholipid profile are critical determinants of clinical efficacy, providing mechanistic context for why formulation differences matter in ARDS trials. |

---

## Singapore Market Information

Calfactant is currently **not registered** in Singapore. There are no active or historical product licences on record.

> If regulatory approval is pursued in the future, a full new drug application (NDA) process with the Health Sciences Authority (HSA) would be required.

---

## Safety Considerations

Detailed safety data (package insert warnings, contraindications, drug interactions) were not available in this Evidence Pack.

> Please refer to the Calfactant (Infasurf) package insert for complete safety information, including handling precautions for intratracheal administration, monitoring requirements during mechanical ventilation, and contraindications in specific patient populations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's high confidence score (95.78%) reflects a mechanistically coherent hypothesis, but the hypothesis has already been tested and **prospectively falsified** in adults: the Phase 3 RCT (NCT00682500) was terminated early for futility, and the 2015 Chest publication confirms that Calfactant does not improve adult ARDS outcomes. The positive paediatric signal (JAMA 2005) is real but does not generalise to adults. Proceeding with a standard adult ARDS repurposing programme would repeat a known failure.

**To reconsider, the following would be needed:**

- **Subgroup hypothesis generation**: Identification of a biologically defined adult subpopulation (e.g., COVID-19-associated ARDS with near-normal compliance, direct ARDS within 6 h of onset, or surfactant protein B–deficient patients) where the mechanism may still apply and where prior trials were underpowered.
- **Mechanistic data (MOA)**: Formal retrieval of Calfactant's complete pharmacological profile from DrugBank to confirm whether any secondary mechanisms (beyond surface tension reduction) have been characterised that could support non-pulmonary or non-surfactant-based activity.
- **Biomarker-stratified trial design**: Any future clinical investigation should incorporate surfactant dysfunction biomarkers (e.g., bronchoalveolar lavage surfactant protein levels, minimum surface tension measurements) as eligibility criteria to enrich the population most likely to benefit.
- **Singapore regulatory pathway assessment**: Given zero existing registrations, a full HSA NDA strategy including GMP-certified supply chain, local clinical data requirements, and YMYL-compliant patient communication materials would be prerequisites before any clinical programme.

> **Research note:** The rank 3 prediction (Pulmonary Edema, score 76.17%) may warrant a separate, exploratory research question — specifically in permeability-type pulmonary oedema overlapping with early ARDS — but requires a distinct and clearly defined protocol before any investment decision.

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before any clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

