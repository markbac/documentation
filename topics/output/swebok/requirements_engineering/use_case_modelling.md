---
title: "Use Case Modelling"
summary: "Modelling system interactions using actors and goals to refine functional requirements."
category: "swebok"
sub_category: "requirements_engineering"
tags:
  
  - "use_cases"
  
  - "uml"
  
  - "requirements"
  
related_topics:
  
  - "Requirements Traceability"
  
  - "Requirements Engineering Fundamentals"
  
depth: "low"
audience: "software_engineers"
doc_type: "introduction"
target_length: "1800"
generated: true
---

# Introduction to Use Case Modelling

Use case modelling is a foundational technique in requirements engineering for capturing, defining, and communicating the intended functional behavior of software systems from the perspective of external users. By focusing on system interactions as perceived by actors (users or other systems) and their goals, use case modelling bridges the communication gap between stakeholders and technical teams, ensuring that software requirements are both complete and unambiguous.

## Technical Context

Use case modelling belongs to the broader family of scenario-based modelling approaches within software engineering. It is a key practice advocated in the Unified Modeling Language (UML) specification and widely referenced in the Software Engineering Body of Knowledge (SWEBOK). Use case models are typically developed during the requirements elicitation and specification phases, but their influence often extends through design, development, and verification.

## Core Concepts of Use Case Modelling

### Actors

In use case modelling, an actor is an external entity that interacts with the system to achieve a specific goal. Actors can be human users, external systems, or hardware components. Crucially, actors are treated as roles, not specific individuals, representing a class of external entities sharing the same interaction pattern.

#### Actor Types

- **Primary actors** initiate interactions to achieve goals.
- **Secondary actors** provide a service or resource the system needs during a use case.

### Use Cases

A use case specifies a sequence of actions performed by the system, leading to an observable result of value to an actor. Use cases encapsulate functional requirements: what the system must do rather than how it does it. Each use case is typically described in terms of:

- **Preconditions:** Conditions that must hold before the use case begins.
- **Main flow:** The nominal sequence of interactions or steps.
- **Alternative flows:** Variations or exceptions to the main flow.
- **Postconditions:** Effects or system states resulting from the use case.

### System Boundary

The system boundary delineates what is inside (the system being developed) and what is outside (the actors and external systems). Being explicit about this boundary prevents scope creep and clarifies interfaces.

### Goals

Each use case is anchored around a goal—an outcome that a particular actor wants to achieve via interaction with the system.

---

## Use Case Diagram Notation

Use case diagrams provide a high-level visual overview of system functionality and external entities. The most common visual conventions follow UML standards.

```mermaid
%% Use Case Model Overview Diagram
%% UML-style use case diagram (simplified for Mermaid)

graph TD
  User[User] --- (Login)
  User --- (View Account)
  User --- (Transfer Funds)
  Manager[Manager] --- (Approve Transfer)
  (Transfer Funds) --- (Validate Balance)
  (Login) -.-> (View Account)
  System[System] -. System Boundary .- (Login)
```

- **Circles/Ovals:** Use cases (system functions)
- **Rectangles:** System boundary (not shown directly in Mermaid, but implied)
- **Stick figure icons or labeled nodes:** Actors
- **Arrows/lines:** Associations between actors and use cases

---

## Describing Use Cases: Templates and Levels of Detail

While diagrams offer an overview, detailed textual descriptions are essential for precise specification. A typical use case description includes:

- **Identifier and Name:** Unique reference
- **Brief Description:** Purpose or goal
- **Primary Actor(s):** Who initiates
- **Stakeholders and Interests:** Broader impact
- **Preconditions:** Required system state
- **Main Success Scenario:** Stepwise flow
- **Extensions/Alternate Flows:** Exceptions, errors
- **Postconditions:** Guarantee(s) on completion
- **Special Requirements:** E.g., usability, performance

#### Example Use Case: "Transfer Funds"

| Element             | Description                                           |
|---------------------|------------------------------------------------------|
| Name                | Transfer Funds                                       |
| Actor               | User                                                 |
| Preconditions       | User is authenticated; source account has funds      |
| Main Flow           | 1. User selects accounts<br>2. System validates<br>3. User enters amount<br>4. System processes transfer |
| Alternate Flow(s)   | Insufficient funds error; invalid account error      |
| Postcondition       | Funds moved; both accounts updated                   |
| Special Requirements| Complete within 2 seconds                            |

---

## Practical Workflow in Use Case Modelling

### 1. Identify Actors

- Engage stakeholders to enumerate all roles interacting with the system.
- Consider interfaces with external hardware, software, or organizational units.

### 2. Identify Goals (Candidate Use Cases)

- Elicit stakeholder goals.
- For each actor, determine what value or result they seek from the system.

### 3. Define Use Cases

