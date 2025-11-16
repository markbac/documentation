# Design Guidelines

This page documents the fundamental architecture and design guidelines for building robust, maintainable, and efficient systems. Adhering to these practices ensures teams can deliver features efficiently, scale systems predictably, and maintain clarity as the codebase grows.

---

## 1. Architectural Patterns

### 1.1 Use Proven Architectural Patterns

**Guideline:**  
Select architectural patterns that suit your system’s requirements and constraints. Where possible, favour established patterns such as Layered Architecture, Microservices, Event-Driven, or Client-Server.

**Why it matters:**  
Proven patterns reduce the risk of unforeseen design flaws, ease onboarding for new engineers, and provide a shared mental model.

**Example:**  
For a web application expected to scale, microservices may be appropriate, isolating domains such as authentication, payments, and reporting.

**Expectation:**  
Document the chosen pattern and rationale in the architecture decision record (ADR) for traceability.

---

## 2. Layering and Separation of Concerns

### 2.1 Enforce Strict Layering

**Guideline:**  
Organise system components into clear layers (e.g., Presentation, Application, Domain, Infrastructure). Minimise dependencies between layers, permitting downward dependencies only.

**Why it matters:**  
Layering limits the impact of changes, simplifies reasoning, and prevents accidental coupling between distinct concerns.

**Example:**  
A service layer should never reference web controllers directly, but should expose interfaces consumed by the presentation layer.

**Expectation:**  
Maintain clear directory structure and interface segregation reflective of the layers.

### 2.2 Clearly Define Interfaces Between Layers

**Guideline:**  
Define formal interfaces—APIs, abstractions, or contracts—between layers. Avoid “leaking” internal representations (e.g., passing database entity objects to the UI).

**Why it matters:**  
Interfaces decouple implementation, allowing independent evolution and testing of layers.

**Example:**  
Use Data Transfer Objects (DTOs) to pass data between the domain and presentation layers.

---

## 3. Concurrency

### 3.1 Design for Safe Concurrent Execution

**Guideline:**  
Identify code that may run in parallel (threads, processes, async tasks). Ensure re-entrant and thread-safe design in such contexts.

**Why it matters:**  
Concurrency bugs can be subtle, costly, and nondeterministic.

**Example:**  
When sharing mutable state between threads, use synchronisation primitives (locks, atomic variables), or design for immutability where feasible.

**Expectation:**  
Document all assumptions about concurrency in code and design reviews. Explicitly highlight any synchronisation strategies.

### 3.2 Prefer Stateless or Idempotent Operations

**Guideline:**  
Where possible, design operations to be stateless or idempotent, so repeating the same operation produces the same result.

**Why it matters:**  
Idempotent and stateless components simplify retries, scaling, and error handling in concurrent systems.

**Example:**  
A payment service should be able to safely retry a transaction creation call without double-charging.

---

## 4. Resource Constraints

### 4.1 Identify and Manage Bottlenecks Early

**Guideline:**  
Identify likely resource constraints (CPU, memory, I/O, network bandwidth) at design time.

**Why it matters:**  
Designing without regard for constraints can lead to bottlenecks that are expensive to fix post-deployment.

**Example:**  
Limit memory usage by streaming large files instead of loading them entirely into memory.

**Expectation:**  
Include resource constraint considerations in design documentation. If in doubt, prototype and measure.

### 4.2 Degrade Gracefully Under Constraint

**Guideline:**  
Build strategies for resource exhaustion (rate limiting, queue backpressure, circuit breakers).

**Why it matters:**  
Well-designed systems remain stable and useful under stress, rather than failing catastrophically.

**Example:**  
Apply rate limiting to public APIs to prevent a single client from overwhelming the service.

---

## 5. Applying These Guidelines

All projects must:

- Document architectural patterns, layering, and resource assumptions explicitly.
- Justify departures from these guidelines via an ADR, reviewed by the architecture group.
- Include practical code examples and counter-examples in technical design reviews.

**Checklist for Design Artefacts:**
- [ ] Chosen architectural pattern and rationale
- [ ] Layer breakdown and primary interfaces
- [ ] Concurrency and thread-safety considerations
- [ ] Identified resource constraints and mitigation strategies

Following these guidelines fosters resilient, maintainable, and evolvable systems across teams and projects.