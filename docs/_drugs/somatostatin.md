---
layout: default
title: Somatostatin
parent: Medium Evidence (L3-L4)
nav_order: 918
evidence_level: L4
indication_count: 10
---

# Somatostatin
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

# Somatostatin: Predicted New Indication Amenorrhea (Original Indication Not Recorded)

## One-Sentence Summary

Somatostatin is a peptide hormone product marketed in Singapore as an injectable (STILAMIN), but the registry record does not state its approved indication.
The TxGNN model predicts it may be effective for **Amenorrhea**, with a score of 98.6%.
**No clinical trials** and **14 publications** were found. The publications concern pituitary tumours in which amenorrhea is a symptom, and none tests somatostatin as a treatment for it.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Somatostatin is a native peptide hormone that suppresses the secretion of several hormones, including growth hormone. The retrieved literature suggests this prediction is largely an artefact of knowledge-graph proximity rather than a treatment rationale.

In the retrieved papers, amenorrhea is a **symptom** of pituitary adenomas, such as prolactinoma, GH-secreting and ACTH-secreting tumours. Somatostatin analogs act on these tumours and the hormone excess they cause. Any benefit for amenorrhea would therefore be **indirect**, through tumour or hormone control. No retrieved evidence shows that somatostatin itself restores menstruation. The high score most likely reflects the drug's closeness to pituitary disease in the knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28170483](https://pubmed.ncbi.nlm.nih.gov/28170483/) | 2017 | Review | JAMA | Pituitary adenomas can hypersecrete hormones or cause mass effects, so early diagnosis and treatment matter |
| [15765032](https://pubmed.ncbi.nlm.nih.gov/15765032/) | 2004 | Review | Minerva Endocrinol | Excess prolactin from pituitary tumours causes amenorrhea-galactorrhea in women |
| [17644863](https://pubmed.ncbi.nlm.nih.gov/17644863/) | 2002 | Review | Eat Weight Disord | Anorexia nervosa features amenorrhea alongside GH/IGF-I axis changes |
| [15578985](https://pubmed.ncbi.nlm.nih.gov/15578985/) | 2004 | Review | Curr Drug Targets Immune Endocr Metab Disord | Cushing's syndrome includes amenorrhea among its endocrine and metabolic effects |
| [1400888](https://pubmed.ncbi.nlm.nih.gov/1400888/) | 1992 | Case report | J Clin Endocrinol Metab | Woman with primary amenorrhea and a GH-prolactin adenoma. Bromocriptine restored ovulatory menses, and relapsed acromegaly was treated with the somatostatin analog SMS 201-995 (octreotide) plus bromocriptine |
| [41687635](https://pubmed.ncbi.nlm.nih.gov/41687635/) | 2025 | Case report | Georgian Med News | Late diagnosis of acromegaly in a woman with a somatoprolactinoma, whose disease began with amenorrhea |
| [34158336](https://pubmed.ncbi.nlm.nih.gov/34158336/) | 2021 | Case report | BMJ Case Rep | Adolescent with secondary amenorrhoea was found to have ACTH-dependent Cushing disease |
| [24683483](https://pubmed.ncbi.nlm.nih.gov/24683483/) | 2014 | Case report | Endocrinol Diabetes Metab Case Rep | Woman with secondary amenorrhoea had a calcified GH-secreting macroadenoma |
| [21814887](https://pubmed.ncbi.nlm.nih.gov/21814887/) | 2012 | Case report | Pituitary | Woman with amenorrhea and galactorrhea was diagnosed with MEN 1A |
| [2922994](https://pubmed.ncbi.nlm.nih.gov/2922994/) | 1989 | Case series | Acta Neuropathol | Immunocytochemistry of four mixed pituitary adenomas, one linked to amenorrhea-galactorrhea |

None of these publications is a trial of somatostatin for amenorrhea. PMID 1400888 is the only one involving a somatostatin analog, and there it treated acromegaly, not amenorrhea.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06135P | STILAMIN 3000 FOR INJECTION 3 mg/ampoule | Injection, powder, for solution | Not listed in the registry record |

Manufacturer: Merck Serono S.A. / Alfasigma S.p.A. The product is injectable only.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Amenorrhea is a symptom rather than a treatment target, and no trial or study supports somatostatin as a treatment for it. The literature only describes amenorrhea as a feature of pituitary tumours, so the high TxGNN score is not backed by clinical evidence.

**Other predictions for this drug:**
Among the other predicted indications, **multiple endocrine neoplasia** has the strongest support. It has completed Phase 2 trials of somatostatin analogs (octreotide LAR, lanreotide) in neuroendocrine tumours and one Phase 3 MEN1 trial of unknown status. That evidence comes from analogs and imaging tracers, not native somatostatin. It was scored L2 / Proceed with Guardrails and deserves a separate evaluation.

**To proceed, the following is needed:**
- The approved indication from the HSA package insert, to establish the original use
- Package insert warnings and contraindications (safety screening is currently blocked)
- Mechanism of action data from DrugBank
- A clinical rationale showing a direct link to amenorrhea, or a decision to re-focus on the multiple endocrine neoplasia prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

