---
layout: default
title: Testosterone Undecanoate
parent: 僅模型預測 (L5)
nav_order: 964
evidence_level: L5
indication_count: 10
---

# Testosterone Undecanoate
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

# Testosterone Undecanoate: From Hypogonadism to Androgen Insensitivity Syndrome

## One-Sentence Summary

> Testosterone undecanoate is an orally/parenterally administered form of testosterone, conventionally used as androgen replacement therapy in male hypogonadism.
> Among TxGNN's top candidates, the model's highest-scoring prediction (homozygous familial hypercholesterolemia) is flagged by its own mechanistic rationale as likely graph noise with no supporting evidence. The most credible repurposing signal instead points to **Androgen Insensitivity Syndrome (AIS)**, supported by **2 published cohort studies** and a clear, direct pharmacological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack (no Singapore license on file); testosterone undecanoate is broadly known as an androgen/testosterone replacement therapy for hypogonadism |
| Predicted New Indication | Androgen Insensitivity Syndrome (AIS) |
| TxGNN Prediction Score | 95.72% (rank #24,932) |
| Evidence Level | L3 (cohort studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: TxGNN's #1-ranked prediction (homozygous familial hypercholesterolemia, score 98.73%) was excluded from this report's primary focus — its own mechanistic rationale identifies it as a likely spurious graph-embedding link with no biological plausibility and no supporting trials or literature (Evidence Level L5, Hold).*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for testosterone undecanoate in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, testosterone undecanoate is an exogenous androgen that, once de-esterified, binds the androgen receptor (AR) to mediate masculinization, bone density maintenance, and secondary sexual characteristic development.

Androgen Insensitivity Syndrome arises from mutations in the AR gene, causing partial or complete resistance to androgen signaling despite normal or elevated endogenous testosterone. In **partial AIS (PAIS)**, residual AR function can still be leveraged: supraphysiological or supplemental exogenous testosterone may enhance receptor occupancy and partially overcome the reduced receptor sensitivity, promoting virilization and phallic growth. In **complete AIS (CAIS)**, particularly post-gonadectomy patients, testosterone can serve as hormone replacement to support bone mineral density and psychosexual well-being — though its efficacy here is less mechanistically direct than in PAIS, since AR resistance is total.

This is therefore a plausible, receptor-level pharmacological hypothesis rather than a purely graph-derived coincidence — but it is important to note AIS is not a homogeneous population; response is expected to vary substantially between PAIS and CAIS subtypes, and this heterogeneity is not captured by the TxGNN score alone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39039878](https://pubmed.ncbi.nlm.nih.gov/39039878/) | 2024 | Cohort (self-controlled) | Zhonghua Er Ke Za Zhi (Chinese J Pediatrics) | Genetically diagnosed AIS patients (Beijing Children's Hospital, 2009–2021) treated with oral testosterone; evaluated efficacy and safety of androgen therapy in this population |
| [8246276](https://pubmed.ncbi.nlm.nih.gov/8246276/) | 1993 | Cohort (double-blind crossover) | Journal of Sex & Marital Therapy | Oral testosterone undecanoate (Andriol, 120 mg/day) vs. placebo in 4 gonadectomized complete testicular feminization (CAIS) patients; assessed hormone levels, mood, sociosexual functioning, and body image |

---

## Singapore Market Information

Testosterone undecanoate is not currently marketed in Singapore under this evidence pack (0 registered licenses). No local approved-indication or formulation data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: this evidence pack flags a Blocking data gap — Singapore/TFDA-equivalent label warnings and contraindications are not yet available, which prevents a formal S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The AIS hypothesis has a direct receptor-level mechanistic basis and is supported by two published cohort studies (including a 2024 pediatric AIS cohort), placing it at Evidence Level L3 — meaningfully stronger than TxGNN's top-ranked but mechanistically unsupported candidate (HoFH, L5/Hold). However, AIS subtype heterogeneity (PAIS vs. CAIS) and the absence of controlled trials mean this should proceed cautiously, not as a confirmed indication.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: obtain formal drug label warnings/contraindications (currently no Singapore registration exists, so an equivalent reference market label, e.g., US/EU, should be sourced)
- Resolve High-priority gap DG002: confirm detailed MOA via DrugBank API query
- Stratify future evidence review by AIS subtype (partial vs. complete) given divergent expected treatment response
- Consider a systematic literature review beyond the 2 cohort studies currently identified, given the rarity of AIS as a study population
- Two mechanistically plausible but currently unevidenced endocrine candidates (Leydig cell hypoplasia due to LH resistance; 46,XY DSD due to impaired androgen production) warrant a targeted literature search before further action, as they represent standard hormone-replacement logic but lack any trial/literature support in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

