# Deferasirox: From Transfusion-Dependent Iron Overload to HIV Infectious Disease

## One-Sentence Summary

Deferasirox is an oral iron chelator globally approved (FDA 2005, EMA 2006) for the treatment of chronic iron overload caused by repeated blood transfusions, primarily in patients with β-thalassemia and other transfusion-dependent anaemias.
The TxGNN model predicts it may be effective for **HIV Infectious Disease**, hypothesising that intracellular iron chelation could suppress HIV-1 viral replication via the Tat-LTR transactivation pathway.
Current supporting evidence consists of **0 clinical trials** and **2 mechanistic publications**, both limited to in vitro or commentary-level data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic transfusion-dependent iron overload (β-thalassemia and other anaemias) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L4 (preclinical / mechanistic studies only) |
| Singapore Market Status | Not registered |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Deferasirox is a tridentate bis-hydroxyphenyl-triazole oral iron chelator that selectively binds ferric iron (Fe³⁺) with high affinity, forming a stable complex excreted primarily via the faeces. Its proven efficacy in transfusion-dependent iron overload has been established across multiple Phase 3 trials (e.g., the ESCALATOR trial, n = 586), and its iron-lowering effect on serum ferritin and liver iron concentration (LIC) is well-characterised.

The predicted link to HIV rests on a biologically plausible but highly indirect mechanism. HIV-1 replication depends on the Transactivator of Transcription (Tat) protein, which activates the HIV-1 Long Terminal Repeat (LTR) promoter to drive viral gene expression. Endolysosomal iron has been shown to modulate Tat oligomerisation: higher intracellular Fe³⁺ promotes monomeric Tat activity, while iron restriction — such as that induced by an iron chelator like Deferasirox — promotes Tat oligomerisation and upregulates β-catenin expression, thereby suppressing LTR-driven transcription. In principle, reducing intracellular iron bioavailability could limit HIV-1 replication as an adjunct mechanism.

However, this reasoning is entirely grounded in in vitro observations. HIV-1 replication is a complex multi-step process, and iron chelation has not been demonstrated to exert clinically meaningful antiviral effects in human subjects. The mechanistic link is scientifically interesting but remains speculative without supporting animal or clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Mechanistic / In vitro | Journal of Neurovirology | Demonstrated that endolysosomal iron restricts HIV-1 Tat-mediated LTR transactivation by promoting Tat oligomerisation and upregulating β-catenin; raises hypothesis that iron chelation may suppress Tat-driven HIV-1 replication in the CNS context of HAND |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Drug Review / Commentary | Journal of the American Pharmacists Association | Early post-approval review covering Deferasirox alongside other newly approved agents (ramelteon, tipranavir, nepafenac); describes its approved iron chelation indication; no direct antiviral efficacy data |

---

## Singapore Market Information

Deferasirox is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No product licences are on record; the drug is unavailable through the standard Singapore regulatory pathway. Clinicians requiring access would need to apply via the Special Access Route (SAR) or Therapeutic Products Act exemptions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** No safety data (warnings, contraindications, or drug interactions) were retrieved in this Evidence Pack. The TFDA package insert (DG001) and DrugBank MOA entry (DG002) are identified as blocking data gaps. Clinicians should consult the HSA-recognised reference product label (e.g., Exjade® / Jadenu®) directly.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for Deferasirox in HIV infectious disease is mechanistically plausible at the molecular level (iron-Tat-LTR pathway), but is supported only by a single in vitro mechanistic study and a general drug review — constituting Level L4 evidence. No clinical trials have been conducted or registered for this indication, and there is no in vivo or translational data bridging the in vitro finding to human HIV disease. The drug is also unregistered in Singapore, introducing an additional access barrier.

**To proceed, the following is needed:**

- Preclinical animal studies (e.g., HIV-infected humanised mouse models) to evaluate whether systemic iron chelation with Deferasirox produces measurable antiviral effects in vivo
- Pharmacokinetic modelling to determine whether clinically achievable plasma and intracellular concentrations of Deferasirox are sufficient to replicate the iron-restriction effect observed in vitro
- Safety data retrieval: download and parse the Exjade®/Jadenu® SmPC or FDA label to address the blocking DG001 gap (key warnings and contraindications), particularly renal toxicity, hepatic toxicity, and gastrointestinal haemorrhage — all known class effects
- DrugBank MOA data retrieval (DG002) to formally confirm the mechanism and enable structured pharmacological comparison
- Review of any HIV-iron co-morbidity literature (e.g., iron overload in HIV-infected patients receiving multiple transfusions) to identify whether an at-risk subpopulation might be an appropriate early-stage study target
- If preclinical results are positive: design a Phase 1/2 pilot study in a defined population (e.g., HIV-positive patients with documented iron overload) before broader indication pursuit