# Reusable skill template and checklist

Replace placeholders with confirmed task information; an empty template is not a completed skill.

```markdown
---
name: task-skill-name
description: Task, when to use it, and when not to use it.
---
# Skill title
## Goal and scope
## Required inputs and sources
## Judgment criteria
## Steps and decision branches
## Output format
## Positive, negative and missing-input examples
## Exceptions, dependencies and authorization
```

Check that inputs, decisions and outputs are actionable, assumptions are marked, links exist, missing facts prompt specific questions, and examples include expected outputs. Test normal, missing-input and boundary cases; use a new case not used during authoring. Label fictional material and report simulated, actual and independent tests separately. If Xixing cannot actually be invoked, say so and provide a source-based fallback rather than claiming a call.


## Ten checks for a completed skill

1. Trigger: clear use and non-use boundaries.
2. Input: distinguish required information from optional material and ask only for consequential gaps.
3. Criteria: trace judgments to confirmed facts or sources; distinguish facts, assumptions and unknowns.
4. Actions: provide usable inputs, decision branches, outputs and checks without conflicting rules.
5. Delivery: inspect the actual skill and references; provide a usable output structure.
6. Cases: cover normal, negative, missing-input and new cases, marking synthetic cases.
7. Dependencies and authorization: use actual available tools; respect permissions and query uncertain original jobs.
8. Evidence: separate static inspection, simulation, real execution and independent review.
9. Consistency: compare rules, examples and output against actual inputs; never invent identities or dates.
10. Defaults: mark unconfirmed choices and follow the user's requested output without inventing approval.

Fix ordinary quality problems and retest. Preserve a draft and ask a specific question when essential business criteria remain unknown.
