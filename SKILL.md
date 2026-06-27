---
name: loop-builder
description: Design and scaffold reusable learning, feedback, and improvement loops from ambiguous tasks, product ideas, workflows, personal systems, team operations, content processes, research processes, engineering practices, Agent systems, or organizational routines. Use when Codex needs to build a Loop, define a closed-loop process, design feedback capture, create evaluation/update cycles, generate Loop artifacts/templates/logs, turn one-off work into reusable principles, or plan how any system should learn from repeated action and correction.
---

# Loop Builder

## Core Idea

A Loop is not repeated execution. A Loop is a system where each round of action changes the next round.

Use this skill to convert a task, workflow, product process, learning practice, creative routine, research process, engineering habit, Agent behavior, or organizational operation into a minimum viable feedback loop with clear inputs, actions, observations, updates, and reuse.

Do not stop at advice when the user is building a concrete Loop. Produce durable artifacts: design docs, record schemas, feedback tags, review templates, experiment plans, update logs, or scaffolded files.

When working inside a project that has local Loop principles, read them before designing the Loop. In this workspace, read `.agents/loop-principles.md` before creating or updating Loop artifacts.

## Non-Negotiable Rules

- Apply `如无必要，勿增实体`: do not add roles, stages, tools, files, directories, records, abstractions, ceremonies, metrics, or gates unless they are necessary to close the Loop, reduce meaningful risk, preserve reusable learning, or satisfy a confirmed project constraint.
- Respect role position and authority. If the current role would decide, perform work, or modify artifacts outside its assigned responsibility, it must immediately state the boundary, stop, and hand off to the responsible role or subagent.
- Give every active role category or subagent category an independent workspace folder. A role category is a reusable responsibility type such as demand intake, product/workflow, development, testing/evaluation, governance/risk, Loop Manager, domain owner, or Super Assistant. Multiple concrete roles or sessions in the same category may share that category folder when their responsibility boundary is the same; create separate folders only when ownership boundaries, authority, records, or confidentiality differ.
- Give every role a Loop charter at creation time: goal, implementation standard, constraints, inputs, outputs, records, evaluation/feedback signals, update responsibility, authority boundary, role category, category workspace, and handoff rules.
- Check every role's tools and skills before execution. Required skills, tools, data access, scripts, references, and permissions must be identified, available/activated/installed/substituted, or explicitly marked as blockers.
- Create a Loop Manager at the very start of every concrete Loop project, before demand intake and before implementation roles. The Loop Manager is distinct from a project manager: it governs the whole Loop system, not ordinary delivery management. It manages Loop cadence, status, risks, decisions, blockers, handoffs, review rituals, role self-review, role advice summaries, role health checks, experience distillation checks, resource status, project-level reflection, and feedback to the Super Assistant. During implementation role creation or role/personnel/session adjustment, it must maintain the active role registry: selected roles, role categories, role IDs, category workspaces, Codex sessions, authority boundaries, readiness, health, resource needs, status, and handoff targets. After any role is created, activated, paused, replaced, closed, or its concrete person/agent/session changes, the Loop Manager must notify every other active role, record the notification in `interaction-evidence-log.md` and the relevant role workspaces, and include what changed, why, effective time, affected boundaries, handoff impact, and required action. It must not do development, testing conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, or role-specific implementation work.
- Treat Codex goal-setting with the Loop Manager as management input, not execution authorization. When the user sets a goal, the Loop Manager must turn it into a goal contract, task dispatch packet, target role/session, role category, category workspace, evidence requirements, and gate. It must choose the target from the active role registry, update dispatch status against that role, and route the work to the responsible role or record a blocker if that role/session is unavailable; it must not perform developer, tester, product, governance, or release work itself.
- Let roles communicate directly to resolve ordinary disagreements about assigned tasks, handoffs, evidence, or standards. If a disagreement affects scope, acceptance criteria, risk, schedule, resource allocation, role authority, or cannot be resolved quickly, escalate it to the Loop Manager. The Loop Manager records options, evidence, impact, and recommendations, then asks the user or domain owner to decide.
- Require all role-to-role messages and interactions to be recorded in project documents. Handoffs, advice, decisions, disagreements, questions, answers, status updates, test findings, acceptance feedback, implementation claims, blocker reports, and update proposals must be logged in `interaction-evidence-log.md`, the sender/receiver category workspace, or another named project document. Each record must include date/time, sender role, receiver role, interaction type, summary, decision or requested action, document/material path or artifact reference, evidence gap status, follow-up owner, and status. Do not treat an unrecorded role message as part of the Loop state.
- Require every active role to sync task status to the project owner during task flow at the cadence defined in the dispatch packet, and immediately when the role completes its assigned task before handoff, return, closure, or acceptance. The project owner defaults to the Loop owner / Super Assistant unless the user names another project owner. Each status sync must be recorded as `role-status-sync` in `interaction-evidence-log.md` and the role category workspace, with task ID, role ID, current state, progress, completed work, evidence, blockers, risks, next handoff, ETA or completion time, and any decision needed. Loop Manager monitors missing or stale status syncs but does not perform the role's work.
- When a project manager / delivery coordinator is selected, every new project question, request, issue, or work item must be classified by project nature and routed through the complete workflow for that project type. For software development, the workflow must cover demand clarification, product/workflow scope, codebase exploration when needed, architecture/design, implementation, testing/evaluation, code review and specialized reviews as needed, release/operation readiness, and review/update. Every role created for the Loop must include its project-type workflow requirement: which workflow stage it belongs to, required prior inputs, required outputs, status-sync duties, quality gate, next handoff, and what it must not skip. Loop Manager checks workflow completeness but does not perform project-manager delivery execution.
- Create a demand intake role before implementation roles. It must turn rough ideas into concrete use cases with actor, scenario, trigger, preconditions, steps, expected output, measurable acceptance standard, constraints, records, feedback signal, owner, and confirmation status.
- Require demand intake to use `grill-me` when available before declaring demand implementation-ready.
- Select implementation roles from the existing reusable role library whenever possible. Match project needs and confirmed use cases to existing role categories first; create a new role only when no existing role can responsibly cover the work. Present the selected role set, excluded candidate roles, reasons, category workspaces, authority boundaries, and tool/skill readiness to the user for confirmation before implementation.
- Treat every role as an expert advisor, but separate confirmed requirements from recommendations, assumptions, risks, and questions. Important advice cannot silently become execution scope.

