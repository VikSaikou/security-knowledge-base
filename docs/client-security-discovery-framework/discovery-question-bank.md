# Discovery Question Bank

## Purpose

This question bank supports structured cybersecurity discovery conversations.

The questions are designed to uncover more than the client’s initial technical request. They help identify:

* the business reason behind the request;
* weaknesses in the current process;
* hidden operational constraints;
* informal workarounds;
* unclear ownership;
* security and compliance risks;
* expected outcomes and success criteria.

The questions should not be used as a rigid interview script. The consultant should select and adapt them according to the client, project stage, and available time.

---

## 1. Why Is This Being Discussed Now?

These questions help identify the event, pressure, or business concern that initiated the request.

| Discovery question                                                       | What it may reveal                                                                     |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| What made this issue important now?                                      | Incident, audit finding, customer request, management pressure, or operational failure |
| Was there a specific event that initiated this project?                  | Previous incident, failed implementation, complaint, or regulatory requirement         |
| What would happen if nothing changed during the next six months?         | Actual urgency and business impact                                                     |
| How did you determine that the current solution is no longer sufficient? | Limitations of the existing control                                                    |
| Who currently experiences this problem most directly?                    | Main affected stakeholder                                                              |
| Who has previously attempted to address the issue?                       | Previous ownership and organisational knowledge                                        |
| What was tried before?                                                   | Existing controls and previous decisions                                               |
| Why did the previous approach not fully solve the problem?               | Resource, process, technology, or ownership gaps                                       |

A useful opening question is:

> What made you start reviewing this area?

This allows the client to explain the situation without forcing the conversation toward a specific product.

---

## 2. Current Process

These questions help establish how the process works in practice rather than how it is expected to work.

| Discovery question                                                         | What it may reveal                                |
| -------------------------------------------------------------------------- | ------------------------------------------------- |
| Could you describe how this process currently works from beginning to end? | Actual workflow and dependencies                  |
| Could you describe the most recent real example?                           | Difference between documented and actual practice |
| Which parts of the process are manual?                                     | Error risk and automation opportunities           |
| Where do delays usually occur?                                             | Bottlenecks                                       |
| Who makes the final decision?                                              | Decision authority                                |
| How are approvals recorded?                                                | Auditability and evidence gaps                    |
| What happens when the responsible person is unavailable?                   | Key-person dependency                             |
| Do different teams perform this process differently?                       | Lack of standardisation                           |
| How does a new employee learn this process?                                | Documentation and knowledge-management maturity   |
| Which systems, spreadsheets, emails, or tickets are used?                  | Fragmented tools and unstructured information     |

---

## 3. Workarounds and Informal Practices

Workarounds often reveal where formal security controls conflict with operational reality.

| Discovery question                                             | What it may reveal                                          |
| -------------------------------------------------------------- | ----------------------------------------------------------- |
| What do people do when the official process is too slow?       | Control bypass and shadow processes                         |
| Have employees created their own way of completing the task?   | Shadow IT, spreadsheets, personal tools, or shared accounts |
| Which exceptions are regularly required?                       | Controls that do not match business needs                   |
| Which rules are most difficult for users to follow?            | Usability and adoption problems                             |
| How are urgent requests handled?                               | Emergency access and approval weaknesses                    |
| Does any important part of the process exist only in email?    | Lack of traceability and structured records                 |
| What happens outside normal working hours?                     | Support, escalation, and incident-response gaps             |
| When was the process last bypassed, and why?                   | Real friction and behavioural risk                          |
| Are there any shared accounts or informal access arrangements? | Accountability and access-control weaknesses                |
| What information is kept outside the official system?          | Uncontrolled data storage                                   |

A workaround should not automatically be treated as user negligence.

It may indicate that the official process is too slow, unclear, unavailable, or incompatible with the work that people need to perform.

---

## 4. Business and Security Impact

These questions help translate a technical concern into business risk.

| Discovery question                                                       | What it may reveal                  |
| ------------------------------------------------------------------------ | ----------------------------------- |
| How does this problem affect daily work?                                 | Productivity and operational impact |
| How many people are regularly affected?                                  | Scale of the problem                |
| How often does the problem occur?                                        | Likelihood and frequency            |
| What happens if the issue is not detected quickly?                       | Potential impact                    |
| Has this caused delays, complaints, or missed commitments?               | Customer and reputational impact    |
| Has this issue appeared in an audit or assessment?                       | Compliance exposure                 |
| Which systems or business processes depend on this service?              | Second-order consequences           |
| Which data could be affected?                                            | Confidentiality and privacy impact  |
| How does management currently view this risk?                            | Priority and risk appetite          |
| Does the issue create additional work, delays, or direct financial loss? | Cost and resource impact            |

---

## 5. People, Roles, and Ownership

A technically effective solution can still fail when responsibility is unclear.

| Discovery question                                                     | What it may reveal                |
| ---------------------------------------------------------------------- | --------------------------------- |
| Who is the business owner of this process or system?                   | Accountability                    |
| Who will administer the solution after implementation?                 | Operational ownership             |
| Who approves changes?                                                  | Governance and decision authority |
| Whose work will change most after implementation?                      | Change impact                     |
| Who may receive additional work because of the solution?               | Hidden operational cost           |
| Who is allowed to approve exceptions?                                  | Exception governance              |
| Who should be informed when something goes wrong?                      | Escalation path                   |
| How are responsibilities divided between internal teams and suppliers? | Responsibility gaps               |
| How is knowledge transferred to new administrators?                    | Continuity risk                   |
| Who confirms that the final result is acceptable?                      | Acceptance authority              |

---

## 6. Constraints

