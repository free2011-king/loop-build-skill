# Candidate Role Library

Read this reference when building software, product, Agent, workflow, digital-employee, or engineering Loops that need reusable role presets instead of initializing every role from scratch.

## Contents

- [Selection Workflow](#selection-workflow)
- [Activation Rule](#activation-rule)
- [Core Software/Product Candidates](#core-softwareproduct-candidates)
- [Claude Code Feature Development Role Patterns](#claude-code-feature-development-role-patterns)
- [Role Capability Source Tracking](#role-capability-source-tracking)
- [Extended Software Development Candidates](#extended-software-development-candidates)
- [Skill / Tool / Knowledge Match](#skill--tool--knowledge-match)
- [Product Manager Capability Pattern](#product-manager-capability-pattern)
- [Loop Manager Fixed-Time Retrospective Pattern](#loop-manager-fixed-time-retrospective-pattern)
- [Extended Software Skill / Tool / Knowledge Match](#extended-software-skill--tool--knowledge-match)
- [Project-Type Workflow Defaults](#project-type-workflow-defaults)
- [Default Handoffs](#default-handoffs)
- [Extended Software Handoffs](#extended-software-handoffs)
- [Interaction Documentation And Evidence](#interaction-documentation-and-evidence)
- [Disagreement Resolution](#disagreement-resolution)
- [Reuse Checklist](#reuse-checklist)

Use these roles as an existing reusable role pool, not mandatory entities. Select roles according to the project's confirmed needs and use cases, then ask the user or domain owner to confirm the selected implementation role set before execution. Activate only the roles needed by confirmed use cases and the implementation plan. Loop Manager and project manager are different roles: Loop Manager is mandatory for concrete Loop projects and governs the whole Loop; project manager/delivery coordinator is optional and only selected when delivery coordination needs a separate owner.

## Selection Workflow

1. Start from confirmed project needs and use cases.
2. Match each need to an existing candidate role and role category.
3. Select the smallest role set that can cover the work without unclear authority, evidence, record, or confidentiality boundaries.
4. List candidate roles that are not selected and explain why they are unnecessary for this Loop round.
5. Prepare a confirmation packet with selected roles, excluded candidates, category workspaces, authority boundaries, handoff paths, required tools/skills, readiness status, and blockers.
6. Ask the user or domain owner to confirm the selected role set before implementation.
7. Create a new role only when no existing role can responsibly cover the confirmed need.

## Activation Rule

Apply `如无必要，勿增实体`: a candidate role becomes active only when it has a concrete goal, implementation standard, authority boundary, role category, category workspace, Codex session mapping, tool/skill readiness, knowledge base, records, gate, and handoff rule.

## Core Software/Product Candidates

| Candidate Role | Default Position | Activate When | Must Not Do |
| --- | --- | --- | --- |
| Product manager / workflow designer | Understand complete user needs and convert confirmed use cases into product scope, workflow, acceptance standards, non-goals, risks, outcome metrics, and release slices | User value, target users, workflow, scope, priority, acceptance criteria, or success metrics are unclear | Implement code, declare tests passed, approve business acceptance, ignore user evidence, or silently expand scope |
| Developer / implementer | Build the confirmed technical slice and provide implementation evidence | Confirmed scope needs code, configuration, integration, automation, data, or platform changes | Redefine scope, declare QA passed, approve release, or bypass governance |
| Tester / evaluator | Verify behavior against use cases, acceptance standards, regressions, and quality gates | Runnable artifact, implementation diff, or reviewable output exists | Implement fixes silently, approve business acceptance, or rewrite product scope |
| Loop Manager | Govern the whole Loop: role registry, cadence, fixed-time retrospectives, blockers, handoffs, role health checks, resource status, experience distillation, role self-review, role advice, communication-efficiency review, role responsibility/skill optimization, project reflection, and feedback to Super Assistant | Always for every concrete Loop project; created at project start before demand intake and implementation roles | Do development, testing conclusions, business acceptance, governance decisions, production release, project-manager delivery execution, or role-specific execution |
| Project manager / delivery coordinator | Classify each new question/request by project nature and coordinate the complete workflow for that project type, including milestones, timeline, cross-team dependencies, stakeholder status, and delivery rituals | Delivery scheduling, external dependencies, stakeholder reporting, multi-team coordination, or project-type workflow completeness needs a dedicated owner | Govern Loop learning, maintain role health, replace Loop Manager, decide product scope, do implementation, declare QA pass, approve release, own experience distillation, or skip required project-type workflow stages |


## Claude Code Feature Development Role Patterns

These software-development role candidates are derived from the locally available Claude Code official `feature-dev`, `code-review`, `pr-review-toolkit`, `claude-code-setup`, `frontend-design`, and `security-guidance` plugins. Treat them as reusable role options, not mandatory roles. Activate them only when the confirmed use case needs their responsibility boundary.

The core development pattern learned from Claude Code is:

```text
discover requirements -> explore codebase -> clarify gaps -> design architecture -> implement -> review quality -> summarize decisions and next steps
```

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

## Skill / Tool / Knowledge Match

| Candidate Role | Best-Practice Skill Match | Tool Match | Knowledge Base To Prepare | Core Records |
| --- | --- | --- | --- | --- |
| Product manager / workflow designer | `loop-builder`; `grill-me` when scope is rough; product discovery, user research, prioritization, roadmap/PRD, and product analytics skills when available | User/domain interviews, support/sales feedback, analytics or process evidence, competitor/domain references, diagram/spec/roadmap tools, docs | User segments, jobs/pains/gains, scenarios, user-need statements, goals/non-goals, assumptions, constraints, use cases, workflow, acceptance standards, outcome metrics, priority model, release slicing principles | User evidence, product decisions, assumptions, tradeoffs, priority rationale, scope changes, open questions, confirmation evidence |
| Developer / implementer | Framework/language/repo skills; code review and security skills when relevant | Repository, package manager, dev server, test runner, logs, debugger, CI output | Architecture, coding standards, repo conventions, integration contracts, environment setup, error handling, rollback notes | Changed files, commands run, test output, implementation notes, blockers |
| Tester / evaluator | Testing/evaluation skills; browser/API/performance/security tools when relevant | Test runner, browser automation, API client, fixtures/test data, logs, acceptance checklist | Test strategy, acceptance criteria, regression areas, data setup, quality gates, known risks | Test plan, pass/fail results, defect reports, evidence, regression notes |
| Loop Manager | `loop-builder`; Loop governance, fixed-time retrospective, communication-efficiency analysis, role-design, and skill-improvement practices | Role registry, health check tracker, communication-efficiency tracker, responsibility/skill improvement backlog, resource log, handoff tracker, decision log, risk log, review cadence | Loop object, role map, handoff rules, communication signals, health signals, resource thresholds, self-review prompts, experience distillation standards, role optimization principles, improvement principles | Status, blockers, decisions, risk log, handoff log, communication-efficiency report, role responsibility optimization proposals, skill/tool improvement proposals, role health report, resource report, role advice summary, reflection updates |
| Project manager / delivery coordinator | project management and delivery coordination practices; software delivery workflow when project type is software | Status board, milestone plan, dependency tracker, stakeholder update log, workflow checklist | Project type, required lifecycle stages, milestones, timeline, dependencies, delivery rituals, stakeholder communication needs | Delivery status, workflow stage map, milestone risks, dependency updates, stakeholder summaries |

## Product Manager Capability Pattern

Use this baseline whenever the Product manager / workflow designer role is created. It is adapted from established product discovery, user-need, and agile product-owner practices: discover the problem before committing to a solution, describe user needs in observable terms, maintain outcome-oriented scope, and prepare evidence-backed handoffs.

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

### Product Manager Source Tracking

When online or external product-management references shape the role requirements, record the source link, source type, adopted capability, and date in the role workspace or product spec. Useful source families include product discovery, user-need statements, agile product-owner accountability, PRD/spec templates, prioritization frameworks, and product analytics guidance.


### Product Manager Reference Sources To Track

| Source | Adopted Capability | Usage In Role Skill |
| --- | --- | --- |
| [Nielsen Norman Group: Discovery Phase](https://www.nngroup.com/articles/discovery-phase/) | Discover the problem space before committing to design or build decisions | Require discovery, evidence, problem framing, and assumptions before scope handoff |
| [Nielsen Norman Group: User Need Statements](https://www.nngroup.com/articles/user-need-statements/) | Express needs as user, need, goal, and outcome rather than feature requests | Require user-need statements and user context in product packages |
| [GOV.UK Service Manual: Start By Learning User Needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) | Start service/product work by learning real user needs and context | Require user/domain evidence, target users, scenarios, constraints, and evidence gaps |
| [Scrum Guide: Product Owner](https://scrumguides.org/scrum-guide.html#product-owner) | Maintain product value, product goal, backlog clarity, ordering, and transparency | Require priority logic, release slicing, outcome metrics, and transparent decisions |


## Loop Manager Fixed-Time Retrospective Pattern

Every concrete project must have a Loop Manager and a fixed-time retrospective cadence. Use weekly as the default cadence unless the project defines a shorter cycle, milestone-based cadence, or incident-triggered review.

The Loop Manager retrospective must treat the following as core distillation and adjustment targets:

- User-to-role communication efficiency: repeated clarification loops, slow answers, missing evidence, unclear decisions, mismatched expectations, and better question/confirmation formats.
- Role-to-role communication efficiency: handoff delay, incomplete handoff packages, stale status syncs, repeated rework, missing interaction records, and clearer message/document templates.
- Role responsibility optimization: overlapping authority, responsibility gaps, unclear gates, wrong handoff targets, roles doing out-of-boundary work, and role charter updates.
- Role skill/tool optimization: missing skills, underused skills, unavailable tools, weak checklists, insufficient references, required training, activation/install actions, and fallback quality.
- Project resource fit: people, agent/session availability, time budget, data/material access, external dependencies, and overloaded roles.
- Reusable learning: rules, templates, prompts, checklists, role definitions, skill updates, and project principles that should change before the next cycle.

The output must be recorded as concrete updates, not only observations: communication-rule updates, handoff-template updates, role-registry updates, role-charter changes, skill/tool readiness actions, training/checklist updates, and feedback to the Super Assistant.

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

## Project-Type Workflow Defaults

When project manager / delivery coordinator is selected, each new project question, request, issue, or work item must be classified by project nature and routed through the complete workflow for that type.

For software development, use this default lifecycle unless the user confirms a narrower lifecycle:

```text
demand clarification -> product/workflow scope -> codebase exploration when needed -> architecture/design -> implementation -> testing/evaluation -> code review and specialized reviews as needed -> release/operation readiness -> review/update
```

Every selected role's charter must state its workflow stage, required prior inputs, required outputs/evidence, status-sync duty to the project owner, quality gate, next handoff, and non-skippable workflow steps.

## Default Handoffs

| From | To | Trigger | Handoff Package |
| --- | --- | --- | --- |
| Demand intake | Product manager / workflow designer | Use cases are confirmed but scope/workflow/acceptance needs design | Confirmed use cases, user/domain evidence, constraints, open decisions, acceptance draft, evidence gaps |
| Product manager / workflow designer | Developer / implementer | Scope, acceptance standards, and user/domain-owner confirmation are complete | Product problem statement, target users, confirmed use cases/user stories, workflow, release slice, outcome metric, non-goals, constraints, assumptions, risks, evidence links/gaps |
| Developer / implementer | Tester / evaluator | Implementation is ready for verification | Changed files, run commands, build notes, known risks, test suggestions |
| Tester / evaluator | Developer / implementer | Defect or regression is found | Repro steps, expected versus actual result, evidence, severity, affected use case |
| Tester / evaluator | Domain owner | Acceptance evidence is ready | Test results, unresolved risks, release recommendation |
| Any role | Loop Manager | Blocker, decision, boundary issue, or recurring feedback appears | Status, owner, evidence, decision needed, deadline |


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

Every role-to-role message must be recorded in `interaction-evidence-log.md` or another named project document. Every handoff package must also include the detailed material needed by the receiver: local document/material path, online document link, artifact reference, data source, log, test output, screenshot, ticket, pull request, or decision record.

If a role only has a summary, it must either attach/source the supporting material, create the smallest useful document, or mark the handoff as an evidence gap. Do not use chat-only or unrecorded role messages as implementation-ready state.

## Disagreement Resolution

Roles should communicate directly first when they disagree about assigned work, evidence, standards, implementation approach, test interpretation, or handoff content.

Escalate to the Loop Manager when the disagreement changes scope, acceptance criteria, risk boundary, schedule, resource allocation, role authority, release readiness, or cannot be resolved quickly. The Loop Manager records the competing options and impact, then asks the user or domain owner to decide.

## Reuse Checklist

- [ ] Candidate roles were selected from confirmed use cases and project needs, not assumed as mandatory.
- [ ] Non-selected candidate roles have an explicit exclusion reason.
- [ ] The user or domain owner confirmed the selected implementation role set before execution.
- [ ] Loop Manager and project manager/delivery coordinator are separate roles; Loop Manager is mandatory, project manager is optional and justified only when delivery coordination needs a separate owner.
- [ ] Each active role has a completed Loop charter, project-type workflow requirement, role category, category workspace, Codex session mapping, and handoff rule.
- [ ] Implementation covenant exists before execution, with role boundaries, communication content requirements, evidence requirements, handoff packages, status-sync rules, and escalation paths accepted.
- [ ] Each active role has skills, tools, references, data access, and permissions checked.
- [ ] Product, project management, development, testing, and Loop Manager boundaries do not overlap.
- [ ] All role-to-role messages and interactions are recorded in project documents, and handoffs include document/material paths, online links, artifact references, or explicit evidence gaps.
- [ ] Disagreement handling is clear: role-to-role communication first, Loop Manager escalation for major issues, user/domain-owner decision for unresolved or high-impact conflicts.
- [ ] Each role has a prepared knowledge base: goals, standards, constraints, workflow, principles, records, feedback, and update responsibility.