For detailed role creation, Loop Manager, demand intake, tool readiness, boundary, advisor, self-review, and Codex session rules, read `references/role-system.md` whenever defining roles, workspaces, sessions, implementation teams, tool/skill readiness, or project governance.

For software, product, Agent, workflow, digital-employee, or engineering Loops, read `references/candidate-role-library.md` before forming the implementation team. Start from existing reusable candidate roles such as Loop Manager, product manager, optional project manager/delivery coordinator, codebase explorer, software architect, developer, tester, code reviewer, security reviewer, performance analyzer, UI/frontend reviewer, documentation/API role, governance/risk, and domain owner. Select only the roles required by project needs and confirmed use cases, document why each selected role is needed, document why non-selected candidate roles are excluded, and ask the user to confirm the selected implementation role set before execution.

## Input Refinement Standard

When the user provides rough goals, standards, constraints, stages, metrics, or success criteria, refine them before treating them as executable Loop knowledge.

Refined Loop knowledge must be:

- Actionable: each item tells an actor what to do, decide, record, or avoid.
- Testable: each item has an observable pass/fail signal or review method.
- Quantified where useful: use counts, thresholds, timeboxes, rates, sample sizes, owner names, dates, or explicit decision options when they change execution.
- Bounded: define scope, exclusions, risk boundaries, and handoff conditions.
- Recordable: define what evidence or event should be captured.
- Owned: assign the responsible role or owner.
- Reusable: phrase the item so the next similar Loop can reuse it.

