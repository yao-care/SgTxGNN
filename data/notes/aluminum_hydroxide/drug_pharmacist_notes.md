# Aluminum Hydroxide: From Gastric Hyperacidity to Active Peptic Ulcer Disease

## One-Sentence Summary

Aluminum hydroxide (Al(OH)₃) is a classical antacid historically used to neutralize excess gastric acid and relieve symptoms of acid-related disorders including heartburn and hyperacidity.
The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**,
with **0 registered clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Singapore regulatory registration available |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not available from the current Evidence Pack. Based on known pharmacology, aluminum hydroxide is a classical antacid whose primary mechanism involves neutralizing secreted gastric acid through the reaction: H⁺ + Al(OH)₃ → AlCl₃ + H₂O. This raises intragastric pH, thereby reducing pepsin activity (which requires an acidic environment to remain proteolytically active). Beyond simple acid buffering, aluminum-containing antacids have been shown in multiple studies to exhibit cytoprotective properties: adsorbing bile acids, promoting endogenous prostaglandin synthesis (particularly PGE₂), and stimulating epidermal growth factor (EGF) secretion—all of which contribute to mucosal repair and ulcer healing.

The relationship between aluminum hydroxide and active peptic ulcer disease is physiologically direct. Peptic ulcers develop when the balance between aggressive factors (gastric acid, pepsin) and mucosal defense mechanisms is disrupted. By simultaneously neutralizing both acid and pepsin, and by stimulating mucosal cytoprotective pathways, aluminum hydroxide addresses multiple key pathophysiological drivers of impaired ulcer healing. Multiple RCT-level publications from the 1980s–1990s confirmed that intensive antacid therapy achieves ulcer healing rates comparable to cimetidine (50% vs 67% at 3 weeks), validating the mechanistic rationale beyond simple symptom relief.

Although modern peptic ulcer management has shifted toward proton pump inhibitors (PPIs) and *H. pylori* eradication, aluminum hydroxide retains a mechanistically coherent role—particularly for mucosal cytoprotection and adjunctive acid control. The TxGNN model's high prediction score (99.64%) reflects this well-established pharmacological basis extensively documented in the literature over five decades.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT (3-arm) | Scand J Gastroenterol | 72 patients with duodenal/prepyloric ulcers; antacid suspension (85 mmol acid buffering) vs cimetidine 1 g/day vs placebo over 12 weeks; healing rate 50% with antacid vs 67% with cimetidine vs lower with placebo at 3 weeks |
| [6086186](https://pubmed.ncbi.nlm.nih.gov/6086186/) | 1984 | RCT / Clinical Controlled Trial | Clin Gastroenterol | Comparative evaluation of antacids and anticholinergics in duodenal ulcer treatment; discusses receptor subclasses and differential efficacy of treatment combinations |
| [1769429](https://pubmed.ncbi.nlm.nih.gov/1769429/) | 1991 | Pharmacological / Mechanism Study | Digestion | Aluminum-containing antacids (Maalox 70 and Al(OH)₃) protect gastric mucosa and enhance healing of chronic gastroduodenal ulcerations; protective effects linked to prostaglandin pathways and intragastric pH modulation |
| [22950493](https://pubmed.ncbi.nlm.nih.gov/22950493/) | 2013 | Review | Curr Pharm Design | Comprehensive update on antacid gastroprotective and ulcer-healing mechanisms beyond prostaglandins; covers pre-epithelial, epithelial, and post-epithelial mucosal defense mechanisms enhanced by aluminum-containing antacids |
| [2390927](https://pubmed.ncbi.nlm.nih.gov/2390927/) | 1990 | Pharmacological Study | Dig Dis Sci | Maalox 70 and its active component Al(OH)₃ significantly enhance prostaglandin (PGE₂) and epidermal growth factor (EGF) secretion in the gastric mucosa, contributing to ulcer healing in rat models |
| [9334882](https://pubmed.ncbi.nlm.nih.gov/9334882/) | 1997 | In vitro Study | Jpn J Pharmacol | Al(OH)₃ at 0.1–1 mg/ml prevented both acid- (pH 4.0) and pepsin- (pH 4.5) induced damage to rat gastric epithelial cells; confirms direct cytoprotective activity independent of acid buffering |
| [37146](https://pubmed.ncbi.nlm.nih.gov/37146/) | 1979 | Expert Review | Fortschritte der Medizin | Antacid therapy in peptic ulcer: neutralizing capacity depends on chemical composition; optimal dosing requires 40–80 mval acid neutralization taken 1 and 3 hours after meals |
| [9305482](https://pubmed.ncbi.nlm.nih.gov/9305482/) | 1997 | Clinical Study | Aliment Pharmacol Ther | Aluminum-magnesium hydroxide antacids and H2-receptor antagonists may aggravate *H. pylori* gastritis in duodenal ulcer patients—important safety consideration in the context of *H. pylori*-associated ulcer disease |
| [2401189](https://pubmed.ncbi.nlm.nih.gov/2401189/) | 1990 | Retrospective Clinical Study | Drugs Exp Clin Res | 267 pediatric patients with peptic symptoms evaluated over 4 years; antacids among pharmacological treatments assessed for acute phase and relapse prevention in gastroduodenal ulcer disease |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | In vitro Pharmacological Study | Med Pharm Rep | Systematic evaluation of acid-neutralizing capacity (ANC) and other physicochemical properties of commercially available antacid formulations; provides framework for comparing aluminum-containing preparations |

---

## Singapore Market Information

Aluminum hydroxide (DrugBank ID: DB06723) is currently **not marketed in Singapore**. No Health Sciences Authority (HSA) regulatory registrations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple RCT-level publications and mechanistic studies provide consistent support for aluminum hydroxide in healing active peptic ulcers through acid neutralization and mucosal cytoprotection; however, its positioning requires careful qualification relative to current standard-of-care (PPIs and *H. pylori* eradication), and the absence of any Singapore regulatory registration means a formal approval pathway must be established before clinical deployment.

**To proceed, the following is needed:**
- Obtain Singapore HSA regulatory registration or document a legal basis for formulary use (e.g., unregistered therapeutic product pathway)
- Retrieve and review the full package insert (PI) to document warnings, contraindications, and special population precautions
- Confirm mechanism of action details via DrugBank API query to complete the MOA gap (DG002)
- Clarify clinical positioning: adjunctive antacid vs. standalone therapy; define target patient population not adequately covered by PPIs
- Assess long-term safety risks specific to intended population: phosphate depletion syndrome (particularly in patients with renal impairment or alcoholism), risk of aluminum accumulation in chronic kidney disease
- Evaluate interaction with *H. pylori* management protocols—evidence suggests aluminum-magnesium antacids may aggravate *H. pylori* gastritis (PMID 9305482), requiring clear patient selection criteria