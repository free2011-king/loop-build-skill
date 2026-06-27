# Loop Role System

Read this reference when creating Loop roles, role workspaces, Codex sessions, implementation teams, Loop Manager duties, tool/skill readiness checks, role boundaries, advisor contributions, or role self-review rhythms.

## Contents

- [Role Creation Gate](#role-creation-gate)
- [Role Category Workspace Rule](#role-category-workspace-rule)
- [Early-Stage Role Minimalism](#early-stage-role-minimalism)
- [Existing Role Selection Gate](#existing-role-selection-gate)
- [Implementation Covenant](#implementation-covenant)
- [Document Governance And Index](#document-governance-and-index)
- [Demand Intake Role](#demand-intake-role)
- [Loop Manager](#loop-manager)
- [Default Loop Manager Distillation Time Nodes](#default-loop-manager-distillation-time-nodes)
- [Role Skill Evolution With Loop Manager](#role-skill-evolution-with-loop-manager)
- [Project-Type Workflow Governance](#project-type-workflow-governance)
- [Active Role Registry](#active-role-registry)
- [Goal Setting And Dispatch In Codex](#goal-setting-and-dispatch-in-codex)
- [Role Status Sync To Project Owner](#role-status-sync-to-project-owner)
- [Boundary And Handoff Rule](#boundary-and-handoff-rule)
- [Disagreement Resolution](#disagreement-resolution)
- [Interaction Documentation And Evidence](#interaction-documentation-and-evidence)
- [Tool And Skill Readiness](#tool-and-skill-readiness)
- [Advisor Contribution](#advisor-contribution)
- [Codex Session Rule](#codex-session-rule)

## Role Creation Gate

Create a role only when it is necessary to close the Loop, reduce meaningful risk, preserve reusable learning, or satisfy a confirmed project constraint. For each role, define:

- Position: why this role exists and what it is not.
- Authority boundary: what it may decide, modify, approve, or reject.
- Role category and workspace: folder ownership for the role category, concrete roles/sessions sharing that category, editable files, readable files, and handoff targets.
- Loop charter: goal, standard, constraints, inputs, outputs, records, evaluation signals, feedback signals, and update responsibility.
- Project-type workflow requirement: project type, workflow stage, required prior inputs, required outputs, status-sync cadence, quality gate, next handoff, and workflow steps this role must not skip.
- Required tools and skills: skills, tools, scripts, references, data access, permissions, readiness status, fallback, blocker, and owner.
- Advisor contribution: best-practice suggestions, risks, options, assumptions, and confirmation needs.
- Codex session: separate thread/session when Codex is used for an active concrete role or subagent, mapped back to its role-category workspace.

Do not create a role that only has a name, folder, or session.

## Role Category Workspace Rule

Every role category must have its own independent folder under `roles/`. A role category is a reusable responsibility type such as demand intake, product/workflow, development, testing/evaluation, governance/risk, Loop Manager, domain owner, or Super Assistant.

Multiple concrete roles, people, agents, or Codex sessions in the same category may share the same category folder when they have the same responsibility boundary and record type. For example, two developer sessions may both use `roles/development/` if both perform implementation work under the same authority boundary.

Create a separate folder only when a concrete role has a distinct category, separate authority boundary, separate ownership, separate records, or different confidentiality/access constraints. Do not create folders merely because there are multiple people, agents, sessions, or task instances in the same category.

Each category workspace should record:

- Category name and responsibility boundary.
- Concrete roles, agents, people, or sessions currently using the folder.
- Owned records and editable artifacts.
- Handoff targets for work outside the category boundary.
- Category-level self-review and reusable learning.

## Early-Stage Role Minimalism

At project start, keep the active role set small. Create the Loop Manager and usually 2-3 other active roles needed to clarify demand and run the next Loop round. Those role files or category workspaces may be separate for clarity; the constraint is role count and responsibility sprawl, not forcing multiple roles into one file. Do not activate product, project-management, architecture, development, testing, security, review, documentation, or governance roles merely because they exist in the candidate library.

Candidate roles may be listed in `team-formation.md`, `candidate-role-library.md`, `role-sessions.md`, or `role-workspaces.md` as deferred options. A listed candidate is not an active role until the user/domain owner confirms it or confirmation is explicitly delegated, the Loop Manager adds it to `role-registry.md`, its authority boundary and workspace are clear, and the role-change broadcast is recorded. If a role is active or explicitly prepared for confirmation, its file/workspace may be separate.

Use these split triggers before adding a specialized role:

- The current role set is overloaded or repeatedly blocked.
- A responsibility boundary becomes unclear or a role repeatedly acts outside its authority.
- A workflow stage requires specialized expertise, independent review, risk isolation, or parallel execution.
- Handoffs, status syncs, or evidence records show repeated friction that a clearer role boundary would reduce.
- Compliance, confidentiality, evidence integrity, or stakeholder needs require separate ownership.

The Loop Manager owns staged role splitting after project start. During fixed-time retrospectives and blocker reviews, it should recommend creating, activating, merging, pausing, closing, or combining roles based on evidence. A role split is complete only after registry update, workspace decision, all-role notification, and interaction evidence record.

## Existing Role Selection Gate

Before implementation begins, select roles from the existing reusable role library according to the project's confirmed needs and use cases. Existing role categories are the default source of implementation roles.

The Loop owner must prepare a role selection packet for user or domain-owner confirmation. The packet should include:

- Confirmed project needs or use cases that require role coverage.
- Selected existing roles and role categories.
- Why each selected role is necessary.
- Existing candidate roles intentionally excluded and why they are not needed now.
- Category workspace for each selected role.
- Authority boundary, handoff path, required records, and evidence expectations.
- Tool and skill readiness, substitutes, or blockers.

Do not proceed into implementation until the selected role set is confirmed by the user/domain owner or confirmation is explicitly delegated to the Loop owner. Prefer Loop Manager plus 2-3 other active roles and deferred candidates over a fully split team at project start. Create a new role only when no existing role category can cover the responsibility without creating unclear authority, record, evidence, or confidentiality boundaries.

## Implementation Covenant

Before implementation begins, the Loop Manager must create and maintain a project-level implementation covenant for all selected implementation roles. The covenant is separate from individual role charters: charters define each role, while the covenant defines how roles work together.

The covenant must include:

- Role boundary matrix: role category, ownership, decision authority, editable artifacts, must-not-do list, handoff triggers, and receiving roles.
- Communication content requirements: every role-to-role message must include sender role, receiver role, task/goal ID when available, interaction type, context, summary, requested action or decision, evidence/document links, evidence gaps, blocker/risk status, follow-up owner, deadline or next sync, and record location.
- Message type rules: handoff, question, answer, advice, role-status-sync, blocker, defect, acceptance feedback, decision request, disagreement, update proposal, and role-change-broadcast.
- Handoff package standards: required source materials, current state, completed work, open questions, acceptance criteria, known risks, evidence links, and next owner.
- Status-sync rules: cadence, completion-sync requirement, project owner receiver, and required fields.
- Evidence and record rules: where interactions are recorded and what counts as missing evidence.
- Boundary violation handling: what a role must do when work falls outside its authority.
- Disagreement and escalation path: direct role communication first, Loop Manager escalation for scope/risk/authority/schedule/resource issues, and user/domain-owner decision when needed.
- Covenant review/update rhythm: Loop Manager checks covenant quality during fixed-time retrospectives and updates it when communication friction, role overlap, role gaps, or repeated evidence gaps appear.

No implementation role should treat a task as execution-ready until the covenant exists, the relevant role boundaries are filled, communication content requirements are clear, and the covenant acceptance status is recorded.

## Document Governance And Index

To prevent document explosion, every concrete Loop project must maintain a single `document-index.md` as the source of truth for user-created and user-managed project documents. This index controls how many active documents each user, domain owner, or role owner creates and manages.

Before creating a new document, the responsible role must check `document-index.md` and decide whether the content can be added to an existing indexed document. Create a new document only when the content has a distinct purpose, owner, lifecycle, evidence boundary, confidentiality boundary, or handoff requirement that cannot be cleanly handled by an existing document.

`document-index.md` must track:

- User / owner / role responsible for the document.
- Document path or external link.
- Document type and purpose.
- Why this is a separate document instead of a section in an existing document.
- Related Loop stage, role category, task ID, or goal ID.
- Active / draft / merged / archived / superseded status.
- Last review date and next review date.
- Merge, archive, or delete candidate status.
- Evidence or handoff dependencies.

Loop Manager reviews the index during fixed-time retrospectives. If a user or role exceeds its project-defined document budget, Loop Manager must request a merge/archive decision before allowing more documents unless a new document is required by role boundary, evidence, compliance, confidentiality, or handoff needs.

## Demand Intake Role

Create the demand intake role before implementation roles. It owns rough demand, clarification, refinement, concrete use cases, open questions, acceptance criteria, confirmation status, and the first handoff to the Loop owner.

Each use case must include actor, scenario, trigger, preconditions, steps, expected output, measurable acceptance standard, constraints, exclusions, records, feedback signal, owner, and confirmation status.

When `grill-me` is available, demand intake must use it before declaring demand implementation-ready. Record grilling questions, exposed gaps, revised requirements, rejected assumptions, and confirmation needs in the demand intake workspace or `use-cases.md`.

## Loop Manager

Every concrete Loop project must have a Loop Manager from the very beginning of the project. Create it before demand intake and before implementation roles so it can maintain the Loop system as roles appear. Do not treat the Loop Manager as optional once a project becomes a concrete Loop project.

The Loop Manager is distinct from a project manager. The Loop Manager owns Loop governance: cadence, fixed-time retrospective rituals, status, risks, decisions, blockers, handoffs, major disagreement escalation, review rituals, role self-review, role advice summaries, role health checks, resource status, project-level reflection, the active role registry, experience distillation checks, communication-efficiency review, role responsibility optimization, role skill/tool improvement, and feedback to the Super Assistant. A project manager or delivery coordinator, when needed, owns ordinary delivery coordination such as milestones, timelines, external dependency chasing, and stakeholder status reporting.

The Loop Manager must not do development, testing conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, or role-specific implementation work. It asks the responsible role to act, tracks the handoff, and verifies whether the returned output satisfies the agreed gate.

The Loop Manager regularly checks each active role's health: readiness, workload, blockers, stale handoffs, resource gaps, tool/permission gaps, context decay, missing records, and whether the role's workspace has current evidence.

The Loop Manager regularly asks each active role to self-review conversations, outputs, and feedback, then distill standards, reusable experience, mistakes, surprises, unresolved questions, and update proposals into that role category's workspace. It checks that experience is actually written down, not just discussed.

The Loop Manager periodically prompts the user or domain owner with role advice summaries so the user can hear professional suggestions instead of only commands or status updates.

The Loop Manager must run fixed-time retrospectives at the cadence defined for the project, weekly by default when no cadence is specified. The retrospective must not be a generic status report: it must distill what changed, what was learned, and what should improve in the next cycle.

Each fixed-time retrospective must explicitly review user-to-role communication efficiency, role-to-role communication efficiency, handoff friction, repeated clarification loops, stale or missing status syncs, role responsibility overlap or gaps, role boundary confusion, role skill/tool gaps, role skill/tool upgrades, and whether each role's charter or workspace should be adjusted.

The Loop Manager records these findings as concrete improvement proposals: communication rule changes, handoff-template changes, role responsibility changes, role skill/tool readiness changes, role training/checklist updates, registry updates, candidate-role library updates, or skill/template update candidates.

The Loop Manager and Super Assistant must also track reusable role capability sources at the project cadence, monthly by default when no cadence is specified. Capability sources include ECC / Everything Claude Code, Claude Code plugins, local `.codex/plugins` metadata, available skills/tools, and trusted role references. A source change should update candidate roles only when it changes role responsibilities, activation triggers, skill/tool matches, evidence requirements, authority boundaries, handoff packages, or review gates. Record source, version/date when available, observed capability, proposed role-library change, owner, and status.

## Default Loop Manager Distillation Time Nodes

Every project-level Loop Manager starts with these automatic distillation time nodes unless the user or domain owner confirms a different cadence:

| Time Node | Default Trigger | Distillation Focus | Required Output |
| --- | --- | --- | --- |
| Project-start baseline | Immediately when the Loop project is created | Loop object, active roles, deferred roles, document budget, risk/resource baseline, communication rules, and first gates | Baseline entry in Loop Manager workspace and `role-registry.md` / `document-index.md` checks |
| Task or stage completion checkpoint | When a role completes a task, stage, handoff, or dispatch packet | What changed, evidence returned, status-sync quality, handoff quality, reusable learning, and next owner | Completion distillation note in `interaction-evidence-log.md` or the responsible role workspace |
| Weekly fixed retrospective | Weekly by default when no cadence is specified | Communication efficiency, role health, resource fit, responsibility boundaries, skill/tool gaps, reusable principles, and document growth | Retrospective summary, improvement proposals, and updated role/document records |
| Event-triggered review | Major blocker, role change, repeated handoff friction, major disagreement, failed gate, user correction, or material risk | Cause, affected roles, boundary change, communication update, role split/merge need, and prevention rule | Decision/conflict entry, role-registry update when needed, and all-role notification when roles change |
| Project-closure distillation | When a project, milestone, release, or Loop round closes | What became reusable, what should be archived, which roles should pause/close, and what skill/template/principle should update | Closure note, archive/merge decisions, and feedback to Super Assistant |

## Role Skill Evolution With Loop Manager

Every active role's skill requirements are living Loop artifacts. Do not treat role skills, tools, prompts, checklists, references, or working standards as fixed at role creation time.

Each active role must record skill-learning signals in its role-category workspace:

- Skill or tool that helped the role perform better.
- Missing skill, tool, reference, permission, or checklist that blocked or weakened the work.
- Repeated mistake, handoff failure, test failure, user correction, or quality gap linked to a skill issue.
- Better prompt, workflow, checklist, template, source, example, or validation method discovered during work.
- Proposed update to role charter, candidate-role library, implementation covenant, generated template, or reusable skill.
- Evidence for the update: task ID, interaction record, test output, review finding, user feedback, source link, or explicit evidence gap.

Loop Manager assists this evolution without taking over the role's expertise. It collects skill-learning signals during task/stage completion checkpoints, weekly fixed retrospectives, event-triggered reviews, role self-reviews, and project-closure distillation. It then converts validated signals into concrete updates:

- Role workspace updates for role-specific lessons, examples, checklists, and prompts.
- Role charter updates for responsibility boundaries, must-not-do rules, evidence standards, and skill/tool readiness.
- Candidate-role library updates when a skill changes activation triggers, required tools, knowledge base, handoff package, or review gate.
- Implementation covenant updates when communication, handoff, evidence, or escalation rules should change.
- Template/script/skill update candidates when the learning should affect future Loop projects.

Loop Manager must distinguish proposed, accepted, rejected, and applied skill updates. A skill update is not complete until the target artifact, owner, evidence, and next review point are recorded.

## Project-Type Workflow Governance

When a project manager / delivery coordinator is selected, every new project question, request, issue, or work item must be classified by project nature and routed through the complete workflow for that project type. The project manager / delivery coordinator owns delivery-flow completeness, milestone/dependency coordination, and stakeholder status for the selected project type. It does not replace Loop Manager, product owner, developer, tester, reviewer, domain owner, or governance roles.

For software development projects, the default complete workflow is:

```text
demand clarification -> product/workflow scope -> codebase exploration when needed -> architecture/design -> implementation -> testing/evaluation -> code review and specialized reviews as needed -> release/operation readiness -> review/update
```

Each role created for the Loop must include a project-type workflow requirement in its role charter and category workspace. The requirement must state which project workflow stage the role belongs to, what prior inputs it requires, what outputs and evidence it must produce, when it must sync status to the project owner, which quality gate applies, what the next handoff is, and which workflow steps it must not skip.

The Loop Manager checks that project-type workflow requirements exist and that the project manager / delivery coordinator is not bypassing the required workflow. If no project manager is selected, the Loop owner must still ensure the role charters contain project-type workflow requirements.

## Active Role Registry

When implementation roles are selected, confirmed, created, activated, paused, replaced, closed, or when their concrete person/agent/Codex session changes, the Loop Manager must maintain an active role registry. This registry is the source of truth for task dispatch and role management during implementation.

The registry must include:

- Role ID.
- Role name and role category.
- Concrete person, agent, or Codex session if known.
- Category workspace and editable artifacts.
- Authority boundary and must-hand-off targets.
- Required tools, skills, data, references, permissions, and readiness status.
- Role health, resource needs, stale handoffs, context gaps, and last self-review date.
- Current status such as proposed, confirmed, active, paused, blocked, replaced, or closed.
- Dispatch owner, current task, blockers, and last review/update time.

The Loop Manager must update the registry before the first implementation dispatch and after any role/personnel/session change. If a task appears to belong to a role that is not in the registry, the Loop Manager must either update the registry through the role-selection/confirmation path or record the task as blocked.

After any role is created, activated, paused, replaced, closed, or its concrete person/agent/Codex session changes, the Loop Manager must notify every other active role. The notification must state what changed, why it changed, effective time, affected authority boundaries, handoff impacts, records to update, and required actions. Record the broadcast in `interaction-evidence-log.md`; if the change affects a specific role's work, also record or summarize it in that role category's workspace. A role change is not complete until the registry update and all-role notification are both recorded.

## Goal Setting And Dispatch In Codex

Goal-setting interaction with the Loop Manager is important and should be used. It is a management input, not permission for the Loop Manager to execute role-specific work.

When the user gives the Loop Manager a goal in Codex, the Loop Manager must classify the message before acting:

- Goal setting: refine the goal into a goal contract and dispatch packet.
- Role dispatch: select the responsible active role from the role registry, then send the task packet to that role/session.
- Review/status: inspect returned evidence and gates.
- Escalation/decision: prepare options and ask the user/domain owner to decide.
- Direct execution request: if the work belongs to another role, convert it into a dispatch packet and hand it off.

The Loop Manager may create or update management artifacts in its own category workspace: active role registry, goal contract, task packet, dispatch log, status, blocker, risk, decision request, handoff, or review note.

The Loop Manager must not implement code, write tests, decide QA conclusions, redefine product scope, approve business acceptance, make governance decisions, release production work, or perform project-manager delivery execution.

Each dispatch packet must include:

- Task ID and goal.
- Target role ID from the active role registry.
- Target role/subagent/session.
- Role category, workspace, and authority boundary.
- Source materials, document links, artifact references, and evidence gaps.
- Required stage knowledge base and role knowledge base.
- Required tools/skills/readiness status.
- Inputs, expected outputs, definition of done, constraints, and non-goals.
- Quality gate, evidence requirements, due point, and return format.

If the target role is not registered, the Loop Manager records the packet as blocked until role selection or registry update is complete. If the target Codex role/session is registered but unavailable, the Loop Manager records the packet in the target role-category workspace or dispatch log, marks execution as blocked or waiting for role execution, updates the registry status, and reports that it has not performed the role's work.

## Role Status Sync To Project Owner

Every active role must sync task status to the project owner while work is flowing. The project owner defaults to the Loop owner / Super Assistant unless the user explicitly names another project owner.

The dispatch packet must define the status-sync cadence, completion-sync requirement, receiver, and record location. At minimum, a role must sync status:

- When it accepts or starts a dispatched task.
- At the cadence defined by Loop Manager for the task, stage, or risk level.
- When it becomes blocked, discovers a material risk, or needs a decision.
- Before handing off work to another role.
- Immediately after completing its assigned task, before return, closure, acceptance, or release decisions.

Each status sync must include task ID, goal ID, role ID, role category, current state, progress or completion status, completed work, evidence links or document paths, blockers, risks, next handoff, ETA or completion time, and decisions needed. Record the sync as `role-status-sync` in `interaction-evidence-log.md` and summarize it in the role category workspace. If a role finishes work without a completion sync to the project owner, the task is not ready to close.

The Loop Manager monitors missing or stale status syncs, records gaps, and asks the responsible role to update status. It must not perform the role's work to compensate for missing status.

## Boundary And Handoff Rule

Before acting, every role must identify its position, responsibility boundary, decision authority, editable artifacts, and required handoffs.

If a role needs to decide, perform work, or modify files, systems, tools, data, or artifacts outside its assigned responsibility, it must:

```text
state role position -> state boundary -> announce out-of-scope action -> stop local action -> hand off to responsible role/subagent -> record handoff -> review returned result
```

This rule applies even when no file modification is involved.

## Disagreement Resolution

Roles may communicate directly with each other to resolve ordinary disagreements about assigned tasks, handoffs, evidence, implementation approach, test interpretation, or working standards.

Record the discussion result in the relevant role-category workspace or handoff log when the decision changes work, standards, records, or next actions.

Escalate to the Loop Manager when a disagreement:

- Changes product scope, acceptance criteria, release readiness, governance/risk boundary, schedule, cost, resource allocation, or role authority.
- Blocks progress across roles.
- Has competing recommendations that cannot be reconciled quickly.
- Affects user/domain-owner commitments.
- Creates risk that one role would decide outside its authority.

The Loop Manager must not decide the substance of major disputes unless explicitly delegated. It prepares a decision packet with issue, roles involved, options, evidence, impact, recommendations, unresolved risks, and deadline, then sends it to the user or domain owner for decision.

## Interaction Documentation And Evidence

All role-to-role messages and interactions must be recorded in project documents. This applies to handoffs, advice, decisions, questions, answers, status updates, disagreement records, blocker reports, defect reports, test findings, acceptance feedback, implementation claims, and update proposals.

Use `interaction-evidence-log.md` as the project-level message ledger. A role may also duplicate or summarize relevant entries in its category workspace, but the interaction should remain traceable from the project-level log.

Each interaction record must include:

- Date/time.
- Sender role and receiver role.
- Interaction type.
- Summary of the message.
- Requested action, decision, or next step.
- Local document/material path, online document link, artifact reference, data source, log, test output, screenshot, ticket, pull request, or decision record when available.
- Evidence gap status when supporting material is missing.
- Follow-up owner.
- Status.

If no supporting material exists, the sender must first check `document-index.md`, then reuse or update an existing indexed document when possible. Create the smallest useful new document/material only when the index shows that no existing document can responsibly hold it; otherwise request it from the responsible role or mark the interaction as an evidence gap/blocker. Do not treat unrecorded role messages, unsupported summaries, or chat-only claims as implementation-ready Loop state.

## Tool And Skill Readiness

A role is not execution-ready until required skills, tools, scripts, references, data access, and permissions have been checked. Each missing item must be activated, installed, substituted, downgraded, or marked as a blocker with an owner.

Record readiness in team formation, role charters, implementation plan, or role-category workspace before the role begins execution.

## Advisor Contribution

Every role is also an expert advisor. It should enrich assigned work with best practices, risks, options, recommended standards, and improvement ideas.

Separate confirmed requirements from advisor recommendations, assumptions, risks, and questions. Advisor recommendations cannot silently become execution scope; important changes need confirmation.

## Codex Session Rule

When using Codex, treat each active role or subagent as a separate thread/session with its own role context and category workspace. The Super Assistant stays in the coordination session and sends scoped work to role sessions.

If thread creation is unavailable or not explicitly requested, still record the intended role-session mapping and keep role outputs separated by role-category workspace.
