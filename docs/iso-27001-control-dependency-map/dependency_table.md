# ISO/IEC 27001:2022 Control Dependency Table


| Source | Target | Type | Strength | Confidence | Degraded state |
|---|---|---|---|---|---|
| 5.1 InfoSec Policy | 5.2 Roles & Resp. | ENABLES | 4 | High | Roles lose formal authority; accountability blurs. |
| 5.1 InfoSec Policy | Cl.6.1 Risk Assess/Treat | ENABLES | 4 | High | Risk management loses mandate, becomes ad hoc. |
| 5.1 InfoSec Policy | 5.10 Acceptable Use | ENABLES | 4 | High | Acceptable-use rules lack authority and enforcement basis. |
| 5.9 Asset Inventory | Cl.6.1 Risk Assess/Treat | ENABLES | 5 | High | Unknown assets stay unassessed; risk picture incomplete. |
| 5.9 Asset Inventory | 5.12 Classification | ENABLES | 4 | High | Assets can't be reliably classified with an incomplete inventory. |
| 5.2 Roles & Resp. | Cl.6.1 Risk Assess/Treat | SUPPORTS | 3 | Medium | Risk items lack owners; treatment stalls. |
| 5.2 Roles & Resp. | 5.24 Incident Planning | ENABLES | 4 | High | Incident plan lacks assigned responders. |
| 5.7 Threat Intelligence | Cl.6.1 Risk Assess/Treat | SUPPORTS | 3 | Medium | Risk assessments miss current threat context. |
| 5.36 Compliance Review | Cl.6.1 Risk Assess/Treat | PROVIDES_EVIDENCE | 3 | Medium | Risk register misses audit-found control failures. |
| 5.36 Compliance Review | 5.1 InfoSec Policy | PROVIDES_EVIDENCE | 2 | Low | Policy drifts out of date without review updates. |
| 5.27 Incident Learning | Cl.6.1 Risk Assess/Treat | PROVIDES_EVIDENCE | 3 | Medium | Risk register doesn't reflect real incident history. |
| Cl.6.1 Risk Assess/Treat | 5.15 Access Control | ENABLES | 4 | High | Access rules become generic, not risk-tailored. |
| Cl.6.1 Risk Assess/Treat | 5.19 Supplier Security | ENABLES | 3 | Medium | Supplier due diligence loses prioritization. |
| Cl.6.1 Risk Assess/Treat | 8.8 Vuln Mgmt | ENABLES | 3 | Medium | Patch prioritization loses risk grounding. |
| Cl.6.1 Risk Assess/Treat | 5.30 BC Readiness | ENABLES | 4 | High | Continuity scope becomes guesswork. |
| Cl.6.1 Risk Assess/Treat | 6.3 Awareness Training | SUPPORTS | 4 | High | Training content isn't risk-prioritized; effort misallocated. |
| 5.9 Asset Inventory | 8.8 Vuln Mgmt | ENABLES | 5 | High | Unregistered assets stay unpatched. |
| 5.9 Asset Inventory | 8.15 Logging | ENABLES | 4 | High | Logging has blind spots on unmanaged systems. |
| 5.9 Asset Inventory | 5.30 BC Readiness | SUPPORTS | 3 | Medium | Continuity plans misjudge critical systems. |
| 5.9 Asset Inventory | 8.1 Endpoint Devices | ENABLES | 3 | High | Unregistered endpoints escape security management. |
| 5.12 Classification | 8.10 Info Deletion | ENABLES | 3 | Medium | Deletion/retention rules become inconsistent. |
| 5.12 Classification | 5.15 Access Control | SUPPORTS | 3 | Medium | Access decisions lose sensitivity-based justification. |
| 5.15 Access Control | 8.5 Secure Auth | ENABLES | 4 | High | Authentication strength drifts below risk profile. |
| 5.15 Access Control | 8.2 Privileged Access | ENABLES | 4 | High | Privileged accounts proliferate inconsistently. |
| 5.15 Access Control | 5.18 Access Lifecycle | ENABLES | 5 | High | Provisioning/de-provisioning loses policy basis; orphaned accounts accumulate. |
| 5.18 Access Lifecycle | 8.2 Privileged Access | SUPPORTS | 3 | Medium | Privileged accounts aren't consistently reviewed/removed. |
| 5.19 Supplier Security | 8.8 Vuln Mgmt | SUPPORTS | 2 | Medium | Vendor-component vulnerabilities go untracked. |
| 5.19 Supplier Security | Cl.6.1 Risk Assess/Treat | PROVIDES_EVIDENCE | 2 | Low | Risk register misses supply-chain exposure. |
| 5.19 Supplier Security | 5.23 Cloud Security | ENABLES | 4 | High | Cloud provider risk goes unmanaged. |
| 5.10 Acceptable Use | 6.3 Awareness Training | SUPPORTS | 3 | Medium | Training lacks concrete behavioral rules to reinforce. |
| 6.3 Awareness Training | 5.26 Incident Response | SUPPORTS | 4 | Medium | Incidents reported late or missed by staff. |
| 6.3 Awareness Training | 5.15 Access Control | SUPPORTS | 2 | Low | Credential sharing erodes access control. |
| 6.3 Awareness Training | 8.7 Malware Protection | SUPPORTS | 2 | Low | Users more likely to trigger malware via unsafe behavior. |
| 8.1 Endpoint Devices | 8.7 Malware Protection | ENABLES | 4 | High | Malware protection coverage becomes inconsistent. |
| 8.1 Endpoint Devices | 5.15 Access Control | SUPPORTS | 2 | Low | Access decisions can't factor device trust/posture. |
| 8.7 Malware Protection | 8.16 Monitoring | SUPPORTS | 3 | Medium | Malware infections take longer to detect. |
| 8.32 Change Management | 8.9 Config Management | ENABLES | 4 | High | Configuration drifts uncontrolled. |
| 8.9 Config Management | 8.8 Vuln Mgmt | ENABLES | 4 | High | Vulnerability scanning loses a secure baseline. |
| 8.9 Config Management | 8.6 Capacity Mgmt | SUPPORTS | 2 | Low | Capacity planning lacks an accurate configuration baseline. |
| 8.6 Capacity Mgmt | 5.30 BC Readiness | RECOVERY DEPENDENCY | 3 | Medium | Continuity/failover plans assume capacity that isn't actually available. |
| 5.23 Cloud Security | 8.8 Vuln Mgmt | SUPPORTS | 2 | Medium | Cloud-hosted vulnerabilities go untracked. |
| 5.7 Threat Intelligence | 8.8 Vuln Mgmt | SUPPORTS | 3 | Medium | Patch prioritization ignores real-world exploit activity. |
| 5.7 Threat Intelligence | 8.16 Monitoring | SUPPORTS | 2 | Low | Detection use-cases aren't tuned to current attacker techniques. |
| 8.10 Info Deletion | Cl.6.1 Risk Assess/Treat | SUPPORTS | 2 | Low | Stale/excess data inflates unrecognized exposure. |
| 8.15 Logging | 8.16 Monitoring | ENABLES | 5 | High | Monitoring has no reliable data; detection collapses. |
| 8.16 Monitoring | 5.25 Event Assessment | ENABLES | 5 | High | Raw monitoring output goes untriaged. |
| 8.16 Monitoring | 8.8 Vuln Mgmt | PROVIDES_EVIDENCE | 3 | Medium | Actively-exploited vulnerabilities seen in monitoring don't feed back into patching. |
| 5.25 Event Assessment | 5.26 Incident Response | ENABLES | 4 | High | Response is triggered late or misclassified. |
| 5.24 Incident Planning | 5.26 Incident Response | ENABLES | 5 | High | Response becomes improvised and slower. |
| 8.8 Vuln Mgmt | 5.26 Incident Response | SUPPORTS | 3 | Medium | More incidents stem from known, preventable flaws. |
| 8.13 Backup | 5.30 BC Readiness | RECOVERY DEPENDENCY | 5 | High | Continuity plan can't actually restore operations. |
| 5.26 Incident Response | 5.30 BC Readiness | ENABLES | 3 | Medium | Continuity invocation is delayed or missed. |
| 5.26 Incident Response | 5.27 Incident Learning | ENABLES | 3 | Medium | Post-incident reviews don't happen; root causes recur. |
| 5.30 BC Readiness | 5.29 Disruption Security | ENABLES | 3 | Medium | Security safeguards may be dropped under pressure. |
| 5.29 Disruption Security | 5.26 Incident Response | SUPPORTS | 2 | Low | Responders may deprioritize security mid-incident. |
| 8.2 Privileged Access | 8.16 Monitoring | SUPPORTS | 3 | Medium | Monitoring loses visibility on high-risk accounts. |
