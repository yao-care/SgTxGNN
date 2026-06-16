---
layout: default
title: Estradiol
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Estradiol
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

# Estradiol: From Menopausal Hormone Therapy to Symptomatic Form of Fragile X Syndrome in Female Carrier

## One-Sentence Summary

Estradiol is the primary endogenous estrogen in humans, widely used internationally for menopausal hormone replacement therapy (HRT), primary ovarian insufficiency (POI), and hypogonadism—though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Symptomatic Form of Fragile X Syndrome in Female Carrier**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Singapore registration; internationally established for menopausal HRT, primary ovarian insufficiency, and female hypogonadism |
| Predicted New Indication | Symptomatic Form of Fragile X Syndrome in Female Carrier |
| TxGNN Prediction Score | 98.76% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Estradiol (17β-estradiol) is the biologically active form of human endogenous estrogen, primarily synthesized by granulosa cells of the ovarian follicle. It exerts its effects by binding to nuclear estrogen receptors α (ERα) and β (ERβ), which in turn modulate transcription of a wide array of target genes. ERα predominates in reproductive tissues, while ERβ is highly expressed in the brain, bone, and cardiovascular system—giving estradiol broad pleiotropic effects including neuroprotection, bone preservation, and cardiovascular modulation. Detailed mechanism of action data is not available in this evidence pack, and retrieval from DrugBank is flagged as a pending data gap.

The mechanistic rationale proposed by TxGNN connects estradiol to FMR1 premutation female carriers through the established link between FMR1 premutation (CGG repeats 55–200) and fragile X-associated primary ovarian insufficiency (FXPOI). FXPOI affects approximately 20–25% of female premutation carriers, causing early ovarian failure and consequent estrogen deficiency. Since estradiol HRT is the standard of care for POI and associated hypoestrogenism, the knowledge graph likely infers a therapeutic role via this pathway. Additionally, ERβ-mediated neuroprotective signalling in the CNS offers a theoretical basis for mitigating some of the cognitive or mood symptoms that symptomatic female carriers may experience.

However, the critical distinction is that "symptomatic FXS in female carrier" is a broader clinical entity than FXPOI alone—it may encompass FXTAS (fragile X-associated tremor/ataxia syndrome), cognitive difficulties, and emotional dysregulation that are not solely attributable to estrogen deficiency. No direct evidence exists to support estradiol as a treatment for these neurological manifestations. The high TxGNN score most likely reflects an indirect co-morbidity pathway in the training graph rather than a genuine therapeutic signal. This prediction is classified as **L5 (model prediction only)** and warrants a **Hold** decision.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Estradiol currently holds no active drug registrations with the Health Sciences Authority (HSA) of Singapore. There are 0 product licences on record and the drug is classified as **not marketed** locally.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No registrations found |

> For international reference: Estradiol is approved in multiple jurisdictions (EU, US, Japan, Taiwan) under products such as Estraderm, Progynova, Estrogel, and Vivelle-Dot for menopausal HRT, POI, and female hypogonadism.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings and contraindications specific to Singapore were flagged as a Blocking data gap (DG001). Retrieval from HSA package inserts is required before any clinical safety evaluation can proceed. Known international safety signals for estradiol include increased risk of endometrial hyperplasia (if used without progestogen), thromboembolic events, and breast cancer with long-term HRT—these should be confirmed via local labelling.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero clinical or published evidence linking estradiol to therapeutic benefit in symptomatic FMR1 premutation female carriers beyond the known management of FXPOI-related hypoestrogenism, and the TxGNN L5 prediction alone is insufficient to justify progression.

**To proceed, the following is needed:**
- Clarify the target symptom domain: if the intent is specifically to treat FXPOI-related estrogen deficiency, this falls within established HRT practice and does not require a repurposing programme
- Translational or mechanistic research demonstrating whether ERβ-mediated neuroprotection reduces cognitive/mood symptoms in FMR1 premutation carriers specifically
- At minimum one published observational study or case series of estradiol use in symptomatic female FMR1 carriers as a primary intervention
- Retrieve Estradiol MOA data from DrugBank (DG002) to support mechanistic analysis
- Obtain HSA/TFDA package insert warnings and contraindications (DG001, Blocking) before any safety assessment
- Seek HSA registration if the drug is to be used clinically in Singapore (currently 0 licences)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

