# Industry Alignment

## Overview

Industry alignment refers to the deliberate process of mapping internal engineering practices, requirements, and outputs to established external standards. This ensures that our designs, documentation, and products are not only consistent and interoperable, but also recognised, trusted, and transferable within our professional domain.

Aligning to industry standards is not optional: it is a core aspect of modern engineering. Regulatory compliance, customer requirements, interoperability, and long-term maintainability all depend upon it.

This page explains how to identify, map to, and document alignment to external standards in all applicable engineering work.

---

## Why Industry Alignment Matters

### Regulatory Compliance

Many industries are subject to formal regulations (e.g., ISO, IEC, IEEE standards). Misalignment may result in legal repercussions, certification failure, or barriers to market access.

### Interoperability

Standard alignment enables our systems and products to work seamlessly with third-party solutions, easing integration, upgrades, or migrations within ecosystems.

### Quality Assurance

External standards codify best practices. Mapping to them ensures our deliverables are robust, maintainable, and subject to external audit if necessary.

### Longevity and Maintainability

Aligning to well-established standards reduces technical debt and minimises bespoke approaches that hinder future support or expansion.

---

## How to Map to External Standards

### 1. Identifying Applicable Standards

Begin each project by determining which external standards are relevant. Consider:

- **Domain standards:** (e.g., ISO 9001 for quality management, IEC 61508 for functional safety)
- **Interface or protocol standards:** (e.g., REST, OPC UA)
- **Data and documentation standards:** (e.g., ISO/IEC/IEEE 15288 for systems engineering)
- **Regulatory requirements:** as imposed by authorities or sectors (e.g., CE, UKCA, FDA)

**Example:**  
For an embedded device in a safety-critical environment, IEC 61508 and ISO 26262 may both apply.

#### Action  
- Keep an up-to-date register of standards per domain or project within your documentation repository.
- Consult with your team’s compliance lead or standards officer to confirm selections.

---

### 2. Mapping Internal Artefacts to Standards

For each standard, identify the specific requirements or clauses that apply. Explicitly document how each internal artefact (design document, process, test case, etc.) satisfies these clauses.

#### Mapping Table Example

| Standard Reference      | Requirement Description       | Internal Artefact            | Evidence/Notes     |
|------------------------ |------------------------------|------------------------------|--------------------|
| ISO 9001:2015 8.5.1     | Control of production        | Manufacturing Work Instr.     | WI-1234, Rev B     |
| IEC 61508-3:7.4.4.1     | Software module testing      | Unit Test Specification      | UTS-002, Jenkins   |

**Tip:** Maintain mapping tables in your main design specification or compliance report.

---

### 3. Documenting and Reviewing Alignment

All mapping activities must be auditable and maintained alongside project documentation. This allows for:

- Internal peer reviews
- External audits or certification efforts
- Demonstrable traceability in case of dispute or problem

**Required Documentation:**
- Index of relevant standards per project
- Mapping tables (as above)
- References to test evidence or artefacts
- Deviations with rationale and approvals

---

### 4. Managing Deviations and Exceptions

Occasionally, a standard may not be fully applicable or suitable for a specific context. In these scenarios:

- Document each deviation with clear justification.
- Obtain formal approval from the appropriate authority (e.g., design authority, compliance lead).
- Record any mitigations or compensations put in place.

**Example:**  
A legacy module does not meet the latest secure communications protocol (per ISO/IEC 27001). The exception is documented, risk-assessed, and a migration plan is recorded.

---

### 5. Maintaining Alignment

External standards evolve. To ensure ongoing compliance:

- Review and update mappings whenever standards are revised.
- Embed periodic standards review checkpoints into project lifecycles.
- Assign clear owners (usually a standards coordinator or compliance lead) to monitor for changes.

---

## Practical Example: Mapping a REST API to Industry Standards

**Scenario:** Developing an internal REST API to be used by external partners.

**Relevant Standards Identified:**  
- OpenAPI Specification (OAS) for interface documentation  
- ISO/IEC 27001 for security controls

**Process:**  
1. Rigorously document all endpoints using the latest OAS version.  
2. Map all security-related requirements from ISO/IEC 27001 to API authentication, transport encryption (TLS), and audit logging.  
3. Complete a mapping table noting which internal policies and technical controls align to each referenced standard clause.

---

## Expectations for Engineers

- Proactively identify relevant standards for each new activity.
- Map all significant outputs to specific standard requirements, maintaining up-to-date traceability.
- Document any exceptions, including rationale and authorising signatures.
- Ensure all mapping documentation is complete, current, reviewed, and accessible to all project stakeholders.

---

## Summary

Industry alignment is an essential discipline in engineering practice. It safeguards quality, enables interoperability, and ensures compliance. By systematically identifying, mapping, and maintaining our alignment with external standards, we improve the credibility, safety, and longevity of our engineering work.

For further guidance, refer to the [Standards Register Appendix](/appendices/standards-register) or contact the compliance office.