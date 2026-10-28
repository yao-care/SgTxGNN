---
layout: default
title: Tobramycin
parent: Medium Evidence (L3-L4)
nav_order: 999
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Tobramycin"
predicted_indications: ["exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "epidemic keratoconjunctivitis"]
description: "Tobramycin: predicted new indication Exposure keratitis (evidence level L4). Approved use: Not recorded in the local data"
---

# Tobramycin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Tobramycin: Exposure keratitis
{: .text-alpha }

## One-Sentence Summary

Tobramycin is an aminoglycoside antibiotic, originally used for bacterial eye infections and related conditions such as conjunctivitis, uveitis and staphylococcal infection.
The TxGNN model predicts it may be effective for **exposure keratitis**,
but there are **no registered clinical trials** and only **8 publications** (mostly case reports and laboratory studies), so the evidence is very limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Exposure keratitis |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L4 |
| Singapore Market Status | Marketed (valid licences: 5 of 5) |
| Number of Registrations | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Tobramycin is a bactericidal aminoglycoside. It inhibits bacterial protein synthesis by binding to the 30S ribosomal subunit and is used topically against ocular bacterial infections. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description relies on general pharmacological knowledge.

Exposure keratitis is mainly a drying and surface injury of the cornea, caused for example by incomplete eyelid closure. An antibiotic would address only secondary bacterial infection of the damaged cornea. The connection to the original indications is therefore indirect: both involve the corneal and conjunctival surface, but the underlying problem differs.

The retrieved literature is also indirect. It consists of bacterial keratitis case reports, susceptibility data, and an in vitro study showing that aminoglycosides can be toxic to corneal epithelial cells. That toxicity is a concern in an already compromised cornea.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42842711](https://pubmed.ncbi.nlm.nih.gov/42842711/) | 2026 | Retrospective cohort | Cornea | Compared characteristics and outcomes of MRSA and MSSA *Staphylococcus aureus* keratitis |
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In vitro study | Current Eye Research | Aminoglycosides, including tobramycin, showed cytotoxicity to rabbit corneal epithelial cells |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | In vitro study | Nippon Ganka Gakkai Zasshi | Compared MIC and post-antibiotic effect of eyedrops on isolates from infectious keratitis in Japan |
| [42358321](https://pubmed.ncbi.nlm.nih.gov/42358321/) | 2026 | In vitro study (veterinary) | Frontiers in Veterinary Science | Effect of fluorometholone on antibiotic susceptibility of canine ocular bacteria |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | Contact lens-related *Bacillus cereus* keratitis |
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Case report | Oxford Medical Case Reports | Multidrug-resistant *Shewanella algae* keratitis in a patient who could not close his eyes |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Case report | Eye & Contact Lens | Bilateral MRSA keratitis after photorefractive keratectomy |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Case report | Yan Ke Xue Bao | Paracentral corneal dellen as a rare sign of Graves ophthalmopathy |

None of these studies directly tests tobramycin in exposure keratitis.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04451P | TOBREX Sterile Ophthalmic Solution 0.3% | Solution | Not available |
| SIN04722P | TOBREX Sterile Ophthalmic Ointment 0.3% | Ointment | Not available |
| SIN04309P | TOBRADEX Ophthalmic Ointment | Ointment | Not available |
| SIN04438P | TOBRADEX Sterile Ophthalmic Suspension | Solution | Not available |
| SIN13647P | ZYLET Sterile Ophthalmic Suspension | Suspension, sterile | Not available |

All five registrations are valid single-ingredient licences (ophthalmic products).

## Safety Considerations

- **Disease-related cautions (from knowledge-graph data, not label text)**: Tobramycin is linked to possible contraindications or cautions in conditions including kidney disease, myasthenia gravis and other neuromuscular junction disorders, Parkinson disease, glaucoma and ocular hypertension, herpes simplex virus keratitis, and fungal, viral or tuberculous eye infections.
- **Corneal toxicity**: An in vitro study found aminoglycoside toxicity to corneal epithelial cells, which matters for a damaged cornea in exposure keratitis.
- **Drug Interactions**: 100 interactions were identified. The **Major** ones are with **magnesium sulfate** and **mannitol**. Moderate interactions include other aminoglycosides and nephrotoxic or ototoxic agents (neomycin, kanamycin, vancomycin, amphotericin B), as well as proton pump inhibitors (omeprazole, pantoprazole, lansoprazole, rabeprazole, dexlansoprazole), aspirin and mesalazine/sulfasalazine-type drugs.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials and the literature is indirect (case reports, susceptibility data and a corneal toxicity study). Exposure keratitis is mainly a surface-drying problem, and tobramycin would at most help with secondary infection, while its corneal epithelial toxicity is a safety concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Singapore-registered products (HSA)
- Detailed mechanism-of-action data from DrugBank
- Clinical data on topical tobramycin for secondary infection in exposure keratitis, including corneal safety
- Approved indication text for the Singapore licences, to confirm which uses are currently registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

