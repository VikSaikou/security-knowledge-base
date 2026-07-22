# Workflow 001 — Access Request Approval

This page describes the minimum workflow for requesting, approving, implementing, and validating user access. It is intended to ensure that access is not created without a recorded request, approval, implementation note, and validation evidence.

## Workflow Overview

```text
Microsoft Forms
    ↓
Microsoft Lists item is created
    ↓
Power Automate starts the approval
    ↓
If approved, an IT task or ticket is created
    ↓
IT implements access in Microsoft Entra ID
    ↓
IT adds an implementation note
    ↓
A validation note is added
    ↓
A SharePoint Wiki or runbook link is attached
```

## Minimum Implementation

1. A manager submits the access request through Microsoft Forms.
2. The response is automatically recorded in Microsoft Lists.
3. Power Automate sends the request to the direct manager or system owner for approval.
4. When approved, the record is marked as **Ready for IT**.
5. IT creates the user in Microsoft Entra ID.
6. IT records the status as **Implemented** and **Validated**.
7. The record retains the request, approval, implementation, and validation history as evidence.

## Approval Options

SharePoint Lists and document libraries also support approval workflows. An item or document can be submitted directly to designated approvers for approval.

## Case Portfolio

| Case | Status | Simple Control | Tools | Evidence |
|---|---:|---|---|---|
| Case 001 — Access Before Day One | In progress | Structured access request before account creation | Forms · Entra ID · Lists | Request, approval, implementation note |
| Case 002 — No Access Without Review Date | Planned | Required review date for temporary access | Forms · Lists · Power Automate | Approval, expiry or review field |
| Case 003 — Group Access Instead of User Access | Planned | Access assigned through groups | Entra ID · SharePoint | Group membership, validation note |
| Case 004 — Ticket Cannot Close Without Validation | Planned | Closure requires an evidence note | Lists · Wiki · Service Desk template | Validation, handoff note |
