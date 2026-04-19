# Avanafil: From Erectile Dysfunction to Amenorrhea

## One-Sentence Summary

Avanafil is a selective PDE5 (phosphodiesterase type 5) inhibitor approved in multiple countries (e.g., the United States as Stendra®) for the treatment of erectile dysfunction, but currently not registered in Singapore.
The TxGNN model's top-ranked prediction is **Amenorrhea** (score: 94.59%), though no clinical trials or publications directly support this direction (Evidence Level: L5).
Across the full set of 10 predicted indications, **Raynaud disease** (rank #5) emerges as the most clinically credible candidate, backed by a mechanistically coherent rationale and class-level evidence from related PDE5 inhibitors.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Erectile dysfunction (not registered in Singapore) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 94.59% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Avanafil is not available in this evidence pack. However, Avanafil is a well-characterised selective PDE5 (phosphodiesterase type 5) inhibitor belonging to the same pharmacological class as sildenafil and tadalafil. Its established mechanism involves blocking PDE5, the enzyme responsible for degrading cyclic GMP (cGMP). This raises intracellular cGMP concentrations in smooth muscle cells, leading to vasodilation and smooth muscle relaxation — effects primarily harnessed in erectile dysfunction treatment.

For amenorrhea, the mechanistic link is theoretically plausible but highly indirect: PDE5 is expressed in uterine endometrium and ovarian tissue, and the NO-cGMP signalling pathway is known to participate in menstrual cycle regulation. Sildenafil has been explored in small studies for improving endometrial perfusion. However, there is no published clinical or preclinical data linking Avanafil specifically to amenorrhea, and the connection remains a model-derived extrapolation rather than an established pharmacological rationale.

Among all 10 predictions in this evidence pack, **Raynaud disease** (rank #5, score: 88.54%) presents the most clinically credible repurposing opportunity. The core pathology of Raynaud's phenomenon — episodic vasospasm and impaired peripheral perfusion — aligns directly with PDE5 inhibition's mechanism of promoting smooth muscle relaxation and vasodilation. Sildenafil and Tadalafil have both demonstrated efficacy in Raynaud's (particularly scleroderma-related secondary Raynaud's) across multiple Phase 2/3 RCTs and a Cochrane systematic review, providing a strong class-effect rationale for studying Avanafil in this setting. In contrast, predictions such as malignant catarrh (rank #3) and infectious bovine rhinotracheitis (rank #4) represent veterinary diseases with no biological relevance to human pharmacology and should be treated as model artefacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Avanafil in amenorrhea.

---

## Literature Evidence

Currently no related literature directly studying Avanafil for amenorrhea.

---

## Singapore Market Information

Avanafil is not currently registered with the Health Sciences Authority (HSA) in Singapore. No marketing authorisations are on record.

> **Note for reviewers**: Avanafil is approved by the US FDA (Stendra®) and EMA (Spedra®) for erectile dysfunction. Prescribers and investigators should refer to the approved product information from these jurisdictions for dosing, safety, and contraindication guidance until Singapore-specific regulatory data becomes available.

---

## Safety Considerations

No drug interaction data, key warnings, or contraindication data were available in this evidence pack (both flagged as data gaps). As a class-level reference:

- **PDE5 inhibitor class warnings**: Contraindicated with nitrates (risk of severe hypotension); caution required in patients with significant cardiovascular disease, hypotension, or recent stroke/myocardial infarction.
- **Drug interactions**: Strong CYP3A4 inhibitors (e.g., ketoconazole, ritonavir) significantly increase Avanafil plasma levels. Alpha-blockers and antihypertensives may potentiate hypotensive effects.

Please refer to the approved package inserts (US FDA/EMA) for complete safety information until TFDA/HSA prescribing information is retrieved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication (amenorrhea) carries an Evidence Level of L5 — no supporting clinical trials or Avanafil-specific publications exist, and the mechanistic link is highly indirect. The overall prediction set is predominantly L5/Hold, with the single exception of Raynaud disease (L4, "Research Question"), which warrants targeted follow-up rather than immediate development.

**To proceed, the following is needed:**

- **Raynaud disease follow-up (most actionable)**: Conduct a focused literature review on Avanafil pharmacokinetics in peripheral vascular conditions; design a Phase 2 pilot protocol leveraging existing class-effect data from sildenafil/tadalafil RCTs in secondary Raynaud's (scleroderma-associated)
- **Safety data gaps**: Retrieve TFDA/HSA package insert warnings and contraindications (Data Gap DG001, Blocking severity) — required before any formal safety screening can proceed
- **MOA data**: Query DrugBank API for Avanafil's detailed mechanism of action (Data Gap DG002, High severity) to enable mechanistic link analysis
- **Regulatory pathway**: Evaluate feasibility of HSA registration for Avanafil as a prerequisite for any Singapore-based clinical investigation
- **Model artefact filtering**: Exclude veterinary disease predictions (malignant catarrh, rank #3; infectious bovine rhinotracheitis, rank #4) and the deprecated ontology concept (obsolete susceptibility to ischemic stroke, rank #7) from future evaluation cycles to improve signal-to-noise ratio in prediction outputs