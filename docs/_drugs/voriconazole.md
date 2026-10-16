---
layout: default
title: Voriconazole
parent: Medium Evidence (L3-L4)
nav_order: 1076
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Voriconazole: predicted new indication Multidrug-resistant tuberculosis (evidence level L4). Approved use: Esophageal candidiasis, candidemia, disseminated candidiasis…"
---

# Voriconazole
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

# Voriconazole: From Invasive Fungal Infections to Multidrug-Resistant Tuberculosis

## One-Sentence Summary

Voriconazole is a triazole antifungal originally used for invasive fungal infections such as aspergillosis, candidemia, esophageal candidiasis and fusariosis.
The TxGNN model predicts it may be effective for **multidrug-resistant tuberculosis**, but this prediction is supported by **no clinical trials** and only **3 publications**, none of which show anti-tuberculosis activity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Esophageal candidiasis, candidemia, disseminated candidiasis, fusariosis, aspergillosis (taken from the knowledge-graph indication list, because the Singapore licence records contain no indication text) |
| Predicted New Indication | Multidrug-resistant tuberculosis |
| TxGNN Prediction Score | 98.67% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, voriconazole inhibits fungal CYP51 (lanosterol 14-alpha-demethylase), blocking ergosterol synthesis in fungal cell membranes. Its efficacy in invasive fungal infections is established.

No direct mechanistic link to tuberculosis has been established. *Mycobacterium tuberculosis* has its own CYP enzymes (such as CYP121 and CYP51-like proteins) that azoles can bind in vitro, but this has not been shown to translate into clinical anti-TB activity. The high TxGNN score most likely reflects the drug's network proximity to antimicrobial indications in the knowledge graph rather than biological evidence.

The only tuberculosis-related publication is a case report of MDR-TB co-existing with aspergilloma and invasive aspergillosis. In that report, voriconazole would treat the fungal co-infection, not the TB. A further practical concern is that rifamycins (rifampin, rifabutin) strongly induce CYP450 enzymes and reduce voriconazole exposure, which complicates its use alongside TB regimens.

Other predictions in the list (cysticercosis, Ambras-type hypertrichosis, Dandy-Walker malformation syndrome, bovine and avian tuberculosis, tuberculoma, tuberculous ascites, and others) also have no plausible mechanistic link and no supporting studies. They appear to be computational artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18992166](https://pubmed.ncbi.nlm.nih.gov/18992166/) | 2008 | Case report | Cases Journal | A diabetic woman had MDR-TB together with aspergilloma and invasive aspergillosis. This is a co-infection and does not show anti-TB activity. |
| [37145297](https://pubmed.ncbi.nlm.nih.gov/37145297/) | 2023 | In vitro study | Brazilian Journal of Microbiology | Photodynamic inactivation of multidrug-resistant *Fonsecaea nubica* (chromoblastomycosis). Not TB-related. |
| [39359062](https://pubmed.ncbi.nlm.nih.gov/39359062/) | 2024 | Microbiological/genetic study | Virulence | Biology and genetic diversity of *Candida krusei* isolates. Not TB-related. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13033P | Vfend Powder for Oral Suspension 40mg/ml | Powder for suspension | Not stated in the licence record |
| SIN12379P | Vfend Film-Coated Tablet 200 mg | Film-coated tablet | Not stated in the licence record |
| SIN12378P | Vfend Film-Coated Tablet 50 mg | Film-coated tablet | Not stated in the licence record |
| SIN12380P | Vfend for Infusion 200 mg/vial | Powder for solution for injection | Not stated in the licence record |
| SIN14859P | Voriconazole Sandoz Film-Coated Tablet 200mg | Film-coated tablet | Not stated in the licence record |

Eleven single-ingredient licences are valid in total, covering oral tablets, oral suspension powder and injectable powder forms. Only the first five are listed here.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

Supplementary information from the knowledge graph (not label text):

- **Disease associations flagged as contraindications**: long QT syndrome (including familial), torsades de pointes, liver disease, gallbladder disease, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, impaired renal function, vision disorder, blindness, cardiomyopathy (including hypertrophic), endomyocardial fibrosis and other myocardial disorders.
- **Drug interactions**: 100 interactions were identified; the first 20 retrieved include several rated **Major**: loperamide, triamcinolone, budesonide and chlorpropamide. Moderate interactions include famotidine, rabeprazole, omeprazole, hydrocortisone, dexamethasone, betamethasone, pioglitazone, alosetron, aprepitant, bisacodyl and clarithromycin. Minor interactions include amphotericin B and cimetidine.
- **Rifamycins**: strong CYP450 induction lowers voriconazole exposure, which is directly relevant to any TB use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model output. There are no registered clinical trials, and the literature consists of a co-infection case report and two unrelated microbiology studies. There is no established mechanism for anti-TB activity, and the interaction with rifamycins is a significant barrier to use in TB regimens.

**To proceed, the following is needed:**
- Mechanism of action data, and in vitro evidence of voriconazole activity against *M. tuberculosis*, including MDR strains
- Preclinical or early-phase clinical data showing anti-mycobacterial efficacy
- A pharmacokinetic assessment of co-administration with rifamycins and second-line TB drugs
- Singapore package insert warnings and contraindications, so that safety screening can proceed
- A QT-prolongation and hepatotoxicity risk review, given the long-term therapy typical of MDR-TB
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

