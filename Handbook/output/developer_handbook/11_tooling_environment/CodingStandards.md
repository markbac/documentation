# Coding Standards (Embedded C)

## Overview

This page defines mandatory coding standards for embedded C development. It provides direct mapping to MISRA C, specifies linting requirements, and details rationale and practical expectations. Following these standards is essential for producing robust, portable, and maintainable embedded software, especially in safety- and mission-critical contexts.

---

## Why Coding Standards Matter

Correctness, safety, and maintainability are paramount in embedded systems. Unlike general-purpose computing, embedded systems often:
- Run with limited resources,
- Must operate without failure,
- May be deployed in safety-critical environments.

Adherence to rigorous coding standards prevents undefined behaviour, reduces bugs, improves code clarity, and facilitates static analysis and code reviews.

---

## Coding Rules and MISRA Mapping

We comply with MISRA C:2012 (including Amendment 1 and Amendment 2) as the baseline for all C code in embedded contexts. Compliance is enforced through documented deviation procedures where strict conformance is infeasible.

**Key expectations:**
- All code must adhere to MISRA C:2012 rules and directives unless a specific, recorded deviation is granted.
- The deviation process must be endorsed by the designated software lead and documented with technical justification.

### Top Applied Rules and their Rationale

Below, we summarise core MISRA C rules, rationale, and practical application or alternative guidance where relevant.

#### 1. No Undefined or Implementation-Defined Behaviour

- **Rule Example:** MISRA C:2012 Rule 1.3—No undefined or critical unspecified behaviour.
- **Importance:** Undefined or implementation-defined behaviour can produce unpredictable results across toolchains, compilers, and CPUs. This is especially risky with low-level operations, such as direct hardware access.
- **Application:** Avoid bitwise operations on signed types, pointer arithmetic outside defined bounds, use of `goto` (except as documented for error-handling patterns), and reliance on language features which change meaning between compilers.

#### 2. Strong Typing and Explicit Casts

- **Rule Example:** MISRA C:2012 Rule 10.x series (expressions shall have appropriate type).
- **Importance:** Implicit conversions (including promotions and demotions) can mask defects, especially for signed/unsigned values and integer overflows typical in embedded systems.
- **Application:** Use explicit casts when necessary, and always annotate rationale for exceptions. E.g., when casting peripheral register values to application variables of different width.

    ```c
    uint16_t sensor = (uint16_t)raw_input;
    ```

#### 3. Restricted Use of Dynamic Memory

- **Rule Example:** MISRA C:2012 Rule 21.3—No use of `malloc`, `calloc`, `realloc` or `free`.
- **Importance:** Dynamic memory allocation is unpredictable and can fragment memory on long-running embedded systems.
- **Application:** All memory must be statically allocated or established at start-up.

#### 4. Safe Macro and Inline Assembly Usage

- **Rule Example:** MISRA C:2012 Rule 20.x—Macros must be function-like when accepting arguments; avoid unsafe macro side-effects.
- **Importance:** Unsafe macros and inline assembly can obfuscate code and create maintainability or safety issues.
- **Application:** Use static inline functions instead of macros where feasible. Macros must not use parameters with side-effects (e.g., `MACRO(x++)`).

    ```c
    #define SQUARE(x) ((x) * (x)) // Acceptable, but document use
    ```
    Vs.
    ```c
    static inline int square(int x) { return x * x; } // Preferred
    ```

#### 5. Deterministic Control Flow

- **Rule Example:** MISRA C:2012 Rule 15.0x—Use structured control flow only.
- **Importance:** Non-structured flow (`goto`, early return, deep nesting) complicates code reasoning and static analysis.
- **Application:** Avoid deep nesting, limit use of conditional compilation, and restrict `goto` to designated error-handling blocks only.

#### 6. Use of Language Features

- **No variable-length arrays** (MISRA Rule 18.8): All array sizes must be compile-time constants.
- **No recursion** (MISRA Rule 17.2): Stack usage must be predictable.
- **No direct use of unqualified pointers**: Pointers to appropriate types must be used; void pointers require explicit justification and documentation.

---

## Linting and Static Analysis

### Required Tools and Configuration

- All code must be analysed using an approved static analysis tool (lint), configured to enforce:
    - Full MISRA C:2012 compliance,
    - Project-specific rules (e.g., interrupts, hardware access conventions),
    - Absence of undefined or implementation-defined constructs.

*Approved tools include:*
- PC-lint / Flexelint
- PRQA QA·C
- IAR Embedded Workbench Misra Checker
- GCC/Clang static analyser (for secondary checking only)

### Linting Workflow

1. **Continuous Integration (CI):**  
   All code is statically analysed in CI as part of the build pipeline. Lint failures block merge.

2. **Baseline:**
   - When introducing a new codebase or updating MISRA version, scan and annotate all findings.
   - Agree on deviations before code merges.

3. **Documented Deviations:**
   - Every deviation (i.e., justified MISRA violation) must reside near the affected code, and be referenced in a central deviations log.
   - Deviations must have technical justification and risk assessment.

4. **Examples:**

    ```c
    /* MISRA Deviations:
     * Rule 21.18 - Standard IO functions used for diagnostic tracing only. Justified on dev boards.
     */

    void trace_output(const char *msg)
    {
        printf("%s\n", msg); /* MISRA Deviation: Rule 21.6 - dev use only. */
    }
    ```

---

## Style Guide

- **File Naming:** Lowercase, words separated by underscores (`adc_driver.c`)
- **Function Naming:** Lowercase, words separated by underscores (`read_adc_channel`)
- **Type Names:** `typedef` names should be suffixed (`_t`).
- **Indentation:** Four spaces, no tabs.
- **Braces:** K&R style, opening brace on same line as statement.

    ```c
    if (status == OK) {
        process();
    }
    ```

- **Commenting:** Doxygen-style comments for functions and public interfaces.
- **No magic numbers:** All significant literals must be named `#define` or `const` variables.

---

## Additional Resources

- [MISRA C:2012 Summary](https://www.misra.org.uk)
- [PC-Lint User Manual]
- [Project Deviation Register] (_internal link_)

---

## Summary

Follow these coding standards uniformly for all embedded C projects. They codify best practices, align with MISRA guidance, and ensure maintainable, safe code suitable for critical embedded applications. Deviations must be rare, justified, and documented. Linting and static analysis are non-negotiable parts of the development workflow. For questions or clarifications, consult your team lead or the project's designated MISRA C champion.