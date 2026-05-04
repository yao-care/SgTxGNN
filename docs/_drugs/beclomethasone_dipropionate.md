---
layout: default
title: Beclomethasone Dipropionate
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
---

# Beclomethasone Dipropionate
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

# Beclomethasone Dipropionate: From Asthma to Atopic Eczema

## One-Sentence Summary

Beclomethasone dipropionate (BDP) is a potent synthetic glucocorticoid corticosteroid widely used internationally for asthma and allergic rhinitis via inhaled or topical routes.
The TxGNN model predicts it may be effective for **Atopic Eczema**,
with **0 registered clinical trials** and **18 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma / Allergic Rhinitis (internationally established use; no Singapore registration on record) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Beclomethasone dipropionate is a potent synthetic glucocorticoid that exerts its anti-inflammatory effects by binding to the glucocorticoid receptor (GR), suppressing the transcription factors NF-κB and AP-1. This leads to downregulation of key pro-inflammatory cytokines — IL-4, IL-13, and IL-31 — along with reduced eosinophil infiltration, mast cell activation, and IgE secretion. These are the defining features of the Th2-mediated allergic immune cascade.

Atopic eczema is mechanistically rooted in this exact Th2-driven immune dysregulation, involving skin barrier dysfunction and chronic eosinophilic skin inflammation. Topical corticosteroids are already the first-line standard of care for atopic dermatitis globally. Applied topically, BDP can directly suppress the epidermal and dermal inflammatory cascade at the core of atopic eczema pathophysiology — making the mechanistic alignment between the drug's known pharmacology and this predicted indication highly credible.

Furthermore, BDP's established indications (asthma, allergic rhinitis) share the same Th2 immunopathological axis as atopic eczema, suggesting the therapeutic effect can translate across atopic conditions. A double-blind, placebo-controlled RCT (PMID 6434024) demonstrated significant clinical improvement in children with severe atopic eczema treated with combined oral and nasal BDP. A clinical series (PMID 1476023) also showed stable disease control with oral BDP in severe childhood atopic dermatitis. Notably, existing evidence is based on non-standard routes of administration (oral, nasal), while large modern topical formulation RCTs remain absent — which constitutes the primary evidence gap.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Beclomethasone dipropionate in atopic eczema.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6434024](https://pubmed.ncbi.nlm.nih.gov/6434024/) | 1984 | RCT | British Medical Journal | Double-blind, placebo-controlled crossover trial in 26 children with severe atopic eczema; combined oral + nasal BDP produced significantly greater improvement than placebo over 4 weeks; mild HPA axis suppression observed but no adverse effects reported |
| [1476023](https://pubmed.ncbi.nlm.nih.gov/1476023/) | 1992 | Clinical Series | Acta Derm Venereol Suppl | Oral BDP achieved stable disease control in 10/14 children with severe atopic dermatitis (mean dose 1000 µg/day); growth deceleration noted at maintenance doses warranting careful monitoring |
| [14522624](https://pubmed.ncbi.nlm.nih.gov/14522624/) | 2003 | Prospective Cohort | J Dermatol Treatment | Corticosteroid wet-wrap therapy in 8 prepubertal children with atopic eczema; assessed short-term growth (knemometry) and bone turnover; highlights systemic exposure risk with occlusive applications |
| [30911861](https://pubmed.ncbi.nlm.nih.gov/30911861/) | 2019 | Pharmaceutical Formulation | AAPS PharmSciTech | Development and validation of BDP mixed micelles in biocompatible hydrogel for enhanced dermal delivery; sub-chronic dermatitis animal model confirmed improved penetration and anti-inflammatory effect |
| [19874229](https://pubmed.ncbi.nlm.nih.gov/19874229/) | 2009 | Experimental | Immunopharmacol Immunotoxicol | Head-to-head mouse comparison of mometasone furoate vs BDP; MF showed greater topical anti-inflammatory potency with lower systemic effects; provides context for relative positioning of BDP among topical corticosteroids |
| [8765824](https://pubmed.ncbi.nlm.nih.gov/8765824/) | 1996 | Experimental | J Allergy Clin Immunol | Topical steroids including BDP enhanced in vitro spontaneous IgE production in atopic dermatitis patients; signals potential for disease relapse with steroid monotherapy and supports need for combination strategies |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Review of systemic effects of intranasal corticosteroids (including BDP) on the HPA axis in patients with co-existing allergic rhinitis, asthma, and atopic dermatitis; recommends cumulative dose monitoring |
| [11488426](https://pubmed.ncbi.nlm.nih.gov/11488426/) | 2001 | Pharmacological Review | Jpn J Pharmacol | Comprehensive review of glucocorticoids including BDP as the most efficacious class for allergic diseases; discusses mechanism of action and comparative pharmacology across routes of administration |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Review | Allergy | Investigation of delayed contact allergy and occasional immediate hypersensitivity to corticosteroids (including BDP) in asthma patients; relevant safety signal for use in atopic individuals |
| [37023229](https://pubmed.ncbi.nlm.nih.gov/37023229/) | 2023 | Computational | J Chem Inf Model | Knowledge graph-based drug repurposing model (DrugRep-KG) identifying BDP–atopic eczema as a predicted association; provides independent computational corroboration of the TxGNN prediction |

---

## Singapore Market Information

Beclomethasone dipropionate is currently **not registered in Singapore**. No Health Sciences Authority (HSA) product authorizations are on record. This means there is no locally approved product label available for reference, and regulatory approval would be required before clinical use in Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Singapore HSA package insert data (key warnings, contraindications) and drug interaction data were not available at the time of this report. Retrieval from the HSA official website and DrugBank API is recommended before any clinical or regulatory decision is made. This represents a blocking data gap for full safety evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A double-blind RCT and multiple clinical series demonstrate that BDP produces measurable clinical benefit in atopic eczema, and the mechanistic link via GR-mediated Th2 suppression is well established and directly aligned with the disease's core pathophysiology. However, existing RCT evidence dates from 1984, uses non-topical routes (oral/nasal), and is limited to small paediatric populations — modern large-scale topical formulation RCTs are absent, and Singapore market registration would need to be initiated from scratch.

**To proceed, the following is needed:**
- Retrieve Singapore HSA package insert (or international equivalent) to document key warnings, contraindications, and approved safety profile
- Query DrugBank API for complete MOA data and drug interaction profile to fill current data gaps
- Conduct or identify a modern topical BDP RCT or systematic meta-analysis specifically in atopic eczema to upgrade evidence from L2 to L1
- Establish a safety monitoring plan covering HPA axis suppression, skin atrophy risk, adrenal function (especially in paediatric populations), and cumulative corticosteroid exposure with concurrent inhaled/nasal BDP use
- Assess HSA regulatory pathway and market entry strategy given the current "Not Marketed" status in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

