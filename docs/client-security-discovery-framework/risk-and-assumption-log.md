# Risk and Assumption Log

## Purpose

The Risk and Assumption Log records uncertainties identified during cybersecurity discovery and solution design.

Its purpose is to ensure that:

* risks are linked to business impact;
* assumptions are not treated as confirmed facts;
* unresolved questions remain visible;
* responsibilities are assigned;
* important decisions are supported by evidence;
* changes in understanding are traceable.

Risks describe what may go wrong.

Assumptions describe what is currently believed to be true but has not yet been sufficiently verified.

---

## 1. Risk and Assumption Workflow

<a href="../client-security-discovery-framework/assets/risk_assumption_workflow.svg"
target="_blank"
rel="noopener noreferrer">
Open the full-size risk and assumption workflow diagram in a new tab </a>

<a href="../client-security-discovery-framework/assets/risk_assumption_workflow.svg"
target="_blank"
rel="noopener noreferrer"> <img src="../client-security-discovery-framework/assets/risk_assumption_workflow.svg"
    alt="Risk and assumption management workflow"
    style="width: 100%; height: auto;"> </a>

---

## 2. Risk Categories

| Category     | Description                                                            |
| ------------ | ---------------------------------------------------------------------- |
| Security     | Confidentiality, integrity, availability, or accountability risk       |
| Operational  | Disruption, delay, error, or process failure                           |
| Compliance   | Legal, regulatory, contractual, or audit exposure                      |
| Financial    | Direct cost, lost revenue, penalties, or inefficient resource use      |
| Reputational | Loss of customer, partner, employee, or public trust                   |
| Technical    | Integration, compatibility, capacity, performance, or reliability risk |
| Human        | User behaviour, skill gaps, resistance, or key-person dependency       |
| Supplier     | Third-party failure, dependency, access, or service risk               |
| Project      | Scope, schedule, budget, ownership, or delivery risk                   |
| Continuity   | Inability to maintain or restore a critical service                    |

---

## 3. Risk Status

| Status            | Meaning                                                  |
| ----------------- | -------------------------------------------------------- |
| Identified        | Risk has been recorded but not yet assessed              |
| Under review      | Additional information is required                       |
| Accepted          | Risk owner has formally accepted the risk                |
| Treatment planned | Mitigation actions have been approved                    |
| In treatment      | Mitigation is being implemented                          |
| Reduced           | Treatment has lowered the risk                           |
| Transferred       | Responsibility or financial impact has been transferred  |
| Avoided           | Activity causing the risk has been stopped or redesigned |
| Closed            | Risk is no longer relevant                               |
| Escalated         | Risk requires a higher-level decision                    |

---

## 4. Risk Register

| Risk ID  | Risk statement | Category | Cause | Business impact | Likelihood          | Impact              | Rating | Existing controls | Treatment | Owner | Status     |
| -------- | -------------- | -------- | ----- | --------------- | ------------------- | ------------------- | ------ | ----------------- | --------- | ----- | ---------- |
| RISK-001 |                |          |       |                 | Low / Medium / High | Low / Medium / High |        |                   |           |       | Identified |
| RISK-002 |                |          |       |                 |                     |                     |        |                   |           |       |            |
| RISK-003 |                |          |       |                 |                     |                     |        |                   |           |       |            |

---

## 5. Risk Statement Format

A useful risk statement connects the cause, possible event, and business consequence.

> Due to **[cause]**, there is a possibility that **[event]**, resulting in **[business impact]**.

### Weak risk statement

> The VPN is insecure.

This does not explain the cause, event, or impact.

### Improved risk statement

> Due to remote access relying only on passwords, there is a possibility that compromised credentials could be used to access internal systems, resulting in unauthorised disclosure of customer and financial information.

---

## 6. Risk Assessment

A simple qualitative model may be used during early discovery.

### Likelihood

| Level  | Description                                                   |
| ------ | ------------------------------------------------------------- |
| Low    | Unlikely under normal conditions                              |
| Medium | Possible and supported by known weaknesses or previous events |
| High   | Expected, recurring, or already observed                      |

### Impact

| Level  | Description                                                                                           |
| ------ | ----------------------------------------------------------------------------------------------------- |
| Low    | Limited disruption with minor recovery effort                                                         |
| Medium | Significant operational, financial, customer, or compliance effect                                    |
| High   | Major service disruption, sensitive-data exposure, legal consequences, or serious reputational damage |

### Risk Rating

