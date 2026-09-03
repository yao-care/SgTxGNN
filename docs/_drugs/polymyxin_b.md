---
layout: default
title: Polymyxin B
parent: 僅模型預測 (L5)
nav_order: 797
evidence_level: L5
indication_count: 10
---

# Polymyxin B
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

# Polymyxin B: From Gram-Negative Bacterial Infections to Bronchitis

## One-Sentence Summary

Polymyxin B is a polymyxin-class antibiotic internationally established for treating serious infections caused by susceptible gram-negative bacteria; it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Bronchitis** (specifically bacterial tracheobronchitis caused by multidrug-resistant gram-negative organisms),
with **0 clinical trials** and **14 publications** currently supporting this direction — evidence that is largely observational/case-series in nature and includes a notable safety signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; internationally established for treatment of serious gram-negative bacterial infections |
| Predicted New Indication | Bronchitis (bacterial tracheobronchitis) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Polymyxin B is not available in this evidence pack. Based on established pharmacological knowledge, Polymyxin B is a cationic cyclic lipopeptide that binds to lipopolysaccharide (LPS) on the outer membrane of gram-negative bacteria, disrupting membrane integrity and causing bacterial cell death. Its efficacy against gram-negative pathogens (including *Pseudomonas aeruginosa*, *Acinetobacter baumannii*, and carbapenem-resistant Enterobacteriaceae) is well proven in systemic and topical use.

For bronchitis — particularly bacterial tracheobronchitis caused by multidrug-resistant gram-negative bacilli — the same antibacterial mechanism is theoretically applicable, and early literature from the 1970s describes case reports of endobronchial or aerosolized Polymyxin B administration for this purpose. However, a separate and consistent body of literature shows that **inhaled Polymyxin B can trigger bronchoconstriction and histamine release** (a non-specific bronchial provocation effect) in patients with asthma or chronic bronchitis. This represents a genuine safety concern for the inhaled route specifically, which must be weighed against any therapeutic benefit. No randomized controlled trial has yet directly confirmed efficacy in bronchitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23124906](https://pubmed.ncbi.nlm.nih.gov/23124906/) | 2013 | Cohort | Infection | Compared Polymyxin B with other antimicrobials for VAP and tracheobronchitis caused by *P. aeruginosa* or *A. baumannii* |
| [17350201](https://pubmed.ncbi.nlm.nih.gov/17350201/) | 2007 | Cohort | Diagn Microbiol Infect Dis | Inhaled Polymyxin B used as salvage treatment for MDR gram-negative respiratory infections including tracheobronchitis; 19 patients treated |
| [4319158](https://pubmed.ncbi.nlm.nih.gov/4319158/) | 1970 | Case series | Chest | Endobronchial Polymyxin B experimental observations in chronic bronchitis |
| [4373513](https://pubmed.ncbi.nlm.nih.gov/4373513/) | 1974 | Case series | J Kansas Med Soc | Pseudomonas tracheobronchitis treated with systemic gentamicin plus polymyxin B aerosol |
| [231152](https://pubmed.ncbi.nlm.nih.gov/231152/) | 1979 | Challenge study (negative safety signal) | Lung | Inhaled Polymyxin B caused bronchial reactivity in asthma and chronic obstructive bronchitis patients |
| [2984629](https://pubmed.ncbi.nlm.nih.gov/2984629/) | 1985 | Challenge study (negative safety signal) | Orvosi hetilap | Polymyxin B sulfate induced non-specific bronchial provocation in bronchial asthma and chronic bronchitis |
| [4322737](https://pubmed.ncbi.nlm.nih.gov/4322737/) | 1971 | Case report | Ann Intern Med | Reported danger of Polymyxin B inhalation |
| [8054833](https://pubmed.ncbi.nlm.nih.gov/8054833/) | 1994 | Preclinical | Clin Auton Res | Intranasal Polymyxin B used to induce guinea-pig eosinophilic bronchitis model to study cough mechanism |
| [28441858](https://pubmed.ncbi.nlm.nih.gov/28441858/) | 2017 | Preclinical | Zhonghua Yi Xue Za Zhi | Mouse model of eosinophilic bronchitis induced by Polymyxin B nasal drops to study airway hyperresponsiveness |
| [7402949](https://pubmed.ncbi.nlm.nih.gov/7402949/) | 1980 | Challenge study | Pneumonologia polska | Compared exercise-induced bronchospasm with histamine/Polymyxin B provocation test in asthma and chronic obstructive bronchitis |

---

## Singapore Market Information

Polymyxin B is not currently registered in Singapore (0 authorizations on file; market status: Not Marketed). No product-level dosage form or approved indication data are available for the local market.

---

## Safety Considerations

- **Repurposing-specific safety signal**: Multiple independent studies (1979–1994) consistently show that **inhaled/aerosolized Polymyxin B can induce bronchoconstriction and histamine release** in patients with asthma or chronic bronchitis via non-specific bronchial provocation. This is a direct safety concern for any bronchitis-related repurposing via the inhaled route and should be treated as a contraindication signal pending further review, independent of formal labeling.
- Formal package insert warnings, contraindications, and drug-interaction data are not available in this evidence pack (TFDA labeling data collection is flagged as a **Blocking** data gap). Please refer to the official package insert once available for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for bronchitis is Level L3 (cohort/case-series only, no completed RCT), the drug is not currently marketed in Singapore, and literature reveals a recurring negative safety signal (bronchoconstriction/histamine release) specifically associated with the inhaled route being proposed for this indication. Efficacy and safety data are insufficient to proceed even under guardrails at this time.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert warnings and contraindications (DG001, Blocking — required before any S1 safety review can proceed)
- Documented mechanism of action data from DrugBank or equivalent source (DG002)
- Prospective or randomized evidence directly evaluating Polymyxin B efficacy in bacterial bronchitis/tracheobronchitis
- Route-specific risk assessment (inhaled vs. systemic) addressing the observed bronchoconstriction/histamine-release signal in asthma/COPD populations
- Confirmation of Singapore registration pathway, since the drug is currently not marketed locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

