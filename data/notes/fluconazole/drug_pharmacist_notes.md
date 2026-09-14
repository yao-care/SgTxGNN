# Fluconazole: From Fungal Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Fluconazole is a broad-spectrum triazole antifungal agent, widely used in clinical practice for treating invasive candidiasis, cryptococcal meningitis, and fungal prophylaxis in immunocompromised patients.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
with **0 clinical trials** and **0 publications** currently supporting this direction.
This prediction appears to be a knowledge graph topology effect rather than a genuine mechanistic signal, and is classified as **Hold** pending further evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Invasive fungal infections (candidiasis, cryptococcal meningitis; based on established pharmacological profile — no Singapore registration data available) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed (0 HSA registrations found) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacology, Fluconazole is a bis-triazole antifungal that selectively inhibits the fungal cytochrome P450 enzyme CYP51 (lanosterol 14α-demethylase), blocking the biosynthesis of ergosterol — the principal structural sterol of the fungal cell membrane. This mechanism confers potent activity against *Candida* species, *Cryptococcus neoformans*, and several dermatophytes, and underlies its widespread use in both systemic and mucosal fungal disease.

Punctate Epithelial Keratoconjunctivitis (PEK) is an inflammatory condition of the corneal epithelium and conjunctiva characterised by diffuse, fine epithelial lesions. Its most common causes are viral infection (adenovirus, herpes simplex), dry eye syndrome, allergic reactions, and toxic/chemical irritation. While Fluconazole may be used in *fungal* keratitis — a distinct and uncommon condition — there is no established fungal etiology for typical PEK. The biological rationale for repurposing a CYP51 inhibitor in a predominantly non-fungal ocular surface condition is therefore very limited.

The high TxGNN score (99.24%, rank #8,703) most likely reflects a graph topology proximity effect: within the knowledge graph, Fluconazole shares edges with "ocular infections" through fungal keratitis nodes, and PEK sits in the adjacent "ocular surface disease" neighbourhood. This structural closeness in the graph does not translate to a direct mechanistic or clinical link. In the absence of any supporting clinical trials or literature, this prediction should be treated with caution and is not currently actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

No HSA (Health Sciences Authority) product registrations were found for Fluconazole in the dataset. This likely represents a data gap rather than confirmed market absence, as Fluconazole is a WHO Essential Medicine and is widely registered as a generic in most regulatory jurisdictions. Verification against the HSA PRISM database is recommended before drawing conclusions about Singapore market availability.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note on a known interaction for context:** Although formal DDI data was not returned in this Evidence Pack, Fluconazole is a well-characterised inhibitor of CYP3A4 and CYP2C9. Literature within the pneumocystosis evidence cluster (PMID 12176555) documents Fluconazole co-administration raising tacrolimus trough levels 2–4 fold — a clinically significant interaction relevant to any immunocompromised patient population where Fluconazole might be considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Punctate Epithelial Keratoconjunctivitis is predominantly a non-fungal condition, and there is currently zero clinical evidence — no trials, no publications — supporting Fluconazole's use in this indication. The TxGNN high score is best explained by knowledge graph neighbourhood proximity to ocular infections rather than a genuine mechanistic or epidemiological signal.

**To proceed, the following is needed:**

- **Mechanistic basis:** Identification of a documented fungal etiology subgroup within PEK patients (e.g., *Candida* or dermatophyte-associated keratoconjunctivitis) before pursuing this indication
- **Preclinical data:** In vitro or animal model data demonstrating antifungal activity relevant to ocular surface pathology
- **MOA data:** Full mechanism of action data from DrugBank (DG002 remediation) to confirm or refute relevance of ergosterol pathway inhibition in this context
- **Safety data:** TFDA package insert warnings and contraindications (DG001 remediation) required before any safety evaluation can proceed
- **Singapore regulatory check:** Direct verification against HSA PRISM database to confirm actual Singapore market status of Fluconazole