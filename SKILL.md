---
name: loop-builder
description: Design and scaffold reusable learning, feedback, and improvement loops from ambiguous tasks, product ideas, workflows, personal systems, team operations, content processes, research processes, engineering practices, Agent systems, or organizational routines. Use when Codex needs to build a Loop, define a closed-loop process, design feedback capture, create evaluation/update cycles, generate Loop artifacts/templates/logs, turn one-off work into reusable principles, or plan how any system should learn from repeated action and correction.
---

# Loop Builder

A Loop is not repeated execution. A Loop is a system where each round of action changes the next round.

Use this skill to turn rough goals, product ideas, engineering work, Agent systems, team operations, research routines, or organizational practices into reusable feedback loops with clear roles, records, gates, learning signals, and update mechanisms.

## Core Rules

- Read local Loop principles before creating or updating Loop artifacts. In this workspace, read `.agents/loop-principles.md` when available.
- Produce durable artifacts for concrete Loop work, but control document growth. Before creating any new project document, check `document-index.md` or create it if missing; reuse, update, or merge into existing documents unless a new document has a distinct owner, purpose, lifecycle, evidence boundary, or confidentiality boundary.
- Apply `如无必要，勿增实体`: add roles, stages, tools, records, gates, or abstractions only when they close the Loop, reduce meaningful risk, preserve reusable learning, or satisfy a confirmed constraint. In early project stages, keep the active role set small: Loop Manager is mandatory, and the other active roles should usually start with 2-3 roles selected for the next Loop round. Separate role files or workspaces are allowed for clarity; avoid activating too many specialized roles before confirmed complexity, workload, risk, or workflow evidence requires splitting them out.
- Separate confirmed requirements from advisor recommendations, assumptions, risks, and questions. Advice does not become execution scope without confirmation.
- Keep role authority explicit. A role that reaches outside its boundary must state the boundary, stop, hand off, and record the handoff.
- Turn hard constraints into explicit gates with owners, evidence, and blockers. If a role changes a user-facing product, workflow, UI design, acceptance standard, risk boundary, release scope, or other confirmed constraint, the change is only a proposal until the user/domain owner or delegated decision owner confirms it. Different roles must enforce the gate at their stage instead of relying on memory.
- Require all role-to-role messages, status syncs, handoffs, disagreements, blockers, advice, test findings, acceptance feedback, implementation claims, and update proposals to be recorded in project documents.

## Reference Routing

Load only the reference needed for the current task:

- Read `references/role-system.md` when defining roles, role categories, role workspaces, Loop Manager duties, implementation covenants, goal dispatch, status sync, interaction records, tool readiness, authority boundaries, Codex sessions, or handoff rules.
- Read `references/candidate-role-library.md` when selecting implementation roles, checking reusable role presets, reviewing product/development role capabilities, or tracking ECC / Everything Claude Code, Claude Code plugins, and other capability sources for candidate-role updates. Start from the existing reusable role pool before creating new roles.
- Read `references/artifact-pack.md` when scaffolding Loop files, checking generated artifact responsibilities, or validating whether a Loop design is complete.
- Read `references/enterprise-digital-employee-loop.md` only for enterprise digital employees, Agent workflows, human-in-the-loop AI employees, or class-Lobster-style frameworks.

## Default Workflow

1. Identify the Loop object.
   Decide what should improve across rounds: quality, judgment, speed, reliability, trust, cost, usefulness, business result, role capability, or communication efficiency.

2. Refine rough input.
   Convert vague goals into actionable, testable, bounded, recordable, owned, and reusable standards. Mark assumptions and confirmation needs.

3. Create Loop governance first.
   For every concrete Loop project, create the Loop Manager at project start, before demand intake and before implementation roles. Loop Manager is mandatory and distinct from project manager/delivery coordination. Give it default automatic distillation time nodes immediately: project-start baseline, task/stage completion checkpoint, weekly fixed retrospective unless another cadence is confirmed, event-triggered review after blockers/role changes/major disagreements, and project-closure distillation.

4. Create demand intake.
   The demand intake role turns rough user ideas into concrete use cases with actor, scenario, trigger, preconditions, steps, expected output, measurable acceptance standard, constraints, records, feedback signal, owner, and confirmation status. Use `grill-me` when available before declaring demand implementation-ready.

5. Select implementation roles conservatively.
   Match confirmed needs to existing candidate roles first, but start with the smallest active role set that can responsibly run the next Loop round. A normal early project shape is Loop Manager plus 2-3 other active roles; choose those roles by project nature instead of by habit. Prepare selected roles, deferred candidate roles, excluded roles, split triggers, reasons, role categories, workspaces, authority boundaries, tool/skill readiness, and first handoff path for user/domain-owner confirmation before implementation. Do not activate specialized roles merely because they exist in the candidate library.

