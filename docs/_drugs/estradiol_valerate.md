---
layout: default
title: Estradiol Valerate
parent: 僅模型預測 (L5)
nav_order: 399
evidence_level: L5
indication_count: 10
---

# Estradiol Valerate
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

# Estradiol Valerate: From Estrogen Deficiency / Menopausal Symptoms to Ovarian Dysfunction

## One-Sentence Summary

Estradiol valerate (EV, Progynova) is a synthetic estrogen prodrug of 17β-estradiol, globally established as hormone replacement therapy for estrogen deficiency and menopausal symptoms — including primary ovarian insufficiency (POI).
The TxGNN model's highest-evidence prediction (rank 10 of 10 candidates) identifies **Ovarian Dysfunction** as the most compelling repurposing target, supported by **animal studies directly testing EV in ovarian failure models**, a landmark *Lancet* systematic review, and **clinical trials with direct estradiol use**.
Singapore currently has no registered EV-containing products; a regulatory access pathway must be established before clinical deployment.

> **Note on multi-prediction context:** TxGNN identified 10 predicted indications for EV. Ranks 1–6 (fragile X syndrome, BPES, rare chromosomal trisomies) carry L5 evidence and "Hold" recommendations due to purely indirect mechanistic inferences via ovarian axis nodes. Rank 7 (anovulation) and rank 10 (ovarian dysfunction) have the strongest clinical relevance and are the focus of this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Estrogen deficiency / menopausal hormone replacement therapy (globally established; not registered in Singapore) |
| Predicted New Indication | Ovarian Dysfunction (incl. Primary Ovarian Insufficiency, POI) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Estradiol valerate is an ester prodrug that undergoes hydrolysis in the gastrointestinal mucosa to release 17β-estradiol (E2) — the primary circulating estrogen in premenopausal women. E2 acts via nuclear estrogen receptors (ERα and ERβ) in the hypothalamus, pituitary, ovaries, uterus, bone, and vasculature. In ovarian dysfunction — particularly Primary Ovarian Insufficiency (POI) — the ovary fails to produce sufficient endogenous E2, leading to elevated gonadotropins (FSH) and a sustained hypoestrogenic state that drives cardiovascular disease, osteoporosis, and psychological morbidity. Supplementing E2 via EV directly addresses the root hormonal deficit.

The mechanistic rationale is among the most direct possible in drug repurposing: EV supplies precisely the hormone that is deficient in the target condition. International guidelines from ESHRE, ACOG, and the British Menopause Society universally list physiological estradiol replacement as the cornerstone of POI management, with EV (Progynova) being one of the most widely prescribed oral formulations globally. The landmark *Lancet* review (PMID 20708256, 2010) consolidates this evidence, and PMID 29054504 directly studied EV's proteomic effects in ovariectomized rats — a validated model of ovarian failure — demonstrating that EV restores plasma protein expression patterns disrupted by estrogen withdrawal.

