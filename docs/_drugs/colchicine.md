---
layout: default
title: Colchicine
parent: Low Evidence (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
---

# Colchicine
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

# Colchicine: From an Unrecorded Local Indication to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine is a microtubule-targeting anti-inflammatory drug that is marketed in Singapore as oral tablets, but the local records provided do not state its approved indication.
The TxGNN model predicts it may be effective against **Plasmodium falciparum malaria**, but there are **0 clinical trials** and only **laboratory (in vitro) literature**, mostly on related compounds rather than colchicine itself.
This is a research question at this stage, not a repurposing candidate ready for clinical development.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Singapore licence data provided |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% (model rank 5631) |
| Evidence Level | L4 (preclinical / mechanism studies only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Colchicine binds tubulin and disrupts microtubule formation. Detailed mechanism-of-action data was not supplied in the Evidence Pack, so this description rests on the pack's rationale notes. Microtubules are essential to cell division in eukaryotic cells, including the malaria parasite, so a microtubule-binding drug could plausibly affect parasite growth.

Several laboratory studies support this idea indirectly. Papers from 1989 to 2013 report that compounds binding tubulin or other cytoskeletal proteins are active against *P. falciparum* in culture. One of them notes that Colcemid, a close colchicine analogue, affected parasite protein synthesis in a similar way to the antimalarial candidate tubulozoles. Another paper suggests parasite tubulin differs from mammalian tubulin at the molecular level. That is encouraging for selectivity but has not been tested with colchicine here.

The link is indirect and has important limits:
- None of the retrieved papers shows colchicine itself clearing malaria parasites in a clinical or animal setting.
- Colchicine has a narrow therapeutic index, so a systemic antimalarial dose is unlikely to be practical.
- The model's high score reflects graph proximity to related nodes, not direct proof of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

All retrieved papers are laboratory or background studies. None is an RCT, and none tests colchicine directly in malaria.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro | PLoS One | Curcumin (not colchicine) disrupts *P. falciparum* microtubules, building on evidence that tubulin-binding agents can affect the parasite |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro | Antimicrob Agents Chemother | Tubulozoles act on parasite protein synthesis; Colcemid (a colchicine analogue) had a similar effect |
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) / [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | In vitro | Cell Biol Int Rep | Tubulin- and actin-binding compounds were active against *P. falciparum* in culture; plasmodial tubulin appears to differ from mammalian tubulin (two records with the same title) |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro | Mol Cell Biol | Expressing the parasite *pfmdr1* gene in mammalian cells increased chloroquine susceptibility; background on drug resistance, not colchicine |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Other | Clin Exp Immunol | Patients with acute malaria commonly carry antibodies to cytoskeletal intermediate filaments; not a drug study |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN15572P | COLCHICINE HALEWOOD TABLET 500 MCG | Tablet | Surepharm Services Limited |
| SIN12301P | COLCITEX TABLET 0.6 mg | Tablet | The United Drug (1996) Co Ltd |

Both products are oral tablets. The approved indication text is not recorded for either licence.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: colchicine is known to have a narrow therapeutic index, which is a key barrier to any systemic antimalarial use. No drug-interaction records were found in the data provided.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The malaria prediction rests on a high model score and indirect laboratory evidence about other tubulin-binding compounds. There are no clinical trials, no colchicine-specific malaria data, and a narrow therapeutic index that makes a practical systemic antimalarial dose doubtful.

**To proceed, the following is needed:**
- Direct in vitro or animal data showing colchicine (or a safer analogue) inhibits *P. falciparum* at achievable, non-toxic concentrations
- The HSA package insert, to establish the approved indication and safety warnings
- Detailed mechanism-of-action data from DrugBank
- A therapeutic-window analysis comparing antiparasitic concentrations with human toxicity

**Other predictions worth a look:** The second-ranked prediction, familial Mediterranean fever (score 99.38%), has a much stronger literature base, with many reviews describing colchicine as standard therapy. It is likely an existing label or guideline use rather than true repurposing. It is best handled as a label-status check, and the specific FMF variant should be confirmed. The remaining predictions (ranks 3 to 10) are supported by model score alone or by unrelated evidence and should stay on hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

