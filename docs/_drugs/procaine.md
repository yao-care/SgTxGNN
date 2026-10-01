---
layout: default
title: Procaine
parent: Low Evidence (L5)
nav_order: 818
evidence_level: L5
indication_count: 10
---

# Procaine
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

# Procaine: From Local Anaesthesia to Methemoglobinemia

## One-Sentence Summary

Procaine is an ester-type local anaesthetic, and the only Singapore product is a 2% topical lotion. The TxGNN model ranks **methemoglobinemia** as its top prediction, but the supporting literature (**0 clinical trials, 8 publications**) shows procaine *causing* methemoglobinemia, not treating it. This is most likely a drug-adverse-effect association, not a therapeutic one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anaesthesia (drug class; no indication text in the Singapore registration record) |
| Predicted New Indication | Methemoglobinemia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 (case reports and observational data only, all pointing to harm, not benefit) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Procaine is a local anaesthetic of the ester class, and its efficacy as a local anaesthetic is well established. Nothing in the data suggests a mechanism by which it would treat methemoglobinemia.

The retrieved literature points the other way. Case reports describe methemoglobinemia after intravenous procaine in adults and after subcutaneous procaine infiltration in a newborn. A 1987 observational study examined the effect of intravenous procaine anaesthesia on methemoglobin levels, and a 1965 report describes the same problem with lignocaine. The high TxGNN score therefore likely reflects a drug-induced adverse-effect link in the knowledge graph. It should be read as a safety signal, not a repurposing opportunity.

The other top-ranked predictions follow a similar pattern. Alpha-type methemoglobinemia and methemoglobin reductase deficiency are closely related conditions, so they are more likely safety concerns than treatment targets. Fibromyalgia and tendinitis are the two predictions with a plausible therapeutic rationale (see Conclusion).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Case report | Acta Physiol Latinoam | Methemoglobinemia due to intravenous procaine (an adverse effect) |
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Observational study | Zhonghua Wai Ke Za Zhi | Effect of intravenous procaine anaesthesia on methemoglobin levels |
| [705003](https://pubmed.ncbi.nlm.nih.gov/705003/) | 1978 | Case report | Rev Esp Anestesiol Reanim | Methemoglobinemia in a newborn after subcutaneous procaine (novocaine) infiltration during general anaesthesia |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Case report | Lancet | Methemoglobinemia following lignocaine, a related local anaesthetic |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Review | Drugs | Rational use of local anaesthetics (general background) |
| [5118947](https://pubmed.ncbi.nlm.nih.gov/5118947/) | 1971 | Review | Laval Med | Overview of local anaesthetics (general background) |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | Pharmacokinetic study | Am J Obstet Gynecol | Placental passage of procaine and para-aminobenzoic acid (not directly relevant) |
| [6745527](https://pubmed.ncbi.nlm.nih.gov/6745527/) | 1984 | Review | Fundam Appl Toxicol | Toxicological interactions of organophosphate insecticides (not directly relevant) |

None of these publications reports a therapeutic benefit of procaine in methemoglobinemia.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09166P | PROCANOL LOTION 2% (ICM Pharma Pte. Ltd.) | Lotion | Not stated in the registration record |

The only registered form is a topical lotion. The methemoglobinemia reports involve intravenous or infiltration use, so any extrapolation across routes would need separate justification.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found for procaine in the queried database.
- **Signals from the retrieved literature** (not from the package insert):
  - Methemoglobinemia, including in a newborn.
  - Hypersensitivity: ester-type local anaesthetics such as procaine are mainly associated with contact dermatitis (type IV). Reactions to procaine-penicillin (e.g., Hoigné's syndrome) are also described.

Please refer to the package insert for key warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is not supported as a treatment. The available evidence shows procaine causing methemoglobinemia, and there are no clinical trials. The TxGNN score appears to reflect a safety association, not therapeutic potential.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (HSA), which are currently missing and block safety screening.
- Mechanism of action data (e.g., from DrugBank).
- A decision on whether to deprioritise methemoglobinemia, alpha-type methemoglobinemia and methemoglobin reductase deficiency as therapeutic targets and handle them as safety flags.
- Consideration of fibromyalgia and tendinitis as research questions. Local procaine injection is mechanistically plausible there. The evidence is a 2022 neural therapy study in supraspinatus tendinopathy and a 2013 comparison of local anaesthetic versus corticosteroid injection in lateral epicondylitis, with no controlled trials for fibromyalgia. Study designs would need verification, and the Singapore lotion would not cover injection routes.

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

