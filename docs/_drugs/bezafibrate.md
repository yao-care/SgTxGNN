---
layout: default
title: Bezafibrate
parent: Medium Evidence (L3-L4)
nav_order: 156
evidence_level: L4
indication_count: 10
---

# Bezafibrate
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Bezafibrate: From Hyperlipidemia to Hypoalphalipoproteinemia

## One-Sentence Summary

Bezafibrate is a fibrate-class lipid-lowering drug, originally used for hyperlipidemia and familial hyperlipidemia.
The TxGNN model predicts it may be effective for **hypoalphalipoproteinemia** (isolated low HDL cholesterol),
but currently there are **no registered clinical trials** and only **3 publications**, none of them controlled trials, supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia, familial hyperlipidemia |
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 98.54% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Bezafibrate is a pan-PPAR agonist (alpha/gamma/delta), and its main target is PPAR-alpha. Activating PPAR-alpha raises the expression of ApoA-I and ApoA-II and lowers triglycerides, which typically increases HDL cholesterol. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description is based on the known pharmacology of the drug.

The original indication, hyperlipidemia, and the predicted indication, low HDL, are both disorders of lipid metabolism, and the drug already acts on the pathways involved. A 2001 study reported improved endothelial function in patients with coronary artery disease and isolated low HDL treated with bezafibrate. However, it was a small non-randomised study, and the other retrieved papers address the triglyceride/HDL relationship and drug-induced low HDL, so they are only indirect support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11483875](https://pubmed.ncbi.nlm.nih.gov/11483875/) | 2001 | Clinical study (small, non-RCT) | J Cardiovasc Pharmacol | Bezafibrate raised HDL and improved endothelial dysfunction in patients with coronary artery disease and isolated low HDL |
| [1575823](https://pubmed.ncbi.nlm.nih.gov/1575823/) | 1992 | Observational study | Atherosclerosis | Low HDL in hypertriglyceridemic patients is linked to disturbed triglyceride metabolism (indirect evidence) |
| [7567762](https://pubmed.ncbi.nlm.nih.gov/7567762/) | 1995 | Case report | Postgrad Med J | Combining probucol with a fibrate caused profoundly low HDL and ApoA-I in two patients (indirect evidence) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10217P | ZAFIBRAL TABLET 200 mg | Film-coated tablet | Not specified |

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: chronic kidney disease, chronic renal failure syndrome, end-stage renal failure
- **Drug Interactions**: The only interaction record is a pharmacology entry linking bezafibrate to its target, PPAR-alpha, and it does not describe a drug-drug interaction. The literature also reports that combining a fibrate with probucol can sharply lower HDL and ApoA-I.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the model score is high, but the evidence is limited to a small non-randomised study and indirect reports, with no registered trials. Bezafibrate is marketed in Singapore, but the package insert safety data are not yet available, and the kidney-related contraindication signals need review.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website
- Mechanism of action data from DrugBank
- Controlled studies of bezafibrate in isolated low HDL, with cardiovascular outcomes or validated surrogate endpoints
- Review of renal function restrictions and the risk of combining with probucol or statins
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

