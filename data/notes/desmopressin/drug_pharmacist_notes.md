# Desmopressin: From von Willebrand Disease & Mild Haemophilia A to Congenital Prothrombin Deficiency

## One-Sentence Summary

Desmopressin (DDAVP) is a synthetic vasopressin analogue approved globally for von Willebrand disease, mild haemophilia A, and diabetes insipidus, though it is not currently registered in Singapore; its haemostatic mechanism centres on releasing von Willebrand factor (vWF) and Factor VIII from vascular endothelial cells.
The TxGNN model predicts it may have utility in **congenital prothrombin deficiency** with a prediction score of **99.70%**, however no clinically relevant trials exist and only **4 publications** provide highly indirect supporting evidence for this specific indication.
At this stage, the prediction is best classified as a **research question** requiring mechanistic validation before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; internationally approved for von Willebrand disease, mild haemophilia A, and central diabetes insipidus |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why Is This Prediction Reasonable?

Desmopressin acts on V2 receptors expressed on vascular endothelial cells, triggering exocytosis of Weibel-Palade bodies and releasing large multimeric vWF and co-stored Factor VIII into the circulation. The resulting surge in vWF enhances platelet adhesion to damaged vessel walls (primary haemostasis), while the rise in Factor VIII accelerates the intrinsic coagulation cascade (secondary haemostasis). This dual haemostatic effect has been validated across multiple bleeding disorders — most robustly in von Willebrand disease Type 1 and mild haemophilia A — and gives desmopressin a broad pharmacological footprint in coagulopathies.

Congenital prothrombin deficiency (Factor II deficiency) is a rare autosomal recessive disorder that disrupts the final common coagulation pathway. Prothrombin is cleaved to thrombin by the prothrombinase complex (Factor Xa / Factor Va / Ca²⁺ / phospholipid), and thrombin is indispensable for converting fibrinogen to fibrin and consolidating the platelet plug. Critically, desmopressin has no direct capacity to supplement prothrombin synthesis or compensate for Factor II deficiency — its vWF and FVIII release pathway operates upstream and in a parallel arm of the coagulation cascade, leaving the prothrombin-thrombin axis unaffected.

The TxGNN model's high-ranking prediction most plausibly reflects a network-level similarity: prothrombin deficiency co-clusters with other congenital coagulopathies in the knowledge graph, several of which do respond to desmopressin. One case report (PMID 2607619) documents DDAVP administration in combined Factor V + Factor VIII deficiency, illustrating adjunctive haemostatic value in mixed coagulopathies; however, this does not constitute evidence for isolated prothrombin deficiency. The overall mechanistic connection is indirect and speculative, and should be regarded as a hypothesis-generating signal rather than a therapeutic lead.

---

## Clinical Trial Evidence

The only retrieved trial is not relevant to this indication:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04567511](https://clinicaltrials.gov/study/NCT04567511) | Phase 4 | Recruiting | 20 | Evaluates **emicizumab** (a bispecific antibody bridging FIXa and FX) in mild haemophilia A with FVIII activity 5–30%. Study drug is not desmopressin; indication is FVIII deficiency, not prothrombin deficiency. Graded irrelevant (Grade C). |

> There are currently **no registered clinical trials** evaluating desmopressin for congenital prothrombin deficiency.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Narrative Review | *Drugs* | Broad review of congenital bleeding disorder management; affirms desmopressin efficacy in mild haemophilia A and vWD; does not address prothrombin deficiency |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case Report | *Rinsho Ketsueki* | DDAVP administered to a patient with combined Factor V + Factor VIII deficiency; prolonged bleeding time partially corrected, suggesting adjunctive haemostatic benefit in mixed coagulopathies — the closest available evidence, though still mechanistically distinct from pure prothrombin deficiency |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case Report | *Rinsho Ketsueki* | Caesarean section managed with Factor VIII concentrate replacement in combined Factor V + Factor VIII deficiency; provides clinical context for managing rare combined coagulopathies but offers no direct DDAVP data for prothrombin deficiency |
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | *Autoimmunity Reviews* | Acquired haemophilia A due to anti-FVIII autoantibodies; covers pathophysiology and treatment; not related to congenital prothrombin deficiency |

---

## Singapore Market Information

Desmopressin is **not currently registered in Singapore**. No marketing authorisations are on record with the Health Sciences Authority (HSA). There are therefore no approved indications, dosage forms, or product-specific safety warnings available through the Singapore regulatory pathway.

> Clinicians seeking prescribing information should refer to equivalent regulatory agencies (e.g., the US FDA, EMA, or Japan PMDA) or the manufacturer's international package insert.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Based on the broader evidence pack, desmopressin carries a **procoagulant / pro-thrombotic signal** in specific subpopulations. In particular:
>
> - **Type 2B von Willebrand disease** and **pseudo-von Willebrand disease (PT-VWD)**: contraindicated — desmopressin-induced release of ultra-large vWF multimers precipitates thrombocytopenia and thrombosis.
> - **Thrombotic thrombocytopenic purpura (TTP)**: contraindicated — case reports document clinical deterioration (PMID 15499705; PMID 21921792) following DDAVP administration in TTP due to ADAMTS13 deficiency.
> - **Inherited thrombophilia** (e.g., Factor V Leiden, Protein C/S deficiency): caution warranted — enhanced vWF multimer release may aggravate pre-existing thrombotic risk.
>
> These signals are not specific to the prothrombin deficiency indication but are relevant to the overall safety profile of desmopressin and must be assessed before any repurposing study is designed.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Despite a high TxGNN score (99.70%), the mechanistic link between desmopressin's vWF/FVIII release action and congenital prothrombin deficiency is indirect and does not address the core Factor II deficiency pathway; no clinical trials or direct literature evidence support this specific indication, and the current evidence base (L4) is insufficient to justify proceeding without foundational mechanistic work.

**To proceed, the following is needed:**

- **Mechanistic clarification**: Determine whether enhanced primary haemostasis (via vWF-GP1b axis) or elevated FVIII could provide a clinically meaningful adjunctive haemostatic benefit in patients with prothrombin deficiency who also have concurrent vWF or FVIII involvement
- **Literature deep-dive**: Conduct a targeted systematic search for case reports or expert opinions describing DDAVP use in congenital prothrombin deficiency (hypoprothrombinemia), particularly in perioperative or obstetric settings where prothrombin concentrate is unavailable
- **MOA gap resolution**: Retrieve full DrugBank mechanism-of-action data (DG002) to strengthen the plausibility analysis
- **Safety baseline**: Download and parse the TFDA/HSA equivalent package insert (DG001) to identify contraindications and warnings relevant to coagulation disorders before any clinical design
- **Preclinical investigation**: If the mechanistic review is supportive, consider an in vitro or animal-model study in prothrombin-deficient systems to quantify any DDAVP-attributable haemostatic improvement
- **Expert consultation**: Engage haematologists specialising in rare coagulation factor deficiencies to assess clinical plausibility and unmet need