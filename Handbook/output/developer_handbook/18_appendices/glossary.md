# Glossary

This glossary defines technical terms, abbreviations, and common language used throughout our engineering documentation. It is designed as a reference for all team members and stakeholders to ensure clear, consistent communication. Precise terminology reduces ambiguity, streamlines onboarding, aids collaboration across teams, and aligns expectations. When in doubt, refer to this glossary or suggest amendments to minimise misunderstandings.

## How to Use This Glossary

- **First reference:** Bold the term and link to this page.
- **Introduce new terms sparingly.** Align with existing definitions whenever possible.
- **Disagree with a definition or need a new term?** Propose updates through the handbook change process, justifying the addition or amendment.

---

## Terms and Abbreviations

### API (Application Programming Interface)

A formal, documented set of rules and definitions allowing two software components to communicate. APIs abstract underlying implementation, offering defined ways to interact with functionality such as data retrieval or command execution.

**Practical example:** 
A weather service exposes an HTTP API. External applications access forecast data by making requests to specified endpoints such as `/forecasts?postcode=SW1A1AA`.

**Why it matters:** 
APIs support integration between systems, enforce security boundaries, and encourage reusability. A clear API contract reduces integration errors.

---

### Availability

The proportion of time a system, component, or service is operational and accessible as required. Typically expressed as a percentage over a given timeframe (e.g., "99.95% monthly availability").

**Practical example:** 
If a web application guarantees 99.95% availability per month, it must not be unavailable for more than ~22 minutes in any calendar month.

**Why it matters:** 
Operational availability impacts user trust, service-level agreements (SLAs), and incident response priorities.

---

### CI/CD (Continuous Integration / Continuous Deployment)

A set of development practices and automation techniques enabling code changes to be reliably built, tested, and delivered to production in small, frequent increments.

- **Continuous Integration (CI):** Automated building and testing of new code when changes are committed.
- **Continuous Deployment (CD):** Automatic release of validated code to production.

**Why it matters:** 
Reduces integration issues, accelerates delivery, and enables rapid feedback for engineering teams.

---

### Container

A lightweight, portable unit bundling application code with its dependencies and configuration, isolated from the underlying environment. Containers are typically managed by an orchestration system (e.g., Kubernetes).

**Practical example:** 
A Python web service and its required libraries are packaged into a Docker container. It can be reliably started on any compatible host, regardless of host-level differences.

**Why it matters:** 
Facilitates reproducible deployments, simplifies scaling, and limits fault isolation risks.

---

### Dependency

Any library, external service, or resource upon which a component relies to function correctly.

**Practical example:** 
A Node.js application’s dependencies are defined in its `package.json` file and installed via `npm install`.

**Why it matters:** 
Managing dependencies carefully is crucial to maintain stability, security, and upgradeability.

---

### Idempotent

A property of an operation such that performing it multiple times has the same effect as performing it once.

**Practical example:** 
Deleting a resource using a `DELETE` HTTP method is idempotent: re-issuing the request either removes the resource or, if it no longer exists, leaves the system unchanged.

**Why it matters:** 
Idempotency is critical for reliable systems, especially in distributed or retry-heavy environments.

---

### Incident

Any event that disrupts, or has the potential to disrupt, normal operation of a system or service.

**Why it matters:** 
Incidents are logged, triaged, and investigated to resolve issues and prevent recurrence. A shared understanding of ‘incident’ triggers effective response protocols.

---

### Latency

The time taken for a data packet, operation, or request to travel from source to destination (or to deliver a response).

**Practical example:** 
A request to the database returns in 120 milliseconds—this is the query’s latency.

**Why it matters:** 
High latency impacts performance and user experience; monitoring and optimisation are core reliability concerns.

---

### Microservice

A small, independently deployable component of a system, focusing on a single business capability and communicating with other services via APIs.

**Practical example:** 
A payment processing service operates independently of a user authentication service in an e-commerce system.

**Why it matters:** 
Microservices enable flexible scaling, isolated fault domains, and technology diversity, at the cost of greater operational complexity.

---

### Regression

A defect or performance decline introduced by a change that was previously working as expected.

**Why it matters:** 
Regression tests are employed to catch such issues before deployment. Detecting regressions early prevents outages and customer impact.

---

### Rollback

Reverting a deployment, configuration, or database to a previous, known-good state.

**Why it matters:** 
Rollbacks are crucial for mitigating incidents resulting from faulty changes. Successful rollbacks depend on robust deployment and data versioning strategies.

---

### SLA (Service Level Agreement)

A documented commitment regarding service quality metrics, such as availability, performance, or support response times, between the provider and user.

**Why it matters:** 
SLAs guide prioritisation of engineering work and ensure accountability.

---

### SLO (Service Level Objective)

A specific, measurable reliability or performance target for a system, typically forming part of an SLA.

**Practical example:** 
“99.99% of login requests must complete in under 1 second over any rolling 30-day period.”

**Why it matters:** 
SLOs drive engineering priorities and operational measurement. They support data-driven decisions about risk and investment.

---

## Best Practices

- Use glossary definitions verbatim in documentation and discussions to enforce shared understanding.
- Regularly review and refine definitions to reflect evolving practices and technology.
- If a term is not listed, avoid defining it ad hoc; request an addition via the handbook amendment process.
- Link terms in new documents to this page, especially on first usage.

---

## Contribution

To suggest additions, amendments, or clarifications, file a handbook amendment with:
- The proposed term and definition.
- Rationale for inclusion or revision.
- Practical examples demonstrating usage.

All proposals are reviewed for clarity, applicability, and alignment with team conventions. This keeps our shared vocabulary current and effective.