A critical bidirectionality caveat must be noted: two animal studies in this dataset show that EV administered at the wrong dose or developmental stage can *cause* ovarian dysfunction rather than treat it. PMID 12960066 demonstrates that prepubertal EV produces anovulation and PCOS-like cystic ovarian morphology in rats (the canonical EV-PCOS model), and PMID 31029417 shows the same model also induces thyroid dysfunction. This bidirectionality is not a disqualifier but a dose-timing precision signal: at physiological replacement doses in adult women with confirmed POI, EV is therapeutic; at supraphysiological doses or in inappropriate developmental windows, it is pathological. Rigorous patient selection, dose titration, and thyroid monitoring are mandatory.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04619914](https://clinicaltrials.gov/study/NCT04619914) | N/A | Completed | 160 | Directly compared CC + **Estradiol Valerate** vs. Letrozole for endometrial thickness and pregnancy rate in anovulatory PCOS women with prior thin endometrium; EV named explicitly as the intervention compound |
| [NCT07379502](https://clinicaltrials.gov/study/NCT07379502) | N/A | Not Yet Recruiting | 60 | Tests **Estradiol Valerate** + Letrozole vs. Letrozole alone for poorly primed endometrium in PCOS ovulation induction; most direct planned trial of EV in ovarian dysfunction context |
| [NCT07398924](https://clinicaltrials.gov/study/NCT07398924) | N/A | Completed | 90 | Randomised trial of vaginal estradiol vs. oral guaifenesin as adjuncts to clomiphene citrate; found estradiol improved endometrial thickness and cervical mucus — supports estradiol's reproductive adjunct role |
| [NCT02186782](https://clinicaltrials.gov/study/NCT02186782) | Phase 4 | Unknown | 600 | Concomitant estradiol with CC vs. CC alone for ovulation induction in infertile women; large-scale Phase 4 assessment of estrogen supplementation in reproductive restoration |
| [NCT02922348](https://clinicaltrials.gov/study/NCT02922348) | Phase 3 | Withdrawn (0 enrolled) | 0 | Planned Phase 3 RCT: HRT vs. combined OCP in women with POI; confirms the clinical question of optimal estrogen replacement for ovarian dysfunction is Phase 3-eligible; withdrawn before enrolment, so no efficacy data available |
| [NCT06686537](https://clinicaltrials.gov/study/NCT06686537) | Phase 2 | Recruiting | 20 | Investigates estradiol response mechanisms at the pituitary/hypothalamic level in obesity-associated ovarian dysfunction (reprometabolic syndrome); mechanistic underpinning for individualized EV dosing in this population |
| [NCT03819140](https://clinicaltrials.gov/study/NCT03819140) | Phase 4 | Completed | 51 | Continuous vs. cyclical combined OCP (estrogen + progestin) in PCOS; indirect evidence on the role of estrogen-containing regimens for chronic anovulation management |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20708256](https://pubmed.ncbi.nlm.nih.gov/20708256/) | 2010 | Review | *Lancet* | Landmark systematic review of POI; establishes estradiol replacement — including oral formulations such as EV — as the evidence-based standard of care for ovarian dysfunction with estrogen deficiency |
| [38715794](https://pubmed.ncbi.nlm.nih.gov/38715794/) | 2024 | Review/Editorial | *Front Endocrinol* | Current management of amenorrhea and estradiol deficiency in adolescents and young women; supports estradiol supplementation as the primary therapeutic approach across age groups |
| [29054504](https://pubmed.ncbi.nlm.nih.gov/29054504/) | 2018 | Animal Study | *J Steroid Biochem Mol Biol* | **Directly studies EV**: proteomics analysis in ovariectomized rats treated with EV shows restoration of plasma protein expression disrupted by ovarian failure — the most direct animal-level evidence for EV in ovarian dysfunction |
| [33749482](https://pubmed.ncbi.nlm.nih.gov/33749482/) | 2021 | Clinical Study | *Gynecol Endocrinol* | Estradiol valerate / nomegestrol acetate (Zoely) as first-line and rescue therapy for ovarian and deep infiltrating endometriosis; demonstrates an EV-containing preparation's clinical utility and tolerability in ovarian disease management |
| [39167808](https://pubmed.ncbi.nlm.nih.gov/39167808/) | 2024 | Review | *N Engl J Med* | Comprehensive review of sexual dysfunction in women; identifies ovarian hormone deficiency as a primary driver and estradiol restoration as the central therapeutic strategy |
| [2179787](https://pubmed.ncbi.nlm.nih.gov/2179787/) | 1990 | Review | *Obstet Gynecol* | Foundational review establishing the biological basis of estrogen therapy in ovarian hormone deficiency; historically supports EV's role across the menopausal spectrum |
| [31029417](https://pubmed.ncbi.nlm.nih.gov/31029417/) | 2019 | Animal Study | *Biochem Biophys Res Commun* | ⚠️ **Warning signal**: EV-induced PCOS model in rats also disrupts thyroid gland histology and biochemistry; clinically important — monitor thyroid function (TSH/T4) in all patients on EV |
| [12960066](https://pubmed.ncbi.nlm.nih.gov/12960066/) | 2003 | Animal Study | *Endocrinology* | ⚠️ **Warning signal**: Prepubertal EV in rats induces anovulation and PCOS-like cystic ovarian morphology via sympathetic nerve activation; confirms dose-timing precision is non-negotiable |

---

## Singapore Market Information

Estradiol valerate is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No product licences are on record. Clinicians wishing to prescribe EV would need to access it through the HSA Special Access Route (SAR) for unlicensed medicinal products, or evaluate alternative registered estradiol formulations (transdermal patches, gels, or other oral forms) that may be available in Singapore.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No registered products in Singapore | — | — |

---

## Safety Considerations

No Singapore package insert is available (no registered products). Safety guidance should be drawn from international prescribing information and established clinical literature.

- **Key Warnings**: Class-level systemic estrogen warnings apply — increased risk of venous thromboembolism, breast cancer with prolonged or high-dose use, endometrial hyperplasia/cancer if used without progestogen in women with an intact uterus, and potential cardiovascular risk in women > 10 years post-menopause or initiating HRT after age 60. Animal data in this dataset additionally flags thyroid disruption at supraphysiological doses (PMID 31029417) — a monitoring item not typically prominent in standard labels.

- **Contraindications**: Suspected or confirmed hormone-sensitive malignancies (breast, uterine); active or history of thromboembolic disease (DVT, PE); undiagnosed abnormal vaginal bleeding; severe hepatic impairment; known hypersensitivity to estradiol or valerate ester; pregnancy.

- **Drug Interactions**: CYP3A4 inducers (rifampicin, phenytoin, carbamazepine, St John's Wort) reduce estradiol plasma levels and may compromise efficacy. CYP3A4 inhibitors (azole antifungals, erythromycin) may increase estradiol exposure. Thyroid hormone replacement requirements may increase in hypothyroid patients on concurrent estrogen therapy due to elevated thyroxine-binding globulin.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Estradiol valerate has one of the most mechanistically direct rationales in the entire prediction set: it replaces the precise hormone deficient in ovarian dysfunction (POI), and is supported by international guidelines, systematic reviews, and animal studies directly using EV in ovarian failure models. The primary barriers are Singapore's absence of registered EV products and the drug's dose-dependent bidirectionality — at physiological doses it is therapeutic, at supraphysiological doses or wrong developmental timing it is pathological — making clinical protocol rigour essential.

**To proceed, the following is needed:**
- Obtain the complete EV prescribing information (Progynova/Bayer or equivalent originator) and review for full safety, contraindication, and monitoring profiles
- Confirm the HSA Special Access Route eligibility and documentation requirements for prescribing EV in Singapore, or identify registered alternative estradiol formulations as potential substitutes
- Define strict patient selection criteria: confirmed POI diagnosis with low serum E2 (< 50 pmol/L) and elevated FSH (> 25 IU/L) on two measurements ≥ 4 weeks apart
- Establish a monitoring protocol covering: thyroid function (TSH/fT4) at baseline and every 6 months; bone density (DXA) at baseline and annually; cardiovascular risk profile; endometrial surveillance in women with intact uterus (add progestogen; transvaginal ultrasound annually)
- For adjunctive use in anovulation/ovulation induction: initiate a prospective case series in Singapore documenting EV dose, co-medication (letrozole/CC), endometrial thickness response, and pregnancy outcomes, before committing to a full RCT
- Address the thyroid monitoring gap flagged by PMID 31029417 — this is not prominent in standard EV labels and should be explicitly included in local clinical guidance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

