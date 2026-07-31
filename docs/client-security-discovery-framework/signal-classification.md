# Signal Classification

## Purpose

The Signal Classification method helps convert unstructured client statements into information that can support security decisions.

During discovery, clients may describe:

* what they want;
* what they observe;
* what they believe;
* what they fear;
* what they currently do;
* what limits the available options.

These statements should not automatically be treated as confirmed requirements.

Classification helps distinguish facts from interpretation and prevents technical decisions from being based on unsupported assumptions.

---

## 1. Signal Types

| Signal type          | Description                                                            | Typical action                                               |
| -------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------ |
| Fact                 | Information supported by evidence or confirmed by an authorised source | Record and use as an input                                   |
| Explicit requirement | A capability or outcome directly requested by the client               | Validate, prioritise, and add to the Requirements Register   |
| Symptom              | An observable problem whose root cause is not yet confirmed            | Investigate further                                          |
| Hidden need          | An underlying need inferred from several statements or behaviours      | Confirm with the client before converting into a requirement |
| Assumption           | A belief that has not yet been sufficiently verified                   | Add to the Assumption Log and define validation              |
| Constraint           | A limitation affecting the available solution options                  | Record and assess its impact                                 |
| Risk                 | A possible event that may cause business harm                          | Add to the Risk Register                                     |
| Workaround           | An informal method used when the normal process does not work          | Identify the cause and related risks                         |
| Success criterion    | A measurable condition used to determine whether the project succeeded | Define validation and acceptance evidence                    |
| Decision             | An agreed direction, approval, rejection, or risk acceptance           | Record the decision maker and rationale                      |

---

## 2. Facts

A fact should be supported by evidence or confirmed by a person authorised to provide the information.

### Example

> “The current remote-access platform supports 100 concurrent users.”

This should be classified as a fact only after reviewing:

* vendor documentation;
* licence information;
* current configuration;
* capacity reports;
* confirmation from the system owner.

Without evidence, it remains an assumption.

### Classification question

> What evidence confirms this statement?

---

## 3. Explicit Requirements

An explicit requirement describes something the client directly requests.

### Example

> “All remote users must use MFA.”

This is an explicit requirement, but additional clarification may still be required:

* Which users are included?
* Which authentication methods are acceptable?
* Are emergency accounts included?
* What happens when the MFA service is unavailable?
* Who approves exceptions?

A direct request is not automatically complete or testable.

### Classification question

> Can this statement be converted into a measurable acceptance criterion?

---

## 4. Symptoms

A symptom describes what the client observes, but not necessarily why it occurs.

### Examples

> “The VPN is slow in the evenings.”

> “Users regularly lose access.”

> “The security team receives too many alerts.”

Possible causes may include:

* insufficient capacity;
* network routing;
* configuration errors;
* expired accounts;
* unstable integrations;
* inappropriate alert thresholds;
* user training gaps.

The consultant should not convert a symptom directly into a product recommendation.

### Classification question

> What evidence would help identify the root cause?

---

## 5. Hidden Needs

A hidden need is an underlying requirement inferred from multiple discovery signals.

### Example

The client says:

* urgent access requests are approved by email;
* shared accounts are sometimes used;
* access removal may take several days;
* nobody is sure who still has access.

The visible request may be:

> “We need a better VPN.”

The likely hidden need is:

> A controlled identity and access-management process with clear ownership, individual accountability, timely access removal, and auditable approvals.

Hidden needs must be confirmed before becoming formal requirements.

### Classification question

> What broader problem would still exist even if the requested technology were implemented?

---

## 6. Assumptions

An assumption is something believed to be true but not yet sufficiently verified.

### Examples

> “All employees use managed devices.”

> “The firewall supports the required integration.”

> “The internal team can maintain the proposed solution.”

> “Ninety days of logging is sufficient.”

Each important assumption should include:

* why it matters;
* validation method;
* owner;
* confidence;
* due date;
* status.

### Classification question

> What would change if this statement proved incorrect?

---

## 7. Constraints

A constraint limits the available solution options.

### Examples

* the solution must be implemented before an audit;
* existing hardware must remain in use;
* only approved vendors may be selected;
* downtime must not exceed one hour;
* the internal team has limited administration capacity;
* data must remain within a specified jurisdiction.

Constraints may be real, negotiable, or only assumed.

### Classification questions

> Who imposed this limitation?

> Is it mandatory, preferred, or historical?

---

## 8. Risks

A risk describes a possible event and its business impact.

### Client statement

> “Former employees sometimes remain in the system for several days.”

### Risk statement

> Due to delays in the offboarding process, there is a possibility that former employees may retain access to internal systems, resulting in unauthorised access, data exposure, or audit findings.

A risk should contain:

* cause;
* possible event;
* business impact;
* owner;
* treatment decision.

### Classification question

> What negative business outcome could result from this situation?

---

## 9. Workarounds

A workaround is an informal method used when the official process is too slow, unclear, unavailable, or impractical.

### Examples

