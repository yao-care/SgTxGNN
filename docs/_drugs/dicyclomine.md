---
layout: default
title: Dicyclomine
parent: Low Evidence (L5)
nav_order: 328
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
monitor_inn: "Dicyclomine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)"]
description: "Dicyclomine: predicted new indication Cauda equina syndrome (evidence level L5). In Singapore: 2 HSA registrations (2 valid)"
---

# Dicyclomine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Dicyclomine: Cauda equina syndrome
{: .text-alpha }

## One-Sentence Summary

The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dicyclomine: "Dicyclomine relieves smooth muscle spasm of the gastrointestinal tract. Animal studies indicate that this action is achieved via a dual mechanism: a specific anticholinergic effect (antimuscarinic) at the acetylcholine-receptor sites with approximately 1/8 the milligram potency of atropine ( in vitro, guinea pig ileum); and a direct effect upon smooth muscle (musculotropic) as evidenced by dicyclomine’s antagonism of bradykinin- and histamine-induced spasms of the isolated guinea pig ileum." ([DailyMed: dicyclomine hydrochloride prescribing information, Slate Run Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e20a1ccf-2f3a-4872-811e-d93fb56b8e83), label version 2026-11-13; accessed 2026-11-19.) Based on known information, dicyclomine is an antimuscarinic antispasmodic that relaxes smooth muscle in the gut. Its efficacy in functional bowel disorders is established, and mechanistically it may be applicable to smooth-muscle spasm in other organs.

In cauda equina syndrome, the bowel and bladder dysfunction could in theory be eased by reduced detrusor overactivity and smooth muscle spasm. This is a symptom-level rationale only. Dicyclomine does not address the underlying nerve root compression, which needs surgical decompression. The very high TxGNN score is a computational prediction with no clinical trial or literature support.

Other predictions in the list are more biologically coherent but equally unsupported by studies:
- **Obsolete neurogenic bladder (score 0.9950)**: Antimuscarinic blockade of detrusor receptors is a well-established mechanism. Agents such as oxybutynin already cover this space, and the disease term is obsolete and should be mapped to a current ontology entry.
- Proton pump inhibitors, H2 blockers and H. pylori eradication are the standard of care.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN02547P | VERAGEL-DMS TABLET | TABLET | Valid |
| SIN03333P | COLIMIX SYRUP | SYRUP | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Contraindications (from knowledge-graph disease associations, not label text)**: Conditions linked to dicyclomine include:
  - Angle-closure glaucoma
  - Benign prostatic hyperplasia
  - Liver disease, liver failure, hepatic coma and hepatic encephalopathy
  - Kidney disease
  - Gastric ulcer
  - Coronary artery disease
  - Hypertension
  - Porphyria
  - Blood disorders (thrombocytopenia, neutropenia, agranulocytosis, anaemia)
  - Sleep apnoea
  - Anxiety and neurotic disorders
  - Substance abuse or dependence
  - Gallbladder disease
- **Drug Interactions**: 100 interactions were found. Most of those listed are Moderate, including:
  - Opioids: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol
  - Other anticholinergic or antihistamine agents: chlorpheniramine, acrivastine, phenyltoloxamine, hyoscyamine, aclidinium, amitriptyline
  - Others: ethanol, loperamide, amantadine, galantamine, acebutolol, botulinum toxin type A, acetylcholine

  Minor interactions include acetaminophen and hydrochlorothiazide.
- Anticholinergic adverse effects (tachycardia, urinary retention, cognitive impairment) may be relevant to several predicted indications.

Please also refer to the package insert for the full warnings, as label text was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication of cauda equina syndrome rests on a high TxGNN score alone, with no trials or publications. The rationale is symptom-level only and does not address the underlying cause. The drug is already marketed in Singapore, but only for its existing uses.

**To proceed, the following is needed:**
- Mechanism of action data
- Package insert warnings and contraindications from the Singapore regulator
- Approved indication text for the Singapore licences
- A literature and trial search specific to dicyclomine in neurogenic bowel and bladder dysfunction
- Mapping of the obsolete "neurogenic bladder" term to a current ontology entry

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: dicyclomine hydrochloride prescribing information, Slate Run Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e20a1ccf-2f3a-4872-811e-d93fb56b8e83) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