If a user-provided item is vague, refine it into a concrete draft and mark it as an assumption, or ask for the missing decision when guessing would create meaningful risk. Do not leave generic goals such as "improve quality", "make it usable", or "do testing" without standards, signals, records, and gates.

## Default Workflow

1. Identify the loop object

   Decide what should improve across rounds: skill, quality, judgment, speed, accuracy, consistency, reliability, trust, cost, output usefulness, or business results.

2. Assign the Loop owner and create the Loop Manager

   A Loop must have one owner. In this user's system, the default Loop owner is the Super Assistant. The owner drives the whole process and coordinates roles.

   Create the Loop Manager at project start, before demand intake and before implementation role selection. The Loop Manager manages the whole Loop operating system: cadence, active role registry, role health checks, resource status, role self-review, experience distillation, role advice summaries, blockers, risks, handoffs, project-level reflection, and feedback to the Super Assistant. It is not the project manager. A separate project manager/delivery coordinator is optional and only exists when delivery scheduling, milestone tracking, external dependency coordination, or stakeholder status reporting cannot be covered cleanly by another role.

3. Create the demand intake role

   Define the role responsible for receiving, clarifying, refining, and confirming the user's need. It owns the initial demand record, rough-to-executable refinement, concrete use cases, open questions, acceptance criteria, confirmation status, and first handoff.

   Each use case should define ID/name, actor, scenario/trigger, preconditions, steps, expected output, measurable acceptance standard, constraints/exclusions, records, feedback signal, owner, and confirmation status.

   If `grill-me` is installed, use it before handoff and treat the grilling result as input for refining use cases, standards, risks, and confirmation questions.

4. Refine rough inputs into executable standards

   Convert the user's goals, constraints, and success criteria into concrete Loop knowledge. For each important item, define the action, owner, measurable or observable standard, record, and confirmation status.

5. Select the implementation roles and skill map

   Create only the implementation roles required by the confirmed need. For software/product/build-oriented Loops, start from the existing reusable candidate role library rather than inventing roles from scratch: Loop Manager, product manager/workflow designer, optional project manager/delivery coordinator, codebase explorer, software architect, developer/implementer, tester/evaluator, code reviewer, security reviewer, performance analyzer, UI/frontend reviewer, documentation/API role, governance/risk, and domain owner. Match confirmed use cases to existing role categories first. Create a new role only when the project need cannot be covered by an existing role category without blurring authority or evidence boundaries.

   For each selected role, define position, category, responsibility boundary, Loop charter, project-type workflow requirement, category workspace, Codex thread/session mapping, required skills, required tools/data/references/permissions, readiness status, advisor contribution, activation trigger, inputs, outputs, gates, and handoffs. Also record non-selected candidate roles and why they are not needed for this project.

   Tell the user the proposed Loop implementation role set and ask them to confirm the role selection before execution. The confirmation packet must include selected roles, excluded existing roles, selection reasons, authority boundaries, category workspaces, tool/skill readiness, and the first handoff path. After confirmation, the Loop Manager records the active roles in `role-registry.md` before any task dispatch. Do not proceed into implementation until the role selection is confirmed or the user explicitly delegates confirmation to the Loop owner.

6. Define the minimum viable loop

   Start with the smallest full cycle that can run:

   ```text
   goal -> input -> action -> observation -> update -> reuse
   ```

   For build-oriented Loops such as software products, Agent systems, or digital employees, split action into explicit build lifecycle stages:

   ```text
   design -> develop -> test -> release -> operate -> review -> update
   ```

   Do not collapse development and testing into a generic action when they carry different owners, records, and gates.

   For every stage, create or update a stage knowledge base with goal, implementation standard, constraints, execution workflow, principles, inputs, outputs, and records. Build the first version of all stage knowledge bases during design, then require requester or domain-owner confirmation before execution.

