---
layout: default
title: Sodium Sulfate
parent: Low Evidence (L5)
nav_order: 923
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sodium Sulfate: predicted new indication Dyspepsia (evidence level L5). Approved use: Not stated in the registration data (osmotic laxative / bowel prepara…"
monitor_inn: "Sodium sulfate"
predicted_indications: ["dyspepsia", "dry eye syndrome", "stomach disease", "sclerosing cholangitis", "bronchitis", "methemoglobinemia, alpha type", "methemoglobinemia", "methemoglobin reductase deficiency", "postgastrectomy syndrome", "primary hereditary glaucoma"]
---

# Sodium Sulfate
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

## Sodium Sulfate: From Bowel Cleansing (Osmotic Laxative) to Dyspepsia
{: .text-alpha }

## One-Sentence Summary

Sodium sulfate is an osmotic saline laxative, registered in Singapore as a component of an oral bowel-preparation solution (FORTRANS).
The TxGNN model predicts it may be effective for **dyspepsia**, but **no clinical trials** and only **3 preclinical or unrelated publications** support this, and none of them tests sodium sulfate as a treatment.
The prediction is best read as a model artifact, not an actionable lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (osmotic laxative / bowel preparation by drug class) |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, sodium sulfate is an osmotic saline laxative: it is poorly absorbed and draws water into the bowel lumen, which promotes evacuation.

This action has no known link to the pathophysiology of functional dyspepsia (impaired gastric accommodation, visceral hypersensitivity, delayed gastric emptying and similar mechanisms). The three papers retrieved for this prediction mostly use **dextran sodium sulfate (DSS)**, a different chemical used to induce colitis in animals. They do not show any therapeutic benefit of sodium sulfate. The high TxGNN score most likely reflects a knowledge-graph artifact, not a real pharmacological relationship.

Other top-ranked predictions (dry eye syndrome, stomach disease, sclerosing cholangitis, bronchitis, methemoglobinemia, glaucoma and others) show the same pattern. They have no trials and no plausible mechanism. The only exception is a 1985 cat study on acetaminophen toxicosis, which is weak, indirect, animal-only evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36614242](https://pubmed.ncbi.nlm.nih.gov/36614242/) | 2023 | Preclinical | Int J Mol Sci | Atractylodin, a herbal compound, reduced colitis in a DSS mouse model via PPARα. Dyspepsia is mentioned only as a traditional use of the herb. Sodium sulfate was not tested. |
| [33918638](https://pubmed.ncbi.nlm.nih.gov/33918638/) | 2021 | Preclinical | Molecules | DSS-induced intestinal injury in pigs changed donepezil pharmacokinetics. Unrelated to sodium sulfate therapy. |
| [40391232](https://pubmed.ncbi.nlm.nih.gov/40391232/) | 2025 | Preclinical | J Inflamm Res | Si-Ni Decoction (herbal) was studied in ulcerative colitis through network pharmacology and animal validation. Sodium sulfate was not tested. |

None of these publications evaluates sodium sulfate for dyspepsia.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09234P | FORTRANS FOR ORAL SOLUTION | Granule, for solution | Indication text not recorded in the data compiled for this report |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are model-derived associations, not label text): kidney disease, anuria, intestinal obstruction, ileus, paralytic ileus, toxic megacolon, appendicitis, gastroparesis, pyloric stenosis, chronic diarrheal disease, Clostridium difficile colitis, epilepsy, atrioventricular block, hypercalcemia, potassium deficiency, nephrocalcinosis, and periodic paralysis syndromes, among others.
- **Drug Interactions**: 100 interactions were found in the database. The 20 reviewed include one Major interaction (**amiodarone**) and many Moderate ones, such as abarelix, abiraterone, acetazolamide, salbutamol, aldesleukin, alfentanil, amantadine, amiloride, aminophylline, amitriptyline and aripiprazole. Many involve electrolyte disturbance or QT-related risk.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials, the literature is unrelated or preclinical (mostly DSS colitis models, a different compound), and there is no plausible mechanism linking an osmotic laxative to dyspepsia. The safety profile (laxative effect, electrolyte shifts, many interactions) also argues against use in this setting.

**To proceed, the following is needed:**
- The HSA package insert, to confirm the approved indication, warnings and contraindications
- Mechanism of action data (for example from DrugBank)
- A clear mechanistic hypothesis for dyspepsia, followed by relevant preclinical or clinical evidence
- Review of the other predicted indications (for example methemoglobinemia, where the only evidence is a single feline study) only if new, direct evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

