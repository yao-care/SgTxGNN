# Indacaterol: From COPD to Bronchial Disease

## One-Sentence Summary

Indacaterol is a once-daily ultra-long-acting β2-adrenoceptor agonist (ultra-LABA) globally approved for COPD and asthma maintenance treatment, though no Singapore registration records are currently on file.

The TxGNN model's top-ranked novel predictions — including nephrogenic syndrome of inappropriate antidiuresis (rank 1, score 99.54%), headache disorders, and trigeminal autonomic cephalalgia — all lack mechanistic plausibility and are rated **Hold (L5)**; by contrast, **bronchial disease** (asthma; rank 7) is supported by **37 clinical trials** and **20 publications**, achieving the only **L1 (Proceed with Guardrails)** recommendation in this dataset.

The high TxGNN scores for the novel conditions likely reflect knowledge graph semantic adjacency rather than true biological signal, making bronchial disease the only clinically actionable prediction in this Evidence Pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | COPD (globally approved; Singapore registration not found — likely data gap) |
| Predicted New Indication | Bronchial Disease (Asthma) — highest-evidence TxGNN prediction |
| TxGNN Prediction Score | 99.18% (rank 7 by score; rank 1 by evidence quality) |
| Evidence Level | L1 — Multiple completed Phase 3 RCTs |
| Singapore Market Status | Not Registered (HSA verification required) |
| Number of Registrations | 0 (suspected data gap — not a confirmed regulatory exclusion) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Indacaterol is an inhaled ultra-LABA that selectively activates β2-adrenoceptors on airway smooth muscle. Receptor binding triggers the Gs-protein → adenylyl cyclase → cAMP ↑ → PKA cascade, which phosphorylates and inactivates myosin light-chain kinase (MLCK), resulting in smooth muscle relaxation and bronchodilation sustained for approximately 24 hours. Secondary pharmacological effects include suppression of mast cell degranulation (reducing histamine and leukotriene release) and enhancement of mucociliary clearance. In fixed-dose combination with glycopyrronium (a long-acting muscarinic antagonist, LAMA), it delivers dual bronchodilation via complementary receptor pathways; the addition of mometasone furoate (an inhaled corticosteroid, ICS) provides the anti-inflammatory layer essential for asthma control.

Both COPD and bronchial disease (asthma) converge on the same endpoint of airway obstruction mediated by smooth muscle contraction, making Indacaterol's β2-agonist mechanism directly applicable across both conditions. In asthma specifically, airway hyperresponsiveness and eosinophilic inflammation drive reversible bronchoconstriction — the precise pathophysiology that ultra-LABAs address. This mechanistic overlap is why Indacaterol, originally developed for COPD (Onbrez® Breezhaler®), was subsequently developed in ICS-containing combinations (Atectura® QMF149; Enerzair® QVM149) approved in the EU and Japan specifically for inadequately controlled asthma.

The TxGNN model's nine other top-ranked predictions require a frank assessment: all are rated L5 (model prediction only). NSIAD (rank 1) involves AVPR2 gain-of-function mutations in renal collecting ducts — a pathway entirely disconnected from β2-adrenoceptor signalling. Headache disorders (rank 2) and trigeminal autonomic cephalalgia (rank 3) are contradicted mechanistically, as β2-agonist-induced vasodilation could theoretically worsen vascular headache, and migraine prophylaxis relies on β-blockers (opposite mechanism). Musculoskeletal predictions (paratenonitis, calcific tendinitis) and hair/skin predictions (hypertrichosis, Ambras syndrome) lack any known β2 receptor involvement. Only anaphylaxis (rank 9, L4) presents a pharmacological rationale — short-acting β2-agonists are guideline-listed adjuncts for anaphylaxis bronchospasm — but Indacaterol's ultra-long half-life (t½ ≈ 40–52 h) and slow onset make it entirely unsuitable for acute emergency scenarios.

---

## Clinical Trial Evidence

