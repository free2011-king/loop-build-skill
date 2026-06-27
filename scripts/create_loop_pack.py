#!/usr/bin/env python3
"""Scaffold a reusable Loop artifact pack."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    source_hash = hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or f"loop-{source_hash}"


def write_text(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"{path} already exists; pass --force to overwrite")
    path.write_text(content, encoding="utf-8")


def write_csv(path: Path, rows: list[list[str]], force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"{path} already exists; pass --force to overwrite")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Loop artifact pack.")
    parser.add_argument("name", help="Human-readable Loop name")
    parser.add_argument("--out", default="loops", help="Output parent directory")
    parser.add_argument("--type", default="general", help="Loop type, e.g. product, learning, research")
    parser.add_argument("--slug", help="Directory name to use instead of an auto-generated slug")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    loop_dir = Path(args.out) / (args.slug or slugify(args.name))
    loop_dir.mkdir(parents=True, exist_ok=True)
    role_workspaces = [
        ("demand-intake", "Demand intake role"),
        ("loop-manager", "Loop Manager"),
        ("super-assistant", "Super Assistant / Loop owner"),
        ("domain-owner", "User / domain owner"),
        ("product-workflow", "Product manager / workflow designer"),
        ("project-management", "Project manager / delivery coordinator"),
        ("development", "Developer / implementer"),
        ("testing-evaluation", "Tester / evaluator"),
        ("governance-risk", "Governance or risk owner"),
    ]

    write_text(
        loop_dir / "loop-design.md",
        f"""# {args.name} Loop Design

## Loop Type

{args.type}

## Loop Owner

Super Assistant

The Loop owner is responsible for driving the whole process from goal, input, action, observation, update, to reuse. The owner coordinates the needed project roles instead of treating the Loop as a one-step task.

## Participating Roles

- Demand intake role:
- Loop Manager:
- User / domain owner:
- Product manager / workflow designer:
- Project manager / delivery coordinator, if needed:
- Developer / implementer:
- Tester / evaluator:
- Governance or risk owner, if needed:

## Loop Object

What should improve after each round?

- 

## Minimum Viable Loop

```text
goal -> input -> action -> observation -> update -> reuse
```

## Goal

- 

## Refined Goal Standard

- Actionable:
- Testable:
- Quantified where useful:
- Bounded:
- Recordable:
- Owned:
- Reusable:
- Assumptions to confirm:

## Inputs

- 

## Actions

- 

## Observation Signals

- 

## Minimum Records

- 

## Update Mechanism

- 

## Reuse Rule

- 

## First Build Order

1. 
2. 
3. 

## Risks And Anti-Patterns

- 
""",
        args.force,
    )

    write_text(
        loop_dir / "loop-manager.md",
        f"""# {args.name} Loop Manager

Every Loop project must have a Loop Manager from project start, before demand intake and before implementation roles. The Loop Manager is distinct from a project manager: it governs the whole Loop system, not ordinary delivery logistics. It manages Loop rhythm and project-level reflection, maintains the active role registry during role creation and role/personnel/session changes, broadcasts role changes to every other active role, checks project-type workflow completeness, checks role health, checks resource status, checks whether each role has synced task status to the project owner at the required cadence and on completion, checks whether each role has distilled reusable experience into its workspace, receives goal-setting interactions in Codex, turns goals into dispatch packets, routes tasks against the registered role list, requires each role to run regular self-review, regularly collects each role's professional advice, handles major disagreement escalation, prompts the user or domain owner to consider advice and major decisions, then sends improvement feedback to the Super Assistant. The Loop Manager does not do development, testing conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, or role-specific implementation work.

## Role Charter

| Item | Definition |
| --- | --- |
| Role name | Loop Manager |
| Workspace | `roles/loop-manager/` |
| Codex thread/session | dedicated Loop Manager session when Codex is used |
| Owns | Active role registry, Loop cadence, role health checks, resource status checks, project-owner status sync checks, status, risks, decisions, blockers, handoffs, role self-review, experience distillation checks, role advice collection, user/domain-owner advice prompts, project reflection, feedback to Super Assistant |
| May edit | Loop Manager workspace, role-registry.md, project status, reflection records, role advice summaries, improvement proposals |
| Must not do | Development, implementation, test conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, role-specific execution |
| Must hand off | Implementation work, QA conclusions, business acceptance, governance decisions, release decisions, skill edits unless explicitly delegated |

## Management Cadence

| Cadence | Activity | Output |
| --- | --- | --- |
| Role creation, personnel/session adjustment, or role status change | Update active role registry with role ID, category, workspace, session, boundary, readiness, health, resources, and status; notify every other active role; record the notification | role-registry.md update, interaction-evidence-log.md broadcast record, affected role workspace updates |
| Each stage handoff | Check owner, input, output, records, gate | Handoff status |
| User sets a goal in Codex | Convert the goal into a goal contract and dispatch packet; route to responsible role/session; define project-owner status sync cadence and completion sync requirement | Goal dispatch log update |
| Weekly or cycle review | Review progress, blockers, risks, feedback, updates | Reflection summary |
| Each role message or interaction | Confirm the message is recorded in `interaction-evidence-log.md` or a named project document, and check whether it includes document/material paths, online links, artifact references, or explicit evidence gaps | Interaction/message log update |
| Project-owner status sync cadence | Check active roles sync task status to the project owner at the dispatch-defined cadence and immediately on completion, blocker, decision need, or handoff | role-status-sync record and stale-sync gap list |
| Role change broadcast | After a role is created, activated, paused, replaced, closed, or its person/agent/session changes, notify all other active roles with change summary, reason, effective time, boundary impact, handoff impact, and required action | Broadcast notification record |
| Project-type workflow completeness | For each new question/request/issue/work item, check that the project manager or Loop owner classified project nature, selected the full workflow, and wrote each role's workflow-stage requirement into its charter | Project workflow checklist and role charter updates |
| Role health cadence | Check each active role's readiness, workload, blockers, stale handoffs, context gaps, missing records, tool/permission/resource gaps, and last self-review | Role health report |
| Resource review cadence | Check people/agent/session availability, tool access, data/material readiness, time budget, external dependencies, and overloaded roles | Resource status report |
| Role self-review cadence | Require each active role to distill standards, feedback, experience, and update proposals from its conversations and outputs | Role self-review records |
| Experience distillation check | Verify each role's reusable experience, mistakes, surprises, and update proposals have been written into its category workspace or Loop artifacts | Experience distillation status |
| Role advice cadence | Ask active roles for best-practice suggestions, risks, options, assumptions, and confirmation needs; summarize them for the user or domain owner | Role advice summary and user decision requests |
| Before execution gates | Verify required artifacts and confirmations | Gate recommendation |
| After project learning | Send improvement proposal to Super Assistant | Skill/principle/template update candidate |
| Major role disagreement | Collect issue, options, evidence, impact, recommendations, and decision need; ask user/domain owner to decide | Decision packet and conflict log update |

## Project-Type Workflow Rule

When a project manager / delivery coordinator is selected, every new project question, request, issue, or work item must be classified by project nature and routed through the complete workflow for that project type. If no project manager is selected, the Loop owner performs this classification and Loop Manager checks that role charters contain the workflow requirements.

For software development, the default workflow is:

```text
demand clarification -> product/workflow scope -> codebase exploration when needed -> architecture/design -> implementation -> testing/evaluation -> code review and specialized reviews as needed -> release/operation readiness -> review/update
```

| Date | Work Item | Project Type | Required Workflow | Project Manager / Owner | Roles With Workflow Requirement | Missing Stage / Gap | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | software / product / agent / workflow / research / other |  | Project manager / delivery coordinator or Super Assistant |  |  |  |

## Role Boundary Rule

Loop Manager manages the system of work; it does not perform the specialized work. When it detects work outside its position, it must hand off instead of doing it.

| Out-of-Scope Work | Responsible Role |
| --- | --- |
| Development or implementation | Developer / implementer |
| Test design or test conclusion | Tester / evaluator or QA role |
| Business acceptance or release decision | User / domain owner |
| Governance, compliance, approval, or permission boundary | Governance or risk owner |
| Delivery scheduling, milestone logistics, stakeholder status reporting | Project manager / delivery coordinator, when this optional role is selected |
| Skill file edits | Super Assistant unless explicitly delegated |

## Goal Setting Dispatch Rule

Goal-setting with Loop Manager is a valid and important Codex interaction. It is not permission for Loop Manager to execute developer, tester, product, governance, release, or other role-specific work.

When the user sets a goal, Loop Manager must:

1. Classify the interaction as goal setting, role dispatch, review/status, escalation/decision, or direct execution request.
2. Convert goal-setting into a goal contract.
3. Select the responsible role from `role-registry.md`; if no registered role fits, record a blocker or initiate role-selection confirmation.
4. Create a dispatch packet for the responsible role/session.
5. Include role ID, role category, workspace, authority boundary, source materials/links, evidence requirements, tool/skill readiness, definition of done, return format, project owner, status-sync cadence, and completion-sync requirement.
6. Route the packet to the responsible role/session, or record a blocker if the session is unavailable.
7. Update role registry and dispatch status while the task moves through waiting, active, blocked, returned, accepted, or closed.
8. Review returned evidence after the responsible role acts.

If the responsible role is not registered, Loop Manager records the packet as blocked until the role registry is updated through role selection or confirmation. If the responsible role/session is registered but unavailable, Loop Manager records the packet in `goal-dispatch-log.md` and the target role workspace, updates the role registry status, then reports waiting/blocked. It must not perform the role's work itself.

| Date | User Goal | Classified As | Registry Role ID | Target Role / Session | Dispatch Packet | Status | Blocker |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |

## Role Change Broadcast

