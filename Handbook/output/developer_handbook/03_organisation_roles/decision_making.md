# Decision Making

Effective decision making is critical to the success of engineering projects and the smooth operation of teams. This document outlines the governance structure underpinning decision making, specifies approval processes, and describes how to ensure decisions are well-informed and robust. Adhering to these guidelines ensures that decisions are made transparently, with the right stakeholders involved, and to a consistently high standard.

## Governance Structure

### Defined Roles and Responsibilities

Decision making relies on clarity of roles. Each key role in the organisation has decision rights appropriate to its remit:

- **Engineers**: Make technical decisions within the boundaries defined by architectural guidelines and project requirements.
- **Technical Leads**: Oversee technical direction, resolve cross-team dependencies, and escalate significant technical choices.
- **Engineering Managers**: Approve resource allocation, delivery timelines, and major process changes.
- **Architects**: Set overall technical strategy and enforce adherence to architectural standards.
- **Product Owners/Managers**: Decide on product direction, feature priority, and release scope.
- **Executive/Steering Committees**: Approve strategy-level changes, budget adjustments, and high-risk or high-impact decisions.

**Why this matters:** Clear assignment prevents confusion, accelerates progress, and avoids duplicated or conflicting decisions.

### Decision Tiers

Decisions are categorised based on their impact:

1. **Operational Decisions**: Low-risk, routine, and reversible (e.g., code formatting, minor refactoring). Taken by the primary engineer or immediate team.
2. **Tactical Decisions**: Affect team plans, require cross-discipline input, or involve moderate risk (e.g., API design changes, tool selection). Require consultation and approval from Technical Lead or Manager.
3. **Strategic Decisions**: Affect multiple teams, the architecture, or the organisation’s trajectory (e.g., migration to a new technology, architectural overhaul). Require consensus from senior engineering leadership, architects, and product owners.

**Example:** A decision to update a logging library is operational; replacing a logging strategy across all products is strategic.

## Approval Processes

### Decision Records

For tactical and strategic decisions, a Decision Record (DR) must be completed. A DR includes:

- **Context and problem statement**
- **Options considered**
- **Stakeholder input**
- **Chosen solution and rationale**
- **Approval signatures or evidence (e.g., meeting minutes, digital sign-off)**
- **Impact assessment and rollback plan**

All DRs must be accessible in the team’s knowledge base.

**Why this matters:** Rigorous documentation ensures accountability, makes past decisions auditable, and allows new team members to understand historical context.

### Review and Escalation

- **Operational**: No formal review required; peer discussion recommended for learning.
- **Tactical**: Reviewed and approved by the Technical Lead or Engineering Manager.
- **Strategic**: Formal review by cross-functional group appropriate to the scope (e.g., architecture review board, steering committee).

Escalation should occur if:

- The decision scope expands (affecting more teams or budgets).
- There is significant uncertainty or disagreement.
- Risks exceed accepted thresholds.

### Consensus and Disagreement

Where possible, decisions should be made by consensus. If consensus cannot be reached within a reasonable timeframe:

- The designated decision maker for the tier in question is empowered to decide.
- Dissent must be recorded in the DR, with the reasoning explained.
- Mechanisms for appeal or revisit (if new information emerges) must be specified.

## Ensuring Decision Quality

### Stakeholder Involvement

Decisions must involve all relevant stakeholders early. This includes engineers affected by the change, security and compliance representatives for significant technical decisions, and product owners for user-facing impacts.

**Example:** When redesigning an authentication system, include engineers, security officers, and product owners to capture technical, compliance, and user experience considerations.

### Evidence-Driven Choices

All decisions, especially at the tactical and strategic tiers, must be based on:

- Quantitative data (e.g., benchmarks, incident reports)
- Qualitative insights (e.g., user feedback, expert opinion)
- Feasibility assessments (proof of concept, pilots)

Decisions made without adequate evidence risk subpar outcomes and technical debt.

### Impact Assessment and Risk Management

Every significant decision requires an impact assessment covering:

- Affected systems, teams, and processes
- Risks and mitigations
- Benefits and trade-offs
- Rollback or contingency plans

This process ensures anticipated and unanticipated consequences are managed effectively.

## Summary

- **Decision making is tiered** by impact and risk, with clear role-based responsibilities.
- **Formal records and review** are required for tactical and strategic choices.
- **Stakeholder input, evidence, and impact analysis** underpin decision quality.
- **Escalation and documentation** maintain transparency and auditability.
- These practices exist to safeguard quality, consistency, and accountability, enabling teams to make confident, well-informed decisions that align with organisational goals.