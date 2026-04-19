# Danazol: From Endometriosis to Amenorrhea

## One-Sentence Summary

Danazol is a synthetic steroid originally approved by the FDA for the treatment of endometriosis, fibrocystic breast disease, and hereditary angioedema.
The TxGNN model predicts it may be effective for **Amenorrhea**,
with **0 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis, fibrocystic breast disease, hereditary angioedema (based on known FDA approvals; no Singapore regulatory data available) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.9995% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured data fields. Based on known information from published literature, Danazol is a synthetic steroid derived from 17α-ethinyltestosterone — an "impeded androgen" with multiple and diverse biological effects. It acts by binding to steroid transport proteins in the circulation and to androgen, progesterone, and glucocorticoid receptors in target tissues. Most importantly, it centrally inhibits gonadotropin (FSH and LH) pulse secretion, suppressing gametogenesis and steroidogenesis, while also directly reducing gonadal and adrenal steroid production through effects on specific enzymatic pathways (PMID 2404115).

The connection between Danazol's established use in endometriosis and the predicted indication of amenorrhea is mechanistically direct and clinically well-documented. By creating a hypoestrogenic, hypoprogestogenic state, Danazol reliably induces anovulation and endometrial atrophy — pharmacological amenorrhea is both a known consequence and, in many clinical contexts, an explicit therapeutic goal of Danazol treatment. This mechanism has been leveraged to induce therapeutic amenorrhea in endometriosis patients, to suppress menstruation in transgender and non-binary individuals, and to manage abnormal uterine bleeding.

The prediction is therefore not speculative: multiple published clinical trials have used amenorrhea induction as a primary or co-primary endpoint when comparing Danazol against GnRH analogues (e.g., nafarelin), and a 2024 multicenter retrospective cohort study (PMID 39051650) directly evaluated Danazol for menstrual suppression in transgender individuals, confirming its reliable and clinically meaningful amenorrhea-inducing effect in contemporary practice.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2140996](https://pubmed.ncbi.nlm.nih.gov/2140996/) | 1990 | RCT | Fertility and Sterility | Double-blind RCT (n=82) comparing nafarelin 400 μg/day vs danazol 600 mg/day in endometriosis over 6 months; amenorrhea induction was a primary endpoint; both arms showed significant active lesion regression |
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Systematic Review | Menopause | Evidence-based review of pharmacological therapies for abnormal uterine bleeding; evaluates danazol among agents for inducing amenorrhea and reducing bleeding with discussion of efficacy and tolerability |
| [36434439](https://pubmed.ncbi.nlm.nih.gov/36434439/) | 2023 | Systematic Review | Archives of Gynecology and Obstetrics | Systematic review and meta-analysis of gestrinone for endometriosis; contextualises danazol-class antiestrogens as agents that induce endometrial atrophy and amenorrhea as their primary mechanism |
| [39051650](https://pubmed.ncbi.nlm.nih.gov/39051650/) | 2024 | Retrospective Cohort | Women's Health | Multicenter retrospective study directly evaluating danazol for menstrual suppression in transgender/non-binary individuals; confirms amenorrhea induction alongside reversible androgenic effects |
| [6819580](https://pubmed.ncbi.nlm.nih.gov/6819580/) | 1982 | Clinical Study | Progress in Clinical and Biological Research | Clinical study on danazol in endometriosis and infertility; documents suppression of ovarian function and amenorrhea as key therapeutic mechanisms with fertility outcomes after cessation |
| [2404115](https://pubmed.ncbi.nlm.nih.gov/2404115/) | 1990 | Review | Journal of Reproductive Medicine | Comprehensive review of danazol's biological effects; describes central FSH/LH inhibition, gonadal suppression, and immunoregulatory effects, establishing amenorrhea as a direct pharmacological consequence |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | Journal of the Royal Army Medical Corps | Comparative review of therapeutic amenorrhea induction methods; discusses danazol alongside GnRH analogues and oral contraceptives, evaluating relative efficacy and adverse effect profiles |
| [2523321](https://pubmed.ncbi.nlm.nih.gov/2523321/) | 1989 | Clinical Study | Fertility and Sterility | Randomised comparison of gestrinone vs danazol 600 mg/day (n=39 infertile patients); amenorrhea induction rate used as a treatment response metric; dose escalation performed if amenorrhea not achieved at 1 month |
| [16280355](https://pubmed.ncbi.nlm.nih.gov/16280355/) | 2006 | Review | Human Reproduction Update | Review of endometriosis management; explains the therapeutic rationale for pharmacological amenorrhea — ovarian down-regulation causes lesion regression in this estrogen-dependent disease |
| [6210867](https://pubmed.ncbi.nlm.nih.gov/6210867/) | 1982 | Clinical Study | Obstetrics and Gynecology | Double-blind dose-response study of danazol (100–600 mg/day, n=27) in endometriosis; documents dose-dependent amenorrhea induction and proportional clinical improvement across dose levels |

---

## Singapore Market Information

Danazol is currently **not marketed in Singapore**. No product registrations were found in the Health Sciences Authority (HSA) database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No registrations on file |

---

## Safety Considerations

All structured safety fields (key warnings, contraindications, drug interactions) were not retrievable from the data sources queried. Please refer to the package insert for complete safety information.

Based on published literature, the following clinically important signals are noted:

- **Androgenic side effects**: Weight gain, acne, hirsutism, oily skin, voice deepening, and clitoral enlargement have been reported at therapeutic doses
- **Contraindicated in pregnancy**: Risk of virilization of a female fetus; also contraindicated during breastfeeding due to potential androgenic effects on the nursing infant via breast milk transfer
- **Drug interaction — statins**: Co-administration of danazol 600 mg/day with lovastatin 40 mg/day has been associated with rhabdomyolysis and pancreatitis (PMID 18691993); statin dose reduction or avoidance is warranted
- **Hepatotoxicity**: Liver function monitoring is recommended during treatment; cholestatic jaundice and peliosis hepatis have been reported

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Danazol's amenorrhea-inducing effect is mechanistically direct, clinically well-established, and supported by Level 2 evidence (including an RCT with amenorrhea as a primary endpoint and multiple systematic reviews). This is not a speculative new indication but an extension of a well-documented pharmacological property into explicitly defined patient populations (e.g., endometriosis with therapeutic amenorrhea goals, transgender individuals requiring menstrual suppression).

**To proceed, the following is needed:**

- **Regulatory pathway assessment**: Danazol has zero Singapore registrations; a full HSA product registration application would be required before any clinical use
- **Complete safety review**: Retrieve and parse the full prescribing information (package insert) to document all contraindications, warnings, and monitoring requirements
- **MOA documentation**: Query DrugBank API (DB01406) to formally populate the mechanism of action field for regulatory submissions
- **Patient population definition**: Clarify which amenorrhea sub-indication (endometriosis-related, transgender menstrual suppression, abnormal uterine bleeding) is the primary target, as safety and monitoring requirements differ
- **Comparative effectiveness review**: Evaluate Danazol vs GnRH analogues for the target indication in Singapore clinical context, given that GnRH analogues have more favourable safety profiles for some populations
- **DDI screening**: Conduct formal drug-drug interaction assessment, particularly regarding statins and anticoagulants, using an updated interaction database