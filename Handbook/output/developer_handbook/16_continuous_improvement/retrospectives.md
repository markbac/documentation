# Retrospectives

Continuous improvement is foundational to effective engineering teams. Retrospectives are a key tool in this process, enabling teams to regularly reflect, learn, and adapt. This page details proven formats, essential follow-up practices, and how to foster a culture focused on prevention rather than blame.

---

## Purpose of Retrospectives

Retrospectives are structured sessions that allow teams to inspect how they work, identify strengths, uncover inefficiencies, and agree on actionable improvements. Regular retrospectives ensure lessons are captured and acted upon, reducing the recurrence of issues and increasing overall team performance.

---

## Recommended Retrospective Formats

Selecting a suitable format depends on team maturity, size, and the challenges at hand. The following formats have demonstrated effectiveness across various engineering contexts:

### 1. Start, Stop, Continue

- **Purpose**: Highlight clear actions and ongoing habits.
- **How it Works**: Each team member proposes activities to *start* (new beneficial practices), *stop* (ineffective or harmful practices), and *continue* (proven successful actions).
- **Benefits**: Simple, actionable; surfaces concrete suggestions.
- **Example**:
  - *Start*: Pair reviewing critical code changes.
  - *Stop*: Relying on ad hoc production access for debugging.
  - *Continue*: Maintaining the incident log after outages.

### 2. 4Ls (Liked, Learned, Lacked, Longed For)

- **Purpose**: Surface emotional and pragmatic feedback.
- **How it Works**: Team members list what they liked, learned, lacked, or longed for during the cycle.
- **Benefits**: Encourages broader reflection, addresses morale as well as process.
- **Example**:
  - *Liked*: Everyone contributed to incident resolution.
  - *Learned*: The new deployment script saves 20 minutes per release.
  - *Lacked*: Clear documentation for onboarding new joiners.
  - *Longed For*: Earlier reminders about scheduled maintenance.

### 3. Timeline-Based Retrospective

- **Purpose**: Analyse a significant project phase or incident.
- **How it Works**: The team constructs a timeline of key events, then discusses what went well and where issues emerged.
- **Benefits**: Effective for complex or longer periods, uncovers hidden dependencies.
- **Example**: Used after a major outage to trace decisions leading up to failure and recovery.

### Facilitation Tips

- Assign a facilitator (can be rotated).
- Allocate a fixed duration (typically 30–60 minutes).
- Encourage equal participation.
- Use collaborative tools for remote teams (e.g., virtual whiteboards).

---

## Follow-up Rules

Retrospectives have limited value without disciplined follow-up. Adopt these rules to ensure outcomes result in meaningful change:

### 1. Trackable Action Items

- **What to Do**: Document each agreed action using a team-visible tracking system (e.g., your project board).
- **Why**: Ensures actions are not forgotten and responsibilities are clear.

### 2. Assign Owners and Due Dates

- **What to Do**: Assign an owner and a realistic completion date for every action.
- **Why**: Named responsibility drives accountability and clarity.

### 3. Review Progress Consistently

- **What to Do**: Begin each retrospective by reviewing the status of previous actions.
- **Why**: Maintains momentum; surfaces systemic blockers.

### 4. Keep Actions Scalable

- **What to Do**: Break down large or vague items into manageable, shippable changes (batching multiple improvements is discouraged).
- **Why**: Small, iterative changes embed continuous improvement and reduce risk of inaction.

#### Example of Poor vs. Effective Follow-up

- **Ineffective**: “Improve code review process.”
- **Effective**: “Trial a code review checklist for all pull requests next sprint; [owner], due by [date].”

---

## Establishing a Culture of Prevention

Retrospectives work best in environments where the goal is learning and prevention, not assigning blame. To foster this:

### 1. No Blame Policy

- Focus on *processes* and *systems*, not individuals.
- Facilitators should redirect “who” discussions to “what” and “why”.

### 2. Root Cause Analysis

- Ask why issues occurred, progressing beyond immediate symptoms (“the five whys” technique is useful).
- The intention is to address underlying causes rather than superficial fixes.

### 3. Encourage Transparency

- Teams should feel safe to share mistakes or concerns without fear of reproach.
- Celebrate candour that helps prevent future problems.

### 4. Document and Share Learnings

- Retrospective summaries (actions and context) should be accessible to the wider engineering organisation, especially after incidents.
- This prevents repeat errors across teams and builds collective wisdom.

---

## Practical Example

After a missed release deadline, the team runs a retrospective using the Start/Stop/Continue format.

- *Start*: Conducting estimates as a group instead of individually.
- *Stop*: Accepting mid-sprint feature requests without review.
- *Continue*: Daily standups to surface blockers early.

Actions are tracked in the team's Jira board. Each item is assigned an owner and reviewed at the next meeting.

---

## Expectations

- Hold retrospectives at a regular, predictable cadence (e.g., every two weeks, or immediately after major events/incidents).
- Every team member participates actively.
- Record all actions publicly and transparently.
- Actions are completed within agreed timeframes or re-evaluated if blocked.
- The focus is always on systems and improvement, not individual fault.

---

## Summary

Retrospectives are critical for sustained team improvement when run with structure, transparency, and commitment to follow-up. Focus on actionable outcomes, prevent recurrence through root cause analysis, and prioritise learning over blame. This practice forms a cornerstone of high-performing engineering teams.