# Enterprise Digital Employee Loop Scenario

This is a scenario reference for applying the general Loop Builder method to enterprise internal digital employees, Agent workflows, class-Lobster-style frameworks, or human-in-the-loop AI employees. Do not treat this scenario as the default shape of every Loop.

## Principle

Do not begin by designing complex tools for every step. Begin by designing minimum record points for the whole loop, then add tools to high-value steps.

```text
Tools can be added later; record points must exist from the start.
```

If a digital employee only has execution tools but no process records or review mechanism, it is automation, not a learning Loop.

## Three Layers

1. Business execution tools

   Help the digital employee do work: retrieve knowledge, query CRM, generate documents, call approval flows, create tickets, update internal systems, or send notifications.

2. Process record tools

   Record how the work happened: task type, context used, tools called, output, user edits, failures, handoffs, and risk decisions.

3. Review and improvement tools

   Turn records into future improvements: prompt updates, knowledge-base patches, tool-schema changes, routing changes, approval policy changes, evaluation cases, or workflow revisions.

## Build Lifecycle Loop

Digital employee construction has two connected loops:

1. Build loop: design, develop, test, release, accept.
2. Operation loop: run real tasks, collect feedback, review, update.

Do not skip the build loop. A digital employee should not enter real work only because it can generate an answer.

Minimum build lifecycle:

```text
role/task definition
-> workflow design
-> prompt and tool design
-> knowledge connection
-> logging and feedback design
-> development
-> test case construction
-> offline evaluation
-> sandbox trial
-> business acceptance
-> limited release
-> production operation loop
```

Recommended build records:

```text
build_id
owner
role_scope
task_types
workflow_version
prompt_version
knowledge_sources
tools_enabled
test_cases
offline_eval_result
sandbox_trial_result
acceptance_owner
release_decision
known_risks
created_at
```

Quality gates:

- Design gate: task scope, user, risk boundary, and success metrics are clear.
- Development gate: prompt, workflow, knowledge source, tool permissions, and logs exist.
- Test gate: offline test cases pass; known failures are categorized.
- Sandbox gate: real users try limited tasks without high-risk automation.
- Acceptance gate: business owner approves limited release.
- Release gate: rollback, monitoring, feedback capture, and review cadence exist.

## Stage Knowledge Base

Every build stage should maintain its own knowledge base. Do not rely on a single global project document, because each stage has different goals, standards, constraints, workflows, principles, and evidence.

Minimum stage knowledge base fields:

```text
stage
goal
implementation_standard
constraints
execution_workflow
principles
inputs
outputs
records
owner
review_gate
reuse_rule
```

Recommended stages:

- role-and-task-definition
- workflow-design
- prompt-tool-knowledge-design
- development
- test-case-construction
- offline-evaluation
- sandbox-trial
- business-acceptance
- limited-release
- production-operation
- weekly-review-and-update

Stage knowledge base rule:

If a stage produces decisions that affect later work, those decisions must be captured as reusable knowledge before the next stage starts.

The first version of every stage knowledge base must be completed during the design stage. After the stage knowledge base is drafted, the Loop owner must ask the requester or business/domain owner to confirm it. Do not proceed to development, testing, sandbox, acceptance, or release with unconfirmed stage knowledge.

Confirmation should cover:

- Stage goals are correct.
- Implementation standards are acceptable.
- Constraints and risk boundaries are complete.
- Execution workflows match how the organization should work.
- Principles are acceptable for future reuse.
- Inputs, outputs, records, owners, and gates are clear.

## Minimum Task Run Record

Every task run should have at least:

```text
task_id
user_id
department
agent_role
task_type
input
context_used
tools_called
output
human_feedback
status
error_reason
created_at
```

Add richer fields only when the loop needs them.

## Key Steps

1. Task intake

   Classify task type, business scene, risk level, required tools, permissions, and approval need.

2. Knowledge retrieval

   Record source documents, citations, confidence, missing knowledge, and whether the user accepted the answer.

3. Tool calling

   Record tool name, input parameters, permission check, result, success or failure, and failure reason.

4. Output generation

   Preserve original output, user-edited output, diff, rating, adoption status, and feedback tags.

5. Review cadence

   Batch review records weekly or by release cycle. Update only the highest-impact prompts, knowledge entries, tool descriptions, approval rules, or workflows.

## Suggested Feedback Tags

Use a small set first:

```text
information_wrong
missing_context
tone_wrong
format_wrong
weak_action
policy_risk
tool_error
good_reusable
```

## First-Version Build Order

1. Choose one concrete job task.
2. Define no more than five task types.
3. Define success metrics: adoption rate, edit rate, time saved, error rate, tool success rate, or human handoff rate.
4. Design the workflow, prompt, knowledge path, tool path, feedback controls, and logs.
5. Develop the minimum digital employee.
6. Build test cases from real or representative tasks.
7. Run offline evaluation and sandbox trial.
8. Pass business acceptance before limited release.
9. Add human feedback controls: accept, edit, reject, reason tags.
10. Review weekly and update only one to three high-impact items.

## Anti-Patterns

- Building a full enterprise Agent platform before one real task loop works.
- Treating memory as chat history only.
- Recording outputs but not user corrections.
- Letting agents modify prompts or policies automatically in high-risk domains.
- Optimizing tool count instead of task success.
- Measuring activity volume instead of adoption, correction rate, and failure reasons.
