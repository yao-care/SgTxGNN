---
layout: default
title: Ivermectin
parent: 僅模型預測 (L5)
nav_order: 345
evidence_level: L5
indication_count: 10
---

# Ivermectin
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

# Ivermectin: From Parasitic Infections to Vulvovaginal Candidiasis

## One-Sentence Summary

Ivermectin is a broad-spectrum antiparasitic agent established for treating nematode and ectoparasite infections (including strongyloidiasis, onchocerciasis, and scabies).
The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis**, ranking it 1st with a score of 99.95%;
however, **0 clinical trials** and **0 directly relevant publications** currently support this direction, and the mechanistic rationale is critically weak, raising serious concern that this prediction reflects a knowledge graph (KG) node bias rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parasitic infections (antiparasitic agent — strongyloidiasis, onchocerciasis, scabies); formal indication data not available in system |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (Data Gap DG002 — DrugBank API query pending). Based on pharmacological context provided in the prediction rationale, Ivermectin acts by binding to glutamate-gated chloride (GluCl) ion channels found exclusively in invertebrate nerve and muscle cells, causing paralysis and death of susceptible parasites (nematodes, ectoparasites). At therapeutic doses, this mechanism has negligible activity in mammalian cells, which is the basis for Ivermectin's established safety profile in antiparasitic therapy.

Vulvovaginal candidiasis is a fungal infection caused by *Candida* species (most commonly *C. albicans*). Fungi do not possess GluCl channels — Ivermectin's primary molecular target — meaning there is **no established mechanistic basis** for antifungal activity. Some in vitro data have suggested Ivermectin may inhibit *Candida* biofilm formation, possibly through membrane permeability changes, but these findings are preliminary, inconsistent, and have not generated any clinical investigations.

Notably, all 10 top-ranked TxGNN predictions for Ivermectin cluster around candidiasis, vulvovaginal conditions, and HPV infection — a pattern highly inconsistent with its antiparasitic pharmacology. This uniformity is a recognised signature of **KG node bias**, where a drug's graph neighbourhood becomes spuriously enriched for co-located disease nodes rather than biologically plausible targets. The prediction score of 99.95% therefore reflects statistical artefact rather than mechanistic plausibility, and should be interpreted with extreme caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No directly relevant literature is available for vulvovaginal candidiasis.

> **Note on retrieved literature across all 10 predicted indications:** Two records were retrieved during the evidence search, but neither supports the predicted indications:
>
> | PMID | Year | Type | Journal | Finding |
> |------|------|------|---------|---------|
> | [35835488](https://pubmed.ncbi.nlm.nih.gov/35835488/) | 2022 | Case Report | *BMJ Case Reports* | Disseminated strongyloidiasis treated with Ivermectin — this is Ivermectin's **original** indication, not the predicted one |
> | [10098288](https://pubmed.ncbi.nlm.nih.gov/10098288/) | 1999 | Case Report | *Australasian Journal of Dermatology* | Crusted scabies in immunocompromised children treated with Ivermectin — again, an **original** indication; patient's concurrent mucocutaneous candidiasis was not treated by Ivermectin |

---

## Singapore Market Information

Ivermectin is currently **not registered** in Singapore. No product licences are on record, and no approved indication text is available through the Singapore regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, drug interactions) were not retrieved in this evidence pack due to Data Gap DG001 (TFDA package insert not yet parsed). DDI query returned no results. Full safety assessment is blocked until DG001 is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction sits at Evidence Level L5 — model prediction only — with zero supporting clinical trials, zero relevant publications, and no credible mechanistic link between Ivermectin's antiparasitic mechanism and Candida infection biology. The clustering of all 10 top predictions around candidiasis/vulvovaginal conditions is a strong signal of KG node bias; this candidate is not suitable for further repurposing development without first resolving the model artefact.

**To proceed, the following is needed:**

- **Resolve KG node bias:** Audit the TxGNN knowledge graph neighbourhood for Ivermectin to identify which node relationships are driving the candidiasis cluster; consider re-running predictions after graph correction
- **Complete MOA data (DG002):** Query DrugBank API for Ivermectin's full mechanism of action to enable proper mechanistic plausibility assessment
- **Complete safety data (DG001):** Parse TFDA package insert PDF to retrieve warnings and contraindications; this is currently a blocking data gap
- **Assess in vitro antifungal evidence:** Conduct a targeted PubMed search for Ivermectin + *Candida* + in vitro / biofilm to determine whether any preclinical signal exists that could justify upgraded investigation
- **If in vitro signal confirmed:** Commission a formal preclinical study before any clinical consideration is warranted

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

