---
layout: default
title: Penicillamine
parent: Low Evidence (L5)
nav_order: 774
evidence_level: L5
indication_count: 10
---

# Penicillamine
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

# Penicillamine: From Rheumatoid Arthritis and Wilson Disease to Megaloblastic Anemia

## One-Sentence Summary

Penicillamine is a copper and cystine chelator, originally used for conditions such as Wilson disease, cystinuria and rheumatoid arthritis.
The TxGNN model predicts it may be effective for **megaloblastic anemia** (top-ranked prediction), but **no clinical trials and no publications** support this prediction, and the proposed link is most likely a network artifact.
Overall evidence is **model prediction only**, so the recommendation is to hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, cystinuria, Wilson disease and other metabolic conditions (the approved indication text on the Singapore licence is blank) |
| Predicted New Indication | Megaloblastic anemia |
| TxGNN Prediction Score | 98.02% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, penicillamine is a thiol-based chelator that binds copper and cystine and also has immunomodulatory effects. Its efficacy in Wilson disease, cystinuria and rheumatoid arthritis is established.

For megaloblastic anemia, however, no plausible mechanistic link was found. This condition is driven by vitamin B12 or folate deficiency, which copper chelation does not address. Penicillamine can also cause haematological toxicity, including marrow suppression, so the high TxGNN score (0.98) most likely reflects network proximity in the knowledge graph rather than true therapeutic potential.

Among the other top-ranked predictions, the most credible signals are indirect and also weak:
- **Tricarboxylic acid cycle disorder (score 93.5%, L4):** only an indirect link through copper homeostasis and cuproptosis, supported by mechanistic reviews. No study tests penicillamine in this setting.
- **Disease of transporter activity (score 93.0%, L4):** this category includes Wilson disease, which is already an established indication, so it is not a true repurposing signal. The Phase 3 CHELATE trial in the literature used penicillamine as the comparator.
- **Glycogen branching enzyme deficiency forms, adult polyglucosan body disease, X-linked chronic granulomatous disease, G6PD-deficiency haemolytic anemia and others:** prediction only, with no supporting mechanism or clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No publications were found for megaloblastic anemia. The table below lists the most relevant items retrieved for the second- and third-ranked predictions, for context only. None tests penicillamine in a new indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36183738](https://pubmed.ncbi.nlm.nih.gov/36183738/) | 2022 | RCT | Lancet Gastroenterol Hepatol | CHELATE: Phase 3 non-inferiority trial of trientine tetrahydrochloride versus penicillamine for maintenance therapy in Wilson disease (existing indication) |
| [29625923](https://pubmed.ncbi.nlm.nih.gov/29625923/) | 2018 | Review | Clin Res Hepatol Gastroenterol | Wilson disease update: copper accumulation in liver and brain, effective lifelong treatments |
| [39420162](https://pubmed.ncbi.nlm.nih.gov/39420162/) | 2024 | Review | Drugs | Trientine tetrahydrochloride development, built on experience in penicillamine-intolerant patients |
| [37150036](https://pubmed.ncbi.nlm.nih.gov/37150036/) | 2023 | Review | Biomed Pharmacother | Cuproptosis: copper binding to lipoylated TCA-cycle enzymes and relevance to cardiovascular disease |
| [42551357](https://pubmed.ncbi.nlm.nih.gov/42551357/) | 2026 | Review | J Trace Elem Med Biol | Copper homeostasis and cuproptosis in metabolic diseases |
| [18568852](https://pubmed.ncbi.nlm.nih.gov/18568852/) | 2008 | Review | Crit Rev Clin Lab Sci | Comprehensive review of Wilson disease diagnosis |
| [39147330](https://pubmed.ncbi.nlm.nih.gov/39147330/) | 2024 | Preclinical (animal) | Biochem Pharmacol | Melatonin alleviates brain injury in copper-laden rats; penicillamine and zinc gluconate noted as current therapies |
| [5644093](https://pubmed.ncbi.nlm.nih.gov/5644093/) | 1968 | Observational | Am J Med | Effect of D-penicillamine and diet on plasma cystine in cystinosis |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08173P | CUPRIPEN 250 CAPSULE 250 mg (Laboratorios Rubio SA) | Capsule (oral) | Not stated in the data compiled for this report |

---

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from drug-disease relationships in the knowledge graph, not from package insert text):
- Blood disorders: thrombocytopenia, leukopenia, agranulocytosis, neutropenia (including congenital forms), aplastic anemia, iron deficiency anemia and other deficiency anemias
- Kidney disorders: kidney disease, glomerulonephritis
- Neuromuscular and autoimmune conditions: myasthenia gravis, neuromuscular junction disease, pemphigus
- Oral and skin conditions: aphthous stomatitis (canker sore), Rowell syndrome
- Other: pyoureter

The haematological entries are particularly relevant to the predicted indication, because anemia and marrow suppression are themselves concerns with penicillamine. In addition, hemolysis in G6PD deficiency warrants caution.

**Drug Interactions:** 64 interactions are recorded; the 20 shown are all of Moderate severity. They fall mainly into two groups:
- Calcium, magnesium and aluminium products and antacid-type agents (e.g. calcium carbonate, calcium acetate, magnesium oxide, aluminium hydroxide, kaolin, attapulgite, magaldrate)
- Zinc and iron products (zinc sulfate, zinc acetate, iron)

These are typically chelation or absorption interactions, so separating the timing of doses is likely to be relevant.

For warnings and full contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for megaloblastic anemia is high (98.02%), but there are no clinical trials or publications, and no plausible mechanism links a copper and cystine chelator to a B12/folate deficiency anemia. Penicillamine itself carries haematological toxicity, which argues against benefit. Evidence is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for penicillamine, to allow a proper mechanistic-link analysis
- The package insert warnings and contraindications from HSA, to complete safety screening
- Any mechanistic or preclinical evidence supporting penicillamine in the predicted indication
- If the project wants a more credible lead, a focused review of the tricarboxylic acid cycle disorder direction (copper/cuproptosis), which has indirect mechanistic support but no direct testing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

