# Feature Flags

Feature flags (also known as feature toggles) are a critical technique in modern software engineering enabling teams to modify system behaviour without deploying new code. Proper use of feature flags supports safer deployments, controlled roll-outs, rapid experimentation, and reduced incident impact.

This page outlines the correct handling of feature flag lifecycles, embedded constraints, and kill-switch policies within our development workflow.

---

## 1. Feature Toggle Lifecycle

A feature flag’s effectiveness depends on disciplined use from creation to removal.

### 1.1. Creation

When adding a feature flag:

- **Define the purpose explicitly:**  
  Document *why* the flag exists (e.g. phased rollout, experiment, ops kill-switch).
- **Select an appropriate flag type:**  
  Common types include:
  - *Release flags*: protect partially-built features.
  - *Experiment flags*: for A/B tests or multi-variant behaviour.
  - *Ops flags*: for emergency enabling/disabling of functionality.
- **Scope flags tightly:**  
  Flags should affect the smallest necessary unit (service/module/function).
- **Name flags consistently:**  
  Use descriptive, namespaced flag keys (e.g. `checkout.enable_new_address_form`).
- **Document default states and expected impact:**  
  Both in code and adjoining design documents.

**Example:**  
```python
if feature_flags.enabled("org.checkout.enable_new_address_form"):
    # New address form logic
else:
    # Existing address form logic
```

### 1.2. Use in Code

- **Minimise code branching:**  
  Avoid excessive nesting or spreading flags throughout the codebase; isolate toggled logic where possible.
- **Centralise evaluation:**  
  Use a shared component/library to evaluate flags, ensuring consistent state across services.
- **Don’t embed business logic in flag evaluations:**  
  Keep flag checks lightweight; avoid introducing side effects.

### 1.3. Monitoring

- **Instrument flag effects:**  
  Where toggles affect user experience or critical operations, ensure observability is in place.  
  Collect metrics for both flag states.
- **Log flag changes:**  
  Auditable logs (who changed what/when) are mandatory for all flag state changes, especially kill-switches.

### 1.4. Removal

- **Remove flags promptly:**  
  Once a feature is fully rolled out and the flag is no longer needed, delete both flag checks and configuration.
- **Clean up tests and documentation:**  
  Remove test cases and technical documentation referring to retired flags.
- **Verify in production:**  
  Confirm the feature remains stable after flag removal.

---

## 2. Embedded Constraints

Feature flags should never become a substitute for sustainable engineering or production safety.

### 2.1. Avoid Flag Creep

Flags intended as temporary must not become permanent. Long-lived flags introduce:

- Increased code complexity and reduced maintainability.
- Risk of inconsistent feature state across environments.
- Higher cognitive load for developers and operations.

**Actions:**
- Set an expiration or review date for all new flags at creation time.
- Track flags using a central registry or metadata file reviewed regularly by the team.

### 2.2. Prevent Configuration Drift

For flags controlling critical paths (e.g. payments, authentication):

- **Synchronise state:**  
  Ensure flag state is in sync across all related services and environments to avoid difficult-to-debug inconsistencies.
- **Restrict direct modification:**  
  Only allow approved personnel to change production flags.
- **Use configuration management:**  
  Manage flag states through versioned, declarative configuration where practical.

### 2.3. Default States

- Default flag values must be explicitly set.
- The default should represent the “safe” or “current” behaviour, not the “untested” or “risky” path.

---

## 3. Kill-Switch (Emergency Disable) Policies

Certain feature flags serve as operational kill-switches to disable functionality immediately in response to incidents or regressions.

### 3.1. When to Use a Kill-Switch

Use a dedicated kill-switch flag for any non-essential or novel functionality where rapid disablement may be required (e.g. new external integration, experimental compute-intensive process).

### 3.2. Implementation

- **No-caching for critical flags:**  
  Evaluate kill-switches in real time; never cache their values in client or service logic.
- **Immediate effect:**  
  The flag system must propagate changes with minimal delay (sub-minute), including graceful fallback where relevant.
- **Safe fallback:**  
  Always verify that disabling the flagged feature will restore a known stable state.
- **Alerting:**  
  Trigger monitoring alerts when a kill-switch is activated, notifying both engineering and operational staff.

### 3.3. Audit and Accountability

- All kill-switch activations must be traceable to an individual operator.
- Justification for activation must be recorded, with references to related incidents.

---

## 4. Summary of Best Practices

- Every flag must have a documented purpose, owner, type, and expiry/review timeline.
- Minimise long-lived or permanent flags. Routinely review and remove stale flags.
- For kill-switches, prioritise speed, safety, observability, and auditability.
- Avoid embedding flags as a substitute for high-quality code or robust release processes.

---

*For any questions about feature flag usage or kill-switch policy, contact the DevOps lead or consult with the Platform Reliability team.*