A role creation, activation, pause, replacement, closure, or concrete person/agent/session adjustment is not complete until Loop Manager has updated `role-registry.md`, notified every other active role, and recorded the broadcast in `interaction-evidence-log.md`. If the change affects a role's current work, also record or summarize it in that role category workspace.

| Date | Change ID | Changed Role ID | Change Type | Summary | Reason | Effective Time | Roles Notified | Boundary / Handoff Impact | Required Action | Interaction Record | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | created / activated / paused / replaced / closed / personnel-session-change |  |  |  | all active roles except changed role / all active roles |  |  | interaction-evidence-log.md | draft |

## Project Owner Status Sync

Every active role must sync task status to the project owner while work is flowing. The project owner defaults to the Loop owner / Super Assistant unless the user names another project owner. Completion sync is mandatory before handoff, return, closure, or acceptance.

| Date | Task ID | Role ID | Role | Project Owner | Sync Type | Current State | Completed Work / Progress | Evidence | Blocker / Risk | Next Handoff | Decision Needed | Next Sync Due | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Super Assistant / Loop owner | start / periodic / blocker / handoff / completion | waiting / active / blocked / completed / returned |  |  |  |  |  |  | draft |

## Project Status

| Date | Stage | Status | Blocker | Risk | Decision Needed | Owner |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## Role Health Checks

| Date | Role ID | Role | Health Signal | Blocker / Stale Handoff / Context Gap | Resource Need | Last Self-Review | Experience Distilled? | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | healthy / warning / blocked |  |  |  | yes / no |  |

## Resource Status

| Date | Resource Type | Needed By Role | Available? | Gap / Constraint | Owner | Next Check |
| --- | --- | --- | --- | --- | --- | --- |
|  | people / agent / session / tool / data / permission / budget / dependency |  | yes / no / partial |  |  |  |

## Reflection Log

| Date | Evidence | What Changed | Loop Weakness | Proposed Improvement | Send To Super Assistant? |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Role Self-Review Tracker

| Date | Role | Workspace | Conversation / Work Reviewed | Standards Distilled | Feedback Distilled | Experience Distilled | Update Proposal | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

## Role Advice Summary

Loop Manager uses this section to avoid one-way command management. Regularly collect each active role's advice, then prompt the user or domain owner with options and tradeoffs when advice affects scope, standards, risk, or next action.

| Date | Role | Advice / Best Practice | Risk Or Tradeoff | Needs User / Domain Confirmation? | Decision |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Disagreement Escalation

Roles should communicate directly first to resolve ordinary disagreements about assigned work, handoff content, evidence, standards, implementation approach, or test interpretation. Escalate to Loop Manager when the disagreement changes scope, acceptance criteria, risk boundary, schedule, resource allocation, role authority, release readiness, or cannot be resolved quickly.

Loop Manager prepares the decision packet; the user or domain owner decides major issues.

| Date | Roles Involved | Issue | Options | Evidence | Impact | Recommendation | User / Domain Decision | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

## Interaction Message Review

Loop Manager checks that every role-to-role message and interaction is recorded in `interaction-evidence-log.md` or another named project document. Handoffs, advice, defect reports, decisions, questions, answers, status updates, acceptance feedback, and implementation claims must include detailed supporting material when available: local document/material path, online document link, artifact reference, data source, logs, test output, screenshots, tickets, pull requests, or decision records.

| Date | Interaction Type | Sender | Receiver | Message Summary | Document / Material / Online Link | Evidence Gap? | Follow-Up Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

## Feedback To Super Assistant

Use this section when project learning should update Loop Builder, local Loop principles, templates, scripts, or role definitions.

| Date | Feedback | Suggested Artifact To Update | Reason | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
""",
        args.force,
    )

    write_text(
        loop_dir / "team-formation.md",
        f"""# {args.name} Team Formation

Create the Loop Manager first at project start. Then create the demand intake role and select implementation roles from the existing reusable role library according to confirmed project needs and use cases. Do not prebuild roles, sessions, folders, or skills that the demand does not require. Create a new role only when no existing role category can responsibly cover the work.

## Demand Intake Role

| Item | Definition |
| --- | --- |
| Role name | Demand intake role |
| Workspace | `roles/demand-intake/` |
| Codex thread/session | dedicated intake session if Codex is used; otherwise current coordination session until team confirmation |
| Owns | Initial demand record, rough-to-executable refinement, open questions, acceptance criteria, first handoff |
| May edit | Demand intake workspace and confirmed demand artifacts |
| Must hand off | Implementation, testing, release, governance, and domain acceptance |

## Demand Intake Record

| Field | Value |
| --- | --- |
| User request |  |
| Refined demand |  |
| Goal |  |
| Success standard |  |
| Constraints |  |
| Use cases | See `use-cases.md` |
| Open questions |  |
| Confirmation status | draft |

## Advisor Contribution Requirement

Every active role is also an expert advisor. Roles are organized by role category; multiple concrete roles or sessions in the same category can share one category workspace when their boundary is the same. Each role must enrich its assigned work with best-practice suggestions, risks, options, recommended standards, assumptions, and confirmation needs. Keep confirmed requirements separate from advisor recommendations. Important advice cannot become execution scope until the user, domain owner, or delegated Loop owner confirms it.

Demand intake must proactively suggest useful use cases, measurable acceptance standards, risk boundaries, and anti-patterns to avoid.

## Project-Type Workflow Classification

For every new project question, request, issue, or work item, classify the project nature and choose the full workflow before creating or adjusting roles. When the project manager / delivery coordinator is selected, it owns delivery-flow completeness for the project type. If no project manager is selected, the Loop owner performs this classification and Loop Manager checks it.

Software development default workflow:

```text
demand clarification -> product/workflow scope -> codebase exploration when needed -> architecture/design -> implementation -> testing/evaluation -> code review and specialized reviews as needed -> release/operation readiness -> review/update
```

| Work Item / Question | Project Type | Required Workflow | Project Manager / Owner | Workflow Stages Needed | Roles Required By Stage | Confirmation Status |
| --- | --- | --- | --- | --- | --- | --- |
|  | software / product / agent / workflow / research / other |  | Project manager / delivery coordinator or Super Assistant |  |  | draft |

## Existing Role Selection

Select from existing reusable roles before creating any new role. The selected implementation role set must be confirmed by the user or domain owner before execution.

| Project Need / Use Case | Selected Existing Role | Role Category | Why Needed | Category Workspace | Authority Boundary | Required Tools / Skills | Readiness / Blocker | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | draft |

## Excluded Candidate Roles

Record existing roles that are not selected for this Loop round so the team stays intentionally small.

| Candidate Role | Role Category | Exclusion Reason | Reconsider Trigger | Confirmed By |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Implementation Team Proposal

Add only roles required by the confirmed demand and selected role set.

| Role Category | Role / Subagent | Needed? | Reason | Required Skill(s) | Category Workspace | Codex Thread / Session | Trigger | Inputs | Outputs | Gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| loop-manager | Loop Manager | Yes | Govern the whole Loop, role registry, role health, resources, experience distillation, and project-level reflection | loop-builder | `roles/loop-manager/` | dedicated Loop Manager session when Codex is used | Always, from project start | Loop artifacts, role status, feedback, resource needs | Role registry, health report, resource report, reflection, improvement proposals | Feedback sent to Super Assistant when needed |
| super-assistant | Super Assistant / Loop owner | Yes | Own and coordinate the Loop | loop-builder | `roles/super-assistant/` | current coordination session | Always | Confirmed demand | Coordination, handoff, review | Loop artifacts updated |
| project-management | Project manager / delivery coordinator | Candidate | Coordinate delivery milestones, timeline, external dependencies, stakeholder status, and delivery rituals when needed | project management / delivery coordination | `roles/project-management/` | dedicated project-management session when needed | Delivery coordination cannot be cleanly owned by another role | Confirmed plan, dependencies, milestones | Delivery status, dependency tracker, stakeholder summary | Delivery logistics are visible and not confused with Loop governance |
| product-workflow | Product manager / workflow designer | Candidate | Define product scope, user value, workflow, acceptance standards, and release slices | loop-builder; grill-me when refining scope | `roles/product-workflow/` | dedicated product role session when needed | Product or workflow ambiguity exists | Confirmed demand, use cases, domain constraints | Product spec, workflow, acceptance criteria, scope decisions | User/domain-owner confirms scope and standards |
| development | Developer / implementer | Candidate | Build the agreed product, workflow, integration, or automation | language/framework skills; repo tools; test runner | `roles/development/` | dedicated developer session when implementation starts | Development work is approved | Product spec, stage KB, implementation plan | Code/config/scripts, build notes, implementation evidence | Tests or review artifacts are ready for tester |
| testing-evaluation | Tester / evaluator | Candidate | Verify behavior, acceptance standards, quality, regressions, and release readiness evidence | test strategy; framework test tools; evaluation tools | `roles/testing-evaluation/` | dedicated tester session when review starts | Testable output exists | Use cases, acceptance criteria, implementation evidence | Test plan, findings, pass/fail evidence, quality risks | Release/acceptance decision has evidence |
|  |  |  |  |  |  |  |  |  |  |

## Role Loop Charter Requirement

Every role created for this Loop must define:

- Role position:
- Role category: what this role exists to do, and what it must not do.
- Project-type workflow requirement: project type, workflow stage, required prior inputs, required outputs, status-sync duty, quality gate, next handoff, and steps this role must not skip.
- Goal.
- Implementation standard.
- Constraints.
- Inputs.
- Outputs.
- Records.
- Evaluation / feedback signals.
- Advisor contribution: best-practice suggestions, risks, options, assumptions, and confirmation needs.
- Required tools and skills, with readiness status.
- Update responsibility.
- Authority boundary.
- Role category and category workspace.
- Handoff rules.

Do not treat a role as valid until its boundary is concrete enough to decide whether a requested action belongs to that role or must be handed off.

