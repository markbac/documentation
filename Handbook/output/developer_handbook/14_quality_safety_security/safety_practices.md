# Safety Practices

This page details essential safety practices in engineering, emphasising hazard analysis, Failure Modes and Effects Analysis (FMEA), and the preparation of safety cases. These methods are critical for systematically identifying, evaluating, and managing risks throughout the product and process lifecycle.

---

## 1. Hazard Analysis

### 1.1 Purpose and Importance

Hazard analysis is the process of identifying potential sources of harm (hazards) within a system, process, or product. The aim is to recognise risks early, enabling mitigation before they cause injury, environmental harm, or property damage.

**Why it matters:**  
Effective hazard analysis prevents foreseeable accidents, informs design decisions, and is often a regulatory requirement. Without it, hazards may go unrecognised until after an incident occurs.

### 1.2 Key Steps

1. **System Definition:**  
   Clearly delineate system boundaries and operational context. Include intended use, foreseeable misuse, operating environment, and interfaces.

2. **Hazard Identification Techniques:**  
   - *Brainstorming* (with cross-disciplinary teams)
   - *Checklists* (e.g., standard hazards for similar systems)
   - *Task analysis* (evaluate each operation step for risk)
   - *Review of historical data* (past incident/near-miss reports)

3. **Hazard Recording:**  
   Document each identified hazard, its cause(s), potential consequences, and existing control measures.

4. **Preliminary Risk Estimation:**  
   For each hazard, estimate likelihood and potential severity without further risk controls (see 'Risk Assessment' in the Quality, Safety, and Security section).

#### Example

When developing an automated conveyor, hazards may include:
- Entanglement in moving parts
- Emergency stop failure
- Electrical shock from exposed wiring

---

## 2. Failure Modes and Effects Analysis (FMEA)

### 2.1 Overview

FMEA is a structured technique to systematically evaluate how components, subsystems, or processes might fail and the consequences of those failures. It aims to prioritise risks, guiding mitigation efforts to areas of greatest concern.

**Why it matters:**  
FMEA uncovers weaknesses in design or procedure, allowing prevention or minimisation of failures before they have real-world consequences.

### 2.2 FMEA Process

1. **Scope Definition:**  
   Specify whether the analysis covers a product, process, or software component, and define the boundaries.

2. **Item Function List:**  
   Enumerate the functions or requirements for every element analysed.

3. **Identify Failure Modes:**  
   For each function, describe all realistic ways failure could occur (e.g., mechanical breakage, incorrect output).

4. **Effects Analysis:**  
   For every failure mode, list the consequences at the item level, system level, and end-user level.

5. **Cause Identification:**  
   Record potential root causes for each failure mode (e.g., material fatigue, user error).

6. **Current Controls:**  
   Note existing design features or processes that prevent or detect failure.

7. **Risk Evaluation (Scoring):**  
   Assign ratings (typically 1–10) for:
   - Severity (impact if it occurs)
   - Occurrence (likelihood of cause)
   - Detection (likelihood it would be detected before occurrence)
   The *Risk Priority Number* (RPN) is calculated as Severity × Occurrence × Detection.

8. **Prioritisation and Mitigation:**  
   Focus improvement actions on high-RPN items. Actions might include design changes, enhanced testing, or revised procedures.

#### Example Table Entry (simplified)

| Function                | Failure Mode      | Effect                | Cause      | S | O | D | RPN |
|-------------------------|------------------|-----------------------|------------|---|---|---|-----|
| Emergency stop circuit  | Stuck switch     | Cannot stop conveyor  | Contam.    | 9 | 3 | 6 | 162 |

- *S* = Severity, *O* = Occurrence, *D* = Detection, RPN = S×O×D.

---

## 3. Safety Cases

### 3.1 Definition and Rationale

A safety case is a structured argument, supported by evidence, that a system is acceptably safe for a specified application in its operational environment.

**Why it matters:**  
Safety cases give regulators, customers, and internal stakeholders clear justification for risk acceptance. They clarify assumptions, limitations, and give visibility on safety-critical decisions.

### 3.2 Typical Structure

1. **Safety Claim:**  
   Statement of safety intent (e.g., “The automated conveyor is safe for unsupervised operation in a warehouse environment”).

2. **Supporting Arguments:**  
   Narrative and logical reasoning to link evidence to the claim. Arguments may follow a “top-down” (starting from the safety goal) or “bottom-up” (building from detailed evidence) structure.

3. **Evidence:**  
   Documentation that supports the argument, such as:
   - Results from hazard analyses and FMEA
   - Test and inspection data
   - Compliance certificates
   - Operational procedures and training records

4. **Assumptions and Context:**  
   State any assumptions made (e.g., “Power supply will remain within specified limits”) and define the system context.

5. **Residual Risks and Justification:**  
   Explicitly identify any residual risks and rationale for their acceptance (e.g., “Likelihood and severity of electrical shock reduced to level ALARP by interlocks and insulation”).

### 3.3 Maintenance and Review

- Safety cases are living documents. Maintain and review them throughout the project lifecycle, especially when design or operational changes occur.
- Update evidence and arguments to reflect current understanding and practices.

---

## 4. Expectations and Best Practices

- **Integrate safety analysis into all lifecycle stages,** not as a last step.
- **Document clearly:** Record assumptions, decisions, and justifications for traceability.
- **Involve the right stakeholders:** Cross-functional input improves hazard identification and mitigation.
- **Review and update analyses** after incidents or significant changes.
- **Retain records** that demonstrate due diligence for regulatory and legal compliance.

---

## Summary

Hazard analysis, FMEA, and safety cases are essential tools for managing safety risks in engineering. These systematic approaches ensure hazards are identified, risks are prioritised and mitigated, and that safety justifications are robust and maintainable. By applying these practices routinely and rigorously, the team can protect personnel, users, and the business from avoidable harm and liability.