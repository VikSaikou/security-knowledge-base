# Trust Boundary Analysis

This project models a public digital service used by citizens and employees to process sensitive information.

The same system is examined through multiple architectural and security perspectives. Each diagram adds one layer of analysis while preserving the same trust zones, trust boundaries, components, and identifiers.

## Analysis sequence

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

## Scenario

The organization provides a public digital service used by citizens and employees to process sensitive information.

The service includes:

- a public-facing web application;
- internal and privileged users;
- a sensitive database;
- backup storage;
- audit logging;
- three consistently numbered trust boundaries.

## Core idea

A trust boundary is a point where trust assumptions change.

The diagrams examine:

- where trust changes;
- what crosses each boundary;
- which controls protect it;
- how it may be attacked;
- how protection is verified;
- what happens when it fails;
- how trust is restored.