Trials below are selected from bronchial disease evidence (Grade A relevance; ordered by phase and enrollment):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02571777](https://clinicaltrials.gov/study/NCT02571777) | Phase 3 | Completed | 3,092 | 52-week double-blind comparison of QVM149 (Indacaterol 150µg/Glycopyrronium 50µg/Mometasone 80 or 160µg) vs QMF149 (Indacaterol/Mometasone) in poorly controlled asthma — pivotal evidence for Enerzair® EU approval |
| [NCT02554786](https://clinicaltrials.gov/study/NCT02554786) | Phase 3 | Completed | 2,216 | 52-week triple-dummy RCT of QMF149 (150/160µg and 150/320µg) vs Mometasone alone in poorly controlled asthma — key Atectura® registration trial |
| [NCT03158311](https://clinicaltrials.gov/study/NCT03158311) | Phase 3 | Completed | 1,426 | 24-week non-inferiority study of QVM149 vs free triple combination (Salmeterol/Fluticasone + Tiotropium) in uncontrolled moderate-to-severe asthma |
| [NCT00529529](https://clinicaltrials.gov/study/NCT00529529) | Phase 3 | Completed | 805 | 26-week double-blind, double-dummy safety trial of Indacaterol (300/600µg) vs Salmeterol in moderate-to-severe persistent asthma |
| [NCT01079130](https://clinicaltrials.gov/study/NCT01079130) | Phase 3 | Completed | 511 | Double-blind placebo-controlled parallel-group trial assessing 14-day bronchodilator efficacy of Indacaterol vs placebo and Salmeterol in persistent asthma |
| [NCT03100825](https://clinicaltrials.gov/study/NCT03100825) | Phase 3 | Completed | 96 | 52-week open-label safety study of QVM149 in Japanese patients with asthma — provides Asian population long-term safety data for regulatory submissions |
| [NCT01609478](https://clinicaltrials.gov/study/NCT01609478) | Phase 2 | Completed | 335 | 12-week double-blind placebo-controlled RCT evaluating Indacaterol acetate (75 and 150µg) efficacy, safety, and PK in persistent asthma — dose selection study for QMF149 |
| [NCT02892019](https://clinicaltrials.gov/study/NCT02892019) | Phase 2 | Completed | 79 | 2-week double-blind active-controlled study of Indacaterol acetate (75 and 150µg) in pediatric asthma (ages 6–11) — PK bridging to adults for Phase 3 dose identification |
| [NCT02953041](https://clinicaltrials.gov/study/NCT02953041) | Phase 4 | Completed | 31 | Crossover study assessing Glycopyrronium and Indacaterol, as monotherapy and combination, on methacholine dose-response curve — mechanistic validation of dual bronchodilation |
| [NCT02059434](https://clinicaltrials.gov/study/NCT02059434) | Phase 1 | Completed | 55 | Randomised placebo-controlled PK/PD study of LAS190792 in mild asthma and moderate-to-severe COPD — early bronchodilation mechanism and safety confirmation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [32653074](https://pubmed.ncbi.nlm.nih.gov/32653074/) | 2020 | RCT | The Lancet. Respiratory Medicine | IRIDIUM study: MF-IND-GLY (Enerzair®) vs ICS-LABA demonstrated superiority in FEV1 improvement and exacerbation reduction in inadequately controlled asthma — the pivotal registration trial |
| [39905183](https://pubmed.ncbi.nlm.nih.gov/39905183/) | 2025 | Systematic Review / Meta-analysis | Scientific Reports | BDP/FOR/GLY triple inhaler vs other triple therapies in uncontrolled asthma — confirms class-level benefit of single-inhaler LABA/LAMA/ICS for uncontrolled disease |
| [33871819](https://pubmed.ncbi.nlm.nih.gov/33871819/) | 2021 | Review | Drugs | Comprehensive clinical review of Indacaterol/Glycopyrronium/Mometasone (Enerzair® Breezhaler®) — mechanism, Phase 3 evidence synthesis, EU approval rationale, and safety profile |
| [35072888](https://pubmed.ncbi.nlm.nih.gov/35072888/) | 2022 | Review | Advances in Therapy | Development strategy of IND/GLY/MF — describes how this became the first once-daily single-inhaler LABA/LAMA/ICS approved for asthma in adults, including the digital sensor co-approval |
| [32967685](https://pubmed.ncbi.nlm.nih.gov/32967685/) | 2020 | RCT / PK | Respiratory Research | Head-to-head PK, lung function, and tolerability comparison of Indacaterol maleate vs acetate salt in asthma patients — supports salt switch in QMF149/QVM149 development |
| [28768531](https://pubmed.ncbi.nlm.nih.gov/28768531/) | 2017 | Crossover RCT | Respiratory Research | Randomised three-way crossover: Glycopyrronium and Indacaterol (mono/combination) on methacholine dose-response curves in mild asthmatics — quantifies bronchoprotection at airway sensitivity, reactivity, and maximal response levels |
| [34329722](https://pubmed.ncbi.nlm.nih.gov/34329722/) | 2021 | Pharmacology | Pulmonary Pharmacology & Therapeutics | Dose-bridging methodology for mometasone furoate across MF/IND and MF/IND/GLY fixed-dose combinations — regulatory framework for ICS component |
| [31404293](https://pubmed.ncbi.nlm.nih.gov/31404293/) | 2019 | Cohort Study | Frontiers in Pharmacology | Prevalence of airway eosinophilia and hyperresponsiveness in COPD phenotypes — clarifies overlap with asthma pathophysiology and ICS utility in obstructive airway disease |
| [19609496](https://pubmed.ncbi.nlm.nih.gov/19609496/) | 2009 | Review | Advances in Therapy | Early seminal review of Indacaterol as a novel once-daily LABA — Phase 2/3 efficacy and safety data for COPD and asthma, documenting rapid onset with 24-hour sustained bronchodilation |
| [22611179](https://pubmed.ncbi.nlm.nih.gov/22611179/) | 2012 | Review | Pharmacological Reviews | Comprehensive pharmacology of bronchodilators — mechanistic foundation of β2-adrenoceptor agonists and muscarinic antagonists in obstructive airway disease management |

---

## Singapore Market Information

No HSA registration records are available for Indacaterol in Singapore. This is almost certainly a **data gap** rather than a confirmed absence of approval: Indacaterol-containing products (Onbrez® Breezhaler® for COPD; Atectura® Breezhaler® for asthma; Enerzair® Breezhaler® for asthma with digital sensor) are approved by EMA and PMDA Japan. Verification with HSA's online product search is required before drawing any regulatory or commercial conclusions.

*No license table is presented as zero registration records are available in the current dataset.*

---

## Safety Considerations

Safety data from TFDA or HSA product monographs was not available for this report. The following are known class-level concerns for ultra-LABAs based on published literature and international product information — these should be confirmed against the HSA-approved package insert:

- **LABA class warning (asthma)**: Long-acting β2-agonists carry a class label regarding increased risk of asthma-related hospitalisation or death when used as monotherapy without an inhaled corticosteroid. All approved Indacaterol asthma indications are in fixed-dose ICS combinations (QMF149, QVM149)
- **Cardiovascular effects**: Tachycardia, palpitations, and QTc prolongation potential; monitor ECG in patients with pre-existing cardiac arrhythmias. Hypokalemia risk increases with high doses or concurrent non-potassium-sparing diuretics
- **Post-inhalation cough**: A well-documented class effect of Indacaterol dry powder inhalation (transient, typically resolving within seconds); not indicative of bronchospasm
- **Paradoxical bronchospasm**: Possible upon first use — discontinue immediately and switch to alternative therapy if it occurs

For complete warnings, contraindications, and drug-drug interaction data, obtain the current EMA/HSA-approved Summary of Product Characteristics (SmPC) or package insert.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Indacaterol has robust L1-level clinical evidence for bronchial disease (asthma), including multiple large completed Phase 3 RCTs with over 3,000 patients in the pivotal trials. The Enerzair® and Atectura® fixed-dose combinations have received regulatory approval in the EU and Japan for inadequately controlled asthma — establishing a clear, validated clinical pathway. The absence of Singapore registration records is likely a local data gap requiring immediate HSA verification before any market or clinical decisions are made.

**Important caveat on TxGNN novel predictions:**
Nine of the ten TxGNN predictions are rated **Hold (L5)**. The model's top novel predictions (NSIAD, headache disorders, trigeminal autonomic cephalalgia, paratenonitis, calcific tendinitis, hypertrichosis, myositis, Ambras syndrome) each contradict or are entirely disconnected from Indacaterol's β2-adrenoceptor mechanism. These high scores should be treated as knowledge graph artefacts. Anaphylaxis (rank 9, L4) has marginal pharmacological rationale but is clinically unsuitable given Indacaterol's ultra-long duration — further investigation would require a dedicated research protocol.

**To proceed, the following is needed:**

- **Immediate**: Verify HSA Singapore registration status for Onbrez® (COPD), Atectura® (asthma), and Enerzair® (asthma) — zero records is almost certainly a data gap, and this determination changes the entire regulatory pathway
- **Regulatory data (Blocking — DG001)**: Obtain HSA/EMA-approved package insert for complete safety warnings, contraindications, and interaction data
- **Mechanistic documentation (High — DG002)**: Confirm DrugBank MOA entry for formal mechanism record (anticipated: selective β2-adrenoceptor agonist, 24-hour duration of action)
- **If pursuing Singapore market entry**: Assess HSA regulatory pathway requirements, LABA monotherapy restrictions for asthma indications, mandatory ICS co-formulation requirements, and post-marketing surveillance obligations
- **Safety monitoring plan**: Cardiac monitoring (ECG, serum potassium, heart rate), respiratory function testing (FEV1, peak flow diary), and asthma exacerbation tracking throughout any trial or access programme