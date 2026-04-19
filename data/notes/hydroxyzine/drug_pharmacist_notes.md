# Hydroxyzine: From Pruritus and Anxiety to Allergic Urticaria

## One-Sentence Summary

Hydroxyzine is a first-generation H1 antihistamine historically indicated for pruritus, anxiety, and pre-operative sedation, but currently **not registered in Singapore**.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, with its active metabolite cetirizine providing Phase 3 RCT-level evidence and class-level antihistamine literature offering extensive supporting context.
A total of **1 clinical trial** and **20 publications** currently support this direction, though most evidence is indirect (metabolite- or class-level rather than Hydroxyzine-specific).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; historically used for pruritus, anxiety, and allergic symptoms |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Hydroxyzine is a piperazine-class first-generation H1 receptor antagonist. It competitively blocks peripheral histamine H1 receptors, thereby inhibiting histamine-mediated vasodilation, increased vascular permeability, and itch signal transmission through sensory nerves. It also possesses anticholinergic and mild anxiolytic properties via CNS H1 blockade. Its carboxylated active metabolite, cetirizine, exhibits even greater H1 selectivity and is among the world's most widely used second-generation antihistamines.

Allergic urticaria is driven by IgE-mediated mast cell degranulation, which releases large quantities of histamine and triggers the characteristic wheal-and-flare skin response. The mechanistic link between H1 antagonism and urticaria symptom control is therefore direct and well-established. A 2017 review by Kaplan (PMID 28913986) explicitly states that "first-generation antihistamines, such as hydroxyzine or diphenhydramine, were employed similarly in the past" for chronic spontaneous urticaria before second-generation agents became dominant.

