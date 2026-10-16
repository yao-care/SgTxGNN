---
layout: default
title: Procaine
parent: Medium Evidence (L3-L4)
nav_order: 827
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Procaine: predicted new indication Methemoglobinemia (evidence level L4). Approved use: Not stated in the Singapore licence record (a local anaesthetic by dr…"
monitor_inn: "Procaine"
predicted_indications: ["methemoglobinemia", "methemoglobinemia, alpha type", "Tourette syndrome", "anaphylaxis", "methemoglobin reductase deficiency", "hyperthyroidism", "fibromyalgia", "tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa"]
---

# Procaine
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

# Procaine: From Local Anaesthesia to Methemoglobinemia (Top TxGNN Prediction)

## One-Sentence Summary

Procaine is a local anaesthetic, and its only Singapore registration is a 2% topical lotion.
The TxGNN model's top-ranked prediction is **methemoglobinemia**, but the published literature describes procaine as a *cause* of this condition rather than a treatment. No clinical trials support the prediction, and the **5 publications** found are case reports, a review, and observational or pharmacokinetic studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence record (a local anaesthetic by drug class) |
| Predicted New Indication | Methemoglobinemia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Procaine is an ester-type local anaesthetic. Its anaesthetic effect is generally attributed to sodium channel blockade, although the data compiled for this report did not confirm a primary molecular target. Pharmacology records list ryanodine receptors (RyR1 and RyR2) as related targets, without supporting bioactivity data.

The prediction is **not mechanistically reasonable as a therapy**. The literature links procaine, like lignocaine, to *inducing* methemoglobinemia, including a case of methemoglobinemia after intravenous procaine and a clinical observation of methemoglobin levels under intravenous procaine anaesthesia. Aromatic amine metabolites of local anaesthetics can oxidise haemoglobin iron. The high TxGNN score most likely reflects a drug-disease association in the knowledge graph, such as drug-induced methemoglobinemia, and not therapeutic potential. This should be treated as a **safety signal**, not a repurposing opportunity.

The same applies to the related predictions "methemoglobinemia, alpha type" and "methemoglobin reductase deficiency", which have no supporting evidence. In the latter, procaine could be harmful.

### Other Predictions Worth Noting

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Fibromyalgia | 99.23% | L4 | Only uncontrolled 1950s-60s reports of procaine infiltration for fibrositic or myofascial pain. Plausible mechanism (nociceptive blockade at trigger points). A reasonable research question. |
| Tendinitis | 99.20% | L3 | The most relevant signal is a 2022 clinical study of 1% procaine neural therapy in supraspinatus tendinopathy. Other items are indirect or involve non-procaine agents. A reasonable research question. |
| Anaphylaxis | 99.29% | L4 | Literature documents procaine, including procaine penicillin, as a cause of allergic and pseudo-allergic reactions (e.g. Hoigné's syndrome). Adverse, not therapeutic. |
| Hyperthyroidism | 99.25% | L4 | Old, low-quality reports (1945-1976) on procaine block or injection therapy. No modern evidence. |
| Tourette syndrome, idiopathic granulomatous myositis, myositis fibrosa | 99.34%, 99.18%, 99.18% | L5 | Model prediction only. No trials or literature. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for methemoglobinemia (or for any of the top 10 predicted indications).

---

## Literature Evidence

Publications for the top prediction, methemoglobinemia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Clinical observational study | Zhonghua Wai Ke Za Zhi | Effect of intravenous procaine anaesthesia on methemoglobin levels (no abstract available). |
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Case report | Acta Physiol Latino Am | Methemoglobinemia caused by intravenous procaine. |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Case report | Lancet | Methaemoglobinaemia following lignocaine, a related local anaesthetic. |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Review | Drugs | General review of the rational use of local anaesthetics. |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | Pharmacokinetic study | Am J Obstet Gynecol | Passage of procaine and para-aminobenzoic acid across the human placenta. |

For the most relevant modern signal in a secondary prediction (tendinitis):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35480510](https://pubmed.ncbi.nlm.nih.gov/35480510/) | 2022 | Clinical study | Pak J Med Sci | Effect of 1% procaine injection (neural therapy) on shoulder pain and dysfunction in supraspinatus tendinopathy. |
| [23494116](https://pubmed.ncbi.nlm.nih.gov/23494116/) | 2013 | RCT | Arch Orthop Trauma Surg | Corticosteroid vs. local anaesthetic injection in lateral epicondylitis (comparator not procaine-specific). |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09166P | PROCANOL LOTION 2% | Lotion | Not stated in the licence record |

The licence is a valid single-ingredient product (manufacturer: ICM Pharma Pte. Ltd.).

---

## Safety Considerations

- **Drug Interactions**: 17 interaction records were compiled. One is rated **Major**: nitrous acid. Most others are **Moderate**, mainly with other local anaesthetics (lidocaine, benzocaine, cocaine, tetracaine, oxybuprocaine, cinchocaine) and with sulfasalazine. Minor interactions include laronidase, hyaluronidase, and doxorubicin (including liposomal).
- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): long QT syndrome and torsades de pointes, atrioventricular block, cardiovascular and heart disease, kidney and liver disease, gallbladder disease, thrombocytopenia, systemic lupus erythematosus, myasthenia gravis and neuromuscular junction disease, butyrylcholinesterase deficiency, potassium deficiency, hypotensive disorder, agranulocytosis and neutropenia (including congenital forms), and Clostridium difficile colitis.
- **Literature-derived signals**: methemoglobinemia after procaine, and allergic or pseudo-allergic reactions (e.g. anaphylaxis, contact dermatitis, Hoigné's syndrome), mostly with procaine penicillin.

Please refer to the package insert for authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, methemoglobinemia, is an adverse effect of procaine and not a therapeutic target, so it is a safety signal rather than a repurposing opportunity. Evidence for the other predictions is old, uncontrolled, or absent. Tendinitis and fibromyalgia are the only plausible candidates, and they are better treated as research questions than as repurposing decisions.

**To proceed, the following is needed:**
- The HSA package insert, to confirm warnings, contraindications, and the approved indication for the licensed lotion.
- Detailed mechanism of action data.
- For tendinopathy or fibromyalgia: a controlled comparative study against lidocaine or other local anaesthetics, using a procaine formulation and route registered in Singapore (the only licence is a topical lotion).
- A formal methemoglobinemia risk assessment, including monitoring in patients with methemoglobin reductase deficiency.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

