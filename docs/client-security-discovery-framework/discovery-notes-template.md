# Discovery Notes Template

## Purpose

This template is used to record and structure information gathered during a cybersecurity discovery conversation.

The objective is to separate:

* confirmed facts;
* client statements;
* assumptions;
* symptoms;
* hidden needs;
* risks;
* constraints;
* decisions;
* follow-up actions.

The notes should capture what the client actually said without immediately treating every statement as a confirmed requirement.

---

## 1. Meeting Information

| Field                 | Details                                                         |
| --------------------- | --------------------------------------------------------------- |
| Client / organisation |                                                                 |
| Project / request     |                                                                 |
| Meeting date          |                                                                 |
| Meeting type          | Initial discovery / Follow-up / Technical workshop / Validation |
| Participants          |                                                                 |
| Note taker            |                                                                 |
| Document version      |                                                                 |
| Confidentiality level | Public / Internal / Confidential / Restricted                   |

---

## 2. Initial Client Request

### Client’s stated request

> Record the request using the client’s own wording.

### Reason for the request

| Question                               | Notes |
| -------------------------------------- | ----- |
| Why is this being discussed now?       |       |
| Was there a specific triggering event? |       |
| Who requested the project?             |       |
| What happens if nothing changes?       |       |
| Is there a deadline?                   |       |

### Initial interpretation

> Briefly describe what the request may indicate. Mark this as an initial interpretation, not a confirmed conclusion.

---

## 3. Current Situation

### Current process

Describe how the relevant process or system currently works.

```text
Trigger:
1.
2.
3.
Outcome:
```

### Systems and tools involved

| System / tool | Purpose | Owner | Users | Criticality | Notes |
| ------------- | ------- | ----- | ----- | ----------- | ----- |
|               |         |       |       |             |       |

### Data involved

| Data type | Where processed | Sensitivity | Access required by | Notes |
| --------- | --------------- | ----------- | ------------------ | ----- |
|           |                 |             |                    |       |

### Current controls

| Existing control | Purpose | Evidence available | Known limitation |
| ---------------- | ------- | ------------------ | ---------------- |
|                  |         |                    |                  |

---

## 4. Client Statements and Discovery Findings

Record important statements as accurately as possible.

| Discovery ID | Client statement | Interpretation | Signal type | Confidence          |
| ------------ | ---------------- | -------------- | ----------- | ------------------- |
| DISC-01      |                  |                |             | High / Medium / Low |
| DISC-02      |                  |                |             | High / Medium / Low |
| DISC-03      |                  |                |             | High / Medium / Low |

### Signal types

Use one of the following classifications:

* **Fact** — supported by evidence or confirmed by an authorised person;
* **Explicit requirement** — directly requested by the client;
* **Symptom** — observable problem without a confirmed root cause;
* **Hidden need** — underlying need inferred from the discussion;
* **Assumption** — statement that still requires validation;
* **Constraint** — limitation affecting solution design;
* **Risk** — potential negative impact;
* **Workaround** — informal method used to bypass the normal process;
* **Success criterion** — condition used to evaluate the result;
* **Decision** — agreed direction or conclusion.

---

## 5. Workarounds and Process Friction

| Workaround or issue | Why it occurs | Who uses it | Risk created | Further validation |
| ------------------- | ------------- | ----------- | ------------ | ------------------ |
|                     |               |             |              |                    |

### Questions to consider

* What happens when the normal process is too slow?
* Which steps are completed through email or spreadsheets?
* Are shared accounts or informal access methods used?
* Which rules are regularly bypassed?
* What happens outside normal working hours?
* What depends on one specific person?

---

## 6. Stakeholders and Ownership

| Role / stakeholder          | Responsibility | Decision authority | Affected by change | Concerns or expectations |
| --------------------------- | -------------- | ------------------ | ------------------ | ------------------------ |
| Business owner              |                |                    |                    |                          |
| System owner                |                |                    |                    |                          |
| Technical administrator     |                |                    |                    |                          |
| Security / compliance       |                |                    |                    |                          |
| End users                   |                |                    |                    |                          |
| Supplier / service provider |                |                    |                    |                          |

### Ownership gaps

> Record any process, system, risk, or decision that does not have a clearly identified owner.

---

## 7. Requirements

### Functional requirements

| Requirement ID | Requirement | Source | Priority              | Confirmed |
| -------------- | ----------- | ------ | --------------------- | --------- |
| REQ-F-01       |             |        | Must / Should / Could | Yes / No  |

### Security requirements

