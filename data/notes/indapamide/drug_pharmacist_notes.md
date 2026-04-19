# Indapamide: From Hypertension to Chronic Pulmonary Heart Disease

## One-Sentence Summary

Indapamide is a thiazide-like sulfonamide diuretic with antihypertensive properties, originally used in the management of hypertension. The TxGNN model predicts it may be effective for **Chronic Pulmonary Heart Disease (Cor Pulmonale)**, with **0 clinical trials** and **3 publications** currently providing peripheral support for this direction. The overall evidence base remains preclinical and indirect, and the current recommendation is **Hold** pending further mechanistic clarification and dedicated clinical investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (antihypertensive / thiazide-like diuretic) |
| Predicted New Indication | Chronic Pulmonary Heart Disease |
| TxGNN Prediction Score | 92.97% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Indapamide is a sulfonamide-class thiazide-like diuretic that inhibits sodium reabsorption in the distal convoluted tubule, promoting natriuresis and diuresis. Importantly, it also exerts vasodilatory effects through modulation of calcium channels in vascular smooth muscle, reducing peripheral vascular resistance independently of its diuretic action — a property that distinguishes it from conventional thiazides.

Chronic pulmonary heart disease (cor pulmonale) is characterised by right ventricular hypertrophy and eventual right heart failure, driven by sustained pulmonary arterial hypertension — most commonly secondary to chronic obstructive pulmonary disease (COPD). The theoretical basis for Indapamide's applicability lies in its ability to reduce preload: by decreasing circulating volume and alleviating fluid retention, it may ease the volume overload burden frequently seen in right-sided heart failure. A 2008 Russian observational series (PMID 19069455) reported that long-term Noliprel therapy (a fixed-dose combination of perindopril and indapamide) in COPD patients complicated by chronic pulmonary heart disease slowed cardiac remodelling, improved right and left ventricular function, and reduced pulmonary artery pressure — though the contribution of indapamide's component cannot be isolated.

However, the core pathology of cor pulmonale is elevated pulmonary vascular resistance driven by hypoxic vasoconstriction and structural remodelling — mechanisms that a diuretic cannot meaningfully reverse. Excessive diuresis may paradoxically worsen right ventricular filling pressure, precipitating haemodynamic compromise. The TxGNN model prediction likely reflects shared cardiovascular disease node connectivity in the knowledge graph rather than a direct, actionable therapeutic pathway for Indapamide in this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Indapamide in chronic pulmonary heart disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19069455](https://pubmed.ncbi.nlm.nih.gov/19069455/) | 2008 | Observational/Case Series | Klinicheskaia meditsina | Long-term Noliprel (perindopril + indapamide) in COPD complicated by chronic pulmonary heart disease significantly slowed further cardiac remodelling, improved systolic and diastolic function of both ventricles, reduced pulmonary artery pressure, increased exercise tolerance, and reduced frequency of progressive right ventricular insufficiency |
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | Review | JACC Heart Failure | Reviews the mechanistic continuum from longstanding hypertension to heart failure; sustained pressure overload induces diastolic dysfunction and concentric LV hypertrophy, providing pharmacological rationale for antihypertensive intervention to prevent cardiac remodelling |
| [19623566](https://pubmed.ncbi.nlm.nih.gov/19623566/) | 2009 | Case Report | Pharmacoepidemiology and Drug Safety | Describes indapamide overdose in an 89-year-old COPD patient resulting in prolonged severe hypotension and marked diuresis for 4.5 days — documents indapamide's potent haemodynamic and diuretic effects in a pulmonary disease context, primarily as a safety signal |

---

## Singapore Market Information

Indapamide currently has **no registered products** in Singapore under the Health Sciences Authority (HSA). There are **0 active licences** on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Full TFDA/HSA package insert data (warnings, contraindications) was not available in this evidence pack (Data Gap DG001). Detailed drug–drug interaction data was also not retrievable (DDI query returned no results). Obtaining the complete prescribing information is a **blocking requirement** before any clinical safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score of 92.97%, the supporting clinical evidence for Indapamide in chronic pulmonary heart disease is extremely sparse — limited to 3 peripheral publications with no dedicated randomised trials, and the most directly relevant study concerns a combination product (perindopril + indapamide) in a small observational series. The mechanistic link is indirect and the risk of haemodynamic harm from excessive diuresis in right heart failure patients is a genuine clinical concern that cannot be dismissed without prospective safety data.

**To proceed, the following is needed:**
- Obtain Indapamide mechanism of action data (DrugBank API, primary pharmacology literature) to formally characterise the preload-reduction and vasodilatory rationale
- Download and parse the TFDA/HSA full prescribing information PDF to identify contraindications and warnings relevant to patients with pulmonary hypertension or right heart failure
- Conduct a dedicated literature review isolating Indapamide monotherapy effects (vs. combination products such as Noliprel) in cor pulmonale or right ventricular failure
- Assess preload sensitivity thresholds in chronic pulmonary heart disease — define safe diuretic dosing ranges to avoid worsening right ventricular filling
- Consider whether the perindopril component of Noliprel (not Indapamide alone) drives the renoprotective and cardiac benefits observed in PMID 19069455
- If mechanistic review supports a plausible role, design a small proof-of-concept observational study in COPD patients with stable cor pulmonale as the minimum next clinical step