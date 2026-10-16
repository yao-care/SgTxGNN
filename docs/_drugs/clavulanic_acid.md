---
layout: default
title: Clavulanic Acid
parent: Low Evidence (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Clavulanic Acid: predicted new indication Ureaplasma urethritis (evidence level L5). Approved use: Bacterial infections (urinary tract infection, bacterial pneumonia…"
---

# Clavulanic Acid
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

# Clavulanic Acid: From Bacterial Infections to Ureaplasma Urethritis

## One-Sentence Summary

Clavulanic acid is a beta-lactamase inhibitor, originally used together with amoxicillin to treat bacterial infections such as urinary tract infection and bacterial pneumonia.
The TxGNN model's top-ranked prediction is **Ureaplasma urethritis**, but **no clinical trials** and **no relevant literature** support it, and the mechanism is biologically implausible.
The strongest signal among the predictions is for **gonococcal urethritis** (9 publications, including several 1980s clinical studies), although this is a historical use rather than a new opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (urinary tract infection, bacterial pneumonia, staphylococcal infection, and others). The approved indication text in the Singapore licences is blank, so this comes from the knowledge graph. |
| Predicted New Indication | Ureaplasma urethritis (rank 1) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (rank 1 has only general urethritis literature and no studies of clavulanate in Ureaplasma; the "L4" label in the compiled data is not supported by the data, so it is treated as model prediction only). Best of the other predictions: L3 (gonococcal urethritis). |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From general knowledge, clavulanic acid is a beta-lactamase inhibitor. It has little antibacterial activity of its own, but it protects partner penicillins such as amoxicillin from enzymatic breakdown, which widens their spectrum.

For the top prediction, **Ureaplasma urethritis**, the rationale is weak. Ureaplasma has no cell wall, so beta-lactam antibiotics are expected to be ineffective, and clavulanate adds nothing against it. The retrieved papers cover general urethritis (a *Pasteurella bettyae* report, diagnostic reviews, empirical treatment) and do not test clavulanate against Ureaplasma. The high score most likely reflects the model's network proximity to other urethritis indications, not a real mechanism.

Other predictions fall into three groups:

- **Gonococcal urethritis (rank 2):** Biologically plausible. Clavulanate restores amoxicillin activity against penicillinase-producing *Neisseria gonorrhoeae*. Several 1980s studies of single-dose and two-dose amoxicillin/clavulanate in men reported cure rates of roughly 90% or higher, and in some studies the combination beat kanamycin or procaine penicillin. However, current resistance is mostly chromosomal, and guideline therapy is now ceftriaxone-based, so this is historical use.
- **Infection-related conditions (ranks 3-5):** Uterine inflammatory disease, xanthogranulomatous pyelonephritis and urogenital tuberculosis have indirect or very weak rationale. For tuberculosis, clavulanate does inhibit the mycobacterial beta-lactamase BlaC, but it is not a standard agent for urogenital TB.
- **Non-infectious conditions (ranks 6-10):** Abdominal ectopic pregnancy, celiac trunk compression syndrome, abdominal cystic lymphangioma, lymph node palisaded myofibroblastoma and disease of the uterine broad ligament have no plausible antibacterial mechanism and are likely knowledge-graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (Ureaplasma urethritis), and none for any of the other nine predictions.

---

## Literature Evidence

**Ureaplasma urethritis (top-ranked prediction).** None of the retrieved papers evaluates clavulanate in Ureaplasma infection.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Review | Rev Esp Quimioter | Best empirical treatment for urethritis in Madrid (general urethritis; no Ureaplasma-specific clavulanate data) |
| [19544099](https://pubmed.ncbi.nlm.nih.gov/19544099/) | 2009 | Review | Rev Esp Quimioter | Three-year review of the microorganisms causing male urethritis |
| [34366085](https://pubmed.ncbi.nlm.nih.gov/34366085/) | 2021 | Case report | Infect Dis Now | First association of *Pasteurella bettyae* with urethritis and balanitis in men who have sex with men |
| [9669200](https://pubmed.ncbi.nlm.nih.gov/9669200/) | 1998 | Review | Int J Androl | Possible role of anaerobic bacteria in chronic prostatitis |

**Gonococcal urethritis (best-supported alternative prediction, rank 2).**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3533755](https://pubmed.ncbi.nlm.nih.gov/3533755/) | 1986 | Randomised comparative trial | Genitourin Med | Cefuroxime axetil vs amoxicillin 3 g + clavulanic acid 0.25 g (with probenecid) in 500 patients with uncomplicated gonorrhoea |
| [6365235](https://pubmed.ncbi.nlm.nih.gov/6365235/) | 1984 | Comparative trial | Br J Vener Dis | In 121 men, single-dose amoxicillin/clavulanate left 9.4% culture-positive at 7 days vs 26.3% with procaine penicillin |
| [6428699](https://pubmed.ncbi.nlm.nih.gov/6428699/) | 1984 | Clinical study | Br J Vener Dis | Two-dose Augmentin cured 95.9% vs 87.4% with kanamycin in 192 men; equally effective against penicillinase-producing strains |
| [4007860](https://pubmed.ncbi.nlm.nih.gov/4007860/) | 1985 | Clinical study | Genitourin Med | Amoxicillin 3 g + clavulanic acid 125 mg cured 97 of 100 patients with anogenital gonorrhoea, including 85% of penicillinase-producing strain infections |
| [3004176](https://pubmed.ncbi.nlm.nih.gov/3004176/) | 1985 | Clinical study | Afr J Med Med Sci | Single-dose Augmentin in Ibadan, Nigeria, where about 80% of gonococcal strains were penicillinase-producing |
| [6757686](https://pubmed.ncbi.nlm.nih.gov/6757686/) | 1982 | Clinical study | Med J Malaysia | Single-dose oral amoxicillin/clavulanic acid in males with gonococcal urethritis |
| [3147528](https://pubmed.ncbi.nlm.nih.gov/3147528/) | 1988 | Clinical study/Review | Sex Transm Dis | Options for antibiotic-resistant gonorrhoea, including clavulanic acid added to penicillin or amoxicillin |
| [3132029](https://pubmed.ncbi.nlm.nih.gov/3132029/) | 1988 | Laboratory study | Hinyokika Kiyo | Penicillinase production and antibiotic susceptibility of gonococcal isolates, including amoxicillin/clavulanate |
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Review | Rev Esp Quimioter | Empirical treatment of urethritis |

**Other predictions:** Uterine inflammatory disease has only indirect support (a postpartum endometritis guideline, veterinary studies, a murine *Chlamydia* model and a case report). Urogenital tuberculosis has a single case report (PMID [26847806](https://pubmed.ncbi.nlm.nih.gov/26847806/)) in which amoxicillin/clavulanate was given but not evaluated. The remaining predictions have no literature.

---

## Singapore Market Information

Clavulanic acid has 12 valid single-ingredient registrations in Singapore (none cancelled), across film-coated tablets, powder for oral suspension and powder for injection. The approved indication text is not available in the compiled data. Five main registrations are listed:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08956P | AUGMENTIN TABLET 1 g | Film-coated tablet | Not available |
| SIN09827P | AUGMENTIN TABLET 625 mg | Film-coated tablet | Not available |
| SIN09831P | AUGMENTIN FOR ORAL SUSPENSION 228 mg/5 ml | Powder for suspension | Not available |
| SIN15043P | SALACLAV POWDER FOR SOLUTION FOR INJECTION 1.2G/VIAL | Powder for solution for injection | Not available |
| SIN10599P | CURAM FILM-COATED TABLET 625 mg | Film-coated tablet | Not available |

---

## Safety Considerations

Package insert warnings and contraindications were not available in the compiled data, so please refer to the package insert for them.

- **Disease-level contraindications (knowledge graph, not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, cholestasis (including benign recurrent and familial intrahepatic forms), *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis and chronic Epstein-Barr virus infection syndrome. These should be verified against the label.
- **Drug interactions:** 16 interactions were identified.
  - **Major (2):** leflunomide and teriflunomide.
  - **Moderate (14):** naltrexone, balsalazide, asparaginase *Escherichia coli*, pegaspargase, brentuximab vedotin, clofarabine, epirubicin, idelalisib, interferon beta-1a, interferon beta-1b, peginterferon beta-1a, tioguanine, trabectedin and methotrexate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, Ureaplasma urethritis, has no trials, no relevant literature and an implausible mechanism (Ureaplasma lacks a cell wall), so its high TxGNN score should not be taken at face value. The only prediction with real clinical evidence is gonococcal urethritis, but those studies are from the 1980s and current guidelines use ceftriaxone, so it is a historical use rather than a new repurposing opportunity. Mechanism of action data and package insert safety data are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (a blocking gap for safety screening)
- Mechanism of action data
- Approved indication text for the Singapore licences
- For gonococcal urethritis: current local resistance surveillance data and a comparison with guideline-recommended regimens
- For Ureaplasma urethritis: in vitro susceptibility data, if any, before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

