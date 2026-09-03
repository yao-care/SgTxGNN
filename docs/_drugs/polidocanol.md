---
layout: default
title: Polidocanol
parent: 僅模型預測 (L5)
nav_order: 796
evidence_level: L5
indication_count: 10
---

# Polidocanol
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

# Polidocanol: From Varicose Veins to Esophageal Variceal Bleeding

## One-Sentence Summary

Polidocanol is a detergent-type sclerosing agent, historically used for the treatment of varicose veins and spider veins via peripheral sclerotherapy. The TxGNN model predicts it may be effective for **esophageal varices with bleeding**, with **7 clinical trials (including 1 completed Phase 3 RCT)** and **20 publications** currently supporting this direction — reflecting its long-established off-label use in endoscopic injection sclerotherapy (EIS).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Varicose veins / spider veins (peripheral sclerotherapy) — no Singapore-specific approved indication text available |
| Predicted New Indication | Esophageal varices with bleeding |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Polidocanol is a detergent-type sclerosant: once injected into a vessel, it damages the vascular endothelium and triggers thrombosis/fibrosis, causing the vessel to collapse and be obliterated. This is exactly the pharmacological basis of endoscopic injection sclerotherapy (EIS) for esophageal varices — not a novel theoretical mechanism, but a decades-long, well-documented clinical application.

Esophageal varices are, mechanistically, a venous pathology similar to peripheral varicose veins (dilated, fragile veins prone to rupture and bleeding). The same "endothelial injury → thrombosis → fibrotic obliteration" principle that underlies Polidocanol's approved use in varicose vein treatment directly transfers to variceal sclerotherapy in the upper GI tract. This is corroborated by extensive clinical literature dating back to the 1980s (e.g., PMID 3552917, PMID 2693076) comparing polidocanol against other sclerosants (ethanolamine oleate, cyanoacrylate) for esophageal and gastric variceal bleeding, and by a completed Phase 3 RCT (NCT00161915) that used polidocanol-based sclerotherapy as a comparator arm for acute variceal hemostasis.

