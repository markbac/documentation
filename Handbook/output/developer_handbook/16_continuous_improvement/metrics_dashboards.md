# Metrics and Dashboards

## Purpose

This page provides practical guidance on what to visualise on engineering dashboards, and why doing so enables effective and continuous improvement. It is intended to help you select, define, and justify metrics that guide action, offering clarity rather than noise.

## Why Visualise Metrics?

Visualising metrics makes essential information visible and accessible, supporting informed and timely decision-making. Well-chosen metrics, clearly presented, help teams:

- Identify bottlenecks and inefficiencies
- Track the effectiveness of changes
- Align day-to-day activity with strategic objectives
- Respond early to emerging issues
- Foster a culture of accountability and improvement

Conversely, poor or poorly presented metrics create confusion, distract from priorities, and undermine trust.

## Guiding Principles

When deciding what to visualise:

- **Prioritise actionable metrics:** Only display measures that clearly inform improvement or decision-making.
- **Show trends, not just snapshots:** Metrics should reveal changes over time, not just current values.
- **Present leading indicators:** Where possible, prefer metrics that predict future outcomes rather than simply reporting the past.
- **Contextualise with targets or benchmarks:** Always provide reference points so deviations are understood.
- **Be transparent:** Show both successes and failures. Hiding problems delays their resolution.

## Essential Metrics to Visualise

The following categories cover the core areas typically relevant to engineering teams. Not every metric is required for every team or context; select those that are meaningful for your objectives.

### 1. Delivery Performance

**Objective:** Understand how reliably and quickly value is shipped.

#### Example Metrics

- **Lead Time:** Time from work inception (idea or ticket created) to production deployment.
    - *Why?* Reveals how long it takes to deliver a feature or fix, highlighting process delays.
    - *How to Visualise:* Line chart over time, segmented by type of work (bug, feature).
- **Deployment Frequency:** Number of production releases per time period.
    - *Why?* Frequent, small releases usually correlate with lower risk and higher quality.
    - *How to Visualise:* Bar or run chart; annotate points where frequencies dip.
- **Change Failure Rate:** Percentage of deployments causing failures or requiring hotfixes.
    - *Why?* Measures stability and the effect of process or technical changes.
    - *How to Visualise:* Stacked bar with total releases vs failures.

### 2. Quality and Reliability

**Objective:** Detect defects and systemic issues early; maintain trust in software.

#### Example Metrics

- **Defect Escape Rate:** Number of defects found in production vs total discovered.
    - *Why?* High rates may indicate inadequate pre-production verification.
    - *How to Visualise:* Trend line; compare with testing coverage.
- **Mean Time to Recovery (MTTR):** Average time to restore service after a failure.
    - *Why?* Shorter MTTR demonstrates effective incident response.
    - *How to Visualise:* Line chart; mark incidents exceeding expectations.
- **Customer-Reported Issues:** Rate and severity of externally reported defects.
    - *Why?* Indicates customer impact, guiding quality improvement.
    - *How to Visualise:* Volume and severity heatmap.

### 3. Flow and Process Health

**Objective:** Expose sources of friction, rework, or waste in the delivery process.

#### Example Metrics

- **Work in Progress (WIP):** Number of items actively being worked on at any one time.
    - *Why?* Excess WIP leads to context switching and delayed outcomes.
    - *How to Visualise:* Daily or weekly counts, highlighted if above target thresholds.
- **Queue Times:** Time items spend waiting at each stage of the workflow.
    - *Why?* Highlights process bottlenecks.
    - *How to Visualise:* Stacked bar or cumulative flow diagram.
- **Blocked Items:** Number and duration of tickets blocked, with reasons.
    - *Why?* Provides early signals of systemic impediments.
    - *How to Visualise:* List or tally with trend annotations.

### 4. Technical Debt and Code Health

**Objective:** Monitor aspects of code quality that affect long-term maintainability.

#### Example Metrics

- **Code Churn:** Percentage of code changed over time, especially in the same files.
    - *Why?* Persistent churn in particular areas may reflect design issues.
    - *How to Visualise:* Time series by module or feature.
- **Automated Test Coverage:** Percentage of code exercised by tests.
    - *Why?* Helps assess confidence in refactoring or deploying.
    - *How to Visualise:* Coverage trend line; highlight sudden drops.
- **Static Analysis Warnings:** Number and severity of style or bug warnings.
    - *Why?* Guides refactoring priorities.
    - *How to Visualise:* Stacked bar by warning category.

## Dashboard Design Considerations

- **Clarity:** Use clear labelling, simple visual styles, and avoid clutter.
- **Accessibility:** Ensure all team members can easily access and interpret dashboards.
- **Drill-Down Capabilities:** Provide the ability to investigate anomalies, not just surface-level stats.
- **Automated Refresh:** Data should update without manual intervention to maintain relevance.
- **Single Source of Truth:** Dashboards should reference authoritative systems directly, avoiding manual copying.

## Anti-Patterns

Avoid the following:

- **Vanity Metrics:** Tracking numbers (e.g., 'commits per developer') that do not lead to meaningful change.
- **Overloading with Data:** Too many metrics dilute focus and reduce adoption.
- **Hiding Bad News:** Dashboards should never mask negative trends; these are key triggers for improvement.

## Example: Applying the Guidance

**Scenario:** You notice that deployment frequency has decreased over the last month, while mean lead time has increased.

- **Action:** Use the dashboard to identify corresponding increases in WIP or blocked items.
- **Root Cause:** Drill down into queue times at different workflow stages to identify the bottleneck.
- **Response:** Plan targeted improvements where delays are occurring, and monitor relevant charts to confirm the effect.

## Summary

Visualising the right metrics through effective dashboards is a foundation of continuous improvement. Good metric selection, informed by clear rationale and focused on actionable insights, allows engineering teams to detect issues early, measure progress, and drive positive change. Always tailor dashboards to present information that matters to your specific objectives, and commit to honest, evidence-driven visualisation.