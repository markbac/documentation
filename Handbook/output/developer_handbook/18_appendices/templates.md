# Templates

This section provides references and guidance for reusable templates used throughout engineering projects. Consistent use of standard templates ensures clarity, efficiency, and a common understanding across the team. Templates are provided for common artefacts such as design documents, code reviews, incident reports, and more. Each template has a defined purpose and scope—ensure you select the correct template for your task.

---

## Why Use Templates?

Templates establish a structured, uniform approach to documentation. Their use provides several clear benefits:

- **Consistency:** Information is presented in a predictable layout, making documents easier to write, review, and understand.
- **Efficiency:** Starting with pre-defined sections eliminates ambiguity over what to include and reduces duplicated effort.
- **Quality:** Templates prompt contributors to address critical considerations, reducing omissions and improving the calibre of documentation.
- **Onboarding:** New team members can quickly adopt project standards and conventions, accelerating their effectiveness.

## How to Use Templates

1. **Select the Appropriate Template**
   - Review the purpose and guidance for each template below and choose the one that best fits your current need.
2. **Copy the Template**
   - Access the template from its repository or linked location. Do **not** write directly in the master document.
3. **Fill in Each Section Fully**
   - Complete all relevant fields. If a section does not apply, state "Not applicable" and briefly explain why.
4. **Maintain Clarity and Brevity**
   - Use clear, concise language. Write so that another engineer, unfamiliar with your context, could follow your logic and conclusions.
5. **Review Before Circulation**
   - Ensure all required information is present and that the completed document meets our documentation standards.

## Template Index

Below is a list of available templates, their intended use, and direct links to the current versions.

| Template Name                  | Description                                              | Link                                    |
|------------------------------- |---------------------------------------------------------|-----------------------------------------|
| Design Document                | For proposing, describing, and reviewing new designs.   | [Design Document Template](../templates/design-doc.md)   |
| Architecture Decision Record   | To log architectural choices and their context.          | [ADR Template](../templates/adr.md)                   |
| Code Review Checklist          | Checklist for reviewers to ensure code quality.          | [Code Review Checklist](../templates/code-review.md)    |
| Incident Report                | Post-mortem analysis for production incidents.           | [Incident Report Template](../templates/incident.md)    |
| Test Plan                      | Defines approach, scope, and cases for testing features. | [Test Plan Template](../templates/test-plan.md)         |
| Meeting Notes                  | For consistent capture of meeting discussions/actions.   | [Meeting Notes Template](../templates/meeting-notes.md) |
| Release Checklist              | Ensures all steps are complete before production release.| [Release Checklist](../templates/release.md)            |

**Note:** For the latest updates and additions, refer to the [Templates Directory](../templates/).

## Practical Example: Using the Design Document Template

**Scenario:** A team member proposes a new microservice to handle user notifications.

**Application:**

1. **Locate the template:** Go to [Design Document Template](../templates/design-doc.md).
2. **Copy the template to a new document:** Name it to match your project's naming convention.
3. **Complete each section:**  
   - **Overview:** Write a concise summary of the service and its goals.
   - **Background:** Explain why this service is needed (e.g. performance bottleneck in the current system).
   - **Proposed Solution:** Detail your architectural approach, components, and data flow.
   - **Alternatives Considered:** Briefly describe alternative designs and rationale for not choosing them.
   - **Impact Assessment:** Address risks, dependencies, and operational concerns.
   - **Open Questions:** List unresolved issues or areas needing input.
4. **Circulate for review:** Share the filled-in document via the designated channel for feedback.

**Outcome:** All stakeholders can quickly understand and assess the proposed service, enabling informed decision-making and efficient iteration.

## Expectations and Best Practices

- **Adhere to the template structure:** Only modify or omit sections with clear justification.
- **Seek feedback:** Consult with your lead or peers if uncertain about how to complete a section.
- **Flag deviations:** Where a project diverges from template norms, explicitly document and explain deviations.
- **Contribute improvements:** If a template does not serve its purpose well, propose enhancements via a pull request.

## Frequently Asked Questions

**Q: What if my documentation does not fit any existing template?**  
A: Use the [General Documentation Template](../templates/general-doc.md) as a starting point, or consult your lead to discuss creating a new template.

**Q: Should templates be updated?**  
A: Absolutely. Templates are living documents and should evolve as best practices and requirements change. Suggest improvements with clear justification.

---

For template requests or questions, contact the [Documentation Maintainers](mailto:team-docs@example.com). Always use the most recent template version to ensure alignment with current standards.