7. Create the implementation plan and role/subagent assignment

   Map each stage to responsible owner/role, role category, whether a dedicated subagent is required, why it is necessary, authority boundary, category workspace, Codex session mapping, tool/skill readiness, stage knowledge base, inputs, outputs, records, quality gate, and next handoff.

   Default to one Super Assistant as Loop owner switching stage knowledge bases. Add dedicated subagents only when needed for specialized execution, independent review, parallel work, risk isolation, or long-running operation.

8. Design observation points

   Choose signals that prove whether the loop improved, such as adoption, correction rate, failure reason, time saved, test pass rate, quality rating, decision accuracy, risk events, completion rate, or reuse rate.

9. Capture structured records

   Record the minimum event data needed to debug, compare, and improve later. Do not wait for a complete analytics platform.

10. Convert feedback into updates

   Decide what feedback can change: principle, checklist, template, prompt, SOP, knowledge base, tool schema, workflow routing, approval policy, UI, evaluation set, training material, or role definition.

11. Save the learning

   Put valuable learning into a durable artifact: project docs, checklists, templates, scripts, tests, skill instructions, prompts, or operational dashboards.

## Artifact Mode

When the user has a concrete scenario, create a Loop file pack unless they only ask for explanation. Default location inside a project is:

```text
loops/<loop-slug>/
```

Use `scripts/create_loop_pack.py` to scaffold the pack when file creation is appropriate:

```bash
python <skill-dir>/scripts/create_loop_pack.py "<loop name>" --out loops --type "<loop type>" --slug "<ascii-slug>"
```

Generated files include:

- `loop-design.md`: loop object, minimum viable loop, records, signals, update mechanism, first build order.
- `team-formation.md`: demand intake, existing-role selection, implementation role set, excluded candidate roles, skill/tool readiness, and requester confirmation of role selection.
- `candidate-role-library.md`: reusable candidate roles with best-practice skill, tool, knowledge-base, record, and handoff matches.
- `use-cases.md`: concrete, measurable use cases created by demand intake.
- `role-loop-charters.md`: role goals, standards, constraints, records, evaluation/feedback, update duties, authority, and handoffs.
- `loop-manager.md`: Loop-level cadence, role health checks, resource status, role self-review rhythm, experience distillation checks, project reflection, feedback to Super Assistant, and skill-iteration candidates.
- `stage-knowledge-base.md`: per-stage goals, standards, constraints, workflows, principles, outputs, and records.
- `stage-confirmation-checklist.md`: requester/domain-owner confirmation gate for the stage knowledge base.
- `implementation-plan.md`: stage execution plan, responsible roles, subagent justification, gates, tool readiness, and handoffs.
- `role-workspaces.md`: category folder ownership map for each role/subagent category, including when multiple concrete roles share one category folder.
- `role-sessions.md`: Codex thread/session map for each role/subagent.
- `role-registry.md`: Loop Manager-maintained active role list with role IDs, categories, workspaces, sessions, authority boundaries, readiness, status, and dispatch ownership.
- `goal-dispatch-log.md`: Loop Manager goal intake, role-registry-based routing, task dispatch packets, project-owner status sync cadence, completion sync requirements, and blocked dispatches.
- `decision-conflict-log.md`: role disagreement records, Loop Manager escalation packets, and user/domain-owner decisions.
- `interaction-evidence-log.md`: required message and interaction records for all role-to-role communication, with document/material paths, artifact references, data sources, online links, evidence gaps, follow-up owners, and status.
- `refinement-standard.md`, `run-log.csv`, `feedback-tags.md`, `weekly-review.md`, `experiment-plan.md`, and `update-log.md`.

After scaffolding, customize files for the user's scenario. Do not leave placeholders if the user gave enough context.

Before moving past Loop design, explicitly ask the requester or domain owner to confirm the stage knowledge base. If confirmation is missing, stop at design artifacts and do not proceed to execution, development, testing, sandbox, acceptance, or release.

