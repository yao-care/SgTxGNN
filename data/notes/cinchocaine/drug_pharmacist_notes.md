# Cinchocaine: From Local Anesthesia to Bronchitis

## One-Sentence Summary

Cinchocaine (also known as dibucaine) is an amide-type local anesthetic that blocks voltage-gated sodium channels (Nav), traditionally used for topical pain relief and local anesthesia.
The TxGNN model predicts it may be effective for **Bronchitis**, based on the theoretical anti-inflammatory properties of amide-class local anesthetics on airway sensory nerves.
However, this prediction is currently supported by **0 clinical trials** and **0 publications**, representing model-only evidence with no clinical translation data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local anesthesia (amide-type sodium channel blocker) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cinchocaine is an amide-class local anesthetic that exerts its pharmacological effect by blocking voltage-gated sodium channels (Nav), thereby inhibiting the generation and propagation of action potentials in sensory and motor nerves. It is structurally and mechanistically related to other amide-class agents such as lidocaine and bupivacaine, though it carries a significantly higher systemic toxicity profile than most modern alternatives in this class.

The mechanistic rationale for the bronchitis prediction rests on a class-level observation: amide-class local anesthetics — particularly intravenous lidocaine — have demonstrated anti-inflammatory properties in airway settings. These include inhibition of airway sensory nerve subtypes (Nav1.7 and Nav1.8) and suppression of leukocyte Nav channel activation, which theoretically could reduce neurogenic inflammation and bronchial hypersensitivity in bronchitis. The TxGNN knowledge graph may have identified this shared mechanistic node linking sodium channel blockade to airway inflammatory pathways.

However, the extrapolation from class-level (lidocaine IV) to Cinchocaine specifically carries substantial uncertainty. Cinchocaine's systemic toxicity risk is considerably higher than lidocaine's, limiting any potential systemic administration route. Furthermore, there is essentially no published translational evidence connecting Cinchocaine directly to bronchitis treatment. The prediction likely reflects shared graph topology within the model rather than drug-specific biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Cinchocaine is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No product authorizations are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No registrations found |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** No formal safety data (warnings, contraindications, or drug-drug interactions) was retrieved during the evidence collection phase for this candidate. Clinicians should be aware that Cinchocaine carries a well-established profile of systemic cardiovascular and CNS toxicity at supra-therapeutic doses, consistent with other amide-class local anesthetics. Additionally, the following mechanistic safety signals were identified during repurposing analysis across the top 10 predicted indications:
>
> - **Ranks 8 & 10 (Neonatal Myasthenia Gravis; Myasthenia Gravis with Thymus Hyperplasia):** ⚠️ Potential contraindication. Cinchocaine's Nav blockade may further impair neuromuscular junction (NMJ) transmission in patients already experiencing NMJ dysfunction, potentially worsening muscle weakness and precipitating respiratory failure. These predicted indications are mechanistically harmful rather than therapeutic.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications — including the top-ranked bronchitis — carry an L5 evidence level (model prediction only), with zero clinical trials and zero supporting publications identified across any indication. The mechanistic link between Cinchocaine's Nav-blocking mechanism and bronchitis remains theoretical and extrapolated from a related drug (lidocaine) at the class level. Furthermore, Cinchocaine's elevated systemic toxicity profile and its absence from the Singapore market make clinical translation highly challenging without substantial prior evidence.

**To proceed, the following is needed:**

- **MOA verification:** Retrieve complete mechanism of action data from DrugBank (DB00527) to confirm Nav channel subtype selectivity and any secondary targets relevant to airway inflammation
- **Safety data retrieval:** Download and parse the package insert (if available in any registered jurisdiction) to obtain formal contraindications, warnings, and drug interaction data — currently a blocking data gap (DG001)
- **Comparative mechanistic review:** Commission a structured literature review of IV lidocaine in bronchitis/COPD/airway inflammation to assess whether class-level evidence could be extrapolated to Cinchocaine with any scientific justification
- **Toxicity risk assessment:** Evaluate whether any administration route (e.g., inhaled or topical airway delivery) could achieve local anti-inflammatory effects while circumventing the systemic toxicity that makes oral/IV routes impractical
- **Safety signal escalation for MG indications:** Formally flag ranks 8 and 10 (neonatal and thymus-hyperplasia-associated myasthenia gravis) as mechanistically contraindicated — these should be excluded from further repurposing consideration without independent evidence contradicting the NMJ safety concern
- **Singapore regulatory pathway review:** If future evidence warrants, assess HSA registration requirements for a novel indication given that Cinchocaine has zero current registrations in Singapore