---
layout: default
title: Turoctocog Alfa
parent: Low Evidence (L5)
nav_order: 1026
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Turoctocog alfa: From Haemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Turoctocog alfa is a recombinant factor VIII (FVIII) replacement product, marketed in Singapore as Novoeight, and is used for haemophilia A.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The high score appears to reflect graph proximity to haemostasis terms rather than a plausible mechanism, so the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Haemophilia A (FVIII replacement; the Singapore licence records contain no indication text) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, turoctocog alfa is a recombinant FVIII product. It supplies the missing clotting factor in haemophilia A, where the tenase complex (FVIIIa/FIXa) cannot form properly.

The predicted disease is a different kind of problem. Release disorders are intrinsic platelet defects in granule secretion and signalling. FVIII levels are normal in these patients, so supplying more FVIII does not address the primary defect. The 99.99% score most likely comes from the disease sitting close to haemostasis terms in the knowledge graph. **The mechanistic rationale is weak.**

The other top-ranked predictions show the same pattern: they are mostly platelet-related or von Willebrand-related bleeding disorders.

| Rank | Predicted Disease | Score | Assessment |
|----|------|------|------|
| 2 | Pseudo-von Willebrand disease | 99.99% | Gain-of-function GPIbα defect; plasma FVIII is usually normal, so the rationale is weak. Standard care is platelet transfusion or VWF-directed therapy. |
| 3 | Glanzmann thrombasthenia | 99.99% | Integrin αIIbβ3 defect; FVIII would not correct it. Platelet transfusion and recombinant FVIIa are established options. |
| 4 | Scott syndrome | 99.95% | Loss of the phosphatidylserine surface on platelets; the link to FVIII is indirect and speculative. |
| 5 | Acquired coagulation factor deficiency | 99.95% | The most plausible entry, but only if the deficiency is specifically FVIII (e.g., acquired hemophilia A). Autoantibody inhibitors usually neutralise human recombinant FVIII, and the term is too generic. Classed as a research question only. |
| 6 | Bleeding diathesis due to a collagen receptor defect | 99.91% | Platelet-intrinsic adhesion defect; FVIII does not address it. |
| 7 | Haemorrhagic disorder due to constitutional thrombocytopenia | 99.91% | Bleeding is due to low platelet counts, not FVIII deficiency. |
| 8 | "Flood factor deficiency" | 99.61% | Ambiguous name, possibly a knowledge-graph artifact; needs ontology curation before evaluation. |
| 9 | Thrombotic thrombocytopenic purpura | 99.54% | ADAMTS13 deficiency drives thrombosis. A procoagulant factor runs against treatment, so this is a safety concern, not an opportunity. |
| 10 | Hereditary thrombocytosis with transverse limb defect | 99.52% | No plausible link to FVIII replacement. |

None of the ten predictions has any registered trial or published literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Four Novoeight licences are registered (powder and solvent for solution for injection). The records do not include approved indication text.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16109P | Novoeight Powder and Solvent for Solution for Injection 250 IU/vial | Injection, powder, for solution |
| SIN16111P | Novoeight Powder and Solvent for Solution for Injection 500 IU/vial | Injection, powder, for solution |
| SIN16110P | Novoeight Powder and Solvent for Solution for Injection 1000 IU/vial | Injection, powder, for solution |
| SIN16713P | Novoeight Powder and Solvent for Solution for Injection 2000 IU/vial | Injection, powder, for solution |

The manufacturer is Novo Nordisk A/S (Kalundborg and Hagedornsvej sites), with the solvent supplied by Vetter Pharma-Fertigung.

---

## Safety Considerations

- **Thrombotic risk**: For thrombotic thrombocytopenic purpura (rank 9), giving a procoagulant factor such as FVIII is mechanistically opposed to treatment, and elevated FVIII is a recognised thrombotic risk factor. This indication should not be pursued.
- **Inhibitors**: In acquired FVIII deficiency with autoantibody inhibitors, human recombinant FVIII is usually neutralised, so efficacy is doubtful.

No drug interaction records were found. For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and the mechanism does not fit: the bleeding in the predicted diseases is platelet-mediated, not FVIII-mediated. The high TxGNN score appears to be an artifact of graph proximity.

**To proceed, the following is needed:**
- HSA package insert (warnings, contraindications, approved indication), currently a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- Ontology curation of ambiguous disease terms such as "flood factor deficiency"
- For the one hypothesis worth exploring, acquired coagulation factor deficiency (acquired haemophilia A), a literature review of inhibitor-related efficacy before any further work
- Exclusion of thrombotic thrombocytopenic purpura from further evaluation on safety grounds

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

