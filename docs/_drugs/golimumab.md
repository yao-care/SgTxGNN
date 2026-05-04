---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
---

# Golimumab
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

# Golimumab: From Inflammatory Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Golimumab (Simponi®) is a fully human anti-TNF-α monoclonal antibody globally approved for rheumatoid arthritis, psoriatic arthritis, and ankylosing spondylitis, though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis** with a prediction score of **99.73%**,
supported by **3 clinical trials** and **6 publications** — though none directly evaluate rheumatoid vasculitis as a primary endpoint.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis, Psoriatic Arthritis, Ankylosing Spondylitis (globally; not registered in Singapore) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Golimumab is a fully human IgG1κ monoclonal antibody that selectively binds both soluble and transmembrane forms of tumour necrosis factor-alpha (TNF-α), blocking its interaction with cell-surface receptors (p55 and p75). By neutralising TNF-α signalling, golimumab suppresses downstream pro-inflammatory cascades — including cytokine production, endothelial cell activation, and leukocyte recruitment — that are central to the pathogenesis of multiple immune-mediated inflammatory diseases. This mechanism has been clinically validated across its approved indications in rheumatoid arthritis, psoriatic arthritis, and ankylosing spondylitis.

Rheumatoid vasculitis is a severe extra-articular complication of long-standing seropositive rheumatoid arthritis, characterised by immune complex deposition and TNF-α-driven chronic vascular wall inflammation leading to necrotising vasculitis of small-to-medium vessels. Because TNF-α is a key mediator in this inflammatory cascade, golimumab's mechanism is scientifically plausible for this indication. It is notable that the clinical introduction of biologic DMARDs — including anti-TNF agents — has been historically associated with a marked reduction in the incidence of rheumatoid vasculitis, suggesting that sustained TNF inhibition may both treat and prevent this complication.

However, existing clinical evidence remains indirect. No completed randomised controlled trial has evaluated golimumab with rheumatoid vasculitis as a primary endpoint. The available data derive from observational studies in broad RA populations, individual case reports, and class-level evidence from other TNF inhibitors. The TxGNN high prediction score most likely reflects the strong topological proximity of RA and its vascular complications within the knowledge graph, rather than direct clinical validation. A formal research question needs to be established before further development is pursued.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Multinational observational study of tocilizumab in RA patients with inadequate response to non-biological DMARDs or one biologic agent; 6-month follow-up in routine clinical practice. Population may include patients with extra-articular RA manifestations, but rheumatoid vasculitis was not a primary or secondary endpoint. Provides safety background for biologic use in this patient group. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large epidemiological study examining incident immune-mediated inflammatory diseases (IMIDs) in patients treated with biologics and immunosuppressive drugs; scope is very broad and specificity for rheumatoid vasculitis is low. Relevant only as background contextual data. |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing elective total shoulder arthroplasty; not related to vasculitis pathology. Minimal relevance to this repurposing question. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Systematic Review / RCT Analysis | Int J Mol Sci | Network meta-analysis of 36 RCTs comparing five TNF inhibitors (including golimumab) on radiographic joint destruction in RA; confirms class-wide efficacy of TNFi at both standard and high doses. Provides strong indirect support for golimumab's anti-inflammatory potency in the RA spectrum. |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case Report | Rheumatology Int | RA patient on golimumab who developed pyoderma gangrenosum and pyogenic arthritis presenting as severe sepsis; the abstract explicitly notes that anti-TNF biologics have reduced the incidence of rheumatoid vasculitis in seropositive RA patients — directly supporting the mechanistic rationale. |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Cohort | Semin Arthritis Rheum | Analysis of end-stage renal disease frequency and causes in RA patients, with review of RA treatment in this setting; provides context for systemic RA complications including vasculitis-related renal involvement. |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Narrative Review | BMC Medicine | Broad review of biologic therapies for autoimmune and rheumatologic diseases; contextualises anti-TNF mechanism and discusses limitations including infection risk and administration challenges. |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case Report | Ocular Immunol Inflamm | Golimumab successfully treated refractory Behçet disease-associated uveitis (a vasculitis-spectrum condition) off-label; provides indirect evidence that golimumab can suppress vascular inflammatory pathology beyond its approved indications. |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case Report | Joint Bone Spine | Two cases of Takayasu's arteritis (large-vessel vasculitis) developing paradoxically under anti-TNF therapy; raises an important safety signal — anti-TNF agents may occasionally induce, rather than suppress, certain vasculitic conditions. This warrants careful patient selection. |

