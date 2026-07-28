# Authorization Flow

> **Core question:** What is each authenticated user allowed to do?

![Authorization Flow diagram](assets/authorization-flow.svg)

## Purpose

This diagram shows the resources and actions available to each user type after successful authentication.

Authorization determines what an authenticated identity is permitted to do.

## AZ-01 — External user authorization

### Allowed

- Submit data
- View own data
- Update own application

### Restricted

- View other users’ data
- Perform administrative actions

## AZ-02 — Internal user authorization

### Allowed

- View assigned cases
- Update case data
- Process applications

### Restricted

- Access unassigned cases
- Perform system administration

## AZ-03 — Administrator authorization

### Allowed

- Manage system configuration
- Manage access
- Review audit information

### Restricted

- Access business data unless required for an approved task

## This diagram answers

- What is each authenticated user allowed to do?
- Which resources can each user access?
- Which actions are restricted?
- Where is privileged access required?
- Which trust boundaries are crossed during authorized access?
