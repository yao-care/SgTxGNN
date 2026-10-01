---
layout: default
title: Isoniazid
parent: Medium Evidence (L3-L4)
nav_order: 551
evidence_level: L4
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is a long-established anti-tuberculosis drug, and three oral tablet products are registered in Singapore.
The TxGNN model predicts it may be effective for **conjunctivitis**, but the support is weak: **1 clinical trial** (not about conjunctivitis) and **20 publications**, mostly old case reports of tuberculosis-related eye disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (general drug knowledge; the Singapore records give no indication text) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Isoniazid is an anti-tubercular agent that acts against mycobacteria by inhibiting mycolic acid synthesis. It is effective against tuberculosis, and mechanistically it might be relevant to eye infections caused by mycobacteria.

The link to conjunctivitis is indirect. The literature describes **tuberculous** conjunctivitis, phlyctenular keratoconjunctivitis linked to tuberculosis, and conjunctivitis as part of a BCG-related reactive arthritis. These are infection-specific settings. None shows isoniazid treating conjunctivitis in general, which is mostly viral, bacterial or allergic. The high TxGNN score probably reflects the drug's proximity to mycobacterial disease in the knowledge graph, not a demonstrated treatment effect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Compared systemic drug reactions under the 3HP and 1HP regimens (isoniazid/rifapentine-based) for latent TB infection. Conjunctivitis is not an outcome or indication, so relevance is low. |

---

## Literature Evidence

No randomised controlled trials were found. Ten of the 20 retrieved publications are listed below. Papers not classified in the Evidence Pack are labelled "Not classified".

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optometry Clinics | Systemic drugs can cause ocular adverse effects, including conjunctivitis. This is a harm signal, not a treatment signal. |
| [5005929](https://pubmed.ncbi.nlm.nih.gov/5005929/) | 1971 | Review | Annals of Ophthalmology | Review titled "Rifampicin"; no abstract available. |
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Not classified | American Review of Respiratory Disease | Isoniazid prophylaxis for phlyctenular keratoconjunctivitis among Eskimos in Alaska; no abstract available. |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Not classified | Annales d'Oculistique | Local isoniazid use in ocular tuberculosis; no abstract available. |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case report | Middle East African Journal of Ophthalmology | Tuberculous conjunctivitis in an anophthalmic socket in a patient with prior miliary TB. |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report | Medicine | Phlyctenular keratoconjunctivitis linked to primary sinonasal TB in a child. |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Not classified | Cornea | Conjunctival tuberculosis presenting as a chronic red eye. |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Archives of Ophthalmology | Primary tuberculosis of the conjunctiva; no abstract available. |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Not classified | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, 13 of them in children with primary TB. |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Not classified | Canadian Journal of Ophthalmology | Conjunctival phlyctenulosis as a presenting sign of impending clinical tuberculosis. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN00373C | PDP-ISONIAZID TABLET 300 mg | Tablet (oral) | Pharmascience Inc. |
| SIN06651P | PDP-ISONIAZID TABLET 300 mg | Tablet (oral) | Pharmascience Inc. |
| SIN01302P | ISONIAZID TABLET 100 mg | Tablet (oral) | Atlantic Laboratories Corpn Ltd |

The records do not include approved indication text. All three products are oral tablets, and no ophthalmic or topical formulation is registered.

---

## Safety Considerations

Please refer to the package insert for safety information.

The Evidence Pack has no drug-interaction records for isoniazid. The retrieved literature, however, repeatedly reports adverse effects relevant to any new use: hepatotoxicity (particularly with methotrexate or other hepatotoxic drugs), peripheral neuropathy in slow acetylators, rhabdomyolysis and mania (single case reports).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The conjunctivitis prediction rests on a high model score and on case reports of tuberculosis-related eye disease, where isoniazid treats the underlying infection. No study shows benefit in conjunctivitis generally. The only registered trial is about latent TB, and the registered products are oral tablets only.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism-of-action data from DrugBank
- A defined target population (for example, confirmed tuberculous or phlyctenular conjunctivitis) and a route/formulation assessment, since no ocular formulation exists
- Modern controlled evidence, or at least a systematic review, of isoniazid for ocular disease

A side note from the wider prediction list: **leprosy** (rank 5) has a more biologically plausible link, with 1950s reports of isoniazid use. However, the *katG* gene of *M. leprae* is a pseudogene, which argues against activity, and isoniazid is not part of standard leprosy therapy. It is best treated as a research question, not a candidate for development.

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