---

## Singapore Market Information

Golimumab is not currently registered in Singapore. No product authorisations were identified in the regulatory database (total registrations: 0).

For reference, golimumab is commercially available globally as **Simponi®** (subcutaneous, 50 mg/0.5 mL monthly) and **Simponi Aria®** (intravenous, 2 mg/kg), with approved indications including rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis, non-radiographic axial spondyloarthritis, and polyarticular-course juvenile idiopathic arthritis across the US, EU, and Japan. Any use in Singapore would require import under the HSA's Special Access Route (SAR) or Conditional Licensing framework.

---

## Safety Considerations

No local label data (warnings, contraindications) are available for Singapore. The following class-level considerations apply to all anti-TNF monoclonal antibodies including golimumab, based on globally published prescribing information:

- **Serious Infections**: Significant increased risk of serious bacterial, viral, fungal, and opportunistic infections. TNF-α is essential for host defence; inhibition impairs granuloma integrity.
- **Tuberculosis Reactivation**: Mandatory TB screening (TST and/or IGRA) is required before initiating therapy. Latent TB must be treated prior to golimumab use. The paradoxical case (PMID 22999907) described above underscores this concern.
- **Paradoxical Vasculitis**: Rare cases of new-onset or worsening vasculitic conditions (including Takayasu's arteritis) have been reported under anti-TNF therapy — a critical safety signal directly relevant to this repurposing question.
- **Malignancy**: Possible increased risk of lymphoma and other malignancies, particularly with long-term use and concomitant immunosuppressants.
- **Demyelinating Disorders**: New onset or exacerbation of central or peripheral demyelinating disease has been reported.
- **Heart Failure**: Use with caution or avoid in patients with NYHA Class III/IV heart failure.
- **Live Vaccines**: Do not administer live vaccines during treatment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic basis for golimumab in rheumatoid vasculitis is scientifically plausible — TNF-α is a known driver of the vascular inflammation in this condition, and anti-TNF therapy has been shown epidemiologically to reduce its incidence — the complete absence of direct RCT evidence with rheumatoid vasculitis as a primary endpoint, combined with a critical safety signal (paradoxical anti-TNF-induced vasculitis), means this cannot proceed beyond the hypothesis-generating stage without additional data.

**To proceed, the following is needed:**

- **Label retrieval**: Obtain full prescribing information (EMA SmPC or FDA label for Simponi®) to confirm formal warnings, contraindications, and dosing — this is currently a blocking data gap
- **Targeted literature search**: Conduct a systematic search specifically for anti-TNF agents in rheumatoid vasculitis as a confirmed diagnosis, including registry-based data from BSRBR, CORRONA, and other biologics registries
- **Safety signal resolution**: Critically evaluate the paradoxical vasculitis signal (PMID 22999907) and assess whether rheumatoid vasculitis (small-vessel, immune-complex mediated) is mechanistically distinct from large-vessel vasculitis (TNF-driven granuloma) for purposes of anti-TNF safety profiling
- **Epidemiological evidence**: Assess historical data on rheumatoid vasculitis incidence before and after widespread anti-TNF adoption as indirect real-world efficacy evidence
- **Regulatory pathway assessment**: Define the HSA Special Access Route requirements for off-label use of an unregistered biologic in Singapore
- **Research proposal**: If evidence review supports proceeding, design a prospective observational registry study in seropositive RA patients with active vasculitis receiving golimumab
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