## Skill Installation / Activation Plan

Each role must use suitable tools and skills. Do not start role execution until required skills, tools, data access, scripts, references, and permissions are checked.

| Role / Subagent | Skill Needed | Tool / Access Needed | Available? | Install / Activate / Substitute Action | Fallback | Blocker? | Owner | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Demand intake role | loop-builder; grill-me | project context; user/domain input | check local skills and context | Install `grill-me` from `mattpocock/skills` if missing; use before handoff | Run manual grilling questions if skill unavailable | yes if no demand context | Super Assistant | Grill rough demand, assumptions, standards, and proposed use cases before treating demand as implementation-ready |
| Product manager / workflow designer | loop-builder; grill-me when scope is unclear | user/domain input; product references; analytics or process evidence if available | check project context | Activate product/spec/design skills if available | Use structured PRD/use-case checklist | yes if no domain decision-maker | Product manager / workflow designer | Convert use cases into scope, workflow, standards, and release slices |
| Project manager / delivery coordinator | project management / delivery coordination | milestone context; dependency owners; stakeholder channels | check project context | Activate project tracking tools if available | Use lightweight delivery log | no unless delivery coordination is required | Project manager / delivery coordinator | Coordinate delivery logistics without replacing Loop Manager |
| Developer / implementer | framework/language/repo skills | code repo; package manager; dev server; test runner; logs | check repo and permissions | Activate/install required coding skills and toolchain | Implement smallest verifiable slice or mark blocker | yes if repo/tool access missing | Developer / implementer | Build only confirmed scope with evidence |
| Tester / evaluator | testing/evaluation skills | test runner; acceptance criteria; test data; browser/API tools if needed | check repo and environment | Activate/install required testing tools | Manual checklist with recorded evidence | yes if no runnable artifact or acceptance criteria | Tester / evaluator | Verify behavior independently from development |
|  |  |  |  |  |  |  |  |  |

## User Confirmation Of Role Selection

- [ ] Demand intake role is accepted.
- [ ] Selected existing implementation roles are accepted.
- [ ] Excluded candidate roles and exclusion reasons are accepted.
- [ ] New roles, if any, are justified because no existing role category can cover the work.
- [ ] Required skills are accepted.
- [ ] Tool and skill readiness has been checked for every active role.
- [ ] Role categories, category workspaces, shared-folder rules, and Codex sessions are accepted.
- [ ] Authority boundaries and first handoff path are accepted.
- [ ] Role advisor contribution and confirmation rules are accepted.
- [ ] Proceed to implementation planning.

## Confirmation

- Confirmation date:
- Confirmation evidence:
- Decision: draft
""",
        args.force,
    )

    write_text(
        loop_dir / "candidate-role-library.md",
        f"""# {args.name} Candidate Role Library

Use this library before creating project roles. Start from these existing reusable role presets for software, product, Agent, workflow, or digital-employee Loops. Select roles according to confirmed project needs and use cases, ask the user or domain owner to confirm the selected implementation role set, then activate only the roles needed by the confirmed plan.

## Selection Workflow

1. Start from confirmed project needs and use cases.
2. Match each need to an existing candidate role and role category.
3. Select the smallest role set that can cover the work without unclear authority, evidence, record, or confidentiality boundaries.
4. List candidate roles that are not selected and explain why they are unnecessary for this Loop round.
5. Prepare a confirmation packet with selected roles, excluded candidates, category workspaces, authority boundaries, handoff paths, required tools/skills, readiness status, and blockers.
6. Ask the user or domain owner to confirm the selected role set before implementation.
7. Create a new role only when no existing role can responsibly cover the confirmed need.

## Activation Rule

Apply `如无必要，勿增实体`: a candidate role is not active until the implementation plan gives it a concrete goal, authority boundary, role category, category workspace, tools/skills, knowledge base, records, gates, and handoff rules.

## Reusable Candidate Roles

| Candidate Role | Role Category | Default Position | Activate When | Must Not Do | Default Category Workspace | Codex Session |
| --- | --- | --- | --- | --- | --- | --- |
| Product manager / workflow designer | product-workflow | Convert confirmed use cases into product scope, workflow, acceptance standards, and release slices | Product value, workflow, scope, or acceptance standard is unclear | Implement code, declare tests passed, approve business acceptance, or silently expand scope | `roles/product-workflow/` | Dedicated product role session |
| Developer / implementer | development | Build the confirmed technical slice and provide implementation evidence | Confirmed scope needs code, configuration, integration, automation, or platform changes | Redefine scope, declare QA passed, approve release, or bypass governance | `roles/development/` | Dedicated developer session |
| Tester / evaluator | testing-evaluation | Verify behavior against use cases, acceptance standards, regressions, and quality gates | Runnable artifact or reviewable implementation exists | Implement fixes silently, approve business acceptance, or rewrite scope | `roles/testing-evaluation/` | Dedicated tester session |
| Loop Manager | loop-manager | Govern the whole Loop: role registry, cadence, blockers, handoffs, role health checks, resource status, experience distillation, role self-review, role advice, reflection, and feedback to Super Assistant | Always for concrete Loop projects; created at project start before demand intake and implementation roles | Do development, testing conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, or role-specific execution | `roles/loop-manager/` | Dedicated Loop Manager session |
| Project manager / delivery coordinator | project-management | Classify each new question/request by project nature and coordinate the complete workflow for that project type, including milestones, timeline, cross-team dependencies, stakeholder status, and delivery rituals | Delivery scheduling, external dependencies, stakeholder reporting, multi-team coordination, or project-type workflow completeness needs a dedicated owner | Govern Loop learning, maintain role health, replace Loop Manager, decide product scope, do implementation, declare QA pass, approve release, own experience distillation, or skip required project-type workflow stages | `roles/project-management/` | Dedicated project-management session when needed |


## Claude Code Feature Development Role Patterns

These software-development role candidates are derived from the locally available Claude Code official `feature-dev`, `code-review`, `pr-review-toolkit`, `claude-code-setup`, `frontend-design`, and `security-guidance` plugins. Treat them as reusable role options, not mandatory roles. Activate them only when the confirmed use case needs their responsibility boundary.

The core development pattern learned from Claude Code is:

```text
discover requirements -> explore codebase -> clarify gaps -> design architecture -> implement -> review quality -> summarize decisions and next steps
```

## Project-Type Workflow Defaults

When project manager / delivery coordinator is selected, each new project question, request, issue, or work item must be classified by project nature and routed through the complete workflow for that type.

For software development, use this default lifecycle unless the user confirms a narrower lifecycle:

```text
demand clarification -> product/workflow scope -> codebase exploration when needed -> architecture/design -> implementation -> testing/evaluation -> code review and specialized reviews as needed -> release/operation readiness -> review/update
```

Every selected role's charter must state its workflow stage, required prior inputs, required outputs/evidence, status-sync duty to the project owner, quality gate, next handoff, and non-skippable workflow steps.

## Extended Software Development Candidates

| Candidate Role | Role Category | Default Position | Activate When | Must Not Do | Default Category Workspace |
| --- | --- | --- | --- | --- | --- |
| Codebase explorer / implementation researcher | code-exploration | Trace existing implementation, entry points, call chains, data flow, dependencies, conventions, and key files before design or changes | Existing codebase is unfamiliar, feature touches multiple modules, or implementation patterns must be discovered | Design final architecture, implement changes, approve quality, or decide product scope | `roles/code-exploration/` |
| Software architect / technical designer | architecture-design | Convert confirmed requirements and codebase findings into an implementation blueprint with component design, data flow, files to change, tradeoffs, and build sequence | Feature requires architecture decisions, new abstractions, integrations, or cross-module changes | Implement code without approval, override product scope, declare QA pass, or skip codebase evidence | `roles/architecture-design/` |
| Code reviewer / quality reviewer | code-review | Review changed code for bugs, project guideline compliance, maintainability, high-confidence correctness issues, and actionable fixes | Code has been written or a PR/diff is ready for review | Rewrite scope, perform business acceptance, make release decisions, or report low-confidence noise as blockers | `roles/code-review/` |
| Test writer / test coverage analyst | test-engineering | Design or assess tests for behavior, edge cases, regressions, negative paths, and critical business logic coverage | New functionality, changed logic, low coverage, or PR readiness needs test confidence | Declare product acceptance, rewrite implementation silently, or chase coverage metrics without risk rationale | `roles/test-engineering/` |
| Security reviewer | security-review | Review auth, permissions, secrets, injection, XSS, SSRF, path traversal, deserialization, data exposure, and high-risk flows | Auth, payments, PII, external input, credentials, file/network access, or security-sensitive code is involved | Approve governance or business risk alone, implement unrelated refactors, or expose secrets in records | `roles/security-review/` |
| Error-handling / reliability auditor | reliability-error-handling | Find silent failures, weak catch blocks, hidden fallbacks, poor logging, retry issues, and non-actionable user errors | Changes include try/catch, fallback behavior, async operations, external APIs, jobs, or critical user flows | Replace QA, product, or security approval; change behavior without responsible owner confirmation | `roles/reliability-error-handling/` |
| Type design / domain model analyst | type-design | Review type boundaries, invariants, encapsulation, illegal states, validation, and domain model clarity | New domain types, schemas, DTOs, state machines, permissions, or refactors introduce important invariants | Force over-engineered types, change runtime behavior silently, or approve business semantics | `roles/type-design/` |
| Code simplifier / refactoring reviewer | code-quality-refinement | Improve clarity, reduce unnecessary complexity, remove duplication, and align modified code with local conventions while preserving behavior | Implementation works but feels complex, duplicated, deeply nested, clever, or hard to maintain | Change feature behavior, broaden scope, or refactor unrelated code | `roles/code-quality-refinement/` |
| Performance analyzer | performance-analysis | Identify bottlenecks, N+1 queries, expensive loops, memory leaks, hot paths, caching needs, and measurement gaps | Performance is a requirement, high-traffic paths change, database-heavy code changes, or users report slowness | Prematurely optimize without evidence, bypass correctness/security, or invent unsupported performance claims | `roles/performance-analysis/` |
| UI / frontend reviewer | frontend-ux | Review frontend implementation for accessibility, responsive behavior, visual hierarchy, interaction quality, and user-facing polish | User-facing UI, components, forms, dashboards, or frontend-heavy work is included | Decide product scope, implement backend behavior, or accept release alone | `roles/frontend-ux/` |
| API documenter / technical documentation role | technical-documentation | Produce or verify API docs, OpenAPI specs, endpoint behavior, integration notes, and developer-facing documentation | APIs, SDKs, MCP tools, public interfaces, or integration contracts are created or changed | Invent behavior not present in code, approve implementation quality, or replace tests | `roles/technical-documentation/` |
| Dependency updater / migration helper | dependency-migration | Plan and execute dependency updates, framework migrations, compatibility checks, incremental rollout, and rollback notes | Dependencies are outdated, security advisories exist, major upgrades are needed, or framework migration is planned | Upgrade production-critical dependencies without tests, ignore compatibility, or change feature scope | `roles/dependency-migration/` |

