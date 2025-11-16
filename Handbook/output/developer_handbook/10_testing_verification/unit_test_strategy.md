# Unit Test Strategy

This page defines our unit testing strategy, covering determinism, mocking, coverage, and Continuous Integration (CI) requirements. Adhering to this guidance ensures unit tests deliver reliable, actionable feedback and foster confidence in our codebase.

---

## 1. Determinism

**Definition**: A deterministic test yields the same outcome on every run, given unchanged code and dependencies.

**Why it matters**: 
- Non-deterministic (flaky) tests erode trust in the test suite.
- Flakiness makes CI failures difficult to diagnose, wasting engineering time.

**Guidelines**:
- Avoid reliance on timing, randomness, or external state.
- Where randomness is necessary, seed pseudo-random number generators with fixed values within the test.
- Do not depend on real system clock time. Instead, inject or mock time sources.
- Ensure no dependency on the order in which tests are run. Each test must be isolated.

**Example**:
```python
import random

def test_random_selection():
    random.seed(42)
    assert random.choice(['apple', 'banana']) == 'banana'
```

---

## 2. Mocking and Isolation

**Definition**: Mocking replaces dependencies (I/O, databases, APIs, etc.) with controllable test doubles.

**Why it matters**:
- Isolates the unit under test and ensures failures point directly to the code in question.
- Removes non-determinism caused by network, file system, or concurrent system state.

**Guidelines**:
- Mock all external services, system calls, and data stores.
- Do not make network calls or perform real disk I/O in unit tests.
- When mocking, assert not only on outputs but also on expected side effects and interaction patterns.
- Use libraries provided by your language’s ecosystem (e.g., unittest.mock in Python, Moq in .NET).
- Keep mocking configurations close to the test code to improve readability.

**Example**:
```python
from unittest.mock import Mock
def test_service_calls_api():
    api_client = Mock()
    api_client.get_data.return_value = {"value": 42}
    result = process(api_client)
    assert result == expected_result
    api_client.get_data.assert_called_once()
```

---

## 3. Coverage

**Definition**: Coverage measures the proportion of code exercised by tests (often reported as line, branch, or path coverage).

**Why it matters**:
- High coverage reduces the risk of undetected regressions.
- Gaps indicate untested, potentially unreliable code.

**Guidelines**:
- Target a minimum of 90% line coverage for critical modules and 80% for general code. Projects may set stricter targets as appropriate.
- Use coverage reports to identify missing tests. Do not blindly increase coverage—ensure tests are meaningful and assertions reflect intended behaviour.
- Include edge cases and typical data, not just “happy paths”.
- Treat excluded code (e.g., legacy, auto-generated, or platform-specific fallbacks) as technical debt and track it as such.

**Example**:
Ensure the following function is not covered only for valid inputs:
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
```

---

## 4. Continuous Integration (CI) Expectations

**Definition**: CI automatically runs tests on each commit/merge request, ensuring code quality and feedback.

**Why it matters**:
- Prevents regressions from entering shared branches.
- Encourages developers to maintain and improve the test suite.

**Guidelines**:
- All unit tests must pass in the CI environment before code is merged.
- The CI environment must reflect the target production environment as closely as practical (matching Python/Java version, OS, etc.).
- Flaky tests or those requiring manual intervention are not permitted in the main test suite.
- Coverage thresholds must be enforced by the CI pipeline; code that reduces coverage below the project baseline should not be merged without review.
- Test output should be clear and actionable. Failures must indicate sufficient context for troubleshooting.

---

## Summary Checklist

- [ ] Tests are deterministic and repeatable.
- [ ] All external dependencies and side effects are mocked or stubbed.
- [ ] Coverage is measured, gaps are identified and justified, and targets are met.
- [ ] Tests run and pass in CI, with failures providing clear diagnostics.

By following this strategy, we maintain a robust, maintainable codebase. For further details on test structure, see related pages (e.g., [Test Naming], [Integration Testing], [Code Review Process]).