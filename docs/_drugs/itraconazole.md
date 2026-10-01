---
layout: default
title: Itraconazole
parent: Medium Evidence (L3-L4)
nav_order: 554
evidence_level: L4
indication_count: 10
---

# Itraconazole
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

# Itraconazole: From Fungal Infections to Pneumocystosis

## One-Sentence Summary

Itraconazole is an azole antifungal used for fungal infections, and it is marketed in Singapore under 5 registrations. The TxGNN model predicts it may be effective for **pneumocystosis** (score 99.3%), but there are **0 registered clinical trials** and only **20 loosely related publications**, none of which show itraconazole treating this disease. The prediction is supported by the model alone and the mechanism argues against it, so the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (the HSA records provide no indication text) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank. Itraconazole is known to inhibit fungal CYP51 (lanosterol 14-alpha-demethylase), which blocks ergosterol synthesis. This is why it works against ergosterol-dependent fungi.

That mechanism fits this prediction poorly. *Pneumocystis jirovecii* has little or no ergosterol in its membranes. A 2003 study that cloned the Pneumocystis Erg11 enzyme also notes that the organism is intrinsically resistant to azole antifungals. The high TxGNN score most likely reflects a shared antifungal or opportunistic-infection neighbourhood in the knowledge graph. It probably does not reflect a real treatment effect. Most retrieved papers mention itraconazole only in co-infection or general prophylaxis settings, alongside *Pneumocystis*.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | Double-blind, placebo-controlled phase III trial of itraconazole prophylaxis against deep fungal infections in HIV patients. It targets fungal infections in general, not pneumocystosis, and the provided abstract reports no results. |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | Primary and secondary prophylaxis of opportunistic infections in HIV. Background context only. |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Therapy and prophylaxis of systemic protozoan infections, including *Pneumocystis carinii*. Background on established treatment. |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | Prophylaxis and treatment of infection in bone marrow transplant recipients. General context. |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | Infection after lung transplantation. General context. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Penetration of anti-infective agents, including antifungals, into pulmonary epithelial lining fluid. Relevant to lung drug exposure. |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | Mechanism study | Am J Respir Cell Mol Biol | Cloned the Pneumocystis lanosterol 14-alpha-demethylase (Erg11), the azole target. The organism is described as intrinsically resistant to azole antifungals. |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report | Frontiers in Immunology | *T. marneffei* and *P. jirovecii* coinfection in a child with a STAT1 mutation. Itraconazole is not shown to treat pneumocystosis. |
| [8967681](https://pubmed.ncbi.nlm.nih.gov/8967681/) | 1996 | Case report | Annals of Internal Medicine | Uveitis associated with rifabutin prophylaxis plus itraconazole therapy. A safety signal, not an efficacy finding. |
| [2233233](https://pubmed.ncbi.nlm.nih.gov/2233233/) | 1990 | Review | Medicine | Disseminated histoplasmosis in AIDS. Background on a different opportunistic infection. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16379P | JAMP Itraconazole Oral Solution 10 mg/ml | Solution |
| SIN12459P | Unitrac Capsule 100 mg | Capsule |
| SIN08206P | Sporanox Capsule 100 mg | Capsule |
| SIN09823P | Sporanox Oral Solution 10 mg/ml | Solution |
| SIN11355P | Canditral Capsule 100 mg | Capsule |

Oral capsule and oral solution formulations are both available. The HSA records provided contain no approved-indication text.

## Safety Considerations

Please refer to the package insert for safety information.

One literature signal: a 1996 case report describes uveitis in a patient receiving rifabutin prophylaxis together with itraconazole (PMID 8967681).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no registered trials and no published evidence of itraconazole treating pneumocystosis, so it rests on the model score alone. *Pneumocystis* lacks the ergosterol target and is described as intrinsically azole-resistant, so the mechanistic link is weak. Other predictions for this drug have more support, notably cryptococcal meningitis (L2, with itraconazole-specific trials and comparative studies) and penicilliosis (L3, with an itraconazole pharmacokinetic study in talaromycosis).

**To proceed, the following is needed:**
- Any direct evidence that itraconazole treats or prevents pneumocystosis, or a mechanistic explanation that overcomes *Pneumocystis* azole resistance.
- Detailed mechanism of action data from DrugBank.
- The HSA package insert, covering warnings, contraindications and approved indications, to allow safety screening.
- Drug interaction data, since the DDI query returned no results.
- A decision on whether to redirect effort to the better-supported predictions (cryptococcal meningitis, penicilliosis).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

