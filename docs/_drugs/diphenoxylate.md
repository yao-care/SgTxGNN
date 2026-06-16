---
layout: default
title: Diphenoxylate
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
---

# Diphenoxylate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Diphenoxylate: From Acute Non-Specific Diarrhea to Gastroenteritis

## One-Sentence Summary

Diphenoxylate is a synthetic opioid antidiarrheal agent known globally (marketed as Lomotil in combination with atropine) for reducing intestinal motility in acute diarrhea, but is currently not registered in Singapore.
The TxGNN model ranks **gastroenteritis** as the most clinically actionable predicted indication — among 10 total predictions — with **2 clinical trial records** and **20 publications** providing supporting evidence; the top-ranked TxGNN prediction by score is gastroduodenitis (90.83%), though that indication currently has no supporting studies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally used for acute non-specific diarrhea |
| Predicted New Indication | Gastroenteritis (highest-evidence actionable prediction; TxGNN rank #3) |
| TxGNN Prediction Score | 87.33% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacological knowledge, Diphenoxylate is a synthetic piperidine opioid derivative that acts as a **mu-opioid receptor agonist** in the gastrointestinal tract. This receptor activation reduces intestinal peristalsis, decreases mucosal secretion, and prolongs gut transit time — directly addressing the cardinal symptoms of diarrhea. It is typically combined with atropine (as Lomotil) to deter abuse.

Gastroenteritis is characterised by acute-onset diarrhea, often accompanied by nausea, vomiting, and abdominal cramping. The core pathophysiology involves disrupted intestinal fluid and electrolyte transport together with accelerated motility. Diphenoxylate's mechanism — reducing peristalsis and luminal secretion — maps directly onto this symptom profile. Multiple pharmacotherapy reviews (PMID 3893119, PMID 111547) consistently include diphenoxylate as a standard antidiarrheal option, and a double-blind comparative study (PMID 6753707) confirmed equivalent efficacy to loperamide in patients with chronic diarrhea.

One critical caveat shapes the "guardrails" recommendation: in bacterial or toxin-mediated gastroenteritis, inhibiting intestinal motility may delay the clearance of pathogens and toxins, potentially prolonging illness or precipitating serious complications such as toxic megacolon. Multiple publications specifically flag diphenoxylate-class agents as contraindicated in pseudomembranous colitis and antibiotic-associated colitis (PMID 7354554, PMID 1147432). Safe use therefore requires careful patient selection, restricting the drug to non-infectious or presumed viral gastroenteritis in adults, and excluding febrile, bloody-stool presentations.

---

## Clinical Trial Evidence

The two trials retrieved for the gastroenteritis search query are IBD-related interventional studies of etrolizumab, not diphenoxylate trials. They are included for transparency but carry **Grade C relevance** to this repurposing hypothesis.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02403323](https://clinicaltrials.gov/study/NCT02403323) | Phase 3 | Terminated | 790 | Open-label extension of etrolizumab for moderately-to-severely active Crohn's disease; unrelated to diphenoxylate use in gastroenteritis — retrieved by broad GI inflammation query (Grade C relevance) |
| [NCT05733845](https://clinicaltrials.gov/study/NCT05733845) | N/A | Recruiting | 100 | Observational molecular mechanism study of IBD non-response to biologics; no interventional relevance to diphenoxylate repurposing for acute gastroenteritis (Grade C relevance) |

> **Note:** No clinical trials specifically evaluating diphenoxylate for gastroenteritis are currently registered on ClinicalTrials.gov. The absence of directly relevant trials is a key evidence gap for this repurposing direction.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [6753707](https://pubmed.ncbi.nlm.nih.gov/6753707/) | 1981 | Comparative Clinical Study | Ann Clin Res | Double-blind crossover study (n=29) comparing diphenoxylate vs loperamide for chronic post-resection diarrhea; both effective, loperamide required fewer capsules for equivalent diarrhea control |
| [39958914](https://pubmed.ncbi.nlm.nih.gov/39958914/) | 2024 | Case Report | Discoveries (Craiova) | Diphenoxylate (Lomotil) toxicity in a 2-year-old with acute gastroenteritis — CNS and respiratory depression; highlights critical paediatric safety risk from even small doses |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | Am J Med | Comprehensive antidiarrheal therapy review; diphenoxylate listed as synthetic antidiarrheal reducing stool frequency ~50%; recommends caution in microorganism-driven diarrhea |
| [111547](https://pubmed.ncbi.nlm.nih.gov/111547/) | 1979 | Review | Am J Hosp Pharm | Pharmacotherapy of diarrhea review; diphenoxylate explicitly named alongside loperamide as opioid-class synthetic antidiarrheal; reviews mechanism and clinical use in acute and chronic diarrhea |
| [21283398](https://pubmed.ncbi.nlm.nih.gov/21283398/) | 1983 | Review | Can Fam Physician | Four mechanisms of diarrhea reviewed (osmotic, secretory, exudative, motility); identifies rotavirus and Norwalk virus as common gastroenteritis causes; contextual background for patient selection |
| [18097699](https://pubmed.ncbi.nlm.nih.gov/18097699/) | 2007 | Review | Der Internist | Traveler's diarrhea treatment review; motility inhibitors discussed as adjunct; recommends withholding antiperistaltis agents in febrile or bloody diarrhea — directly relevant safety guidance |
| [7354554](https://pubmed.ncbi.nlm.nih.gov/7354554/) | 1980 | Safety Communication | JAMA | Antiperistaltic agents including diphenoxylate contraindicated in pseudomembranous colitis; critical safety signal for subtype exclusion in gastroenteritis workup |
| [1147432](https://pubmed.ncbi.nlm.nih.gov/1147432/) | 1975 | Letter | Ann Intern Med | Lomotil (diphenoxylate + atropine) associated with worsening antibiotic-associated colitis; risk of toxic megacolon; reinforces need to exclude antibiotic-related gastroenteritis |
| [760500](https://pubmed.ncbi.nlm.nih.gov/760500/) | 1979 | Review | Am J Clin Nutr | Animal model of clindamycin-induced enterocolitis; antiperistaltic drug use worsens outcome — mechanistic rationale for contraindication in toxin-mediated gastroenteritis |
| [18192964](https://pubmed.ncbi.nlm.nih.gov/18192964/) | 2007 | Review | Rev Gastroenterol Disord | Diarrhea management in IBD; loperamide and diphenoxylate discussed for motility-driven diarrhea; cautions against use in active mucosal inflammation — relevant analogy for infectious gastroenteritis |

---

## Singapore Market Information

Diphenoxylate is currently not registered in Singapore. No product authorization records are on file (total registrations: 0).

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, and drug–drug interactions) is not available in the current Evidence Pack. The following signals are derived from retrieved literature:

- **Critical Contraindications (literature-derived)**: Diphenoxylate is contraindicated in pseudomembranous colitis and antibiotic-associated colitis (PMID 7354554, PMID 1147432). Use in these settings risks toxic megacolon and death.
- **Paediatric Toxicity**: Even therapeutic doses in young children can cause life-threatening CNS and respiratory depression (PMID 39958914). The drug should not be used in children under 2 years; extreme caution is required in older children.
- **Infectious Diarrhea**: Should not be used when gastroenteritis presents with fever, bloody stools, or recent antibiotic use, as motility inhibition may delay pathogen/toxin clearance and worsen outcome.

Please refer to the full prescribing information (package insert) for complete safety information, including drug–drug interactions and dosing contraindications, which could not be retrieved in this analysis cycle.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Diphenoxylate's mu-opioid receptor mechanism directly targets the motility-driven diarrhea that characterises gastroenteritis, and published pharmacotherapy reviews alongside one comparative clinical study confirm its antidiarrheal efficacy. However, no Singapore registration exists, no dedicated clinical trials in acute gastroenteritis have been conducted, and the drug carries well-documented risks in infectious subtypes and in paediatric patients that require strict prescribing safeguards before any repurposing application.

**To proceed, the following is needed:**

- Obtain and parse the full prescribing information (package insert) to document complete contraindications, warnings, and drug–drug interactions (currently blocking — DG001)
- Confirm mechanism of action via DrugBank API (DG002) to enable formal mechanistic rationale scoring
- Conduct a systematic review or meta-analysis specifically focused on diphenoxylate in viral/non-bacterial acute gastroenteritis in adults
- Define eligible patient population with explicit exclusion criteria: children under 2, febrile diarrhea, bloody stools, recent antibiotic use, and suspected pseudomembranous colitis
- Evaluate the regulatory pathway for Singapore registration, given zero current authorizations
- Compare risk–benefit profile against loperamide (a closely related mu-opioid agonist with a larger evidence base and more favourable safety profile in the same indication) to determine whether diphenoxylate offers any clinical advantage worth pursuing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

