# Apixaban: From Atrial Fibrillation / VTE to Migraine Disorder

## One-Sentence Summary

Apixaban is a selective direct oral anticoagulant (Factor Xa inhibitor) widely used for stroke prevention in atrial fibrillation and venous thromboembolism treatment.
The TxGNN model predicts it may have potential for **Migraine Disorder** (TxGNN Score 99.02%),
but existing evidence is limited to **1 indirectly relevant clinical trial** and **4 publications** — notably, two case reports show a **negative signal specific to Apixaban**, suggesting the evidence base is insufficient for repurposing at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atrial fibrillation (stroke prevention), venous thromboembolism treatment and prevention |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on established pharmacology, Apixaban is a selective, direct, and reversible inhibitor of Factor Xa (FXa) — the convergence point of both the intrinsic and extrinsic coagulation pathways. By blocking FXa, Apixaban prevents thrombin generation and fibrin clot formation without directly inhibiting thrombin itself. This places it in the class of direct oral anticoagulants (DOACs) along with rivaroxaban and edoxaban.

The mechanistic hypothesis linking Apixaban to migraine centres on patent foramen ovale (PFO)-related paradoxical microembolism. In susceptible individuals, right-to-left shunting of microemboli through a PFO may trigger cortical spreading depression (CSD) — the neurophysiological substrate of migraine aura. By suppressing micro-thrombus formation, FXa inhibition could theoretically reduce this embolic trigger. Additionally, FXa has been shown to activate pro-inflammatory protease-activated receptors (PAR-1 and PAR-2), which may modulate neurogenic inflammation relevant to migraine pathophysiology.

