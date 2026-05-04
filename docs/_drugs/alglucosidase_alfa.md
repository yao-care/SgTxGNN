---
layout: default
title: Alglucosidase Alfa
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Alglucosidase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Alglucosidase Alfa: From Pompe Disease (GSD II) to Adult Polyglucosan Body Disease

## One-Sentence Summary

Alglucosidase alfa is a recombinant human acid alpha-glucosidase (GAA) enzyme replacement therapy, originally approved for Pompe disease (Glycogen Storage Disease Type II), in which deficient lysosomal GAA leads to progressive glycogen accumulation in muscle and cardiac tissue.
The TxGNN model predicts it may have potential benefit in **Adult Polyglucosan Body Disease (APBD)**, a related lysosomal glycogen metabolism disorder.
However, this prediction is currently supported by **no clinical trials** and **no published literature**, making this a hypothesis-generating signal only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pompe disease (Glycogen Storage Disease Type II) — enzyme replacement therapy for GAA deficiency |
| Predicted New Indication | Adult Polyglucosan Body Disease (APBD) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 — Model prediction only, no supporting studies |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Alglucosidase alfa is a recombinant form of the lysosomal enzyme acid alpha-glucosidase (GAA), which is deficient in Pompe disease (GSD type II). By delivering exogenous GAA to lysosomes via mannose-6-phosphate receptor–mediated uptake, the drug restores the cell's capacity to degrade intralysosomal glycogen, thereby preventing its pathological accumulation in skeletal muscle, cardiac muscle, and respiratory muscles. This mechanism of action is well established in GSD II and forms the biological rationale for exploring related lysosomal glycogen disorders.

Adult Polyglucosan Body Disease (APBD) is caused by mutations in the *GBE1* gene encoding glycogen branching enzyme, and is therefore a distinct enzymatic defect from Pompe disease. Rather than excess glycogen accumulation in lysosomes (as in GSD II), APBD is characterised by the formation of abnormally structured polyglucosan bodies — poorly branched, insoluble glycogen-like aggregates — that accumulate in neurons, astrocytes, and muscle cells, leading to a progressive neurological syndrome (upper and lower motor neuron signs, peripheral neuropathy, neurogenic bladder) typically presenting in the fifth or sixth decade of life.

The mechanistic link proposed by TxGNN is an indirect one: both conditions belong to the broader category of lysosomal and cytoplasmic glycogen metabolism disorders. The hypothesis is that enhanced lysosomal glycogen clearance by alglucosidase alfa might reduce the glycogen substrate pool available for polyglucosan body formation, thereby partially attenuating APBD pathology. This represents a plausible but speculative extrapolation — the causative enzymatic defects are different (GAA vs. GBE1), and no preclinical or clinical data currently validate this cross-disease application. The prediction is best interpreted as a research question worthy of mechanistic investigation rather than a near-term clinical opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Alglucosidase alfa is not currently registered or marketed in Singapore. No authorisation records were found in the Singapore Health Sciences Authority (HSA) database.

> **Note:** Alglucosidase alfa (brand names: Myozyme®, Lumizyme®) is approved in the United States (FDA, 2006/2010), European Union (EMA, 2006), and multiple other jurisdictions for the treatment of Pompe disease. Clinicians requiring access in Singapore would need to apply via the Special Access Route (SAR) or the Exemption under the Health Products Act.

---

## Safety Considerations

Please refer to the package insert for safety information. Key known safety considerations for alglucosidase alfa from published literature include:

- **Infusion-associated reactions**: Including anaphylaxis and severe hypersensitivity reactions; risk is highest in immune-tolerant-naïve infants. Pre-medication and risk stratification are standard of care.
- **Cardiac arrhythmia risk**: Particularly relevant in infantile-onset Pompe disease patients with pre-existing cardiac hypertrophy.
- **Immunogenicity**: Anti-drug antibodies (including high-sustained antibody titres, HSAT) can reduce efficacy; immune tolerance induction protocols may be required.
- **Risk in respiratory compromise**: Patients with advanced respiratory failure may require ventilatory support during and after infusions.

Formal safety data for use in APBD is entirely unavailable and cannot be extrapolated without prospective evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.47%) to alglucosidase alfa for APBD, and the mechanistic rationale — shared lysosomal glycogen metabolism pathway — provides a biologically coherent, if indirect, hypothesis. However, with zero clinical trials, zero published literature, and no Singapore regulatory registration, the evidence base is entirely model-derived (L5). The enzymatic defects in GSD II (GAA) and APBD (GBE1) are distinct, making direct mechanism transfer uncertain.

**To advance this candidate, the following steps are needed:**

- **Preclinical validation**: Assess whether alglucosidase alfa reduces polyglucosan body burden in *GBE1*-knockdown or *Gbe1*-mutant animal models (mouse models of APBD are available).
- **Mechanistic studies**: Clarify whether mannose-6-phosphate receptor expression in affected neuronal and glial cells is sufficient for adequate drug uptake in APBD pathological tissue.
- **Natural history comparison**: Identify whether any Pompe disease patients with concurrent GBE1 heterozygous variants, or vice versa, offer observational clues.
- **Orphan disease landscape review**: Confirm that no investigator-initiated studies on GAA replacement in polyglucosan disorders exist in grey literature or conference abstracts (search scope was limited to ClinicalTrials.gov and PubMed).
- **MOA data gap remediation**: Obtain full DrugBank mechanistic profile (flagged as DG002) to support formal mechanistic link scoring.
- **Regulatory pathway planning**: If preclinical data are supportive, evaluate feasibility of a Singapore SAR application and an investigator-initiated Phase 1/2 basket trial in lysosomal glycogen disorders.

> ⚠️ *This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

