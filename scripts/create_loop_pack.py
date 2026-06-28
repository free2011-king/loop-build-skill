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
    ]

    write_text(
        loop_dir / "loop-design.md",
        f"""# {args.name} Loop Design

## Loop Type

{args.type}

## Loop Owner

Super Assistant

The Loop owner is responsible for driving the whole process from goal, input, action, observation, update, to reuse. The owner coordinates the needed project roles instead of treating the Loop as a one-step task.

## Initial Active Roles

- Demand intake role:
- Loop Manager:
- Super Assistant / Loop owner:

## Deferred Candidate Roles

Loop Manager is mandatory. Start the project with 2-3 other active roles that are actually needed for the next Loop round. Role files and category workspaces may be separate for clarity; avoid activating every specialized candidate at project start.

- User / domain owner, when direct decision/acceptance records need a dedicated workspace:
- Product manager / workflow designer, when user need, scope, workflow, priority, or acceptance criteria are unclear:
- Project manager / delivery coordinator, when delivery milestones, external dependencies, stakeholder status, or schedule logistics need a separate owner:
- Developer / implementer, when implementation work is confirmed:
- Tester / evaluator, when testable output exists or independent evaluation is needed:
- Governance or risk owner, when compliance, security, permission, confidentiality, or release risk requires separate ownership:

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

## Document Governance

- Document index: `document-index.md`
- Project metadata: `project-metadata.md`
- Document count rule: check the index before creating any new document; reuse, update, merge, or archive existing documents unless a new document has a distinct owner, purpose, lifecycle, evidence boundary, confidentiality boundary, or handoff need.
- Per-user / per-owner document budget: define in `document-index.md` before execution.

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
        loop_dir / "document-index.md",
        f"""# {args.name} Document Index

Use this single index to prevent document explosion. Every project document created or managed by a user, domain owner, role, or agent must be tracked here unless it is an external source that is only cited and not managed by this Loop.

## Document Governance Rule

Apply `如无必要，勿增实体` to documents. Before creating a new document, check this index and decide whether the content can be added to an existing document. Create a new document only when it has a distinct owner, purpose, lifecycle, evidence boundary, confidentiality boundary, or handoff requirement.

If a user, domain owner, role owner, or agent exceeds the document budget set below, Loop Manager must request a merge/archive/delete decision before allowing more documents unless the new document is required by compliance, confidentiality, evidence integrity, or role-boundary needs.

## Document Budget By User / Owner

| User / Owner / Role | Active Document Budget | Current Active Count | Review Cadence | Over Budget? | Decision Needed |
| --- | --- | --- | --- | --- | --- |
| User / domain owner | TBD | 0 | fixed-time retrospective | no |  |
| Super Assistant / Loop owner | TBD | 0 | fixed-time retrospective | no |  |
| Loop Manager | TBD | 0 | fixed-time retrospective | no |  |
|  |  |  |  |  |  |

## Managed Document Index

| Document ID | Path / Link | Title | Type | Owner / User | Role Category | Purpose | Why Separate Document? | Related Task / Goal / Stage | Status | Last Review | Next Review | Merge / Archive Candidate | Evidence / Handoff Dependencies |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DOC-001 | `loop-design.md` | Loop Design | core artifact | Super Assistant / Loop owner | super-assistant | Define Loop object, minimum viable loop, records, signals, and update mechanism | Core scaffold artifact | Loop design | active |  |  | no |  |
| DOC-002 | `document-index.md` | Document Index | governance index | Loop Manager | loop-manager | Control document count and lifecycle | Required single index to prevent document explosion | Whole project | active |  |  | no |  |
| DOC-003 | `project-metadata.md` | Project Metadata | metadata | Loop Manager | loop-manager | Maintain project identity, active roles, division of work, thread/session basics, and metadata change history | Required initialization metadata that changes with the project | Whole project | active |  |  | no |  |
| DOC-004 | `team-formation.md` | Team Formation | planning artifact | Super Assistant / Loop owner | super-assistant | Confirm roles, role selection, excluded roles, and readiness | Core role-selection artifact | Team formation | active |  |  | review after role confirmation |  |
|  |  |  |  |  |  |  |  |  | draft / active / merged / archived / superseded |  |  | yes / no |  |

## New Document Decision Log

| Date | Proposed Document | Requested By | Existing Document Checked | Decision | Reason | Index Updated? | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | create / reuse / merge / archive / reject |  | yes / no |  |

## Merge / Archive Queue

| Date | Document ID | Current Owner | Reason | Proposed Action | Decision Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | duplicate / stale / superseded / over budget / wrong owner | merge / archive / delete / keep | Loop Manager / user / domain owner | proposed |
""",
        args.force,
    )

    write_text(
        loop_dir / "project-metadata.md",
        f"""# {args.name} Project Metadata

This file is initialized with every Loop project and maintained by Loop Manager as project metadata changes. It summarizes role information, division of work, thread/session basics, and metadata history. Detailed role authority stays in `role-registry.md`; detailed Codex thread/session routing stays in `role-sessions.md`; this file gives the current project-level view.

## Metadata Rules

- Loop Manager owns this file and updates it whenever roles, role status, division of work, project owner, thread/session mapping, or coordination channels change.
- Keep this file as metadata, not a task log. Detailed task dispatch belongs in `goal-dispatch-log.md`; detailed interactions belong in `interaction-evidence-log.md`.
- After a role or thread/session change, update this file, update `role-registry.md` or `role-sessions.md`, notify all active roles, and record the broadcast.
- Use this file during project restart, thread handoff, onboarding, review, and closure.

## Project Identity

| Field | Value |
| --- | --- |
| Project / Loop name | {args.name} |
| Loop type | {args.type} |
| Loop owner | Super Assistant |
| Loop Manager role ID | LM-001 |
| Project owner function | Super Assistant / Loop owner unless delegated |
| Project metadata owner | Loop Manager |
| Document index | `document-index.md` |
| Role registry | `role-registry.md` |
| Role sessions | `role-sessions.md` |
| Last metadata review |  |
| Metadata status | draft |

## Role And Division Metadata

| Role ID | Role | Role Category | Active? | Division Of Work | Must Hand Off | Category Workspace | Thread / Session | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LM-001 | Loop Manager | loop-manager | yes | Loop governance, role registry, metadata, cadence, retrospectives, communication efficiency, role health, resources, dispatch tracking, experience distillation checks | Development, testing conclusions, business acceptance, governance decisions, release, project-manager delivery execution, role-specific implementation | `roles/loop-manager/` | dedicated Loop Manager session when Codex is used | active |
| SA-001 | Super Assistant / Loop owner | super-assistant | yes | Overall Loop coordination, user-facing coordination, handoff review, update proposals | Role-specific execution outside assignment | `roles/super-assistant/` | current coordination session | active |
| DI-001 | Demand intake role | demand-intake | yes | Clarify rough demand, produce confirmed executable use cases, assumptions, open questions, and confirmation packet | Product scope beyond confirmed input, implementation, testing, release, governance, domain acceptance | `roles/demand-intake/` | dedicated intake session if Codex is used | active |
|  |  |  | yes / no / deferred |  |  |  |  | proposed / active / paused / blocked / closed |

## Thread / Session Metadata

| Thread / Session ID | Role ID | Role | Purpose | Workspace | Created / Activated | Last Used | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| current coordination session | SA-001 | Super Assistant / Loop owner | Coordinate Loop with user | `roles/super-assistant/` | project start |  | active |  |
| dedicated Loop Manager session when Codex is used | LM-001 | Loop Manager | Govern Loop metadata, registry, cadence, role health, resources, and dispatch | `roles/loop-manager/` | project start / when created |  | planned / active |  |
| dedicated intake session if Codex is used | DI-001 | Demand intake role | Clarify demand and confirmation package | `roles/demand-intake/` | project start / when created |  | planned / active |  |
|  |  |  |  |  |  |  | planned / active / paused / closed |  |

## Metadata Change Log

| Date | Change Type | Changed Metadata | Reason | Updated Files | Roles Notified | Notification Record | Updated By |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | role / division / thread-session / project-owner / workspace / status |  |  | project-metadata.md / role-registry.md / role-sessions.md | all active roles | interaction-evidence-log.md | Loop Manager |
""",
        args.force,
    )

    write_text(
        loop_dir / "loop-manager.md",
        f"""# {args.name} Loop Manager

Every concrete Loop project must have a Loop Manager from project start, before demand intake and before implementation roles. The Loop Manager is distinct from a project manager: it governs the whole Loop system, not ordinary delivery logistics. It manages Loop rhythm, default automatic distillation time nodes, fixed-time retrospectives, communication-efficiency review, role responsibility optimization, role skill/tool improvement, role skill-evolution tracking, and project-level reflection, maintains the active role registry during role creation and role/personnel/session changes, broadcasts role changes to every other active role, checks project-type workflow completeness, checks role health, checks resource status, checks whether each role has synced task status to the project owner at the required cadence and on completion, checks whether each role has distilled reusable experience into its workspace, receives goal-setting interactions in Codex, turns goals into dispatch packets, routes tasks against the registered role list, requires each role to run regular self-review, regularly collects each role's professional advice, handles major disagreement escalation, prompts the user or domain owner to consider advice and major decisions, then sends improvement feedback to the Super Assistant. The Loop Manager does not do development, testing conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, or role-specific implementation work.

## Role Charter

| Item | Definition |
| --- | --- |
| Role name | Loop Manager |
| Workspace | `roles/loop-manager/` |
| Codex thread/session | dedicated Loop Manager session when Codex is used |
| Owns | Active role registry, Loop cadence, fixed-time retrospectives, role health checks, resource status checks, project-owner status sync checks, communication-efficiency review, role responsibility optimization, role skill/tool improvement, status, risks, decisions, blockers, handoffs, role self-review, experience distillation checks, role advice collection, user/domain-owner advice prompts, project reflection, feedback to Super Assistant |
| May edit | Loop Manager workspace, project-metadata.md, role-registry.md, project status, reflection records, role advice summaries, improvement proposals |
| Must not do | Development, implementation, test conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, role-specific execution |
| Must hand off | Implementation work, QA conclusions, business acceptance, governance decisions, release decisions, skill edits unless explicitly delegated |

## Management Cadence

| Cadence | Activity | Output |
| --- | --- | --- |
| Project-start baseline | Record Loop object, initial active roles, deferred candidate roles, project metadata, document budget, risk/resource baseline, communication rules, first gates, and first review dates | Baseline entry in Loop Manager workspace, project-metadata.md check, role-registry.md check, document-index.md check |
| Role creation, personnel/session adjustment, or role status change | Update project metadata and active role registry with role ID, category, workspace, session, boundary, readiness, health, resources, and status; notify every other active role; record the notification | project-metadata.md update, role-registry.md update, interaction-evidence-log.md broadcast record, affected role workspace updates |
| Each stage handoff | Check owner, input, output, records, gate | Handoff status |
| Hard constraint gate check | Check user-facing product/UI/workflow/scope/acceptance/risk/release changes for decision owner, human-participation classification, confirmation evidence, enforcing roles, stop condition, and downstream blockers | Hard constraint gate status, human-required/delegated-review/automated-pass classification, and blocked-action list |
| Project-owner acceptance translation gate | Translate user demand into verifiable acceptance standards, evidence requirements, open assumptions, and a confirmation packet before dispatch or execution | Acceptance translation packet and user/domain-owner confirmation record |
| Task or stage completion checkpoint | Distill what changed, evidence returned, status-sync quality, handoff quality, reusable learning, and next owner | Completion distillation note in interaction-evidence-log.md or responsible role workspace |
| User sets a goal in Codex | Convert the goal into a goal contract and dispatch packet; route to responsible role/session; define project-owner status sync cadence and completion sync requirement | Goal dispatch log update |
| Fixed-time retrospective, weekly by default unless project cadence says otherwise | Review progress, blockers, risks, user-role communication efficiency, role-to-role communication efficiency, handoff friction, responsibility overlap/gaps, skill/tool gaps, feedback, and updates | Retrospective summary, communication-efficiency report, responsibility/skill improvement proposals |
| Event-triggered review | Run after major blocker, role change, repeated handoff friction, major disagreement, failed gate, user correction, or material risk | Cause analysis, prevention rule, role/document/communication update proposal |
| Project-closure distillation | Preserve reusable learning, decide which documents to merge/archive, decide which roles pause/close, and send skill/template/principle feedback to Super Assistant | Closure note, archive/merge decisions, role closure updates, skill/principle/template feedback |
| Each role message or interaction | Confirm the message is recorded in `interaction-evidence-log.md` or a named project document, and check whether it includes document/material paths, online links, artifact references, or explicit evidence gaps | Interaction/message log update |
| Project-owner status sync cadence | Check active roles sync task status to the project owner at the dispatch-defined cadence and immediately on completion, blocker, decision need, or handoff | role-status-sync record and stale-sync gap list |
| Role change broadcast | After a role is created, activated, paused, replaced, closed, or its person/agent/session changes, notify all other active roles with change summary, reason, effective time, boundary impact, handoff impact, and required action | Broadcast notification record |
| Project metadata review | Check role information, division of work, thread/session basics, project owner function, workspace ownership, and metadata change history against current project reality | project-metadata.md update and stale metadata fixes |
| Project-type workflow completeness | For each new question/request/issue/work item, check that the project manager or Loop owner classified project nature, selected the full workflow, and wrote each role's workflow-stage requirement into its charter | Project workflow checklist and role charter updates |
| Role health cadence | Check each active role's readiness, workload, blockers, stale handoffs, context gaps, missing records, tool/permission/resource gaps, and last self-review | Role health report |
| Resource review cadence | Check people/agent/session availability, tool access, data/material readiness, time budget, external dependencies, and overloaded roles | Resource status report |
| Role self-review cadence | Require each active role to distill standards, feedback, communication friction, responsibility-fit issues, skill/tool gaps, experience, and update proposals from its conversations and outputs | Role self-review records |
| Experience distillation check | Verify each role's reusable experience, mistakes, surprises, and update proposals have been written into its category workspace or Loop artifacts | Experience distillation status |
| Role skill-evolution checkpoint | Collect each role's skill signals, missing tools, useful prompts, better checklists, repeated mistakes, review findings, and proposed role-skill updates | Role skill evolution backlog and target artifact update decisions |
| Role advice cadence | Ask active roles for best-practice suggestions, risks, options, assumptions, and confirmation needs; summarize them for the user or domain owner | Role advice summary and user decision requests |
| Candidate role capability source tracking | Check ECC / Everything Claude Code, Claude Code plugins, local skills/tools, and trusted role references for changes that affect candidate-role responsibilities, activation triggers, skill/tool matches, evidence requirements, or handoffs | Candidate role capability source tracking log and proposed role-library updates |
| Before execution gates | Verify required artifacts and confirmations | Gate recommendation |
| After project learning | Send improvement proposal to Super Assistant, including communication rules, role responsibility changes, skill/tool upgrades, and template updates | Skill/principle/template update candidate |
| Major role disagreement | Collect issue, options, evidence, impact, recommendations, and decision need; ask user/domain owner to decide | Decision packet and conflict log update |

## Default Automatic Distillation Time Nodes

These time nodes are active by default when the project is created. Change them only when the user/domain owner confirms a different cadence.

| Time Node | Default Trigger | Distillation Focus | Required Output | Status |
| --- | --- | --- | --- | --- |
| Project-start baseline | Immediately when this Loop project is created | Loop object, active roles, deferred roles, document budget, risk/resource baseline, communication rules, and first gates | Baseline note, role-registry.md check, document-index.md check | active |
| Task or stage completion checkpoint | Role completes a task, stage, handoff, or dispatch packet | What changed, evidence returned, status-sync quality, handoff quality, reusable learning, and next owner | Completion distillation note | active |
| Weekly fixed retrospective | Weekly by default unless the project defines another cadence | Communication efficiency, role health, resource fit, responsibility boundaries, skill/tool gaps, reusable principles, and document growth | Retrospective summary and improvement proposals | active |
| Event-triggered review | Major blocker, role change, repeated handoff friction, major disagreement, failed gate, user correction, or material risk | Cause, affected roles, boundary change, communication update, role split/merge need, and prevention rule | Decision/conflict entry, registry update when needed, all-role notification when roles change | active |
| Project-closure distillation | Project, milestone, release, or Loop round closes | Reusable learning, archive/merge decisions, role pause/closure, and skill/template/principle updates | Closure note and feedback to Super Assistant | active |

## Project Owner Core Operating Principles

The project owner function may be held by a project manager / delivery coordinator, the Loop owner, or temporarily by Loop Manager when no separate project manager exists. Its most important task is to translate user demand into verifiable acceptance standards before dispatch or execution.

- Translate user demand into verifiable acceptance standards before execution or dispatch.
- Separate the user's original words, the project owner's interpretation, assumptions, open questions, and confirmed standards.
- Treat confirmation as the start signal. If standards are missing, ambiguous, unconfirmed, or not testable, mark the work blocked or discovery-needed.
- Dispatch confirmed work to registered roles instead of silently doing role-specific execution.
- Preserve acceptance standards, evidence requirements, confirmation records, and feedback so the Loop can learn.
- Minimize user interruption after standards are confirmed and work is standardized, delegated, objectively checkable, and evidence-backed.

## Acceptance Translation Packet

| Date | Work Item / Goal ID | User Demand In Original Words | Interpreted Goal / Scenario | Verifiable Acceptance Standards | Evidence Required | Human Participation | Assumptions / Questions | Confirmation Owner | Confirmation Record | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | observable pass/fail checks | implementation/test/review/release evidence | human-required / delegated-review / automated-pass |  | user / domain owner / delegated decision owner |  | draft / waiting-confirmation / confirmed / blocked |

## Project-Type Workflow Rule

When a project manager / delivery coordinator is selected, every new project question, request, issue, or work item must be classified by project nature and routed through the complete workflow for that project type. If no project manager is selected, the Loop owner performs this classification and Loop Manager checks that role charters contain the workflow requirements.

For software development, the default workflow is:

```text
demand clarification -> product/workflow scope -> codebase exploration when needed -> architecture/design -> implementation -> testing/evaluation -> code review and specialized reviews as needed -> release/operation readiness -> review/update
```

| Date | Work Item | Project Type | Required Workflow | Project Manager / Owner | Roles With Workflow Requirement | Missing Stage / Gap | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | software / product / agent / workflow / research / other |  | Project manager / delivery coordinator or Super Assistant |  |  |  |

## Hard Constraint Gates

Hard constraints must be explicit gates, not remembered preferences. Use this section for mandatory confirmations, human-participation classification, automated-pass eligibility, and blocked downstream work.

Example: if the product manager / workflow designer changes UI design, product workflow, scope, release slice, or acceptance criteria after prior confirmation, the change remains a proposal until the user/domain owner confirms it. Developer implementation, tester acceptance, UI/frontend approval, and release-readiness work must use the last confirmed version until confirmation evidence is recorded.

Use `human-required` for aesthetic judgment, taste, brand feel, product direction, user value tradeoffs, ambiguous demand, governance/risk authorization, or changed confirmed constraints. Use `automated-pass` for standardized production when requirements are clear, authority is delegated, objective checks pass, evidence is recorded, and no confirmed constraint changes.

| Gate ID | Constraint | Human Participation | Triggering Change / Stage | Proposing Role | Enforcing Roles | Decision Owner | Required Evidence | Stop Condition | Record Location | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HCG-001 | Product/UI/workflow changes need user/domain-owner confirmation | human-required for new aesthetic/product/value/meaning decisions; delegated-review only if explicitly delegated | Product manager changes UI design, workflow, scope, release slice, or acceptance criteria | Product manager / workflow designer | Loop Manager; developer; tester; UI/frontend reviewer; release/governance owner when selected | User / domain owner / delegated Loop owner | Before/after summary, changed artifact or screenshot/design link, affected use cases, acceptance impact, confirmation record | No downstream implementation, acceptance, or release-readiness proceeds on the changed item | interaction-evidence-log.md / product workspace / implementation-covenant.md | draft |
| HCG-002 | Standardized production with clear requirements may proceed without user participation | automated-pass | Requirement is confirmed, repeatable, low-risk, and objectively checkable | Responsible execution role | Loop Manager; tester/reviewer when selected | Delegated role owner | Confirmed requirement, objective checklist/test/script output, produced artifact, status sync | Escalate to human-required or delegated-review if checks fail, ambiguity appears, or a confirmed constraint changes | interaction-evidence-log.md / role workspace | draft |
|  |  | human-required / delegated-review / automated-pass |  |  |  |  |  |  |  | draft / waiting-confirmation / confirmed / blocked / automated-pass / closed |

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
3. Translate the user's demand into verifiable acceptance standards, evidence requirements, and confirmation questions.
4. Obtain user/domain-owner confirmation or record the work as blocked/discovery-needed.
5. Select the responsible role from `role-registry.md`; if no registered role fits, record a blocker or initiate role-selection confirmation.
6. Create a dispatch packet for the responsible role/session.
7. Include role ID, role category, workspace, authority boundary, source materials/links, confirmed acceptance standards, evidence requirements, tool/skill readiness, definition of done, return format, project owner, status-sync cadence, and completion-sync requirement.
8. Route the packet to the responsible role/session, or record a blocker if the session is unavailable.
9. Update role registry and dispatch status while the task moves through waiting, active, blocked, returned, accepted, or closed.
10. Review returned evidence after the responsible role acts.

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

## Communication Efficiency And Role Optimization Review

At the fixed-time retrospective cadence, Loop Manager must review how well the user and project roles communicate, and whether each role's responsibility boundary and skill/tool readiness should be adjusted.

| Date | Review Window | User-To-Role Communication Friction | Role-To-Role Communication Friction | Responsibility Overlap / Gap | Skill / Tool Gap | Proposed Communication Update | Proposed Role Responsibility Update | Proposed Skill / Tool Update | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  | Loop Manager | draft |

## Reflection Log

| Date | Evidence | What Changed | Loop Weakness | Proposed Improvement | Send To Super Assistant? |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Role Self-Review Tracker

| Date | Role | Workspace | Conversation / Work Reviewed | Standards Distilled | Feedback Distilled | Experience Distilled | Update Proposal | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

## Role Skill Evolution Backlog

Every role's skills, prompts, checklists, references, and tool requirements should improve through real work. Roles provide domain learning; Loop Manager provides cadence, evidence discipline, cross-role comparison, and artifact updates.

| Date | Role | Skill Signal | Evidence | Proposed Skill / Checklist / Prompt / Tool Update | Target Artifact | Decision | Owner | Next Review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | repeated blocker / user correction / review finding / test gap / useful prompt / missing tool / better checklist / new reference |  |  | role workspace / role charter / candidate-role-library.md / implementation-covenant.md / generated template / SKILL.md | proposed / accepted / rejected / applied | Loop Manager / role owner |  |

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

Loop Manager checks that every role-to-role message and interaction is recorded in `interaction-evidence-log.md` or another indexed project document. Before a role creates another document for supporting material, it must check `document-index.md` and reuse or update an existing document when possible. Handoffs, advice, defect reports, decisions, questions, answers, status updates, acceptance feedback, and implementation claims must include detailed supporting material when available: local document/material path, online document link, artifact reference, data source, logs, test output, screenshots, tickets, pull requests, or decision records.

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

Create the Loop Manager first at project start. Then create 2-3 other active roles needed for the next Loop round. The default scaffold starts with Super Assistant / Loop owner and Demand intake; add a third non-manager role early only when the project nature clearly needs it. Role files and category workspaces may be separate for active or explicitly prepared roles. Select implementation roles from the existing reusable role library, but do not activate roles, sessions, or skills that the next Loop round does not require. Create a new role only when no existing role category can responsibly cover the work.

## Initial Role Split Policy

- Initial active roles: Loop Manager plus 2-3 other roles. Default: Super Assistant / Loop owner and Demand intake.
- Deferred candidates are not active roles until confirmed by the user/domain owner or explicitly delegated to the Loop owner.
- Loop Manager owns staged role splitting after project start and should recommend activation, merging, pausing, or closure based on evidence.
- Split roles only when workload, workflow stage, specialist skill, risk isolation, independent review, confidentiality, compliance, stakeholder reporting, or repeated handoff friction proves the smaller role set is no longer enough.
- Separate files/workspaces are allowed for active roles and explicitly prepared roles; avoid creating active role status for every candidate role.

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

Select from existing reusable roles before creating any new role. The selected implementation role set must be confirmed by the user or domain owner before execution. Prefer Loop Manager plus 2-3 other active roles and deferred candidates over a fully split team at project start.

| Project Need / Use Case | Selected Existing Role | Role Category | Why Needed | Category Workspace | Authority Boundary | Required Tools / Skills | Readiness / Blocker | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | draft |

## Deferred Candidate Roles

Record roles that may be useful later but are not active in the current Loop round.

| Candidate Role | Role Category | Candidate Workspace | Activation / Split Trigger | Why Deferred Now | Review Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| User / domain owner | domain-owner | `roles/domain-owner/` | Dedicated decision/acceptance records, confidentiality boundary, or recurring domain-owner work appears | External confirmation may be enough at project start | Loop Manager | deferred |
| Product manager / workflow designer | product-workflow | `roles/product-workflow/` | User need, scope, workflow, priority, acceptance, or outcome metric is unclear enough to require a dedicated owner | Demand intake and Loop owner may cover early discovery | Loop Manager | deferred |
| Project manager / delivery coordinator | project-management | `roles/project-management/` | Delivery milestones, external dependencies, stakeholder status, or schedule logistics need separate ownership | Delivery coordination may not be needed in early exploration | Loop Manager | deferred |
| Developer / implementer | development | `roles/development/` | Confirmed implementation work is ready | No implementation before confirmed demand/scope | Loop Manager | deferred |
| Tester / evaluator | testing-evaluation | `roles/testing-evaluation/` | Testable output, independent evaluation, or quality gate exists | No testable artifact yet | Loop Manager | deferred |
| Governance or risk owner | governance-risk | `roles/governance-risk/` | Compliance, security, permission, confidentiality, or release risk needs separate ownership | Governance boundary may be light early | Loop Manager | deferred |

## Excluded Candidate Roles

Record existing roles that are not selected for this Loop round so the team stays intentionally small.

| Candidate Role | Role Category | Exclusion Reason | Reconsider Trigger | Confirmed By |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Implementation Team Proposal

Add only roles required by the confirmed demand and selected role set. Candidate rows below are not active until their activation trigger is met and the Loop Manager updates `role-registry.md`.

| Role Category | Role / Subagent | Needed? | Reason | Required Skill(s) | Category Workspace | Codex Thread / Session | Trigger | Inputs | Outputs | Gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| loop-manager | Loop Manager | Yes | Govern the whole Loop, role registry, role health, resources, experience distillation, and project-level reflection | loop-builder | `roles/loop-manager/` | dedicated Loop Manager session when Codex is used | Always, from project start | Loop artifacts, role status, feedback, resource needs | Role registry, health report, resource report, reflection, improvement proposals | Feedback sent to Super Assistant when needed |
| super-assistant | Super Assistant / Loop owner | Yes | Own and coordinate the Loop | loop-builder | `roles/super-assistant/` | current coordination session | Always | Confirmed demand | Coordination, handoff, review | Loop artifacts updated |
| project-management | Project manager / delivery coordinator | Candidate | Coordinate delivery milestones, timeline, external dependencies, stakeholder status, and delivery rituals when needed | project management / delivery coordination | `roles/project-management/` | dedicated project-management session when needed | Delivery coordination cannot be cleanly owned by another role | Confirmed plan, dependencies, milestones | Delivery status, dependency tracker, stakeholder summary | Delivery logistics are visible and not confused with Loop governance |
| product-workflow | Product manager / workflow designer | Candidate | Understand complete user needs and define product scope, user value, workflow, acceptance standards, outcome metrics, and release slices | loop-builder; grill-me when refining scope; product discovery/user research/prioritization skills when available | `roles/product-workflow/` | dedicated product role session when needed | Product, user need, workflow, priority, or acceptance ambiguity exists | Confirmed demand, use cases, user/domain evidence, constraints, evidence gaps | Product problem statement, target users, workflow, acceptance criteria, outcome metric, scope decisions, release-slice rationale | User/domain-owner confirms scope, standards, and remaining evidence gaps |
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
| Product manager / workflow designer | loop-builder; grill-me when scope is unclear; product discovery/user research/prioritization skills when available | user/domain input; product references; interviews; support/sales feedback; analytics or process evidence if available | check project context | Activate product/spec/design/analytics skills if available | Use structured product discovery, user-need, PRD, and prioritization checklist | yes if no domain decision-maker or no user evidence path | Product manager / workflow designer | Understand complete user needs and convert use cases into scope, workflow, standards, outcome metrics, and release slices |
| Project manager / delivery coordinator | project management / delivery coordination | milestone context; dependency owners; stakeholder channels | check project context | Activate project tracking tools if available | Use lightweight delivery log | no unless delivery coordination is required | Project manager / delivery coordinator | Coordinate delivery logistics without replacing Loop Manager |
| Developer / implementer | framework/language/repo skills | code repo; package manager; dev server; test runner; logs | check repo and permissions | Activate/install required coding skills and toolchain | Implement smallest verifiable slice or mark blocker | yes if repo/tool access missing | Developer / implementer | Build only confirmed scope with evidence |
| Tester / evaluator | testing/evaluation skills | test runner; acceptance criteria; test data; browser/API tools if needed | check repo and environment | Activate/install required testing tools | Manual checklist with recorded evidence | yes if no runnable artifact or acceptance criteria | Tester / evaluator | Verify behavior independently from development |
|  |  |  |  |  |  |  |  |  |

## User Confirmation Of Role Selection

- [ ] Demand intake role is accepted.
- [ ] Selected existing implementation roles are accepted.
- [ ] Active role set is intentionally minimal for this Loop round.
- [ ] Deferred candidate roles and activation/split triggers are accepted.
- [ ] Excluded candidate roles and exclusion reasons are accepted.
- [ ] New roles, if any, are justified because no existing role category can cover the work.
- [ ] Required skills are accepted.
- [ ] Tool and skill readiness has been checked for every active role.
- [ ] Role categories, category workspaces, shared-folder rules, and Codex sessions are accepted.
- [ ] Authority boundaries and first handoff path are accepted.
- [ ] `implementation-covenant.md` is accepted, including role-boundary matrix, communication content requirements, evidence rules, handoff packages, status-sync rules, and escalation path.
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

Use this library before creating project roles. Start from these existing reusable role presets for software, product, Agent, workflow, or digital-employee Loops. At project start, Loop Manager is mandatory and the other active roles should usually start with 2-3 roles chosen for the next Loop round. Keep specialized roles as deferred candidates until there is confirmed need, complexity, risk, workload, or workflow evidence. Separate role files or category workspaces are allowed for active or explicitly prepared roles. Select roles according to confirmed project needs and use cases, ask the user or domain owner to confirm the selected implementation role set, then activate only the roles needed by the confirmed plan.

## Selection Workflow

1. Start from confirmed project needs and use cases.
2. Match each need to an existing candidate role and role category.
3. Select a small active role set that can cover the next Loop round without unclear authority, evidence, record, or confidentiality boundaries. Use Loop Manager plus 2-3 other active roles as the normal early-project range.
4. List deferred candidate roles, the trigger that would activate each one, and why they are not needed now.
5. List candidate roles that are excluded entirely and explain why they are unnecessary for this Loop round.
6. Prepare a confirmation packet with selected roles, deferred candidates, excluded candidates, split triggers, category workspaces, authority boundaries, handoff paths, required tools/skills, readiness status, and blockers.
7. Ask the user or domain owner to confirm the selected role set before implementation.
8. Create a new role only when no existing role can responsibly cover the confirmed need.

## Activation Rule

Apply `如无必要，勿增实体`: a candidate role is not active until the implementation plan gives it a concrete goal, authority boundary, role category, category workspace, tools/skills, knowledge base, records, gates, and handoff rules.

## Staged Role Splitting

The Loop Manager owns staged role splitting after project start. It should keep the early active set small while the work is still exploratory or low risk, then recommend activation or separation when evidence shows a real need.

Use these triggers to split or activate a specialized role:

- The current owner is overloaded or repeatedly blocked.
- Responsibilities overlap, create gaps, or cause boundary violations.
- The workflow needs independent review, parallel execution, risk isolation, or specialist skill.
- Handoffs, status syncs, or evidence records show repeated friction.
- Compliance, confidentiality, release readiness, stakeholder reporting, or evidence integrity requires separate ownership.

The Loop Manager may also recommend merging, pausing, or closing roles when the project stabilizes or when a previous split is no longer useful. Record every split/merge decision in `role-registry.md`, `team-formation.md`, and `interaction-evidence-log.md`.

## Reusable Candidate Roles

| Candidate Role | Role Category | Default Position | Activate When | Must Not Do | Default Category Workspace | Codex Session |
| --- | --- | --- | --- | --- | --- | --- |
| Product manager / workflow designer | product-workflow | Think through the product problem, repeatedly clarify user needs with the user/domain owner, and convert confirmed use cases into product scope, workflow, acceptance standards, non-goals, risks, outcome metrics, and release slices | User value, target users, workflow, scope, priority, acceptance criteria, or success metrics are unclear | Implement code, declare tests passed, approve business acceptance, ignore user evidence, silently expand scope, or hand off ambiguous demand as ready | `roles/product-workflow/` | Dedicated product role session |
| Developer / implementer | development | Build the confirmed technical slice and provide implementation evidence | Confirmed scope needs code, configuration, integration, automation, or platform changes | Redefine scope, declare QA passed, approve release, or bypass governance | `roles/development/` | Dedicated developer session |
| Tester / evaluator | testing-evaluation | Verify behavior against use cases, acceptance standards, regressions, and quality gates | Runnable artifact or reviewable implementation exists | Implement fixes silently, approve business acceptance, or rewrite scope | `roles/testing-evaluation/` | Dedicated tester session |
| Loop Manager | loop-manager | Govern the whole Loop: role registry, cadence, fixed-time retrospectives, blockers, handoffs, role health checks, resource status, experience distillation, role self-review, role advice, communication-efficiency review, role responsibility/skill optimization, reflection, and feedback to Super Assistant | Always for every concrete Loop project; created at project start before demand intake and implementation roles | Do development, testing conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, or role-specific execution | `roles/loop-manager/` | Dedicated Loop Manager session |
| Project manager / delivery coordinator | project-management | Translate user demand into verifiable acceptance standards for confirmation, classify each new question/request by project nature, and coordinate the complete workflow for that project type, including milestones, timeline, cross-team dependencies, stakeholder status, and delivery rituals | Delivery scheduling, acceptance-standard coordination, external dependencies, stakeholder reporting, multi-team coordination, or project-type workflow completeness needs a dedicated owner | Treat private understanding as execution permission, govern Loop learning, maintain role health, replace Loop Manager, decide product scope, do implementation, declare QA pass, approve release, own experience distillation, or skip required project-type workflow stages | `roles/project-management/` | Dedicated project-management session when needed |


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

## Role Capability Source Tracking

Track ECC / Everything Claude Code, Claude Code official or curated plugins, local `.codex/plugins` metadata, available skills/tools, and trusted external role references as capability sources for candidate roles.

Use monthly as the default tracking cadence when the project does not define one. Also review sources after plugin/tool updates, new skill installs, major project retrospectives, repeated role failures, repeated handoff friction, or when a role's skill/tool readiness is blocked.

Do not update the candidate role library merely because a source exists. Update candidate-role requirements only when the source changes at least one of these:

- Role responsibility boundary or must-not-do boundary.
- Activation trigger or exclusion reason.
- Skill/tool/knowledge match.
- Evidence, record, or handoff package requirement.
- Workflow stage, quality gate, or review expectation.
- Communication, status-sync, or implementation covenant requirement.

| Date | Source | Version / Date / Link | Observed Capability | Affected Candidate Role | Proposed Requirement Change | Evidence | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | ECC / Everything Claude Code / Claude Code plugin / local skill / tool / external reference |  |  |  |  |  | Loop Manager / Super Assistant | proposed / accepted / rejected / applied |

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
| Product manager / workflow designer | `loop-builder`; `grill-me` when scope is rough; product discovery, user research, prioritization, roadmap/PRD, and product analytics skills when available | User interviews, domain references, support/sales feedback, analytics/process evidence, competitor/domain references, diagram/spec/roadmap tools | User segments, jobs/pains/gains, scenarios, user-need statements, goals/non-goals, assumptions, constraints, use cases, workflow, acceptance standards, outcome metrics, priority model, release slicing principles | User evidence, product decisions, assumptions, tradeoffs, priority rationale, scope changes, open questions, confirmation evidence |
| Developer / implementer | Framework/language/repo skills; code review and security skills when relevant | Repository, package manager, dev server, test runner, logs, debugger, CI output | Architecture, coding standards, repo conventions, integration contracts, environment setup, error handling, rollback notes | Changed files, commands run, test output, implementation notes, blockers |
| Tester / evaluator | Testing/evaluation skills; browser/API/performance/security tools when relevant | Test runner, browser automation, API client, fixtures/test data, logs, acceptance checklist | Test strategy, acceptance criteria, regression areas, data setup, quality gates, known risks | Test plan, pass/fail results, defect reports, evidence, regression notes |
| Loop Manager | `loop-builder`; Loop governance, fixed-time retrospective, communication-efficiency analysis, role-design, and skill-improvement practices | Role registry, health check tracker, communication-efficiency tracker, responsibility/skill improvement backlog, resource log, handoff tracker, decision log, risk log, review cadence | Loop object, role map, handoff rules, communication signals, health signals, resource thresholds, self-review prompts, experience distillation standards, role optimization principles, improvement principles | Status, blockers, decisions, risk log, handoff log, communication-efficiency report, role responsibility optimization proposals, skill/tool improvement proposals, role health report, resource report, role advice summary, reflection updates |
| Project manager / delivery coordinator | project management and delivery coordination practices; software delivery workflow when project type is software | Status board, milestone plan, dependency tracker, stakeholder update log, workflow checklist | User demand, project type, acceptance translation packet, required lifecycle stages, milestones, timeline, dependencies, delivery rituals, stakeholder communication needs | Acceptance confirmation record, delivery status, workflow stage map, milestone risks, dependency updates, stakeholder summaries |

## Project Owner Acceptance Translation Pattern

Use this pattern whenever a project manager / delivery coordinator is selected, or when Loop Manager / Loop Owner temporarily carries the project owner function because no separate project manager exists.

The project owner function must translate the user's demand into verifiable acceptance standards before execution. It does not start implementation from private interpretation.

Core operating principles:

- Translate user demand into verifiable acceptance standards before execution or dispatch.
- Keep user wording, interpretation, assumptions, questions, and confirmed standards separate.
- Ask the user/domain owner or delegated decision owner to confirm the standards before work begins.
- If standards are missing, ambiguous, unconfirmed, or not testable, mark the task blocked or discovery-needed.
- Dispatch confirmed work to registered roles and preserve evidence so the Loop can learn.
- Avoid user interruption for standardized production only after standards are confirmed and objective checks are defined.

Acceptance translation packet:

- User demand in original wording.
- Interpreted goal, target user, scenario, and desired outcome.
- Verifiable acceptance standards with observable pass/fail checks.
- Positive examples, negative examples, edge cases, non-goals, and constraints.
- Evidence expected from developer, tester, reviewer, release, or standardized production roles.
- Human participation classification for each acceptance gate.
- Open assumptions, questions, and confirmation owner.
- User/domain-owner confirmation record.

Role enforcement rule:

- Project manager / delivery coordinator owns this packet when selected.
- Loop Manager may prepare and track this packet only when no project manager exists, but still must not perform role-specific execution.
- Product manager helps convert vague demand into product meaning and acceptance standards.
- Developer, tester, reviewer, and release roles refuse execution or acceptance when standards are missing, ambiguous, or unconfirmed.
- Standardized production may proceed only after standards are confirmed and objective checks/evidence are defined.

## Product Manager Capability Pattern

Use this baseline whenever the Product manager / workflow designer role is created. It is adapted from established product discovery, user-need, and agile product-owner practices: discover the problem before committing to a solution, describe user needs in observable terms, maintain outcome-oriented scope, and prepare evidence-backed handoffs. The role must think like a product owner, not a task transcriber: it should challenge unclear requests, explore user value, compare options, identify non-goals, and keep communicating with the user/domain owner until the need is clear enough to implement or explicitly marked blocked.

### Product Thinking And Clarification Loop

The product manager must run a clarification loop with the user/domain owner until the demand is clear, bounded, and testable. Do not hand off to developer, architect, tester, or codebase explorer while the core user need is still ambiguous.

Each clarification round should:

- Restate the user's need in product terms: target user, problem/job, desired outcome, context, and value.
- Ask focused questions about ambiguity, edge cases, priority, workflow, constraints, acceptance, and tradeoffs.
- Offer product options when useful, including MVP slice, complete workflow, manual fallback, phased release, or explicit non-goal.
- Record what changed after the user's answer: confirmed facts, rejected assumptions, open questions, scope changes, and evidence gaps.
- Decide whether another clarification round is needed before handoff.

Demand is ready for handoff only when target user, problem, outcome, scope boundary, acceptance criteria, priority/release slice, evidence or evidence gap, and confirmation owner are explicit. If the user cannot yet clarify, mark the product package as blocked or discovery-needed rather than pretending it is implementation-ready.

### User Need Completeness Checklist

The product manager must not treat a requested feature as complete demand until these items are explicit or marked as open questions:

- Target users / segments: who is affected, who decides, who operates, and who is excluded.
- User context: scenario, trigger, workflow moment, environment, constraints, and frequency.
- Problem and job: what the user is trying to accomplish, current pain, workaround, and why now.
- Desired outcome: user value, business value, success metric, and how improvement will be observed.
- Evidence: interview notes, domain-owner confirmation, analytics, support/sales signal, process record, competitive/domain reference, or explicit evidence gap.
- Scope boundary: in-scope behavior, non-goals, assumptions, dependencies, risks, privacy/security/accessibility concerns, and edge cases.
- Priority logic: impact, urgency, confidence, effort, dependencies, risk reduction, and release-slice rationale.
- Acceptance package: acceptance criteria, examples, negative cases, quality attributes, measurement plan, and confirmation owner.

### Product Manager Workflow

1. Discovery: collect user/domain evidence, segment users, identify jobs/pains, map current workflow, and separate problem statements from solution ideas.
2. Definition: write product problem statement, user-need statements, goals/non-goals, assumptions, constraints, risks, success metrics, and decision options.
3. Prioritization: compare candidate scope by user value, business value, risk, confidence, effort, dependencies, and learning value.
4. Specification: convert confirmed scope into PRD/spec, workflow, user stories or use cases, acceptance criteria, release slice, and measurement plan.
5. Alignment: confirm with user/domain owner and record stakeholder decisions, tradeoffs, unresolved questions, and evidence gaps.
6. Handoff: give downstream roles the confirmed spec, evidence links, open decisions, non-goals, risks, acceptance criteria, and completion status sync.
7. Learning: after delivery or feedback, update product assumptions, metrics, user-need patterns, and next-slice recommendations.

### Product Manager Handoff Gate

Before handing to developer, architect, tester, or codebase explorer, the product manager must provide:

- Product problem statement and target user segment.
- Confirmed use cases / user stories with actor, scenario, trigger, steps, expected result, and acceptance criteria.
- Evidence references or explicit evidence gaps.
- Scope, non-goals, assumptions, dependencies, and risks.
- Priority / release slice rationale.
- Outcome metric or observation signal.
- User/domain-owner confirmation status and remaining decisions.

If the product manager changes UI design, product workflow, scope, release slice, or acceptance criteria after a prior confirmation, it must create a new change proposal and get user/domain-owner confirmation before downstream implementation, testing, or release-readiness work proceeds.

### Product Manager Source Tracking

When online or external product-management references shape the role requirements, record the source link, source type, adopted capability, and date in the role workspace or product spec. Useful source families include product discovery, user-need statements, agile product-owner accountability, PRD/spec templates, prioritization frameworks, and product analytics guidance.


### Product Manager Reference Sources To Track

| Source | Adopted Capability | Usage In Role Skill |
| --- | --- | --- |
| [Nielsen Norman Group: Discovery Phase](https://www.nngroup.com/articles/discovery-phase/) | Discover the problem space before committing to design or build decisions | Require discovery, evidence, problem framing, and assumptions before scope handoff |
| [Nielsen Norman Group: User Need Statements](https://www.nngroup.com/articles/user-need-statements/) | Express needs as user, need, goal, and outcome rather than feature requests | Require user-need statements and user context in product packages |
| [GOV.UK Service Manual: Start By Learning User Needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) | Start service/product work by learning real user needs and context | Require user/domain evidence, target users, scenarios, constraints, and evidence gaps |
| [Scrum Guide: Product Owner](https://scrumguides.org/scrum-guide.html#product-owner) | Maintain product value, product goal, backlog clarity, ordering, and transparency | Require priority logic, release slicing, outcome metrics, and transparent decisions |


## Hard Constraint Gate Pattern

Hard constraints must be written as gates with owners, evidence, stop conditions, and human-participation classification. Use this pattern for user-facing product/UI/workflow changes, scope changes, acceptance-standard changes, governance/risk boundaries, release-readiness decisions, standardized production, and other mandatory project principles.

| Gate | Human Participation | Proposing Role | Enforcing Roles | Decision Owner | Required Evidence | Stop Condition |
| --- | --- | --- | --- | --- | --- | --- |
| Product/UI/workflow change confirmation | human-required for new aesthetic direction, taste, product meaning, user-value tradeoff, or changed acceptance meaning; delegated-review only if explicitly delegated | Product manager / workflow designer | Loop Manager, developer, tester, UI/frontend reviewer, release/governance owner when selected | User or domain owner unless explicitly delegated | Before/after summary, changed artifact or screenshot/design link, rationale, affected use cases, acceptance impact, confirmation record | No implementation, testing acceptance, or release-readiness work proceeds on the changed product/UI/workflow until confirmation evidence is recorded |
| Scope or acceptance criteria change | human-required unless the change is within a pre-confirmed standard rule | Demand intake or product manager | Loop Manager, developer, tester, code reviewer | User or domain owner | Changed scope, non-goals, acceptance criteria, affected tasks, decision record | Downstream roles use the last confirmed scope only; unconfirmed changes return as blockers |
| Standardized production with clear requirements | automated-pass | Responsible execution role | Loop Manager, tester/reviewer when selected | Delegated role owner | Confirmed requirement, objective checklist/test/script output, produced artifact, status sync | No user participation needed unless checks fail, ambiguity appears, or a confirmed constraint changes |
| Risk/governance/release boundary | human-required or delegated-review by authorized governance/release owner | Governance/risk owner or release owner | Loop Manager, developer, tester, project manager if selected | Governance owner, domain owner, or release owner | Risk decision, mitigation, rollback/monitoring plan, approval record | Release or high-risk action is blocked until approval evidence exists |

Role enforcement rule:

- Product manager proposes and records product/UI/workflow changes, then asks for confirmation.
- Loop Manager checks whether the gate has owner, evidence, decision status, and downstream blockers.
- Developer refuses to implement against unconfirmed product/UI/workflow changes.
- Tester refuses to mark acceptance against unconfirmed criteria.
- UI/frontend reviewer checks user-facing consistency and evidence but does not replace user confirmation.
- Project manager, when selected, checks workflow stage completeness but does not override the gate.
- Standardized production roles proceed without user interruption when requirements are clear, authority is delegated, checks pass, and evidence is recorded.

## Loop Manager Fixed-Time Retrospective Pattern

Every concrete project must have a Loop Manager and a fixed-time retrospective cadence. Use weekly as the default cadence unless the project defines a shorter cycle, milestone-based cadence, or incident-triggered review. At project creation, the Loop Manager also receives default automatic distillation time nodes: project-start baseline, task/stage completion checkpoint, weekly fixed retrospective, event-triggered review, and project-closure distillation.

The Loop Manager retrospective must treat the following as core distillation and adjustment targets:

- User-to-role communication efficiency: repeated clarification loops, slow answers, missing evidence, unclear decisions, mismatched expectations, and better question/confirmation formats.
- Role-to-role communication efficiency: handoff delay, incomplete handoff packages, stale status syncs, repeated rework, missing interaction records, and clearer message/document templates.
- Role responsibility optimization: overlapping authority, responsibility gaps, unclear gates, wrong handoff targets, roles doing out-of-boundary work, and role charter updates.
- Role skill/tool optimization: missing skills, underused skills, unavailable tools, weak checklists, insufficient references, required training, activation/install actions, and fallback quality.
- Project resource fit: people, agent/session availability, time budget, data/material access, external dependencies, and overloaded roles.
- Reusable learning: rules, templates, prompts, checklists, role definitions, skill updates, and project principles that should change before the next cycle.

The output must be recorded as concrete updates, not only observations: communication-rule updates, handoff-template updates, role-registry updates, role-charter changes, skill/tool readiness actions, training/checklist updates, and feedback to the Super Assistant.

### Role Skill Evolution Pattern

Every active role should gradually improve its own skill requirements with Loop Manager support. The role supplies domain-specific learning from real work; Loop Manager supplies cadence, evidence discipline, cross-role comparison, and artifact updates.

Track role-skill updates with this lifecycle:

```text
observed skill signal -> proposed update -> evidence review -> accepted/rejected -> artifact update -> next review
```

Valid skill signals include repeated blockers, user corrections, review findings, test gaps, missing tools, useful prompts, better checklists, new references, improved handoff packages, and changed capability sources.

| Date | Role | Skill Signal | Evidence | Proposed Skill / Checklist / Prompt / Tool Update | Target Artifact | Decision | Next Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | role workspace / role charter / candidate-role-library.md / implementation-covenant.md / generated template / SKILL.md | proposed / accepted / rejected / applied |  |

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
- [ ] Implementation covenant exists before execution, with role boundaries, communication content requirements, evidence requirements, handoff packages, status-sync rules, and escalation paths accepted.
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
        loop_dir / "implementation-covenant.md",
        f"""# {args.name} Implementation Covenant

This covenant is the shared operating agreement for all implementation roles. Individual role charters define each role's responsibilities; this covenant defines how selected roles work together without blurring boundaries, losing evidence, or relying on chat-only coordination.

## Covenant Gate

No implementation task is execution-ready until this covenant is drafted, reviewed with the selected active roles, and accepted by the user/domain owner or delegated Loop owner. The Loop Manager maintains this covenant and checks it during fixed-time retrospectives.

| Item | Status / Owner |
| --- | --- |
| Covenant owner | Loop Manager |
| Applies to | All selected implementation roles and role sessions |
| Accepted by | User / domain owner / delegated Loop owner |
| Acceptance evidence |  |
| Review cadence | Fixed-time retrospective; additionally after role changes, repeated handoff friction, boundary violations, or recurring evidence gaps |
| Current status | draft |

## Role Boundary Matrix

Each active implementation role must know what it owns, what it may decide, what it may edit, what it must not do, and when it must hand off.

| Role Category | Role / Session | Owns | May Decide | May Edit | Must Not Do | Handoff Trigger | Handoff Target | Boundary Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| demand-intake | Demand intake role | Demand clarification, use cases, acceptance draft | Whether demand is clear enough to ask for confirmation | Demand intake workspace, use-cases.md | Implement, test, approve release, or hand off unconfirmed use cases as ready | Scope/workflow design needed; implementation needed; evidence missing | Product/workflow, Loop owner, or Loop Manager | Confirmed use cases and open questions |
| product-workflow | Product manager / workflow designer | Product scope, workflow, user need, acceptance criteria, release slice | Product recommendation and scope options; not final business acceptance unless delegated | Product/workflow docs and assigned scope artifacts | Implement, test, approve business acceptance, or silently expand scope | Technical design, code exploration, implementation, test planning, domain decision | Codebase explorer, architect, developer, tester, domain owner | Product package and confirmation status |
| code-exploration | Codebase explorer / implementation researcher | Repo facts, entry points, patterns, dependencies | Findings and evidence-backed implementation paths | Exploration notes and assigned analysis docs | Final architecture, implementation, QA approval, or product scope decision | Architecture/design or implementation planning needed | Architect / developer | File references, dependency map, risks |
| architecture-design | Software architect / technical designer | Architecture/design blueprint | Technical design options within confirmed scope | Architecture/design docs and assigned ADRs | Implement without handoff, override product scope, declare QA pass | Build-ready design exists or scope conflict appears | Developer, product manager, Loop Manager | Design decision, tradeoffs, test strategy |
| development | Developer / implementer | Confirmed implementation slice | Local implementation details within confirmed design/scope | Assigned code/config/scripts and development notes | Redefine scope, declare QA passed, approve release, or bypass governance | Verification needed; scope unclear; risk/governance issue appears | Tester, reviewer, product manager, governance/risk, Loop Manager | Changed files, commands, build/test evidence |
| testing-evaluation | Tester / evaluator | Verification against use cases and acceptance criteria | Test findings and pass/fail evidence; not business acceptance unless delegated | Test/evaluation docs and assigned test files | Implement fixes silently, approve business acceptance, or rewrite product scope | Defect found; acceptance evidence ready; scope ambiguity appears | Developer, product manager, domain owner, Loop Manager | Test plan, results, defects, evidence |
| code-review | Code reviewer / quality reviewer | Diff review and maintainability/correctness findings | Review findings and severity recommendations | Review notes and assigned review docs | Rewrite scope, perform business acceptance, or make release decisions | Fix required; specialized review needed; risk unresolved | Developer, specialized reviewer, Loop Manager | Findings with file references |
| governance-risk | Governance or risk owner | Risk, policy, permission, compliance boundaries | Governance/risk recommendations or approvals within delegated authority | Governance/risk docs | Product ownership, implementation, or QA conclusions | Risk decision needed or mitigation required | Domain owner, developer, Loop Manager | Risk decision, mitigation, residual risk |

## Communication Content Requirements

Every role-to-role message, handoff, question, answer, blocker report, advice, status sync, defect report, acceptance feedback, disagreement, implementation claim, or update proposal must be recorded in `interaction-evidence-log.md`, the sender/receiver category workspace, or another named project document.

Each recorded interaction must include these fields:

| Required Field | Meaning |
| --- | --- |
| Date / time | When the interaction happened |
| Sender role ID / role category | Who sends the message |
| Receiver role ID / role category | Who must act or know |
| Task ID / goal ID | Which dispatch, goal, use case, defect, or decision this concerns |
| Interaction type | handoff / question / answer / advice / role-status-sync / blocker / defect / acceptance-feedback / decision-request / disagreement / update-proposal / role-change-broadcast |
| Context | Why this message exists and what prior artifact it depends on |
| Summary | Short factual description of the message |
| Requested action / decision / next step | What the receiver should do or decide |
| Evidence / links | Local document path, online link, artifact reference, data source, log, test output, screenshot, ticket, pull request, or decision record |
| Evidence gap | Missing material and whether it blocks execution |
| Boundary check | Whether the request is inside the receiver's authority; if not, handoff target |
| Blocker / risk | Any blocker, risk, ambiguity, or dependency |
| Follow-up owner | Who owns the next action |
| Due point / next sync | Deadline, cadence, or next checkpoint |
| Status | draft / sent / received / waiting / active / blocked / resolved / closed |

## Message Type Rules

| Interaction Type | Required Extra Content | Not Execution-Ready If Missing |
| --- | --- | --- |
| handoff | Source materials, completed work, current state, open questions, acceptance criteria, risks, next owner | Receiver cannot identify scope, evidence, or next action |
| question | Specific uncertainty, affected task/use case, decision options if known, deadline | Question is broad, context-free, or not assigned to a receiver |
| answer | Direct answer, confidence, evidence, assumptions, remaining gaps | Answer has no evidence and affects implementation, testing, or acceptance |
| advice | Recommendation, rationale, tradeoff, risk, whether confirmation is needed | Advice is mixed with confirmed scope without marking status |
| role-status-sync | Current state, completed work/progress, evidence, blockers, next handoff, ETA/completion time | Missing on task start, blocker, handoff, or completion |
| blocker | Blocking condition, owner, impact, attempted resolution, decision needed, next check | Owner or required decision is unclear |
| defect | Repro steps, expected/actual result, evidence, severity, affected use case, environment | Developer cannot reproduce or affected standard is unclear |
| acceptance-feedback | Acceptance criteria checked, pass/fail evidence, unresolved risk, decision owner | Business acceptance is implied without domain/user confirmation |
| decision-request | Options, evidence, impact, recommendation, decision owner, deadline | Decision changes scope/risk/authority without user/domain-owner path |
| disagreement | Roles involved, issue, direct resolution attempt, options, impact, escalation status | Scope/risk/authority/schedule impact is hidden |
| update-proposal | Artifact to update, reason, evidence, owner, expected improvement | Proposal has no target artifact or owner |
| role-change-broadcast | Changed role, change type, reason, effective time, boundary/handoff impact, required action | Active roles are not notified or records are missing |

## Hard Constraint Gates

Hard constraints are mandatory gates. A gate is open until the required decision owner confirms it and the evidence is recorded, unless the gate is classified as `automated-pass`. Downstream roles must treat open human-required gates as blockers.

Example: if the product manager / workflow designer changes UI design, product workflow, scope, release slice, or acceptance criteria, the change remains a proposal until the user/domain owner confirms it. Developer implementation, tester acceptance, UI/frontend approval, and release-readiness work must use the last confirmed version until confirmation evidence is recorded.

Use `human-required` for aesthetic judgment, taste, brand feel, product direction, user value tradeoffs, ambiguous demand, governance/risk authorization, or changed confirmed constraints. Use `automated-pass` for standardized production when requirements are clear, authority is delegated, objective checks pass, evidence is recorded, and no confirmed constraint changes.

| Gate ID | Constraint | Human Participation | Trigger | Proposing Role | Enforcing Roles | Decision Owner | Required Evidence | Stop Condition | Record Location | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HCG-001 | Product/UI/workflow changes require user/domain-owner confirmation | human-required for new aesthetic/product/value/meaning decisions; delegated-review only if explicitly delegated | Product manager changes UI design, workflow, scope, release slice, or acceptance criteria | product-workflow | Loop Manager; development; testing-evaluation; frontend-ux; release/governance owner when selected | User / domain owner / delegated Loop owner | Before/after summary, changed artifact or screenshot/design link, affected use cases, acceptance impact, confirmation record | No implementation, test acceptance, UI approval, or release-readiness work proceeds on the changed item | interaction-evidence-log.md / product workspace / stage-confirmation-checklist.md | draft |
| HCG-002 | Standardized production with clear requirements may proceed without user participation | automated-pass | Requirement is confirmed, repeatable, low-risk, and objectively checkable | responsible execution role | Loop Manager; tester/reviewer when selected | Delegated role owner | Confirmed requirement, objective checklist/test/script output, produced artifact, status sync | Escalate to human-required or delegated-review if checks fail, ambiguity appears, or a confirmed constraint changes | interaction-evidence-log.md / role workspace | draft |
|  |  | human-required / delegated-review / automated-pass |  |  |  |  |  |  |  | draft / waiting-confirmation / confirmed / blocked / automated-pass / closed |

## Gate Enforcement By Role

| Role Category | Gate Responsibility |
| --- | --- |
| product-workflow | Propose product/UI/workflow changes with before/after evidence, impact, and confirmation request; do not hand off changed scope as ready until confirmed |
| loop-manager | Track gate status, stop handoffs with missing confirmation, record blockers, and ask the decision owner to confirm |
| development | Refuse implementation against unconfirmed product/UI/workflow/scope/acceptance changes |
| testing-evaluation | Refuse acceptance against unconfirmed criteria or changed workflows |
| frontend-ux | Review user-facing consistency and evidence, but do not replace user/domain-owner confirmation |
| project-management | Check workflow-stage completeness when selected; do not override gate decisions |
| governance-risk / release | Block release or high-risk action until required approval evidence exists |
| standardized execution roles | Proceed without user interruption when requirements are clear, authority is delegated, objective checks pass, and evidence is recorded; escalate when subjective judgment or ambiguity appears |

## Handoff Package Standard

A handoff package must include:

- Task ID / goal ID / use case ID.
- Sending role and receiving role.
- Current state and completed work.
- Source materials and evidence links.
- Scope, non-goals, assumptions, risks, and open questions.
- Acceptance criteria or quality gate relevant to the receiver.
- Files, docs, tickets, logs, screenshots, PRs, or artifacts the receiver should inspect.
- Evidence gaps and whether they block execution.
- Expected output and return format.
- Status-sync cadence and completion-sync requirement.

## Boundary Violation Handling

When a role is asked to decide, edit, approve, or execute outside its boundary, it must:

```text
state role position -> state boundary -> identify out-of-scope item -> stop local action -> hand off to responsible role -> record handoff -> wait for returned evidence or decision
```

## Disagreement And Escalation

Roles should communicate directly first for ordinary disagreements about assigned tasks, evidence, standards, implementation approach, or test interpretation. Escalate to Loop Manager when disagreement affects scope, acceptance criteria, risk boundary, schedule, resource allocation, role authority, release readiness, or cannot be resolved quickly. Loop Manager prepares the decision packet; user/domain owner decides unresolved high-impact issues.

## Covenant Review And Updates

Loop Manager reviews this covenant during fixed-time retrospectives and after repeated communication friction, handoff failures, stale status syncs, boundary confusion, role changes, or recurring evidence gaps.

| Date | Trigger | Covenant Gap | Proposed Update | Affected Roles | Decision Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
|  | fixed-time review / role change / handoff failure / boundary issue / evidence gap |  |  |  | Loop Manager / user / domain owner | draft |
""",
        args.force,
    )

    write_text(
        loop_dir / "role-loop-charters.md",
        f"""# {args.name} Role Loop Charters

Each active role or subagent must carry explicit Loop responsibilities. Do not create a role that only has a name, folder, or session. Candidate charters below are reusable presets; they do not activate a role by themselves.

Every role is also an advisor. The charter must make room for role-specific best-practice recommendations, risk warnings, assumptions, options, and confirmation needs.

## Charter Map

| Role / Subagent | Role Category | Goal | Implementation Standard | Constraints | Inputs | Outputs | Records | Evaluation / Feedback | Update Responsibility | Category Workspace | Handoff Rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Demand intake role | demand-intake | Turn rough demand into confirmed executable use cases | Demand record and use cases have actor, scenario, trigger, steps, measurable acceptance standard, constraints, records, feedback signal, owner, and confirmation status | Do not invent high-risk business facts; do not hand off vague ideas as implementation-ready | User request, context, constraints | Refined demand, use cases, open questions, confirmation packet | Demand intake record, use-cases.md, assumptions | User confirmation, ambiguity resolved, use cases executable and measurable | Update demand record and use cases before team formation | `roles/demand-intake/` | Hand off confirmed use cases to Loop owner and implementation roles |
| Loop Manager | loop-manager | Govern the whole Loop from project start | Registry, fixed-time retrospectives, communication-efficiency review, responsibility/skill optimization, status, risks, decisions, blockers, handoffs, role health checks, resource status, role self-reviews, experience distillation checks, advice summaries, and reflection are current | Do not do development, testing conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, or silently edit skill files | Loop artifacts, role outputs, feedback, gate results, role self-reviews, health/resource signals | Project status, role health report, resource report, reflection summary, role self-review tracker, experience distillation status, role advice summary, improvement proposals | Project status, reflection log, health/resource log, role self-review tracker, role advice summary, feedback to Super Assistant | Stage progress, blockers, recurring failures, role health, resources, role self-review completion, experience captured, role advice surfaced, skill-update candidates | Require role self-review, check role health/resources, verify experience distillation, collect role advice, and send improvement proposals to Super Assistant | `roles/loop-manager/` | Hand off execution to responsible roles; hand off delivery logistics to project manager if selected; send skill feedback to Super Assistant |
| Super Assistant / Loop owner | super-assistant | Drive the Loop end to end | Loop artifacts, handoffs, gates, and updates stay current | Do not perform out-of-scope role work silently | Confirmed demand, role outputs, feedback | Coordination, review, updates | Handoff log, update log, review notes | Gate status, unresolved risks, user feedback | Update Loop artifacts and next-round rules | `roles/super-assistant/` | Hand off role-specific execution to responsible roles |
| Project manager / delivery coordinator | project-management | Translate user demand into verifiable acceptance standards for confirmation and coordinate delivery logistics when selected | Acceptance standards, milestones, dependency updates, stakeholder status, and delivery risks are current | Do not treat private understanding as execution permission, govern Loop learning, maintain role health, replace Loop Manager, decide product scope, implement, test, approve release, or own experience distillation | User demand, confirmed plan, milestones, dependencies, stakeholder needs | Acceptance translation packet, delivery status, milestone/dependency tracker, stakeholder updates | Acceptance confirmation record, delivery log, dependency tracker, status summaries | Acceptance standards confirmed before dispatch; milestones and dependencies visible; Loop Manager can see resource/schedule risks | Update acceptance/delivery coordination artifacts, not Loop governance artifacts | `roles/project-management/` | Hand off Loop governance to Loop Manager; product meaning/scope questions to product/domain owner; implementation to developer |
| Product manager / workflow designer | product-workflow | Turn confirmed use cases into complete user-need understanding, product/workflow scope, and acceptance standards | Product thinking and user clarification loop are complete: target users, user context, problem/job, outcome metric, scope, workflow, non-goals, risks, release slices, and acceptance standards are explicit and confirmed | Do not implement, test, approve business acceptance, ignore evidence gaps, expand scope silently, or hand off ambiguous demand as ready | Confirmed use cases, domain constraints, user feedback/evidence, analytics or process signals | Product problem statement, user-need statements, clarification rounds, workflow, acceptance criteria, release slice recommendation, measurement plan | User evidence, product decisions, assumptions, tradeoffs, priority rationale, scope changes, open questions, clarification history | Domain/user confirmation, ambiguity reduced, developer/tester can act from evidence | Continue user clarification until demand is clear or blocked; update product assumptions, scope, standards, and next-slice recommendations before development handoff | `roles/product-workflow/` | Hand off only confirmed product package to developer/architect/codebase explorer and evidence review to tester |
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
| Product manager / workflow designer | software | product/workflow scope | Confirmed use cases and user/domain evidence or explicit evidence gaps | Product problem statement, target users, user-need statements, scope, workflow, acceptance criteria, outcome metric, release slice, hard-constraint change proposals when needed | Sync before scope handoff and completion | Scope, UI/product/workflow changes, and remaining evidence gaps confirmed by user/domain owner | Codebase explorer, architect, developer, or tester | User need confirmation, scope confirmation, product/UI/workflow change confirmation, evidence-gap disclosure |
| Codebase explorer / implementation researcher | software | codebase exploration | Confirmed scope and repo area | Entry points, data flow, patterns, risks | Sync findings before architecture handoff and completion | Findings cite files/evidence | Software architect | Evidence-backed exploration |
| Software architect / technical designer | software | architecture/design | Scope and exploration notes | Architecture decision, build sequence, test strategy | Sync design before implementation handoff and completion | Design fits repo patterns and constraints | Developer / implementer | Architecture gate |
| Developer / implementer | software | implementation | Confirmed design/scope and closed hard-constraint gates | Code/config/scripts, build evidence | Sync on start, blocker, handoff, and completion | Runnable implementation with evidence; no unconfirmed product/UI/workflow/scope changes | Tester/evaluator and reviewers | Hard constraint confirmation, test/review handoff |
| Tester / evaluator | software | testing/evaluation | Use cases, acceptance criteria, implementation evidence, closed hard-constraint gates | Test plan, results, defects, risks | Sync findings and completion before acceptance handoff | Evidence-based pass/fail against confirmed criteria | Developer or domain owner | Hard constraint confirmation, test evidence |
| Project manager / delivery coordinator | software / product / agent / workflow / research / other | acceptance translation and workflow coordination | User demand, project type, and selected workflow | Verifiable acceptance standards, confirmation record, workflow stage map, milestone/dependency status | Sync acceptance confirmation and delivery status to project owner at cadence and on flow changes | No dispatch before acceptance standards are confirmed; no required stage silently skipped | Responsible next role / Loop owner | Acceptance translation confirmation and project-type workflow completeness |
| Loop Manager | all | Loop governance | Role registry, workflow map, role outputs, communication-efficiency signals, responsibility/skill improvement signals | Health/resource/status/workflow/communication/responsibility/skill gap checks | Monitor stale syncs; request updates | Governance artifacts current | Super Assistant / responsible role | Role execution boundaries |
|  |  |  |  |  |  |  |  |  |

## Advisor Contribution Record

| Role / Subagent | Best-Practice Suggestions | Risks / Anti-Patterns | Options / Tradeoffs | Assumptions | Confirmation Needed |
| --- | --- | --- | --- | --- | --- |
| Demand intake role |  |  |  |  |  |
| Loop Manager | Collect role advice, check role health/resources, review communication efficiency, optimize role responsibilities/skills, and verify experience distillation for user/domain-owner/Super Assistant decisions | One-way command management hides role expertise and role decay | Prompt user with options versus decide internally |  |  |
| Project manager / delivery coordinator | Surface delivery risks, dependency delays, and stakeholder status | Delivery logistics can be confused with Loop governance | Coordinate schedule versus ask Loop Manager for Loop-level decision |  |  |
| Product manager / workflow designer | Recommend user-need framing, scope slices, workflows, acceptance standards, metrics, and non-goals | Feature-list thinking, ambiguous value, missing evidence, or scope creep | MVP versus complete workflow; learning slice versus delivery slice |  |  |
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

- [ ] Project owner translated the user's demand into verifiable acceptance standards before dispatch or execution.
- [ ] User wording, interpretation, assumptions, questions, acceptance standards, evidence requirements, and confirmation owner are separate.
- [ ] The user/domain owner or delegated decision owner confirmed the acceptance standards, or the work is blocked/discovery-needed.
- [ ] The stage knowledge base has been reviewed.
- [ ] Each stage has a goal, implementation standard, constraints, workflow, principles, inputs, outputs, and records.
- [ ] Stage inputs and outputs connect clearly.
- [ ] Hard constraint gates are identified, including user/domain-owner confirmation needed for product, UI, workflow, scope, acceptance, risk, governance, or release changes.
- [ ] Human participation is classified: aesthetic/product/value/risk/authorization/ambiguity points are human-required; standardized clear production may be automated-pass.
- [ ] Open questions are recorded with owners and dates.

## Stage Confirmation

| Stage | Goal | Standard | Constraints | Workflow | Principles | Records | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |

## Acceptance Translation Confirmation

| Work Item / Goal ID | User Demand In Original Words | Interpreted Goal / Scenario | Verifiable Acceptance Standards | Evidence Required | Human Participation | Confirmation Owner | Confirmation Record | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | observable pass/fail checks | implementation/test/review/release evidence | human-required / delegated-review / automated-pass | user / domain owner / delegated decision owner |  | draft / confirmed / blocked |

## Hard Constraint And Human Participation Confirmation

| Gate ID | Constraint | Human Participation | Changed Artifact / Stage | Decision Owner | Confirmation Or Automated Evidence | Downstream Roles Blocked Until Confirmed | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HCG-001 | Product/UI/workflow changes require user/domain-owner confirmation | human-required / delegated-review | UI design / workflow / scope / acceptance criteria | User / domain owner / delegated Loop owner |  | developer / tester / UI reviewer / release owner | draft |
| HCG-002 | Standardized production with clear requirements may proceed without user participation | automated-pass | Repeatable production step | Delegated role owner | Objective checklist/test/script output and status sync | none unless checks fail or ambiguity appears | draft |

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
- Role split rule: start with Loop Manager plus 2-3 other active roles. Let Loop Manager split, activate, merge, pause, or close roles only when evidence shows the current role set is overloaded, unclear, risky, missing specialist skill, or causing repeated handoff/status/evidence friction.
- Role boundary rule: before acting, each role must identify its position, responsibility boundary, editable artifacts, and required handoffs. If it would need to make a decision, do work, or modify files, systems, tools, data, or artifacts outside its responsibility, it must state the boundary, stop the action, and hand off to the responsible role or subagent.
- Project owner acceptance rule: before dispatch or execution, the project owner function must translate user demand into verifiable acceptance standards, evidence requirements, assumptions, confirmation questions, and a confirmation record. Understanding the user privately is not execution permission.
- Hard constraint gate rule: before implementation, testing, acceptance, or release-readiness work, check whether the task depends on a changed product, UI design, workflow, scope, acceptance standard, risk boundary, or release condition. If the required user/domain-owner confirmation is missing, record the blocker and stop the downstream action.
- Human participation rule: require human input for aesthetic judgment, taste, product direction, user value tradeoffs, ambiguous demand, risk/governance authorization, or changed confirmed constraints. Standardized production can proceed without user input when requirements are clear, authority is delegated, objective checks pass, and evidence is recorded.
- Tool and skill readiness rule: before a role starts execution, verify its required skills, tools, scripts, references, data access, and permissions. If any required capability is missing, install it, activate it, substitute it, downgrade scope, or mark the role blocked.
- Implementation covenant rule: before execution, confirm `implementation-covenant.md` defines role boundaries, communication content requirements, evidence rules, handoff packages, status-sync rules, and escalation paths for all selected implementation roles.
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
- Keep early projects small. Candidate roles listed in planning files are not active until confirmed, registered, and broadcast by Loop Manager.
- Update this registry when a role is created, confirmed, activated, paused, blocked, replaced, closed, or its concrete person/agent/session changes.
- Update `project-metadata.md` whenever role information, division of work, project owner function, workspace ownership, or thread/session basics change.
- After any role/personnel/session change, notify every other active role and record the broadcast in `interaction-evidence-log.md`; also record or summarize it in affected role workspaces.
- Use `Role ID` in `goal-dispatch-log.md` for every task dispatch.
- If no registered role can own a task, record the dispatch as blocked and start role-selection confirmation instead of assigning the work informally.
- Loop Manager manages this registry but must not perform role-specific implementation work.
- Loop Manager must review communication efficiency, responsibility fit, and skill/tool gaps at the fixed-time retrospective cadence and record concrete adjustment proposals.

## Active Roles

| Role ID | Role / Subagent | Role Category | Concrete Person / Agent / Session | Category Workspace | Authority Boundary | Owns | Must Hand Off | Required Tools / Skills | Readiness | Health / Resource Status | Last Self-Review | Experience Distilled? | Status | Current Task | Blocker | Last Updated | Updated By |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LM-001 | Loop Manager | loop-manager | dedicated Loop Manager session when Codex is used | `roles/loop-manager/` | Govern Loop registry, cadence, fixed-time retrospectives, communication efficiency, role responsibility/skill optimization, role health, resources, status, blockers, handoffs, advice, reflection, and dispatch; do not perform role-specific or delivery execution | Role registry, dispatch log, status, risks, decisions, blocker tracking, communication-efficiency tracking, responsibility/skill improvement backlog, health/resource tracking, experience distillation checks, reflection | Development, testing conclusions, business acceptance, governance decisions, release, project-manager delivery execution, role-specific implementation | loop-builder; Loop governance and retrospection practices | available | healthy / resources available |  |  | active |  |  |  | Loop Manager |
| SA-001 | Super Assistant / Loop owner | super-assistant | current coordination session | `roles/super-assistant/` | Own and coordinate the Loop end to end; hand off role-specific work | Loop coordination, handoff records, review notes, update proposals | Development, testing conclusions, governance decisions, production config unless assigned | loop-builder | available | healthy / resources available |  |  | active |  |  |  | Loop Manager |
| DI-001 | Demand intake role | demand-intake | dedicated intake session if Codex is used | `roles/demand-intake/` | Clarify rough demand and produce confirmed executable use cases; do not perform implementation, testing, release, governance, or domain acceptance | Demand intake record, use cases, assumptions, open questions, confirmation packet | Product scope beyond confirmed input, implementation, testing, release, governance, domain acceptance | loop-builder; grill-me when available | available / check needed | healthy / resources available |  |  | active |  |  |  | Loop Manager |
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

When using Codex, each active role or subagent should run in its own thread/session with a scoped prompt and its assigned workspace. The Super Assistant remains in the coordinating thread/session. Early projects should usually use Loop Manager plus 2-3 other role sessions at most; candidate sessions below are not created until the role is confirmed and registered.

Loop Manager must mirror thread/session basics in `project-metadata.md` whenever a role session is created, activated, paused, replaced, closed, or repurposed.

## Codex Session Map

| Role Category | Role / Subagent | Codex Thread / Session | Category Workspace | Session Scope | Receives From | Returns To |
| --- | --- | --- | --- | --- | --- | --- |
| demand-intake | Demand intake role | dedicated intake session if Codex is used | `roles/demand-intake/` | Receive, clarify, refine, and confirm demand | User / requester | Super Assistant |
| loop-manager | Loop Manager | dedicated Loop Manager session when Codex is used | `roles/loop-manager/` | Govern Loop cadence, fixed-time retrospectives, role registry, communication efficiency, role responsibility/skill optimization, role health, resource status, role self-review, experience distillation, reflection, risks, blockers, and feedback to Super Assistant | Super Assistant and role outputs | Super Assistant |
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

## Acceptance Translation Before Dispatch

The project owner function must translate user demand into verifiable acceptance standards before dispatch. Private understanding is not execution permission.

| Date | Goal ID | User Demand In Original Words | Interpreted Goal / Scenario | Verifiable Acceptance Standards | Evidence Required | Confirmation Owner | Confirmation Record | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | observable pass/fail checks | implementation/test/review/release evidence | user / domain owner / delegated decision owner |  | draft / waiting-confirmation / confirmed / blocked |

## Goal Contract

| Date | Goal ID | User Goal | Refined Goal | Scope | Non-Goals | Acceptance Standard | Constraints | Source Materials / Links | Confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  | draft |

## Dispatch Packet

| Date | Task ID | Goal ID | Registry Role ID | Target Role / Session | Role Category | Project Type | Workflow Stage | Category Workspace | Authority Boundary | Required Knowledge Base | Required Tools / Skills | Inputs / Links | Verifiable Acceptance Standards / Confirmation | Expected Output | Definition Of Done | Evidence Required | Project Owner | Status Sync Cadence | Completion Sync Required | Return Format | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | software / product / agent / workflow / research / other |  |  |  |  |  |  | confirmed standards and confirmation record |  |  |  | Super Assistant / Loop owner | before handoff; on blocker; on completion; periodic cadence TBD | yes |  | waiting |

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

Every active role category or subagent category must have an independent workspace folder under `roles/`. A role category is a reusable responsibility type, not every individual person, agent, session, or task instance. Multiple concrete roles or sessions in the same category may share the category folder when they have the same responsibility boundary and record type. Separate folders/files are allowed for active roles or explicitly prepared roles when they clarify ownership. Candidate workspace paths below are reservations unless the role is selected or the user/domain owner asks for a prepared file.

## Workspace Map

| Role Category | Role / Subagent | Codex Thread / Session | Category Workspace | Concrete Roles / Sessions Sharing Folder | Owns | May Edit | Must Hand Off |
| --- | --- | --- | --- | --- | --- | --- | --- |
| demand-intake | Demand intake role | dedicated intake session if Codex is used | `roles/demand-intake/` | Demand intake agents/sessions with the same intake boundary | Initial demand record, refinement, open questions, acceptance criteria | Its category workspace and confirmed demand artifacts | Implementation, testing, release, governance, domain acceptance |
| loop-manager | Loop Manager | dedicated Loop Manager session when Codex is used | `roles/loop-manager/` | Loop Manager sessions for this Loop | Project metadata, active role registry, Loop cadence, fixed-time retrospectives, communication-efficiency review, role responsibility/skill optimization, role health checks, resource status, decisions, blockers, role self-review, experience distillation checks, role advice summary, reflection, feedback to Super Assistant | Its category workspace, `project-metadata.md`, `role-registry.md`, project status, role health tracker, resource status, role self-review tracker, experience distillation status, role advice summary, reflection records, improvement proposals | Development, test conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, role-specific execution, skill edits unless delegated |
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

Every role-to-role message must be recorded here or in another named project document listed in `document-index.md`. Every interaction should include detailed supporting material when available: a local document/material path, online document link, artifact reference, data source, log, test output, screenshot, ticket, pull request, or decision record.

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
        if slug == "product-workflow":
            role_specific_capability = """
## Product Manager Capability Baseline

This role must fully consider user needs before turning demand into build scope. It must think like a product owner, not a task transcriber: challenge unclear requests, explore user value, compare options, identify non-goals, and keep communicating with the user/domain owner until the need is clear enough to implement or explicitly blocked. A requested feature is not implementation-ready until the role has either documented or explicitly marked open questions for:

- Target users / segments, decision makers, operators, and excluded users.
- User context, trigger, workflow moment, frequency, constraints, and edge cases.
- Problem/job, current pain or workaround, desired outcome, and why this matters now.
- User value, business value, outcome metric, observation signal, and measurement plan.
- Evidence source: interview, domain-owner confirmation, analytics, support/sales signal, process record, domain reference, or evidence gap.
- Scope, non-goals, assumptions, dependencies, risks, privacy/security/accessibility considerations, and release-slice rationale.
- Acceptance criteria, examples, negative cases, quality attributes, confirmation owner, and remaining decisions.

## Product Clarification Loop

Repeat this loop until the demand is clear, bounded, and testable:

1. Restate the user's need in product terms: target user, problem/job, desired outcome, context, and value.
2. Ask focused questions about ambiguity, edge cases, priority, workflow, constraints, acceptance, and tradeoffs.
3. Offer product options when useful: MVP slice, complete workflow, manual fallback, phased release, or explicit non-goal.
4. Record what changed after the user's answer: confirmed facts, rejected assumptions, open questions, scope changes, and evidence gaps.
5. Decide whether another clarification round is needed before handoff.

| Round | User / Domain Input | Product Restatement | Questions Asked | User Answer | Confirmed Facts | Rejected Assumptions | Open Questions | Scope / Acceptance Change | Need Another Round? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  | yes / no |

Before handoff, provide a product package with problem statement, user-need statements, confirmed use cases/user stories, workflow, acceptance criteria, evidence links or gaps, priority rationale, outcome metric, scope/non-goals, risks, and user/domain-owner confirmation status.
"""
        else:
            role_specific_capability = ""
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

## Hard Constraint Gate Responsibility

This role must enforce hard constraints at its workflow stage. If a received task depends on an unconfirmed product/UI/workflow/scope/acceptance/risk/release change, stop execution, record the blocker, and return it to the responsible role or Loop Manager. If the task is standardized production with clear requirements, delegated authority, objective checks, and no changed confirmed constraint, it can proceed as `automated-pass` without user participation.

| Gate ID | Constraint | Human Participation | This Role's Enforcement Duty | Required Confirmation / Evidence | Blocked Action If Missing | Status |
| --- | --- | --- | --- | --- | --- | --- |
| HCG-001 | Product/UI/workflow changes require user/domain-owner confirmation | human-required / delegated-review | Check whether this role is asked to act on changed product/UI/workflow/scope/acceptance content | Confirmation record, changed artifact, before/after summary, affected use cases | implementation / acceptance / UI approval / release-readiness / handoff | draft |
| HCG-002 | Standardized production with clear requirements may proceed without user participation | automated-pass | Check whether requirements are stable, objective checks exist, and no confirmed constraint changed | Confirmed requirement, checklist/test/script output, produced artifact, status sync | escalate to human-required if checks fail or ambiguity appears | draft |

{use_case_responsibility}
{role_specific_capability}
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

Tasks assigned to this role by Loop Manager must arrive as dispatch packets that reference this role's registry ID in `role-registry.md`. This role executes only packets within its authority boundary. Each packet must define confirmed verifiable acceptance standards, the project owner, status-sync cadence, and whether completion sync is required.

| Date | Task ID | Goal ID | Registry Role ID | Project Type | Workflow Stage | Objective | Source Materials / Links | Verifiable Acceptance Standards / Confirmation | Expected Output | Definition Of Done | Evidence Required | Project Owner | Status Sync Cadence | Completion Sync Required | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | software / product / agent / workflow / research / other |  |  |  | confirmed standards and confirmation record |  |  |  | Super Assistant / Loop owner | before handoff; on blocker; on completion; periodic cadence TBD | yes |  |

## Acceptance Standards Before Execution

- [ ] The task includes confirmed verifiable acceptance standards.
- [ ] User wording, interpretation, assumptions, and open questions are separate.
- [ ] Evidence requirements are clear enough for this role to return proof.
- [ ] Human participation classification is clear: human-required, delegated-review, or automated-pass.
- [ ] If standards are missing, ambiguous, unconfirmed, or not testable, mark the task blocked/discovery-needed and sync to the project owner.

## Project Owner Status Sync

This role must sync task status to the project owner during task flow at the cadence defined in its dispatch packet. Completion sync is mandatory before handoff, return, closure, or acceptance. Record each sync here and in `interaction-evidence-log.md` as `role-status-sync`.

| Date / Time | Task ID | Goal ID | Registry Role ID | Project Owner | Sync Type | Current State | Completed Work / Progress | Evidence / Links | Blocker / Risk | Next Handoff | Decision Needed | Next Sync Due | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Super Assistant / Loop owner | start / periodic / blocker / handoff / completion | waiting / active / blocked / completed / returned |  |  |  |  |  |  | draft |

## Self-Review

At the cadence defined by the Loop Manager, review this role's conversations, outputs, and feedback. Distill:

- Standards discovered:
- Feedback received:
- Communication friction with user or other roles:
- Responsibility boundary confusion, overlap, or gaps:
- Skill/tool gaps or improvement opportunities:
- Experience worth reusing:
- Mistakes or surprises:
- Proposed updates to role charter, stage knowledge, communication rules, handoff templates, skills/tools, tests, or the Loop skill:

## Skill Evolution Notes

Use this section to help Loop Manager gradually optimize this role's skills and working standards.

| Date | Skill / Tool / Prompt / Checklist Signal | Evidence | Proposed Update | Target Artifact | Sent To Loop Manager? | Status |
| --- | --- | --- | --- | --- | --- | --- |
|  | missing skill / useful technique / repeated mistake / better prompt / tool gap / reference gap |  |  | role workspace / role charter / candidate-role-library.md / implementation-covenant.md / template / SKILL.md | yes / no | proposed / accepted / rejected / applied |

## May Edit

- This category workspace.
- Files explicitly assigned to this category by `implementation-plan.md` or `role-workspaces.md`.

## Must Hand Off

- Any file, system, data, tool, or artifact outside this role category's assigned authority.

## Interaction Message And Evidence

- Record every role-to-role message or interaction in `interaction-evidence-log.md`, this category workspace, or another named project document.
- Include document/material paths, online document links, artifact references, data sources, logs, test output, screenshots, tickets, pull requests, or decision records when available.
- If supporting material is missing, check `document-index.md` first, then reuse or update an existing document when possible. Create the smallest useful new document only when the index shows it is necessary; otherwise request it from the responsible role or mark an evidence gap before treating the interaction as execution-ready.
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

## Communication Efficiency Review

| Area | Friction Observed | Cause | Proposed Update | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| User-to-role communication |  |  |  | Loop Manager | draft |
| Role-to-role communication |  |  |  | Loop Manager | draft |
| Handoff / status sync |  |  |  | Loop Manager | draft |

## Role Responsibility And Skill Optimization

| Role | Responsibility Overlap / Gap | Skill / Tool Gap | Proposed Role Charter Update | Proposed Skill / Tool Update | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Loop Manager | draft |

## Top Feedback Patterns

1. 
2. 
3. 

## Root Causes

- 

## Updates To Make

- Communication rule:
- Role responsibility / charter:
- Role skill / tool readiness:
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