| Requirement ID | Requirement | Related risk | Priority              | Validation method |
| -------------- | ----------- | ------------ | --------------------- | ----------------- |
| REQ-S-01       |             |              | Must / Should / Could |                   |

### Operational requirements

| Requirement ID | Requirement | Owner | Support implications | Priority |
| -------------- | ----------- | ----- | -------------------- | -------- |
| REQ-O-01       |             |       |                      |          |

### Compliance or contractual requirements

| Requirement ID | Source | Requirement | Evidence required | Owner |
| -------------- | ------ | ----------- | ----------------- | ----- |
| REQ-C-01       |        |             |                   |       |

---

## 8. Constraints

| Constraint ID | Constraint | Type                                                | Impact on solution | Confirmed |
| ------------- | ---------- | --------------------------------------------------- | ------------------ | --------- |
| CON-01        |            | Budget / Time / Technical / Legal / Skills / Vendor |                    | Yes / No  |

Possible constraints include:

* budget;
* implementation deadline;
* acceptable downtime;
* existing infrastructure;
* approved vendors;
* team skills;
* procurement requirements;
* data-location restrictions;
* contractual obligations;
* support capacity.

---

## 9. Risks

| Risk ID | Risk description | Cause | Business impact | Existing controls | Proposed treatment | Owner |
| ------- | ---------------- | ----- | --------------- | ----------------- | ------------------ | ----- |
| RISK-01 |                  |       |                 |                   |                    |       |

### Risk statement format

> Due to **[cause]**, there is a possibility that **[event]**, resulting in **[business impact]**.

Example:

> Due to shared emergency accounts, there is a possibility that user actions cannot be attributed to an individual, resulting in delayed incident investigation and audit findings.

---

## 10. Assumptions and Validation

| Assumption ID | Assumption | Why it matters | Evidence required | Owner | Status                      |
| ------------- | ---------- | -------------- | ----------------- | ----- | --------------------------- |
| ASM-01        |            |                |                   |       | Open / Confirmed / Rejected |

Assumptions must not be presented as confirmed requirements until they have been validated.

---

## 11. Success Criteria

| Criterion ID | Expected outcome | Measurement | Baseline | Target | Approver |
| ------------ | ---------------- | ----------- | -------- | ------ | -------- |
| SC-01        |                  |             |          |        |          |

Examples:

* all privileged remote access requires MFA;
* inactive accounts are removed within a defined period;
* access events are available in central logging;
* failed authentication attempts generate alerts;
* the solution can be supported by the internal team;
* the business owner approves the pilot result.

---

## 12. Decisions

| Decision ID | Decision | Reason | Decision maker | Date | Related requirement or risk |
| ----------- | -------- | ------ | -------------- | ---- | --------------------------- |
| DEC-01      |          |        |                |      |                             |

---

## 13. Open Questions

| Question ID | Open question | Why it matters | Responsible person | Due date | Status          |
| ----------- | ------------- | -------------- | ------------------ | -------- | --------------- |
| Q-01        |               |                |                    |          | Open / Answered |

---

## 14. Evidence Requested

| Evidence ID | Evidence required | Purpose | Source / owner | Received | Notes |
| ----------- | ----------------- | ------- | -------------- | -------- | ----- |
| EVD-01      |                   |         |                | Yes / No |       |

Possible evidence:

* network diagram;
* user and access export;
* configuration screenshots;
* incident records;
* audit findings;
* policies and procedures;
* system inventory;
* authentication logs;
* supplier documentation;
* contractual security requirements.

---

## 15. Follow-Up Actions

| Action ID | Action | Owner | Priority            | Due date | Status                        |
| --------- | ------ | ----- | ------------------- | -------- | ----------------------------- |
| ACT-01    |        |       | High / Medium / Low |          | Open / In progress / Complete |

---

## 16. Discovery Summary

### Confirmed problem

> Summarise the problem using only confirmed information.

### Likely hidden need

> Describe the underlying need identified during discovery. Clearly mark it as an interpretation if it has not yet been validated.

### Main business risk

> Describe the most important operational, financial, compliance, security, or reputational impact.

### Recommended next step

> State the next action required before selecting or implementing a technical solution.

---

## 17. Quality Check

Before finalising the notes, confirm that:

* facts and assumptions are clearly separated;
* the client’s original wording is preserved where important;
* every important requirement has a source;
* major risks have an identified owner;
* unclear statements have follow-up questions;
* success criteria are measurable;
* operational ownership has been considered;
* evidence requirements are recorded;
* technical recommendations have not been made prematurely;
* the client can confirm or correct the summary.
