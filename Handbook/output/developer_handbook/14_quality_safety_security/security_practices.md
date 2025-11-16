# Security Practices

This page sets out essential security practices for engineers. The focus areas are threat modelling, certificate and key handling, Software Bill of Materials (SBOM), and vulnerability management. Adhering to these guidelines is mandatory for all projects and systems.

---

## 1. Threat Modelling

### What Is Threat Modelling?

Threat modelling is the structured process of identifying and assessing security threats and vulnerabilities in a system or process. The aim is to understand potential attackers, their objectives, and weak points in the design.

### Why It Matters

- **Proactive Defence:** Identifies vulnerabilities before code is written or deployed.
- **Risk Reduction:** Enables focused mitigation, minimising likelihood and impact of breaches.
- **Requirement Alignment:** Ensures security controls address real-world attack scenarios.

### How To Conduct Threat Modelling

1. **Define Scope:**  
   Determine what is in scope (e.g., application, API, service, infrastructure).

2. **Diagram the System:**  
   Create accurate data flow diagrams highlighting external and internal entities, processes, data stores, and data flows.

3. **Identify Threats:**  
   Use frameworks like STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) to systematically assess each component and interaction.

4. **Evaluate Risks:**  
   For each identified threat, assess likelihood and potential impact. Prioritise high-risk areas.

5. **Specify Mitigations:**  
   Document controls, countermeasures, or design changes necessary to address each risk.

6. **Review and Iterate:**  
   Revisit threat models with every significant architectural or code change.

**Example:** When building an API, consider threats like API key leakage (Information Disclosure), unauthorised access (Spoofing), or tampering with data in transit.

---

## 2. Certificate and Key Handling

### Principles

- **Least Privilege:** Grant minimum permissions necessary for keys and certificates.
- **Secure Storage:** Store secrets encrypted, using managed vault services where feasible (e.g., AWS Secrets Manager, Azure Key Vault).
- **Controlled Access:** Limit access to secrets through audited role-based access control (RBAC).
- **Short Lifespans:** Use short-lived certificates and keys, and rotate them regularly.

### Handling Certificates

- **Generation:** Use strong, well-reviewed tools (e.g., OpenSSL, cfssl). Generate private keys locally; never share via insecure channels.
- **Validation:** Always verify certificate authenticity during use (e.g., TLS, mTLS). Reject self-signed or expired certificates in production unless explicitly justified.
- **Renewal and Revocation:** Automate renewal where possible. Implement certificate revocation checking (e.g., CRL, OCSP) to prevent use of compromised certs.

### Handling Private Keys

- **No Source Code:** Keys must never be hardcoded or committed to version control.
- **Paper Trail:** Track key generation, usage, and retirement in a secure inventory.
- **Ephemeral Use:** For transient workflows (e.g., CI/CD pipelines), avoid persistent storage—fetch keys at runtime and wipe from disk after use.

### Example

For a web service using TLS:

- Generate the certificate signing request (CSR) and private key locally.
- Securely transmit only the CSR for signing.
- Store the resulting certificate and key in a secrets vault accessed by the web server process under a service account.
- Rotate certificates at least quarterly or per the institution’s policy.

---

## 3. Software Bill of Materials (SBOM)

### What Is an SBOM?

An SBOM is a machine-readable, structured inventory of components, libraries, and modules comprising a software system, noting versions and source origins.

### Why It Matters

- **Transparency:** Ensures awareness of all dependencies, direct and transitive.
- **Vulnerability Assessment:** Enables mapping vulnerabilities to specific components in use.
- **License Compliance:** Assist in identification of license risks or obligations.

### Expected Practice

- **Automated Generation:** Generate an SBOM for every built artefact using tools like CycloneDX, SPDX, or native language tooling (e.g., `npm audit`, `pip-licenses`, `mvn dependency:tree`).
- **Artefact Inclusion:** Attach SBOM files to produced artefacts and deployments.
- **Update on Change:** Regenerate SBOM whenever dependencies or build parameters change.
- **Central Registry:** Store SBOMs in a central, queryable location within the organisation for audit and response purposes.

**Example:**  
A team using Python should integrate `cyclonedx-bom` into the build process to produce an up-to-date SBOM upon every release and push it to the organisation’s SBOM registry.

---

## 4. Vulnerability Management

### Principles

- **Early Detection:** Identify vulnerabilities prior to deployment.
- **Continuous Monitoring:** Regularly check for new vulnerabilities affecting live systems.
- **Rapid Remediation:** Address critical vulnerabilities promptly through patching or mitigation.

### Required Activities

1. **Automated Scanning:**
   - Integrate dependency and container scanning (e.g., Snyk, Trivy, Dependabot) into CI pipelines.
   - Scan base images, OS packages, and application dependencies.

2. **Triage and Tracking:**
   - Assess each discovered vulnerability for severity and exploitability in the specific deployment context.
   - Log all identified vulnerabilities in the team’s issue tracker with defined owners and remediation deadlines.

3. **Remediation Policy:**
   - Apply patches for Critical and High severity issues within a defined SLA (e.g., 14 days for Critical, 30 days for High).
   - Document and risk-assess any exceptions. Approved exceptions must have interim mitigations.

4. **Verification:**
   - Re-scan after remediation to confirm fixes.
   - Track closure of all vulnerability tickets; unresolved issues must not block pipeline visibility.

**Example:**  
If Trivy flags an outdated library with a critical issue in a production container image, the engineering team must upgrade the dependency within the SLA, re-image and deploy, and re-scan to confirm resolution.

---

## Summary

Adherence to these practices is essential for the security and resilience of systems. Threat modelling anticipates risks during design; robust certificate and key handling secures cryptographic trust; SBOMs deliver essential component transparency; and continual vulnerability management upholds the operational integrity of assets. All engineers are responsible for integrating these measures into their work from planning through deployment and maintenance.