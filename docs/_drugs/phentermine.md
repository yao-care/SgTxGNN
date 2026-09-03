---
layout: default
title: Phentermine
parent: 僅模型預測 (L5)
nav_order: 777
evidence_level: L5
indication_count: 10
---

# Phentermine
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

# Phentermine: From Obesity to Fatty Liver Disease

## One-Sentence Summary

> Phentermine is a sympathomimetic anorectic historically used as a short-term adjunct for obesity/weight management. Among the candidates surfaced by the TxGNN model, the only indication supported by concrete evidence is **Fatty Liver Disease (NAFLD/MASLD)**, backed by **2 clinical trials** (including one completed Phase 4 study directly testing phentermine) and **15 publications**. TxGNN's numerically highest-scoring predictions (e.g., hypervitaminosis, rare genetic syndromes) carry no supporting evidence and are treated in this report as low-confidence graph noise rather than the primary candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; internationally labeled for short-term adjunctive treatment of obesity (per literature, e.g., PMID 22348915) |
| Predicted New Indication | Fatty Liver Disease (NAFLD/MASLD) |
| TxGNN Prediction Score | 77.74% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for phentermine is not available in this evidence pack (data gap DG002). Based on the supporting literature collected here, phentermine is a noradrenergic sympathomimetic amine that suppresses appetite by promoting norepinephrine release in the hypothalamus, and has been FDA-approved for decades as a short-term obesity treatment — including as the anorectic component of the phentermine/topiramate combination (Qsymia).

Fatty liver disease (NAFLD/MASLD) is pathophysiologically driven by obesity and insulin resistance, and clinically meaningful weight loss is an established route to reducing hepatic fat content. Phentermine's effect on NAFLD therefore appears to be **indirect and weight-mediated** rather than a direct hepatic mechanism — consistent with the completed Phase 4 trial (NCT03849729) that directly measured phentermine's effect on intrahepatic fat infiltration prior to bariatric surgery. A caveat noted in the evidence pack: much of the review literature discusses phentermine only as part of the phentermine/topiramate combination, so phentermine's independent contribution (separate from topiramate, which has its own hepatic and metabolic effects) is not yet clearly isolated.

