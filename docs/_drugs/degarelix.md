---
layout: default
title: Degarelix
parent: Low Evidence (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Degarelix: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not stated in the Singapore licence records compiled for this report"
---

# Degarelix
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

# Degarelix: From Its Approved Use in Advanced Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Degarelix is a GnRH receptor antagonist that is marketed in Singapore as an injectable (FIRMAGON). The HSA licence records compiled for this report do not contain indication text.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction, and the mechanistic link is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records compiled for this report |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on its known drug class, degarelix is a GnRH receptor antagonist. It suppresses LH and FSH, which in turn lowers gonadal androgens.

Hypertrichosis is generally not androgen-dependent, unlike hirsutism, so the link between androgen suppression and this condition is weak. The very high TxGNN score reflects graph-based proximity in the knowledge network, not supporting trials or literature.

The other top predictions are also weakly supported. Most are congenital or structural conditions (for example Ambras syndrome, Dandy-Walker malformation syndromes, and genetic hair shaft abnormalities) that hormone suppression would not be expected to correct. Two predictions are more plausible at the pathway level:
- **Central precocious puberty** is the most biologically coherent, because suppressing the GnRH axis is already the standard of care there (with GnRH agonists). However, there are no paediatric data for degarelix, it is given as a depot injection with injection-site reactions, and approved agents already exist.
- **Familial male-limited precocious puberty** is mechanistically contradicted, because the disease acts downstream of GnRH and LH.

For allergic urticaria, degarelix has a known hypersensitivity signal, so it may cause rather than treat the condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14350P | FIRMAGON Powder and Solvent for Solution for Injection 120 mg | Injection, powder, for solution | Not stated in the records compiled |
| SIN14351P | FIRMAGON Powder and Solvent for Solution for Injection 80 mg | Injection, powder, for solution | Not stated in the records compiled |

---

## Cytotoxicity

Degarelix is used in hormone-dependent cancer, but it is a hormonal (GnRH antagonist) therapy rather than a conventional cytotoxic agent. This classification is based on its drug class, and no toxicity data were available in the compiled data. Please refer to the package insert warnings and precautions.

---

## Safety Considerations

- **Disease associations from the knowledge graph** (not label text): long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease, gallbladder disease and potassium deficiency disease are linked to degarelix as contraindication edges.
- **Drug Interactions**: The interaction query returned 100 interactions in total; 20 are listed in the data compiled for this report. Most are moderate. The two **major** interactions are:
  - Cisapride
  - Dolasetron

  Moderate interactions include clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron, famotidine, loperamide and several laxatives and bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol, lactulose, lactitol, magnesium citrate, magnesium hydroxide, castor oil, glycerin, mineral oil). Metronidazole is a minor interaction. Many of these agents are linked to QT prolongation or electrolyte disturbance, which is consistent with the QT-related disease associations above.
- **Hypersensitivity**: Injection-site and hypersensitivity reactions are known with degarelix, and rare urticaria or anaphylaxis has been reported with GnRH antagonists.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no clinical trials or publications, and the mechanism linking GnRH antagonism to hypertrichosis is weak. Hypertrichosis is generally not androgen-dependent. The safety profile also raises QT-prolongation and hypersensitivity concerns.

**To proceed, the following is needed:**
- The HSA package insert, to confirm approved indications, warnings and contraindications
- Mechanism of action data from DrugBank
- Preclinical or mechanistic evidence for a role of GnRH antagonism in hypertrichosis
- A literature and trial search specific to hypertrichosis and degarelix
- If a more plausible direction is pursued, a separate assessment of central precocious puberty, including paediatric safety, formulation suitability and added value over existing GnRH agonists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

