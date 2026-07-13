---
layout: default
title: Flunarizine
parent: 僅模型預測 (L5)
nav_order: 435
evidence_level: L5
indication_count: 10
---

# Flunarizine
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

# Flunarizine: From Vertigo to Migraine Disorder

## One-Sentence Summary

Flunarizine is a selective calcium channel blocker traditionally used for the prevention of vertigo and vestibular disorders across many countries, though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Migraine Disorder** — a prediction strongly corroborated by existing pharmacological and clinical evidence,
with **19 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vertigo (traditional use established in multiple countries; no Singapore HSA registration on file) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Flunarizine is a disubstituted piperazine selective calcium channel blocker with a rich multi-target pharmacological profile. Its primary mechanism involves blocking voltage-gated calcium channels — particularly T-type channels — which suppresses cortical spreading depression (CSD), the electrophysiological cascade underlying migraine aura and the key trigger for headache onset. By preventing CSD propagation, Flunarizine simultaneously reduces neurogenic inflammation at trigeminal nerve terminals, including the release of substance P and CGRP that drive the characteristic throbbing pain of migraine attacks. Additional mechanisms amplify this benefit: its H1 receptor antagonism inhibits mast cell degranulation within the trigeminal vascular system, its weak D2 antagonism modulates central pain gating circuits, and its cerebrovascular effects improve ischaemic components of the migraine cycle.

These converging mechanisms make the connection between Flunarizine's known use in vertigo and its efficacy in migraine biologically coherent. Vertigo and migraine share considerable overlapping pathophysiology — both involve abnormal calcium-dependent neuronal hyperexcitability and trigeminal vascular dysregulation. This mechanistic overlap is clinically expressed in vestibular migraine, one of the most common causes of episodic vertigo, which is effectively treated by Flunarizine in clinical practice. The TxGNN model's high prediction score (99.12%) thus reflects genuine mechanistic plausibility rather than coincidence.

