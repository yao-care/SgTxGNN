# Inclisiran: From Hypercholesterolemia to Aortic Malformation

## One-Sentence Summary

Inclisiran is a PCSK9-targeting siRNA therapy approved internationally for reducing LDL cholesterol in patients with hypercholesterolaemia, including familial hypercholesterolaemia — though it remains unregistered in Singapore.
The TxGNN model identified 10 new potential indications; **aortic malformation** carries the strongest available evidence (**L3**, 2 Phase 3 recruiting trials), while **migraine susceptibility** shows indirect biological plausibility at **L4** (20 publications, no direct Inclisiran studies).
The remaining 8 predicted indications are unsupported model-only signals (**L5, Hold**) and are most likely knowledge graph artefacts without actionable clinical relevance.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolaemia / Familial Hypercholesterolaemia (internationally approved; not registered in Singapore) |
| Highest-Evidence Predicted Indication | Aortic Malformation |
| TxGNN Prediction Score (Aortic Malformation) | 99.76% |
| Evidence Level | L3 (aortic malformation); L4 (migraine susceptibility); L5 (all others) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** (8 of 10 predictions) / **Proceed with Guardrails** (aortic malformation) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Inclisiran is a small interfering RNA (siRNA) that silences PCSK9 mRNA specifically in hepatocytes. By preventing PCSK9 synthesis, it preserves LDL receptor expression on the hepatocyte surface, leading to sustained LDL cholesterol clearance from the bloodstream — with the clinical convenience of twice-yearly subcutaneous dosing.

For **aortic malformation**, the mechanistic rationale rests on the lipid-vascular axis: chronically elevated LDL-C promotes lipid deposition and inflammatory remodelling within the aortic wall, contributing to structural changes such as aortic aneurysm and dilation. Statins have prior precedent in aortic aneurysm management through this same pathway, providing indirect class-level biological plausibility. LDL-C reduction via PCSK9 inhibition could theoretically slow such lipid-driven aortic remodelling — particularly relevant in familial hypercholesterolaemia patients who face accelerated vascular disease from childhood.

It is critical to note, however, that the two clinical trials retrieved (NCT06597019 and NCT06597006) are evaluating Inclisiran's established cholesterol-lowering effect in paediatric familial hypercholesterolaemia patients — **aortic malformation is not their stated primary endpoint**. The connection to aortic malformation is indirect: it represents a potential long-term vascular benefit in high-risk patients, rather than a direct treatment target.

---

## Predicted Indications Overview

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Concern |
|------|---------|-------------|----------------|----------------|-------------|
| 1 | Potassium deficiency disease | 99.93% | L5 | Hold | PCSK9/LDLR pathway has no known link to potassium homeostasis; likely KG false-positive |
| 2 | Esophageal disease | 99.87% | L5 | Hold | No pharmacological rationale; Inclisiran acts exclusively in hepatocytes |
| 3 | Atypical coarctation of aorta | 99.86% | L5 | Hold | Congenital structural defect; unrelated to lipid metabolism |
| 4 | Migraine disorder | 99.83% | L5 | Hold | Theoretical CNS PCSK9 expression; no clinical evidence |
| 5 | Non-syndromic esophageal malformation | 99.83% | L5 | Hold | Congenital developmental defect; KG cluster effect |
| 6 | Migraine with brainstem aura | 99.78% | L5 | Hold | Subset of migraine cluster; no independent evidence |
| 7 | Migraine with/without aura (susceptibility) | 99.78% | L4 | Research Question | Genetic overlap with epilepsy documented; no Inclisiran-specific data |
| 8 | Aortic malformation | 99.76% | **L3** | **Proceed with Guardrails** | 2 Phase 3 trials recruiting; indirect evidence via LDL-C reduction in HeFH/HoFH |
| 9 | Esophageal ulcer | 99.73% | L5 | Hold | Derives from esophageal disease cluster; no mechanistic basis |
| 10 | Raynaud disease | 99.73% | L5 | Hold | Peripheral vasospasm; PCSK9 inhibition has negligible clinical relevance here |

**Pattern analysis:** Three clusters dominate the predictions — an esophageal cluster (ranks 2, 5, 9), a migraine cluster (ranks 4, 6, 7), and an aortic cluster (ranks 3, 8). The esophageal and aortic-structural clusters likely reflect broad "cardiovascular disease" node connections in the knowledge graph. The migraine cluster is the only group with a discoverable (if indirect) biological rationale.

---

## Clinical Trial Evidence

