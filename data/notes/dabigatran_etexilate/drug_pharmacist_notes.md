# Dabigatran Etexilate: From Anticoagulation to Sclerosing Cholangitis

---

## One-Sentence Summary

Dabigatran etexilate (Pradaxa) is a direct thrombin inhibitor (DTI) approved globally for prevention of stroke in non-valvular atrial fibrillation and treatment of venous thromboembolism.
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**, with **0 clinical trials** and **1 tangentially related publication** currently identified — the sole literature entry concerns a different drug (cilofexor) and does not provide direct evidence for dabigatran in this indication.
At this stage, the repurposing signal rests entirely on model prediction without experimental or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anticoagulation: Atrial fibrillation (stroke prevention), VTE treatment and prevention |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for dabigatran etexilate is not captured in this evidence pack. Based on established pharmacology, dabigatran etexilate is a prodrug hydrolyzed in vivo to dabigatran — a potent, competitive direct inhibitor of thrombin (Factor IIa). By blocking thrombin, it prevents fibrinogen-to-fibrin conversion, inhibits thrombin-induced platelet aggregation, and reduces pro-inflammatory signaling through protease-activated receptors (PAR-1 and PAR-4).

The mechanistic rationale for dabigatran in sclerosing cholangitis (PSC) draws on evidence that thrombin can activate PAR-2 on hepatic stellate cells, promoting their proliferation and contributing to periductal fibrosis — a defining feature of PSC. If this pathway is operative in bile duct fibrosis, thrombin inhibition could, in theory, slow fibrotic progression around the intrahepatic and extrahepatic bile ducts.

This connection, however, is highly speculative. There are no published animal model studies or human clinical data validating dabigatran's antifibrotic activity in PSC or secondary sclerosing cholangitis. The TxGNN score likely reflects topological proximity between coagulation and liver disease nodes in the knowledge graph rather than a validated drug–disease relationship. Without preclinical proof-of-concept data, this prediction cannot advance beyond hypothesis generation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for dabigatran etexilate in sclerosing cholangitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | DDI Study (non-clinical) | *Clinical Pharmacokinetics* | Evaluated the drug-drug interaction potential of **cilofexor** (a selective FXR agonist in development for PSC and NASH) as victim and perpetrator — dabigatran is not the investigational drug; PSC appears only as the disease context for cilofexor's clinical programme |

> ⚠️ **Important caveat:** This publication does not study dabigatran as a treatment for sclerosing cholangitis. It is included because it co-mentions PSC and a drug with DDI potential; it provides no efficacy or mechanistic evidence for dabigatran in this disease.

---

## Singapore Market Information

Dabigatran etexilate is **not currently registered** with the Health Sciences Authority (HSA) of Singapore. No product authorisations were identified in this dataset.

> Note: Dabigatran etexilate (Pradaxa®) is registered in many other jurisdictions (EU, US, Japan, Taiwan) for atrial fibrillation and VTE indications. HSA registration status should be independently verified via the HSA PRISM database.

---

## Safety Considerations

Detailed HSA-approved labelling, contraindications, and drug interaction data were not available in this evidence pack. Please refer to the package insert for complete safety information.

> **Known DDI signal (from literature, not DDI database):** Although the structured DDI query returned no results, the evidence pack's HIV indication literature (ranks 10) contains multiple cohort studies and case series demonstrating that ritonavir- and cobicistat-boosted antiretroviral agents elevate dabigatran plasma exposure 2–4-fold via P-glycoprotein inhibition, substantially increasing bleeding risk. This is a clinically significant interaction that must be assessed in any future use scenario.

---

## Notable Secondary Finding: Rheumatoid Arthritis (Rank 9)

While not the top-ranked prediction, the **rheumatoid arthritis** indication (TxGNN score 98.70%) was flagged within this evidence pack as carrying the strongest mechanistic rationale of the entire batch:

- Thrombin activates PAR-1 on synovial fibroblasts → NF-κB → IL-6 / TNF-α / MMP release
- Thrombin modulates the kallikrein–kinin system (KKS) → bradykinin accumulation → B1/B2 receptor activation → synovial vasodilation and pain
- Intra-articular fibrin deposition amplifies local inflammation

A 2022 rat study (PMID [36142208](https://pubmed.ncbi.nlm.nih.gov/36142208/)) directly demonstrated that dabigatran improved CFA-induced arthritis by modulating the KKS. This is the only indication in this dataset supported by an animal model using dabigatran itself. It warrants separate, dedicated evaluation at evidence-gathering stage (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score (99.82%) to sclerosing cholangitis, but this reflects knowledge graph connectivity rather than biological validation. The one retrieved publication concerns a different drug; there are zero clinical trials, zero animal studies, and zero mechanistic experiments supporting dabigatran for PSC. The drug is also unregistered in Singapore, adding a regulatory barrier. The overall evidence package does not meet the threshold to proceed to safety screening.

**To proceed, the following is needed:**

- **Preclinical proof-of-concept:** Test dabigatran in an established PSC mouse model (e.g., Mdr2⁻/⁻ mice) to assess antifibrotic and cholestasis-modifying effects
- **Mechanism validation:** Confirm whether thrombin/PAR-2 signalling is active in bile duct fibroblasts and hepatic stellate cells in PSC lesions
- **Safety data gap closure:** Retrieve full HSA/TFDA prescribing information, contraindications, black-box warnings, and complete DDI profile
- **Singapore regulatory pathway assessment:** Determine whether HSA registration or a named-patient/clinical trial exemption would be required prior to any clinical use
- **Reprioritisation consideration:** Given the stronger mechanistic and preclinical evidence base for rheumatoid arthritis (PMID 36142208), consider whether RA should be advanced in parallel as the primary repurposing hypothesis for dabigatran etexilate