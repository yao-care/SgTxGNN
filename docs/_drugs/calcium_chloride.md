---
layout: default
title: Calcium Chloride
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
---

# Calcium Chloride
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

# Calcium Chloride: From Calcium Supplementation to Dyspepsia

## One-Sentence Summary

Calcium chloride (CaCl₂) is an inorganic calcium salt clinically used for hypocalcaemia treatment and cardiac resuscitation, with no registered indications in Singapore.
The TxGNN model predicts potential efficacy for **Dyspepsia** with a confidence score of 97.47%, supported by **10 retrieved clinical trials** and **5 publications** — however, none of these directly test CaCl₂ for this indication, and the underlying mechanistic rationale is considered weak and potentially contrary to safe clinical use.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication recorded in Singapore regulatory data |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 97.47% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for calcium chloride is not available in the current Evidence Pack. Based on established pharmacology, CaCl₂ is an electrolyte that dissociates in aqueous solution to provide calcium (Ca²⁺) and chloride (Cl⁻) ions. Its proven clinical applications include emergency treatment of hypocalcaemia, cardiac resuscitation, reversal of calcium channel blocker toxicity, and correction of hyperkalemic cardiac arrhythmias.

Dyspepsia is characterised by upper gastrointestinal discomfort — including bloating, early satiety, epigastric pain, and nausea. The TxGNN model may have identified calcium chloride as a candidate because calcium-based compounds, particularly calcium carbonate (CaCO₃), are widely used antacids. CaCO₃ neutralises gastric acid through its alkaline buffering properties, thereby relieving dyspeptic symptoms. However, CaCl₂ is chemically and functionally distinct: it does not possess alkaline buffering capacity and cannot neutralise gastric acid in the same manner as carbonate-based antacids.

> ⚠️ **Mechanistic Warning:** Rather than being a treatment candidate, concentrated CaCl₂ is corrosive to the gastric mucosa. A published case report documents severe corrosive gastritis, gastric stenosis, and perforation following accidental ingestion of CaCl₂ (PMID 34897144). Additionally, a 1966 veterinary publication (PMID 6012101) describes the use of Locke-Ringer's solution — a multi-electrolyte mixture *containing* CaCl₂ among other salts — for calf dyspepsia, representing the sole indirect historical connection between calcium and this indication; this does not support CaCl₂ alone as a therapeutic agent. The model prediction is likely a false positive driven by superficial chemical similarity between calcium chloride and calcium carbonate. The predicted direction is mechanistically unsupported and potentially harmful.

---

## Clinical Trial Evidence