It is worth noting that current clinical guidelines favor endoscopic variceal ligation (EVL) over sclerotherapy for non-bleeding (primary prophylaxis) cases due to higher complication rates (esophageal ulceration, stricture) with sclerotherapy — this is reflected in the lower evidence tier (L2) and more cautious recommendation for the "without bleeding" indication (rank 2) compared to the acute bleeding indication (rank 1).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00161915](https://clinicaltrials.gov/study/NCT00161915) | Phase 3 | Completed | N/A | RCT comparing endoscopic fibrin sealant vs. ligature ± polidocanol for acute hemostasis and prevention of rebleeding in esophageal varices. |
| [NCT02361593](https://clinicaltrials.gov/study/NCT02361593) | N/A | Completed | 120 | RCT evaluating transparent cap-assisted endoscopic sclerotherapy with lauromacrogol (polidocanol) injection for esophageal varices. |
| [NCT01923064](https://clinicaltrials.gov/study/NCT01923064) | N/A | Completed | 96 | Cyanoacrylate + lipiodol vs. cyanoacrylate + lauromacrogol for gastric varices (disease-area relevant, agent differs). |
| [NCT02468206](https://clinicaltrials.gov/study/NCT02468206) | N/A | Completed | 64 | Cyanoacrylate injection vs. BRTO for prevention of gastric variceal rebleeding (disease-area relevant, agent differs). |
| [NCT02468180](https://clinicaltrials.gov/study/NCT02468180) | N/A | Unknown | 70 | Cyanoacrylate injection vs. BRTO for primary prophylaxis of gastric variceal bleeding (disease-area relevant, agent differs). |
| [NCT02468167](https://clinicaltrials.gov/study/NCT02468167) | N/A | Unknown | 70 | Cyanoacrylate injection vs. BRTO for management of acute gastric variceal bleeding (disease-area relevant, agent differs). |
| [NCT05500625](https://clinicaltrials.gov/study/NCT05500625) | N/A | Unknown | 70 | EUS-guided coil + cyanoacrylate vs. BRTO for gastric varices (disease-area relevant, agent differs). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9255525](https://pubmed.ncbi.nlm.nih.gov/9255525/) | 1997 | RCT | Endoscopy | Prospective study of cyanoacrylate + polidocanol vs. polidocanol alone for bleeding esophageal varices in unselected cirrhotic patients. |
| [3552917](https://pubmed.ncbi.nlm.nih.gov/3552917/) | 1987 | RCT | Hepato-gastroenterology | Randomized trial: ethanolamine oleate superior to polidocanol for EIS of esophageal varices, but polidocanol efficacy confirmed. |
| [10385713](https://pubmed.ncbi.nlm.nih.gov/10385713/) | 1999 | RCT | Gastrointest Endosc | Randomized trial of ligation vs. combined ligation + sclerotherapy for bleeding esophageal varices. |
| [2693076](https://pubmed.ncbi.nlm.nih.gov/2693076/) | 1989 | RCT | Endoscopy | Prospective randomized trial comparing ethanolamine and polidocanol for eradication of esophageal varices (81% vs. 64% eradication). |
| [10376453](https://pubmed.ncbi.nlm.nih.gov/10376453/) | 1999 | RCT | Endoscopy | Randomized prospective trial: combined ligation + sclerotherapy vs. ligation alone for eradication of bleeding esophageal varices. |
| [9514542](https://pubmed.ncbi.nlm.nih.gov/9514542/) | 1998 | RCT | J Hepatol | Endoscopic sclerotherapy with fibrin glue vs. polidocanol to prevent early esophageal variceal rebleeding. |
| [32517718](https://pubmed.ncbi.nlm.nih.gov/32517718/) | 2020 | Review | BMC Gastroenterol | Systematic review and pooled analysis of rebleeding risk after cyanoacrylate treatment of gastroesophageal varices. |
| [29473522](https://pubmed.ncbi.nlm.nih.gov/29473522/) | 2017 | Review | Curr Clin Pharmacol | Evidence-based review of off-label uses of Polidocanol, directly discussing its expanded applications beyond varicose veins. |
| [31261565](https://pubmed.ncbi.nlm.nih.gov/31261565/) | 2019 | Review | Medicine (meta-analysis) | Meta-analysis of sandwich method with/without lauromacrogol for gastric variceal bleeding in liver cirrhosis. |
| [33731585](https://pubmed.ncbi.nlm.nih.gov/33731585/) | 2021 | Cohort | Eur J Gastroenterol Hepatol | Complications and risk factors of elective endoscopic cyanoacrylate + lauromacrogol injection for gastric varices. |

---

## Singapore Market Information

Polidocanol is currently **not marketed** in Singapore, with **0 registered licenses**. No authorization records are available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication (esophageal varices with bleeding) is backed by L1-level evidence — a completed Phase 3 RCT plus multiple older RCTs directly using polidocanol/lauromacrogol for variceal sclerotherapy — and reflects a mechanistically well-established, decades-old off-label clinical practice rather than a novel hypothesis. However, Polidocanol has no current Singapore market registration and the safety label (TFDA/HSA warnings, contraindications) is a **blocking data gap**, so the drug cannot yet clear the S1 safety pre-screen.

**To proceed, the following is needed:**
- Resolve **DG001 (Blocking)**: obtain official label warnings/contraindications (download and parse PDF from the relevant regulatory agency) before any safety sign-off.
- Resolve **DG002 (High)**: retrieve formal mechanism-of-action data from DrugBank to strengthen the mechanistic-link analysis.
- Confirm route/formulation compatibility (injectable sclerosant) for the GI endoscopic use case, as this differs from its original peripheral venous indication.
- Assess Singapore registration pathway, since the drug is not currently marketed locally.
- Note that the "without bleeding" (prophylactic) indication (rank 2, L2 evidence) carries a weaker recommendation ("Research Question") due to guideline preference for EVL over sclerotherapy in that setting — this should not be conflated with the acute-bleeding indication above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

