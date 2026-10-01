---
layout: default
title: Polymyxin B
parent: Medium Evidence (L3-L4)
nav_order: 797
evidence_level: L3
indication_count: 10
---

# Polymyxin B
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Polymyxin B: From Anti-infective Use to Bronchitis

## One-Sentence Summary

Polymyxin B is a polypeptide antibiotic active against Gram-negative bacteria. In Singapore it is registered only in combination products for ear, eye, skin and vaginal use.
The TxGNN model predicts it may be effective for **bronchitis**, but **no clinical trials** are registered for this indication. Only a few of the **14 publications** are directly relevant, and they are mostly small, older studies or safety reports.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration data (the registered products are all anti-infective combinations) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database. Polymyxin B is a bactericidal lipopeptide that binds lipid A in the outer membrane of Gram-negative bacteria. It is a last-line agent against multidrug-resistant organisms such as *Pseudomonas aeruginosa* and *Acinetobacter baumannii*.

The plausible link to bronchitis is the treatment of Gram-negative tracheobronchitis, for example with aerosolised polymyxin B. Small cohort and case-series reports use it this way in multidrug-resistant respiratory infection. This would be an extension of an existing antibacterial use rather than a new mechanism.

Much of the bronchitis-related literature is not therapeutic. It describes polymyxin B as a bronchial provocation agent in asthma and chronic bronchitis, and as a tool for building eosinophilic bronchitis animal models. These papers point to a safety concern, not support for efficacy. Bronchitis is also usually viral or non-infectious, which limits where an antibiotic could help.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bronchitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23124906](https://pubmed.ncbi.nlm.nih.gov/23124906/) | 2013 | Review/Meta-analysis | Infection | Compared polymyxin B with other antimicrobials for ventilator-associated pneumonia and tracheobronchitis caused by *P. aeruginosa* or *A. baumannii* |
| [17350201](https://pubmed.ncbi.nlm.nih.gov/17350201/) | 2007 | Cohort | Diagn Microbiol Infect Dis | 19 patients given inhaled polymyxin B for multidrug-resistant Gram-negative respiratory infection (14 pneumonia, the rest tracheobronchitis), mostly as salvage therapy |
| [4373513](https://pubmed.ncbi.nlm.nih.gov/4373513/) | 1974 | Case series | J Kans Med Soc | *Pseudomonas* tracheobronchitis treated with systemic gentamicin plus polymyxin B aerosol |
| [4319158](https://pubmed.ncbi.nlm.nih.gov/4319158/) | 1970 | Experimental/Observational | Chest | Endobronchial polymyxin B in chronic bronchitis (title only, no abstract) |
| [231152](https://pubmed.ncbi.nlm.nih.gov/231152/) | 1979 | Challenge study (safety signal) | Lung | Bronchial reactivity to inhaled polymyxin B in asthma and chronic obstructive bronchitis |
| [2984629](https://pubmed.ncbi.nlm.nih.gov/2984629/) | 1985 | Challenge study (safety signal) | Orv Hetil | Polymyxin B-induced non-specific bronchial provocation in asthma and chronic bronchitis |
| [4322737](https://pubmed.ncbi.nlm.nih.gov/4322737/) | 1971 | Case report/Commentary (safety signal) | Ann Intern Med | Warning about the danger of polymyxin B inhalation |
| [7402949](https://pubmed.ncbi.nlm.nih.gov/7402949/) | 1980 | Challenge study | Pneumonol Pol | Exercise-induced bronchospasm compared with histamine and polymyxin B provocation tests |
| [8054833](https://pubmed.ncbi.nlm.nih.gov/8054833/) | 1994 | Preclinical (not relevant) | Clin Auton Res | Intranasal polymyxin B used to induce a guinea-pig eosinophilic bronchitis model |
| [28441858](https://pubmed.ncbi.nlm.nih.gov/28441858/) | 2017 | Preclinical (not relevant) | Zhonghua Yi Xue Za Zhi | Polymyxin B used to create an eosinophilic bronchitis mouse model |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04945P | POLYDEXA EAR DROPS | Solution | Not listed in the registration data |
| SIN04358P | MAXITROL STERILE OPHTHALMIC SUSPENSION | Solution | Not listed in the registration data |
| SIN04413P | POLYBAMYCIN OINT. | Ointment | Not listed in the registration data |
| SIN07745P | POLYGYNAX VAGINAL CAPSULE | Capsule | Not listed in the registration data |

None of the registered products is an inhaled or systemic respiratory formulation. Any bronchitis use would therefore need a different dosage form or route.

---

## Safety Considerations

- **Inhalation risk (from the literature, not from the registration data)**: Several PMIDs (231152, 2984629, 4322737) report that inhaled polymyxin B causes basophil degranulation, histamine release and bronchoconstriction. The effect is seen in most atopic asthmatics and also in chronic bronchitis. This is the main concern for any respiratory use.
- **Drug interactions**: No interaction records were found.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score (99.87%) is not backed by any registered trial. The relevant literature is limited to small, older cohort and case-series reports, and several papers describe bronchoconstriction after inhalation, which is a direct safety problem for bronchitis. The "from" side of this repurposing is also unclear, because the Singapore registrations list no approved indications.

For context, two other predictions for this drug have stronger evidence:
- **Conjunctivitis (L1)**: Phase 3/4 trials and several RCTs of polymyxin B/trimethoprim, which is essentially an established topical use.
- **Respiratory tract infectious disease (L2)**: Phase 2/3 and PK/PD studies in multidrug-resistant ventilator-associated pneumonia.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (blocking for safety screening)
- Mechanism of action data from DrugBank
- A prospective trial in bacterial tracheobronchitis, restricted to confirmed Gram-negative infection and excluding patients with asthma or COPD
- A decision on the dosage form and route, since none of the registered products is suitable
- A safety plan covering bronchospasm monitoring and nephrotoxicity and neurotoxicity if used systemically
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

