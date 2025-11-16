# Developer Testing

## Overview

Developer testing encompasses all testing activities that individual engineers are expected to undertake during the software development process, prior to code review or dedicated QA involvement. Its purpose is to ensure that code meets functional requirements, integrates correctly, handles errors gracefully, and does not introduce regressions. Comprehensive developer testing is essential for product quality, team velocity, reduced rework, and maintainable software.

---

## Developer Testing Responsibilities

As a developer, you are responsible for verifying that your code and any related changes work as intended and do not negatively impact existing behaviour. This includes, at a minimum:

- Writing automated tests (unit, integration, as appropriate)
- Manually verifying features and bug fixes in relevant environments
- Running and updating the test suite
- Investigating, understanding, and resolving failing tests before submission

These responsibilities apply to all code changes, including new features, bug fixes, and refactorings.

---

## Types of Developer Testing

### Unit Testing

Unit tests verify that individual functions, methods, or classes produce the expected results given a variety of inputs. They should:

- Be fast, deterministic, and isolated — not relying on network services, databases, or shared state
- Focus on the smallest testable parts of the codebase
- Clearly cover both standard behaviour and edge cases

**Example:**

If you write a function to calculate VAT:

```python
def calculate_vat(amount, rate=0.2):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    return amount * rate
```

The unit tests should cover:

- Typical calculation
- Boundary values (e.g., amount = 0)
- Exception raising for negative values

### Integration Testing

Integration tests focus on the interactions between components, such as services, modules, or external systems. They should validate:

- Correct communication between modules
- Behaviour against databases or APIs (using test doubles or dedicated test environments if required)
- Success and failure paths related to real-world usage

**Example:**

If you implement code that writes to both a cache and database, an integration test should confirm the correct update of records in both systems when the function is invoked, as well as proper error handling when one dependency fails.

### Manual Verification

Not all issues can be identified with automated testing. You are expected to manually verify:

- End-to-end feature behaviour in the application
- User-facing changes in the environments relevant to the change (local development, staging, etc.)
- Bug fixes by reproducing the original fault and confirming resolution
- Edge cases not easily automated (e.g., unusual browser/device, complex user flows)

Manual verification is especially important for code that alters the UI, impacts accessibility, or changes interactions with third-party systems.

---

## Test Coverage Expectations

- **Every code change must include relevant, meaningful automated tests.**
- All logical branches, including error handling and boundary cases, should be sufficiently covered.
- When enhancing or altering existing behaviour, extend or update the related tests.
- Legacy code improvements should increase coverage where feasible, but never decrease it.

---

## Running and Maintaining Tests

Before submitting a change for review:

- **Run the entire local test suite and ensure all tests pass.**
- Investigate and resolve any failing tests — do not ignore or skip them.
- If tests have been modified as part of the change, double-check they accurately reflect the new intended behaviour.
- Periodically update pre-commit or CI scripts to match the current structure of the test suite.

---

## Rationale: Why Developer Testing Matters

- **Catch issues early:** Identifies functional errors and integration issues before they reach reviewers or QA, preventing rework.
- **Facilitates safe changes:** Builds confidence when refactoring or extending code by signalling regressions immediately.
- **Documents intent:** Well-written tests clarify how a component is expected to behave, improving maintainability.
- **Reduces defects:** Lowers the rate of bugs reaching production, fostering higher team and customer trust.

---

## Summary Checklist

Before submitting any code for review:

- [ ] Written or updated automated unit and/or integration tests
- [ ] Manually verified changes in relevant environments
- [ ] Run and passed the test suite
- [ ] Investigated and fixed test failures
- [ ] Ensured coverage of both typical and edge cases

---

Consistent, diligent developer testing is a non-negotiable part of our engineering process. It is essential to producing robust, reliable, and maintainable software.