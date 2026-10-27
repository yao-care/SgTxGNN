---
layout: default
title: Cefuroxime
parent: Low Evidence (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cefuroxime: predicted new indication Top-ranked by TxGNN: polyclonal hyperviscosity syndrome. Best evidenc… (evidence level L5). Approved use: Bacterial infections (infectious otitis media, bacterial…"
monitor_inn: "Cefuroxime"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "Peptostreptococcus infectious disease", "blood group incompatibility", "urinary tract infection (disease)", "premalignant hematological system disease", "monoclonal gammopathy", "suppurative otitis media", "hematological disease associated with an acquired peripheral neuropathy"]
---

# Cefuroxime
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Cefuroxime: From Bacterial Infections to Urinary Tract Infection
{: .text-alpha }

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic, originally used for bacterial infections such as otitis media, pneumonia, meningitis, gonorrhoea and Lyme disease.
The TxGNN model's top-ranked prediction is **polyclonal hyperviscosity syndrome**, but it has no supporting evidence and is not biologically plausible. The best-supported prediction is **urinary tract infection (UTI)**, with **5 clinical trials** (1 directly relevant observational study) and **20 publications** in the data compiled for this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (infectious otitis media, bacterial pneumonia, bacterial meningitis, gonorrhoea, Lyme disease, etc.), based on knowledge-graph indication data. The Singapore licence records do not include indication text. |
| Predicted New Indication | Top-ranked by TxGNN: polyclonal hyperviscosity syndrome. Best evidence-supported: urinary tract infection |
| TxGNN Prediction Score | 99.76% (polyclonal hyperviscosity syndrome); 99.62% (urinary tract infection) |
| Evidence Level | L5 for polyclonal hyperviscosity syndrome; L3 for urinary tract infection |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold for polyclonal hyperviscosity syndrome; Proceed with Guardrails for urinary tract infection |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cefuroxime is a second-generation cephalosporin that kills bacteria by inhibiting cell wall synthesis (binding penicillin-binding proteins). It is active against common respiratory pathogens and many Gram-negative organisms.

**Top-ranked prediction (polyclonal hyperviscosity syndrome):** There is no mechanistic link. This is a haematological/immunological condition with no bacterial target. The high score is a graph-based artefact, with no trials or literature behind it. The same applies to the other highly ranked non-infectious predictions (hyperamylasaemia, congenital analbuminaemia, blood group incompatibility, premalignant haematological disease, monoclonal gammopathy and haematological disease associated with acquired peripheral neuropathy). These should not be pursued.

**Best-supported prediction (UTI):** Cefuroxime is active against common uropathogens such as *E. coli*, *Klebsiella* and *Proteus*. UTI is a bacterial infection like the drug's established indications, so this is a plausible extension of existing use rather than a new mechanism. Reviews of cefuroxime axetil describe efficacy in UTI, a randomised comparison against aztreonam exists in upper UTI (1989), and a completed observational study evaluated cefuroxime in pyelonephritis. No Phase 3 RCT testing cefuroxime for UTI appears in the data.

**Other infectious predictions:** Suppurative otitis media is closely related to the already-labelled indication of infectious otitis media, so it is largely a restatement of an existing use. Peptostreptococcus infection is biologically plausible, but the only evidence is a 1981 in-vitro study centred on ceftazidime (Evidence Level L4).

---

## Clinical Trial Evidence

Trials for urinary tract infection (the only prediction with clinical trials):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04616352](https://clinicaltrials.gov/study/NCT04616352) | N/A | Completed | 973 | Effect of inappropriate cefuroxime therapy in adults hospitalised with pyelonephritis (directly relevant, observational) |
| [NCT01507974](https://clinicaltrials.gov/study/NCT01507974) | N/A | Completed | 220 | Preventive antibiotics in pregnant women with recurrent UTI (antibiotic not confirmed as cefuroxime) |
| [NCT02789579](https://clinicaltrials.gov/study/NCT02789579) | Early Phase 1 | Unknown | 150 | One-week antimicrobial prophylaxis before minimally invasive upper tract lithotomy (cefuroxime-specific relevance unclear) |
| [NCT05577273](https://clinicaltrials.gov/study/NCT05577273) | N/A | Unknown | 1000 | Antibiotic prophylaxis at urinary catheter removal (not clearly cefuroxime-specific) |
| [NCT02009098](https://clinicaltrials.gov/study/NCT02009098) | Phase 4 | Withdrawn | 0 | Antibiotic prophylaxis after caesarean section; withdrawn with no participants, so provides no evidence |

No clinical trials are registered for any of the other predicted indications.

---

## Literature Evidence

Selected publications (urinary tract infection and suppurative otitis media):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41693075](https://pubmed.ncbi.nlm.nih.gov/41693075/) | 2026 | Systematic review | Pharmacotherapy | Oral β-lactams versus TMP/SMX and fluoroquinolones for complicated UTI: effectiveness, safety and PK |
| [38215770](https://pubmed.ncbi.nlm.nih.gov/38215770/) | 2024 | Randomised trial | Lancet Infect Dis | De-escalation from antipseudomonal β-lactams in Enterobacterales bloodstream infection (indirect) |
| [2689345](https://pubmed.ncbi.nlm.nih.gov/2689345/) | 1989 | Randomised comparison | Infection | Aztreonam versus cefuroxime in gram-negative upper UTI |
| [8799689](https://pubmed.ncbi.nlm.nih.gov/8799689/) | 1996 | Review | Drugs | Cefuroxime axetil: antibacterial activity, pharmacokinetics and therapeutic efficacy |
| [18611587](https://pubmed.ncbi.nlm.nih.gov/18611587/) | 1994 | Review | Int J Antimicrob Agents | Cefuroxime axetil activity against respiratory pathogens |
| [6349019](https://pubmed.ncbi.nlm.nih.gov/6349019/) | 1983 | Review | Ther Drug Monit | Cefuroxime antimicrobial activity, pharmacology and clinical efficacy |
| [6344037](https://pubmed.ncbi.nlm.nih.gov/6344037/) | 1983 | Review | Pharmacotherapy | Cefuroxime mechanism, spectrum, pharmacokinetics and adverse reactions |
| [7142073](https://pubmed.ncbi.nlm.nih.gov/7142073/) | 1982 | Pharmacokinetic study | J Antimicrob Chemother | Cefuroxime diffusion into middle ear effusions in chronic purulent otitis media |
| [11980456](https://pubmed.ncbi.nlm.nih.gov/11980456/) | 2001 | Review | Indian J Pediatr | Antimicrobial use and choice in otitis media |
| [19802974](https://pubmed.ncbi.nlm.nih.gov/19802974/) | 1981 | In vitro study | J Antimicrob Chemother | Comparison of ceftazidime and cefuroxime against anaerobes; cefuroxime inhibited 79% of isolates at 16 mg/l (Peptostreptococcus) |

Most remaining UTI and otitis media publications are microbiology and susceptibility surveys, which provide only background evidence. The literature linked to blood group incompatibility (a salmonella resistance surveillance study) is unrelated to the indication. The monoclonal gammopathy papers concern infections in neutropenic patients and do not support treating the underlying disorder.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12049P | CEFTIL TABLET 250 mg | Film-coated tablet | Not available |
| SIN15154P | CEFUROXIME-AFT POWDER FOR INJECTION 1.5G/VIAL | Powder for injection | Not available |
| SIN10946P | SHINCEF FOR INJECTION 750 mg/vial | Powder for injection | Not available |
| SIN02365P | ZINNAT TABLET 250 mg | Film-coated tablet | Not available |
| SIN02364P | ZINNAT TABLET 500 mg | Film-coated tablet | Not available |

There are 8 valid single-ingredient registrations in total, covering oral (film-coated tablet) and injectable (powder for solution) forms.

---

## Safety Considerations

- **Contraindication-related conditions (from knowledge-graph data, not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotising enterocolitis, congenital prothrombin deficiency.
- **Drug Interactions (100 interactions found; all those listed are Moderate):**
  - Acid-suppressing agents: famotidine, ranitidine, cimetidine, nizatidine, and proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, rabeprazole, pantoprazole)
  - Antacids: aluminium hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide
  - Aminoglycosides: kanamycin, neomycin
  - Others: balsalazide

Please refer to the package insert for warnings and full safety information.

---

## Conclusion and Next Steps

**Decision: Hold for polyclonal hyperviscosity syndrome and the other non-infectious predictions; Proceed with Guardrails for urinary tract infection**

**Rationale:**
- The top-ranked predictions are non-infectious conditions with no mechanism, trials or literature, so they should not be pursued (Evidence Level L5). UTI is the one prediction with a plausible mechanism, a completed relevant observational study (N=973) and supportive reviews (Evidence Level L3). Because it is an extension of cefuroxime's existing antibacterial use and lacks a Phase 3 RCT, it warrants cautious progression with guardrails.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently missing, blocking safety screening)
- Approved indication text for the Singapore licences, to confirm whether UTI is already labelled
- Mechanism of action data
- Local antimicrobial resistance (susceptibility) data for Singapore uropathogens
- Comparative clinical trial data (ideally a Phase 3 RCT) for cefuroxime in UTI or pyelonephritis
- Review of renal, hepatic and coagulation risks and the listed drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

