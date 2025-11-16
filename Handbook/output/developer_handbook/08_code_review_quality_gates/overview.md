# Overview: Code Review and Quality Gates

This page outlines the key processes and metrics involved in code review and the use of quality gates. It covers quality metrics, static analysis, code coverage, and compliance with MISRA standards. This guidance is intended to ensure software robustness, maintainability, and conformity to industry requirements.

---

## Purpose and Value of Code Review and Quality Gates

Code reviews and well-defined quality gates are essential for:

- **Early Detection of Defects:** Identifying logic errors, bugs, and vulnerabilities before code reaches production.
- **Enforcing Coding Standards:** Promoting consistency, readability, and maintainability across the codebase.
- **Knowledge Sharing:** Facilitating team learning and onboarding by discussing design decisions and implementation details.
- **Regulatory Compliance:** Ensuring the code meets relevant safety and industry standards such as MISRA.

Without such controls, defects propagate unchecked, technical debt accumulates, and compliance risks increase, jeopardising software quality and project timelines.

---

## Core Quality Metrics

Quality gates enforce thresholds for specific, measurable criteria each change must satisfy before integration. Common metrics include:

- **Build Success:** Code compiles without errors or warnings (warnings must not be ignored).
- **Automated Test Outcomes:** All unit, integration, and system tests must pass.
- **Code Coverage:** A measured proportion of the codebase exercised by automated tests (see below).
- **Static Analysis:** Automated checks for coding errors, standard violations, and potential defects.
- **Code Review Approval:** At least one, ideally two, qualified engineers must approve each change.
- **Defect Density:** The number of issues found per lines of code (monitored over time, not as an immediate gate).

These metrics are both *quantitative* (e.g., code coverage percentage) and *qualitative* (e.g., reviewer assessment of code clarity).

---

## Static Analysis

Static analysis examines source code for errors and violations without executing the program. It serves to:

- **Detect Defects:** Identifies common issues such as null dereferences, unreachable code, resource leaks, concurrency flaws, and security vulnerabilities.
- **Enforce Standards:** Checks conformance to coding standards, including style guides and rules such as those defined by MISRA.

**Tooling and Integration:**
- Static analysis must be automated in the Continuous Integration (CI) environment.
- Typical tools: *Cppcheck*, *Clang-Tidy*, *PC-lint*, *Coverity* (for C/C++), configured with the project’s chosen ruleset.

**Example:**  
If a static analyser reports a potential division by zero, that defect must be either corrected or explicitly justified (with a suppressing comment and reviewer sign-off).

**Action on Findings:**
- New code **must not** introduce new static analysis warnings or errors.
- Legacy issues may be documented, but not ignored; create tickets for remediation.

---

## Code Coverage

**Definition:**  
Code coverage measures the percentage of source code exercised by automated tests (unit, integration).

**Rationale:**  
Higher coverage provides stronger evidence that the most critical paths, edge cases, and error handling have been tested, reducing the probability of undetected bugs.

**Requirements:**
- Target coverage levels (typically 80%+ for unit-tested modules; requirements may vary by criticality).
- Coverage must be measured and reported in CI (tools: *gcov*, *lcov*, *Bullseye Coverage*, etc).
- Coverage *gaps* (untested code) must be justified in code review (e.g., low-risk getter, platform-specific branch).

**Misconceptions:**  
Code coverage is *necessary but not sufficient* for quality. It does not guarantee bug-free code—review focus should include:
- Whether critical paths are tested.
- The validity of test cases, not just their quantity.

**Example:**  
If a module’s constructor is never exercised in tests, despite high overall coverage, reviewers must question this in code review and request additional tests.

---

## MISRA Compliance

**Context:**  
MISRA (Motor Industry Software Reliability Association) standards define strict rules for writing safe, reliable, and portable C or C++ code, widely applied in automotive and safety-critical contexts.

**Application:**
- All applicable code must adhere to the configured MISRA ruleset (e.g., MISRA C:2012).
- Compliance must be checked via static analysis tools configured for MISRA, with findings integrated into CI reports.

**Deviations:**
- Any deviations from MISRA rules must be justified with evidence, formally documented (in-code annotation and project deviation logs), and reviewed/approved by a senior engineer.
- Repeated or persistent violations require corrective action plans.

**Example:**  
If MISRA prohibits the use of dynamic memory allocation, any required usage must be isolated, justified, and specifically approved.

---

## Practical Process: Implementing Quality Gates

1. **Pre-commit:**
   - Engineers run local static analysis and tests, address all failures, and generate code coverage reports.
2. **Code Review Submission:**
   - Ensure the PR/MR passes automatic builds, test suites, and static analysis in CI.
   - Attach coverage and compliance reports as review artefacts.
3. **Review Checklist:**
   - Confirm no new warnings/errors from static analysis.
   - Verify targeted code coverage is met; request tests or justifications where not.
   - Assess for coding standard and MISRA compliance.
   - Provide and respond to review feedback. All discussions must be resolved before approval.
4. **Integration:**
   - Merge is allowed only when all required quality gates pass, and necessary reviewer approvals are secured.

---

## Summary

Effective code review and quality gate processes—including robust static analysis, comprehensive coverage, and strict standards compliance (e.g., MISRA)—are critical to delivering software that is reliable, maintainable, and fit for its intended context. Following this guidance ensures that quality is built-in, not inspected in as an afterthought.