## Skill / Tool / Knowledge Matching

| Candidate Role | Best-Practice Skill Match | Tool Match | Knowledge Base To Prepare | Core Records |
| --- | --- | --- | --- | --- |
| Product manager / workflow designer | `loop-builder`; `grill-me` when scope is rough; product/spec/design skills when available | User interviews, domain references, analytics/process evidence, diagram/spec tools | Goals, non-goals, personas/actors, use cases, workflow, acceptance standards, constraints, release slicing principles | Product decisions, assumptions, tradeoffs, scope changes, confirmation evidence |
| Developer / implementer | Framework/language/repo skills; code review and security skills when relevant | Repository, package manager, dev server, test runner, logs, debugger, CI output | Architecture, coding standards, repo conventions, integration contracts, environment setup, error handling, rollback notes | Changed files, commands run, test output, implementation notes, blockers |
| Tester / evaluator | Testing/evaluation skills; browser/API/performance/security tools when relevant | Test runner, browser automation, API client, fixtures/test data, logs, acceptance checklist | Test strategy, acceptance criteria, regression areas, data setup, quality gates, known risks | Test plan, pass/fail results, defect reports, evidence, regression notes |
| Loop Manager | `loop-builder`; Loop governance and retrospection practices | Role registry, health check tracker, resource log, handoff tracker, decision log, risk log, review cadence | Loop object, role map, handoff rules, health signals, resource thresholds, self-review prompts, experience distillation standards, improvement principles | Status, blockers, decisions, risk log, handoff log, role health report, resource report, role advice summary, reflection updates |
| Project manager / delivery coordinator | project management and delivery coordination practices; software delivery workflow when project type is software | Status board, milestone plan, dependency tracker, stakeholder update log, workflow checklist | Project type, required lifecycle stages, milestones, timeline, dependencies, delivery rituals, stakeholder communication needs | Delivery status, workflow stage map, milestone risks, dependency updates, stakeholder summaries |


## Extended Software Skill / Tool / Knowledge Match

| Candidate Role | Best-Practice Skill Match | Tool Match | Knowledge Base To Prepare | Core Records |
| --- | --- | --- | --- | --- |
| Codebase explorer / implementation researcher | code exploration, repo analysis, architecture mapping | Repository search, git history, dependency graph, logs, docs | Entry points, call chains, data flow, module boundaries, similar features, key files | Exploration notes, file:line references, dependency map, assumptions, gaps |
| Software architect / technical designer | architecture design, system design, framework-specific skills | Repo, diagrams/spec tools, ADR templates, prior patterns | Existing patterns, integration contracts, component responsibilities, data flow, rollout plan | Architecture decision, tradeoffs, implementation blueprint, risk notes |
| Code reviewer / quality reviewer | code review, project convention review | git diff, linters, type checker, test output, CLAUDE/AGENTS rules | Project rules, review thresholds, severity model, known risky areas | Findings, confidence scores, file:line references, fix suggestions |
| Test writer / test coverage analyst | testing/evaluation skills | Test runner, fixtures, coverage tools, browser/API tools | Test strategy, behavior contracts, edge cases, regression matrix | Test plan, test cases, coverage gaps, pass/fail evidence |
| Security reviewer | security review, threat modeling | SAST/dependency scanners, secret scanners, auth logs, diff review | Threat model, sensitive data flows, authz/authn rules, forbidden patterns | Security findings, exploit path, severity, mitigation, residual risk |
| Error-handling / reliability auditor | reliability review, error-handling standards | Logs, tracing, job queues, API clients, failure fixtures | Error taxonomy, logging rules, retry/fallback policy, user error standards | Silent failure findings, error paths, logging gaps, fallback decisions |
| Type design / domain model analyst | type design, domain modeling | Type checker, schema validators, model definitions | Invariants, state transitions, validation boundaries, illegal states | Type ratings, invariant list, enforcement gaps, recommended changes |
| Code simplifier / refactoring reviewer | refactoring, maintainability review | Diff, complexity checks, local style rules | Local conventions, refactoring constraints, behavior preservation rules | Simplification notes, before/after rationale, unchanged behavior evidence |
| Performance analyzer | performance profiling, database optimization | Profilers, query logs, benchmarks, tracing, load tests | Hot paths, performance targets, baseline metrics, caching rules | Bottleneck findings, benchmark evidence, optimization plan, tradeoffs |
| UI / frontend reviewer | frontend design, accessibility, UX review | Browser, Playwright, accessibility tools, screenshots | UI standards, accessibility rules, responsive breakpoints, design references | UI findings, screenshots, accessibility issues, responsive evidence |
| API documenter / technical documentation role | API documentation, technical writing | OpenAPI tools, route scanner, docs generator, examples | API contracts, request/response schemas, auth rules, error codes | API docs, examples, changelog notes, doc gaps |
| Dependency updater / migration helper | migration planning, dependency management | Package manager, changelogs, test runner, lockfile diff | Version map, compatibility notes, migration sequence, rollback plan | Upgrade plan, changed dependencies, test evidence, rollback notes |


## Extended Software Handoffs

| From | To | Trigger | Handoff Package |
| --- | --- | --- | --- |
| Demand intake | Codebase explorer / implementation researcher | Requirements are confirmed but repo patterns are unknown | Confirmed use cases, repo area, questions, constraints |
| Codebase explorer / implementation researcher | Software architect / technical designer | Existing patterns, key files, and implementation paths are mapped | Exploration notes, file:line references, dependency map, risks, open questions |
| Software architect / technical designer | Developer / implementer | Architecture and build sequence are confirmed | Architecture decision, files to modify, data flow, tests needed, risks |
| Developer / implementer | Code reviewer / quality reviewer | Implementation diff is ready | Changed files, run commands, known risks, test output |
| Developer / implementer | Test writer / test coverage analyst | New behavior or changed logic needs coverage | Use cases, implementation notes, changed files, behavior contracts |
| Developer / implementer | Security reviewer | Security-sensitive code changed | Threat-relevant diff, data flow, auth/payment/PII context, secrets policy |
| Developer / implementer | Error-handling / reliability auditor | Error handling, fallback, async, job, or external API paths changed | Failure paths, logs, fallback policy, test evidence |
| Developer / implementer | Performance analyzer | Hot path, database, or performance-critical code changed | Baseline metrics, changed files, expected performance target |
| Developer / implementer | UI / frontend reviewer | User-facing UI changed | Screenshots/URL, design context, interaction notes, accessibility expectations |
| Developer / implementer | API documenter / technical documentation role | Public API, SDK, endpoint, or integration contract changed | Route/schema changes, examples, auth/error behavior, version notes |
| Code reviewer / quality reviewer | Code simplifier / refactoring reviewer | Code is correct but too complex or inconsistent | Review findings, changed files, behavior preservation constraints |
| Any software review role | Loop Manager | Review changes scope, risk, schedule, authority, release readiness, or cannot be resolved quickly | Finding, evidence, impact, options, recommendation, decision needed |

## Interaction Documentation And Evidence

Every role-to-role message must be recorded in `interaction-evidence-log.md` or another named project document. Every handoff package must include the detailed material needed by the receiver: local document/material path, online document link, artifact reference, data source, log, test output, screenshot, ticket, pull request, or decision record.

If a role only has a summary, it must either attach/source the supporting material, create the smallest useful document, or mark the handoff as an evidence gap. Do not use chat-only or unrecorded role messages as implementation-ready state.

## Disagreement Resolution

Roles should communicate directly first when they disagree about assigned work, evidence, standards, implementation approach, test interpretation, or handoff content.

Escalate to the Loop Manager when the disagreement changes scope, acceptance criteria, risk boundary, schedule, resource allocation, role authority, release readiness, or cannot be resolved quickly. The Loop Manager records the competing options and impact, then asks the user or domain owner to decide.

## Reuse Checklist

- [ ] Chosen candidates are necessary for confirmed use cases and project needs.
- [ ] Non-selected candidate roles have explicit exclusion reasons.
- [ ] User/domain-owner confirmation was obtained for the selected implementation role set.
- [ ] Each active role has a completed Loop charter.
- [ ] Each active role has a project-type workflow requirement with project type, workflow stage, required inputs, outputs/evidence, quality gate, status-sync duty, and next handoff.
- [ ] Each active role has a role category, category workspace, and Codex session mapping.
- [ ] Each active role has required skills/tools/knowledge checked and recorded.
- [ ] Product, development, testing, and Loop Manager boundaries do not overlap.
- [ ] All role-to-role messages and interactions are recorded in project documents, and handoffs include document/material paths, online links, artifact references, or explicit evidence gaps.
- [ ] Disagreement handling is clear: role-to-role communication first, Loop Manager escalation for major issues, user/domain-owner decision for unresolved or high-impact conflicts.
- [ ] Handoff rules are clear for scope questions, implementation blockers, defects, acceptance decisions, and governance risks.
""",
        args.force,
    )

    write_text(
        loop_dir / "use-cases.md",
        f"""# {args.name} Use Cases

