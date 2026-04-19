# Atracurium Besylate: From Neuromuscular Blockade to Preeclampsia

## One-Sentence Summary

Atracurium besylate is a non-depolarising neuromuscular blocking agent (NMB) widely used in anaesthesia to facilitate endotracheal intubation and maintain skeletal muscle relaxation during surgical procedures, including in pregnant patients.
The TxGNN model predicts it may be effective for **Preeclampsia**, with **0 clinical trials** and **4 publications** identified in the evidence search — however, critical review reveals that none of these studies evaluate atracurium as a *treatment* for preeclampsia; they describe its use as an anaesthetic adjunct administered to preeclamptic patients undergoing caesarean section.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neuromuscular blockade during anaesthesia and surgical procedures (not registered in Singapore; known from medical literature) |
| Predicted New Indication | Preeclampsia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, atracurium besylate is a competitive antagonist of nicotinic acetylcholine receptors (nAChR) at the skeletal neuromuscular junction, producing reversible, dose-dependent muscle paralysis. Its defining pharmacokinetic property is **Hofmann elimination** — a spontaneous, pH- and temperature-dependent degradation process that is independent of renal or hepatic function — making it particularly suitable for patients with end-organ compromise, including those with preeclampsia-related organ dysfunction.

The high TxGNN score most likely reflects **clinical co-occurrence** rather than therapeutic potential: preeclamptic patients who require emergency caesarean section under general anaesthesia routinely receive atracurium as part of the standard anaesthetic protocol. The knowledge graph likely captures this frequent association between the drug and the disease context. Preeclampsia itself is a hypertensive disorder of pregnancy driven by placental endothelial dysfunction, and its management relies on antihypertensives (labetalol, hydralazine, nifedipine) and magnesium sulphate (MgSO₄) for seizure prophylaxis — mechanisms entirely unrelated to neuromuscular blockade.

A clinically important safety signal exists in this pairing: **MgSO₄, the first-line therapy for preeclampsia/eclampsia prophylaxis, potentiates the neuromuscular blocking effect of atracurium** and can significantly prolong its duration of action. This pharmacodynamic interaction requires dose reduction and enhanced neuromuscular monitoring when both agents are co-administered — further confirming that atracurium's presence in preeclampsia-related literature represents an anaesthetic management consideration, not a repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for atracurium in the treatment of preeclampsia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3778800](https://pubmed.ncbi.nlm.nih.gov/3778800/) | 1986 | Case Series | British Journal of Anaesthesia | Clinical observation of atracurium use in pre-eclamptic patients; describes safe administration as NMB adjunct during anaesthesia, not as a treatment for preeclampsia |
| [9646009](https://pubmed.ncbi.nlm.nih.gov/9646009/) | 1998 | PK/PD Review | Clinical Pharmacokinetics | Pharmacokinetics of NMBs (including atracurium) during pregnancy; notes that volume of distribution and clearance via Hofmann elimination are unchanged in pregnant patients |
| [18383970](https://pubmed.ncbi.nlm.nih.gov/18383970/) | 2008 | Case Series | Revista Española de Anestesiología y Reanimación | Remifentanil for haemodynamic control during C-section in high-risk patients (including severe preeclampsia ineligible for spinal anaesthesia); atracurium used as background NMB in the general anaesthesia protocol |
| [41103680](https://pubmed.ncbi.nlm.nih.gov/41103680/) | 2025 | RCT (anaesthesia comparison) | Anesthesiology and Pain Medicine | Comparison of IL-6, leptin, and adiponectin levels after C-section under general vs. spinal anaesthesia; atracurium included as part of the general anaesthesia regimen, not the study intervention |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinically Important Interaction**: Magnesium sulphate (MgSO₄), the standard prophylactic therapy for preeclampsia-related seizures, is known to significantly potentiate neuromuscular blockade from atracurium. If atracurium is used in any preeclampsia context, dose reduction and continuous neuromuscular monitoring are required.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for atracurium in preeclampsia is assessed as a **false positive driven by clinical co-occurrence**: atracurium appears in preeclampsia-related literature solely as an anaesthetic adjunct, not as a therapeutic agent. There is no biological mechanism linking neuromuscular junction blockade to the core pathophysiology of preeclampsia (placental ischaemia, endothelial dysfunction, hypertension, proteinuria), and no clinical trial has ever evaluated atracurium as a repurposing candidate for this indication. Across all 10 TxGNN-predicted indications for this drug, the same pattern holds — the model captures perioperative context, not therapeutic signal.

**To proceed, the following is needed:**

- Retrieve the full product SmPC / package insert (originator source or HSA equivalent) to document contraindications, warnings, and dosing — currently a blocking data gap
- Obtain DrugBank MOA entry for DB00732 to formally confirm pharmacological classification
- No further repurposing investigation is recommended for the drug–preeclampsia pair or any of the 10 predicted indications in this pack; this candidate should be flagged as low-priority and archived pending any future mechanistic evidence