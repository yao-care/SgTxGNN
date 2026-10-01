---
layout: default
title: Galsulfase
parent: Low Evidence (L5)
nav_order: 463
evidence_level: L5
indication_count: 10
---

# Galsulfase
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

# Galsulfase: From Mucopolysaccharidosis VI to Ptosis-Strabismus-Ectopic Pupils Syndrome

## One-Sentence Summary

Galsulfase is an enzyme replacement therapy for mucopolysaccharidosis VI (MPS VI), where it replaces the missing enzyme that breaks down dermatan sulfate.
The TxGNN model gives its top prediction, **ptosis-strabismus-ectopic pupils syndrome**, a high score, but there are **0 clinical trials** and **0 publications** behind it, and no plausible biological link.
Across all 10 predictions the only mechanistically coherent one is Scheie syndrome (another MPS disorder), which has 4 indirect publications and still no direct support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | MPS VI (Maroteaux-Lamy syndrome). The Singapore registration text is blank, so this comes from the drug's known mechanism description |
| Predicted New Indication | Ptosis-strabismus-ectopic pupils syndrome |
| TxGNN Prediction Score | 97.89% (model rank 17,533) |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank for this record. From the evidence pack's description, galsulfase is a recombinant N-acetylgalactosamine-4-sulfatase (arylsulfatase B). It degrades dermatan sulfate inside lysosomes, and its role is to clear the substrate that accumulates in MPS VI.

The top prediction, ptosis-strabismus-ectopic pupils syndrome, is a rare congenital disorder of eye movement and pupil function. It has no known glycosaminoglycan storage component, so an enzyme that clears dermatan sulfate has no obvious target. The same holds for the other top-9 predictions. They are congenital eyelid, cranial nerve or extraocular muscle disorders (for example congenital Horner syndrome, jaw-winking syndrome, epiblepharon), and none involves lysosomal storage. The high scores (97.5–97.9%) reflect graph-based similarity only and should not be read as biological plausibility.

Scheie syndrome (rank 10, score 94.79%) is the only candidate with a coherent pathway link, because it is also an MPS disorder. However, it is caused by alpha-L-iduronidase deficiency, a different enzyme at a separate step of the degradation pathway. Galsulfase cannot correct that defect, and an approved, mechanism-matched therapy (laronidase) already exists.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top prediction (ptosis-strabismus-ectopic pupils syndrome).

For reference, the four publications retrieved for Scheie syndrome (rank 10) are general MPS enzyme replacement therapy papers. None was shown to test galsulfase in Scheie syndrome, so this evidence is class-level and indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22210671](https://pubmed.ncbi.nlm.nih.gov/22210671/) | 2011 | Review | Rheumatology (Oxford) | Overview of MPS therapy. Enzyme replacement is available for MPS I (including Scheie), II and VI, with multidisciplinary care recommended |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de Médecine Interne | Review of enzyme replacement across lysosomal storage diseases (Gaucher, Fabry and others) |
| [20040314](https://pubmed.ncbi.nlm.nih.gov/20040314/) | 2009 | Review | Int J Clin Pharmacol Ther | Enzyme replacement reduces peripheral disease burden in MPS, but neurological manifestations remain hard to treat |
| [20040319](https://pubmed.ncbi.nlm.nih.gov/20040319/) | 2009 | Cohort | Int J Clin Pharmacol Ther | Infusion-related reactions to enzyme replacement in MPS I, II and VI patients were usually easy to manage |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16831P | NAGLAZYME Concentrate for Solution for Infusion 5mg/5ml (Vetter Pharma-Fertigung GmbH & Co. KG) | Infusion, solution concentrate | Not stated in the registration record |

## Safety Considerations

- **Infusion-related reactions**: Hypersensitivity reactions have been reported with enzyme replacement therapy across MPS types I, II and VI, but were usually manageable in a published cohort (PMID 20040319).
- **Drug Interactions**: No interactions were found in the queried database.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction rests on a model score alone. There are no trials or publications, and the mechanism gives no reason to expect a lysosomal enzyme to help a congenital eye-movement or pupil disorder. Scheie syndrome is the only pathway-adjacent option, but galsulfase acts at a different enzymatic step and a specific therapy already exists.

**To proceed, the following is needed:**
- The HSA package insert, to establish warnings, contraindications and the registered indication (blocking for any safety screening)
- Detailed mechanism-of-action data from DrugBank
- Direct evidence, such as preclinical or clinical data, testing galsulfase in any predicted indication
- If pursuing Scheie syndrome, a comparison against laronidase and a rationale for why galsulfase would add value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