6. Track reusable role capability sources.
   During fixed-time reviews, and monthly by default when no cadence is set, check ECC / Everything Claude Code, Claude Code plugins, local plugin/tool metadata, and relevant external role references for new or changed role capabilities. Update candidate-role requirements only when the source changes a responsibility boundary, skill/tool match, evidence standard, activation trigger, or handoff rule.

7. Evolve role skills gradually.
   Treat every role's skills, tools, checklists, references, prompts, and working standards as improvable Loop artifacts. With Loop Manager support, each role should record skill gaps, useful techniques, repeated mistakes, missing tools, better prompts, and update proposals after real work. Loop Manager distills these into role charter updates, candidate-role library updates, implementation covenant changes, templates, or skill update candidates at the default distillation time nodes.

8. Establish role operating rules.
   Give every active role a Loop charter and category workspace. Before execution, create `implementation-covenant.md` so active roles share one agreement for role boundaries, communication content requirements, handoff packages, status sync, evidence, and escalation.

9. Define hard constraint gates.
   Convert mandatory principles into stage gates. For each hard constraint, record the trigger, decision owner, enforcing role, required evidence, stop condition, and next handoff. Example: if the product manager changes UI/product design, scope, workflow, or acceptance criteria, the user/domain owner must confirm the change before developer implementation, tester acceptance, or release-readiness work proceeds.

10. Design the smallest full cycle.
   Define `goal -> input -> action -> observation -> update -> reuse`. For build-oriented Loops, use explicit lifecycle stages such as `design -> develop -> test -> release -> operate -> review -> update` instead of collapsing development and testing.

11. Choose observation and update mechanisms.
   Define what gets recorded, who reviews it, what signal shows improvement, and which artifact changes before the next round. Control document count per user/owner through `document-index.md`, with an explicit document budget, purpose, owner, status, and merge/archive decision for each managed document.

12. Scaffold and customize artifacts when useful.
   Use the script described in `references/artifact-pack.md`, then customize generated files for the user's scenario. Do not leave placeholders when the user gave enough context.

13. Stop at gates when confirmation is missing.
    Before moving past Loop design, ask the requester or domain owner to confirm the stage knowledge base and selected role set. Do not proceed to execution, development, testing, acceptance, or release when required confirmation is missing.

## Mandatory Governance Highlights

- Loop Manager manages the Loop system: role registry, cadence, fixed-time retrospectives, role health, resource status, role self-review, experience distillation, role advice, communication-efficiency review, role responsibility/skill optimization, blockers, risks, handoffs, goal dispatch, and feedback to Super Assistant.
- Loop Manager does not perform development, testing conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, or role-specific implementation.
- Loop Manager owns staged role splitting after project start. It should recommend creating, activating, merging, pausing, or closing roles when real evidence shows overloaded responsibilities, unclear authority, repeated handoff friction, missing expertise, parallel work needs, risk isolation needs, or workflow stages that can no longer be handled by the current small role set.
- Loop Manager must have default automatic distillation time nodes from project start: project-start baseline, task/stage completion checkpoint, weekly fixed retrospective by default, event-triggered review for blockers/role changes/major disagreements, and project-closure distillation.
- Loop Manager assists every active role in gradually optimizing its skills. It does not rewrite a role's professional judgment for it; it collects evidence, skill gaps, repeated failures, useful practices, and update proposals, then routes confirmed improvements into role workspaces, role charters, candidate-role requirements, templates, implementation covenant rules, or skill update candidates.
- Project manager/delivery coordinator is optional and separate from Loop Manager. Select it only when delivery scheduling, milestones, external dependencies, stakeholder reporting, or workflow coordination needs a separate owner.
- Every active role must sync status to the project owner at the dispatch-defined cadence and immediately on completion, blocker, handoff, return, or closure.
- Role/personnel/session changes are not complete until Loop Manager updates `role-registry.md`, notifies every other active role, and records the broadcast.
- Hard constraints are not preferences. A product, UI, workflow, scope, acceptance, risk, governance, or release change that requires user/domain-owner confirmation must be blocked by each downstream role until confirmation evidence is recorded.

## Output Shape

For a Loop-design answer, provide the Loop owner, Loop Manager, Loop Manager automatic distillation time nodes, role skill-evolution mechanism, hard constraint gates, initial minimal active role set, deferred candidate roles and split triggers, role categories, Loop object, minimum viable loop, key records, feedback/evaluation signals, update mechanism, first implementation order, selected/excluded roles, implementation covenant status, category workspaces, interaction evidence rule, disagreement/escalation path, risks, confirmation needed, and artifact path if files were created.

Keep the result concrete enough that the user can start building immediately.
