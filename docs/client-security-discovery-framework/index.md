# Client Security Discovery Framework

## Overview

<div class="grid cards" markdown>

-   **From ambiguity to actionable requirements**

---

    A reusable framework for converting ambiguous cybersecurity client requests into validated requirements, risks, ownership decisions, and measurable implementation outcomes.

</div>

Security projects often begin with an incomplete request:

> “We need a VPN.”
> “The auditor requires MFA.”
> “Remote access is no longer working well.”
> “We need a more secure solution.”

These statements describe a visible symptom, but they do not always reveal the underlying business need, operational constraint, security risk, or expected outcome.

The **Client Security Discovery Framework** is a reusable method for converting ambiguous client concerns into structured and verifiable information.

It helps identify:

* the business reason behind the request;
* the current process and its weaknesses;
* technical, operational, and human constraints;
* security risks and unverified assumptions;
* ownership and decision-making responsibilities;
* measurable success and validation criteria.

## Purpose

The purpose of this framework is not to recommend a product immediately.

Its purpose is to ensure that a proposed security solution addresses the actual problem and can realistically be implemented, maintained, and accepted by the organisation.

The framework supports conversations with business owners, IT teams, security specialists, system administrators, and other stakeholders.

## How to Use This Framework

The documents are arranged in the order a typical security discovery process would follow.

The process begins with the **Discovery Question Bank**, which helps gather information from the client. The findings are recorded in the **Discovery Notes Template** and then reviewed using **Signal Classification** to separate facts, symptoms, assumptions, hidden needs, risks, and requirements.

Confirmed needs are transferred to the **Requirements Register**, while uncertainty and potential negative outcomes are tracked in the **Risk and Assumption Log**.

The **AustraKey Remote Access Example** demonstrates how all parts of the framework can be applied together to an ambiguous client request.

## Discovery Process

The framework follows a structured workflow that converts an initial client request into validated requirements, risks, and expected outcomes.

<a href="assets/client_security_discovery_process.svg"
   target="_blank"
   rel="noopener noreferrer">
  Open the full-size discovery process diagram in a new tab
</a>

<a href="assets/client_security_discovery_process.svg"
   target="_blank"
   rel="noopener noreferrer">
  <img src="assets/client_security_discovery_process.svg"
       alt="Client Security Discovery Framework process"
       style="width: 100%; height: auto;">
</a>

During discovery, client statements are classified as:

* explicit requirements;
* symptoms;
* hidden needs;
* assumptions;
* constraints;
* risks;
* workarounds;
* success criteria.

This separation helps prevent assumptions from being treated as confirmed facts.

## Framework Outputs

A completed discovery process should produce at least four practical outputs:

1. a summary of the client’s current situation;
2. a list of validated requirements and constraints;
3. a risk and assumption register;
4. agreed implementation and validation criteria.

These outputs create a traceable link between the original client concern and the final technical recommendation.

## Example Scenario

The framework is demonstrated using **AustraKey**, a fictional 50-person fintech company preparing to improve secure remote access for employees working across several countries.

The example will show how an initial request for a “better VPN” can be translated into broader requirements concerning identity, MFA, managed devices, access ownership, logging, support, and residual risk.

## Project Status

This repository currently contains the initial version of the framework and its document structure.

The content will be expanded with:

* a detailed discovery question bank;
* reusable discovery templates;
* a requirements register;
* a risk and assumption log;
* a completed AustraKey example.