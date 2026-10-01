---
layout: default
title: Clavulanic Acid
parent: Medium Evidence (L3-L4)
nav_order: 259
evidence_level: L4
indication_count: 10
---

# Clavulanic Acid
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

# Clavulanic Acid: From Bacterial Infections (Beta-Lactamase Inhibitor Combination) to Ureaplasma Urethritis

## One-Sentence Summary

Clavulanic acid is a beta-lactamase inhibitor, used together with amoxicillin to treat bacterial infections.
The TxGNN model predicts it may be effective for **Ureaplasma urethritis**, but there are **0 registered clinical trials** and **4 publications**, none of which reports clavulanate activity against Ureaplasma.
The prediction is mechanistically implausible and is most likely a graph-proximity artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections, as a beta-lactamase inhibitor partner for amoxicillin (general pharmacology; label indication text is not available in the Singapore record) |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Clavulanic acid inhibits bacterial beta-lactamase enzymes, which protects amoxicillin from degradation. On its own it adds little antibacterial activity. It widens amoxicillin's spectrum to beta-lactamase-producing organisms.

The prediction does not hold up mechanistically. *Ureaplasma* has no cell wall, so beta-lactam antibiotics are intrinsically inactive against it, and a beta-lactamase inhibitor cannot fix that. The four retrieved papers concern urethritis or prostatitis in general and never report clavulanate efficacy against *Ureaplasma*. The very high TxGNN score most likely reflects the drug's proximity to other urethritis terms in the knowledge graph, not a real therapeutic signal.

For context, another urethritis prediction in the same output, **gonococcal urethritis** (rank 2, same TxGNN score, L3), has a real rationale. Clavulanate restores amoxicillin activity against penicillinase-producing *Neisseria gonorrhoeae*, and 1980s single-dose amoxicillin/clavulanate studies exist, including one from Singapore (PMID 3898395). That use is historical and has been superseded by cephalosporin-based regimens, so it is not a new repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34366085](https://pubmed.ncbi.nlm.nih.gov/34366085/) | 2021 | Case report/series | Infectious Diseases Now | First reported association of *Pasteurella bettyae* with urethritis and balanitis in men who have sex with men; no clavulanate efficacy data |
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Review | Rev Esp Quimioter | Discusses the best empirical treatment of urethritis in a Madrid city-centre population; no Ureaplasma-specific clavulanate data |
| [19544099](https://pubmed.ncbi.nlm.nih.gov/19544099/) | 2009 | Retrospective review | Rev Esp Quimioter | 3-year review of the prevalence and trends of microorganisms causing male urethritis in Madrid |
| [9669200](https://pubmed.ncbi.nlm.nih.gov/9669200/) | 1998 | Observational | Int J Androl | Examines the possible role of anaerobic bacteria in chronic prostatitis in 50 patients; not about clavulanate treatment of Ureaplasma |

## Singapore Market Information

12 registrations are recorded. Five main ones are listed below (approved indication text is not available in the record).

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN08956P | AUGMENTIN TABLET 1 g | Film-coated tablet |
| SIN16749P | CLAMOX FILM-COATED TABLETS 1G | Film-coated tablet |
| SIN11027P | ENHANCIN TABLETS 625 mg | Film-coated tablet |
| SIN15043P | SALACLAV POWDER FOR SOLUTION FOR INJECTION 1.2G/VIAL | Powder for solution for injection |
| SIN11219P | AMOCLA TABLETS 625 mg | Film-coated tablet |

Available routes are oral (film-coated tablets), injectable (powder for solution) and other (powder for suspension).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
*Ureaplasma* lacks a cell wall, so beta-lactams and their inhibitors are not expected to work against it. There are no clinical trials, and the literature contains no clavulanate-specific evidence. The high TxGNN score alone does not justify progressing this candidate.

**To proceed, the following is needed:**
- Direct in vitro or clinical evidence of clavulanate-containing regimens against *Ureaplasma* (none expected given the mechanism)
- Retrieval of the Singapore package insert (approved indications, warnings, contraindications), which is currently missing and blocks safety screening
- Detailed mechanism of action data from DrugBank
- If urethritis remains of interest, redirect review to the gonococcal urethritis prediction, and assess whether it adds anything beyond current guideline-preferred therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

