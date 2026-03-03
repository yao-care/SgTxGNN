---
layout: default
title: CQL Syntax Notes
parent: SMART on FHIR
nav_order: 9
description: "Clinical Quality Language syntax reference"
permalink: /smart/cql-notes/
---

# CQL Syntax Learning Notes

Clinical Quality Language (CQL) reference for healthcare application developers.

---

## What is CQL?

**Clinical Quality Language (CQL)** is a high-level, domain-specific language for expressing clinical knowledge. It's used for:

- Clinical decision support rules
- Quality measures
- Research cohort definitions

---

## Basic Syntax

### Library Declaration

```cql
library DrugRepurposingLogic version '1.0.0'

using FHIR version '4.0.1'

include FHIRHelpers version '4.0.1'
```

### Context

```cql
context Patient
```

---

## Data Types

### Primitives

| Type | Example |
|------|---------|
| `Integer` | `42` |
| `Decimal` | `3.14` |
| `String` | `'Aspirin'` |
| `Boolean` | `true`, `false` |
| `DateTime` | `@2024-01-15T10:30:00` |

### Intervals

```cql
Interval[1, 10]           // Closed interval
Interval(1, 10)           // Open interval
Interval[@2024-01-01, @2024-12-31]  // Date interval
```

### Lists

```cql
{ 'Aspirin', 'Metformin', 'Lisinopril' }
```

---

## Queries

### Basic Query

```cql
define "Active Medications":
  [MedicationRequest: status = 'active']
```

### With Relationships

```cql
define "Medications for Diabetes":
  [MedicationRequest] MR
    where MR.status = 'active'
      and exists (
        [Condition: code in "Diabetes Conditions"] C
          where C.subject = MR.subject
      )
```

### Sorting and Limiting

```cql
define "Recent Medications":
  [MedicationRequest] MR
    where MR.status = 'active'
    sort by authoredOn desc
```

---

## Expressions

### Conditional Logic

```cql
define "Risk Level":
  if Score > 0.9 then 'High'
  else if Score > 0.5 then 'Medium'
  else 'Low'
```

### Null Handling

```cql
define "Safe Score":
  Coalesce(PredictionScore, 0)

define "Has Score":
  PredictionScore is not null
```

### Existence Checks

```cql
define "Has Active Medication":
  exists [MedicationRequest: status = 'active']
```

---

## Value Sets

### Definition

```cql
valueset "Diabetes Medications": 'http://example.org/fhir/ValueSet/diabetes-meds'
```

### Usage

```cql
define "Patient On Diabetes Medication":
  exists [MedicationRequest: medication in "Diabetes Medications"]
```

---

## Functions

### Built-in Functions

```cql
// String functions
Length('Aspirin')        // 7
Upper('aspirin')         // 'ASPIRIN'
StartsWith('DB00945', 'DB')  // true

// Date functions
Today()
Now()
AgeInYears()

// Math functions
Abs(-5)                  // 5
Round(3.7)              // 4
```

### Custom Functions

```cql
define function "EvidenceLevel"(score Decimal):
  case
    when score >= 0.99 then 'L4'
    else 'L5'
  end
```

---

## Drug Repurposing Example

```cql
library DrugRepurposingCDS version '1.0.0'

using FHIR version '4.0.1'
include FHIRHelpers version '4.0.1'

codesystem "DrugBank": 'https://www.drugbank.ca'

context Patient

define "Active Medications":
  [MedicationRequest] MR
    where MR.status = 'active'

define "Medications With Predictions":
  "Active Medications" MR
    where exists (
      MR.medication.coding C
        where C.system = 'https://www.drugbank.ca'
    )

define "High Confidence Candidates":
  "Medications With Predictions" MR
    return {
      medication: MR.medication.coding.display,
      drugbankId: MR.medication.coding.code
    }
```

---

## Testing CQL

### CQL Testing Framework

```cql
// Test case
define "Test Active Medication Count":
  Count("Active Medications") = 3
```

### Online Tools

- [CQL Fiddle](https://cql-runner.dataphoria.org/)
- [CQL Translator](https://github.com/cqframework/clinical_quality_language)

---

## Resources

- [CQL Specification](https://cql.hl7.org/)
- [CQL Authoring Guide](https://cql.hl7.org/02-authorsguide.html)
- [CQF Ruler](https://github.com/DBCG/cqf-ruler) - FHIR CQL Evaluation
