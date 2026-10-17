---
layout: default
title: Tislelizumab
parent: Low Evidence (L5)
nav_order: 997
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tislelizumab: predicted new indication Mixed-type autoimmune hemolytic anemia (evidence level L5). Approved use: Not stated in the HSA licence record (published sources describe use…"
monitor_inn: "Tislelizumab"
predicted_indications: ["mixed-type autoimmune hemolytic anemia", "idiopathic aplastic anemia", "dermatitis", "paroxysmal nocturnal hemoglobinuria", "drug-induced autoimmune hemolytic anemia", "proteinuria", "acne keloid", "neonatal autoimmune hemolytic anemia", "primary CD59 deficiency", "amyopathic dermatomyositis"]
---

# Tislelizumab
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

# Tislelizumab: From Advanced Solid Tumours to Mixed-Type Autoimmune Hemolytic Anemia

## One-Sentence Summary

Tislelizumab is an anti-PD-1 monoclonal antibody used in cancer immunotherapy, and the HSA licence record in the data compiled for this report does not list an approved indication text.
The TxGNN model predicts it may be effective for **mixed-type autoimmune hemolytic anemia**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model-only prediction (Evidence Level L5), and the biology points the opposite way: PD-1 blockade is more likely to cause autoimmune hemolysis than to treat it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA licence record (published sources describe use in Hodgkin lymphoma, bladder cancer, oesophageal squamous cell carcinoma and other cancers) |
| Predicted New Indication | Mixed-type autoimmune hemolytic anemia |
| TxGNN Prediction Score | 93.76% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known information, tislelizumab is a humanized IgG4 antibody that binds PD-1 (PDCD1, CD279) on T cells. It blocks the PD-1/PD-L1 pathway and reactivates anti-tumour immunity.

The prediction is **not mechanistically convincing**. Autoimmune hemolytic anemia is driven by an overactive immune response against red blood cells. Enhancing T-cell activity through PD-1 blockade would be expected to worsen this condition, and immune checkpoint inhibitors are reported to cause autoimmune hemolytic anemia. The TxGNN score likely reflects network proximity in the knowledge graph (a disease-association link) rather than a true treatment signal.

Other top-ranked predictions show the same pattern. These include idiopathic aplastic anemia, drug-induced autoimmune hemolytic anemia, neonatal autoimmune hemolytic anemia and amyopathic dermatomyositis. All are immune-mediated conditions that PD-1 blockade would more plausibly aggravate. Dermatitis and proteinuria, ranked third and sixth, appear in the literature only as adverse events of tislelizumab.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for mixed-type autoimmune hemolytic anemia.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17089P | TEVIMBRA CONCENTRATE FOR SOLUTION FOR INFUSION 100MG/10ML | Infusion, solution concentrate | Not stated in the licence record |

Manufacturer: Boehringer Ingelheim Biopharmaceuticals (China) Ltd. The single licence is valid and the product is a single-ingredient injectable.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-1 checkpoint inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Low as a direct effect; immune-mediated haematological toxicity (for example agranulocytosis, hemolysis) has been reported |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function, thyroid function, skin and renal immune-related adverse events |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Immune-related adverse events**: Reports in the literature describe severe cutaneous reactions, including Stevens-Johnson syndrome/toxic epidermal necrolysis (SJS/TEN), DRESS, psoriasiform and lichenoid eruptions. One case report also describes TEN with agranulocytosis.
- **Renal toxicity**: Reported cases include thrombotic microangiopathy (with fruquintinib) and granulomatosis with polyangiitis.
- **Haematological autoimmunity**: Checkpoint inhibitors as a class are reported to cause immune-mediated hemolysis, which is directly relevant to the predicted indication.
- **Drug interactions**: The only recorded interaction entry is its pharmacological target, PD-1 (CD279). It carries no severity level and is not a drug-drug interaction.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials or publications. The mechanism of PD-1 blockade argues against benefit in autoimmune hemolytic anemia and for possible harm. None of the other top-ranked predictions has trial evidence either. The dermatitis and proteinuria literature documents adverse events, not therapeutic benefit.

**To proceed, the following is needed:**
- HSA package insert warnings, contraindications and approved indication text (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Preclinical or mechanistic evidence that PD-1 blockade could benefit autoimmune hemolytic anemia, which is currently contradicted by reported immune-mediated hemolysis
- A review of reported cases of checkpoint-inhibitor-associated hemolysis to clarify the safety signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

