---
layout: default
title: Fenofibric Acid
parent: Low Evidence (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
---

# Fenofibric Acid
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

# Fenofibric Acid: From Its Registered Use (Indication Not Recorded) to Cholesterol-Ester Transfer Protein Deficiency

## One-Sentence Summary

Fenofibric acid is the active form of fenofibrate, a lipid-lowering fibrate. It is marketed in Singapore as Trilipix, but the record does not state the approved indication.
The TxGNN model ranks **cholesterol-ester transfer protein (CETP) deficiency** first (97.85%), yet **no clinical trials or publications** support this prediction. Among the other predictions, **hyperlipoproteinemia** has the most support (1 trial, 20 publications), but this is likely close to the drug's existing use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available data |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 97.85% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Fenofibric acid is a PPAR-alpha agonist. It increases lipoprotein lipase activity, lowers triglycerides and VLDL, modestly lowers LDL-C and raises HDL-C. Detailed mechanism-of-action data are not available in the drug record, so this description comes from the candidate analysis.

The link to CETP deficiency is weak. CETP deficiency is already a high-HDL, low-LDL state, so lowering lipids is not an obvious treatment goal. The prediction appears to come from shared lipid-metabolism neighbours in the knowledge graph, not from a treatment rationale. It should be treated as a model artefact until shown otherwise.

## Other Predicted Indications

| Rank | Disease | Score | Evidence Level | Decision | Comment |
|---|---|---|---|---|---|
| 2 | Hyperlipoproteinemia | 97.73% | L3 | Proceed with Guardrails | Best supported, but the label may already cover it. Verify before calling it repurposing. |
| 3 | Hyperlipidemia due to hepatic triglyceride lipase deficiency | 97.03% | L5 | Hold | No evidence that fibrates correct hepatic lipase deficiency. |
| 4 | Familial hypercholesterolemia | 96.99% | L3 | Research Question | Small, old fenofibrate studies with surrogate lipid endpoints only. |
| 5 | Homozygous familial hypercholesterolemia | 96.67% | L4 | Hold | One indirect study. PPAR-alpha effects are unlikely to help in severe LDL-receptor deficiency. |
| 6 | Hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency | 96.58% | L5 | Hold | Fibrates increase biliary cholesterol saturation, a theoretical concern in this bile acid defect. |
| 7 | Hypercholesterolemia, autosomal dominant | 94.49% | L3 | Research Question | Largely the same evidence as familial hypercholesterolemia, not independent support. |
| 8 | Hypolipoproteinemia | 88.24% | L5 | Hold | Lowering lipoproteins further has no therapeutic rationale and may be counterproductive. |
| 9 | Hepatopulmonary syndrome | 87.22% | L5 | Hold | Speculative anti-inflammatory and vascular rationale only. |
| 10 | Idiopathic copper-associated cirrhosis | 87.22% | L5 | Hold | Speculative link, and fibrate hepatotoxicity in cirrhosis is a concern. |

## Clinical Trial Evidence

For the headline prediction (CETP deficiency): Currently no related clinical trials registered.

For the best-supported prediction (hyperlipoproteinemia):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01974297](https://clinicaltrials.gov/study/NCT01974297) | NA | Unknown | 194 | Atorvastatin 20 mg alone vs atorvastatin/fenofibric acid 10/135 mg in mixed hyperlipidemia not at goal on atorvastatin 10 mg. No results available. |

## Literature Evidence

For the headline prediction (CETP deficiency): Currently no related literature available.

For hyperlipoproteinemia, the 10 most relevant of 20 publications are listed below. All studied fenofibrate (the prodrug), not fenofibric acid itself, and none is a Phase 2/3 RCT.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9174678](https://pubmed.ncbi.nlm.nih.gov/9174678/) | 1997 | Clinical study (PK/PD) | Eur J Clin Pharmacol | Examined how plasma fenofibric acid levels relate to lipid changes in type IIA/IIB hyperlipoproteinemia. |
| [3436157](https://pubmed.ncbi.nlm.nih.gov/3436157/) | 1987 | Double-blind study | Curr Med Res Opin | Bezafibrate vs fenofibrate in 64 type II diabetics with hyperlipoproteinemia over 4 months. |
| [3902379](https://pubmed.ncbi.nlm.nih.gov/3902379/) | 1985 | Randomised comparative study | Curr Med Res Opin | Bezafibrate vs fenofibrate in 40 patients with primary hyperlipoproteinemia over 4 months. |
| [3994783](https://pubmed.ncbi.nlm.nih.gov/3994783/) | 1985 | Double-blind comparative study | Atherosclerosis | Ciprofibrate and fenofibrate both lowered total, LDL and VLDL cholesterol and apoB, and raised HDL. |
| [7225166](https://pubmed.ncbi.nlm.nih.gov/7225166/) | 1981 | Clinical study | Atherosclerosis | Dose-response study in 56 patients, with comparison against clofibrate. Elevated lipoproteins fell in each type. |
| [3282894](https://pubmed.ncbi.nlm.nih.gov/3282894/) | 1988 | Clinical study | Eur J Clin Pharmacol | Single daily 200 mg dose was effective and well tolerated in 12 type IIB patients. |
| [6428905](https://pubmed.ncbi.nlm.nih.gov/6428905/) | 1984 | Clinical study | Eur J Clin Invest | Serum lipids fell, but the lithogenic index of bile rose, a gallstone-related signal. |
| [18245819](https://pubmed.ncbi.nlm.nih.gov/18245819/) | 2008 | Preclinical mechanistic | J Biol Chem | Fibrates repress PCSK9 through dual mechanisms, and PPAR-alpha activation counteracts statin-induced PCSK9. |
| [7208345](https://pubmed.ncbi.nlm.nih.gov/7208345/) | 1980 | Review | Nouv Presse Med | Pharmacology overview. Fenofibrate is active against types IIa, IIb and IV hyperlipoproteinemia. |
| [9666952](https://pubmed.ncbi.nlm.nih.gov/9666952/) | 1998 | Clinical study (indirect) | QJM | Atorvastatin compared with simvastatin-fenofibrate and simvastatin-cholestyramine in familial hypercholesterolaemia. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14375P | Trilipix Modified Release Capsules 45mg | Capsule, delayed release pellets | Not listed in the record |
| SIN14376P | Trilipix Modified Release Capsules 135mg | Capsule, delayed release pellets | Not listed in the record |

Both products are oral and made by Fournier Laboratories Ireland Limited and Mylan Laboratories SAS.

## Safety Considerations

Please refer to the package insert for safety information.

Two points from the literature and candidate analysis are worth noting. Fibrates can increase the lithogenic index of bile (PMID 6428905). Hepatotoxicity is a concern in cirrhosis.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The headline prediction, CETP deficiency, rests on model score alone (L5). It has no trials or literature, and the biology argues against a therapeutic benefit. The related prediction of hyperlipoproteinemia has more support, but it consists of small, old fenofibrate studies and one trial with unknown status and no results. This is probably not true repurposing.

**To proceed, the following is needed:**
- The Singapore package insert, to confirm approved indications, warnings and contraindications
- Confirmation of whether hyperlipoproteinemia is already on the label
- Detailed mechanism-of-action data from DrugBank
- Any fenofibric acid-specific efficacy data, if hyperlipoproteinemia or familial hypercholesterolemia is pursued
- A clinical rationale, if CETP deficiency is to be considered further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

