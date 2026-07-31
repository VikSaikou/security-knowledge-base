# Methodology

## 1. Purpose and scope

This model analyzes how a defined set of ISO/IEC 27001:2022 Annex A controls and one core ISO clause activity (Clause 6.1 Risk Assessment/Treatment) depend on one another in typical operation. It focuses on **functional dependency** — which controls rely on others to work as intended — and on what becomes weaker when an upstream control is ineffective.

The model does not assess an organization's actual control maturity, does not calculate risk reduction or residual risk, and does not cover every Annex A control or every ISO clause. It is limited to the controls represented in the Level 1 and Level 2 diagrams and the consolidated dependency table. Controls outside this set may have equally important dependencies that are simply out of scope for this version.

## 2. Source model

The model combines two node types:

- **ISO/IEC 27001 clause/process nodes** — currently represented by Clause 6.1 Risk Assessment/Treatment, a core management-system activity rather than a discrete safeguard.
- **ISO/IEC 27001:2022 Annex A controls** — the technical, organizational, physical, and people safeguards referenced by short ID and paraphrased name (e.g., "5.9 Asset Inventory").

Clause 6.1 is treated differently from Annex A controls throughout the model: it is visually distinguished in every diagram (a separate node style) because it functions as a coordinating process that many Annex A controls both feed into and draw from, rather than as a standalone safeguard. Analytical dependencies — not textual or clause-numbering relationships — connect all nodes.

## 3. Control selection

Level 1 intentionally contains a limited, management-relevant set of controls. Its purpose is to remain legible in a briefing or board setting, so only controls with clear cross-domain influence and their strongest dependencies are included. Adding every control or every weak relationship would make Level 1 unusable for its intended audience.

Level 2 diagrams exist because a single compact diagram cannot represent operational nuance without becoming unreadable. Each Level 2 view expands one functional cluster — Governance + Risk; Prevent + Access + Supplier + Vulnerability; Detect + Respond + Recover — showing more of the supporting dependencies relevant to practitioners working within that domain, while cross-referencing controls that sit in other clusters.

## 4. Dependency identification

A candidate dependency was recorded only after working through the following questions:

- What becomes weaker in the target control if the source control is ineffective?
- Does the target control still function, at reduced quality, without the source — or does it stop functioning entirely?
- Does the source control enable operation, provide supporting context, provide evidence for assessment, or support recovery specifically?
- Is the relationship direct enough to record, or does it only exist through an intermediate control already captured elsewhere?
- Is the direction correct — does the source genuinely precede or enable the target, rather than the reverse?

Relationships that could not be clearly answered against these questions were excluded rather than recorded speculatively.

## 5. Relationship taxonomy

| Type | Definition | Generic example |
|---|---|---|
| `ENABLES` | The target control cannot function as intended without the source | A defined roles structure enables incident response ownership |
| `SUPPORTS` | The source strengthens or improves the target without being strictly required | Staff awareness training supports faster incident reporting |
| `PROVIDES_EVIDENCE` | The source's output is used to assess, tune, or improve the target | Compliance review findings feed into risk register updates |
| `RECOVERY_DEPENDENCY` | The target's recovery outcome specifically depends on the source | Verified backups are a precondition for restoring operations |

## 6. Strength scoring

Strength (1–5) measures the expected degree of downstream degradation in the target control if the source control fails:

1. Minor contextual contribution
2. Useful but non-essential support
3. Meaningful operational dependency
4. Strong dependency; target is materially degraded
5. Critical dependency; target may become ineffective

Strength describes dependency impact, not the general importance of a control. A control can be organizationally critical while contributing only low-strength dependencies to other controls in this model.

## 7. Confidence scoring

| Level | Meaning |
|---|---|
| High | Strongly supported by clear operational logic, consistent across typical organizations |
| Medium | Reasonable professional interpretation; likely but not universally certain |
| Low | Plausible relationship, more sensitive to organization-specific context |

Confidence reflects certainty in the relationship as a general pattern. Actual behavior in any specific organization remains contextual and may differ.

## 8. Degraded-state analysis

Each dependency row includes a "Degraded state" description — a short, plain-language statement of the operational consequence when the source control is ineffective. These statements are written to be observable and specific (e.g., "unregistered assets stay unpatched") rather than abstract restatements of the relationship, so that a reader can use them as a practical checklist when investigating a suspected control weakness.

## 9. Diagram inclusion rules

- Every dependency with Strength 4–5 must appear in Level 1 or in an appropriate Level 2 diagram.
- Weaker dependencies (typically Strength 1–2, and some Strength 3) may be recorded in the table only, to preserve diagram readability.
- Level 1 prioritizes management readability over completeness.
- Level 2 diagrams provide domain-level detail for practitioners.
- The dependency table is the authoritative, complete register; diagrams are readability-constrained views derived from it, not independent sources.

## 10. Quality assurance

The current version was reviewed against the following checks:

- Every arrow shown in a diagram exists as a corresponding row in the table.
- All Strength 4–5 dependencies are represented in at least one diagram.
- Source and target direction was reviewed for each dependency to confirm logical correctness.
- Control labels were standardized so that identical names are used across all diagrams and the table.
- The full dependency set was checked for duplicate pairs and contradictory relationship types.
- Clause/process nodes were visually distinguished from Annex A control nodes in every diagram.
- Diagram arrow counts and table row counts were reconciled and the difference explained (weaker, table-only dependencies).

## 11. Methodological limitations

This is an analytical model built for this project, not official ISO guidance, and it carries no certification or endorsement authority. Dependency relationships are typical patterns; actual behavior differs by architecture, outsourcing arrangements, control maturity, and organizational risk context. Control labels are short paraphrases for diagram compactness and are not verbatim ISO text. The model is intended to support professional judgment, not replace it — findings should be validated against an organization's actual control environment before being used to guide decisions.

## 12. Adapting the model

To adapt this model to a specific organization:

1. Confirm the scope, assets, and control set that applies to the organization.
2. Validate which represented controls are actually applicable and implemented.
3. Review each dependency's direction for correctness in the organization's environment.
4. Adjust strength and confidence ratings to reflect actual architecture and maturity.
5. Document organization-specific degraded states where they differ from the generic descriptions.
6. Obtain review and sign-off from the relevant control owners.
7. Version any changes so the adapted model remains traceable to this baseline.