## Loop Quality Test

A proposed Loop is weak if it cannot answer these questions:

- What exactly improves after each round?
- Is there a demand intake role that refined rough ideas into concrete, measurable use cases?
- Did demand intake use `grill-me` when available before implementation handoff?
- Were rough goals refined into actionable, testable, bounded, owned, recordable standards?
- Who owns the Loop end to end?
- Is there a Loop Manager created at project start, distinct from project manager/delivery coordination, and barred from development, testing conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, and role-specific implementation?
- Did the implementation role set form by selecting from existing reusable roles based on confirmed demand rather than unnecessary role creation?
- Does every active role have a Loop charter, project-type workflow requirement, authority boundary, role category, category workspace, handoff rule, Codex session mapping if used, advisor contribution, tool/skill readiness status, role health/resource status, and an entry in the Loop Manager's active role registry? After any role/personnel/session change, did the Loop Manager notify all other active roles and record that broadcast in project documents?
- When the user sets a goal with the Loop Manager in Codex, does the Loop Manager choose the responsible role from the active role registry, dispatch a task packet to that role, update dispatch status, and avoid executing out-of-role work?
- Is there a disagreement path: role-to-role communication first, Loop Manager escalation for major issues, and user/domain-owner decision for unresolved or high-impact conflicts?
- Are all role-to-role messages and interactions recorded in project documents, with sender, receiver, interaction type, summary, requested action or decision, evidence link/path, follow-up owner, and status? Do active roles sync task status to the project owner at the required cadence and immediately on completion, with `role-status-sync` evidence?
- Did the user confirm the selected Loop implementation role set before execution, including selected roles, excluded candidates, role categories, authority boundaries, and category workspaces?
- What signal shows whether it improved?
- What gets recorded automatically or manually?
- If something is being built, what are the development, testing, release, and acceptance gates?
- Does each stage have its own goal, standard, constraints, workflow, principles, outputs, and records?
- Did the requester or domain owner confirm the stage knowledge base before execution began?
- Who or what reviews the record?
- What artifact changes before the next round?
- How will the next similar task reuse the learning?

A Loop is valid when it is repeatable, observable, updatable, transferable, and saved somewhere durable.

## Design Heuristics

- Prefer one real business scene over a broad platform plan.
- Make the first loop small enough to run this week.
- Turn adjectives into evidence: replace "good", "usable", "accurate", or "safe" with standards, examples, thresholds, review methods, or gates.
- Treat the user's first description as raw material to improve: enrich it with best practices, but label assumptions, advice, risks, and confirmation needs.
- Add records before adding complex tooling.
- Apply `如无必要，勿增实体` before adding any role, stage, tool, artifact, record field, metric, approval gate, or directory.
- Do not create a subagent per stage by default; assign subagents only when the implementation plan justifies why the Super Assistant plus stage knowledge base is insufficient.
- Treat out-of-scope modification and out-of-role work as handoff triggers.
- Treat corrections and surprises as high-value learning data.
- Record failures in categories that can change future behavior.
- Avoid automatic self-modification for risky systems; batch review and version updates.
- If a process only executes work and never records feedback, it is automation, not a learning Loop.

## Scenario References

Keep the core Loop method general. Load scenario references only when the user's request matches them.

- Enterprise digital employees, Agent workflows, human-in-the-loop AI employees, or class-Lobster-style frameworks: read `references/enterprise-digital-employee-loop.md`.

## Output Shape

When answering a Loop-design request, provide the Loop owner, roles and role categories, loop object, minimum viable loop, key records, feedback/evaluation signals, update mechanism, first implementation order, implementation plan with responsible role/subagent assignment and category workspace assignment, role message documentation rule, interaction evidence rule, disagreement/escalation path, risks or anti-patterns, confirmation needed before execution, and artifact pack path if files were created.

Keep the result concrete enough that the user can start building immediately.