The demand intake role must turn user ideas into concrete use cases before implementation planning. Each use case must be specific, executable, measurable, and reviewable.

When `grill-me` is available, demand intake must run a grilling session on rough demand, assumptions, standards, and proposed use cases before handoff. Record grilling questions, exposed gaps, revised requirements, rejected assumptions, and confirmation needs here or in `roles/demand-intake/workspace.md`.

Demand intake is also an advisor. It should propose improved use cases, acceptance standards, risk boundaries, and missing scenarios, while clearly marking what is confirmed versus recommended, assumed, risky, or awaiting confirmation.

## Use Case Quality Standard

Every use case must include:

- Use case ID and name.
- Actor or user.
- Scenario and trigger.
- Preconditions.
- Step-by-step action.
- Expected output.
- Measurable acceptance standard.
- Constraints and exclusions.
- Records to capture.
- Evaluation or feedback signal.
- Owner and confirmation status.

## Use Case Table

| ID | Name | Actor | Scenario / Trigger | Preconditions | Steps | Expected Output | Acceptance Standard | Constraints / Exclusions | Records | Feedback Signal | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UC-001 |  |  |  |  |  |  |  |  |  |  | Demand intake role | draft |

## Advisor Recommendations

| Date | Source Role | Recommendation | Why It Helps | Confirmation Needed | Status |
| --- | --- | --- | --- | --- | --- |
|  | Demand intake role |  |  |  | draft |

## Open Questions

- 

## Confirmation

- Confirmation date:
- Confirmation evidence:
- Decision: draft
""",
        args.force,
    )

    write_text(
        loop_dir / "role-loop-charters.md",
        f"""# {args.name} Role Loop Charters

Each active role or subagent must carry explicit Loop responsibilities. Do not create a role that only has a name, folder, or session.

Every role is also an advisor. The charter must make room for role-specific best-practice recommendations, risk warnings, assumptions, options, and confirmation needs.

## Charter Map

| Role / Subagent | Role Category | Goal | Implementation Standard | Constraints | Inputs | Outputs | Records | Evaluation / Feedback | Update Responsibility | Category Workspace | Handoff Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Demand intake role | demand-intake | Turn rough demand into confirmed executable use cases | Demand record and use cases have actor, scenario, trigger, steps, measurable acceptance standard, constraints, records, feedback signal, owner, and confirmation status | Do not invent high-risk business facts; do not hand off vague ideas as implementation-ready | User request, context, constraints | Refined demand, use cases, open questions, confirmation packet | Demand intake record, use-cases.md, assumptions | User confirmation, ambiguity resolved, use cases executable and measurable | Update demand record and use cases before team formation | `roles/demand-intake/` | Hand off confirmed use cases to Loop owner and implementation roles |
| Loop Manager | loop-manager | Govern the whole Loop from project start | Registry, status, risks, decisions, blockers, handoffs, role health checks, resource status, role self-reviews, experience distillation checks, advice summaries, and reflection are current | Do not do development, testing conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, or silently edit skill files | Loop artifacts, role outputs, feedback, gate results, role self-reviews, health/resource signals | Project status, role health report, resource report, reflection summary, role self-review tracker, experience distillation status, role advice summary, improvement proposals | Project status, reflection log, health/resource log, role self-review tracker, role advice summary, feedback to Super Assistant | Stage progress, blockers, recurring failures, role health, resources, role self-review completion, experience captured, role advice surfaced, skill-update candidates | Require role self-review, check role health/resources, verify experience distillation, collect role advice, and send improvement proposals to Super Assistant | `roles/loop-manager/` | Hand off execution to responsible roles; hand off delivery logistics to project manager if selected; send skill feedback to Super Assistant |
| Super Assistant / Loop owner | super-assistant | Drive the Loop end to end | Loop artifacts, handoffs, gates, and updates stay current | Do not perform out-of-scope role work silently | Confirmed demand, role outputs, feedback | Coordination, review, updates | Handoff log, update log, review notes | Gate status, unresolved risks, user feedback | Update Loop artifacts and next-round rules | `roles/super-assistant/` | Hand off role-specific execution to responsible roles |
| Project manager / delivery coordinator | project-management | Coordinate delivery logistics when selected | Milestones, dependency updates, stakeholder status, and delivery risks are current | Do not govern Loop learning, maintain role health, replace Loop Manager, decide product scope, implement, test, approve release, or own experience distillation | Confirmed plan, milestones, dependencies, stakeholder needs | Delivery status, milestone/dependency tracker, stakeholder updates | Delivery log, dependency tracker, status summaries | Milestones and dependencies visible; Loop Manager can see resource/schedule risks | Update delivery coordination artifacts, not Loop governance artifacts | `roles/project-management/` | Hand off Loop governance to Loop Manager; scope decisions to product/domain owner; implementation to developer |
| Product manager / workflow designer | product-workflow | Turn confirmed use cases into product/workflow scope and acceptance standards | Scope, workflow, user value, non-goals, risks, release slices, and acceptance standards are explicit and confirmed | Do not implement, test, approve business acceptance, or expand scope silently | Confirmed use cases, domain constraints, user feedback | Product spec, workflow, acceptance criteria, release slice recommendation | Product decisions, assumptions, tradeoffs, scope changes | Domain/user confirmation, ambiguity reduced, developer can implement | Update product scope and standards before development handoff | `roles/product-workflow/` | Hand off implementation to developer and evidence review to tester |
| Developer / implementer | development | Build the confirmed technical slice | Changes are scoped, runnable, reviewed, and accompanied by implementation evidence | Do not change product scope, declare QA pass, approve release, or bypass governance | Product spec, implementation plan, stage knowledge base, repo context | Code/config/scripts, implementation notes, build evidence | Changed files, commands run, test output, blockers | Build passes, unit checks run, tester has evidence | Update implementation notes and handoff package | `roles/development/` | Hand off verification to tester and scope questions to product manager |
| Tester / evaluator | testing-evaluation | Verify implementation against use cases and acceptance standards | Findings are evidence-based, reproducible, and tied to standards | Do not implement fixes silently, approve business acceptance, or redefine scope | Use cases, acceptance criteria, implementation evidence, runnable artifact | Test plan, pass/fail results, defects, quality risks | Test cases, evidence, failure categories, regression notes | Acceptance criteria verified or defects filed | Update quality standards, regression checks, and feedback signals | `roles/testing-evaluation/` | Hand off defects to developer and acceptance decisions to domain owner |
|  |  |  |  |  |  |  |  |  |  |  |

## Project-Type Workflow Requirements

Every role must know where it sits in the project workflow. For software development, use the lifecycle below unless the user confirms a narrower lifecycle:

```text
demand clarification -> product/workflow scope -> codebase exploration when needed -> architecture/design -> implementation -> testing/evaluation -> code review and specialized reviews as needed -> release/operation readiness -> review/update
```

| Role / Subagent | Project Type | Workflow Stage | Required Prior Inputs | Required Outputs / Evidence | Status Sync Duty | Quality Gate | Next Handoff | Must Not Skip |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Demand intake role | software / product / agent / workflow / research / other | demand clarification | User request, context, constraints | Confirmed use cases, assumptions, acceptance draft | Sync to project owner on handoff and completion | Use cases are measurable and confirmed | Product/workflow or Loop owner | Confirmation before implementation |
| Product manager / workflow designer | software | product/workflow scope | Confirmed use cases | Scope, workflow, acceptance criteria, release slice | Sync before scope handoff and completion | Scope confirmed by user/domain owner | Codebase explorer or developer | Scope confirmation |
| Codebase explorer / implementation researcher | software | codebase exploration | Confirmed scope and repo area | Entry points, data flow, patterns, risks | Sync findings before architecture handoff and completion | Findings cite files/evidence | Software architect | Evidence-backed exploration |
| Software architect / technical designer | software | architecture/design | Scope and exploration notes | Architecture decision, build sequence, test strategy | Sync design before implementation handoff and completion | Design fits repo patterns and constraints | Developer / implementer | Architecture gate |
| Developer / implementer | software | implementation | Confirmed design/scope | Code/config/scripts, build evidence | Sync on start, blocker, handoff, and completion | Runnable implementation with evidence | Tester/evaluator and reviewers | Test/review handoff |
| Tester / evaluator | software | testing/evaluation | Use cases, acceptance criteria, implementation evidence | Test plan, results, defects, risks | Sync findings and completion before acceptance handoff | Evidence-based pass/fail | Developer or domain owner | Test evidence |
| Project manager / delivery coordinator | software / product / agent / workflow / research / other | workflow coordination | Project type and selected workflow | Workflow stage map, milestone/dependency status | Sync delivery status to project owner at cadence and on flow changes | No required stage silently skipped | Responsible next role / Loop owner | Project-type workflow completeness |
| Loop Manager | all | Loop governance | Role registry, workflow map, role outputs | Health/resource/status/workflow gap checks | Monitor stale syncs; request updates | Governance artifacts current | Super Assistant / responsible role | Role execution boundaries |
|  |  |  |  |  |  |  |  |  |

## Advisor Contribution Record