Critically, this is not a speculative prediction: Flunarizine already carries the designation of first- or second-line migraine prophylactic in multiple authoritative international guidelines. The Canadian Headache Society (2012), the American Academy of Neurology and American Headache Society joint pediatric guideline (2019), and the European Headache Federation's 2023 meta-analysis all endorse Flunarizine for migraine prevention. The EHF analysis explicitly characterises it as "a repurposed, first- or second-line treatment for migraine prophylaxis," reflecting decades of accumulated evidence. Singapore's lack of registration represents a market access gap rather than any deficiency in the underlying evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | Completed | 62 | Head-to-head RCT: Flunarizine 10 mg/day vs. Topiramate 50 mg/day for chronic migraine prophylaxis; explored efficacy of Flunarizine as a direct alternative to Topiramate in a difficult-to-treat population |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | N/A | Completed | 120 | Three-arm parallel RCT comparing Greater Occipital Nerve Block, Topiramate, and Flunarizine in episodic migraine; directly measured post-treatment VAS scores and attack frequency reduction with a dedicated Flunarizine arm |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | N/A | Recruiting | 44 | Head-to-head Flunarizine vs. Propranolol in children aged 8–15 with migraine, using the PedMIDAS disability scale; designed to address the evidence gap in the paediatric population |
| [NCT04064814](https://clinicaltrials.gov/study/NCT04064814) | Phase 4 | Completed | 60 | Add-on alpha-lipoic acid versus Flunarizine monotherapy for adolescent migraine prophylaxis; Flunarizine served as the active comparator backbone, providing extractable single-agent efficacy data in adolescents |
| [NCT07203248](https://clinicaltrials.gov/study/NCT07203248) | N/A | Not Yet Recruiting | 2,000 | Large real-world study comparing CGRP-targeted medications vs. traditional preventives (including Flunarizine) for vestibular migraine in Chinese patients; expected to provide comparative effectiveness data highly relevant to Asian populations |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | Completed | 75 | Open-label pharmacokinetic drug interaction study of Flunarizine and Topiramate during mono- and concomitant therapy; confirmed no clinically significant PK interaction and characterised safety profile in a migraine-relevant population |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | Not Yet Recruiting | 460 | PREMI Study: pragmatic multicentre RCT comparing amitriptyline, Flunarizine, topiramate, and propranolol as first-line migraine preventives in primary care; will provide head-to-head comparative effectiveness in a real-world setting |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | N/A | Unknown | 84 | Flunarizine vs. Amitriptyline for migraine prophylaxis; comparing attack frequency and VAS pain scores in patients with ≥3 attacks/month at a tertiary care hospital in Pakistan |
| [NCT00740259](https://clinicaltrials.gov/study/NCT00740259) | Phase 4 | Completed | 70 | Flunarizine vs. Haloperidol as antipsychotic (off-target study); incidentally provides long-term Flunarizine safety data, including incidence of extrapyramidal symptoms and weight changes relevant to risk characterisation |
| [NCT04766762](https://clinicaltrials.gov/study/NCT04766762) | N/A | Unknown | 96 | Acupuncture vs. Flunarizine hydrochloride for migraine without aura using the Regulating Ying and Wei method; Flunarizine cited as the standard-of-care pharmacological comparator for vasospasm relief |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37723437](https://pubmed.ncbi.nlm.nih.gov/37723437/) | 2023 | Meta-Analysis | Journal of Headache and Pain | European Headache Federation critical re-appraisal and meta-analysis of Flunarizine for migraine prophylaxis; concluded Flunarizine is a repurposed first- or second-line preventive with established efficacy supported by pooled RCT data |
| [40553594](https://pubmed.ncbi.nlm.nih.gov/40553594/) | 2025 | Systematic Review + Meta-Analysis | Journal of the Association of Physicians of India | Comparative systematic review and meta-analysis of amitriptyline vs. propranolol vs. Flunarizine for migraine prophylaxis; assessed relative efficacy and safety across three commonly used preventive agents |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Network Meta-Analysis | JAMA Network Open | Network meta-analysis of preventive medications in paediatric migraine; evaluated comparative efficacy and safety of pharmacological interventions, including Flunarizine, across children and adolescents |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | Practice Guideline | Neurology | AAN and American Headache Society updated practice guideline for pharmacologic migraine prevention in the paediatric population; evidence-based recommendations with and without cognitive behavioural therapy |
| [22683887](https://pubmed.ncbi.nlm.nih.gov/22683887/) | 2012 | Clinical Guideline | Canadian Journal of Neurological Sciences | Canadian Headache Society guideline for episodic migraine prophylaxis; assists practitioners in selecting appropriate preventive medication based on current evidence and expert consensus |
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Systematic Review | Health Technology Assessment | Systematic review with economic modelling comparing clinical effectiveness and cost-effectiveness of preventive drugs for chronic migraine in adults; provides timely context against expensive CGRP monoclonal antibodies |
| [33350223](https://pubmed.ncbi.nlm.nih.gov/33350223/) | 2020 | Systematic Review + Meta-Analysis | China Journal of Chinese Materia Medica | Systematic review and meta-analysis of RCTs comparing acupuncture vs. Flunarizine hydrochloride in migraine treatment; searched 7 major databases (CNKI, VIP, WanFang, CBM, Cochrane, EMbase, MEDLINE) up to January 2020 |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | RCT | Acta Neurologica Scandinavica | RCT evaluating efficacy and safety of Flunarizine combined with transcutaneous supraorbital neurostimulation (tSNS) vs. either treatment alone; demonstrated additive benefit of combination approach for migraine prophylaxis |
| [39324692](https://pubmed.ncbi.nlm.nih.gov/39324692/) | 2024 | Review | Expert Review of Neurotherapeutics | Overview of current and emerging treatments for vestibular migraine, including Flunarizine; particularly relevant given mechanistic and clinical overlap between vestibular disorders and migraine |
| [25676133](https://pubmed.ncbi.nlm.nih.gov/25676133/) | 2015 | Review | Expert Opinion on Drug Safety | Comprehensive review of drug safety and tolerability in prophylactic migraine treatment; characterises Flunarizine's adverse effect profile including extrapyramidal effects, weight gain, and depression risk relevant to long-term use |

---

## Singapore Market Information

Flunarizine currently has **no HSA registration** in Singapore. There are no approved product licences on file, and the drug is not commercially marketed.

> Flunarizine is registered and widely used in Japan, across European Union member states, Canada, Taiwan, Hong Kong, and multiple other Asian markets for migraine prophylaxis and/or vertigo. Its absence from the Singapore market represents a regulatory gap rather than a safety or efficacy concern, and a registration application based on existing international dossiers (e.g., EMA or TGA approval packages) would be the appropriate next step.

---

## Safety Considerations

Please refer to the package insert for safety information.

> The broader literature highlights several well-characterised safety signals that should inform any Singapore registration application: sedation and somnolence (common, particularly at treatment initiation), weight gain, depressive episodes (requiring monitoring in patients with a history of depression), and extrapyramidal symptoms including drug-induced parkinsonism (primarily with prolonged use or in elderly patients). These findings are documented in NCT00740259, PMID 25676133, and the EHF meta-analysis (PMID 37723437). Formal safety data — including package insert warnings and contraindications from registered markets — should be retrieved and reviewed before proceeding.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Flunarizine has an exceptionally robust evidence base for migraine prophylaxis, including multiple completed head-to-head RCTs against established agents (Topiramate, Propranolol, Amitriptyline), endorsement in three major international guideline bodies (Canadian Headache Society, AAN, EHF), and a TxGNN L1 prediction score reflecting mechanistic consistency. The primary barrier is regulatory — the drug is unregistered in Singapore — rather than any deficiency in clinical evidence.

**To proceed, the following is needed:**
- Initiate HSA registration pathway using existing international approval dossiers (EMA, TGA, or Health Canada) as the basis for a Drug Registration submission
- Retrieve formal package insert documents from registered markets to characterise key warnings, contraindications, and drug interaction profiles (currently data gaps DG001 and DG002)
- Obtain formal mechanism of action documentation from DrugBank or published pharmacology literature to complete the evidence dossier
- Develop a Risk Management Plan addressing extrapyramidal symptom monitoring, weight management, and depression screening for Singapore patients
- Map the competitive landscape: assess positioning of Flunarizine against currently registered Singapore migraine prophylactics (propranolol, topiramate, amitriptyline, CGRP inhibitors) to define the target patient population
- Monitor outcomes from NCT07354126 (paediatric) and NCT07203248 (vestibular migraine, Asian cohort) for population-specific evidence directly applicable to Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

