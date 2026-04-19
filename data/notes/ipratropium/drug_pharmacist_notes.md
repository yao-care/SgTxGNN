# Ipratropium: From Bronchospasm to Obstructive Lung Disease

## One-Sentence Summary

Ipratropium (Atrovent®) is an inhaled anticholinergic bronchodilator with decades of established global use for bronchospasm and COPD, though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Obstructive Lung Disease**,
with **50 clinical trials** and **20 publications** currently supporting this direction — consistent with its recognised international pharmacological profile.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; globally established for bronchospasm and COPD |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological information, Ipratropium is a competitive muscarinic receptor antagonist (M1/M2/M3) — a synthetic quaternary isopropyl derivative of atropine — that blocks parasympathetically mediated bronchoconstriction and excessive mucus secretion. It is a first-line inhaled bronchodilator for obstructive airway diseases marketed internationally as Atrovent® and as part of Combivent® (with salbutamol) and Berodual® (with fenoterol).

Obstructive lung disease, encompassing COPD, chronic bronchitis, and bronchospasm, is characterised by excessive vagal (cholinergic) tone contributing to airway narrowing. Ipratropium directly targets this mechanism by competitively antagonising muscarinic receptors on bronchial smooth muscle, reducing airway resistance and improving expiratory airflow (FEV₁). This mechanistic alignment explains why the TxGNN model achieves a near-perfect prediction score of 99.97% — the drug's known pharmacology and the predicted indication are essentially synonymous.