**Note on other TxGNN-predicted candidates:** The raw model output ranked several other diseases above fatty liver disease by prediction score — hypervitaminosis, proximal 16p11.2 microdeletion syndrome, obsolete hypertelorism, frontorhiny, pentosuria, lethal polymalformative syndrome (Boissel type), and migraine with brainstem aura. All of these returned **zero clinical trials and zero literature**, and the evidence pack's own mechanistic rationale flags them as implausible or as knowledge-graph noise. Two additional candidates carry partial signals worth flagging as cautions rather than opportunities:
- **Postural orthostatic tachycardia syndrome (POTS)** — the single retrieved publication (PMID 26968177) is a case report describing stimulant medication *mimicking or aggravating* POTS symptoms, not treating it. Phentermine's sympathomimetic action is mechanistically more likely to worsen than improve POTS.
- **Migraine disorder** — the retrieved literature attributes migraine-preventive effects to the *topiramate* component of the phentermine/topiramate combination, not to phentermine itself; one case report (PMID 25911503) even describes topiramate withdrawal (with phentermine added) affecting migraine control, further pointing to topiramate as the active agent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03849729](https://clinicaltrials.gov/study/NCT03849729) | Phase 4 | Completed | 92 | Evaluated effectiveness and tolerability of phentermine in reducing intrahepatic fat infiltration and adipose tissue, and postoperative complications, in patients undergoing bariatric surgery. |
| [NCT07058155](https://clinicaltrials.gov/study/NCT07058155) | Phase 4 | Recruiting | 70 | OPTIMAL Trial: evaluates TIPS combined with interval metabolic surgery for advanced liver disease/portal hypertension in patients with obesity; phentermine's role as an intervention is not clearly primary (graded C relevance). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32153507](https://pubmed.ncbi.nlm.nih.gov/32153507/) | 2020 | Systematic Review | Frontiers in Endocrinology | Systematic review of weight-loss medications' effects on hepatic steatosis/steatohepatitis; GLP-1 agonists best studied, but reviews anorectics including phentermine. |
| [35501557](https://pubmed.ncbi.nlm.nih.gov/35501557/) | 2022 | Review | Current Obesity Reports | Reviews anti-obesity medication effects on NAFLD, with focus on hepatic histology outcomes. |
| [36120448](https://pubmed.ncbi.nlm.nih.gov/36120448/) | 2022 | Review | Frontiers in Endocrinology | Compares anti-obesity agents to identify the optimal option for NAFLD patients. |
| [30502373](https://pubmed.ncbi.nlm.nih.gov/30502373/) | 2019 | Review | Metabolism | Reviews obesity-NAFLD pathophysiology and links weight loss to reduced liver-specific and all-cause mortality in NAFLD. |
| [41025003](https://pubmed.ncbi.nlm.nih.gov/41025003/) | 2025 | Review | World Journal of Gastroenterology | Updated review of anti-obesity drug efficacy/safety in MASLD/MASH, noting hepatotoxicity and altered hepatic metabolism concerns in this population. |
| [39604664](https://pubmed.ncbi.nlm.nih.gov/39604664/) | 2025 | Cohort | Digestive Diseases and Sciences | Cohort study on weight-management therapy success (7% total body weight loss target) in MASLD/MASH patients with psychiatric comorbidities. |
| [35430025](https://pubmed.ncbi.nlm.nih.gov/35430025/) | 2022 | Review | Journal of Clinical Lipidology | Roundtable discussion noting extended-release phentermine/topiramate promotes meaningful weight loss in RCTs relevant to fatty liver risk reduction. |
| [36059008](https://pubmed.ncbi.nlm.nih.gov/36059008/) | 2022 | Review | Paediatric Drugs | Reviews phentermine/topiramate's pediatric approval, noting the combination was also studied for NASH. |
| [39720872](https://pubmed.ncbi.nlm.nih.gov/39720872/) | 2025 | Cohort | JPEN | Describes topiramate (phentermine-topiramate combination component) treatment outcomes in pediatric MASLD. |
| [18560368](https://pubmed.ncbi.nlm.nih.gov/18560368/) | 2008 | Basic Science | International Journal of Obesity | Preclinical study of amylin combined with phentermine or sibutramine on food intake and body weight in diet-induced obese rats. |

---

## Singapore Market Information

Phentermine has **no current market registration in Singapore** (`market_status`: 未上市, 0 licenses on record). No authorization numbers, product names, or approved indication text are available to tabulate.

---

## Safety Considerations

Structured safety data (key warnings, contraindications, drug interactions) is not currently available for this drug (data gap DG001, blocking).

- **Mechanistic caution from evidence review:** As a sympathomimetic stimulant, phentermine's pharmacology may be inappropriate for, or could aggravate, conditions with pre-existing sympathetic overactivity — this is illustrated by the case-report evidence retrieved under the POTS candidate indication (PMID 26968177), which describes stimulant medication mimicking/worsening postural tachycardia rather than treating it.

Please refer to the official package insert for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 4 trial directly measuring phentermine's effect on intrahepatic fat, supported by a consistent body of review literature linking anti-obesity pharmacotherapy to NAFLD/MASLD improvement, gives fatty liver disease reasonable (L2) evidence support — but the effect is indirect (weight-mediated), phentermine's independent contribution versus its combination partner topiramate is not fully isolated, and the drug is not currently marketed in Singapore.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert data — warnings, contraindications (blocking gap DG001)
- Drug's original mechanism of action (DG002) for a complete mechanistic justification
- Evidence isolating phentermine's independent effect on hepatic fat from the topiramate component in combination studies
- Regulatory pathway assessment given phentermine's current unregistered status in Singapore
- Cardiovascular/sympathetic risk screening protocol, given the mechanistic caution raised by the POTS-related case report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

