---
layout: default
title: Ursodeoxycholic Acid
parent: Low Evidence (L5)
nav_order: 1036
evidence_level: L5
indication_count: 10
---

# Ursodeoxycholic Acid
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

# Ursodeoxycholic Acid: From Bile Acid-Related Liver and Gallstone Disease to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Ursodeoxycholic acid (UDCA) is a bile acid medicine marketed in Singapore as oral capsules and tablets. The Singapore records supplied here do not state its approved indication, so the original use is taken from general pharmacology (cholestatic liver disease and gallstones) and needs checking against the package insert.
The TxGNN model's top-ranked prediction is **homozygous familial hypercholesterolemia**, but there are **0 clinical trials** and **0 publications** supporting it.
Among the ten predictions, **diabetic nephropathy** has the most coherent supporting evidence, though it is still preclinical only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Singapore records (general use: cholestatic liver disease and gallstones; to be confirmed against the package insert) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, UDCA is a bile acid that changes the bile acid pool and affects intestinal cholesterol absorption. Its efficacy in its original indications is established, but mechanistically it is unlikely to be applicable to homozygous familial hypercholesterolemia.

Homozygous familial hypercholesterolemia is caused by loss of function of the LDL receptor (LDLR). A bile acid effect is unlikely to replace missing LDL receptor activity. No trials or literature were retrieved, so the very high score (99.86%) is not backed by a plausible mechanism. It should be treated as a model artefact until shown otherwise.

The other predictions fall into three groups:

- **Diabetic nephropathy (score 96.7%, evidence level L4):** This is the only prediction with a coherent mechanism. UDCA and its taurine conjugate TUDCA reduce endoplasmic reticulum (ER) stress and podocyte apoptosis, lower oxidative stress, and decrease SGLT2 expression in the kidney. All supporting studies are in cells or animals.
- **COL4A1-related disorders (brain small vessel disease 1 and familial hematuria-retinal arteriolar tortuosity-contractures syndrome):** There is a theoretical chemical-chaperone rationale (reducing ER stress from collagen IV misfolding). It has no drug-specific evidence.
- **Platelet disorders, primary hyperoxaluria, Glanzmann thrombasthenia, and the lipid disorders:** No plausible UDCA mechanism was identified, and no evidence was found.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for homozygous familial hypercholesterolemia. No clinical trials were registered for any of the other nine predicted indications either.

---

## Literature Evidence

Currently no related literature available for homozygous familial hypercholesterolemia.

The strongest literature among the other candidates is for diabetic nephropathy (6 records shown). All are preclinical or observational, and none tests UDCA treatment in humans.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27193377](https://pubmed.ncbi.nlm.nih.gov/27193377/) | 2016 | Preclinical (animal) | Biol Pharm Bull | UDCA, an ER stress inhibitor, reduced oxidative stress and improved diabetic nephropathy in db/db mice |
| [26999661](https://pubmed.ncbi.nlm.nih.gov/26999661/) | 2016 | Preclinical (in vitro/in vivo) | Lab Invest | UDCA and 4-phenylbutyrate prevented ER stress-induced podocyte apoptosis in diabetic db/db mice |
| [22429686](https://pubmed.ncbi.nlm.nih.gov/22429686/) | 2012 | Preclinical (animal) | Diabetes Res Clin Pract | UDCA decreased SGLT2 expression and oxidative stress in the kidneys of diabetic rats |
| [18648192](https://pubmed.ncbi.nlm.nih.gov/18648192/) | 2008 | Preclinical (in vitro) | Am J Nephrol | TUDCA reduced ER stress and apoptosis induced by advanced glycation end products in cultured mouse podocytes |
| [39384774](https://pubmed.ncbi.nlm.nih.gov/39384774/) | 2024 | Cohort (observational) | Nutr Diabetes | Bile acid metabolism is altered step-wise in diabetic kidney disease patients; UDCA treatment was not tested |
| [25360643](https://pubmed.ncbi.nlm.nih.gov/25360643/) | 2014 | Preclinical (mechanistic) | Zhongguo Yi Xue Ke Xue Yuan Xue Bao | ER stress regulates calcineurin expression in podocytes in diabetic nephropathy |

For brain small vessel disease 1, 18 records were retrieved. They are general reviews of ocular and congenital anomalies matched on disease terms, and none mentions UDCA. The only record for hypolipoproteinemia is a case report of fibrinogen storage disease, which does not involve UDCA treatment.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN05742P | URSOFALK CAPSULE 250 mg | Capsule | Losan Pharma GmbH |
| SIN14545P | URSOFALK FILM-COATED TABLETS 500MG | Film-coated tablet | Losan Pharma GmbH |
| SIN16926P | URSOSAN HARD CAPSULES 250 MG | Capsule | PRO.MED.CS Praha a. s. |
| SIN16918P | URSOSAN FORTE FILM-COATED TABLETS 500MG | Film-coated tablet | PRO.MED.CS Praha a. s. |
| SIN15883P | GRINTEROL HARD CAPSULE 250MG | Capsule | Joint Stock Company "Grindeks" |

All products are oral. The records contain no approved indication text.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (homozygous familial hypercholesterolemia) is supported only by a model score. It has no trials, no literature, and no plausible mechanism, since the disease stems from LDL receptor loss of function. The nine other predictions are also at L5 or L4 with no clinical evidence. Diabetic nephropathy (L4) is the only one with a coherent preclinical rationale.

**To proceed, the following is needed:**
- Singapore package insert (HSA) warnings, contraindications, and approved indications. This is a blocking gap for safety screening.
- Mechanism of action data for UDCA (for example from DrugBank).
- Re-prioritisation of diabetic nephropathy as the lead research question. This needs a literature review for human data and a safety assessment, which is feasible given UDCA's long marketed use.
- Remapping of the obsolete disease term "familial combined hyperlipidemia" to a current ontology term before further assessment.
- Route compatibility checks for any candidate moved forward. These are still pending, and the registered forms are oral only.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

