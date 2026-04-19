# Atovaquone: From Pneumocystis Pneumonia to Toxoplasmosis

## One-Sentence Summary

Atovaquone is an antiprotozoal agent used for the treatment and prophylaxis of *Pneumocystis jirovecii* pneumonia (PCP) and malaria (combined with proguanil as Malarone).
The TxGNN model predicts it may be effective for **Toxoplasmosis**, with strong mechanistic plausibility supported by **3 clinical trials** and **20 publications**.
Among all 10 TxGNN predictions analysed, toxoplasmosis carries the highest evidence level (L2) and is the only indication recommended for **Proceed with Guardrails**.

> **Note on top TxGNN ranking**: The highest TxGNN-ranked prediction is **Leprosy** (94.24%, L5 — model prediction only, no supporting clinical studies). This report focuses on **Toxoplasmosis** (TxGNN score 86.67%, Evidence Level L2) as the most actionable and evidence-supported repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pneumocystis jirovecii Pneumonia (PCP); Malaria prophylaxis/treatment |
| Predicted New Indication | Toxoplasmosis |
| TxGNN Prediction Score | 86.67% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank was not available for this analysis. However, based on known pharmacology, Atovaquone is a hydroxynaphthoquinone antiprotozoal whose primary mechanism is direct inhibition of the **cytochrome bc1 complex** (ubiquinol:cytochrome c oxidoreductase, Complex III) in the mitochondrial electron transport chain of protozoa. This disrupts the proton gradient and collapses the mitochondrial membrane potential, halting ATP synthesis and pyrimidine biosynthesis essential for parasite survival.

*Toxoplasma gondii* is an **apicomplexan parasite**—the same broad taxonomic class as *Pneumocystis jirovecii*—and possesses a functional mitochondrial electron transport chain that serves as a validated and conserved drug target. The mechanistic link between Atovaquone's antiprotozoal action and *T. gondii* is therefore directly analogous to its activity against PCP: same target class, same pharmacological principle. This biological plausibility is strong, not speculative.

