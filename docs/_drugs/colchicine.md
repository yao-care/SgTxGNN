---
layout: default
title: Colchicine
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
---

# Colchicine
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

# Colchicine: From Gout to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine is a long-established anti-inflammatory agent primarily used to treat acute gout attacks, Familial Mediterranean Fever (FMF), and recurrent pericarditis.
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**, with **0 clinical trials** and **6 publications** (all in vitro or basic science studies) currently supporting this direction.
Evidence is limited to preclinical mechanistic data, placing this prediction at an early exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout; autoinflammatory conditions (no Singapore regulatory data available — drug not registered) |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Colchicine's hallmark mechanism is binding to β-tubulin and inhibiting microtubule polymerisation. This disrupts cell division, neutrophil chemotaxis, and — through downstream effects on cytoskeletal scaffolding — NLRP3 inflammasome activation. Although DrugBank pharmacology data was not retrieved in this evidence pack, Colchicine's tubulin-targeting action is one of the most well-characterised small-molecule mechanisms in clinical pharmacology.

*Plasmodium falciparum* depends on a functional tubulin/microtubule system for intraerythrocytic cell division and gametocyte formation. Several in vitro studies from the late 1980s–1990s demonstrated that compounds binding to cytoskeletal proteins — including colcemid (a structural congener of Colchicine) and tubulozole isomers with colcemid-like effects on protein synthesis — inhibit P. falciparum growth in erythrocyte cultures. This body of work established parasite tubulin as a pharmacologically tractable target and provides indirect mechanistic support for the TxGNN prediction.

Critically, P. falciparum tubulins are structurally distinct from mammalian tubulins at the molecular level. This divergence may offer selectivity, but it also means Colchicine's affinity and potency against the parasite — and its therapeutic index in an in vivo malaria context — are entirely unknown. Colchicine carries a narrow therapeutic window in humans, and there are currently no clinical or animal model data to establish whether an effective antimalarial dose is safe. The TxGNN model likely identified this candidate based on pharmacological graph similarities, not direct experimental evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In Vitro Study | Cell Biology International Reports | Nine tubulin-binding substances tested against intraerythrocytic P. falciparum; parasite tubulins appear molecularly distinct from mammalian tubulins; tubulozole-T showed promising selective antimalarial activity |
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | In Vitro Study | Cell Biology International Reports | Duplicate report of the same cytoskeletal compound screen; colchicine-class agents active in vitro with differential host vs. parasite selectivity noted |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In Vitro Study | Antimicrobial Agents and Chemotherapy | Tubulozole isomers (mechanism resembling colcemid) inhibit P. falciparum protein synthesis; colcemid itself shows analogous effect, providing indirect support for the colchicine-related mechanism |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In Vitro Study | PLoS ONE | Curcumin (a structurally distinct tubulin binder) disrupts P. falciparum microtubule architecture in vitro, further validating parasite tubulin as a druggable target |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In Vitro / Molecular | Molecular and Cellular Biology | pfmdr1-encoded Pgh1 expressed in mammalian cells increases chloroquine susceptibility; provides background context on P. falciparum drug resistance mechanisms relevant to any repurposing candidate |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Serological Study | Clinical and Experimental Immunology | Anti-intermediate filament antibodies detected in 82% of acute malaria patients; supports the concept that cytoskeletal disruption is a biologically significant feature of P. falciparum infection |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Colchicine has a well-known narrow therapeutic window. Toxicity data (warnings, contraindications, drug–drug interactions) was not retrieved in this evidence pack. Before any research use in malaria settings, a full safety profile review — particularly regarding renal and hepatic dose adjustments, CYP3A4/P-gp interactions, and myelosuppression risk — is essential.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
All supporting evidence is limited to in vitro and basic science studies from the 1980s–2010s; no clinical trials have been registered, and there are no animal model or pharmacokinetic data to define whether an effective antimalarial dose of Colchicine is achievable within its narrow therapeutic window. This indication cannot advance beyond hypothesis generation at this stage.

**To proceed, the following is needed:**

- Retrieve full MOA and safety profile from DrugBank (DG001, DG002 data gaps must be resolved)
- In vitro selectivity studies: determine IC₅₀ against P. falciparum versus host erythrocyte/hepatocyte toxicity to establish a preliminary therapeutic index
- Rodent malaria model (e.g., P. berghei) proof-of-concept study to confirm in vivo efficacy and tolerability
- Pharmacokinetic modelling to assess whether oral Colchicine achieves adequate parasite-inhibiting concentrations in blood without systemic toxicity
- Comparative assessment against current first-line antimalarials (artemisinin-based combination therapies) to define potential niche (e.g., transmission-blocking via gametocyte inhibition)
- Singapore regulatory pathway assessment if preclinical data becomes supportive (note: currently not registered with HSA)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