None of the 10 clinical trials retrieved for dyspepsia directly test calcium chloride. They are presented below for disease landscape context only.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT06320379](https://clinicaltrials.gov/study/NCT06320379) | N/A | Recruiting | 64 | Assesses the effect of an undisclosed dietary supplement on quality of life and digestion in adults with functional dyspepsia — disease-relevant, but does not test CaCl₂ |
| [NCT01149369](https://clinicaltrials.gov/study/NCT01149369) | Phase 2 | Completed | 126 | Aprepitant (NK1 receptor antagonist) for 4 weeks in patients with chronic nausea and vomiting of presumed gastric origin — demonstrates NK1 pathway as a dyspepsia/gastroparesis target; does not involve CaCl₂ |
| [NCT05346302](https://clinicaltrials.gov/study/NCT05346302) | Early Phase 1 | Completed | 249 | Biomarker, facial, and audio data collection to predict early infection via early warning scores — immunisation study with no relevance to dyspepsia or CaCl₂ |
| [NCT05111912](https://clinicaltrials.gov/study/NCT05111912) | Phase 2 | Completed | 206 | XW003 (once-weekly GLP-1 analogue) vs. liraglutide 3 mg for obesity management — metabolic disease trial with no connection to dyspepsia treatment or CaCl₂ |
| [NCT01725126](https://clinicaltrials.gov/study/NCT01725126) | Phase 2 | Completed | 53 | GSK2890457 first-in-human safety and tolerability study in healthy volunteers and T2DM patients — no specific connection to dyspepsia or CaCl₂ |
| [NCT02202161](https://clinicaltrials.gov/study/NCT02202161) | Phase 2 | Completed | 70 | GSK2330672 (bile acid transport inhibitor) safety/PK/PD vs. sitagliptin combined with metformin in T2DM — no connection to dyspepsia or CaCl₂ |
| [NCT01929863](https://clinicaltrials.gov/study/NCT01929863) | Phase 2 | Completed | 16 | GSK2330672 crossover study in T2DM on metformin — confirms bile acid inhibitor safety profile; no connection to dyspepsia or CaCl₂ |
| [NCT05258513](https://clinicaltrials.gov/study/NCT05258513) | N/A | Completed | 83 | Geranylgeraniol (GG) supplementation on sexual health function in males and females — no connection to dyspepsia or CaCl₂ |
| [NCT05813548](https://clinicaltrials.gov/study/NCT05813548) | N/A | Completed | 42 | App-based lifestyle change programme for body composition in women aged 30–55 — no connection to dyspepsia or CaCl₂ |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Transdermal vitamin and mineral patch absorption in post-bariatric surgery patients — evaluates micronutrient deficiency correction, not dyspepsia treatment; no connection to CaCl₂ |

---

## Literature Evidence

None of the 5 publications retrieved directly demonstrate CaCl₂ efficacy in human dyspepsia.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40317635](https://pubmed.ncbi.nlm.nih.gov/40317635/) | 2025 | Animal/Mechanistic | Neurogastroenterology and Motility | Amitriptyline + domperidone combination suppresses FD-like behaviour in rats via central and peripheral mechanisms — provides insight into FD pathophysiology but has no CaCl₂ involvement |
| [35319360](https://pubmed.ncbi.nlm.nih.gov/35319360/) | 2022 | Formulation Study | Current Drug Metabolism | Aceclofenac-loaded microspheres designed to reduce NSAID-induced gastrointestinal side effects including dyspepsia — highlights GI protection strategies; no CaCl₂ connection |
| [31185476](https://pubmed.ncbi.nlm.nih.gov/31185476/) | 2020 | In Vitro | Digestion | Traditional herbal formula Banhasasim-Tang modulates interstitial cells of Cajal via M3 muscarinic and 5-HT3 receptors in murine small intestine — GI motility mechanism study with no CaCl₂ connection |
| [5103465](https://pubmed.ncbi.nlm.nih.gov/5103465/) | 1971 | Historical/Case Series | Veterinariia | Historical veterinary report on preparation and use of multi-compound drug mixtures for dyspepsia — calcium salts may have been included as components; insufficient detail for modern evidence assessment |
| [6012101](https://pubmed.ncbi.nlm.nih.gov/6012101/) | 1966 | Animal/Veterinary | Veterinariia | Locke-Ringer's solution (a multi-electrolyte mixture containing CaCl₂, NaCl, KCl, NaHCO₃, and glucose) used for dyspepsia in calves — the sole indirect historical connection between calcium and dyspepsia treatment; evidence is veterinary, approximately 60 years old, and attributes therapeutic effect to the combined electrolyte solution rather than CaCl₂ specifically |

---

## Singapore Market Information

Calcium chloride (DB01164) has no products registered with the Health Sciences Authority (HSA) of Singapore. No license or approved indication data is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Important findings identified during predicted indication analysis:**

- **Gastric Corrosivity Risk:** A published case report (PMID 34897144) documents severe corrosive gastritis, gastric stenosis, and gastric penetration following accidental CaCl₂ ingestion in a human patient, accompanied by marked hypercalcaemia (calcium 18.6 mg/dL). This finding directly contradicts any proposed oral use of CaCl₂ for gastrointestinal indications.
- **Calcium-Alkali Syndrome (TxGNN Rank #2 Prediction — Safety Alert):** The model's second-ranked prediction is calcium-alkali syndrome. This is a condition that CaCl₂ can **cause**, not treat. Excessive calcium supplementation combined with alkaline substances leads to the triad of hypercalcaemia, metabolic alkalosis, and acute kidney injury — this is a recognised adverse effect profile of calcium-based compounds and represents a directional error in the model output that requires attention.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction of dyspepsia for calcium chloride achieves a high confidence score (97.47%) but rests on model inference alone (L5), with zero clinical trials or publications directly testing CaCl₂ for this indication. More critically, mechanistic analysis reveals this prediction is very likely a false positive — CaCl₂ lacks the alkaline buffering properties of carbonate antacids, has documented gastric corrosivity, and may cause rather than treat calcium-related gastrointestinal conditions. Proceeding with this repurposing hypothesis carries a meaningful patient safety risk.

**To proceed, the following is needed:**

- Obtain complete mechanism of action (MOA) data from DrugBank (identified data gap DG002) to determine whether any indirect calcium-signalling pathway could plausibly support the prediction
- Address the Singapore regulatory data gap (DG001) by retrieving the official package insert warnings and contraindications from the HSA or equivalent authority
- Conduct a focused investigation of the **stomach disease (rank 6)** prediction, which represents the most scientifically credible mechanistic hypothesis in this pack: two rat studies (PMID 1638681, PMID 2805233) show oral CaCl₂ inhibits NaCl-induced pyloric mucosal DNA replication and suppresses MNNG-induced gastric carcinogenesis — a potential chemopreventive mechanism that deserves a dedicated preclinical research question
- Clarify formulation context before any further development: intravenous CaCl₂ (electrolyte correction) and oral/luminal CaCl₂ carry fundamentally different safety profiles and should not be conflated in repurposing analyses
- If a gastrointestinal indication involving calcium is to be explored, calcium carbonate or other alkaline calcium salts are the pharmacologically appropriate candidates, not calcium chloride
- Consider implementing pharmacological subtype disambiguation in the TxGNN pipeline to prevent CaCl₂ from inheriting prediction signals from structurally and functionally distinct calcium compounds
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

