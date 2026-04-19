# Ambrisentan: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

## One-Sentence Summary

Ambrisentan is a selective endothelin A (ETA) receptor antagonist approved globally for the treatment of pulmonary arterial hypertension (PAH).
The TxGNN model predicts it may be effective for **Pulmonary Arteriovenous Malformation (PAVM)**, with **0 clinical trials** and **1 publication** (a single case report) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary Arterial Hypertension (PAH) |
| Predicted New Indication | Pulmonary Arteriovenous Malformation |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory database. Based on known scientific literature, Ambrisentan is a selective ETA receptor antagonist: it blocks endothelin-1 (ET-1) from binding to ETA receptors on pulmonary vascular smooth muscle cells, thereby reducing vasoconstriction and inhibiting pathological vascular remodeling. This mechanism underpins its approved use in PAH.

The proposed mechanistic link runs through hereditary hemorrhagic telangiectasia (HHT). HHT is caused by mutations in *Endoglin* or *ALK1* — genes encoding components of the TGF-β signaling pathway — and can simultaneously manifest as both PAVM and PAH in the same patient. Because ET-1 signaling and the Endoglin/ALK1 pathway are known to interact at the endothelial cell level, there is an indirect biological rationale for exploring ETA antagonism in this disease context.

However, this connection remains indirect and mechanistically weak for PAVM specifically. Pulmonary arteriovenous malformations are primarily structural abnormalities — persistent, abnormal direct connections between pulmonary arteries and veins — arising from defective endothelial development rather than ongoing vasoconstrictive or proliferative signaling. ETA antagonism addresses functional vascular tone and remodeling; it has no established role in correcting fixed anatomical malformations. The elevated TxGNN score most likely reflects the model's knowledge graph proximity between PAH and HHT-related vascular nodes, rather than a direct pharmacological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case Report | World Journal of Clinical Cases | A rare case of HHT presenting with concurrent PAH; family genetic analysis of *Endoglin/ALK1* mutations performed. Ambrisentan was used to manage the PAH component; PAVM was not treated with Ambrisentan, and the report does not establish efficacy for PAVM. |

---

## Singapore Market Information

Ambrisentan is currently **not registered in Singapore**. No authorization records or approved indications are available. Patients in Singapore requiring Ambrisentan would need to obtain it through special access pathways.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Globally, Ambrisentan (brand names Letairis®, Volibris®) carries a boxed warning for **embryo-fetal toxicity** (Category X / contraindicated in pregnancy) and is distributed under a Risk Evaluation and Mitigation Strategy (REMS) in the United States. Peripheral edema and hepatotoxicity monitoring requirements should be considered in any use scenario. Drug interaction risk with CYP3A4 and P-glycoprotein substrates/inhibitors is also relevant.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole supporting evidence for PAVM is a single case report documenting Ambrisentan's use for the PAH component in an HHT patient — not for PAVM itself. There is no mechanistic basis for using an ETA receptor antagonist to correct structural pulmonary arteriovenous malformations, and the drug is not currently registered in Singapore, creating an additional regulatory barrier.

**To proceed, the following is needed:**
- Preclinical studies demonstrating a functional role of ETA receptor signaling in PAVM formation or progression
- Mechanistic investigation of Endoglin/ALK1–ET-1 signaling cross-talk in HHT-associated PAVM models
- Case series or prospective observational data in HHT patients with concurrent PAVM and PAH receiving ETA antagonists
- Singapore Health Sciences Authority (HSA) registration pathway assessment for Ambrisentan
- Full MOA documentation via DrugBank API to enable complete mechanistic analysis

---

> **Supplementary Note — Other High-Priority Predictions from This Evidence Pack**
>
> While the top-ranked TxGNN prediction (PAVM) warrants a Hold decision, the evidence pack contains three additional PAH subtypes with substantially stronger clinical evidence that merit separate, more detailed evaluation:
>
> | Indication | Evidence Level | Decision | Key Evidence |
> |---|---|---|---|
> | PAH associated with Congenital Heart Disease (Rank 2) | L2 | Proceed with Guardrails | 9 clinical trials; 17 publications; Phase 3b COMPLETED (n=134, Chinese cohort) |
> | PAH associated with Connective Tissue Disease (Rank 3) | L2 | Proceed with Guardrails | 3 clinical trials (2 COMPLETED); 19 publications; systematic review + meta-analysis |
> | PAH associated with HIV Infection (Rank 5) | L1 | Proceed with Guardrails | Phase 3 double-blind RCT COMPLETED (n=64); 4 publications |
>
> These three indications share a common ETA receptor pathway with idiopathic PAH (WHO Group 1), have direct mechanistic overlap, and represent clinically validated repurposing candidates that warrant full individual evaluation reports.