- Write main success scenarios.
- Identify and specify alternative flows and error conditions.

### 4. Draw Use Case Diagram

- Visually link actors to the use cases they participate in.
- Group related use cases and clarify system boundary.

### 5. Review and Iterate

- Validate completeness and accuracy with stakeholders.
- Refine based on feedback; ensure coverage of all relevant functional requirements.

---

## Use Case Modelling in Practice

### Integration Points

- **Requirements Traceability:** Use cases can be traced to system requirements, design artifacts, and test cases, facilitating coverage assessment and impact analysis.
- **User Interface Design:** Use cases inform user stories, personas, and navigation flows.
- **Testing:** Each use case can be directly mapped to functional tests or acceptance criteria.

### Assumptions and Constraints

- Use case modelling typically abstracts away from user interface details, data attributes, and implementation specifics.
- Non-functional requirements (performance, security) are less effectively captured directly but may be referenced in special requirements sections of use cases.
- Use cases are not algorithmic specifications; they focus on interactions and observable results.

### Levels of Use Cases

Use cases can be described at varying levels of granularity:

- **Summary level:** Broad business processes or high-level goals.
- **User goal level:** Core interactions meaningful to users.
- **Sub-function level:** Less frequent, supporting or system-internal functions.

## Common Variations and Patterns

### <<include>>, <<extend>>, and Generalization

UML supports three principal relationships among use cases for structuring:

- **Include:** Reuse common behavior, e.g., (Login) included by several use cases needing authentication.
- **Extend:** Optional or conditional behavior, e.g., (Reset Password) extends (Login) only if credentials fail.
- **Generalization:** Use case inheritance, supporting specialization.

```mermaid
%% Relationships between use cases
graph TD
  A[User] --> (Place Order)
  (Place Order) -->|include| (Validate Credit Card)
  (Place Order) -.->|extend| (Apply Discount)
```

### System Actors

Non-human actors, such as external systems, devices, or services, can be involved and should be modelled explicitly.

### Actor Generalization

Actors themselves can be organized in generalization hierarchies if roles overlap.

---

## Engineering Considerations

> [!TIP]
> When identifying actors and use cases, engage a broad range of stakeholders early to avoid omitting critical system interactions.

### Integration and Traceability

- Use cases should be assigned traceable identifiers, ensuring that each requirement, design component, and test case can be linked back to a relevant use case.
- Modern requirements management systems enable such traceability matrices automatically.

### Performance Implications

- Overly granular use cases may lead to excessive documentation and complexity, hampering communication rather than aiding it.
- Conversely, insufficiently detailed use cases may obscure important exceptional flows or business rules.

### Implementation Challenges

- Consistency and completeness: Overlapping or contradictory use cases can introduce ambiguity.
- Evolution: As requirements change, maintaining alignment between diagrams, descriptions, and downstream artifacts is critical.
- Stakeholder understanding: Use cases must be described in a clear, domain-specific language, accessible to both technical and non-technical stakeholders.

> [!CAUTION]
> Use case modelling is most effective for interactive systems with well-defined users. For batch processes, algorithmic processing, or reactive/event-driven systems, alternative or complementary modelling techniques (such as state diagrams or activity diagrams) may be necessary.

---

## Standards and Specification References

- **UML (Unified Modeling Language):** The standard graphical notation for use case diagrams, as described in [OMG UML Specification](https://www.omg.org/spec/UML/).
- **SWEBOK V3.0:** Describes use case modelling as a recommended practice within requirements engineering.
- **IEEE 830-1998:** Suggests including use cases in software requirements specifications (SRS) for clarity and completeness.

---

## Limitations and Common Pitfalls

- **Not Suitable for All Domains:** Event-driven or real-time systems often require additional modelling techniques, as use cases focus on "usage scenarios," not internal event flows.
- **Over-Emphasis on UI:** Focusing use cases too narrowly on UI steps rather than abstract interactions can limit reuse and obscure core system logic.
- **Ambiguity:** Vague actor or goal definitions can lead to incomplete or misaligned requirements.
- **Documentation Overhead:** Excessive detail can slow requirements work without adding proportional value.

> [!WARNING]
> Resist the temptation to directly translate use case diagrams into implementation classes or modules; use cases describe intent and interaction, not software architecture.

---

## Summary

Use case modelling is a powerful, structured technique for capturing and communicating software system functional requirements. By focusing on actors, their goals, and the system's observable behavior, use case modelling offers an accessible, domain-driven means of specifying what a system must do. It forms the conceptual link between stakeholder needs and technical solutions, supporting better design, testing, and traceability throughout the system lifecycle.

While use case modelling is not universally appropriate for every system type, it occupies a central position in requirements engineering, particularly for interactive systems. Understanding its core concepts, practical workflows, and integration with standards such as UML is essential for any software engineer involved in requirements definition and functional specification.