| Role / Subagent | Best-Practice Suggestions | Risks / Anti-Patterns | Options / Tradeoffs | Assumptions | Confirmation Needed |
| --- | --- | --- | --- | --- | --- |
| Demand intake role |  |  |  |  |  |
| Loop Manager | Collect role advice, check role health/resources, and verify experience distillation for user/domain-owner/Super Assistant decisions | One-way command management hides role expertise and role decay | Prompt user with options versus decide internally |  |  |
| Project manager / delivery coordinator | Surface delivery risks, dependency delays, and stakeholder status | Delivery logistics can be confused with Loop governance | Coordinate schedule versus ask Loop Manager for Loop-level decision |  |  |
| Product manager / workflow designer | Recommend scope slices, user workflows, acceptance standards, and non-goals | Ambiguous value or scope creep | MVP versus complete workflow |  |  |
| Developer / implementer | Recommend architecture, implementation plan, technical risks, and maintainability safeguards | Overbuilding, hidden dependencies, untested integration | Simple slice versus reusable abstraction |  |  |
| Tester / evaluator | Recommend test coverage, quality gates, regression checks, and release risk controls | False confidence from happy-path-only testing | Manual evidence versus automated tests |  |  |
|  |  |  |  |  |  |

## Role Creation Gate

- [ ] Every active role has a completed charter and role category.
- [ ] Every active role has a project-type workflow requirement with stage, inputs, outputs/evidence, status-sync duty, quality gate, next handoff, and non-skippable steps.
- [ ] Every active role states its position, what it owns, what it must not do, and when it must hand off.
- [ ] Loop Manager is created at project start and explicitly barred from development, testing conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, and role-specific execution.
- [ ] Loop Manager and project manager/delivery coordinator boundaries are separate; project manager is optional and justified only when delivery coordination needs a dedicated owner.
- [ ] Each charter has evaluation / feedback signals.
- [ ] Each charter has records and update responsibility.
- [ ] Each active role has an advisor contribution record.
- [ ] Each active role has suitable tools and skills identified, available, substituted, or marked as a blocker.
- [ ] Authority boundaries match `role-workspaces.md`.
- [ ] Codex session mapping matches `role-sessions.md`.
""",
        args.force,
    )

    write_text(
        loop_dir / "refinement-standard.md",
        f"""# {args.name} Refinement Standard

Use this file to turn rough user goals, standards, constraints, metrics, or success criteria into executable Loop knowledge.

## Required Quality

Every important goal, standard, constraint, or metric should be:

- Actionable: states what someone should do, decide, record, or avoid.
- Testable: has an observable pass/fail signal or review method.
- Quantified where useful: uses counts, thresholds, timeboxes, rates, sample sizes, owner names, dates, or explicit decision options when they affect execution.
- Bounded: defines scope, exclusions, risk boundaries, and handoff conditions.
- Recordable: names the evidence or event to capture.
- Owned: assigns the responsible role or owner.
- Reusable: can guide the next similar Loop.

## Refinement Table

| Rough Item | Refined Standard | Action | Observable Signal / Threshold | Record | Owner | Confirmation Status |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | draft |

## Vague-To-Executable Conversions

| Vague Wording | Convert Into |
| --- | --- |
| improve quality | target quality signal, review method, failure categories, minimum acceptable result |
| make it usable | user scenario, completion criteria, timebox, adoption/edit/rejection signals |
| do testing | test case count, coverage categories, pass threshold, failure record, owner |
| ensure safety | risk boundary, forbidden actions, approval gate, rollback path, incident record |
| build quickly | timebox, first usable scope, excluded scope, handoff decision |

## Assumptions To Confirm

- 
""",
        args.force,
    )

    write_csv(
        loop_dir / "run-log.csv",
        [
            [
                "run_id",
                "date",
                "actor",
                "loop_type",
                "input",
                "action",
                "output",
                "feedback",
                "feedback_tag",
                "status",
                "failure_reason",
                "update_needed",
                "next_action",
            ]
        ],
        args.force,
    )

    write_text(
        loop_dir / "stage-knowledge-base.md",
        f"""# {args.name} Stage Knowledge Base

Each stage owns its own knowledge. Fill this file as the Loop runs.

## Stage Template

### <stage-name>

Goal:

- 

Implementation standard:

- 

Constraints:

- 

Execution workflow:

1. 
2. 
3. 

Principles:

- 

Inputs:

- 

Outputs:

- 

Records:

- 

Owner:

- 

Review gate:

- 

Reuse rule:

- 
""",
        args.force,
    )

    write_text(
        loop_dir / "stage-confirmation-checklist.md",
        f"""# {args.name} Stage Knowledge Confirmation Checklist

The Loop owner must ask the requester or domain owner to confirm this checklist before execution begins.

## Confirmation Actors

- Requester:
- Domain owner:
- Loop owner: Super Assistant
- Confirmation date:

## Overall Confirmation

- [ ] The stage knowledge base has been reviewed.
- [ ] Each stage has a goal, implementation standard, constraints, workflow, principles, inputs, outputs, and records.
- [ ] Stage inputs and outputs connect clearly.
- [ ] Open questions are recorded with owners and dates.

## Stage Confirmation

| Stage | Goal | Standard | Constraints | Workflow | Principles | Records | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |

## Gate Decision

- [ ] Confirmed: proceed to execution.
- [ ] Confirm with changes: update artifacts, then proceed.
- [ ] Hold: do not proceed.

## Requested Changes

- 
""",
        args.force,
    )

    write_text(
        loop_dir / "implementation-plan.md",
        f"""# {args.name} Implementation Plan

The Loop owner must define this plan before execution begins. Default to Super Assistant plus stage knowledge bases. Add a dedicated subagent only when it is necessary for specialized execution, independent review, parallel work, risk isolation, or long-running operation.

## Execution Principle

- Loop owner: Super Assistant
- Default execution mode: Super Assistant switches stage knowledge bases and coordinates roles.
- Subagent rule: 如无必要，勿增实体. Do not create a subagent unless the stage cannot be handled well by the Loop owner plus its stage knowledge base.
- Role boundary rule: before acting, each role must identify its position, responsibility boundary, editable artifacts, and required handoffs. If it would need to make a decision, do work, or modify files, systems, tools, data, or artifacts outside its responsibility, it must state the boundary, stop the action, and hand off to the responsible role or subagent.
- Tool and skill readiness rule: before a role starts execution, verify its required skills, tools, scripts, references, data access, and permissions. If any required capability is missing, install it, activate it, substitute it, downgrade scope, or mark the role blocked.
- Role category workspace rule: every active role or subagent must use its assigned category folder under `roles/`. Multiple concrete roles or sessions in the same category may share that folder when they have the same responsibility boundary; create separate folders only for distinct categories, authority boundaries, records, or access constraints.
- Codex session rule: when using Codex, each active role or subagent should run in its own thread/session. The Super Assistant coordinates from the main thread/session and hands scoped work to role sessions.

## Stage Assignment

| Stage | Stage Knowledge Base | Responsible Owner / Role | Role Category | Category Workspace | Required Tools / Skills | Tool / Skill Readiness | Dedicated Subagent? | Authority Boundary | Why Needed / Not Needed | Inputs | Outputs | Records | Quality Gate | Next Handoff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Super Assistant | super-assistant | roles/super-assistant/ | loop-builder | available | No |  |  |  |  |  |  |  |

## Required Subagents

List only subagents justified by the implementation plan.

| Subagent | Scope | Trigger Condition | Inputs | Outputs | Review Method |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Out-Of-Scope Modification Handoff

Use this sequence whenever a role detects that a file, system, tool, data source, or artifact modification is outside its assigned authority:

```text
identify role position -> identify boundary -> announce out-of-scope action -> stop local action -> hand off to responsible role/subagent -> record handoff -> review returned result
```

| Date | Current Role | Out-Of-Scope Item | Responsible Role / Subagent | Handoff Reason | Result |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Execution Order

1. Confirm stage knowledge base.
2. Confirm implementation plan and subagent assignment.
3. Start the first executable stage.
4. Record outputs and feedback after each stage.
5. Review gates before handoff.
6. Update Loop artifacts before the next round.

## Open Decisions

- 
""",
        args.force,
    )

    write_text(
        loop_dir / "role-registry.md",
        f"""# {args.name} Active Role Registry

The Loop Manager maintains this file during implementation role creation, confirmation, dispatch, blocking, replacement, and closure. This registry is the source of truth for task dispatch. Do not dispatch implementation work to a role that is missing from this registry.

## Registry Rules

- Add selected roles after user/domain-owner confirmation or explicit delegation to the Loop owner.
- Update this registry when a role is created, confirmed, activated, paused, blocked, replaced, closed, or its concrete person/agent/session changes.
- After any role/personnel/session change, notify every other active role and record the broadcast in `interaction-evidence-log.md`; also record or summarize it in affected role workspaces.
- Use `Role ID` in `goal-dispatch-log.md` for every task dispatch.
- If no registered role can own a task, record the dispatch as blocked and start role-selection confirmation instead of assigning the work informally.
- Loop Manager manages this registry but must not perform role-specific implementation work.

## Active Roles

| Role ID | Role / Subagent | Role Category | Concrete Person / Agent / Session | Category Workspace | Authority Boundary | Owns | Must Hand Off | Required Tools / Skills | Readiness | Health / Resource Status | Last Self-Review | Experience Distilled? | Status | Current Task | Blocker | Last Updated | Updated By |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LM-001 | Loop Manager | loop-manager | dedicated Loop Manager session when Codex is used | `roles/loop-manager/` | Govern Loop registry, cadence, role health, resources, status, blockers, handoffs, advice, reflection, and dispatch; do not perform role-specific or delivery execution | Role registry, dispatch log, status, risks, decisions, blocker tracking, health/resource tracking, experience distillation checks, reflection | Development, testing conclusions, business acceptance, governance decisions, release, project-manager delivery execution, role-specific implementation | loop-builder; Loop governance and retrospection practices | available | healthy / resources available |  |  | active |  |  |  | Loop Manager |
| SA-001 | Super Assistant / Loop owner | super-assistant | current coordination session | `roles/super-assistant/` | Own and coordinate the Loop end to end; hand off role-specific work | Loop coordination, handoff records, review notes, update proposals | Development, testing conclusions, governance decisions, production config unless assigned | loop-builder | available | healthy / resources available |  |  | active |  |  |  | Loop Manager |
|  |  |  |  |  |  |  |  |  |  | healthy / warning / blocked |  | yes / no | proposed / confirmed / active / paused / blocked / replaced / closed |  |  |  |  |

