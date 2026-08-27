---
layout: default
title: Human Thrombin
parent: 僅模型預測 (L5)
nav_order: 496
evidence_level: L5
indication_count: 10
---

# Human Thrombin
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

# Human Thrombin: From Surgical Hemostasis to Primary Release Disorder of Platelets

## One-Sentence Summary

Human thrombin is a serine protease and a central enzyme in the coagulation cascade, used clinically as a topical hemostatic agent in surgery and for endoscopic control of variceal bleeding.
The TxGNN model predicts it may be effective for **primary release disorder of platelets** — a rare condition where platelets fail to properly secrete their granule contents upon activation —
with **13 clinical trials** and **20 publications** in the evidence base, though the majority address broader hemostatic and platelet biology rather than this specific indication directly.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Surgical hemostasis; endoscopic control of gastric/esophageal variceal bleeding |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 96.95% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Human thrombin is a serine protease generated from prothrombin through the coagulation cascade. Beyond its role in converting fibrinogen to fibrin, thrombin is the most potent physiological platelet activator known — it signals through protease-activated receptors PAR1 and PAR4 on the platelet surface, triggering shape change, granule secretion, and aggregation independently of other agonist pathways.

Primary release disorder of platelets encompasses a spectrum of conditions in which platelets fail to adequately release their dense granule contents (ADP, serotonin, calcium) or alpha granule contents (fibrinogen, von Willebrand factor, P-selectin) upon activation. The underlying defect may reside in granule formation, granule content, or the secretion machinery itself. Because thrombin activates platelets via a receptor-mediated (PAR-dependent) pathway that is structurally distinct from many of the signaling steps that are impaired in release disorders, it holds mechanistic plausibility as an agent capable of bypassing certain upstream defects and eliciting residual secretion responses. A 1976 study (PMID 984037) directly demonstrated that thrombin activates endogenous phospholipases in platelets and drives the release of arachidonic acid metabolites — the very metabolic pathway implicated in platelet dense-granule release.

However, the TxGNN prediction should be interpreted cautiously. The mechanistic connection is indirect, and the existing literature reflects physiological characterisation of thrombin–platelet interactions rather than evidence of clinical benefit in patients with defined release disorders. No clinical trial has yet prospectively evaluated exogenous thrombin as a therapy for this condition.

---

## Clinical Trial Evidence