From a repurposing standpoint in Singapore's market context, the 2019 CSACI position statement (PMID 31582993) specifically names hydroxyzine as a first-generation agent with documented efficacy for urticaria, while recommending second-generation alternatives as preferred first-line therapy due to a more favorable tolerability profile (less sedation, lower cardiovascular risk). This means there is a well-defined clinical niche where Hydroxyzine retains relevance — such as parenteral administration in acute settings or combined use for patients requiring sedation alongside antihistamine coverage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Multicenter pilot RCT in hospital Emergency Departments comparing IV cetirizine (the direct active metabolite of hydroxyzine) 10 mg vs IV diphenhydramine 50 mg for acute urticaria; confirms that H1 antihistamine administered via the IV route is effective in this acute-care setting. This is active-metabolite-level evidence, not hydroxyzine itself, and the small sample size indicates feasibility rather than definitive efficacy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Position Statement | Allergy, Asthma, and Clinical Immunology | CSACI official position: explicitly names hydroxyzine as a first-generation antihistamine with known efficacy for urticaria, but recommends second-generation agents preferentially due to hydroxyzine's sedation, cognitive impairment, QTc risk, and overdose fatality potential |
| [28913986](https://pubmed.ncbi.nlm.nih.gov/28913986/) | 2017 | Review | Allergy, Asthma & Immunology Research | Chronic spontaneous urticaria pathogenesis and treatment algorithm; confirms hydroxyzine and diphenhydramine were historically first-line, now replaced by second-generation H1 blockers; omalizumab discussed for antihistamine-refractory cases |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Foundational review of cetirizine as "a piperazine derivative and carboxylated metabolite of hydroxyzine"; establishes strong H1 antagonism + anti-eosinophil chemotaxis in controlled trials for urticaria and allergic rhinitis |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Review | Drugs | Phase III trial data for bilastine vs placebo in urticaria; provides class-level context showing the TSS endpoint methodology applicable to H1 antihistamine evaluations |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Annals of Pharmacotherapy | Comprehensive pharmacist-oriented review of first- and second-generation antihistamines for allergic rhinitis and chronic idiopathic urticaria; explicitly compares efficacy and safety across drug generations |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | PK/PD Review | Clinical Pharmacokinetics | Head-to-head comparative PK/PD review of desloratadine, fexofenadine, and levocetirizine in urticaria; contextualizes H1 receptor occupancy thresholds for clinical efficacy |
| [22994340](https://pubmed.ncbi.nlm.nih.gov/22994340/) | 2012 | Review | Clinical and Experimental Allergy | Framework for predicting the best H1 antihistamine for individual urticaria patients; discusses chronic spontaneous urticaria inter-patient variability and head-to-head study design |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Clinical Studies | Allergy | Compilation of cetirizine (hydroxyzine metabolite) clinical studies in allergic rhinitis and chronic urticaria demonstrating consistent H1-mediated efficacy |
| [11034010](https://pubmed.ncbi.nlm.nih.gov/11034010/) | 2000 | Case Report | Journal of Clinical Gastroenterology | Cetirizine-induced cholestasis case; relevant safety signal — transient hepatic transaminase elevations seen in <2% of patients in US trials; applies to the hydroxyzine → cetirizine metabolic pathway |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clinical Allergy and Immunology | H1-antihistamines in children; Level 1 evidence for H1 antagonist efficacy in allergic conditions including urticaria, with paediatric dosing context |

---

## Singapore Market Information

Hydroxyzine currently has **no registered marketing authorizations in Singapore**. There are no license records on file.

> If clinical use is being considered, this would require an import license, special access scheme, or evaluation under HSA's regulatory pathways for unregistered therapeutic products.

---

## Safety Considerations

> Formal Singapore package insert data (HSA warnings and contraindications) is not currently available. The following is drawn from the published literature included in this evidence pack.

- **Known Class-Level Safety Concerns** (from PMID 31582993 — CSACI Position Statement 2019): First-generation antihistamines including hydroxyzine are associated with **significant and common adverse effects**: sedation, cognitive impairment, poor sleep quality, dry mouth, dizziness, and orthostatic hypotension. Deaths from accidents, intentional and unintentional overdoses, and **sudden cardiac death** have been reported with this drug class.
- **Hepatic Signal**: Transient, reversible hepatic transaminase elevations were observed in <2% of patients in US clinical trials of cetirizine (hydroxyzine's active metabolite); one case of cetirizine-induced cholestasis has been published (PMID 11034010).
- **Drug Interactions**: No interaction data was retrieved in this evidence pack. Formal DDI review against co-medications should be completed before clinical use given hydroxyzine's CNS-depressant and anticholinergic properties.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Hydroxyzine's H1 antagonism directly and mechanistically addresses the core pathophysiology of allergic urticaria, and its active metabolite cetirizine has completed Phase 3 evidence supporting IV antihistamine use in acute urticaria (NCT02023164). Multiple professional society reviews and position statements confirm class-level efficacy — including direct mention of hydroxyzine by name — while positioning second-generation agents as preferred for routine outpatient use. The evidence base is sufficient to justify hydroxyzine's use within a clearly defined clinical context (e.g., acute/parenteral settings, sedation co-indication), provided safety guardrails are in place.

**To proceed, the following is needed:**

- **Regulatory pathway**: Identify the appropriate HSA import or special access pathway for an unregistered product; assess feasibility of formal Singapore registration
- **Full safety review**: Obtain and review the full package insert (including QTc prolongation risk, anticholinergic burden, and overdose precautions) before clinical deployment
- **DDI assessment**: Conduct formal drug-drug interaction review, particularly for co-medications with CNS-depressant or anticholinergic properties
- **Clinical positioning statement**: Define the specific patient population and clinical scenario where hydroxyzine offers advantages over already-available second-generation antihistamines (e.g., IV route availability, combined sedation-antihistamine need, cost considerations)
- **Paediatric dosing data**: If use in children is contemplated, confirm age-appropriate dosing and safety parameters
- **Direct hydroxyzine RCT**: Note that existing evidence is largely metabolite- or class-level; a direct RCT of hydroxyzine in allergic urticaria would strengthen the evidence from L2 to L1