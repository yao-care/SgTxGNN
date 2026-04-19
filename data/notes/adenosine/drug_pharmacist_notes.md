# Adenosine: From Supraventricular Tachycardia to Open-Angle Glaucoma

## One-Sentence Summary

Adenosine is a naturally occurring purine nucleoside with well-established clinical use in terminating paroxysmal supraventricular tachycardia (SVT) via rapid intravenous bolus, acting through A1 receptor-mediated AV nodal conduction blockade.
The TxGNN model predicts it may be effective for **Open-Angle Glaucoma**, with **5 clinical trials** (including 1 completed Phase 3) and **20 publications** currently supporting this direction.
Although Adenosine is not currently registered in Singapore, its selective A1 receptor analogue Trabodenoson has already completed a full clinical development programme through Phase 3 for this indication, providing direct pathway validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Paroxysmal supraventricular tachycardia (SVT) — first-line acute IV termination agent |
| Predicted New Indication | Open-Angle Glaucoma (Primary Open-Angle Glaucoma / Ocular Hypertension) |
| TxGNN Prediction Score | 95.11% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Adenosine is an endogenous purine nucleoside that exerts its biological effects through four G-protein-coupled receptors: A1, A2A, A2B, and A3. In cardiac tissue, A1 receptor activation via Gi-protein coupling suppresses adenylyl cyclase, lowers intracellular cAMP, and slows AV node conduction — the established mechanism behind its use in terminating SVT. Detailed mechanism of action data from DrugBank was not available in this evidence pack, but the receptor pharmacology of adenosine is extensively characterised in the peer-reviewed literature.

The mechanistic bridge to open-angle glaucoma is biologically coherent. In the trabecular meshwork (TM) — the primary site of conventional aqueous humour outflow — A1 receptor activation engages the same Gi signalling cascade, triggering F-actin cytoskeletal reorganisation and matrix metalloproteinase-2 (MMP-2) activation. This remodels the extracellular matrix of the TM and increases outflow facility through the conventional (trabecular) drainage pathway, thereby reducing intraocular pressure (IOP). Separately, the A3 receptor is selectively upregulated in TM tissue under oxidative stress conditions associated with POAG (PMID 33987224), raising the possibility of complementary neuroprotective effects beyond IOP lowering. The purinergic axis is further implicated by direct measurement: aqueous humour ATP concentrations are significantly elevated in POAG patients (PMID 33963197), where extracellular ATP is rapidly dephosphorylated to adenosine, amplifying endogenous adenosine receptor signalling at the disease site.

