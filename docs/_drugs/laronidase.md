---
layout: default
title: Laronidase
parent: 僅模型預測 (L5)
nav_order: 573
evidence_level: L5
indication_count: 10
---

# Laronidase
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

# Laronidase: From Mucopolysaccharidosis I to Lysosomal Storage Disease with Skeletal Involvement

## One-Sentence Summary

Laronidase (recombinant human α-L-iduronidase) is an enzyme replacement therapy originally developed to treat **Mucopolysaccharidosis I (MPS I)**. The TxGNN model predicts it may be effective for **lysosomal storage disease with skeletal involvement**, which the evidence indicates is essentially the skeletal (dysostosis multiplex) manifestation of MPS I itself rather than a novel indication. This direction is currently supported by **4 publications** (no dedicated clinical trials are registered against this specific disease label), on top of the well-established RCT evidence base for laronidase in MPS I generally.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis I (MPS I) — not available from a Singapore-approved label (drug is not locally marketed); derived from literature (PMID 12196045, 25345091) |
| Predicted New Indication | Lysosomal storage disease with skeletal involvement |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action text is currently a data gap (flagged as DG002 in this evidence pack). However, the literature attached to this candidate does describe the mechanism directly: laronidase is a recombinant form of α-L-iduronidase, the lysosomal enzyme that is deficient in MPS I. Once administered, the enzyme is taken up by cells — including fibroblasts and, notably, **osteoblasts** — predominantly via mannose-6-phosphate receptors, after which it is trafficked to lysosomes and processed into its mature, catalytically active form (PMID 18758061). This directly reduces accumulation of the glycosaminoglycans (GAGs) dermatan sulfate and heparan sulfate that drive MPS I pathology (PMID 25345091).

The predicted indication, "lysosomal storage disease with skeletal involvement," is not mechanistically distant from laronidase's known biology — it describes the dysostosis multiplex (multi-site skeletal dysplasia) phenotype that is a core, well-documented feature of MPS I, caused by GAG accumulation in cartilage and bone matrix. The demonstrated uptake of laronidase by osteoblasts in vitro (PMID 18758061), together with a long-term (6.5-year) clinical follow-up of ERT in an attenuated MPS I phenotype (Scheie syndrome) reporting on skeletal radiographs among other parameters (PMID 23127271), supports biological plausibility for a skeletal-specific benefit.

Because of this, the repurposing rationale attached to this candidate explicitly frames it **not as a novel mechanistic hypothesis, but as a phenotypic subset of the drug's own original indication** — meaning the primary open question is one of local market/regulatory availability in Singapore rather than of proving a new mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Review | BioDrugs | Overview of laronidase development as recombinant α-L-iduronidase ERT for MPS I (including Hurler syndrome), with US/EU orphan drug and FDA fast-track status |
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Review | Pediatric Endocrinology Reviews | Describes MPS I disease spectrum (Hurler / Hurler-Scheie / Scheie) caused by α-L-iduronidase deficiency and GAG accumulation, including skeletal manifestations |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | Preclinical (in vitro uptake) | Biological & Pharmaceutical Bulletin | Laronidase is taken up dose-dependently by MPS I fibroblasts **and osteoblasts** mainly via mannose-6-phosphate receptors, then trafficked to lysosomes and processed to its mature form |
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Case Report | Pediatric Neurology | 6.5-year follow-up of ERT in an attenuated MPS I case (Scheie syndrome), including skeletal radiograph monitoring; disease progression noted despite therapy |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/HSA label warnings and contraindications for laronidase are currently flagged as a blocking data gap (DG001) in this evidence pack and must be obtained before any S1 safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic case is unusually strong because the predicted indication is essentially a phenotypic subset of laronidase's own original, already-proven indication (MPS I), supported by direct evidence of enzyme uptake into bone-relevant cells (osteoblasts). However, laronidase is not currently marketed in Singapore (0 registrations), there are no clinical trials registered specifically against this disease label, and key safety/labeling data are missing — so this should proceed only under guardrails addressing regulatory and safety data gaps rather than mechanistic uncertainty.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings, contraindications, and drug-drug interaction data (DG001 — blocking)
- Formal DrugBank/manufacturer mechanism-of-action documentation (DG002)
- Singapore/regional regulatory pathway assessment for an orphan-disease ERT with zero current local registrations
- Skeletal-outcome-specific clinical evidence (e.g., dysostosis multiplex endpoints, bone mineral density, radiographic progression) beyond the existing general MPS I ERT trial base

*For context: nine additional TxGNN-predicted candidates for laronidase were also screened in this evidence pack (e.g., Sanfilippo syndrome, lysosomal disease with hypertrophic cardiomyopathy, and several congenital ophthalmologic/craniofacial syndromes). All were assessed as mechanistically implausible or unsupported by any literature/trial evidence and are recommended for **Hold**.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

