---
layout: default
title: Isoniazid
parent: Medium Evidence (L3-L4)
nav_order: 555
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Isoniazid: predicted new indication Conjunctivitis (evidence level L4). Approved use: Pulmonary tuberculosis"
monitor_inn: "Isoniazid"
predicted_indications: ["conjunctivitis", "rheumatoid arthritis", "shigellosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "leprosy", "brachydactyly-syndactyly syndrome", "vestibular neuronitis", "motor nerve neuritis", "infectious otitis media", "brachial plexus neuritis"]
---

# Isoniazid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Isoniazid: From Pulmonary Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is an antituberculosis drug, originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **conjunctivitis**, but there are currently **0 registered clinical trials** and **12 publications**, none of which show a direct therapeutic effect. The prediction rests on the model alone and the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, isoniazid is a first-line antimycobacterial agent. Its efficacy in tuberculosis is well established, and it is generally understood to act against mycobacteria.

No direct mechanism links isoniazid to conjunctivitis. The related literature mainly covers:
- Ocular adverse effects of systemic drugs.
- Tuberculosis-related (phlyctenular) keratoconjunctivitis, a hypersensitivity reaction to mycobacterial antigens.
- A 1965 population study of isoniazid prophylaxis among Alaskan Eskimos.

The signal is therefore most likely driven by isoniazid's activity against tuberculosis-related eye disease, not by a general anti-conjunctivitis effect. Several retrieved papers (BCG-related arthritis, toxic epidermal necrolysis, Munchausen syndrome by proxy) are not relevant to efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Cohort | Am Rev Respir Dis | Isoniazid prophylaxis and phlyctenular keratoconjunctivitis among Eskimos in southwestern Alaska (no abstract available) |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report | Medicine | Pediatric phlyctenular keratoconjunctivitis associated with primary sinonasal tuberculosis |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Arch Ophthalmol | Primary tuberculosis of the conjunctiva |
| [10084171](https://pubmed.ncbi.nlm.nih.gov/10084171/) | 1999 | Case report | Rev Rhum (Engl Ed) | Isoniazid used for refractory arthropathy after intravesical BCG therapy |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optom Clin | Ocular side effects of systemic drugs, including conjunctivitis |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case series | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, many in children with primary tuberculosis |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Not classified | Ann Ocul | Local isoniazid use in ocular tuberculosis (no abstract available) |
| [14195962](https://pubmed.ncbi.nlm.nih.gov/14195962/) | 1964 | Review | South Med J | Toxic epidermal necrolysis (not relevant to efficacy) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00373C | PDP-ISONIAZID TABLET 300 mg | Tablet | Not available |
| SIN06651P | PDP-ISONIAZID TABLET 300 mg | Tablet | Not available |
| SIN01302P | ISONIAZID TABLET 100 mg | Tablet | Not available |

## Safety Considerations

- **Disease-related cautions (from knowledge-graph contraindication data, not label text)**: liver failure and acute liver failure, hepatitis, liver disease, gallbladder disease, porphyria and other porphyrin metabolism disorders, peripheral neuropathy and other peripheral nervous system disease, diabetes mellitus, diabetic ketoacidosis, gout, substance abuse/dependence, and slow acetylator status.
- **Drug Interactions**: 100 interactions were identified in total. The main ones listed are:
  - Moderate: metformin, pioglitazone, alogliptin, albiglutide, canagliflozin, dapagliflozin, acarbose, chlorpropamide, metronidazole, budesonide, calcitriol, calcifediol, cholecalciferol, alosetron, picosulfuric acid.
  - Minor: hydrocortisone, triamcinolone, dexamethasone, betamethasone.

Please also refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist, and the literature shows only an indirect link through tuberculosis-related eye disease, not a general effect on conjunctivitis. The high TxGNN score is not backed by clinical evidence, and isoniazid has notable hepatic and neurological safety concerns.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator (HSA), which are currently missing and block safety screening.
- Detailed mechanism of action data.
- Evidence of efficacy in a defined population, such as tuberculous phlyctenular keratoconjunctivitis, rather than conjunctivitis in general.
- Clarification of the route of administration, since only oral tablets are registered in Singapore.

---

### Note on other predicted indications

None of the other nine predictions (ranks 2–10) is supported by direct efficacy evidence. They are listed here in brief for context.

- **Rheumatoid arthritis**: the literature reflects tuberculosis prophylaxis in patients on biologics, plus adverse events. The score likely reflects co-prescription.
- **Leprosy**: biologically plausible, since *M. leprae* is a mycobacterium. However, its *katG* gene is a pseudogene, so isoniazid is unlikely to be effective. This is the only other indication flagged as a research question.
- **Motor nerve neuritis**: this reflects isoniazid-induced neuropathy, an adverse effect rather than a therapeutic signal.
- **Shigellosis, colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, vestibular neuronitis, infectious otitis media, brachial plexus neuritis**: model prediction only, with no supporting literature and no plausible mechanism.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

