# Developer Testing and Verification (T&V) in Developer Test Lanes

## Overview

This page outlines the procedures and rationale for developers conducting Testing and Verification (T&V) using developer test lanes. It covers the purpose of these tests, when to use them, how to execute them effectively, and expectations for reporting and follow-up. The aim is to ensure robust code quality, accelerate identification of defects, and uphold the integrity of the main codebase throughout the development cycle.

---

## Purpose of Developer-run T&V

During active development, developers are responsible for continuously verifying their code changes before integration. Developer T&V tests—executed in isolated developer test lanes—provide rapid feedback on new features, bug fixes, and regressions without affecting shared or production environments.

**Key reasons for developer-run T&V:**

- **Early Defect Detection**: Catching issues before code reaches shared branches greatly reduces downstream integration problems.
- **Regression Prevention**: Automated regression tests confirm new changes do not break existing functionalities.
- **Isolated Testing Environment**: Developer lanes provide a safe space to test significant changes or experiments without disrupting other team activities.
- **Efficient Bug Fix Validation**: Developers can quickly verify that reported or discovered bugs are indeed fixed as intended.

---

## Types of T&V Tests to Run

- **Unit Tests**: Validate that individual functions or methods behave correctly in isolation.
- **Integration Tests**: Confirm that components work together as expected, focusing on boundaries and interactions.
- **Regression Test Suites**: Run a predefined set of tests designed to catch re-occurrences of past defects.
- **Feature-specific Tests**: For new or changed functionality, design focused tests to prove requirements are met.
- **Bug Reproduction and Fix Verification**: Reproduce reported issues, apply fixes, and rerun corresponding tests to ensure resolution.

**Example:**  
A recent update to the authentication logic should trigger unit tests for password validation, integration tests with the session management module, and relevant regression tests for login and logout flows.

---

## When to Use Developer Test Lanes

Developer test lanes should be engaged:

- Before submitting code for code review or merge requests.
- After implementing a bug fix, to verify the issue is resolved and no collateral issues are introduced.
- When adding or updating features, especially those impacting critical or heavily used paths.
- To reproduce and diagnose issues reported by users or CI/CD pipelines.

> **Note:** Shared test lanes or central CI environments are not substitutes for developer lanes at this stage as they are resource-constrained and reserved for validated changes.

---

## Setting Up and Running Tests

1. **Obtain or Create a Developer Lane**  
   Set up a dedicated environment reflecting production or target integration environments as closely as possible (tooling and configuration are outlined in the [Environment Setup Guide]).

2. **Check Out a Feature or Bug-fix Branch**  
   Work in a branch isolated from the main or release branches.

3. **Update Dependencies**  
   Ensure all necessary dependencies and data are consistent with target versions.

4. **Run the Relevant Suite(s) of Tests**  
   Use the automated scripts or tools provided by the team (for example, `pytest`, `npm test`, or bespoke frameworks).  
   Example (command line):  
   ```
   ./run-dev-lane-tests.sh --suite=regression
   ```

5. **Interpret and Address Failures**  
   Examine failures thoroughly. Where possible, debug and resolve the root cause immediately.  
   - If a test exposes a previously unknown issue, investigate prior to merging.
   - If failures are not reproducible, log the attempt and consult with testing leads or peers.

6. **Re-run Key Tests After Fixes**  
   After addressing defects, repeat the relevant tests to ensure resolution.

---

## Expectations and Follow-Up Actions

- **No Known Failures on Relevant Tests prior to Merge:** All regression, unit, and feature-related tests must pass before code integration unless a documented and justified exception is approved by the T&V lead.
- **Documenting Test Results:** Record the results of critical test runs in the merge request or issue tracker, noting:
   - Test lane used
   - Suite(s) executed
   - Results and resolutions of failures
   - Any deviations from normal processes
- **Raising Blockers or Flaky Tests:**  
   If tests are consistently unreliable (“flaky”) or blocked by unrelated infrastructure issues, escalate promptly with detailed steps to reproduce.

---

## Example Workflow

1. Developer implements feature `X` in branch `feature/X`.
2. Spawns a developer test lane mirroring the staging environment.
3. Runs:
   - All unit tests (`npm run test:unit`)
   - The regression suite (`./run-dev-lane-tests.sh --suite=regression`)
   - Custom tests for any new endpoints.
4. Finds a regression failure relating to login. Investigates, identifies an unintended side effect, and patches the logic.
5. Repeats the regression suite—now all tests pass.
6. Records the outcome and commands run in the merge request comments.
7. Proceeds to code review.

---

## Rationale

Proactive, developer-run T&V in isolated test lanes shifts defect discovery earlier in the development cycle. This minimises integration friction, reduces the cost of fixing defects, and bolsters product stability. Following the practice outlined above ensures that only high-quality code progresses, benefitting both individual contributors and the wider team.

---

## Further Reading

- [Environment Setup Guide]
- [Test Suite Reference]
- [Continuous Integration Process Overview]

*(Replace bracketed links with actual wiki references as required.)*