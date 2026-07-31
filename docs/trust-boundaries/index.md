# Trust Boundary Analysis

> *Understanding security by understanding where trust changes.*

---
Most architecture diagrams describe **what** a system contains.
Trust boundaries explain **where security decisions must be made.**

Whenever data, identities, or privileges cross a trust boundary, the organization must answer questions such as:
- What is trusted?
- What must be verified?
- Which controls are required?
- How is protection demonstrated?
- What happens if the boundary fails?
---

**Trust boundaries** provide a practical way to analyze security architecture because they focus on **where security decisions must be made** rather than where systems are located.

Once the trust boundaries are identified, every other security perspective can be connected to them—business architecture, data flows, authentication, authorization, security controls, attack paths, recovery, evidence, and failure scenarios. This creates a single, consistent view that links business services, security architecture, operational controls, and risk.

The purpose is not to produce a complete technical architecture. The purpose is to demonstrate a repeatable way of thinking:

- begin with the business service and the people who depend on it;
- identify where trust assumptions change;
- examine what data and identities cross each boundary;
- connect risks to security controls;
- identify evidence that demonstrates control effectiveness;
- explore attack paths and business consequences;
- show how trust can be restored after compromise.

This approach helps translate security architecture into questions that can be discussed with technical teams, auditors, risk owners, and management.


## Why trust boundaries?

Trust boundaries provide a practical bridge between business risk and technical architecture.

They help ask questions such as:
- What changes when information crosses this boundary?
- Which assumptions are no longer valid?
- What must be authenticated, authorized, validated, encrypted, or logged?
- Which controls reduce the risk at this specific point?
- What evidence demonstrates that those controls remain effective?
- What becomes exposed if the boundary fails?
- How does the organization restore trust before returning the service to operation?


## Scenario

The organization provides a public digital service used by citizens and employees to process sensitive information.
The service supports daily operations and stores sensitive data. A temporary outage may be technically tolerable, prolonged disruption could significantly affect citizens and organizational operations.

The service includes:
- a public-facing web application;
- internal and privileged users;
- a sensitive database;
- backup storage;
- audit logging;
- three consistently numbered trust boundaries.

The same system is examined through multiple architectural and security perspectives. Each diagram adds one layer of analysis while preserving the same trust zones, trust boundaries, components, and identifiers.

## Project structure

Instead of analyzing security controls individually, every diagram starts with the same question: **where does trust change**? Each view answers a different question while describing the same system.

Every diagram analyzes **the same public digital service**, but from a different perspective:

1. [Business Architecture](business-architecture.md)
2. [Trust Zones](trust-zones.md)
3. [Trust Boundaries](trust-boundaries.md)
4. [Trust Boundary Controls](trust-boundary-controls.md)
5. [Data Flow](data-flow.md)
6. [Authentication Flow](authentication-flow.md)
7. [Authorization Flow](authorization-flow.md)
8. [Attack Paths](attack-paths.md)
9. [Trust Recovery Paths](trust-recovery-paths.md)
10. [Trust Boundary Evidence](trust-boundary-evidence.md)
11. [Trust Boundary Failure](trust-boundary-failure.md)
