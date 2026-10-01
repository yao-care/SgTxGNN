---
layout: default
title: Chloramphenicol
parent: Low Evidence (L5)
nav_order: 234
evidence_level: L5
indication_count: 10
---

# Chloramphenicol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Chloramphenicol: Conjunctivitis as a Predicted Indication (Largely Confirmation of Existing Use)

## One-Sentence Summary

Chloramphenicol is a broad-spectrum antibiotic already marketed in Singapore as ear drops and eye drops.
The TxGNN model predicts it may be effective for **conjunctivitis**, which is closer to confirming an established topical use than to true repurposing.
Support comes from **0 registered clinical trials** and **18 publications**, including **3 randomised controlled trials**.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L1 (based on published RCTs only; no registered trials) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Chloramphenicol is a bacteriostatic antibiotic that inhibits the bacterial 50S ribosomal peptidyl transferase, which blocks protein synthesis. Bacterial conjunctivitis is a superficial eye infection, so the drug's mechanism fits the disease directly.

Topical ophthalmic chloramphenicol is a long-established use. It is widely prescribed for conjunctivitis in the UK but rarely in the U.S. (PMID 8800624). The prediction therefore mostly confirms an existing use.

Because the registry records list no approved indications, the drug's original indication cannot be stated from this data. Two Singapore products are eye drops or ear drops, consistent with topical use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3300139](https://pubmed.ncbi.nlm.nih.gov/3300139/) | 1987 | RCT | Acta Ophthalmol | Bacterial conjunctivitis in Tanzania: success rate 93% for fusidic acid, 74% for framycetin and 48% for chloramphenicol. In vitro resistance was higher for chloramphenicol. |
| [3554881](https://pubmed.ncbi.nlm.nih.gov/3554881/) | 1987 | RCT | Acta Ophthalmol | Clinical success 84% for fusidic acid vs 81% for chloramphenicol. Trivial side effects such as stinging occurred in 14% vs 5%. |
| [17947266](https://pubmed.ncbi.nlm.nih.gov/17947266/) | 2007 | RCT | Br J Ophthalmol | Equivalency trial of 2.5% povidone-iodine drops vs chloramphenicol for preventing neonatal conjunctivitis in a trachoma-endemic area of Mexico. |
| [6188739](https://pubmed.ncbi.nlm.nih.gov/6188739/) | 1983 | Randomised double-blind trial | J Antimicrob Chemother | 230 patients with presumptive bacterial conjunctivitis. All preparations, including chloramphenicol, were effective with very few adverse effects. |
| [8333258](https://pubmed.ncbi.nlm.nih.gov/8333258/) | 1993 | Comparative clinical study | Acta Ophthalmol | Fusidic acid drops vs chloramphenicol in acute conjunctivitis. No significant difference in response or bacteriological findings. |
| [11952486](https://pubmed.ncbi.nlm.nih.gov/11952486/) | 2002 | Comparative clinical study | Acta Ophthalmol Scand | Fusidic acid vs chloramphenicol drops in neonates with suspected bacterial conjunctivitis. |
| [38511104](https://pubmed.ncbi.nlm.nih.gov/38511104/) | 2024 | Comparative clinical study | Curr Ther Res | Moxifloxacin vs chloramphenicol for bacterial eye infections. Chloramphenicol is used mainly topically because of its known toxicity. |
| [16378567](https://pubmed.ncbi.nlm.nih.gov/16378567/) | 2005 | Systematic review / meta-analysis | Br J Gen Pract | Cochrane update on topical antibiotics for acute bacterial conjunctivitis, testing whether earlier findings apply in primary care. |
| [32959365](https://pubmed.ncbi.nlm.nih.gov/32959365/) | 2020 | Systematic review | Cochrane Database Syst Rev | Interventions for preventing ophthalmia neonatorum (neonatal conjunctivitis). |
| [8800624](https://pubmed.ncbi.nlm.nih.gov/8800624/) | 1996 | Review | Drug Saf | Whether topical ocular chloramphenicol is linked to aplastic anaemia remains controversial. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00230P | CHLORAMPHENICOL EAR DROPS 5% w/v | Solution | Not listed in registry record |
| SIN04574P | CHLORAMPHENICOL EAR DROPS 5% w/v | Solution | Not listed in registry record |
| SIN00231P | XEPANICOL EYE DROPS 0.5% | Solution | Not listed in registry record |

## Safety Considerations

- **Haematological risk (from literature)**: A possible link between topical ocular chloramphenicol and aplastic anaemia has been debated for decades (PMID 8800624) and needs safety review.
- **Local tolerability (from literature)**: Stinging and local discomfort were reported more often with chloramphenicol than with fusidic acid (14% vs 5%, PMID 3554881).
- **Drug interactions**: No interactions were found in the queried database.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several published RCTs and comparative studies support chloramphenicol drops for bacterial conjunctivitis, and the mechanism fits directly. However, there are no registered trials, newer comparators such as moxifloxacin exist, and the aplastic anaemia concern remains unresolved.

The other nine TxGNN predictions (diffuse scleroderma, chronic rhinosinusitis and others) have no credible mechanistic or clinical support. The literature hits for scleroderma and rhinosinusitis are probably artefacts of chloramphenicol's use as a laboratory reporter or culture reagent. These remain on **Hold**.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, which are currently missing and are a blocking gap for safety screening
- Confirmation of the approved indications for the eye-drop product (SIN00231P)
- A formal safety review of the aplastic anaemia signal for topical ocular use
- Local antibiotic-resistance surveillance data to guide use
- Detailed mechanism-of-action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