Importantly, this prediction represents a **validation** of Ipratropium's established global indication rather than a novel repurposing discovery. Multiple landmark Phase 3 randomised controlled trials — including the Lung Health Study (NCT00000568) and head-to-head comparisons with tiotropium — have definitively established Ipratropium's efficacy in COPD. The drug's absence from the Singapore market represents a **market access gap**, not a lack of clinical evidence, and is the primary barrier for local use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000568](https://clinicaltrials.gov/study/NCT00000568) | Phase 3 | Completed | N/A | Landmark Lung Health Study I/III: evaluated Ipratropium's effects on the rate of FEV₁ decline in early COPD (cigarette smokers); foundational RCT establishing the drug's role in obstructive lung disease |
| [NCT02172469](https://clinicaltrials.gov/study/NCT02172469) | Phase 3 | Completed | 215 | Tiotropium 18 µg once daily vs Atrovent® MDI (20 µg QID) in Filipino COPD patients; head-to-head bronchodilator efficacy and safety comparison |
| [NCT00274040](https://clinicaltrials.gov/study/NCT00274040) | Phase 3 | Completed | 141 | Double-blind, double-dummy comparison of tiotropium vs Ipratropium MDI in COPD; confirmed comparative efficacy between long-acting and short-acting anticholinergics |
| [NCT00400153](https://clinicaltrials.gov/study/NCT00400153) | Phase 3 | Completed | 1,480 | Combivent Respimat (ipratropium/salbutamol spray) vs Combivent MDI over 12 weeks in COPD; large non-inferiority trial confirming new-device efficacy |
| [NCT02233881](https://clinicaltrials.gov/study/NCT02233881) | N/A (Post-Marketing) | Completed | 4,222 | Large-scale post-marketing surveillance of Atrovent® inhalets in COPD under routine clinical conditions (Germany); real-world tolerability and efficacy |
| [NCT02182713](https://clinicaltrials.gov/study/NCT02182713) | Phase 4 | Completed | 30 | Combivent® (salbutamol 120 µg + ipratropium 20 µg) vs salbutamol alone in methacholine-induced bronchospasm; demonstrated additive bronchodilator protection |
| [NCT00846586](https://clinicaltrials.gov/study/NCT00846586) | Phase 3 | Completed | 1,134 | Indacaterol 150 µg + tiotropium vs tiotropium alone in moderate-to-severe COPD over 12 weeks; large-scale LABA + LAMA combination study in obstructive lung disease |
| [NCT00239473](https://clinicaltrials.gov/study/NCT00239473) | Phase 3 | Completed | 429 | Tiotropium Respimat (5 µg/10 µg) vs placebo and ipratropium MDI QID over 12 weeks in COPD; Ipratropium as active comparator confirming benchmark efficacy |
| [NCT01019694](https://clinicaltrials.gov/study/NCT01019694) | Phase 3 | Completed | 470 | Long-term safety and patient acceptability of Combivent Respimat vs Atrovent HFA + albuterol HFA in COPD; confirmed patient preference and tolerability |
| [NCT02260011](https://clinicaltrials.gov/study/NCT02260011) | Phase 2 | Completed | 41 | Single-dose crossover study comparing ipratropium HFA-134a vs Atrovent® CFC inhalation aerosol in COPD; bronchodilator bioequivalence confirmed for reformulated propellant |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20163324](https://pubmed.ncbi.nlm.nih.gov/20163324/) | 2010 | Systematic Review/Meta-analysis | Expert Opin Drug Metab Toxicol | Comprehensive synthesis of mechanism, clinical efficacy and safety of inhaled albuterol/ipratropium and their combination in COPD; approved combination therapy >15 years prior |
| [16856113](https://pubmed.ncbi.nlm.nih.gov/16856113/) | 2006 | Cochrane Systematic Review | Cochrane Database Syst Rev | Ipratropium vs long-acting beta-2 agonists (LABAs) for stable COPD; both drug classes recommended in guidelines through different but complementary mechanisms |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Cochrane Systematic Review | Cochrane Database Syst Rev | Updated comparison of tiotropium vs ipratropium bromide in stable COPD; tiotropium showed superiority in exacerbation reduction; Ipratropium remains an evidence-based option |
| [24043433](https://pubmed.ncbi.nlm.nih.gov/24043433/) | 2013 | Cochrane Systematic Review | Cochrane Database Syst Rev | Previous iteration of tiotropium vs ipratropium for COPD; comprehensive evidence synthesis confirming Ipratropium's established role |
| [38457591](https://pubmed.ncbi.nlm.nih.gov/38457591/) | 2024 | RCT | Medicine | Probiotics combined with budesonide and ipratropium bromide vs budesonide/ipratropium alone in 118 COPD patients; assessed improvements in lung function and gut microbiota changes |
| [7813271](https://pubmed.ncbi.nlm.nih.gov/7813271/) | 1995 | RCT | Chest | Non-bronchodilator effects of pirbuterol vs ipratropium in COPD; compared gas exchange and pulmonary circulation, demonstrating unique physiological advantages of each drug class |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Clinical Study | Ann Pharmacother | Concomitant use of ipratropium and tiotropium in COPD; reviewed efficacy and safety data for dual anticholinergic therapy |
| [35616126](https://pubmed.ncbi.nlm.nih.gov/35616126/) | 2022 | Cochrane Systematic Review | Cochrane Database Syst Rev | Magnesium sulfate as adjunct in acute COPD exacerbations; ipratropium constitutes standard of care background treatment, confirming its current first-line status |
| [2977109](https://pubmed.ncbi.nlm.nih.gov/2977109/) | 1988 | Review | Clin Pharmacy | Early foundational review of ipratropium bromide: chemistry, pharmacokinetics, mechanism (cyclic GMP inhibition at parasympathetic nerve endings), and clinical efficacy in obstructive lung disease |
| [15987237](https://pubmed.ncbi.nlm.nih.gov/15987237/) | 2005 | Review | Treat Respir Med | Ipratropium bromide HFA formulation (non-selective muscarinic receptor antagonist on airway smooth muscle); approved in the US for maintenance treatment of bronchospasm associated with COPD |

---

## Singapore Market Information

Ipratropium is not currently registered with the Health Sciences Authority (HSA) of Singapore. No product licences were identified in the regulatory database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No records found | — | Not registered with HSA Singapore |

> **Note:** The absence of local registration does not reflect a lack of clinical evidence. Ipratropium (Atrovent®, Combivent®) is widely approved and marketed in numerous jurisdictions including the EU, US, Japan, and Taiwan. An HSA registration application would require submission of the established clinical dossier.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gap Notice:** Singapore-specific prescribing information (TFDA/HSA package insert warnings, contraindications, and drug interaction data) was not available at the time of this assessment. These represent blocking data gaps (DG001, DG002) that must be resolved before clinical use in Singapore.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
TxGNN's prediction of obstructive lung disease for Ipratropium is strongly validated by an L1 evidence base — multiple completed Phase 3 RCTs including the landmark Lung Health Study, four Cochrane systematic reviews, and over 50 registered clinical trials demonstrating consistent efficacy and an established safety profile. This is not a speculative repurposing; the drug is a globally recognised first-line bronchodilator. The primary barriers to use in Singapore are regulatory registration and local safety data documentation, not clinical evidence.

**To proceed, the following is needed:**
- **HSA registration pathway**: Submit a product licence application to the Health Sciences Authority (Singapore); the drug is off-patent and globally established, supporting an abridged or literature-based dossier
- **Safety documentation** (DG001): Obtain and review Singapore package insert equivalent (warnings, contraindications, special populations) — currently a blocking data gap
- **Mechanism of action data** (DG002): Retrieve full MOA entry from DrugBank API for DB00332 to complete the pharmacological profile
- **Drug interaction data**: No DDI data currently available; cross-reference with Singapore formulary and common co-medications in COPD patients (e.g., other anticholinergics, cardiovascular drugs)
- **Local formulation assessment**: Confirm which dosage forms (MDI, nebuliser solution, Respimat) are appropriate and feasible for the Singapore market
- **Pharmacovigilance plan**: Establish local adverse event monitoring, particularly for anticholinergic effects (urinary retention, angle-closure glaucoma, tachycardia) in the Singapore patient population