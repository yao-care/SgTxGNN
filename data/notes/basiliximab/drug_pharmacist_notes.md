# Basiliximab: From Organ Transplant Rejection to Plasma Cell Myeloma

## One-Sentence Summary

Basiliximab is a chimeric monoclonal antibody targeting the interleukin-2 receptor alpha chain (IL-2Rα / CD25), approved for prophylaxis of acute rejection in renal transplantation.
The TxGNN model predicts it may be effective for **Plasma Cell Myeloma (Multiple Myeloma)**,
with **3 clinical trials** and **3 publications** currently supporting this direction — primarily in the context of haematopoietic stem cell transplantation (HSCT)-related immune complications rather than direct anti-myeloma activity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prophylaxis of acute organ rejection in renal transplantation |
| Predicted New Indication | Plasma Cell Myeloma (Multiple Myeloma) |
| TxGNN Prediction Score | 95.61% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Basiliximab is a chimeric IgG1 monoclonal antibody that competitively antagonises the IL-2Rα subunit (CD25) on the surface of activated T lymphocytes, thereby blocking IL-2-mediated T-cell proliferation and differentiation. This immunosuppressive mechanism has been validated in solid organ transplantation for preventing host immune rejection of grafted tissue.

The mechanistic link to multiple myeloma is indirect but biologically plausible. Multiple myeloma patients frequently require autologous or allogeneic haematopoietic stem cell transplantation (HSCT) as part of their treatment trajectory. In the allogeneic HSCT setting, graft-versus-host disease (GVHD) remains the principal transplant-related complication and a major driver of transplant-related mortality. By blocking IL-2-driven activation of donor T cells, Basiliximab may prevent or attenuate acute GVHD, thereby improving transplant outcomes in myeloma patients. Some investigators have also explored whether depleting regulatory T cells (Tregs) via IL-2R blockade post-autologous HSCT can unmask a beneficial graft-versus-myeloma (GVM) immune response.

It is important to note that this prediction does **not** imply direct anti-myeloma cytotoxic activity. Rather, Basiliximab's proposed role is as a transplant immune-modulatory adjunct. The TxGNN model likely captures the network proximity between IL-2 signalling nodes, T-cell biology, and myeloma treatment pathways within its knowledge graph. Clinical evidence currently resides at the level of small pilot studies and case series, and a causative efficacy signal specific to myeloma has not been established.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | Completed | 30 | Pilot study testing whether regulatory T-cell depletion (using Basiliximab) is feasible and safe in multiple myeloma patients undergoing autologous SCT; primary focus on safety signal rather than efficacy endpoint |
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | Completed | 17 | Basiliximab in combination with cyclosporine for GVHD prevention following non-myeloablative allogeneic transplantation in haematological malignancies; myeloma-specific patient proportion not reported |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | Not Assigned | Terminated | 10 | Compared Basiliximab + cyclosporine vs cyclosporine alone for GVHD prevention; terminated early due to small sample size — provides only limited safety reference signals |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [31940591](https://pubmed.ncbi.nlm.nih.gov/31940591/) | 2020 | Prospective Cohort | Journal for Immunotherapy of Cancer | Pilot study of Treg depletion using Basiliximab in multiple myeloma patients post-autologous HSCT; Tregs reconstitute rapidly after ASCT and may suppress anti-myeloma immune responses; intervention was feasible with manageable safety profile |
| [12476283](https://pubmed.ncbi.nlm.nih.gov/12476283/) | 2002 | Case Series / Prospective | Bone Marrow Transplantation | Evaluated Basiliximab in 17 patients with steroid-refractory acute GVHD after allogeneic SCT (indications including multiple myeloma); found Basiliximab well tolerated and effective in achieving GVHD response in this refractory population |
| [28320553](https://pubmed.ncbi.nlm.nih.gov/28320553/) | 2017 | Case Reports | American Journal of Kidney Diseases | Reports 4 myeloma patients who underwent kidney transplantation (with standard immunosuppression including Basiliximab induction) after achieving sustained remission; demonstrates transplant feasibility in myeloma survivors, not a repurposing efficacy study |

---

## Singapore Market Information

Basiliximab currently has **no registered products** in Singapore. No authorisation records are available for this drug.

---

## Safety Considerations

Safety data for Basiliximab is not available in this Evidence Pack. Please refer to the originator product (Simulect®) package insert for full information on warnings, contraindications, and drug interactions. Key areas to review prior to any clinical application include:

- Hypersensitivity and anaphylactic reactions (known class risk for monoclonal antibodies)
- Infectious complications due to immunosuppression
- Potential impact on the graft-versus-myeloma (GVM) effect when used in allogeneic HSCT for myeloma (theoretical concern: over-suppression may reduce anti-tumour immunity)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between Basiliximab and plasma cell myeloma is biologically indirect — the drug does not target myeloma cells directly, but rather modulates the transplant immune environment via IL-2R blockade. Existing evidence is limited to a Phase 1 pilot (n=30), a small Phase 2 study (n=17), and a 2002 case series, none of which provide a controlled efficacy signal specifically for myeloma. The evidence level (L3) and the indirect mechanistic pathway do not yet support a repurposing development programme without a clearer clinical rationale.

**To proceed, the following is needed:**

- **MOA data gap resolution**: Retrieve full DrugBank entry for Basiliximab to formally document IL-2Rα antagonism and clarify immune-modulatory versus anti-tumour distinctions
- **Safety package review**: Download and parse the TFDA/EMA/FDA prescribing information (package insert) to document contraindications, black-box warnings, and known drug interactions
- **Focused clinical hypothesis**: Define whether the repurposing question is (a) GVHD prevention in allogeneic HSCT for myeloma, or (b) Treg depletion post-autologous HSCT to enhance GVM effect — these require distinct trial designs
- **Efficacy endpoint identification**: Identify prospective data on GVHD rates, transplant-related mortality, or progression-free survival in myeloma-specific cohorts treated with Basiliximab
- **Singapore regulatory pathway assessment**: Confirm whether Basiliximab can be accessed via named-patient, compassionate use, or clinical trial import given its current non-marketed status in Singapore

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical application.