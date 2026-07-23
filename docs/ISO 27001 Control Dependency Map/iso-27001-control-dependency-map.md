# ISO 27001 Control Dependency Map

This project models how selected ISO 27001 controls depend on and reinforce one another.

The current model contains:
- **17 controls**
- **48 control dependencies**
- dependency strength ratings
- confidence ratings
- expected degraded states
- dependency rationales

The map is intended to help answer:
- What stops working when a control is ineffective?
- Which controls jointly reduce a specific risk?
- Which dependencies are strongly supported?
- Where is additional validation required?

[Download the complete dependency register](https://github.com/VikSaikou/security-knowledge-base/blob/c9884dfd3947a13174b90b3910ccc8c86537b18d/docs/assets/data/iso-27001-control-dependencies.xlsx)

## How to read the model

| Field | Meaning |
|---|---|
| Source control | The control that depends on another control |
| Target control | The supporting or required control |
| Dependency strength | Estimated importance of the dependency |
| Confidence | Confidence in the assigned dependency |
| Degraded state | What becomes weaker or unreliable |
| Rationale | Why the dependency exists |

## Controls

{{ excel_table("assets/data/iso27001-control-dependencies.xlsx", "Controls") }}

## Control dependencies

{{ excel_table("assets/data/iso27001-control-dependencies.xlsx", "Dependencies") }}

## Simplified dependency view

```mermaid
flowchart LR
    A["A.5.1 Policies"] --> B["A.5.2 Roles"]
    B --> C["A.5.15 Access Control"]
    C --> D["A.5.18 Access Rights"]
    D --> E["A.8.15 Logging"]
```

The diagram presents only selected anchor relationships.
The dependency register remains the authoritative detailed view.

Limitations

This model represents general control dependencies rather than dependencies
derived exclusively from one threat scenario or one organization.

Dependency strength and confidence values are analytical assessments and
should be validated against:

* organizational context;
* applicable risks;
* implemented processes;
* available evidence;
* control testing results.

[def]: ssets/pictures/control-dependency-chain.sv