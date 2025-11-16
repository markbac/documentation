# Deployment

Deployment refers to the controlled process of releasing application code and infrastructure to production or staging environments. This page details best practices and procedures for programming deployments, ensuring rollouts are reliable, observable, and reversible.

---

## 1. Environments: Staging and Production

### Staging Environment

- **Purpose**: Mirrors the production environment as closely as possible, enabling comprehensive verification before any public or customer-facing releases.
- **Expectations**: All code destined for production must first be deployed to staging. Tests (automated and manual) must pass on staging before proceeding to production.
- **Data**: Use production-like, anonymised datasets or datasets sufficient to simulate realistic traffic and scenarios.

### Production Environment

- **Purpose**: Hosts live traffic and real end users.
- **Expectation**: Only tested, stable artefacts should reach production.
- **Risk**: Any change here potentially impacts customers. Deployments to production must prioritise predictability and safety.

---

## 2. Deployment Strategies

### Rolling Deployments

- New code versions are incrementally rolled out to subsets of servers or containers.
- **Why**: Reduces risk; if an issue arises, only a segment of traffic is affected.
- **Example**: Deploy to 10% of production servers, monitor, then gradually increase to 100% if stable.

### Blue-Green Deployments

- Two production environments (Blue and Green) are maintained. One serves all traffic (active), while the other is updated.
- After deployment, traffic is switched to the newly updated environment.
- **Why**: Offers instant rollback by reverting traffic if something fails.
- **Considerations**: Requires duplicate infrastructure and careful database synchronisation.

### Canary Releases

- Slowly introduce new versions to a small subset of users or servers.
- **Why**: Allows real-world monitoring and rollback with limited exposure.
- **When to Use**: High-impact releases, new features, or experimental changes.

---

## 3. Deployment Automation

### Infrastructure as Code (IaC)

- Use configuration management tools (e.g., Terraform, Ansible) to provision and manage infrastructure.
- **Why**: Guarantees reproducibility and auditability of environment changes.
- **Practice**: Store IaC definitions in version control.

### Deployment Pipelines

- Automate end-to-end process: code integration, testing, staging deployment, production deployment.
- **Tools**: Commonly Jenkins, GitLab CI, or GitHub Actions.
- **Why**: Reduces manual error, enforces consistency, and provides traceability.

#### Pipeline Stages

1. **Build and Package**: Compile artefacts, create versioned images or files.
2. **Test**: Run automated unit, integration, and end-to-end tests.
3. **Staging Deploy**: Deploy candidate to staging, execute acceptance tests.
4. **Manual Approval** (if required): Human validation or product owner confirmation.
5. **Production Deploy**: Release to production, typically with phased strategy (see above).

---

## 4. Configuration Management

- **Separation of Concerns**: Configuration should be external to the application code, often managed through environment variables or configuration management tools.
- **Security**: Secrets (API keys, passwords) should never be hardcoded. Use secure secret management solutions (e.g., AWS Secrets Manager, Vault).
- **Versioning**: Configurations must be versioned alongside application code.

**Example:**

```sh
# Set environment-specific configuration via environment variables
export API_ENDPOINT=https://api.staging.example.com
export DB_USERNAME=staging_user
```

---

## 5. Observability and Health Checks

### Logging and Monitoring

- Application should provide structured, centralised logs for all deployments.
- Deployments should be automatically monitored for errors, latency, and resource usage.
- **Why**: Early detection of regressions or incidents.

### Health Checks

- Each service must expose health endpoints used by load balancers or orchestrators to confirm readiness.
- **Example**: `/healthz` returns HTTP 200 if healthy.

---

## 6. Safe Rollback Procedures

- Every deployment must have a clear, tested rollback plan. Rollback should be automated where feasible.
- **Common Rollback Techniques:**
  - Redeploy previous artefact
  - Revert traffic (Blue-Green or Canary)
  - Restore from backup

---

## 7. Practical Example: Deploying a Web Service

1. **Developer pushes code** to main branch.
2. **Pipeline triggers** automatically:
   - Builds artefact.
   - Runs tests.
   - Deploys artefact to staging, runs smoke tests.
3. **Automated or manual approval** required for production.
4. **Deployment to production** uses a rolling strategy (e.g., Kubernetes rolling update).
5. **Observability tools** monitor for errors or spikes.
6. **If issues are detected**, deploy is automatically reverted via pipeline rollback job.

---

## 8. Key Expectations

- All production deployments are signed off, traceable, and reversible.
- Deployments must not require manual SSH or direct tampering with servers.
- Rollbacks should be fast and reliable.
- Each team is responsible for verifying and documenting their deployment process in this repository.
  
---

## 9. Checklist for Deployments

- [ ] Code reviewed and merged to main
- [ ] All tests pass
- [ ] Artefact built and tagged with version
- [ ] Staging deployment successful
- [ ] Application health confirmed on staging
- [ ] Observability in place
- [ ] Release notes and rollback procedures prepared
- [ ] Approval for production deploy
- [ ] Production deployment completed and monitored
- [ ] Rollback available and tested

---

## Conclusion

Follow these practices rigorously to achieve predictable, reliable, and observable deployments to both staging and production. Adhering to these guidelines preserves system stability and supports rapid delivery of value to users without compromising quality or security. If uncertainty arises at any step, refer to team leads or this documentation before proceeding.