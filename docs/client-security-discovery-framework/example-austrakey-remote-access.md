# AustraKey Remote Access Example

## Purpose

This example demonstrates how the Client Security Discovery Framework can be applied to an ambiguous client request.

The organisation, systems, people, and findings described below are fictional and created for portfolio demonstration purposes.

---

## 1. Organisation Context

**AustraKey** is a fictional fintech company headquartered in Latvia.

| Attribute | Description |
|---|---|
| Employees | Approximately 50 |
| Working model | Hybrid and remote work across several countries |
| Business | Financial technology services |
| Sensitive information | Customer personal data, financial data, employee data, and technical documentation |
| Internal IT | Small internal team supported by external service providers |
| Security objective | Improve remote access while preparing for ISO 27001 implementation |

---

## 2. Initial Client Request

The client begins the discovery conversation with the following request:

> “We need a better and more secure VPN for remote employees.”

This statement identifies a preferred technology, but it does not yet explain:

- why the current solution is insufficient;
- which users and systems are affected;
- what security failures have occurred;
- whether the main problem is technical, operational, or organisational;
- how the organisation will measure success.

The initial request is therefore treated as a starting point rather than a confirmed solution requirement.

---

## 3. Discovery Summary

During the discovery conversation, the following information is identified.

| Discovery ID | Client statement | Initial interpretation | Signal type | Confidence |
|---|---|---|---|---|
| DISC-01 | “The current VPN becomes slow during busy periods.” | Capacity or network-performance limitation may exist | Symptom | Medium |
| DISC-02 | “Some employees connect from personal devices.” | Device trust and support boundaries are unclear | Hidden need | High |
| DISC-03 | “MFA is not required for every remote user.” | Compromised passwords may provide remote access | Risk | High |
| DISC-04 | “Urgent access is sometimes approved through email.” | Approval evidence and ownership may be incomplete | Workaround | High |
| DISC-05 | “We are not always sure who still has access.” | Access reviews and offboarding may be insufficient | Hidden need | High |
| DISC-06 | “The auditor asked how remote access is monitored.” | The organisation requires stronger logging and evidence | External requirement | High |
| DISC-07 | “The internal team cannot support a very complex platform.” | Operational simplicity is an important constraint | Constraint | High |
| DISC-08 | “The solution should be ready before the next audit.” | The implementation has a fixed deadline | Constraint | Medium |

---

## 4. Identified Hidden Need

The initial request focuses on replacing or improving the VPN.

The discovery findings indicate that the broader need is:

> AustraKey requires a controlled remote-access process that combines strong authentication, approved devices, individual accountability, timely access removal, central logging, and clear operational ownership.

Replacing the VPN alone would not fully address:

- inconsistent MFA enforcement;
- access from unmanaged devices;
- delayed access removal;
- unclear approval records;
- insufficient monitoring;
- limited support capacity.

---

## 5. Current-State Process

The current remote-access process appears to operate as follows:

1. A manager requests access by email.
2. IT creates or enables remote access.
3. The employee connects using a username and password.
4. MFA may be applied depending on the account or system.
5. Device ownership and security status are not consistently verified.
6. Access is removed after IT receives an offboarding notification.
7. Logs remain distributed across individual systems.

### Current-State Weaknesses

| Area | Observed weakness |
|---|---|
| Authentication | MFA is not consistently required |
| Device trust | Personal and managed devices are not clearly separated |
| Approval | Access approval may exist only in email |
| Access lifecycle | Removal may depend on manual notification |
| Monitoring | Remote-access logs are not centrally reviewed |
| Accountability | Shared or emergency access may reduce individual attribution |
| Support | The internal team has limited capacity for complex administration |

---

## 6. Stakeholders

| Stakeholder | Responsibility |
|---|---|
| Business owner | Approves the business need and acceptable residual risk |
| IT manager | Owns implementation, support, and administration |
| Security owner | Defines security requirements and reviews evidence |
| HR | Initiates employee onboarding and offboarding |
| Line managers | Approve employee access |
| Employees | Use remote access according to defined requirements |
| External provider | Supports configuration and escalated technical issues |
| Auditor / compliance owner | Confirms required assurance evidence |

---

## 7. Key Requirements

| Requirement ID | Requirement | Type | Source | Priority | Validation method |
|---|---|---|---|---|---|
| REQ-001 | All remote access shall require MFA | Security | DISC-03 | Must | Authentication test without MFA |
| REQ-002 | Remote access shall be limited to approved user groups | Security | DISC-05 | Must | Test with authorised and unauthorised accounts |
| REQ-003 | Administrative access shall be permitted only from managed devices | Security | DISC-02 | Must | Attempt access from unmanaged device |
| REQ-004 | Remote-access events shall be centrally logged | Evidence | DISC-06 | Must | Confirm events in central logging |
| REQ-005 | Access removal shall be completed within one business day after termination | Operational | DISC-05 | Must | Offboarding workflow test |
| REQ-006 | Access requests and approvals shall be traceable | Compliance | DISC-04 | Must | Review access records |
| REQ-007 | The solution shall be supportable by the internal IT team | Operational | DISC-07 | Must | Administrator handover review |
| REQ-008 | A pilot shall be completed before full deployment | Transition | Project team | Should | Pilot report and approval |
| REQ-009 | A documented fallback process shall exist for service failure | Continuity | Security review | Should | Simulated failure test |

---

## 8. Main Risks

