# Choline Salicylate: From Inflammatory Pain to Prinzmetal Angina

## One-Sentence Summary

Choline salicylate is a non-acetylated salicylate with anti-inflammatory and analgesic properties, historically used for musculoskeletal pain and inflammatory conditions.
The TxGNN model predicts it may be effective for **Prinzmetal Angina**, achieving a prediction score of 99.84%; however, this indication currently has **no supporting clinical trials or published literature**, placing it at the lowest evidence tier (L5).
Notably, the second-ranked prediction — **rheumatoid arthritis** — carries L3-level observational evidence from documented clinical use in the 1970s–1980s and warrants separate consideration as a more actionable repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anti-inflammatory and analgesic use (non-acetylated salicylate class; no Singapore registration on record) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 — Model prediction only; no clinical studies found |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for choline salicylate in this dataset. Based on known pharmacological properties, choline salicylate is a non-acetylated salicylate that inhibits cyclooxygenase (COX-1 and COX-2) in a reversible manner, thereby reducing prostaglandin and thromboxane A₂ (TXA₂) synthesis. Unlike aspirin, the non-acetylated structure results in weaker and reversible platelet COX-1 inhibition, which theoretically translates to a more favourable gastrointestinal safety profile for long-term use.

The TxGNN model may be inferring a mechanistic link through the COX-1 → TXA₂ → platelet-mediated vasoconstriction pathway: theoretically, reducing TXA₂ synthesis could attenuate platelet-driven coronary spasm. Prinzmetal angina (variant angina), however, is primarily characterised by episodic rest-onset chest pain caused by transient coronary artery vasospasm driven by smooth muscle hyperreactivity and endothelial dysfunction — conditions managed with calcium channel blockers and long-acting nitrates, not anti-inflammatory or antiplatelet agents.

In practice, aspirin — a closely related and more potent COX-1 inhibitor — has not demonstrated clear benefit in Prinzmetal angina and may even exacerbate vasospasm in certain cases by suppressing prostacyclin (PGI₂) production. Extrapolating this concern to choline salicylate, which has weaker COX-1 inhibitory activity, makes clinical translation even less plausible. The high TxGNN score likely reflects a graph-based structural/network similarity pattern rather than a mechanistically validated pathway, and the prediction must be treated as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Choline salicylate (DB14006) is currently **not registered or marketed in Singapore**. No product licences are on record with the Health Sciences Authority (HSA).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for prescribers:** As a salicylate-class compound, choline salicylate shares class-level concerns common to NSAIDs — including potential renal prostaglandin suppression, gastrointestinal effects, and interactions with anticoagulants — though non-acetylated salicylates are generally considered to have a more favourable GI and platelet safety profile than aspirin. Formal contraindication and warning data specific to this compound were not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.84%) to choline salicylate for Prinzmetal angina, but this is unsupported by any clinical trials or published literature; the pathophysiological rationale is speculative, and the known mechanism of the salicylate class in coronary physiology raises the possibility of net harm rather than benefit in this indication.

**To proceed, the following is needed:**

- **MOA data**: Retrieve full mechanism of action and pharmacology from DrugBank (DB14006) to confirm or refute the TXA₂-vasospasm hypothesis
- **Safety package**: Download and parse the TFDA package insert PDF to populate key warnings and contraindications (currently a blocking data gap)
- **Preclinical evidence review**: Conduct a systematic search for salicylate class effects on coronary vasospasm in animal and in vitro models
- **Priority redirect — Rheumatoid Arthritis (Rank 2, L3)**: The second-ranked TxGNN prediction for rheumatoid arthritis has 4 supporting observational publications and a documented history of clinical use in the 1970s–1980s. This represents a significantly more viable near-term repurposing candidate. A focused safety review, updated literature search for modern RA studies, and assessment of current standard-of-care relevance should be prioritised over the Prinzmetal angina hypothesis.
- **Market feasibility**: Since the drug has no Singapore registration, a regulatory pathway assessment would be required before any clinical development could proceed.