| Likelihood | Low impact | Medium impact | High impact |
| ---------- | ---------: | ------------: | ----------: |
| Low        |        Low |           Low |      Medium |
| Medium     |        Low |        Medium |        High |
| High       |     Medium |          High |        High |

The rating supports prioritisation but does not replace risk-owner judgement.

---

## 7. Risk Treatment Options

| Treatment | Description                                                            |
| --------- | ---------------------------------------------------------------------- |
| Reduce    | Implement controls that decrease likelihood or impact                  |
| Avoid     | Stop or redesign the activity creating the risk                        |
| Transfer  | Transfer part of the impact through contracts, insurance, or suppliers |
| Accept    | Formally accept the risk without additional treatment                  |
| Escalate  | Refer the risk to a person with sufficient authority                   |

A technical team may recommend treatment, but business risk acceptance should be made by an authorised risk owner.

---

## 8. Risk Treatment Plan

| Action ID | Risk ID | Treatment action | Expected effect | Owner | Due date | Evidence required | Status |
| --------- | ------- | ---------------- | --------------- | ----- | -------- | ----------------- | ------ |
| ACT-001   |         |                  |                 |       |          |                   | Open   |

Examples of evidence include:

* configuration export;
* test result;
* screenshot;
* approved procedure;
* training record;
* access review;
* incident simulation;
* monitoring event;
* management approval.

---

## 9. Residual Risk

Controls rarely eliminate all risk.

Residual risk is the risk remaining after treatment has been implemented.

| Risk ID | Initial rating | Implemented treatment | Residual likelihood | Residual impact | Residual rating | Accepted by | Date |
| ------- | -------------- | --------------------- | ------------------- | --------------- | --------------- | ----------- | ---- |
|         |                |                       |                     |                 |                 |             |      |

Residual risk should be visible to the person approving the solution.

---

## 10. Assumption Categories

| Category    | Description                                                            |
| ----------- | ---------------------------------------------------------------------- |
| Business    | Assumption about business priorities, impact, or expected outcomes     |
| Technical   | Assumption about systems, integrations, capacity, or compatibility     |
| Security    | Assumption about threats, controls, vulnerabilities, or access         |
| Operational | Assumption about support, administration, staffing, or procedures      |
| User        | Assumption about user behaviour, skills, or adoption                   |
| Compliance  | Assumption about legal, audit, contractual, or regulatory requirements |
| Project     | Assumption about budget, scope, deadlines, or resources                |
| Supplier    | Assumption about a vendor, service provider, or external dependency    |

---

## 11. Assumption Status

| Status                   | Meaning                                           |
| ------------------------ | ------------------------------------------------- |
| Open                     | Not yet validated                                 |
| Validation planned       | Validation method and owner have been assigned    |
| Confirmed                | Supported by sufficient evidence                  |
| Rejected                 | Evidence shows that the assumption is incorrect   |
| Revised                  | Original assumption has been replaced             |
| Converted to requirement | Confirmed assumption became a project requirement |
| Converted to risk        | Uncertainty was identified as a relevant risk     |
| Closed                   | No longer relevant                                |

---

## 12. Assumption Log

| Assumption ID | Assumption | Category | Source | Why it matters | Validation method | Owner | Due date | Confidence          | Status |
| ------------- | ---------- | -------- | ------ | -------------- | ----------------- | ----- | -------- | ------------------- | ------ |
| ASM-001       |            |          |        |                |                   |       |          | Low / Medium / High | Open   |
| ASM-002       |            |          |        |                |                   |       |          |                     |        |
| ASM-003       |            |          |        |                |                   |       |          |                     |        |

---

## 13. Assumption Writing Guidance

An assumption should be written as a statement that can be tested.

### Weak assumption

> Users understand MFA.

### Improved assumption

> All remote employees have access to a supported authentication method and can complete MFA enrolment without additional hardware.

### Weak assumption

> The current firewall supports the solution.

### Improved assumption

> The current firewall model supports the required VPN capacity, authentication integration, logging, and high-availability configuration.

---

## 14. Assumption Validation

| Validation method        | Example                                                    |
| ------------------------ | ---------------------------------------------------------- |
| Document review          | Review network diagram, policy, contract, or audit report  |
| Technical test           | Verify compatibility, capacity, authentication, or logging |
| Stakeholder confirmation | Obtain confirmation from an authorised owner               |
| Data analysis            | Review logs, tickets, user data, or incident history       |
| Observation              | Observe the actual process being performed                 |
| Pilot                    | Test the proposed solution with a limited user group       |
| Supplier confirmation    | Obtain written confirmation from the vendor                |
| Configuration review     | Inspect current settings and enabled controls              |

