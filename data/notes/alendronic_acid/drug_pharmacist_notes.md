# Alendronic Acid: From Osteoporosis to HIV-Associated Bone Disease

## One-Sentence Summary

Alendronic acid is a bisphosphonate, widely used for the prevention and treatment of osteoporosis by inhibiting bone resorption. The TxGNN model predicts it may be effective for managing **HIV infectious disease**—specifically the secondary bone loss associated with HIV infection and antiretroviral therapy—with **4 clinical trials** and **2 publications** currently supporting this direction. Notably, this repurposing targets **HIV-related bone loss management**, not the treatment of HIV infection itself.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis (bisphosphonate class; original indication data not available in regulatory record) |
| Predicted New Indication | HIV Infectious Disease (HIV-associated bone loss) |
| TxGNN Prediction Score | 96.78% |
| Evidence Level | L1 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Alendronic acid is a nitrogen-containing bisphosphonate that inhibits farnesyl pyrophosphate synthase (FPPS) within the mevalonate pathway. By blocking this enzyme, it disrupts the prenylation of small GTPases (Ras, Rho, Rac) essential for osteoclast function and survival—ultimately suppressing bone resorption. This mechanism is highly effective in conditions where excessive osteoclast activity leads to net bone loss.

HIV infection creates precisely this scenario through multiple converging pathways. Chronic HIV-related inflammation elevates pro-inflammatory cytokines (IL-6, TNF-α), which drive RANKL/OPG axis imbalance and promote osteoclast activation. Antiretroviral drugs—particularly tenofovir and protease inhibitors—further compound this by impairing vitamin D metabolism, reducing renal phosphate reabsorption, and directly suppressing osteoblast activity. The result is a clinically significant secondary osteoporosis distinct from, but mechanistically addressable by, the same FPPS-inhibition strategy used in primary osteoporosis.

The logical connection is therefore two-tiered: alendronate's original indication (primary osteoporosis) and this predicted new application (HIV-associated secondary osteoporosis) share the same effector mechanism—osteoclast suppression via FPPS inhibition. The difference lies upstream, in the cause of osteoclast over-activation rather than its downstream management. This mechanistic bridge explains both the TxGNN prediction and the substantial clinical trial activity found in the literature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00120757](https://clinicaltrials.gov/study/NCT00120757) | Phase 3 | Completed | 140 | Multicenter RCT (ANRS 120 Fosivir): alendronate vs. placebo over 2 years in HIV-1 patients with primary osteoporosis, with calcium and vitamin D supplementation; highest-grade direct evidence for this repurposing |
| [NCT00061256](https://clinicaltrials.gov/study/NCT00061256) | Phase 2 | Completed | 80 | Double-blind, placebo-controlled RCT evaluating once-weekly alendronate combined with calcium and vitamin D in HIV-infected patients with reduced BMD; supports weekly dosing regimen |
| [NCT00921557](https://clinicaltrials.gov/study/NCT00921557) | Phase 2 | Completed | 52 | RCT in HIV-infected children and adolescents with low BMD; assessed lumbar spine BMD changes at 24 and 48 weeks; extends evidence to paediatric population |
| [NCT02322099](https://clinicaltrials.gov/study/NCT02322099) | Phase 4 | Terminated | 53 | Short-course alendronate vs. placebo to prevent BMD loss during ART initiation in antiretroviral-naïve HIV-1 patients; terminated early (reason unknown; n=53); provides partial real-world data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [25300622](https://pubmed.ncbi.nlm.nih.gov/25300622/) | 2014 | Systematic Review + Meta-analysis | AIDS Reviews | Pooled analysis of 8 RCTs investigating bisphosphonate effects on BMD (lumbar spine, femoral neck, total hip) in HIV-infected adults; provides the highest-level synthesised evidence for bisphosphonate efficacy in this population |
| [26890207](https://pubmed.ncbi.nlm.nih.gov/26890207/) | 2016 | Practice Guideline / Pharmacologic Review | Current Opinion in HIV and AIDS | Clinician-focused review of pharmacological strategies for prevention and management of low BMD in people living with HIV; contextualises alendronate within current HIV bone health management practice |

---

## Safety Considerations

Detailed safety data for this drug (key warnings, contraindications, and drug interactions) are not available in the current Evidence Pack. Please refer to the approved package insert for comprehensive safety information.

**Important known safety consideration:** Alendronate requires patients to remain upright for at least 30 minutes after ingestion to reduce the risk of oesophageal irritation. This is clinically relevant when considering use in HIV populations, and constitutes a potential contraindication in patients with oesophageal motility disorders or dysphagia.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed multicenter Phase 3 RCT (NCT00120757, n=140) directly demonstrates alendronate's efficacy in HIV-1-associated osteoporosis, supported by two completed Phase 2 RCTs and a systematic meta-analysis of 8 RCTs—constituting robust L1 evidence for the specific clinical use case of HIV-related bone loss management (not HIV treatment itself). The mechanistic rationale is well-characterised and directly extends from the drug's established pharmacology.

**To proceed, the following is needed:**

- **Safety dossier completion**: Retrieve and review the full Singapore/international package insert for warnings, contraindications, and drug interaction profile—currently a blocking data gap
- **MOA documentation**: Formal DrugBank MOA query to supplement the mechanistic rationale section
- **Singapore regulatory pathway**: Confirm whether an indication for HIV-associated osteoporosis would require a new drug application or can be pursued under an existing registered product (currently 0 Singapore registrations)
- **Population-specific safety review**: Assess interactions between alendronate and common antiretroviral agents (particularly tenofovir, protease inhibitors) given overlapping effects on renal function and bone metabolism
- **Clarification of NCT02322099 termination reason**: Determine whether early termination was due to recruitment difficulties or a safety signal before proceeding
- **Paediatric applicability assessment**: Phase 2 trial data exist for children/adolescents with HIV—evaluate whether a paediatric indication pathway is warranted