| Risk ID | Risk statement | Rating | Proposed treatment | Owner |
|---|---|---|---|---|
| RISK-001 | Due to inconsistent MFA enforcement, compromised credentials may provide unauthorised remote access, resulting in exposure of sensitive data | High | Require MFA for all remote users | Security owner |
| RISK-002 | Due to access from unmanaged devices, malware or insecure configurations may affect internal systems | High | Restrict sensitive access to managed devices | IT manager |
| RISK-003 | Due to delayed offboarding, former employees may retain access after termination | High | Integrate access removal with the offboarding process | HR and IT |
| RISK-004 | Due to incomplete logging, suspicious access may not be detected or investigated | High | Centralise remote-access and authentication logs | Security owner |
| RISK-005 | Due to limited internal capacity, an overly complex solution may become insecure or unavailable after implementation | Medium | Select a supportable solution and provide documentation and training | IT manager |

---

## 9. Important Assumptions

| Assumption ID | Assumption | Why it matters | Validation method | Confidence |
|---|---|---|---|---|
| ASM-001 | Most employees can use organisation-managed devices | Device-control requirements depend on available devices | Review asset inventory | Medium |
| ASM-002 | The current identity platform supports MFA integration | The solution design depends on authentication compatibility | Technical review | Medium |
| ASM-003 | The existing network can support increased remote-access demand | Performance problems may require capacity changes | Review usage and performance data | Low |
| ASM-004 | The internal IT team can manage the selected solution after training | Unsupported complexity would create supplier dependency | Interview IT team and conduct handover test | Medium |
| ASM-005 | The audit requires evidence of remote-access monitoring | Logging scope depends on the actual audit requirement | Review audit finding | High |

---

## 10. Solution Options

| Option | Advantages | Limitations |
|---|---|---|
| Existing VPN with improved configuration | Fastest implementation and lower cost | May not provide strong device-based or application-level controls |
| VPN with mandatory MFA and managed-device restrictions | Addresses the main immediate risks and is easier to support | Still provides broader network access than some users require |
| Zero Trust Network Access | Stronger application-level access and device-context controls | Higher implementation and operational complexity |

---

## 11. Initial Recommendation

The recommended short-term option is:

> Retain or replace the existing VPN with a solution that enforces MFA, approved user groups, managed-device restrictions, central logging, and documented access lifecycle controls.

This option is selected because it:

- addresses the highest-priority risks;
- can be implemented before the expected audit;
- is more realistic for the internal team to support;
- provides a foundation for later Zero Trust Network Access adoption.

A future ZTNA implementation may be evaluated after:

- identities and access ownership are standardised;
- device management coverage is confirmed;
- application access requirements are documented;
- the internal support model is mature enough.

---

## 12. Target Process

1. The manager submits a formal access request.
2. The system owner approves the required access level.
3. IT assigns access through an approved user group.
4. The user completes MFA enrolment.
5. Access is permitted only from an approved device where required.
6. Authentication and remote-access events are centrally logged.
7. Access is reviewed periodically.
8. HR termination notifications trigger access removal.
9. Exceptions are documented, time-limited, and approved.

---

## 13. Validation Plan

| Test ID | Test | Expected result | Related requirement |
|---|---|---|---|
| TEST-001 | Attempt remote login without MFA | Access is denied | REQ-001 |
| TEST-002 | Attempt login with an unauthorised account | Access is denied | REQ-002 |
| TEST-003 | Attempt administrative access from an unmanaged device | Access is denied | REQ-003 |
| TEST-004 | Complete a successful remote login | Event appears in central logging | REQ-004 |
| TEST-005 | Disable a test employee account | Remote access is removed within the defined period | REQ-005 |
| TEST-006 | Review an approved access request | Requester, approver, scope, and date are visible | REQ-006 |
| TEST-007 | Ask an internal administrator to perform a standard support task | Task can be completed using the documentation | REQ-007 |

---

## 14. Residual Risks

Even after the proposed controls are implemented, some risk will remain.

| Residual risk | Recommended response |
|---|---|
| A legitimate account and approved device may still be compromised | Monitor unusual authentication and access activity |
| MFA services may become unavailable | Maintain a controlled fallback process |
| Users may attempt to bypass device restrictions | Define and monitor exception handling |
| Manual offboarding steps may still be delayed | Review removal metrics and integrate systems where possible |
| The VPN may continue to provide broader network access than necessary | Evaluate application-level access in a later phase |

Residual risks should be reviewed and accepted by an authorised business or risk owner.

---

## 15. Traceability Example

| Discovery finding | Resulting requirement or risk | Validation |
|---|---|---|
| DISC-03: MFA is inconsistent | REQ-001 and RISK-001 | TEST-001 |
| DISC-02: Personal devices are used | REQ-003 and RISK-002 | TEST-003 |
| DISC-05: Access ownership is unclear | REQ-002, REQ-005, and RISK-003 | TEST-002 and TEST-005 |
| DISC-06: Auditor requested monitoring evidence | REQ-004 and RISK-004 | TEST-004 |
| DISC-07: Internal capacity is limited | REQ-007 and RISK-005 | TEST-007 |

---

## 16. Management Summary

AustraKey’s initial request for a more secure VPN indicates a broader remote-access governance problem.

The main risks are inconsistent MFA, access from unmanaged devices, delayed access removal, incomplete monitoring, and limited internal support capacity.

The recommended approach is to implement a supportable remote-access solution with mandatory MFA, approved-device controls, traceable access approvals, central logging, and a defined access lifecycle.

The solution should first be tested with a limited pilot group.

A later transition to Zero Trust Network Access may be considered after the organisation improves identity, device, and access-management maturity.

---

## 17. Next Steps

- confirm current user and device inventory;
- review the existing VPN configuration and performance;
- confirm MFA and logging integration options;
- validate audit and contractual requirements;
- identify the business and technical owners;
- define the pilot group;
- confirm acceptance and residual-risk approval criteria.

---

## Disclaimer

This case study is fictional.

It demonstrates a discovery and requirements-analysis approach and does not represent a completed production implementation.