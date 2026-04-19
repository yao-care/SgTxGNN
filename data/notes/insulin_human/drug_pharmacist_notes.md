# Insulin Human: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin human is a recombinant polypeptide hormone universally established as the core replacement therapy for diabetes mellitus, particularly Type 1 diabetes (T1DM), where endogenous insulin secretion is absent or severely deficient.
The TxGNN model predicts it may be effective for **Autoimmune Oophoritis**, with **0 clinical trials** and **0 publications** currently supporting this specific direction.
This prediction is assessed as a **disease co-morbidity network signal** rather than a direct therapeutic association, and warrants careful interpretation before any further investment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diabetes Mellitus (insulin replacement therapy) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on well-established pharmacology, insulin human is a recombinant form of endogenous human insulin. It acts by binding to the insulin receptor (IR) on target cells, activating the PI3K/Akt and MAPK/ERK intracellular signalling cascades, thereby promoting cellular glucose uptake (primarily in skeletal muscle and adipose tissue), suppressing hepatic gluconeogenesis, and facilitating anabolic biosynthesis of glycogen, lipids, and protein.

Autoimmune oophoritis is an immune-mediated disorder in which autoreactive T-lymphocytes and autoantibodies target ovarian steroidogenic cells, leading to progressive ovarian insufficiency. Critically, it frequently co-occurs as a component of Autoimmune Polyglandular Syndrome Type II or III (APS-II/III), and APS-II specifically includes T1DM as one of its defining features. It is this epidemiological co-occurrence — patients with T1DM who require insulin therapy are at elevated risk of developing APS and, consequently, autoimmune oophoritis — that the TxGNN knowledge graph model appears to have captured as a topological connection between insulin and autoimmune oophoritis.

This represents a **comorbidity association, not a therapeutic association**. Insulin has no known pharmacological mechanism to suppress the ovarian autoimmune cascade, modulate the autoantibodies targeting theca or granulosa cells, or reverse the gonadal insufficiency caused by autoimmune oophoritis. The standard of care for autoimmune oophoritis is oestrogen-based hormone replacement therapy (HRT) for symptom management, combined with immunosuppressive agents (e.g., corticosteroids) in selected cases. This prediction is most likely a false positive arising from shared disease-node proximity in the knowledge graph, and the direction of the association (comorbidity) is the opposite of therapeutic utility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

No Singapore Health Sciences Authority (HSA) drug registrations are currently on record for Insulin Human under this Evidence Pack. Insulin human products are however widely available globally under multiple brand names (e.g., Humulin, Novolin) and are typically registered in most major markets. A targeted HSA product search is recommended to verify current local registration status.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note on a critical adverse signal identified within this prediction set:** Among the 10 TxGNN predictions reviewed, **rank 6 (drug-induced localized lipodystrophy)** represents a situation where insulin is itself a well-documented *causative agent* of the predicted condition (via repeat injection-site lipoatrophy or lipohypertrophy), not a therapeutic one. This illustrates a known limitation of knowledge graph models that infer associations from co-occurrence patterns without encoding the *direction* of causality. This finding should be flagged in any downstream filtering pipeline.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for autoimmune oophoritis is driven by disease co-morbidity network topology — autoimmune oophoritis frequently co-occurs with APS type II/III, which itself includes T1DM — rather than any direct pharmacological effect of insulin on ovarian autoimmune pathology. With zero supporting clinical trials and zero supporting literature, and with no biologically plausible therapeutic mechanism, this prediction does not meet the threshold to progress.

**To proceed to the next evaluation stage, the following would be needed:**

- Identification of a biologically plausible mechanism by which insulin could modulate ovarian autoimmune activity (e.g., insulin receptor expression on immune effector cells in ovarian tissue, anti-inflammatory effects of insulin signalling in the ovarian microenvironment)
- At minimum one peer-reviewed preclinical study demonstrating any therapeutic effect of insulin in an autoimmune oophoritis model
- Disambiguation of the TxGNN signal: determine whether the model is encoding a co-morbidity pattern, a shared-biomarker pattern (e.g., anti-islet/anti-ovary cross-reactive antibodies in APS), or a genuine pharmacological relationship

**Higher-priority prediction to consider:**
A review of the full prediction set in this Evidence Pack reveals that **rank 9 (Pancreatic Agenesis)** carries an L4 evidence level with a "Proceed with Guardrails" recommendation and a direct, mechanistically unambiguous rationale: complete absence of endogenous pancreatic beta-cells necessitates exogenous insulin replacement as the primary therapeutic strategy. This prediction is substantially more actionable and is recommended for prioritisation in the next evaluation cycle.

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All predictions should be interpreted in the context of current clinical guidelines and applicable regulatory requirements.