Verbal confirmation may be sufficient for low-impact matters.

High-impact assumptions should normally require stronger evidence.

---

## 15. Assumption Validation Record

| Assumption ID | Evidence reviewed | Result                                          | Decision                  | Confirmed by | Date |
| ------------- | ----------------- | ----------------------------------------------- | ------------------------- | ------------ | ---- |
|               |                   | Supported / Partially supported / Not supported | Confirm / Reject / Revise |              |      |

---

## 16. Link Between Assumptions, Risks, and Requirements

An assumption may affect more than one project element.

| Assumption ID | Related risk | Related requirement | Related decision | Effect if incorrect |
| ------------- | ------------ | ------------------- | ---------------- | ------------------- |
|               |              |                     |                  |                     |

Example:

| Assumption ID | Related risk | Related requirement | Related decision | Effect if incorrect                                   |
| ------------- | ------------ | ------------------- | ---------------- | ----------------------------------------------------- |
| ASM-001       | RISK-003     | REQ-004             | DEC-002          | Additional device-management solution may be required |

---

## 17. Example Risk Records

The following examples use a fictional secure remote-access project.

| Risk ID  | Risk statement                                                                                                                                                            | Category    | Likelihood | Impact | Rating | Existing controls          | Proposed treatment                                      | Owner          |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- | ------ | ------ | -------------------------- | ------------------------------------------------------- | -------------- |
| RISK-001 | Due to password-only remote access, compromised credentials may provide unauthorised access to internal systems, resulting in exposure of customer or financial data      | Security    | High       | High   | High   | Password policy            | Require MFA for all remote access                       | Security Owner |
| RISK-002 | Due to incomplete access records, former employees may retain remote access, resulting in unauthorised access and audit findings                                          | Operational | Medium     | High   | High   | Manual offboarding emails  | Integrate access removal into the offboarding process   | IT Manager     |
| RISK-003 | Due to limited internal technical capacity, the organisation may be unable to maintain the solution after implementation, resulting in outages or insecure configurations | Human       | Medium     | Medium | Medium | External support available | Provide documentation, training, and support escalation | IT Manager     |
| RISK-004 | Due to insufficient logging, suspicious remote-access activity may not be detected or investigated, resulting in delayed incident response                                | Security    | Medium     | High   | High   | Local device logs          | Forward events to central logging and define retention  | Security Owner |

---

## 18. Example Assumption Records

| Assumption ID | Assumption                                                                                      | Category    | Why it matters                                                  | Validation method                                 | Confidence | Status             |
| ------------- | ----------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------------- | ------------------------------------------------- | ---------- | ------------------ |
| ASM-001       | All remote employees use organisation-managed Windows devices                                   | Technical   | Device requirements depend on the available management controls | Review device inventory                           | Medium     | Open               |
| ASM-002       | The current identity provider supports MFA integration with the selected remote-access solution | Technical   | The solution design depends on this integration                 | Review documentation and perform test             | Medium     | Validation planned |
| ASM-003       | The internal IT team can administer the proposed solution after handover                        | Operational | Lack of skills may create supplier dependency                   | Interview administrators and review support model | Low        | Open               |
| ASM-004       | Ninety days of log retention is sufficient for audit and investigation needs                    | Compliance  | Incorrect retention may fail legal or contractual requirements  | Confirm with compliance owner                     | Low        | Open               |

---

## 19. Review Questions

Before closing discovery, confirm:

* Which important statements remain unverified?
* Which assumption would cause the greatest rework if incorrect?
* Which risk has no identified owner?
* Which treatment depends on another unfinished action?
* Which accepted risk requires management approval?
* Which risk is caused by user behaviour or process friction?
* Which control could create a new operational risk?
* What residual risk will remain after implementation?

---

## 20. Minimum Project Output

For a small discovery project, the minimum Risk and Assumption Log should include:

### For each risk

1. risk ID;
2. clear cause-event-impact statement;
3. likelihood;
4. impact;
5. proposed treatment;
6. risk owner;
7. current status.

### For each assumption

1. assumption ID;
2. testable assumption statement;
3. reason it matters;
4. validation method;
5. owner;
6. confidence;
7. current status.

This minimum structure is sufficient to show that uncertainty is actively managed rather than silently converted into technical decisions.
