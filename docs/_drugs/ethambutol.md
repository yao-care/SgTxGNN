---
layout: default
title: Ethambutol
parent: Low Evidence (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Ethambutol
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

# Ethambutol: From Tuberculosis to Epiglottitis

## One-Sentence Summary

Ethambutol is an anti-tuberculosis drug that acts on the mycobacterial cell wall. The TxGNN model predicts it may be effective for **epiglottitis**, but no clinical trials support this, and only **2 publications** touch on it, both about laryngeal tuberculosis rather than classic epiglottitis. The evidence is weak and indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (the Singapore registration records provide no indication text, so this is based on the drug's known use) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (indirect literature only; no trials) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input record. Ethambutol is known to inhibit mycobacterial arabinosyltransferase (EmbB), which blocks arabinogalactan synthesis in the mycobacterial cell wall. It is active only against mycobacteria and is a standard component of multidrug TB regimens.

Classic epiglottitis is usually caused by *Haemophilus influenzae* or other bacteria, which ethambutol does not act on. The mechanism therefore does not support this prediction.

The high score most likely reflects a knowledge-graph link between TB and laryngeal sites. Laryngeal TB can involve the epiglottis, and one case series (41 patients) lists the epiglottis as the second most frequently affected site. That describes tuberculous laryngitis, not epiglottitis in the usual sense. At best, the prediction could apply to epiglottic involvement in laryngeal TB, which is an extension of an existing TB use rather than a new mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Retrospective case series | Eur Respir J | 41 laryngeal TB cases (1975-1985), all with current or prior pulmonary TB. The epiglottis was the second most common site after the true vocal cords. Patients were usually treated with isoniazid, rifampicin and ethambutol. |
| [14720571](https://pubmed.ncbi.nlm.nih.gov/14720571/) | 2004 | Review | Lancet Infect Dis | Review of laryngeal tuberculosis. No abstract is available, so the details of its findings could not be summarised. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN03004P | EBUTOL-100 Tablet 100 mg (Sunward Pharmaceutical) | Tablet, film coated | — |
| SIN03005P | EBUTOL-400 Tablet 400 mg (Sunward Pharmaceutical) | Tablet, film coated | — |

Both products are oral tablets. The registration records provide no approved-indication text.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, and the only literature concerns tuberculous involvement of the larynx, not bacterial epiglottitis, where ethambutol has no activity. The high TxGNN score is likely a knowledge-graph artifact. Other predictions for this drug (for example tubercular laryngitis and tuberculous peritonitis) have more literature (L3), but that evidence is still case-based and combination-therapy-dependent.

**To proceed, the following is needed:**
- Clarify whether the target is classic epiglottitis (not supported) or tuberculous epiglottic/laryngeal involvement (an extension of the existing TB use)
- Obtain the HSA package insert to confirm the approved indications, warnings and contraindications (this blocks safety screening)
- Obtain confirmed mechanism of action data from DrugBank
- Review the full text of the laryngeal TB literature to assess the contribution of ethambutol within multidrug regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

