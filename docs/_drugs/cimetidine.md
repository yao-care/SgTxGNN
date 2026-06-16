---
layout: default
title: Cimetidine
parent: 僅模型預測 (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
---

# Cimetidine
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

# Cimetidine: From Peptic Ulcer Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Cimetidine is the world's first H2-receptor antagonist (FDA-approved 1977), historically used to treat peptic ulcer disease by competitively blocking H2 receptors on gastric parietal cells to suppress gastric acid secretion by approximately 70–80%.
The TxGNN model's highest-ranked novel prediction is **Smouldering Systemic Mastocytosis** (score 99.80%), with mechanistic plausibility via direct H2-mediated symptom control of histamine-driven gastric hypersecretion in mast cell disease — however, **0 clinical trials and 0 publications** currently support this specific application.
This multi-indication evaluation spans 10 predicted indications, with evidence ranging from **L1** (active peptic ulcer disease: multiple RCTs) to **L5** (mastocytosis: model prediction only); Cimetidine is currently **not registered in Singapore**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peptic ulcer disease (first-generation H2-receptor antagonist; FDA-approved 1977) |
| Top Predicted Novel Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 (mastocytosis) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (mastocytosis) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the provided dataset. Based on known pharmacological information, Cimetidine acts as a competitive and reversible antagonist at histamine H2 receptors on gastric parietal cells, suppressing basal, nocturnal, and meal-stimulated gastric acid secretion. Beyond acid suppression, Cimetidine is notable among H2 blockers for possessing weak androgen receptor antagonist activity and immunomodulatory properties — specifically, enhancement of CD4+ T-cell function and inhibition of T-regulatory cell suppressor activity — which distinguish it from second-generation H2 blockers such as ranitidine and famotidine.

Smouldering systemic mastocytosis (SSM) is a WHO-classified subtype of systemic mastocytosis characterised by neoplastic mast cell infiltration and continuous release of histamine, tryptase, and prostaglandin D2. Histamine-driven gastric acid hypersecretion and episodic diarrhoea are among the most debilitating gastrointestinal manifestations of SSM. Combined H1+H2 histamine blockade is explicitly recognised in current mast cell disease management guidelines as first-line symptomatic therapy for mediator-release syndrome — making Cimetidine's H2 antagonism mechanistically and clinically rational in this context.

The TxGNN model's high prediction score most likely reflects the strength of the drug–target–histamine–mast cell pathway in the knowledge graph, rather than validated anti-disease activity. Cimetidine's immunomodulatory properties add a speculative secondary mechanistic angle (potential influence on the neoplastic mast cell microenvironment), but this is entirely unsupported by clinical data. This indication currently remains a research hypothesis requiring prospective case-level validation before any clinical development commitment.

---

## All Predicted Indications

| Rank | Disease | TxGNN Score | Evidence Level | Clinical Trials | Publications | Decision |
|------|---------|-------------|----------------|:---------------:|:------------:|----------|
| 1 | Smouldering systemic mastocytosis | 99.80% | L5 | 0 | 0 | Research Question |
| 2 | Active peptic ulcer disease | 99.79% | L1 | 1 (Phase 3) | 18 | Proceed with Guardrails |
| 3 | Peptic ulcer perforation | 99.77% | L4 | 0 | 20 | Hold |
| 4 | Gastrojejunal ulcer | 99.77% | L3 | 0 | 20 | Research Question |
| 5 | Lymphoadenopathic mastocytosis with eosinophilia | 99.76% | L5 | 0 | 0 | Research Question |
| 6 | Duodenogastric reflux | 99.49% | L3 | 0 | 8 | Research Question |
| 7 | Duodenal obstruction | 99.44% | L4 | 0 | 11 | Hold |
| 8 | Acne | 99.33% | L4 | 0 | 3 | Research Question |
| 9 | Abnormality of glucagon secretion | 99.14% | L5 | 0 | 1 | Hold |
| 10 | Gastroduodenitis | 98.89% | L2 | 0 | 20 | Proceed with Guardrails |

---

## Clinical Trial Evidence

### Smouldering Systemic Mastocytosis (Rank 1)

Currently no related clinical trials registered.

---

### Active Peptic Ulcer Disease (Rank 2 — Highest Evidence Indication)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01757275](https://clinicaltrials.gov/study/NCT01757275) | Phase 3 | Completed | 239 | Multi-centre double-blind RCT (China): high-dose IV esomeprazole vs IV cimetidine for prevention of rebleeding following successful endoscopic haemostasis in bleeding peptic ulcer — Cimetidine used as active comparator, validating both the indication and the intravenous route of administration |

---

## Literature Evidence

### Active Peptic Ulcer Disease (Rank 2 — Highest Evidence Indication)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [73792](https://pubmed.ncbi.nlm.nih.gov/73792/) | 1976 | RCT | Lancet | Landmark double-blind placebo-controlled trial (n=44): 90% ulcer healing at 6 weeks with cimetidine vs 36% with placebo |
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scand J Gastroenterol | Three-arm double-blind RCT (n=72): cimetidine 1g/day vs antacid vs placebo; 67% healing at 3 weeks (p<0.005 vs placebo) |
| [6990861](https://pubmed.ncbi.nlm.nih.gov/6990861/) | 1980 | RCT | Ann Clin Res | Placebo-controlled RCT (n=50): cimetidine 1g/day achieved 82.6% ulcer healing vs 48.0% with placebo over 4 weeks |
| [3092659](https://pubmed.ncbi.nlm.nih.gov/3092659/) | 1986 | Pooled Analysis | Am J Med | Pooled 4 European double-blind RCTs (n=348): enprostil vs cimetidine 400mg BD in duodenal ulcer; comparable healing rates establish cimetidine as the benchmark comparator |
| [6367680](https://pubmed.ncbi.nlm.nih.gov/6367680/) | 1984 | RCT | Arch Intern Med | Tricyclic antidepressants vs cimetidine in peptic ulcer: both effective as ulcer-healing agents in placebo-controlled trials |
| [8057210](https://pubmed.ncbi.nlm.nih.gov/8057210/) | 1994 | Clinical Study | J Pediatr Gastroenterol Nutr | Paediatric retrospective cohort (n=42): cimetidine 20mg/kg/day; 94.7% gastric ulcer and 87.0% duodenal ulcer healing confirmed endoscopically at 8 weeks |
| [3299677](https://pubmed.ncbi.nlm.nih.gov/3299677/) | 1987 | Long-term Trial | Scand J Gastroenterol | Multinational maintenance trial (n=1,842): cimetidine 400mg nightly for up to 4 years; 17.2% symptomatic relapse in year 1, declining to 8.8% by year 3 |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Review | Drug Intell Clin Pharm | Ranitidine pharmacology review: ranitidine 4–10× more potent than cimetidine on molar basis; cimetidine used as the clinical standard for comparison |
| [10701981](https://pubmed.ncbi.nlm.nih.gov/10701981/) | 1999 | DDI Study | J Pharm Biomed Anal | Cimetidine significantly increased proguanil Cmax (p<0.05) and AUC (p<0.005) in peptic ulcer patients — key pharmacokinetic signal for CYP inhibition in real-world patients |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Nizatidine pharmacodynamic and pharmacokinetic review; cimetidine used as inhibitory benchmark across both animal and human gastric acid secretion studies |

---

### Gastroduodenitis (Rank 10 — L2 Evidence)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2253535](https://pubmed.ncbi.nlm.nih.gov/2253535/) | 1990 | RCT | Dig Dis Sci | Endoscopic RCT (4 groups, n=20 each): cimetidine vs sucralfate for prevention of naproxen-induced acute gastroduodenal injury in healthy volunteers; scoring-method sensitivity analysis included |
| [2735335](https://pubmed.ncbi.nlm.nih.gov/2735335/) | 1989 | RCT | Am J Med | Pilot single-blind RCT (n=26 RA patients): sucralfate vs cimetidine 400mg BD in NSAID users with active gastroduodenal lesions; improved endoscopic lesion scores in both arms |
| [3874573](https://pubmed.ncbi.nlm.nih.gov/3874573/) | 1985 | RCT | Ann Intern Med | Double-blind RCT in medical ICU: 14/21 cimetidine patients showed normal or improved gastroduodenal mucosa vs 5/18 placebo (p<0.05); serial endoscopy used |
| [6381185](https://pubmed.ncbi.nlm.nih.gov/6381185/) | 1984 | RCT | Digestion | Double-blind RCT (n=105): cimetidine 1.2–2.4g/day vs placebo in acute spinal injury patients for prevention of stress-related gastroduodenal lesions; haematemesis in 1 placebo patient only |
| [2787809](https://pubmed.ncbi.nlm.nih.gov/2787809/) | 1989 | Clinical Study | J Clin Pharmacol | Single-blind endoscopic tolerability study (n=groups of 20): cimetidine and antacids used for mucosal rescue in NSAID-induced gastroduodenal injury (flurbiprofen, aspirin) |
| [7022726](https://pubmed.ncbi.nlm.nih.gov/7022726/) | 1981 | Clinical Study | Surgery | Controlled trial (n=59 renal transplant patients): cimetidine vs placebo for prophylaxis of post-transplant gastroduodenal ulceration — cimetidine did not significantly reduce incidence |

---

### Peptic Ulcer Perforation (Rank 3 — L4 Evidence)

> ⚠️ The available literature for this indication primarily documents perforation *occurring during or after cessation of* Cimetidine therapy, rather than evidence of protective benefit. Clinical context is cautionary.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7082957](https://pubmed.ncbi.nlm.nih.gov/7082957/) | 1982 | Case Series | Br J Surg | 15-year surgical review: after cimetidine availability, elective peptic ulcer operations fell 45% but perforation rate fell only 10% — limited protection against perforation |
| [6743974](https://pubmed.ncbi.nlm.nih.gov/6743974/) | 1984 | Case Series | Br J Surg | Nine cases of duodenal ulcer perforation occurring while patients were actively on cimetidine therapy; all eventually required truncal vagotomy |
| [6617045](https://pubmed.ncbi.nlm.nih.gov/6617045/) | 1983 | Retrospective Cohort | Clin Pediatrics | 10-year paediatric PUD review (n=61): stress ulcers in young children frequently required surgery for perforation or haemorrhage despite medical treatment |
| [922364](https://pubmed.ncbi.nlm.nih.gov/922364/) | 1977 | Case Report | BMJ | Case report of peptic ulcer perforation following cimetidine withdrawal — acid rebound phenomenon after cessation |

---

### Gastrojejunal Ulcer (Rank 4 — L3 Evidence)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6103209](https://pubmed.ncbi.nlm.nih.gov/6103209/) | 1980 | RCT | Lancet | Sequential RCT: somatostatin vs cimetidine in severe persistent peptic ulcer haemorrhage; somatostatin superior in 7/10 matched pairs — directly relevant to post-anastomotic ulcer bleeding management |
| [6957991](https://pubmed.ncbi.nlm.nih.gov/6957991/) | 1982 | RCT | Scand J Gastroenterol (Suppl) | Pirenzepine vs cimetidine (n=254): 73.4% cimetidine-treated duodenal ulcer patients healed at 4 weeks vs 64.3% pirenzepine — validates cimetidine as clinical standard |
| [6375965](https://pubmed.ncbi.nlm.nih.gov/6375965/) | 1984 | Clinical Study | Crit Care Med | Cimetidine more effective than placebo for stress-ulcer prophylaxis, but no advantage over titrated antacid; clinical utility discussed |

---

### Acne (Rank 8 — L4 Evidence)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6130053](https://pubmed.ncbi.nlm.nih.gov/6130053/) | 1982 | Review | Der Hautarzt | H2-antagonists in dermatology: discusses controversial dermatological applications of cimetidine in urticaria, mastocytosis, and acne — notes weak androgen receptor antagonism as the mechanistic basis for acne/seborrhoea effects |
| [8090657](https://pubmed.ncbi.nlm.nih.gov/8090657/) | 1993 | Review/Clinical Study | Pol Tyg Lek | PCOS hyperandrogenic syndrome management: H2 blockers with anti-androgenic properties (including cimetidine class) mentioned as one treatment modality for acne and seborrhoea reduction within 3 months |

---

### Smouldering Systemic Mastocytosis (Rank 1) and Lymphoadenopathic Mastocytosis with Eosinophilia (Rank 5)

Currently no related literature available.

---

### Abnormality of Glucagon Secretion (Rank 9)

> ⚠️ The sole identified publication (PMID 6088239) concerns radionuclide imaging technique comparison for Meckel's diverticulum diagnosis, not treatment of glucagon secretion disorders. No mechanistic or therapeutic connection is supported. This prediction is considered a knowledge-graph false positive.

---

## Singapore Market Information

Cimetidine is currently **not registered in Singapore**. No product authorisations are on record, and there is no established marketing pathway for this compound in Singapore at present.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No formal drug interaction, warning, or contraindication data was returned from the evidence sources queried. Based on pharmacological knowledge, key risks known for Cimetidine include broad-spectrum CYP450 inhibition (CYP1A2, CYP2C9, CYP2D6, CYP3A4) with clinically significant interactions involving warfarin, phenytoin, theophylline, and other narrow-therapeutic-index drugs; anti-androgenic effects (gynaecomastia, sexual dysfunction) with long-term use; and CNS effects (confusion, agitation) in elderly or renally impaired patients. Formal prescribing information should be consulted before any clinical use.

---

## Conclusion and Next Steps

### Smouldering Systemic Mastocytosis — Top Novel Prediction (Rank 1)

**Decision: Hold**

**Rationale:**
The mechanistic link is rational (H2 blockade directly addresses histamine-driven gastric hypersecretion in mast cell disease, consistent with clinical guidelines), but there is zero dedicated clinical evidence. The high TxGNN score reflects knowledge-graph pathway inference, not clinical validation.

**To proceed, the following is needed:**
- Systematic review of published H2-blocker utilisation within SSM clinical case series and management guidelines
- Prospective case documentation of Cimetidine (or equivalent H2 blocker) outcomes in SSM patients
- Comparative assessment versus newer H2 blockers with lower DDI risk (e.g., famotidine) for the same symptom-control role
- MOA clarification from DrugBank (Data Gap DG002) to quantify immunomodulatory activity relevant to neoplastic mast cell conditions
- Combined H1+H2 blockade protocol design for a hypothesis-testing pilot study

---

### Active Peptic Ulcer Disease — Established Evidence (Rank 2)

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple double-blind RCTs across several decades and a completed Phase 3 trial confirm Cimetidine's efficacy at L1 evidence level. However, current clinical practice has shifted to PPIs and H. pylori eradication protocols, and Cimetidine's broad CYP inhibition profile creates significant drug–drug interaction risk that requires active management.

**To proceed, the following is needed:**
- Singapore HSA marketing authorisation application
- Comprehensive CYP450 drug interaction management plan and prescriber guidance
- Positioning statement relative to modern standard-of-care (PPIs, H. pylori eradication)
- Anti-androgenic adverse effect monitoring protocol for long-term male users
- TFDA package insert extraction to address Data Gap DG001 (formal warnings and contraindications)

---

### Gastroduodenitis — L2 Evidence (Rank 10)

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple RCTs demonstrate Cimetidine's effectiveness in preventing NSAID-induced and stress-induced gastroduodenal mucosal injury, particularly in ICU and post-surgical settings, constituting L2 evidence. This remains a clinically meaningful niche where Cimetidine may offer adjunctive value.

**To proceed, the following is needed:**
- Systematic review against current gastroprotection guidelines (PPIs are now preferred for NSAID co-therapy)
- Risk-benefit analysis of CYP450 inhibition in polymedicated critically ill patients
- Singapore HSA registration application with NSAID-gastroprotection as the target indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

