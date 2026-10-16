---
layout: default
title: Amikacin
parent: Medium Evidence (L3-L4)
nav_order: 82
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Amikacin: predicted new indication Paratyphoid fever (evidence level L4). Approved use: Bacterial pneumonia, Pseudomonas aeruginosa infection, cholangitis…"
monitor_inn: "Amikacin"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "punctate epithelial keratoconjunctivitis", "typhoid fever", "epiglottitis", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "meningococcemia"]
---

# Amikacin
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

# Amikacin: From Bacterial Infections (Pneumonia, Meningitis, Cholangitis) to Paratyphoid Fever

## One-Sentence Summary

Amikacin is an aminoglycoside antibiotic, originally used for serious Gram-negative bacterial infections such as pneumonia, meningitis and cholangitis.
The TxGNN model predicts it may be effective for **paratyphoid fever**,
but there are currently **no registered clinical trials** and only **8 publications** (mostly epidemiology and antibiogram surveys, with no direct amikacin efficacy data), so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, Pseudomonas aeruginosa infection, cholangitis, bacterial meningitis and other bacterial infections (from the knowledge graph; the Singapore licence records do not include approved indication text) |
| Predicted New Indication | Paratyphoid fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, amikacin is an aminoglycoside that inhibits the bacterial 30S ribosomal subunit and has broad Gram-negative activity. Its efficacy in Gram-negative infections is established, so activity against *Salmonella* Paratyphi is plausible.

There are important limitations. *Salmonella* is a facultative intracellular pathogen, and aminoglycosides penetrate cells poorly. Standard enteric fever therapy relies on fluoroquinolones, azithromycin or third-generation cephalosporins, so amikacin has no clear role. The high TxGNN score therefore reflects knowledge-graph similarity rather than demonstrated clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case report | Pediatr Hematol Oncol | Child with leukaemia and acalculous cholecystitis due to *S.* Paratyphi B, successfully treated with cefepime, amikacin and granulocyte support (combination therapy) |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Case series | Mikrobiyol Bul | 48 paratyphi B patients with strains resistant to classical therapy; antibiotic choices and outcomes reported |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Cohort | J Indian Med Assoc | 145 paediatric enteric fever cases; clinical profile and antibiotic sensitivity of *S.* Typhi and Paratyphi |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Surveillance | Med J Armed Forces India | Drug susceptibility of 45 enteric fever isolates, including re-emerging chloramphenicol sensitivity |
| [8354556](https://pubmed.ncbi.nlm.nih.gov/8354556/) | 1993 | Epidemiological survey | Indian J Pathol Microbiol | 280 *S.* Typhi strains; multidrug-resistant strains remained sensitive to aminoglycosides, including amikacin |
| [16410091](https://pubmed.ncbi.nlm.nih.gov/16410091/) | 2006 | Case series | J Pediatr Surg | Four children with splenic abscess managed by percutaneous drainage and antibiotics |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Microbiological survey | Pak J Biol Sci | Isolation and identification of *S.* Paratyphi from enteric fever patients in Quetta |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Epidemiological survey | New Microbiol | Occurrence of *S.* Typhi and Paratyphi in Jordan, 1988–2000 |

None of these studies provides controlled evidence of amikacin efficacy in paratyphoid fever.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11944P | ILDONG AMIKACIN INJECTION 500 mg/2 ml | Injection | Not stated in the available records |
| SIN15908P | AKACIN INJECTION 500MG/2ML | Injection, solution | Not stated in the available records |

---

## Safety Considerations

- **Disease-related cautions (knowledge-graph based, not label text)**: Kidney disease, pyoureter, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, central nervous system vertigo, myasthenia gravis (including adult-onset), neuromuscular junction disease, parkinsonian disorders and Parkinson disease.
- **Drug Interactions** (100 interactions recorded; examples):
  - **Major**: Magnesium sulfate, Mannitol
  - **Moderate**: Amphotericin B (including lipid and liposomal forms), Kanamycin, Neomycin, Acetylsalicylic acid, Exenatide, mesalazine-type agents (Balsalazide, Mesalazine, Olsalazine), and proton pump inhibitors (Omeprazole, Esomeprazole, Lansoprazole, Dexlansoprazole, Pantoprazole, Rabeprazole)

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model scoring and in vitro or epidemiological data. There are no clinical trials, and no study shows clinical efficacy of amikacin in paratyphoid fever. Aminoglycosides penetrate cells poorly, effective first-line alternatives exist, and amikacin carries notable nephrotoxicity, ototoxicity and neuromuscular risks, so the unmet need and benefit–risk case are weak.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently missing and blocking safety screening)
- Mechanism of action data
- Clinical or at least robust in vivo evidence of amikacin efficacy against *Salmonella* Paratyphi, including intracellular activity
- Comparison with standard therapy (fluoroquinolones, azithromycin, third-generation cephalosporins), particularly in multidrug-resistant cases
- Approved indication text for the two Singapore licences, to confirm the on-label scope

---

**Other predictions in this evaluation (all Hold):** typhoid fever and salmonellosis (L4; in vitro and case-level evidence only, with one small comparison showing a 36.4% clinical effective rate for amikacin versus 100% for ofloxacin in typhoid fever), meningococcemia (L4; no direct amikacin evidence), and diffuse scleroderma, punctate epithelial keratoconjunctivitis, epiglottitis, congenital analbuminemia, polyclonal hyperviscosity syndrome and hyperamylasemia (L5; model prediction only, several likely knowledge-graph artifacts).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

