---
layout: default
title: Tyrothricin
parent: Low Evidence (L5)
nav_order: 1028
evidence_level: L5
indication_count: 10
---

# Tyrothricin
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

# Tyrothricin: From a Topical Antibacterial to Insomnia (Top Prediction), with Gastroenteritis as the Only Evidence-Backed Lead

## One-Sentence Summary

Tyrothricin is a topical antibacterial peptide mixture (gramicidin + tyrocidine), marketed in Singapore as a throat lozenge.
The TxGNN model's top prediction is **insomnia** (score 91.5%), but it has **0 clinical trials and 0 publications** behind it and is most likely a knowledge-graph artifact.
The only predicted indication with any supporting literature is **gastroenteritis** (rank 4), with **6 historical reports from 1946-1954** and no modern controlled evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration data (marketed as a throat lozenge) |
| Predicted New Indication | Insomnia (rank 1); gastroenteritis (rank 4) is the only one with literature |
| TxGNN Prediction Score | 91.5% (insomnia); 77.5% (gastroenteritis) |
| Evidence Level | L5 (insomnia); L3 (gastroenteritis) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Tyrothricin is a mixture of gramicidin and tyrocidine, which disrupt bacterial cell membranes. It is used locally and acts mainly against Gram-positive organisms.

**Insomnia (rank 1):** There is no plausible mechanistic link. The drug has no known central nervous system or sleep-related target, so the high score is likely a graph-proximity artifact.

**Gastroenteritis / enterocolitis (ranks 4 and 2):** These are the only predictions with a plausible rationale. Local antibacterial action in the gut could matter in infectious diarrhoea. However:
- Dysentery is mainly caused by Gram-negative organisms (Shigella), so the mechanistic fit is imperfect.
- Most historical reports concern gramicidin, one component, rather than the full tyrothricin mixture.
- Systemic exposure carries a hemolysis risk, which limits non-topical use.

**Other predictions (ranks 3 and 5-10):** The neuromuscular and congenital myasthenic syndromes, osteoarthritis, irritable bowel syndrome and small intestine disease have no credible or only speculative mechanisms, and no evidence. Gramicidin forms cation channels in membranes, which superficially suggests an ion-channel link to neuromuscular disease. This is not a validated rationale, and its non-selective membrane toxicity argues against use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was found for insomnia. The table below lists the literature found for **gastroenteritis**, the only predicted indication with publications. No abstracts were available, so the findings are summarised from the titles.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20248574](https://pubmed.ncbi.nlm.nih.gov/20248574/) | 1946 | Clinical study (uncontrolled, preliminary) | Proc Annu Meet Cent Soc Clin Res | Oral tyrothricin in chronic ulcerative colitis, with clinical and bacteriologic evaluation |
| [14787677](https://pubmed.ncbi.nlm.nih.gov/14787677/) | 1950 | Clinical report (historical) | Sovetskaia meditsina | Gramicidin therapy of acute dysentery |
| [14876589](https://pubmed.ncbi.nlm.nih.gov/14876589/) | 1951 | Clinical report (combination therapy) | Sovetskaia meditsina | Dysentery treated with gramicidin and sulfidin |
| [14359103](https://pubmed.ncbi.nlm.nih.gov/14359103/) | 1954 | Clinical report (pediatric) | Suvremenna meditsina | Gramicidin C in complex therapy of acute dysentery in children |
| [13170681](https://pubmed.ncbi.nlm.nih.gov/13170681/) | 1954 | Clinical report (chronic dysentery) | Zh Mikrobiol Epidemiol Immunobiol | Results of gramicidin treatment of chronic bacillary dysentery |
| [13187005](https://pubmed.ncbi.nlm.nih.gov/13187005/) | 1954 | Clinical report (combination therapy) | Sovetskaia meditsina | Chronic dysentery treated by Bilibin's method with gramicidin and nicotinic acid |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN04392P | DORITHRICIN THROAT LOZENGES (Medice Arzneimittel Pütter GmbH & Co. KG) | Lozenge |

The registration data does not include an approved indication text.

---

## Safety Considerations

- **Systemic toxicity**: The Evidence Pack rationale notes that hemolysis limits non-topical use, so oral or systemic exposure would need re-evaluation.

Please refer to the package insert for full warnings, contraindications and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (insomnia) has no mechanistic rationale and no trials or literature, and is likely a knowledge-graph artifact. The same applies to the neuromuscular, osteoarthritis and IBS predictions.
- Gastroenteritis is the only direction worth a research question. It rests only on six uncontrolled reports from 1946-1954, mostly on gramicidin rather than the full mixture, and carries unresolved oral safety concerns.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications, approved indication), which is a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- A safety and feasibility review of oral or enteric exposure (hemolysis and absorption) before any trial design for gastroenteritis
- A route compatibility assessment, since the only registered form is a lozenge

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

