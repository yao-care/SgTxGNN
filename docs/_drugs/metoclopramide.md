---
layout: default
title: Metoclopramide
parent: Low Evidence (L5)
nav_order: 660
evidence_level: L5
indication_count: 10
---

# Metoclopramide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Metoclopramide: From Nausea and Delayed Gastric Emptying to Gastric Ulcer

## One-Sentence Summary

Metoclopramide is a prokinetic and antiemetic drug, used for nausea, vomiting and slow gastric emptying. The TxGNN model predicts it may help with **gastric ulcer**, but the supporting evidence is weak: **2 registered clinical trials** (neither tests ulcer treatment) and **20 publications**, mostly old reviews, animal studies and unrelated physiology work.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Gastric ulcer |
| TxGNN Prediction Score | 99.93% (model rank 1471) |
| Evidence Level | L4 (preclinical and mechanistic evidence only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From the literature, metoclopramide blocks dopamine D2 receptors and stimulates 5-HT4 receptors. Together these actions speed gastric emptying and reduce nausea and vomiting. The HSA records also give no approved-indication text, so the original use described here comes from the published literature.

Metoclopramide does not suppress stomach acid and does not heal the stomach lining. Any link to gastric ulcer is therefore indirect. It could relieve gastric stasis or nausea in ulcer patients, but it would not treat the ulcer itself. The rodent studies (rat and guinea pig) suggest protection against experimental ulcers, but they are inconsistent and do not show clinical benefit. In one human study, metoclopramide did not change acid secretion in healthy volunteers. The high model score most likely reflects network proximity through motility, dyspepsia and reflux terms rather than a true treatment effect.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Double-blind RCT of metoclopramide before endoscopy in upper GI bleeding. The endpoints are repeat endoscopy and visualisation, not ulcer healing. |
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | Completed | 19 | Pharmacist-led prescribing-safety programme in primary care. It does not test metoclopramide for ulcer. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16807979](https://pubmed.ncbi.nlm.nih.gov/16807979/) | 2006 | RCT | Yonsei Med J | IV metoclopramide plus ranitidine before anaesthesia in day-case surgery (n=40). It evaluated gastric contents, not ulcer disease. |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | Randomised crossover (not formally classified) | MMW Munch Med Wochenschr | In healthy volunteers, metoclopramide did not significantly change gastrin levels or acid secretion. |
| [19225](https://pubmed.ncbi.nlm.nih.gov/19225/) | 1977 | Review | Drugs | Review of drug treatment for gastric and duodenal ulcer. No abstract was available. |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Ann Intern Med | General pharmacology and clinical uses of metoclopramide, mainly as an antiemetic and prokinetic. |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Review (not formally classified) | Postgrad Med | Strategies for refractory peptic lesions that resist standard H2-blocker or sucralfate therapy. |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal study | Arch Int Pharmacodyn Ther | In rats, metoclopramide (20 and 50 mg/kg) protected against aspirin-induced and pylorus-ligated ulcers. |
| [6436177](https://pubmed.ncbi.nlm.nih.gov/6436177/) | 1984 | Animal study | Indian J Physiol Pharmacol | In guinea pigs, protection against three ulcer models without changing acidity, probably through better gastric drainage. |
| [775822](https://pubmed.ncbi.nlm.nih.gov/775822/) | 1976 | Not classified | ZFA | Title indicates ulcer therapy with metoclopramide. No abstract was available. |
| [4779253](https://pubmed.ncbi.nlm.nih.gov/4779253/) | 1973 | Not classified | Curr Med Res Opin | Title indicates bile reflux in gastric ulcer, with effects of smoking, metoclopramide and carbenoxolone. No abstract was available. |
| [6106882](https://pubmed.ncbi.nlm.nih.gov/6106882/) | 1980 | Not classified | Med Klin | Conservative treatment of gastric ulcer. No abstract was available. |

## Singapore Market Information

Six registrations are on record; five are listed in the Evidence Pack. No approved-indication text is available for any of them.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN06638P | PULIN INJECTION 10 mg/2 ml | Injection |
| SIN02804P | METOCLOPRAMIDE TABLET 10 mg | Tablet |
| SIN03349P | METOCLOPRAMIDE SYRUP 5 mg/5 ml | Syrup |
| SIN05202P | METOCLOPRAMIDE INJECTION BP 5 mg/ml | Injection |
| SIN10581P | PULIN FILM-COATED TABLET 10 mg | Film-coated tablet |

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the Evidence Pack.
- **Neurotoxicity**: The retrieved literature includes a report of metoclopramide neurotoxicity (PMID 3059051).
- **Mechanical obstruction and perforation**: Prokinetics are contraindicated when the GI tract is mechanically obstructed. Use with a perforated ulcer is also a potential safety concern.

Please refer to the package insert for full safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is limited to old reviews, rodent studies and unrelated human physiology or procedural work. No trial tests metoclopramide as an ulcer treatment. The mechanism (prokinetic, not acid-suppressing or mucosal-healing) does not directly fit ulcer disease, so the high model score should not be read as clinical support.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A clear clinical rationale for who would benefit, for example ulcer patients with gastric stasis or nausea, and a comparison against standard acid-suppressive therapy
- Clinical evidence in ulcer patients, not surrogate or animal endpoints

Among the other predicted indications, only **gastric dilatation** (functional dilatation from gastroparesis or feed intolerance) reached the research-question stage. Its mechanism is more plausible, but its trials still need their arms verified for a metoclopramide comparator.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

