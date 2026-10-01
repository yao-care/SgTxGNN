---
layout: default
title: Tislelizumab
parent: Low Evidence (L5)
nav_order: 987
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tislelizumab: From an Unspecified Original Indication to Mixed-Type Autoimmune Hemolytic Anemia

## One-Sentence Summary

Tislelizumab is a PD-1 blocking antibody that the literature describes as approved for advanced solid tumours such as lung and esophageal cancer. The Singapore registration record does not state an approved indication.
The TxGNN model predicts it may be effective for **mixed-type autoimmune hemolytic anemia**, but **0 clinical trials** and **0 publications** support this. The mechanism also argues against it, so this is a model-only prediction that is probably in the wrong direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration record (the literature describes use in advanced solid tumours, e.g. NSCLC and esophageal cancer) |
| Predicted New Indication | Mixed-type autoimmune hemolytic anemia |
| TxGNN Prediction Score | 93.76% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Tislelizumab is a PD-1 blocking antibody (humanized IgG4) that releases the brake on T cells to restore anti-tumour immunity. Its use in cancer is well documented in the retrieved literature.

The prediction is **not mechanistically convincing**. Blocking PD-1 reduces immune tolerance and can unmask or worsen autoimmunity. Immune checkpoint inhibitors are themselves recognised causes of immune-mediated hemolysis, so a benefit in autoimmune hemolytic anemia is biologically implausible. The knowledge-graph link probably reflects shared immune-pathway neighbours rather than a treatment effect.

The other top-ranked predictions show the same pattern:
- Several are autoimmune or hemolytic conditions: idiopathic aplastic anemia, drug-induced and neonatal autoimmune hemolytic anemia, and amyopathic dermatomyositis. PD-1 blockade is more likely to trigger or worsen these than to treat them.
- For dermatitis and proteinuria, the literature found is almost entirely about tislelizumab **causing** skin and kidney injury, which is a harm signal rather than a therapeutic one.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN17089P | TEVIMBRA Concentrate for Solution for Infusion 100mg/10mL | Infusion, solution concentrate |

The record lists Boehringer Ingelheim Biopharmaceuticals (China) Ltd as the manufacturer. It does not include the approved indication text.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-1 checkpoint inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Not a typical direct myelosuppressant; immune-mediated hematologic toxicity is possible (a case of agranulocytosis is reported in the literature) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC, liver and renal function, and monitoring for immune-related adverse events (skin, kidney) |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

The package insert warnings and contraindications are not in the record, so please refer to the package insert for formal safety information. No drug interaction data were found.

The literature retrieved for the other predicted indications shows these safety signals:
- **Severe skin reactions**: Stevens-Johnson syndrome/toxic epidermal necrolysis (SJS/TEN) and DRESS, in multiple case reports, case series and systematic reviews. Pharmacovigilance analyses (FAERS) also flag cutaneous toxicity.
- **Renal injury**: thrombotic microangiopathy (with fruquintinib) and granulomatosis with polyangiitis, in single case reports.
- **Hematologic toxicity**: agranulocytosis reported together with TEN in one case.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or literature, and PD-1 blockade is mechanistically expected to aggravate autoimmune hemolysis rather than treat it. The safety literature points toward harm in the immune-mediated conditions examined.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- The approved indication text for the Singapore registration
- Any supporting clinical or preclinical evidence for a benefit in autoimmune hemolytic anemia. Without it, the candidate should not advance.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