The 13 trials retrieved by the evidence query are drawn from a broad coagulation and platelet biology search. None directly investigates human thrombin administration as a treatment for primary release disorder of platelets. The most contextually relevant are listed below:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03341156](https://clinicaltrials.gov/study/NCT03341156) | Phase 3 | Terminated | 14 | Prothrombin complex concentrate (Kcentra) vs. fresh frozen plasma in heart transplant surgery; evaluates coagulation factor supplementation in surgical coagulopathy |
| [NCT05391412](https://clinicaltrials.gov/study/NCT05391412) | Phase 4 | Unknown | 32 | Prophylactic fibrinogen concentrate in paediatric scoliosis surgery; examines coagulation factor correction in predicted surgical blood loss |
| [NCT04808895](https://clinicaltrials.gov/study/NCT04808895) | Phase 3 | Unknown | 204 | Aspirin for prevention of severe SARS-CoV-2 pneumonia; background rationale specifically cites platelet activation and inflammation-driven thrombosis as the mechanistic target |
| [NCT02850692](https://clinicaltrials.gov/study/NCT02850692) | N/A | Unknown | 60 | Portal hypertension in cystic fibrosis; investigates endothelial dysfunction and vascular pathology relevant to platelet–vessel wall interactions |
| [NCT03603769](https://clinicaltrials.gov/study/NCT03603769) | N/A | Completed | 6 | Salmon polar lipids nutraceutical; includes EFSA-regulated claims on reduced platelet aggregation as an endpoint, providing a platelet function measurement context |

> **Note:** No trials in this evidence set directly examine human thrombin as a therapeutic intervention for platelet release disorders. This constitutes a clear evidence gap for the proposed repurposing hypothesis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [984037](https://pubmed.ncbi.nlm.nih.gov/984037/) | 1976 | Basic research | Am J Hematology | Thrombin activates platelet endogenous phospholipases, liberates arachidonic acid from phospholipids, and drives cyclooxygenase-mediated eicosanoid release — directly relevant to thrombin's role in triggering the platelet release reaction |
| [1321709](https://pubmed.ncbi.nlm.nih.gov/1321709/) | 1992 | Review | Disease-a-Month | Comprehensive review of platelet function disorders; describes the four phases of platelet activation (adhesion, aggregation, secretion, procoagulant expression) and documents release/secretion defects as a distinct disease category |
| [33749992](https://pubmed.ncbi.nlm.nih.gov/33749992/) | 2021 | Review | Wound Repair Regen | Current applications of platelet gels; demonstrates that thrombin (or calcium) activation of platelets drives release of growth factors and granule contents, supporting a functional secretion-inducing role |
| [35226963](https://pubmed.ncbi.nlm.nih.gov/35226963/) | 2022 | Review | Hamostaseologie | Genetic analysis of hereditary hemorrhagic, thrombotic, and platelet disorders; covers molecular taxonomy of primary release disorders and their diagnostic workup |
| [6229030](https://pubmed.ncbi.nlm.nih.gov/6229030/) | 1983 | Review | Semin Thromb Hemost | Molecular markers in hemostatic defects; discusses biochemical pathways in platelet activation and abnormalities in the release reaction as measurable endpoints |
| [14727968](https://pubmed.ncbi.nlm.nih.gov/14727968/) | 2002 | Review | Am J Cardiovasc Drugs | New targets for antithrombotic drugs; details the platelet activation cascade via thrombin/PAR signalling and glycoprotein IIb/IIIa as points of pharmacological intervention |
| [2016486](https://pubmed.ncbi.nlm.nih.gov/2016486/) | 1991 | Review | JACC | Platelets and thrombin in restenosis after coronary angioplasty; characterises thrombin-mediated platelet activation and secretion in the context of vascular injury |
| [35344028](https://pubmed.ncbi.nlm.nih.gov/35344028/) | 2022 | Review | Biochemical Journal | Immunothrombosis and tissue factor regulation; discusses the central role of thrombin generation in both physiological and dysregulated coagulation states |
| [30986390](https://pubmed.ncbi.nlm.nih.gov/30986390/) | 2019 | Clinical review | Gastroenterology | AGA practice update on coagulation in cirrhosis; provides clinical guidance on pro-coagulant and haemostatic agent use, relevant to understanding thrombin's clinical deployment context |
| [35343037](https://pubmed.ncbi.nlm.nih.gov/35343037/) | 2022 | Laboratory study | J Thromb Haemost | Von Willebrand factor and thrombin cooperate to accelerate fibrin clotting in engineered microvessels; highlights the interaction between thrombin and platelet-derived factors in establishing haemostatic plugs |

---

## Singapore Market Information

Human thrombin (DrugBank ID: DB11571) has **no current product registrations in Singapore**. The drug is not approved or marketed in Singapore at present. This constitutes a significant regulatory barrier for any repurposing pathway in this jurisdiction and would require a full new drug application or compassionate use designation to proceed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although human thrombin has a compelling mechanistic rationale as one of the most potent physiological inducers of platelet granule secretion, the current evidence for its use in primary release disorder of platelets consists exclusively of mechanistic and physiological studies (L4), with no dedicated clinical trials and no Singapore regulatory registration. The gap between the known topical/endoscopic use of thrombin and the proposed systemic or targeted use for an inherited platelet disorder is substantial and has not been bridged by clinical data.

**To proceed, the following is needed:**
- Dedicated in vitro studies confirming that exogenous thrombin at therapeutic concentrations can rescue granule release in established cellular models of primary release disorder (dense granule deficiency, signalling pathway defects)
- Identification of specific patient subtypes (e.g., isolated dense granule deficiency vs. signalling-pathway defects) most likely to respond, given that thrombin's PAR-mediated activation operates downstream of some — but not all — release disorder mechanisms
- Pharmacokinetic and safety data for routes of administration applicable to platelet disorders (intravenous or targeted delivery), distinct from current topical/endoscopic use
- Drug information package including full mechanism of action, approved prescribing information, and safety data (currently documented as data gaps)
- Regulatory pathway assessment with Singapore HSA for first-in-class or orphan drug designation, given the rarity of primary release disorders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