These questions help prevent technically attractive but impractical recommendations.

| Discovery question                                        | What it may reveal                                |
| --------------------------------------------------------- | ------------------------------------------------- |
| What must not change as part of this project?             | Critical business dependencies                    |
| Which existing systems must remain in use?                | Legacy and integration constraints                |
| Are there fixed deadlines?                                | Audit, contract, procurement, or project pressure |
| How much downtime would be acceptable?                    | Availability requirements                         |
| Is there an expected budget range?                        | Realistic solution scope                          |
| What skills are available within the current team?        | Support and maintenance capability                |
| Are there approved or prohibited vendors?                 | Procurement and technology constraints            |
| Are there contractual, legal, or customer requirements?   | Compliance obligations                            |
| Are there geographical or data-location restrictions?     | Hosting and processing constraints                |
| What level of ongoing administration would be acceptable? | Long-term operational capacity                    |

The best technical solution is not suitable if the organisation cannot purchase, operate, maintain, or support it.

---

## 7. Expected Outcome

These questions help define what success should look like.

| Discovery question                                                             | What it may reveal                                 |
| ------------------------------------------------------------------------------ | -------------------------------------------------- |
| How will you know that the project has succeeded?                              | Success criteria                                   |
| What should be different for users after implementation?                       | Business outcome                                   |
| Which problem must the solution eliminate?                                     | Mandatory requirement                              |
| Which risks only need to be reduced rather than eliminated?                    | Acceptable residual risk                           |
| What evidence will management or auditors require?                             | Documentation and assurance requirements           |
| Which measurements should be compared before and after implementation?         | Baseline and metrics                               |
| Who must approve the final result?                                             | Acceptance criteria                                |
| What should happen if the pilot is unsuccessful?                               | Rollback and decision process                      |
| What would a successful result look like after three months?                   | Post-implementation expectations                   |
| Which result would be technically successful but unacceptable to the business? | Conflict between technical and business objectives |

A useful closing question is:

> What would you like to be able to report to management three months after implementation?

---

## 8. Hidden Priorities

These questions are most useful after trust has been established during the conversation.

| Discovery question                                                              | What it may reveal                           |
| ------------------------------------------------------------------------------- | -------------------------------------------- |
| If only one part of this problem could be solved, which part would matter most? | True priority                                |
| What concerns you most about this project?                                      | Personal, political, or reputational risk    |
| Who may disagree with the proposed change?                                      | Stakeholder resistance                       |
| Is there a previous project that the organisation does not want to repeat?      | Previous failure and organisational learning |
| Where is there disagreement between teams?                                      | Conflicting requirements                     |
| What would be an unpleasant surprise after implementation?                      | Unspoken expectations                        |
| What result would look successful on paper but fail in practice?                | Checkbox implementation risk                 |
| What else do people expect this solution to fix?                                | Unrealistic or hidden expectations           |
| Is there anything important that has not yet been formally documented?          | Missing organisational knowledge             |
| Which part of the situation is most difficult to explain internally?            | Sensitive or politically difficult issues    |

---

## 9. Follow-Up Questions

Short follow-up questions can be used to clarify unclear statements without making the conversation feel like an audit.

* Could you give a recent example?
* How often does that happen?
* Who is usually involved?
* What happens next?
* How is that recorded?
* How do you verify that?
* What happens when it fails?
* Is that the official process or the usual practice?
* Has that assumption been tested?
* Who could confirm this information?

---

## 10. Recording Discovery Findings

Important statements should be recorded and classified after the conversation.

| Field                       | Description                                                                                       |
| --------------------------- | ------------------------------------------------------------------------------------------------- |
| Discovery ID                | Unique reference                                                                                  |
| Client statement            | What the client said                                                                              |
| Interpretation              | What the statement may indicate                                                                   |
| Signal type                 | Requirement, symptom, hidden need, assumption, constraint, risk, workaround, or success criterion |
| Related risk or requirement | Resulting security or business consideration                                                      |
| Owner                       | Person responsible for confirming or addressing the issue                                         |
| Validation required         | Evidence or additional information needed                                                         |
| Confidence                  | High, medium, or low                                                                              |

### Example

| Discovery ID | Client statement                                                | Interpretation                                | Signal type          | Related risk or requirement                               | Owner            | Validation required     | Confidence |
| ------------ | --------------------------------------------------------------- | --------------------------------------------- | -------------------- | --------------------------------------------------------- | ---------------- | ----------------------- | ---------- |
| DISC-01      | “Urgent access is sometimes provided through a shared account.” | The normal access process may be too slow     | Workaround           | Individual accounts and emergency-access process required | IT Manager       | Account and access logs | High       |
| DISC-02      | “We are not sure who still has access.”                         | Access reviews may not be performed regularly | Hidden need          | Periodic access review required                           | System Owner     | Current user export     | High       |
| DISC-03      | “The auditor asked for MFA.”                                    | Compliance is the immediate project driver    | External requirement | MFA implementation and evidence required                  | Compliance Owner | Audit finding           | High       |

---

## Usage Guidance

The question bank contains a universal discovery core.

Project-specific modules can be added for areas such as:

* secure remote access;
* firewall implementation;
* endpoint protection;
* identity and access management;
* logging and monitoring;
* incident response;
* cloud security;
* data protection.

A typical discovery conversation should not use every question.

Questions should be selected according to:

* the client’s initial request;
* the available meeting time;
* the maturity of the organisation;
* the technical solution under consideration;
* the risks already identified.

The goal is not to complete a questionnaire.

The goal is to convert an unclear client concern into validated requirements, risks, constraints, responsibilities, and measurable outcomes.