* shared accounts;
* approvals through personal messages;
* spreadsheets used instead of the official system;
* employees sending files to personal email;
* administrators bypassing change approval during urgent incidents.

Workarounds are valuable discovery signals.

They may reveal:

* excessive process friction;
* unavailable tools;
* unclear responsibility;
* unrealistic policies;
* missing emergency procedures;
* insufficient training.

### Classification question

> What problem is this workaround helping people solve?

---

## 10. Success Criteria

A success criterion defines how the client will determine whether the result is acceptable.

### Weak criterion

> The new solution should be secure.

### Improved criterion

> All remote administrative access requires MFA, is restricted to approved accounts, and generates centrally available authentication logs.

Success criteria should be:

* measurable;
* testable;
* linked to a requirement;
* approved by an appropriate stakeholder;
* supported by evidence.

### Classification question

> How will the client prove that the expected outcome has been achieved?

---

## 11. Decisions

A decision records an agreed project direction.

### Examples

* approve a pilot;
* reject a proposed vendor;
* defer device-compliance enforcement;
* accept residual risk;
* require additional testing;
* exclude a system from the current scope.

A decision record should include:

* decision;
* reason;
* decision maker;
* date;
* affected requirement or risk;
* conditions or follow-up actions.

### Classification question

> Who had the authority to make this decision?

---

## 12. Classification Decision Guide

Use the following questions when reviewing a client statement.

| Question                                                            | Likely classification |
| ------------------------------------------------------------------- | --------------------- |
| Is it supported by evidence?                                        | Fact                  |
| Is the client directly requesting an outcome or capability?         | Explicit requirement  |
| Does it describe something observable without explaining the cause? | Symptom               |
| Does it indicate a broader underlying problem?                      | Hidden need           |
| Is it believed but not yet verified?                                | Assumption            |
| Does it limit available choices?                                    | Constraint            |
| Could it lead to business harm?                                     | Risk                  |
| Is it an informal way of bypassing the normal process?              | Workaround            |
| Does it define how success will be measured?                        | Success criterion     |
| Has an authorised person approved or rejected a direction?          | Decision              |

A single statement may produce more than one signal.

---

## 13. Classification Example

### Client statement

> “When access is urgent, the team sometimes uses a shared administrator account because approval may take two days.”

### Extracted signals

| Signal                                             | Classification       | Resulting action                                          |
| -------------------------------------------------- | -------------------- | --------------------------------------------------------- |
| Approval may take two days                         | Fact or symptom      | Verify ticket and approval records                        |
| Shared administrator account is used               | Workaround           | Record the current practice and identify affected systems |
| The normal process is too slow for urgent access   | Hidden need          | Define an emergency-access process                        |
| User activity may not be individually attributable | Risk                 | Add accountability risk to the Risk Register              |
| Urgent access requires a faster approval path      | Proposed requirement | Validate with the process owner                           |
| Shared access is only used during emergencies      | Assumption           | Review logs and interview administrators                  |

---

## 14. From Signal to Project Output

| Signal type          | Project output                                      |
| -------------------- | --------------------------------------------------- |
| Fact                 | Current-state description                           |
| Explicit requirement | Requirements Register                               |
| Symptom              | Investigation or validation action                  |
| Hidden need          | Client confirmation and possible requirement        |
| Assumption           | Assumption Log                                      |
| Constraint           | Requirements Register or solution-design limitation |
| Risk                 | Risk Register                                       |
| Workaround           | Process-improvement action and related risk         |
| Success criterion    | Validation and acceptance plan                      |
| Decision             | Decision Log                                        |

---

## 15. Confidence Levels

| Confidence | Meaning                                                                             |
| ---------- | ----------------------------------------------------------------------------------- |
| High       | Supported by evidence or confirmed by an authorised owner                           |
| Medium     | Supported by several consistent statements but still requires confirmation          |
| Low        | Based mainly on interpretation, incomplete information, or one unverified statement |

Confidence describes the strength of the available information.

It does not describe the severity of a risk or the priority of a requirement.

---

## 16. Quality Check

Before finalising discovery findings, confirm that:

* client statements are separated from consultant interpretation;
* symptoms are not presented as root causes;
* assumptions have validation actions;
* hidden needs are confirmed before becoming requirements;
* constraints have an identified source;
* risks include business impact;
* workarounds are analysed without automatically blaming users;
* success criteria are measurable;
* decisions identify the authorised decision maker;
* confidence levels reflect the available evidence.

---

## Minimum Project Output

For each important discovery statement, record:

| Field            | Required content                                      |
| ---------------- | ----------------------------------------------------- |
| Discovery ID     | Unique reference                                      |
| Client statement | Original wording or accurate summary                  |
| Interpretation   | What the statement may indicate                       |
| Signal type      | Selected classification                               |
| Required action  | Validation, requirement, risk, decision, or follow-up |
| Owner            | Person responsible for the next step                  |
| Confidence       | High, medium, or low                                  |

This minimum structure demonstrates how ambiguous client information can be converted into controlled and traceable project inputs.
