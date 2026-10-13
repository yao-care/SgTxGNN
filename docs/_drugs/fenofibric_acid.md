---
layout: default
title: Fenofibric Acid
parent: Low Evidence (L5)
nav_order: 423
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

# Fenofibric Acid: From Hyperlipidemia to Hyperlipoproteinemia

## One-Sentence Summary

Fenofibric acid is a lipid-lowering drug originally used for hypertriglyceridemia and hyperlipidemia.
The TxGNN model predicts it may be effective for **hyperlipoproteinemia** (the top-ranked prediction, cholesterol-ester transfer protein deficiency, has no supporting evidence, so the best-supported candidate, hyperlipoproteinemia, is evaluated here).
Evidence is limited to **1 clinical trial** (non-phase, status unknown) and **3 publications**, and this indication largely overlaps with the already-approved use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridemia, hyperlipidemia, familial hyperlipidemia, familial combined hyperlipidemia, hypoalphalipoproteinemia (approved indication text is not available in the Singapore licence records) |
| Predicted New Indication | Top-ranked by TxGNN: cholesterol-ester transfer protein deficiency (evaluated in detail: hyperlipoproteinemia, rank 2) |
| TxGNN Prediction Score | 97.85% (cholesterol-ester transfer protein deficiency); 97.73% (hyperlipoproteinemia) |
| Evidence Level | L5 (cholesterol-ester transfer protein deficiency); L4 (hyperlipoproteinemia) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold (top-ranked indication); Hyperlipoproteinemia: Research Question, better regarded as a label-scope extension |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, fenofibric acid is a PPAR-alpha agonist. PPAR-alpha activation increases lipoprotein lipase activity and reduces hepatic VLDL production, which lowers triglycerides and modestly raises HDL-C.

**Hyperlipoproteinemia (rank 2)** is closely related to the approved indications (hyperlipidemia, hypertriglyceridemia, mixed dyslipidemia), so the mechanism plausibly applies. Because the overlap with the marketed use is large, this is better viewed as a label-scope extension than as true repurposing.

**Cholesterol-ester transfer protein deficiency (rank 1)** is a poor mechanistic fit. This condition is characterized by markedly elevated HDL-C, so a drug that mainly lowers triglycerides is not an obvious treatment. The high score likely reflects proximity to lipid-metabolism nodes in the knowledge graph rather than a defined mechanism.

Other predicted indications were also reviewed:
- **Familial hypercholesterolemia and autosomal dominant hypercholesterolemia:** Fibrates have only modest LDL-C effects. A preclinical study suggests fibrates repress PCSK9, which could theoretically help, but this is indirect. Any use would be adjunctive to statins, ezetimibe or PCSK9 inhibitors.
- **Homozygous familial hypercholesterolemia:** LDL receptor function is absent or severely reduced, so benefit is unlikely.
- **Hypolipoproteinemia:** The drug's direction of effect is opposite to a plausible benefit, so this is likely a graph artifact.
- **Hepatic lipase deficiency hyperlipidemia, CYP7A1 deficiency, hepatopulmonary syndrome and idiopathic copper-associated cirrhosis:** Mechanisms are speculative, with no supporting evidence. The last two are also concerning given hepatic safety considerations.

## Clinical Trial Evidence

Evidence for hyperlipoproteinemia (rank 2). No clinical trials are registered for the top-ranked indication, cholesterol-ester transfer protein deficiency.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01974297](https://clinicaltrials.gov/study/NCT01974297) | NA | Unknown | 194 | Compared atorvastatin/fenofibric acid 10/135 mg combination with atorvastatin 20 mg monotherapy in mixed hyperlipidemia not at lipid goals on atorvastatin 10 mg. No results provided. |

## Literature Evidence

Evidence for hyperlipoproteinemia (rank 2). The same papers also support the familial and autosomal dominant hypercholesterolemia predictions. No literature is available for cholesterol-ester transfer protein deficiency.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9174678](https://pubmed.ncbi.nlm.nih.gov/9174678/) | 1997 | Cohort | Eur J Clin Pharmacol | Relationship between plasma fenofibric acid levels and lipid changes (cholesterol, LDL-C, apoB) in patients with primary type IIA/IIB hyperlipoproteinemia |
| [7208345](https://pubmed.ncbi.nlm.nih.gov/7208345/) | 1980 | Review | La Nouvelle Presse Medicale | Pharmacology of fenofibrate. Active against the main types of hyperlipoproteinemia (IIa, IIb, IV), with sustained activity over 20 months in one study |
| [18245819](https://pubmed.ncbi.nlm.nih.gov/18245819/) | 2008 | Preclinical/Mechanistic | J Biol Chem | PPAR-alpha activation counteracts statin-induced PCSK9 induction (dual mechanisms of fibrate-mediated PCSK9 repression) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14375P | Trilipix Modified Release Capsules 45mg | Capsule, delayed release pellets (oral) | Not available in the records |
| SIN14376P | Trilipix Modified Release Capsules 135mg | Capsule, delayed release pellets (oral) | Not available in the records |

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** liver failure and liver disease, pancreatitis, gallbladder disease, thrombocytopenia, hypothyroidism, myopathy and other muscle disease, rhabdomyolysis, diabetes mellitus and diabetic ketoacidosis, anemia, impaired renal function, and leukopenia and neutropenia (including several congenital forms).
- **Drug Interactions:** 43 interactions were identified.
  - **Major:** rosuvastatin, simvastatin.
  - **Moderate (examples):** insulins (aspart, degludec, detemir, glargine, glulisine, human), sulfonylureas (chlorpropamide, glimepiride, glipizide, glyburide, tolazamide, acetohexamide), meglitinides (nateglinide, repaglinide), chenodeoxycholic acid, naltrexone.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, cholesterol-ester transfer protein deficiency). Hyperlipoproteinemia may be carried forward as a **Research Question** (label-scope extension).

**Rationale:**
- The top-ranked prediction has no trials or literature, and its mechanism does not fit, since the condition already involves high HDL-C. For hyperlipoproteinemia, the evidence is one non-phase trial with unknown status plus pharmacology literature, with no Phase 2/3 RCT. Because it overlaps with the marketed use, true repurposing value is limited.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (a blocking gap for safety screening) and the approved indication text for both licences
- Detailed mechanism of action data from DrugBank
- Phase 2/3 RCT evidence for fenofibric acid alone (not only combinations) in hyperlipoproteinemia
- A review of the major interactions with statins (rosuvastatin, simvastatin) and with glucose-lowering drugs, plus a risk plan for patients with liver, renal or muscle disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