## Role Change Log

| Date | Change Type | Role ID | Role / Category | Previous Status | New Status | Person / Agent / Session Change | Reason | Confirmation Evidence | Notified Roles | Notification Record | Updated By |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | created / confirmed / activated / paused / blocked / replaced / closed / personnel-session-change |  |  |  |  |  |  |  | all active roles | interaction-evidence-log.md | Loop Manager |

## Dispatch Ownership View

| Task ID | Goal ID | Role ID | Role / Session | Status | Expected Return | Evidence Required | Last Check | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | waiting / active / blocked / returned / accepted / closed |  |  |  |  |
""",
        args.force,
    )

    write_text(
        loop_dir / "role-sessions.md",
        f"""# {args.name} Role Sessions

When using Codex, each active role or subagent should run in its own thread/session with a scoped prompt and its assigned workspace. The Super Assistant remains in the coordinating thread/session.

## Codex Session Map

| Role Category | Role / Subagent | Codex Thread / Session | Category Workspace | Session Scope | Receives From | Returns To |
| --- | --- | --- | --- | --- | --- | --- |
| demand-intake | Demand intake role | dedicated intake session if Codex is used | `roles/demand-intake/` | Receive, clarify, refine, and confirm demand | User / requester | Super Assistant |
| loop-manager | Loop Manager | dedicated Loop Manager session when Codex is used | `roles/loop-manager/` | Govern Loop cadence, role registry, role health, resource status, role self-review, experience distillation, reflection, risks, blockers, and feedback to Super Assistant | Super Assistant and role outputs | Super Assistant |
| super-assistant | Super Assistant / Loop owner | current coordination session | `roles/super-assistant/` | Coordinate Loop, assign work, record handoffs, review results | User / requester | User / requester |
| domain-owner | User / domain owner | external confirmation, or dedicated session if used | `roles/domain-owner/` | Business decisions, constraints, acceptance | Super Assistant | Super Assistant |
| product-workflow | Product manager / workflow designer | dedicated role session when needed | `roles/product-workflow/` | Product scope, workflow drafts, acceptance standards, and handoff design | Super Assistant | Super Assistant |
| project-management | Project manager / delivery coordinator | dedicated role session when needed | `roles/project-management/` | Delivery milestones, dependencies, stakeholder status, and delivery logistics | Super Assistant / Loop Manager | Super Assistant / Loop Manager |
| development | Developer / implementer | dedicated role session when implementation starts | `roles/development/` | Build assigned implementation artifacts | Super Assistant | Super Assistant |
| testing-evaluation | Tester / evaluator | dedicated role session when review starts | `roles/testing-evaluation/` | Test/evaluate assigned artifacts | Super Assistant | Super Assistant |
| governance-risk | Governance or risk owner | dedicated role session or external confirmation | `roles/governance-risk/` | Risk, permission, and approval boundaries | Super Assistant | Super Assistant |

## Session Handoff Packet

Every role session should receive:

- Task ID and goal ID from `goal-dispatch-log.md`.
- Role name and authority boundary.
- Assigned workspace.
- Stage knowledge base section to use.
- Inputs and expected outputs.
- Supporting documents, materials, artifact references, data sources, or online document links.
- Known evidence gaps or missing material blockers.
- Files it may edit.
- Files it may read.
- Handoff deadline or gate.
- Return format.

## Session Change Log

| Date | Role Category | Role | Thread / Session | Category Workspace | Change | Reason |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |
""",
        args.force,
    )

    write_text(
        loop_dir / "goal-dispatch-log.md",
        f"""# {args.name} Goal Dispatch Log

Use this log whenever the user sets a goal with the Loop Manager in Codex. Goal setting is management input; it must become a goal contract and task dispatch packet, not silent Loop Manager execution. Each dispatch must target a role listed in `role-registry.md`.

## Dispatch Rule

Loop Manager may refine goals, maintain the active role registry, create task packets, route work to registered roles, track blockers, review returned evidence, and update management artifacts. It must not perform developer, tester, product, governance, release, project-manager delivery execution, or role-specific implementation work.

If the target role is missing from `role-registry.md`, record the dispatch as blocked until role selection or registry update is complete. If the target role/session is registered but unavailable, record the dispatch packet here and in the target role workspace, update the registry status, mark the task waiting or blocked, and report that the role work has not been executed.

## Goal Contract

| Date | Goal ID | User Goal | Refined Goal | Scope | Non-Goals | Acceptance Standard | Constraints | Source Materials / Links | Confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  | draft |

## Dispatch Packet

| Date | Task ID | Goal ID | Registry Role ID | Target Role / Session | Role Category | Project Type | Workflow Stage | Category Workspace | Authority Boundary | Required Knowledge Base | Required Tools / Skills | Inputs / Links | Expected Output | Definition Of Done | Evidence Required | Project Owner | Status Sync Cadence | Completion Sync Required | Return Format | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | software / product / agent / workflow / research / other |  |  |  |  |  |  |  |  |  | Super Assistant / Loop owner | before handoff; on blocker; on completion; periodic cadence TBD | yes |  | waiting |

## Blocked Dispatches

| Date | Task ID | Target Role | Registry Role ID | Missing Role / Session / Skill / Tool / Material | Blocker Owner | Next Action |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |
""",
        args.force,
    )

    write_text(
        loop_dir / "role-workspaces.md",
        f"""# {args.name} Role Workspaces

Every active role category or subagent category must have an independent workspace folder under `roles/`. A role category is a reusable responsibility type, not every individual person, agent, session, or task instance. Multiple concrete roles or sessions in the same category may share the category folder when they have the same responsibility boundary and record type. Create separate folders only when category, authority boundary, ownership, records, or confidentiality/access constraints differ.

## Workspace Map

| Role Category | Role / Subagent | Codex Thread / Session | Category Workspace | Concrete Roles / Sessions Sharing Folder | Owns | May Edit | Must Hand Off |
| --- | --- | --- | --- | --- | --- | --- | --- |
| demand-intake | Demand intake role | dedicated intake session if Codex is used | `roles/demand-intake/` | Demand intake agents/sessions with the same intake boundary | Initial demand record, refinement, open questions, acceptance criteria | Its category workspace and confirmed demand artifacts | Implementation, testing, release, governance, domain acceptance |
| loop-manager | Loop Manager | dedicated Loop Manager session when Codex is used | `roles/loop-manager/` | Loop Manager sessions for this Loop | Active role registry, Loop cadence, role health checks, resource status, decisions, blockers, role self-review, experience distillation checks, role advice summary, reflection, feedback to Super Assistant | Its category workspace, `role-registry.md`, project status, role health tracker, resource status, role self-review tracker, experience distillation status, role advice summary, reflection records, improvement proposals | Development, test conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, role-specific execution, skill edits unless delegated |
| super-assistant | Super Assistant / Loop owner | current coordination session | `roles/super-assistant/` | Super Assistant coordination sessions | Loop coordination notes, handoff records, review notes | Loop-level artifacts and its category workspace | Code, tests, governance decisions, production config |
| domain-owner | User / domain owner | external confirmation, or dedicated session if used | `roles/domain-owner/` | Domain owners sharing the same decision boundary | Business decisions, acceptance notes, domain constraints | Its category workspace and confirmation artifacts | Implementation code and test conclusions |
| product-workflow | Product manager / workflow designer | dedicated role session when needed | `roles/product-workflow/` | Product, workflow, and scope roles with the same product authority | Product scope, workflow drafts, acceptance standards, release slices | Its category workspace and product/workflow docs | Code, tests, production permissions, acceptance decisions |
| project-management | Project manager / delivery coordinator | dedicated role session when needed | `roles/project-management/` | Delivery coordination roles with the same logistics boundary | Milestones, timeline, dependencies, stakeholder status, delivery rituals | Its category workspace, delivery status docs, dependency tracker | Loop governance, role health checks, experience distillation, product scope, implementation, testing, release approval |
| development | Developer / implementer | dedicated role session when implementation starts | `roles/development/` | Developer/implementation sessions with the same implementation boundary | Implementation notes, technical decisions, build evidence | Its category workspace and assigned implementation files | QA conclusions, business acceptance, governance rules |
| testing-evaluation | Tester / evaluator | dedicated role session when review starts | `roles/testing-evaluation/` | Test, evaluation, and review sessions with the same quality boundary | Test cases, evaluation notes, quality findings | Its category workspace and assigned test/evaluation files | Implementation code and business release decisions |
| governance-risk | Governance or risk owner | dedicated role session or external confirmation | `roles/governance-risk/` | Governance/risk roles sharing the same approval boundary | Risk decisions, permission boundaries, approval notes | Its category workspace and governance artifacts | Product workflow ownership and implementation code |

## Handoff Rule

If a role needs to modify a file outside its category workspace or assigned ownership, it must stop, state the boundary, and hand off to the responsible role or subagent category.

## Workspace Change Log

| Date | Role Category | Concrete Role / Session | Workspace Change | Reason | Confirmed By |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
""",
        args.force,
    )

    write_text(
        loop_dir / "interaction-evidence-log.md",
        f"""# {args.name} Interaction Message And Evidence Log