However, the clinical picture is cautionary. Two case reports specifically document that warfarin — a Vitamin K Antagonist (VKA) — was effective in controlling migraine, whereas switching to Apixaban led to migraine recurrence within weeks. This discrepancy suggests that if anticoagulation benefits migraine at all, the mechanism may depend on VKA-specific effects (e.g., suppression of Protein S/C pathways, broader platelet interactions, or anti-inflammatory effects via carboxylation-dependent proteins) that are not replicated by direct FXa inhibition. No randomised controlled trial has specifically tested Apixaban for migraine treatment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure vs. oral anticoagulants vs. antiplatelet therapy for stroke recurrence prevention. Migraine was a secondary observation endpoint only; trial was not designed to test migraine treatment. Apixaban was not the specific study drug. Relevance to Apixaban-migraine indication is low (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Small Trial / Pilot | *Lupus* | Retrospective study of 75 patients with refractory migraine and antiphospholipid antibodies (aPL). Antithrombotic therapy showed symptomatic improvement in a subgroup. Provides indirect mechanistic rationale for anticoagulation in aPL-positive migraine, but drug-specific data for Apixaban is absent. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case Report + Literature Review | *The Neurologist* | **⚠️ Negative signal**: Migraine with aura **worsened** after initiating Apixaban. Review of literature confirms the impact of DOACs on migraine is unclear and controversial. Current data is scarce. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case Report | *Headache* | **⚠️ Negative signal (Apixaban-specific)**: 55-year-old female experienced complete migraine remission on warfarin for 12 years; symptoms returned within 3 weeks of switching to Apixaban, and resolved again upon resuming warfarin. Suggests VKA and FXa inhibitors may operate through different mechanisms. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case Report | *Headache* | Vestibular migraine resolved on a combination of warfarin and topiramate. Supports anticoagulation hypothesis for specific migraine subtypes but involves warfarin, not Apixaban. |

---

## Singapore Market Information

Apixaban is **not currently registered** with the Health Sciences Authority (HSA) in Singapore per the data available in this Evidence Pack (0 registered licences). No authorisation records are available.

> **Note:** This finding is unexpected given Apixaban (Eliquis®) has received regulatory approval in major markets including the US (FDA), EU (EMA), Japan (PMDA), and many others. It is recommended to re-verify current HSA registration status directly via the [HSA Drug Database](https://www.hsa.gov.sg/therapeutic-products/listing-of-registered-therapeutic-products) before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information. No warning, contraindication, or drug interaction data was available in this Evidence Pack.

> **Important data gap:** Apixaban carries a well-known class risk of major and clinically relevant bleeding. Before any off-label use is considered, full prescribing information — including contraindications in patients with active bleeding, severe renal impairment, and concomitant strong dual inhibitors of CYP3A4 and P-gp — must be reviewed from the approved label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score (99.02%) to migraine disorder, but the available clinical evidence is weak (L4) and includes direct negative signals: two case reports specifically document that migraine controlled by warfarin **returned** after switching to Apixaban. This drug-class distinction — VKA versus direct FXa inhibitor — is mechanistically significant and undermines the repurposing hypothesis for Apixaban specifically.

**To proceed, the following is needed:**

- **Resolve the Apixaban-specific negative signal**: The warfarin-responsive / Apixaban-non-responsive pattern in existing case reports must be addressed before any clinical investment. Is there a pathophysiological basis for this difference (e.g., Protein C/S-dependent pathways, broader VKA platelet effects)?
- **Identify the target patient subgroup**: Migraine associated with antiphospholipid antibodies (aPL) or PFO may represent a distinct subgroup where anticoagulation is rational. A prospective cohort study in this subgroup is warranted before any RCT.
- **MOA data**: Retrieve full mechanistic profile from DrugBank (DB06605) to support or refute the neuroinflammatory PAR-1/PAR-2 hypothesis.
- **Safety data**: Obtain TFDA/HSA package insert to complete the S1 safety screening; this is currently a **blocking data gap**.
- **Verify Singapore registration status**: Confirm whether Eliquis® holds current HSA approval for its approved indications.

---

### 📋 Other Notable TxGNN Predictions (Summary)

| Rank | Indication | Evidence Level | Recommendation | Key Comment |
|------|-----------|---------------|---------------|-------------|
| 4 | Rheumatoid Arthritis | L4 | Research Question | Preclinical study (PMID 32141012) shows anti-arthritic effects via JAK2/STAT3 & MAPK inhibition in rat model. Most promising mechanistic lead outside of thrombosis. |
| 8 | Pulmonary Hypertension | **L3** | Research Question | Phase 2 RCT protocol exists for SSc-related PAH (PMID 27932335); CTEPH data available (PMID 39468095). Highest evidence base across all predictions, but current ESC/ERS guidelines do not recommend routine anticoagulation in PAH. |
| 1 | Migraine Disorder | L4 | **Hold** | Negative Apixaban-specific signals in case literature. |
| 3 | Leprosy | L5 | Hold | Single case report involves Apixaban used for PE complication, not leprosy treatment. No mechanistic basis. |
| 6 | Prinzmetal Angina | L5 | Hold | Vasospasm-mediated disease; FXa inhibition has no pharmacological relevance to coronary smooth muscle contraction. |
| 7 | Brachydactyly-Syndactyly Syndrome | L5 | Hold | Genetic developmental disorder (HOXD/GJA1 mutations); no connection to coagulation cascade. |
| 9 | Colobomatous Microphthalmia | L5 | Hold | Congenital developmental syndrome (STRA6 mutation); no biological overlap with FXa. |
| 10 | Kyphoscoliotic Heart Disease | L5 | Hold | Standard VTE indication if VTE risk is elevated; does not constitute repurposing. |

> **Recommendation for further prioritisation:** Among all 10 predictions, **pulmonary hypertension** (especially SSc-related PAH and CTEPH) and **rheumatoid arthritis** offer the most scientifically grounded repurposing hypotheses and should be considered for dedicated evidence review before migraine disorder.

---

*Report generated: 2026-04-05 | Evidence Pack Version: v4 | Candidate ID: TW-DB06605-multi*
*⚠️ This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*