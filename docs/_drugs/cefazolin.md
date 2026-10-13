---
layout: default
title: Cefazolin
parent: Medium Evidence (L3-L4)
nav_order: 220
evidence_level: L4
indication_count: 10
---

# Cefazolin
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

# Cefazolin: From Bacterial Pneumonia and Other Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic, originally used for bacterial infections such as pneumonia, endocarditis, bacterial arthritis and cholangitis.
The TxGNN model predicts it may be effective for **infectious otitis media**, but **no clinical trials** are registered and only **2 publications** (a case report and an unrelated review) touch on this direction, so the prediction rests mainly on the model score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, endocarditis, bacterial arthritis, cholangitis (from the knowledge graph; the approved indication text on the Singapore licences is blank) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, cefazolin is a first-generation cephalosporin that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. It is active against Gram-positive cocci such as *Staphylococcus aureus* and streptococci, and mechanistically may be applicable to otitis media caused by these organisms.

The original indications (staphylococcal and streptococcal pneumonia, endocarditis, bacterial arthritis) are Gram-positive-driven infections. Some otitis media pathogens overlap with these. However, cefazolin has limited activity against *Haemophilus influenzae* and *Moraxella catarrhalis*, the most common causes of acute otitis media. This weakens the link.

The only supporting literature is indirect: a 2025 case report of ceftazidime-cefazolin empiric therapy for pediatric Gradenigo syndrome (a complication of otitis media). The other retrieved paper, on Stevens-Johnson syndrome management (1986), is not relevant.

Other related predictions show a similar pattern:
- **Suppurative otitis media** has a 1982 comparative study (cefmetazole vs cefazolin, 172 evaluable patients) in which cefazolin was only the comparator.
- **Urinary tract infection** is mechanistically credible, because cefazolin is excreted in urine and active against many Enterobacterales. There is still no direct randomized evidence.
- **Bronchitis** is plausible for bacterial cases only, and the evidence is old (1975–1988).

## Clinical Trial Evidence

Currently no related clinical trials registered for infectious otitis media.

For reference, the only trial linked to any of the top-ranked predictions is for urinary tract infection:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01349738](https://clinicaltrials.gov/study/NCT01349738) | N/A | Unknown | 200 | Observational study of asymptomatic bacteriuria and UTI risk in renal transplant patients; does not test cefazolin efficacy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case report | Ann Otol Rhinol Laryngol | Ceftazidime-cefazolin empiric therapy for pediatric Gradenigo syndrome, a complication of acute otitis media |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clin Pharm | Management of Stevens-Johnson syndrome; otitis media appears only as the context of the case. Not relevant to efficacy |

Related evidence for other predicted indications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6752467](https://pubmed.ncbi.nlm.nih.gov/6752467/) | 1982 | Comparative clinical study | Jpn J Antibiot | Cefmetazole vs cefazolin in suppurative otitis media (172 patients analysed); cefazolin was the comparator |
| [6352642](https://pubmed.ncbi.nlm.nih.gov/6352642/) | 1983 | Comparative clinical study | J Antimicrob Chemother | Ceftazidime vs cefazolin plus tobramycin in acute exacerbations of chronic bronchitis (59 patients) |
| [1117117](https://pubmed.ncbi.nlm.nih.gov/1117117/) | 1975 | Cohort/Clinical study | J Am Geriatr Soc | Cefazolin in 15 elderly patients with respiratory infections; 13 had excellent to good results |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14846P | Cefazolin Mevon Powder for Solution for Injection or Infusion 1g/vial | Injection, powder, for solution | Not stated |
| SIN12471P | Cezolin Injection 1 gm/vial | Injection, powder, for solution | Not stated |
| SIN07879P | Cefazolin Sandoz 1 g/vial | Injection, powder, for solution | Not stated |
| SIN14304P | Zepilen Powder for Injection 1g/vial | Injection, powder, for solution | Not stated |
| SIN15018P | Cefazolin-AFT Powder for Injection 500mg/vial | Injection, powder, lyophilized, for solution | Not stated |

A sixth licence, SIN14480P (Cefazolin-AFT 1g/vial), is also valid. All six are single-ingredient injectable products and none has been cancelled.

## Safety Considerations

- **Contraindications (from knowledge graph, not label text)**: blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, congenital prothrombin deficiency.
- **Drug Interactions**: 100 interactions were found in total. The main moderate-level ones are with aminoglycosides (kanamycin, neomycin, streptomycin) and picosulfuric acid. Many others (e.g. amphotericin B, aspirin, metformin, morphine, omeprazole) are of unknown severity.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for infectious otitis media rests almost entirely on the model score. No clinical trials exist, and the only relevant literature is a single case report. Cefazolin's weak coverage of *H. influenzae* and *M. catarrhalis*, the main otitis media pathogens, further reduces the likelihood of benefit. Among the top-ranked predictions, suppurative otitis media (L3) and urinary tract infection (L4) have somewhat stronger rationale, and both are marked as research questions rather than candidates for adoption.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator, as the safety review cannot move forward without them
- Mechanism of action data from DrugBank
- Local otitis media pathogen and susceptibility data to test whether cefazolin coverage is adequate
- Direct comparative human studies of cefazolin in otitis media (none currently exist)
- Consideration of suppurative otitis media or urinary tract infection as better-supported alternative directions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