Use this log for all role-to-role messages and interactions: handoffs, advice, questions, answers, status updates, decisions, defect reports, test findings, acceptance feedback, implementation claims, disagreement records, blocker reports, and update proposals. This log is the project-level message ledger. Relevant role workspaces may duplicate or summarize entries, but unrecorded role messages do not count as Loop state.

## Documentation And Evidence Rule

Every role-to-role message must be recorded here or in another named project document. Every interaction should include detailed supporting material when available: a local document/material path, online document link, artifact reference, data source, log, test output, screenshot, ticket, pull request, or decision record.

If the sender cannot provide material, mark an evidence gap and assign a follow-up owner before treating the interaction as execution-ready.

## Message And Interaction Log

| Date / Time | Interaction Type | Sender Role | Receiver Role | Summary | Requested Action / Decision / Next Step | Document / Material / Online Link | Data / Artifact Reference | Evidence Gap? | Follow-Up Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | handoff / advice / question / answer / status / role-status-sync / defect / decision / acceptance / disagreement / blocker / update proposal / role-change-broadcast |  |  |  |  |  |  |  |  | draft |

## Evidence Gap Queue

| Date | Missing Material | Needed For | Owner | Due | Blocker? | Resolution |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |
""",
        args.force,
    )

    write_text(
        loop_dir / "decision-conflict-log.md",
        f"""# {args.name} Decision And Conflict Log

Use this log when roles disagree or when a decision affects scope, standards, risk, schedule, resources, authority, release readiness, or user/domain commitments.

## Resolution Rule

Roles should communicate directly first for ordinary disagreements about assigned tasks, handoffs, evidence, standards, implementation approach, or test interpretation.

Major or unresolved disagreements must be escalated to the Loop Manager. The Loop Manager records the decision packet with supporting documents/materials/links and asks the user or domain owner to decide.

## Conflict Log

| Date | Roles Involved | Issue | Direct Communication Attempted? | Options | Document / Material / Online Link | Evidence | Impact | Recommendation | Decision Owner | Decision | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  | User / domain owner |  |  |

## Decision Packet Template

- Issue:
- Roles involved:
- Why role-to-role resolution was insufficient:
- Option A:
- Option B:
- Document / material / online link:
- Evidence:
- Impact on scope / standard / risk / schedule / resources / authority:
- Recommendation:
- Decision needed from user or domain owner:
- Deadline:
- Follow-up owner:
""",
        args.force,
    )

    for slug, role_name in role_workspaces:
        role_dir = loop_dir / "roles" / slug
        role_dir.mkdir(parents=True, exist_ok=True)
        if slug == "demand-intake":
            use_case_responsibility = """## Use Case Responsibility

- Convert user ideas into concrete use cases in `use-cases.md`.
- Use `grill-me` before handoff when available.
- Record grilling questions, exposed gaps, revised requirements, rejected assumptions, and confirmation needs.
- Do not hand off unconfirmed use cases to implementation roles."""
        else:
            use_case_responsibility = """## Use Case Responsibility

- Execute, review, evaluate, govern, advise on, or update the use cases assigned by the implementation plan.
- Do not rewrite demand-intake use cases unless explicitly assigned; send demand gaps back to the demand intake role."""
        write_text(
            role_dir / "workspace.md",
            f"""# {args.name} - {role_name} Category Workspace

## Role Category

{slug}

## Concrete Roles / Sessions

- {role_name}

## Owned Work

- 

## Loop Charter

- Role position:
- Role category:
- Must not do:
- Goal:
- Implementation standard:
- Constraints:
- Inputs:
- Outputs:
- Records:
- Evaluation / feedback signals:
- Update responsibility:
- Authority boundary:

## Project-Type Workflow Requirement

This role must follow the workflow for the project type selected in `team-formation.md` and `goal-dispatch-log.md`. For software development, the default workflow is:

```text
demand clarification -> product/workflow scope -> codebase exploration when needed -> architecture/design -> implementation -> testing/evaluation -> code review and specialized reviews as needed -> release/operation readiness -> review/update
```

- Project type:
- Workflow stage owned by this role:
- Required prior inputs:
- Required outputs / evidence:
- Status sync duty to project owner:
- Quality gate:
- Next handoff:
- Workflow steps this role must not skip:

{use_case_responsibility}

## Advisor Contribution

This role is also an expert advisor. Enrich assigned work with best practices, but keep advice separate from confirmed requirements.

- Confirmed requirements:
- Advisor recommendations:
- Best practices applied:
- Risks or anti-patterns:
- Options and tradeoffs:
- Assumptions:
- Needs user or domain-owner confirmation:
- User / domain feedback:

## Tool And Skill Readiness

Before execution, confirm this role has the right tools and skills for its assigned work.

- Required skills:
- Required tools/scripts:
- Required data, references, or permissions:
- Availability:
- Install / activation / substitution action:
- Fallback if unavailable:
- Blocker status:
- Owner:

## Assigned Dispatch Packets

Tasks assigned to this role by Loop Manager must arrive as dispatch packets that reference this role's registry ID in `role-registry.md`. This role executes only packets within its authority boundary. Each packet must define the project owner, status-sync cadence, and whether completion sync is required.

| Date | Task ID | Goal ID | Registry Role ID | Project Type | Workflow Stage | Objective | Source Materials / Links | Expected Output | Definition Of Done | Evidence Required | Project Owner | Status Sync Cadence | Completion Sync Required | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | software / product / agent / workflow / research / other |  |  |  |  |  |  | Super Assistant / Loop owner | before handoff; on blocker; on completion; periodic cadence TBD | yes |  |

## Project Owner Status Sync

This role must sync task status to the project owner during task flow at the cadence defined in its dispatch packet. Completion sync is mandatory before handoff, return, closure, or acceptance. Record each sync here and in `interaction-evidence-log.md` as `role-status-sync`.

| Date / Time | Task ID | Goal ID | Registry Role ID | Project Owner | Sync Type | Current State | Completed Work / Progress | Evidence / Links | Blocker / Risk | Next Handoff | Decision Needed | Next Sync Due | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Super Assistant / Loop owner | start / periodic / blocker / handoff / completion | waiting / active / blocked / completed / returned |  |  |  |  |  |  | draft |

## Self-Review

At the cadence defined by the Loop Manager, review this role's conversations, outputs, and feedback. Distill:

- Standards discovered:
- Feedback received:
- Experience worth reusing:
- Mistakes or surprises:
- Proposed updates to role charter, stage knowledge, templates, tests, or the Loop skill:

## May Edit

- This category workspace.
- Files explicitly assigned to this category by `implementation-plan.md` or `role-workspaces.md`.

## Must Hand Off

- Any file, system, data, tool, or artifact outside this role category's assigned authority.

## Interaction Message And Evidence

- Record every role-to-role message or interaction in `interaction-evidence-log.md`, this category workspace, or another named project document.
- Include document/material paths, online document links, artifact references, data sources, logs, test output, screenshots, tickets, pull requests, or decision records when available.
- If supporting material is missing, create the smallest useful document, request it from the responsible role, or mark an evidence gap before treating the interaction as execution-ready.
- Do not rely on chat-only or unrecorded role messages as Loop state.

| Date / Time | Direction | Interaction Type | Other Role | Summary | Requested Action / Decision / Next Step | Document / Material / Online Link | Evidence Gap? | Follow-Up | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | sent / received | role-status-sync / handoff / advice / question / answer / blocker / update proposal |  |  |  |  |  |  | draft |

## Disagreement Handling

- Communicate directly with the relevant role first for ordinary disagreements about assigned tasks, handoffs, evidence, standards, implementation approach, or test interpretation.
- Record the result here when it changes work, standards, records, or next actions.
- Escalate to Loop Manager when the disagreement affects scope, acceptance criteria, risk boundary, schedule, resource allocation, role authority, release readiness, or cannot be resolved quickly.

| Date | Other Role | Issue | Direct Resolution Result | Escalated To Loop Manager? | User / Domain Decision Needed? |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Working Notes

- 
""",
            args.force,
        )

    write_text(
        loop_dir / "feedback-tags.md",
        f"""# {args.name} Feedback Tags

Use a small tag set first. Add tags only when they change future behavior.

## Default Tags

- good_reusable: Output or action can be reused.
- missing_context: Important input was absent.
- wrong_assumption: The loop made a bad assumption.
- quality_gap: Output quality was below standard.
- workflow_friction: The process was awkward or slow.
- risk_or_policy: A risk, policy, permission, or trust issue appeared.
- unclear_next_step: The next action was not obvious.

## Scenario-Specific Tags

- 
""",
        args.force,
    )

    write_text(
        loop_dir / "weekly-review.md",
        f"""# {args.name} Weekly Review

## Review Window

- Start:
- End:

## What Ran

- Total runs:
- Successful runs:
- Failed or abandoned runs:

## What Improved

- 

## Top Feedback Patterns

1. 
2. 
3. 

## Root Causes

- 

## Updates To Make

- Principle:
- Checklist/template:
- Prompt/SOP/process:
- Tooling or UI:
- Evaluation/test case:

## Changes For Next Round

1. 
2. 
3. 
""",
        args.force,
    )

    write_text(
        loop_dir / "experiment-plan.md",
        f"""# {args.name} Experiment Plan

## Hypothesis

- 

## First Real Scenario

- 

## Participants Or Users

- 

## Success Signals

- 

## Minimum Data To Capture

- 

## Timebox

- 

## Decision Rule

Continue, change, or stop this Loop when:

- 
""",
        args.force,
    )

    write_text(
        loop_dir / "update-log.md",
        f"""# {args.name} Update Log

Record durable changes made because of Loop feedback.

| Date | Evidence | Change Made | Artifact Updated | Expected Effect | Follow-up |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
""",
        args.force,
    )

    print(loop_dir.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
