---
layout: default
title: Aztreonam
parent: High Evidence (L1-L2)
nav_order: 132
evidence_level: L2
indication_count: 10
---

# Aztreonam
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Aztreonam: From Gram-Negative Bacterial Infections to Gonococcal Urethritis

**Note on indication selection:** The top-scored prediction (hyperamylasemia, 99.73%) and most other high-scoring predictions have no clinical or literature support and no plausible mechanism. This report therefore focuses on **gonococcal urethritis** (rank 5), the only prediction with real clinical evidence. The others are summarized at the end.

## One-Sentence Summary

Aztreonam is an injectable monobactam antibiotic used against aerobic gram-negative bacterial infections.
The TxGNN model predicts it may be effective for **gonococcal urethritis**, with **1 clinical trial** and **8 publications** supporting this direction.
Much of the evidence is from the 1980s, and the newest work is a small single-arm study.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the HSA data (aztreonam is an antibacterial for aerobic gram-negative infections) |
| Predicted New Indication | Gonococcal urethritis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Aztreonam is known to inhibit penicillin-binding protein 3 (PBP3) in aerobic gram-negative bacteria, which blocks cell wall synthesis.

*Neisseria gonorrhoeae* is a gram-negative organism, and aztreonam has documented in vitro activity against it, including penicillin-resistant strains. This makes the prediction biologically plausible. Several 1980s studies tested single-dose intramuscular aztreonam for gonorrhea. A 2019–2020 single-arm trial revisited it because ceftriaxone-resistant gonorrhea is a growing threat.

Aztreonam is not a current first-line gonorrhea therapy. Its likely niche is cephalosporin-allergic patients or resistant infections.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03867734](https://clinicaltrials.gov/study/NCT03867734) | Phase 2/3 | Completed | 32 | Demonstration study of aztreonam for **pharyngeal** gonorrhea (2019). Same pathogen and drug, but a different anatomical site from urethritis. The small size limits its weight. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Single-arm open-label trial | Antimicrob Agents Chemother | Single-dose IM aztreonam 2 g in men with gonorrhea, motivated by ceftriaxone-resistance concerns. |
| [6438364](https://pubmed.ncbi.nlm.nih.gov/6438364/) | 1984 | Clinical and bacteriological study | Jpn J Antibiot | 30 men with gonorrheal urethritis treated with aztreonam. Included penicillinase-producing (PPNG) strains (15% of isolates). |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Clinical study | Antimicrob Agents Chemother | Aztreonam 1 g IM vs spectinomycin 2 g IM for uncomplicated gonorrhea. No failures in either group, including 26 urethral infections on aztreonam. |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Clinical study | Genitourin Med | Single 1 g IM dose cleared infection at all sites in 61 men and 26 women, except the pharynx of one patient. Effective against penicillin-sensitive and penicillin-resistant strains. |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Epidemiologic and therapeutic study | Hinyokika Kiyo | One-shot aztreonam therapy for gonorrheal infections, plus epidemiology of infections in Japan. |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | In vitro and clinical study | J Infect Dis | Activity of aztreonam against penicillin-resistant gonococci. |
| [6226596](https://pubmed.ncbi.nlm.nih.gov/6226596/) | 1983 | Clinical study | G Ital Dermatol Venereol | Study of aztreonam in acute gonococcal urethritis (no abstract available). |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Laboratory resistance report | J Infect Chemother | Report of cephem- and aztreonam-high-resistant, non-β-lactamase-producing *N. gonorrhoeae*, which is a caution for use. |

Study designs were judged from titles and abstracts only and could not be fully verified.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00556P | AZACTAM FOR INJECTION 1 g/vial | Injection, powder, for solution | Not stated in the record |

Manufacturer: Catalent Anagni S.R.L. Only an injectable form is registered.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The biological rationale is credible, and historical studies plus one recent single-arm trial suggest aztreonam can clear gonorrhea. However, the evidence is not confirmatory. The only registered trial is a small demonstration study at the pharyngeal site, and the urethral data are from the 1980s. Aztreonam also has no current first-line role. The package insert safety review is a blocking data gap, so the candidate cannot advance yet.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (blocking gap)
- Mechanism of action data from DrugBank
- A comparative, stewardship-aware study, most plausibly in cephalosporin-allergic or resistant gonorrhea, with urethral endpoints
- Current resistance data for aztreonam against gonococcal isolates
- Confirmation of the Singapore approved indication text

**Other predictions (all Hold):**
- **No plausible link (L5):** hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, premalignant hematological system disease, monoclonal gammopathy. These are likely knowledge-graph artifacts. The one paper retrieved for blood group incompatibility concerns resistance genes and is unrelated.
- **Mechanistically unfavorable:** Ureaplasma urethritis. Ureaplasma has no cell wall, so β-lactams are intrinsically inactive.
- **Weak or indirect link:** epiglottitis has only one 1986 pediatric gram-negative case series (L4), and xanthogranulomatous pyelonephritis has no evidence (L5) and is usually managed surgically.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

