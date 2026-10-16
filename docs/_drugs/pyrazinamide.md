---
layout: default
title: Pyrazinamide
parent: Low Evidence (L5)
nav_order: 842
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pyrazinamide: predicted new indication Infectious otitis media (evidence level L5). Approved use: Pulmonary tuberculosis, meningeal tuberculosis, tuberculous meningitis"
---

# Pyrazinamide
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

# Pyrazinamide: From Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

Pyrazinamide is an anti-tuberculosis drug, originally used for pulmonary tuberculosis and tuberculous meningitis.
The TxGNN model predicts it may be effective for **infectious otitis media** with a very high score, but **no clinical trials** and **no publications** currently support this specific prediction.
Related evidence exists only for tuberculous middle ear disease (a few case reports under the "middle ear disease" and "chronic otitis media" predictions).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis, meningeal tuberculosis, tuberculous meningitis (from the knowledge graph; the Singapore licence has no indication text) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, pyrazinamide is a component of standard multi-drug anti-tuberculosis regimens, its efficacy in tuberculosis has been established, and it acts only against *Mycobacterium tuberculosis*.

The prediction is therefore only plausible for **tuberculous otitis media**, a rare extrapulmonary form of TB. Common bacterial otitis media is not covered by pyrazinamide. The very high TxGNN score is most likely driven by closeness to tuberculosis in the knowledge graph and not by pathogen-specific evidence.

Other ear-related predictions fall into three groups:
- **TB-linked, supported only by case reports:** middle ear disease, chronic otitis media, suppurative otitis media. These are extensions of the existing TB indication and not true repurposing.
- **No plausible mechanism:** non-suppurative, allergic, cholesterol granuloma, otosalpingitis and infectious otitis interna. These rest on graph similarity alone.
- **Non-ear prediction:** Lyme disease (rank 9) has no direct clinical evidence for pyrazinamide.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was retrieved for infectious otitis media itself. The closest evidence, retrieved for related ear predictions, is shown below. All items are case-level or non-clinical; none evaluates pyrazinamide efficacy in a controlled way.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26785789](https://pubmed.ncbi.nlm.nih.gov/26785789/) | 2013 | Case report | Int J Mycobacteriol | 55-year-old woman with nasal and middle ear TB treated with rifampicin, isoniazid and pyrazinamide for 9 months; no recurrence after one year |
| [15168420](https://pubmed.ncbi.nlm.nih.gov/15168420/) | 2004 | Case report | Am J Kidney Dis | Tuberculous otitis media in a renal transplant recipient after repeated empiric antibiotic treatment for chronic otitis media |
| [41783873](https://pubmed.ncbi.nlm.nih.gov/41783873/) | 2026 | Case report | Cureus | Otorrhea with an unexpected TB cause; TB otitis media is rare and often diagnosed late |
| [41262919](https://pubmed.ncbi.nlm.nih.gov/41262919/) | 2025 | Case report | Front Pediatr | Extensive orbitofacial TB in a child with MHC class II deficiency (only loosely related to otitis media) |
| [8011030](https://pubmed.ncbi.nlm.nih.gov/8011030/) | 1994 | Case series | Laryngo-Rhino-Otologie | 12 patients with TB first found in the head and neck area, including one with middle ear involvement |
| [1985808](https://pubmed.ncbi.nlm.nih.gov/1985808/) | 1991 | Case report | Dtsch Med Wochenschr | Multiorgan TB with sacroiliitis and severe earache (only loosely related) |
| [21439219](https://pubmed.ncbi.nlm.nih.gov/21439219/) | 2011 | Animal study | J Am Assoc Lab Anim Sci | Torticollis in mice infected with *M. tuberculosis*, including mice on pyrazinamide-containing regimens |
| [2527907](https://pubmed.ncbi.nlm.nih.gov/2527907/) | 1989 | Review | Infect Dis Clin North Am | General overview of new uses for old antibiotics, including pyrazinamide (Lyme disease prediction) |
| [38792737](https://pubmed.ncbi.nlm.nih.gov/38792737/) | 2024 | Clinical report | Microorganisms | Dapsone combination therapy for chronic Lyme disease; not about pyrazinamide |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00900P | PYRAZINAMIDE TABLET 500 mg (Sunward Pharmaceutical Private Limited) | Tablet (oral) | Indication text not available |

---

## Safety Considerations

Please refer to the package insert for safety information.

Based on the knowledge graph (not label text), the following conditions are linked to pyrazinamide as contraindications or cautions:
- **Liver:** liver disease, liver failure, acute liver failure, hepatitis
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, gout
- **Porphyria:** porphyria, inherited porphyria, porphyrin metabolism disease
- **Other:** gallbladder disease, peripheral nervous system disease, peripheral neuropathy, substance abuse/dependence, slow acetylator status

**Drug interactions:** 56 interactions were found in total. Moderate-level ones include picosulfuric acid and naltrexone. Others are of unknown severity, including pantoprazole, omeprazole, lansoprazole, prednisone, prednisolone, amphotericin B, vancomycin, metronidazole, streptomycin, glyburide and acetylsalicylic acid.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no trials and no literature for infectious otitis media. Pyrazinamide works only against mycobacteria, so any benefit would be limited to the rare tuberculous otitis media, which is already covered by the existing TB indication through standard multi-drug therapy. This is an extension of the TB indication and not a true new use.

**To proceed, the following is needed:**
- Mechanism of action data
- Package insert warnings and contraindications from the HSA (a blocking gap for safety screening)
- Approved indication text for the Singapore licence
- Confirmation that the target is tuberculous otitis media specifically, with pathogen-specific evidence (such as culture or PCR-confirmed cases)
- Controlled or cohort data on anti-TB regimens that include pyrazinamide for tuberculous ear disease
- Hepatotoxicity monitoring plan, given the liver-related contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

