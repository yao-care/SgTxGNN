---
layout: default
title: Misoprostol
parent: 僅模型預測 (L5)
nav_order: 663
evidence_level: L5
indication_count: 10
---

# Misoprostol
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

# Misoprostol: From Gastric Ulcer Prevention to Amenorrhea

## One-Sentence Summary

Misoprostol is a prostaglandin E1 (PGE1) analogue whose internationally recognized original indication is prevention of NSAID-induced gastric ulcers (it is not currently registered in the Singapore market, so no local approved-indication text is available in this evidence pack). The TxGNN model's top-ranked prediction is **Amenorrhea**, with a prediction score of **99.64%**, supported by **0 clinical trials** and **7 publications** — however, on inspection, all 7 publications actually concern misoprostol used *together with mifepristone for medical/early pregnancy termination*, not treatment of amenorrhea itself, strongly suggesting this is a knowledge-graph ontology mis-mapping rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | NSAID-induced gastric ulcer prevention (not registered in Singapore — no local license text available; based on internationally known indication) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (`original_moa` is unrecorded). Based on generally known pharmacology, misoprostol is a synthetic PGE1 analogue that acts on prostaglandin E receptors (EP2/EP3/EP4); its cytoprotective effect on gastric mucosa (increasing mucus/bicarbonate secretion, reducing acid secretion) underlies its approved use in preventing NSAID-induced ulcers, while its separate uterotonic effect (myometrial contraction, cervical ripening) underlies its well-established off-label/adjunct use in obstetrics and gynecology (labor induction, postpartum hemorrhage management, and — combined with mifepristone — medical abortion).

**Important caveat flagged in the evidence pack itself:** all 7 supporting publications for the "Amenorrhea" prediction describe misoprostol *combined with mifepristone for terminating very-early pregnancy* (defined clinically as "amenorrhea ≤35 days," i.e., using amenorrhea only as a *pregnancy-dating criterion*, not as the condition being treated). None of the evidence describes misoprostol being used to *treat* amenorrhea as a disorder. This pattern is consistent with a knowledge-graph ontology mapping error — the "amenorrhea" disease node was likely conflated with "early pregnancy" or "pregnancy termination" concepts during graph construction — rather than a real pharmacological repurposing opportunity. There is no known mechanism by which a uterotonic/abortifacient agent would be indicated for the *treatment* of amenorrhea; if anything, the pharmacology points the opposite direction (termination of pregnancy, not restoration of menses).

Given this, the mechanistic rationale for this specific drug–disease pair should be treated as **not credible as a genuine repurposing candidate**, despite the high raw TxGNN score. Analysts should be aware that a high model score does not guarantee a valid signal when the underlying literature reflects an ontology artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | RCT (n=744) comparing self-administered vs. hospital-administered low-dose mifepristone + misoprostol for ultra-early medical abortion (amenorrhea ≤35 days used as a pregnancy-dating criterion, not as the treated condition). |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT | Reproductive Sciences | Dose-ranging RCT (n=2500) testing lower doses of mifepristone + misoprostol for termination of ultra-early pregnancy. |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohort (Feasibility) | Human Reproduction | Feasibility of low-dose mifepristone + misoprostol given before expected menstruation to prevent unintended pregnancy. |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Cohort | J Obstet Gynaecol Res | Safety/efficacy of low-dose mifepristone combined with self-administered misoprostol for early pregnancy termination. |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Cohort | BMJ | Early report on medical management of missed abortion and anembryonic pregnancy using misoprostol-based regimens. |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Canada | Review of endometrial ablation for abnormal uterine bleeding — not directly related to misoprostol treatment. |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case Report | Cureus | Case of acute fatty liver of pregnancy presenting with amenorrhea as a symptom; not related to misoprostol treatment. |

---

## Singapore Market Information

Misoprostol currently has no registered product license in Singapore (0 registrations found in this evidence pack), so no authorization/product-level data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence supporting "Amenorrhea" as a repurposing candidate does not hold up on inspection — all cited literature concerns misoprostol + mifepristone for early pregnancy termination, not treatment of amenorrhea, and there is no plausible mechanism for a uterotonic/abortifacient agent to treat amenorrhea. This pattern strongly suggests a knowledge-graph ontology mapping artifact rather than a genuine repurposing signal, so the candidate should not advance despite the high TxGNN score.

**To proceed, the following is needed:**
- Confirm/correct the knowledge-graph disease-node mapping for "amenorrhea" vs. "pregnancy termination/early pregnancy" before trusting any further predictions built on this node
- Singapore drug label warnings/contraindications (currently a **Blocking** data gap per this evidence pack — required before any S1 safety pre-assessment can proceed)
- Mechanism-of-action data from DrugBank (currently a **High**-severity data gap affecting mechanistic-relevance analysis)
- If a genuine repurposing signal is still of interest from this same evidence pack, consider prioritizing **esophageal disease** (rank 6, evidence level L3, decision stage S2) instead — it has a direct mechanistic rationale (PGE1/EP-receptor mediated mucosal cytoprotection), a supporting case report of successful use in idiopathic esophageal ulceration (PMID 9820375), and mechanistic studies on PGE-mediated esophageal ulcer healing (PMID 25059824), making it a substantially more credible candidate than the top-ranked "Amenorrhea" prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