Beyond mechanism, Atovaquone has established real-world use as an **alternative prophylaxis agent** for toxoplasmosis in immunocompromised patients (e.g., solid organ and stem cell transplant recipients, HIV/AIDS patients) who cannot tolerate first-line trimethoprim-sulfamethoxazole (TMP-SMX). This clinical precedent — documented in international guidelines and retrospective studies — elevates the evidence base well above pure model inference and directly supports the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|--------------|-------|--------|-----------|--------------|
| [NCT00000794](https://clinicaltrials.gov/study/NCT00000794) | Phase 2 | Completed | 100 | Randomised open-label trial comparing Atovaquone + pyrimethamine vs. Atovaquone + sulfadiazine for toxoplasmic encephalitis in AIDS patients; primary outcomes were efficacy, safety, and tolerance of Atovaquone-based combination regimens |
| [NCT00001994](https://clinicaltrials.gov/study/NCT00001994) | N/A | Completed | N/A | Pilot study evaluating Atovaquone as salvage treatment for CNS toxoplasmosis in HIV/AIDS patients who failed or were intolerant of standard pyrimethamine-sulfadiazine therapy; early proof-of-concept evidence |
| [NCT01479361](https://clinicaltrials.gov/study/NCT01479361) | Phase 1 | Completed | 36 | Pharmacokinetic interaction study assessing the impact of atazanavir-ritonavir and efavirenz on Atovaquone exposure in HIV-infected volunteers; provides critical PK context for toxoplasmosis management in the HIV population |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26392504](https://pubmed.ncbi.nlm.nih.gov/26392504/) | 2015 | Systematic Review | Antimicrobial Agents and Chemotherapy | Systematic evaluation of all clinically available medicines with anti-*T. gondii* activity; Atovaquone identified as a key agent for toxoplasmic encephalitis and ocular toxoplasmosis, with activity against both tachyzoites and bradyzoite cysts noted |
| [30209035](https://pubmed.ncbi.nlm.nih.gov/30209035/) | 2018 | Narrative Review | Clinical Microbiology Reviews | Comprehensive treatment review covering historical perspective, animal models, and current clinical practice; discusses Atovaquone as an alternative to pyrimethamine-sulfadiazine for patients failing or intolerant of gold-standard therapy |
| [7588086](https://pubmed.ncbi.nlm.nih.gov/7588086/) | 1995 | Review | Drugs | Foundational pharmacological review of Atovaquone covering PCP and toxoplasmosis treatment in AIDS patients; establishes clinical efficacy profile and tolerability advantage over conventional regimens |
| [8305784](https://pubmed.ncbi.nlm.nih.gov/8305784/) | 1993 | Review | Annals of Pharmacotherapy | Early comprehensive review of Atovaquone's pharmacology, pharmacokinetics, clinical efficacy, and safety profile in opportunistic infections including toxoplasmosis |
| [34595988](https://pubmed.ncbi.nlm.nih.gov/34595988/) | 2021 | Animal Study | Ultrastructural Pathology | Histopathological and ultrastructural assessment of Atovaquone-proguanil combination in chronic murine toxoplasmosis; evaluates tissue-level cyst burden and treatment response |
| [25309522](https://pubmed.ncbi.nlm.nih.gov/25309522/) | 2014 | Animal Study | Frontiers in Microbiology | Novel synergistic combination of diclazuril plus Atovaquone in murine toxoplasmosis model; demonstrates enhanced efficacy against both acute disease and tissue cysts |
| [25210646](https://pubmed.ncbi.nlm.nih.gov/25210646/) | 2014 | Animal Study | International Journal of Clinical Medicine | Synergistic protective efficacy of Atovaquone and diclazuril in fetal-maternal toxoplasmosis; addresses the critical unmet need of congenital infection treatment |
| [10471572](https://pubmed.ncbi.nlm.nih.gov/10471572/) | 1999 | Animal Study | Antimicrobial Agents and Chemotherapy | Dose-response characterisation of clindamycin + Atovaquone synergy in acute murine toxoplasmosis; informs combination dosing rationale for clinical use |
| [40788706](https://pubmed.ncbi.nlm.nih.gov/40788706/) | 2025 | Retrospective Cohort | Gut Microbes | Large TriNetX retrospective cohort (>100,000 individuals) linking Atovaquone-proguanil exposure to reduced digestive cancer risk, potentially mediated through anti-*T. gondii* activity; novel signal for broader clinical impact |
| [27384853](https://pubmed.ncbi.nlm.nih.gov/27384853/) | 2016 | Case Report | Rinsho Ketsueki (Japanese Journal of Clinical Haematology) | Successful early diagnosis and treatment of disseminated toxoplasmosis reactivation following cord blood transplantation; Atovaquone used as part of combination therapy in an immunocompromised host |

---

## Singapore Market Information

Atovaquone currently has **no registered products in Singapore**. There are **0 product licences** on file with the Health Sciences Authority (HSA). No approved indication text, dosage form data, or local prescribing information is available from this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information. No Singapore HSA prescribing information, key warnings, contraindications, or drug interaction data were retrievable in this analysis. Supplementary safety review should be conducted based on international reference product labelling (e.g., US FDA label for Mepron® or EU SmPC).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Atovaquone has a directly applicable and well-characterised mechanism against *Toxoplasma gondii*, supported by a completed Phase 2 randomised trial (NCT00000794, n=100), a proof-of-concept pilot study, and established use in international clinical guidelines as alternative prophylaxis in immunocompromised patients who are intolerant of TMP-SMX. The evidence base is sufficient to justify structured further evaluation, but the absence of Singapore registration and safety data necessitates guardrails before any clinical application.

**To proceed, the following is needed:**

- **Singapore HSA registration pathway assessment**: Atovaquone is unregistered in Singapore; evaluate whether an abridged application based on US FDA or EMA approval is feasible
- **Full safety data retrieval**: Download and review the international package insert (Mepron® / Wellvone®) for complete key warnings, contraindications, and drug interactions — all currently listed as Data Gap
- **MOA data from DrugBank**: Retrieve full mechanism of action profile to complete pharmacological risk and plausibility assessment
- **Target population definition**: Clarify whether the intended use is **treatment** (AIDS-related toxoplasmic encephalitis, alternative salvage) or **prophylaxis** (TMP-SMX-intolerant immunocompromised patients), as regulatory pathway and evidence requirements differ
- **Bioavailability and formulation review**: Atovaquone has notoriously low and variable oral bioavailability (food-dependent); assess whether current formulations are adequate for the target indication and population in a Singapore context
- **Pharmacovigilance plan**: Define haematological and hepatic monitoring parameters for immunocompromised patient populations (transplant recipients, HIV/AIDS patients) who represent the primary target population

---

> **Other TxGNN Predictions Summary**: Of the remaining 9 predicted indications, **Ocular Toxoplasmosis** (L3, Proceed with Guardrails) represents the next most evidence-supported candidate and shares the same mechanistic rationale. All myiasis predictions (ranks 7–10, L5) and Leprosy (rank 1, L5), Acne (rank 4, L5), and Facial nerve palsy/herpes zoster (rank 3, L5) are recommended **Hold** due to lack of biological plausibility or evidence. Nocardiosis (rank 2, L4) is **Hold** pending mechanistic clarification.