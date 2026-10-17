---
layout: default
title: Chlorhexidine
parent: Low Evidence (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Chlorhexidine: predicted new indication Chronic ethmoidal sinusitis (evidence level L5). Approved use: Gingivitis"
monitor_inn: "Chlorhexidine"
predicted_indications: ["chronic ethmoidal sinusitis", "sinusitis", "chronic rhinosinusitis", "paranasal sinus neoplasm (disease)", "tinea corporis", "blastomycosis", "Campylobacter fetus infectious disease", "catatrichy", "cutaneous candidiasis", "keratosis follicularis spinulosa decalvans, autosomal dominant"]
---

# Chlorhexidine
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

# Chlorhexidine: From Gingivitis to Chronic Ethmoidal Sinusitis

## One-Sentence Summary

Chlorhexidine is a broad-spectrum antiseptic, originally used to treat gingivitis.
The TxGNN model predicts it may be effective for **chronic ethmoidal sinusitis**,
but **no clinical trials and no publications** currently support this specific prediction. It rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gingivitis |
| Predicted New Indication | Chronic ethmoidal sinusitis |
| TxGNN Prediction Score | 95.46% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

*Note: The Singapore registrations list no approved indication text. Gingivitis is taken from the knowledge-graph indication data used for the prediction.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chlorhexidine is a broad-spectrum antiseptic. Its use in gingivitis rests on reducing the bacterial burden in the mouth, so it may plausibly reduce bacterial load in sinus disease too.

The link between the original and predicted indications is indirect. Gingivitis is a bacterial-plaque-driven inflammation of the oral cavity, while chronic ethmoidal sinusitis is a chronic inflammatory condition of the sinonasal cavity. The prediction probably reflects network proximity in the knowledge graph rather than a demonstrated mechanism, and no direct supporting link has been established.

Other predictions for this drug have somewhat better indirect support. For **chronic rhinosinusitis** (score 95.22%, Evidence Level L4), an in vitro study of a sinonasal stent coated with slow-release chlorhexidine varnish showed sustained protection against bacterial biofilm. A 2024 review also summarizes antiseptics in otorhinolaryngology. This is indirect, preclinical-level evidence with no patient trials. **Sinusitis** (score 95.30%, L3) has only peripheral literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for chronic ethmoidal sinusitis.

For reference, the closest related predictions have the following indirect evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34834197](https://pubmed.ncbi.nlm.nih.gov/34834197/) | 2021 | In vitro study | Pharmaceutics | Sinonasal stent coated with slow-release chlorhexidine varnish gave sustained protection against bacterial biofilm (chronic rhinosinusitis) |
| [38592477](https://pubmed.ncbi.nlm.nih.gov/38592477/) | 2024 | Review | HNO | Overview of antiseptics in otorhinolaryngology; chlorhexidine is advised only as a mouth and body wash for MRSA decolonization, and evidence of clinical efficacy is lacking for many throat antiseptics (chronic rhinosinusitis) |
| [41140432](https://pubmed.ncbi.nlm.nih.gov/41140432/) | 2025 | RCT | J Neurol Surg B Skull Base | Randomized three-arm trial of preoperative antiseptic preparation in transnasal skull base surgery; this is a prophylaxis setting, not sinusitis treatment (sinusitis) |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08671P | DIFFLAM-C ANTI-INFLAMMATORY ANTISEPTIC SOLUTION | Mouthwash | Not stated |
| SIN08535P | HORF LOZENGES | Lozenge | Not stated |
| SIN08901P | SOOV CREAM | Cream | Not stated |
| SIN04696P | ORAL AID LOTION | Lotion | Not stated |

All four are valid single-ingredient registrations. No sinonasal formulation is registered.

---

## Safety Considerations

- **Contraindications (knowledge-graph data, not label text)**: The knowledge graph records periodontitis as a contraindication-linked disease for chlorhexidine. This needs clarification, because it sits oddly with the drug's oral use.
- **Drug Interactions**: The interaction screen returned 100 potential interacting drugs, but none has a severity level assigned. Examples include acetaminophen, atenolol, amlodipine, alprazolam, chloramphenicol, levothyroxine, celecoxib and erythromycin. These cannot be used for risk judgement until severity is classified.

For all other safety information, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for chronic ethmoidal sinusitis rests on model score alone (Evidence Level L5), with no trials or literature. Mechanistic plausibility is only general antiseptic activity, and no sinonasal formulation is registered in Singapore. Package insert warnings and contraindications are also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, to enable safety screening
- Mechanism of action data from DrugBank
- A targeted literature search on chlorhexidine in chronic sinusitis, covering irrigation or topical sinonasal use and mucosal and ciliary tolerability
- Review of the chronic rhinosinusitis prediction as a more evidence-supported research question, starting with the biofilm data
- Confirmation of a suitable route and formulation for sinonasal use
- Severity classification of the interaction screen results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