*Source: Rank 8 — Aortic Malformation (the only predicted indication with clinical trial data)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06597019](https://clinicaltrials.gov/study/NCT06597019) | Phase 3 | Recruiting | 51 | Double-blind placebo-controlled RCT (Year 1) followed by open-label extension (Year 2). Evaluates safety, tolerability, and efficacy of Inclisiran in children aged 6 to <12 years with **heterozygous familial hypercholesterolaemia (HeFH)** and elevated LDL-C. Primary endpoint is LDL-C reduction; aortic structural outcomes are not the stated primary target. Relevance to aortic malformation is indirect. |
| [NCT06597006](https://clinicaltrials.gov/study/NCT06597006) | Phase 3 | Recruiting | 9 | Double-blind RCT evaluating Inclisiran in children aged 2 to <12 years with **homozygous familial hypercholesterolaemia (HoFH)** and elevated LDL-C. Extremely small enrolment (n=9) is consistent with the ultra-rare nature of HoFH. Design mirrors NCT06597019 with Year 1 double-blind and Year 2 open-label phases. |

> ⚠️ **Important caveat:** Both trials are designed for familial hypercholesterolaemia in children — **not** for aortic malformation as a primary indication. Their relevance to "aortic malformation" stems from the fact that HoFH/HeFH patients develop premature aortic lipid deposition and structural cardiovascular disease, making sustained LDL-C lowering indirectly protective for aortic outcomes. Whether aortic imaging endpoints are included as secondary measures requires direct review of the full trial protocols.

*For all other predicted indications (ranks 1–7, 9–10): Currently no related clinical trials registered.*

---

## Literature Evidence

*Source: Rank 7 — Migraine with or without aura, susceptibility to (the only predicted indication with literature data)*

> ⚠️ **Data quality note:** The 20 retrieved publications predominantly address **epilepsy genetics and neuroinflammation** rather than migraine or PCSK9 inhibition. None directly investigate Inclisiran or any PCSK9 inhibitor for migraine treatment. The search appears to have retrieved publications on epilepsy-migraine genetic comorbidity, which is relevant only as indirect mechanistic background.

The most pertinent publications are listed below (prioritised by relevance to the migraine-PCSK9 hypothesis):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33856647](https://pubmed.ncbi.nlm.nih.gov/33856647/) | 2021 | Review | Molecular Neurobiology | Epilepsy and migraine share genetic and molecular mechanisms including ion channel variants and neuroinflammatory pathways. Provides the strongest background rationale for exploring CNS PCSK9 expression in migraine susceptibility. |
| [23294289](https://pubmed.ncbi.nlm.nih.gov/23294289/) | 2013 | Genetic Association | Epilepsia | Demonstrates shared genetic susceptibility between migraine and epilepsy in the EPGP cohort; supports the concept of overlapping neurological vulnerability. |
| [17460155](https://pubmed.ncbi.nlm.nih.gov/17460155/) | 2007 | Genetic Linkage | Neurology | Maps a familial syndrome of occipitotemporal lobe epilepsy with migraine with visual aura to chromosome 9q; illustrates the biological overlap between the two conditions. |

*All other retrieved publications (17 of 20) address epilepsy models, epilepsy genetics, or neuroinflammation without direct relevance to migraine or PCSK9 biology.*

*For all other predicted indications (ranks 1–6, 8–10): Currently no related literature available.*

---

## Singapore Market Information

Inclisiran is **not currently registered** with Singapore's Health Sciences Authority (HSA). No product licences are on record.

> For reference, Inclisiran (brand name: **Leqvio®**) has received regulatory approval in the European Union (EMA, December 2020) and the United States (FDA, December 2021) for the treatment of adults with primary hypercholesterolaemia (heterozygous familial and non-familial) or mixed dyslipidaemia, as an adjunct to diet and maximally tolerated statin therapy. Prescribers should consult HSA directly for current Singapore registration status and any updated market authorisation applications.

---

## Safety Considerations

Please refer to the package insert for safety information, as no Singapore-specific safety data (key warnings, contraindications, or drug-drug interactions) was available in this Evidence Pack.

> Based on published Phase 3 trial data and the EMA/FDA prescribing information for Inclisiran: the most commonly reported adverse events are **injection-site reactions** (pain, erythema, rash). As an siRNA agent processed independently of cytochrome P450 enzymes, Inclisiran carries a low pharmacokinetic drug-drug interaction burden. No clinically significant interactions have been reported to date. Full contraindication information (including use in pregnancy, renal impairment, and hepatic impairment) should be obtained from the current Summary of Product Characteristics (SmPC) or US Prescribing Information.

---

## Conclusion and Next Steps

**Decision: Hold (8 of 10 predictions) / Proceed with Guardrails (aortic malformation)**

**Rationale:**
The overwhelming majority of TxGNN-predicted indications for Inclisiran are mechanistically implausible knowledge graph signals with no supporting evidence — they should not be pursued. The aortic malformation signal is grounded in the known lipid-vascular biology of familial hypercholesterolaemia and is supported by 2 recruiting Phase 3 trials, but these trials are evaluating Inclisiran's established cholesterol-lowering role, not aortic malformation as a de novo indication. The migraine susceptibility signal warrants monitoring in the scientific literature but has no actionable clinical data at this time.

**To proceed, the following is needed:**

- **Aortic malformation (Proceed with Guardrails):**
  - Confirm whether NCT06597019 and NCT06597006 include aortic imaging or structural cardiovascular endpoints as secondary outcomes
  - Review published Phase 3 adult trial data (ORION-9, ORION-10, ORION-11) for any aortic or vascular structural secondary endpoints
  - Assess whether Inclisiran's benefit in familial hypercholesterolaemia children translates to clinically meaningful aortic protection

- **Migraine susceptibility (Research Question — monitor only):**
  - Search for evolocumab or alirocumab (class-level PCSK9 inhibitor) data in migraine, as class evidence may exist prior to Inclisiran-specific studies
  - Identify whether any neurological secondary endpoints appear in existing Inclisiran cardiovascular outcomes trials

- **All indications:**
  - Obtain complete MOA data from DrugBank (DB14901) to enable proper mechanistic scoring
  - Retrieve and review the full Inclisiran prescribing information (EMA SmPC or FDA PI) for key warnings and contraindications
  - Initiate HSA registration enquiry if Singapore market access is a strategic objective

---

*⚕️ Disclaimer: This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before any therapeutic application.*