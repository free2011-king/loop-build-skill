# Loop Artifact Pack

Read this reference when scaffolding Loop files, checking generated artifact responsibilities, or validating whether a Loop design is complete.

## Contents

- [Scaffold Command](#scaffold-command)
- [Generated Files](#generated-files)
- [Customization Rules](#customization-rules)
- [Confirmation Gates](#confirmation-gates)
- [Loop Quality Test](#loop-quality-test)

## Scaffold Command

When file creation is appropriate, create the Loop pack with:

```bash
python <skill-dir>/scripts/create_loop_pack.py "<loop name>" --out loops --type "<loop type>" --slug "<ascii-slug>"
```

Default location inside a project is:

```text
loops/<loop-slug>/
```

## Generated Files

The scaffold creates these project artifacts:

- `loop-design.md`: Loop object, minimum viable loop, records, signals, update mechanism, and first build order.
- `document-index.md`: single index controlling user/owner-created and managed documents, document budgets, purpose, status, review cadence, and merge/archive decisions.
- `team-formation.md`: demand intake, small initial role set, existing-role selection, deferred candidate roles, split triggers, excluded candidate roles, tool/skill readiness, and requester confirmation.
- `candidate-role-library.md`: reusable candidate roles with best-practice skill, tool, knowledge-base, record, handoff matches, and capability-source tracking for ECC / Everything Claude Code, Claude Code plugins, skills, tools, and external references.
- `use-cases.md`: concrete, measurable use cases created by demand intake.
- `role-loop-charters.md`: role goals, standards, constraints, records, evaluation/feedback, update duties, authority, and handoffs.
- `loop-manager.md`: Loop cadence, default automatic distillation time nodes, fixed-time retrospectives, role health, resources, self-review, experience distillation, communication-efficiency review, responsibility/skill optimization, role skill-evolution tracking, reflection, and feedback to Super Assistant.
- `stage-knowledge-base.md`: per-stage goals, standards, constraints, workflows, principles, outputs, and records.
- `stage-confirmation-checklist.md`: requester/domain-owner confirmation gate for the stage knowledge base.
- `implementation-plan.md`: stage execution plan, responsible roles, subagent justification, gates, tool readiness, and handoffs.
- `implementation-covenant.md`: shared implementation-role covenant for role boundaries, communication content requirements, handoff packages, status sync, evidence, escalation, and review/update records.
- `role-workspaces.md`: category folder ownership map for each role/subagent category, including shared-folder rules.
- `role-sessions.md`: Codex thread/session map for each role/subagent.
- `role-registry.md`: Loop Manager-maintained active role list with IDs, categories, workspaces, sessions, authority boundaries, readiness, status, and dispatch ownership.
- `goal-dispatch-log.md`: Loop Manager goal intake, role-registry-based routing, task dispatch packets, status-sync cadence, completion-sync requirements, and blocked dispatches.
- `decision-conflict-log.md`: role disagreement records, Loop Manager escalation packets, and user/domain-owner decisions.
- `interaction-evidence-log.md`: project-level record for role-to-role communication, evidence links, artifact references, data sources, online links, evidence gaps, follow-up owners, and status.
- `refinement-standard.md`, `run-log.csv`, `feedback-tags.md`, `weekly-review.md`, `experiment-plan.md`, and `update-log.md`: supporting standards, run records, review notes, and update history.

## Customization Rules

- Customize generated files to the user's actual scenario; do not leave placeholders when context is available.
- Before creating any additional document, check `document-index.md`; reuse, merge, or archive existing documents unless a new document is necessary.
- Keep role additions small and justified by confirmed use cases.
- Record selected, deferred, and excluded candidate roles before implementation.
- Keep the initial active role set small: Loop Manager plus usually 2-3 other active roles. Separate role files/workspaces are fine for selected roles; do not activate specialist roles merely because a candidate role exists.
- Keep implementation claims, test findings, decisions, and handoffs traceable to evidence.
- Treat `implementation-covenant.md` as the shared operating agreement for active implementation roles, not a substitute for individual charters.

## Confirmation Gates

Before execution begins, confirm or explicitly delegate confirmation for:

- Refined demand and concrete use cases.
- Selected implementation role set, deferred candidate roles with split triggers, and excluded-role reasons.
- Stage knowledge base.
- Implementation covenant.
- Tool/skill readiness for every active role.
- Required evidence, status-sync cadence, quality gates, and next handoffs.
- Document budget and index owner for each user/role owner who creates or manages project documents.
- Hard constraint gates, including decision owner, enforcing roles, required evidence, stop condition, and record location. Product/UI/workflow changes by the product manager require user/domain-owner confirmation before downstream implementation, testing acceptance, or release-readiness work proceeds.
- Human participation classification for each gate: aesthetic/product/value/risk/authorization judgment is `human-required`; standardized production with clear requirements, delegated authority, objective checks, and recorded evidence may be `automated-pass`.

Stop at design artifacts when required confirmation is missing.

## Loop Quality Test

A Loop is weak if it cannot answer these questions:

- What exactly improves after each round?
- Who owns the Loop end to end?
- Was Loop Manager created at project start, distinct from project manager/delivery coordination?
- Does Loop Manager have default automatic distillation time nodes from project start?
- Did demand intake refine rough ideas into concrete, measurable use cases?
- Were implementation roles selected from confirmed demand instead of invented by habit?
- Is the initial active role set intentionally small, with Loop Manager plus usually 2-3 other active roles and specialist roles deferred until Loop Manager evidence justifies splitting?
- Are role capability sources tracked on a cadence, including ECC / Everything Claude Code, Claude Code plugins, skills, tools, and trusted references, with candidate-role updates recorded only when responsibilities, skill/tool matches, evidence requirements, or handoffs change?
- Does every active role have a charter, workflow stage, authority boundary, category workspace, handoff rule, Codex session mapping if used, advisor contribution, tool/skill readiness, health/resource status, and role-registry entry?
- Is there an accepted implementation covenant covering boundaries, communication requirements, evidence, handoffs, status sync, and escalation?
- Are hard constraints represented as explicit gates with proposing roles, enforcing roles, decision owners, evidence, stop conditions, and blocked downstream actions?
- Does the Loop put humans at aesthetic, product, value, risk, authorization, or ambiguity points while letting standardized clear production pass through objective evidence?
- Are role-to-role messages and status syncs recorded with sender, receiver, type, summary, evidence, owner, and status?
- Does Loop Manager route goals through `role-registry.md` instead of executing role-specific work?
- Does Loop Manager's fixed-time retrospective review user-role communication efficiency, role-to-role communication efficiency, responsibility fit, and skill/tool gaps?
- Does Loop Manager help each active role gradually distill and optimize its skills, tools, prompts, checklists, references, and role requirements from evidence?
- What signal shows whether the Loop improved?
- Is there a `document-index.md` controlling document count per user/owner, with purpose, owner, status, review date, and merge/archive decisions for every managed document?
- What artifact changes before the next round?
- How will the next similar task reuse the learning?

A Loop is valid when it is repeatable, observable, updatable, transferable, and saved somewhere durable.