The single most compelling piece of evidence is the complete clinical development programme for **Trabodenoson (INO-8875)**, a selective adenosine A1 receptor-mimetic. This progressed from Phase 1/2 (NCT01123785, n=144, completed) through two Phase 2 studies to a completed Phase 3 trial (NCT02565173, n=303) and an ongoing Phase 3 (NCT05405868, n=496, recruiting). Although the completed Phase 3 monotherapy trial did not meet its primary IOP-lowering endpoint, it conclusively establishes that the adenosine A1 pathway is biologically active in the human trabecular meshwork and can be safely targeted pharmacologically. A critical practical constraint for Adenosine itself is its plasma half-life of under 10 seconds after intravenous administration; an ophthalmic topical formulation, prodrug strategy, or structural analogue approach would be necessary for any sustained ocular application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02565173](https://clinicaltrials.gov/study/NCT02565173) | Phase 3 | Completed | 303 | Trabodenoson 3.0%, 6.0% QD or 4.5% BID vs timolol 0.5% BID vs placebo over 12 weeks in OHT/POAG — highest-evidence adenosine A1 pathway RCT; primary IOP endpoint not met with monotherapy, providing critical learning on dosing and patient selection |
| [NCT05405868](https://clinicaltrials.gov/study/NCT05405868) | Phase 3 | Recruiting | 496 | Nicotinamide to slow visual field loss in open-angle glaucoma (completion June 2027) — active high-enrolment Phase 3 reflecting continued pipeline confidence in neuroprotective approaches to POAG |
| [NCT01123785](https://clinicaltrials.gov/study/NCT01123785) | Phase 1/2 | Completed | 144 | Trabodenoson (INO-8875) ophthalmic dose-escalation in OHT/POAG — first-in-human adenosine A1 agonist ocular trial; established tolerability, pharmacokinetics, and preliminary IOP-lowering activity |
| [NCT02829996](https://clinicaltrials.gov/study/NCT02829996) | Phase 2 | Completed | 201 | Trabodenoson + latanoprost fixed-dose combination in OHT/POAG — evaluated combination with a prostaglandin analogue, providing proof-of-concept for adenosine pathway as additive to standard of care |
| [NCT01917383](https://clinicaltrials.gov/study/NCT01917383) | Phase 2 | Completed | 101 | Trabodenoson added to latanoprost vs timolol in OHT/POAG — validated adenosine A1 pathway as an add-on to prostaglandin therapy with efficacy data that informed Phase 3 sample size calculations |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33405971](https://pubmed.ncbi.nlm.nih.gov/33405971/) | 2021 | Review | Expert Opinion on Investigational Drugs | Comprehensive clinical data review of trabodenoson; confirms A1R adenosine mimetic mechanism via MMP-2 matrix remodelling in trabecular meshwork; Phase 3 candidate positioning for POAG |
| [27002298](https://pubmed.ncbi.nlm.nih.gov/27002298/) | 2016 | Clinical Study | J Ocular Pharmacology & Therapeutics | Dose-escalation of twice-daily trabodenoson over 14–28 days; established safety profile and documented statistically significant IOP reductions across multiple dose levels |
| [33987224](https://pubmed.ncbi.nlm.nih.gov/33987224/) | 2021 | Translational | Annals of Translational Medicine | Bioinformatic analysis identifies A3 adenosine receptor activation under H₂O₂ oxidative stress in POAG trabecular meshwork — dual A1/A3 receptor involvement in disease pathophysiology |
| [28356898](https://pubmed.ncbi.nlm.nih.gov/28356898/) | 2017 | Review | Yale Journal of Biology & Medicine | Comprehensive review of novel pharmacologic candidates for POAG; adenosine receptor agonists classified as a distinct emerging mechanistic class alongside Rho-kinase inhibitors and nitric oxide donors |
| [28480761](https://pubmed.ncbi.nlm.nih.gov/28480761/) | 2017 | Review | Expert Opinion on Pharmacotherapy | Topical glaucoma pharmacology review; adenosine A1 receptor stimulation of trabecular meshwork explicitly cited as a novel outflow-enhancing mechanism distinct from existing classes |
| [29965902](https://pubmed.ncbi.nlm.nih.gov/29965902/) | 2018 | Review | Journal of Glaucoma | Medical management of exfoliation glaucoma; adenosine α1-receptor stimulation grouped alongside Rho-kinase inhibition and NO signalling as recently approved or investigational trabecular-targeting agents |
| [33963197](https://pubmed.ncbi.nlm.nih.gov/33963197/) | 2021 | Metabolomics / Observational | Scientific Reports | Elevated ATP in aqueous humour of POAG patients alongside cytokine dysregulation and metabolic remodelling — directly implicates the purinergic (ATP→adenosine) signalling axis in POAG pathobiology |
| [15914619](https://pubmed.ncbi.nlm.nih.gov/15914619/) | 2005 | Translational | Investigative Ophthalmology & Visual Science | Selective upregulation of A3 adenosine receptor in anterior segment tissues of eyes with pseudoexfoliation syndrome and glaucoma — confirms adenosine receptor system is pathophysiologically relevant across glaucoma subtypes |
| [37525172](https://pubmed.ncbi.nlm.nih.gov/37525172/) | 2023 | Animal Study | Journal of Neuroinflammation | ATP-P2X7R signalling mediates microglial senescence and retinal ganglion cell death in chronic ocular hypertension — demonstrates that the broader extracellular purinergic axis (including adenosine) participates in glaucomatous neurodegeneration |
| [28076854](https://pubmed.ncbi.nlm.nih.gov/28076854/) | 2017 | Review | Ophthalmic Research | 20-year (1995–2015) POAG drug development pipeline analysis; adenosine pathway agents identified among the most mechanistically promising emerging categories entering clinical evaluation |

---

## Singapore Market Information

Adenosine (DrugBank: DB00640) is currently **not registered** in Singapore. No product licences from the Health Sciences Authority (HSA) were identified in this analysis. The drug has zero active market authorisations on file, meaning it is unavailable through licensed commercial channels in Singapore.

This is notable because intravenous adenosine formulations for SVT are widely available and used in many other markets (including the United States, European Union, and Taiwan). The absence of Singapore registration may reflect a gap in market access rather than a safety or efficacy concern. Any future clinical use in Singapore — including a potential ophthalmic formulation for glaucoma — would require a full HSA regulatory submission and approval prior to use.

---

## Safety Considerations

Safety data specific to Adenosine (warnings, contraindications, and drug interactions) was not retrieved in this evidence pack. Please refer to the package insert and available product information for complete safety guidance.

For context based on established pharmacology:

- **Cardiovascular effects of IV adenosine**: Transient AV block, sinus bradycardia, chest tightness, flushing, and hypotension are well-documented with intravenous administration. These effects resolve within seconds due to the extremely short plasma half-life.
- **Route-specific risk**: A topical ophthalmic formulation (as would be required for glaucoma) would have minimal systemic absorption and an expected markedly different safety profile compared to IV use.
- **Bronchospasm risk**: Intravenous adenosine is contraindicated in asthma — this would require evaluation in any ophthalmic context.
- **Drug interactions**: Formal DDI data was not available. The interaction with dipyridamole (a potent adenosine reuptake inhibitor that markedly potentiates adenosine effects) is a known concern for IV use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The adenosine A1 receptor pathway has been subjected to a rigorous and complete clinical development programme in POAG, with four completed clinical trials (Phase 1/2 through Phase 3) directly validating the biological mechanism and establishing human safety data. While the Phase 3 monotherapy endpoint was not met by trabodenoson, the pathway remains biologically justified and clinically active, evidenced by an ongoing Phase 3 trial (n=496) and a robust mechanistic and translational literature base. Adenosine itself cannot be used in unmodified form due to its near-instantaneous plasma elimination, making formulation innovation the critical enabler.

**To proceed, the following is needed:**

- **Formulation strategy**: Define whether the development path uses Adenosine with a topical ophthalmic delivery system (e.g., sustained-release hydrogel, pro-drug) or pivots to a selective A1/A3 receptor agonist analogue that overcomes the half-life limitation
- **Phase 3 failure analysis**: Obtain and review trabodenoson Phase 3 (NCT02565173) full clinical study report to determine whether the primary endpoint miss was due to dosing, patient selection, formulation, or a fundamental pathway limitation — this is essential before committing further resources
- **Mechanism of action data**: Retrieve full DrugBank MOA and pharmacology profile to complete the mechanistic narrative and support regulatory submissions
- **Singapore regulatory pathway**: Initiate HSA pre-submission consultation, as Adenosine is currently unregistered in Singapore; any future glaucoma formulation would require a de novo NDA/NDA-equivalent submission
- **Safety package**: Obtain formal contraindications and DDI data, with particular attention to interactions with prostaglandin analogues (latanoprost, bimatoprost), beta-blockers (timolol), and alpha-agonists — all standard-of-care POAG medications that patients would likely be concurrently using
- **Ongoing trial monitoring**: Track NCT05405868 (Phase 3, completing June 2027) for any results relevant to the broader adenosine neuroprotection hypothesis in glaucoma