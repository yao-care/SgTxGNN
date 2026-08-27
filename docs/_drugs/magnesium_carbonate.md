---
layout: default
title: Magnesium Carbonate
parent: 僅模型預測 (L5)
nav_order: 621
evidence_level: L5
indication_count: 10
---

# Magnesium Carbonate
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

# Magnesium Carbonate: From Antacid Component to Active Peptic Ulcer Disease

## One-Sentence Summary

Magnesium carbonate is a classic antacid agent used as a buffering component in combination antacid preparations, working through direct chemical neutralization of gastric hydrochloric acid.
The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**, with **no registered clinical trials** but **4 supporting publications** identified for this specific indication.
The mechanistic basis is well-established and chemically straightforward, though clinical evidence for magnesium carbonate as a standalone agent remains limited.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record (used as antacid buffering component in combination preparations) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Magnesium carbonate acts as a chemical antacid through a direct and well-characterized reaction: MgCO₃ + 2HCl → MgCl₂ + H₂O + CO₂. This reaction raises intragastric pH rapidly, reducing the corrosive acid load on ulcerated gastric mucosa. The mechanism is the same core process underlying the entire antacid drug class, and is distinct from more modern acid-suppression strategies (H₂ blockers, proton pump inhibitors) in that it is a passive chemical neutralization rather than receptor-mediated suppression.

The link between this mechanism and active peptic ulcer disease is conceptually direct: peptic ulcers arise from an imbalance between gastric acid secretion and mucosal defense, and reducing acid exposure — even transiently — creates a more permissive environment for mucosal healing. Multiple 1980s randomized controlled trials demonstrated that antacid combination preparations (many of which contain magnesium carbonate alongside aluminum hydroxide or bismuth compounds, such as Caved-S) achieved ulcer healing rates comparable to cimetidine (~63% at 6 weeks, ~91% at 12 weeks). Animal mechanistic studies (PMID 3219285) also showed that Roter tablets — a combination product with magnesium carbonate as a key base constituent — preserved endogenous prostaglandin E₂ synthesis, suggesting potential mucosal cytoprotective co-effects.

The key caveat is that existing evidence consistently uses combination formulations rather than magnesium carbonate as a pure monotherapy. Whether the antacid effect is attributable to magnesium carbonate specifically, or to the synergistic action of the full combination, has not been directly studied. Modern peptic ulcer treatment has shifted to PPI-based H. pylori eradication regimens, repositioning antacids as adjunctive symptom-relief agents rather than primary curative therapies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for active peptic ulcer disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT (3-arm) | Scand J Gastroenterol | 72 patients with duodenal/prepyloric ulcers; antacid + anticholinergic achieved 50% healing at 3 weeks vs 25% placebo (p < 0.05); cimetidine superior at 67% |
| [6755656](https://pubmed.ncbi.nlm.nih.gov/6755656/) | 1982 | RCT | Scand J Gastroenterol Suppl | Treatment of active prepyloric and duodenal ulcers comparing antacid/anticholinergic combination, cimetidine, and placebo |
| [3003883](https://pubmed.ncbi.nlm.nih.gov/3003883/) | 1985 | RCT | Scand J Gastroenterol | 80 duodenal ulcer patients; antacid tablets 4×/day with high- or low-fiber diet; healing rate 67.5% vs 60% (NS); antacid base showed consistent healing benefit |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | In vitro / Quality Assessment | Medicine and Pharmacy Reports | Evaluation of acid-neutralizing capacity (ANC) of antacid preparations marketed in Morocco; physicochemical benchmarking of antacid products |

---

## Singapore Market Information

Magnesium carbonate is not registered in Singapore. No product licenses are on record.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-drug interaction data, key warnings, or contraindication records were retrievable from available databases for this compound at the time of this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for magnesium carbonate in active peptic ulcer disease is chemically sound and directly supported by the antacid class's established mode of action; however, evidence is confined to combination product RCTs from the 1980s, and there is no standalone monotherapy trial data, no registered clinical trials in Singapore-relevant populations, and no Singapore market approval to draw upon.

**To proceed, the following is needed:**

- Confirm whether the intended use case is as a standalone agent or as part of a combination antacid product (the evidence base strongly favors the latter)
- Obtain the full package insert or prescribing information to document warnings, contraindications, and drug interactions — this is currently a blocking data gap
- Establish whether any contemporary Singapore or regional formulations containing magnesium carbonate are in use, which would support a bridging-data strategy rather than a de novo development path
- Conduct a comparative effectiveness review against current standard of care (PPI ± H. pylori eradication) to define the realistic clinical niche: most likely adjunctive or OTC symptom relief, not first-line curative therapy
- If a development pathway is pursued, consider a Phase 2 dose-finding study with objective endpoints (endoscopic healing at 4 and 8 weeks) using a defined magnesium carbonate-containing formulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

