# Cladribine: From Hairy Cell Leukemia to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analog approved for the treatment of hairy cell leukemia (and more recently, relapsing multiple sclerosis), acting via selective intracellular accumulation in lymphoid cells.
The TxGNN model predicts it may be effective for **Parameningeal Embryonal Rhabdomyosarcoma**, a rare pediatric soft tissue sarcoma,
with **no clinical trials** and **no relevant publications** currently supporting this direction — representing the lowest possible level of evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hairy cell leukemia (per DrugBank DB00242; no Singapore HSA registration found) |
| Predicted New Indication | Parameningeal Embryonal Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (data gap DG002). Based on established pharmacological knowledge, Cladribine is a purine nucleoside analog selectively phosphorylated by deoxycytidine kinase (dCK) — an enzyme highly expressed in lymphocytes and monocytes but expressed at much lower levels in most solid tumor cells. Once phosphorylated, Cladribine accumulates intracellularly as cladribine triphosphate, causing DNA strand breaks, inhibiting DNA repair, and triggering apoptosis. This lymphocyte-selective mechanism underpins its proven efficacy in hairy cell leukemia and its immunomodulatory role in multiple sclerosis.

Rhabdomyosarcoma (RMS) is a mesenchymal tumor of skeletal muscle origin — biologically and mechanistically distant from lymphoid malignancies. The mechanistic prerequisite for cladribine activity, namely high dCK expression in tumor cells, is not met in RMS. Published data indicate that dCK expression in RMS cell lines is far below that of lymphoid cells, meaning cladribine is unlikely to be phosphorylated and retained at cytotoxic concentrations within RMS tumor tissue.

The high TxGNN score (99.77%) most likely reflects broad topological connectivity within the knowledge graph between antineoplastic agents and malignancy-related nodes, rather than any direct pharmacological rationale. In practical terms, the model recognizes Cladribine as an anticancer drug and parameningeal embryonal RMS as a cancer — but this structural graph similarity does not translate to a biologically sound repurposing hypothesis. No preclinical data (cell line studies, animal models) or clinical reports support this predicted indication across any of the 10 RMS/sarcoma indications in this pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note on search results:** A PubMed query for Cladribine + liver sarcoma (rank #7 predicted indication) retrieved one result — PMID [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/) (Schleyer et al., 2004, *Der Hautarzt*), which describes cladribine use in **smoldering systemic mastocytosis**. This is an unrelated condition and represents a keyword search mismatch; it provides no evidence supporting cladribine in hepatic or mesenchymal sarcomas.

---

## Singapore Market Information

Cladribine (DrugBank DB00242) has no product registrations with Singapore's Health Sciences Authority (HSA) and is currently not marketed in Singapore.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|-------------------|
| — | (No registered products) | — | — |

---

## Cytotoxicity

Cladribine is a cytotoxic antineoplastic agent belonging to the purine nucleoside analog class. The following assessment is based on class-level pharmacological knowledge, as package insert data was not available in this Evidence Pack (data gap DG001).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Purine nucleoside analog |
| Myelosuppression Risk | High — severe neutropenia, thrombocytopenia, and anaemia are dose-limiting; prolonged CD4+ lymphopenia may persist for months to years |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (during and after each treatment cycle), liver and renal function, serum immunoglobulin levels (due to protracted lymphopenia and infection risk) |
| Handling Protection | Must follow cytotoxic drug handling regulations — closed-system drug transfer devices, appropriate PPE required during preparation and administration |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data including key warnings, contraindications, and drug interactions were not available in this Evidence Pack (data gaps DG001). Package insert retrieval from the relevant regulatory authority is required before any clinical use assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications in this Evidence Pack are rated L5 (model prediction only), with zero supporting clinical trials and no relevant published literature. More critically, Cladribine's mechanism of action — lymphocyte-selective dCK-dependent intracellular phosphorylation — does not align with the biology of rhabdomyosarcoma or any of the other mesenchymal/solid tumor indications predicted. The TxGNN high scores reflect knowledge graph topology rather than pharmacological plausibility.

**To proceed, the following is needed:**

- **Mechanistic feasibility assessment:** Measure dCK expression levels in established RMS cell lines (e.g., RD, Rh30) by Western blot or RNA-seq to determine whether the metabolic activation prerequisite is met
- **In vitro cytotoxicity screen:** If dCK expression is detectable, conduct IC₅₀ assays of cladribine in RMS cell lines as a minimal preclinical validation step
- **MOA data retrieval:** Query DrugBank API to obtain full mechanism of action annotation (data gap DG002)
- **Safety data retrieval:** Download and parse the originator package insert to capture key warnings and contraindications (data gap DG001)
- **Evidence gap review:** Conduct a dedicated PubMed search combining "cladribine" with "rhabdomyosarcoma" or "soft tissue sarcoma" using MeSH terms to confirm absence of any case reports or experimental data not captured by the current automated query