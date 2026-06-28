# Loop Build Skill

Loop Build Skill helps Codex design and scaffold reusable Loop systems: role governance, demand intake, implementation roles, evidence records, feedback cycles, retrospectives, and reusable learning artifacts.

This repository is the git-managed source for the `loop-builder` Codex skill.

## What It Does

- Turns ambiguous work into a closed Loop: `goal -> input -> action -> observation -> update -> reuse`.
- Creates Loop governance first, with a mandatory Loop Manager.
- Gives Loop Manager default automatic distillation time nodes from project start.
- Separates Loop Manager from project manager / delivery coordinator.
- Requires the project owner function to translate user demand into verifiable acceptance standards and get confirmation before dispatch or execution.
- Lets role skills, prompts, tools, checklists, and role requirements improve gradually with Loop Manager support.
- Turns hard constraints into explicit gates with decision owners, enforcing roles, evidence, stop conditions, and blocked downstream actions.
- Classifies human participation so aesthetic/product/value/risk judgment gets human input, while clear standardized production can proceed through objective evidence.
- Selects implementation roles from an existing candidate role library, while keeping the initial active role set small.
- Requires product manager / workflow designer to keep clarifying user needs until they are clear, bounded, testable, and ready for handoff.
- Requires role-to-role messages, handoffs, blockers, advice, status syncs, test findings, and acceptance feedback to be recorded.
- Creates category-based role workspaces so roles of the same category share one project folder.
- Initializes `project-metadata.md` for role information, division of work, thread/session basics, and metadata changes.
- Controls document growth with `document-index.md`, document budgets, review dates, and merge/archive decisions.
- Tracks reusable role capability sources such as ECC / Everything Claude Code, Claude Code plugins, local plugin/tool metadata, and external role references.

## Repository Structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── artifact-pack.md
│   ├── candidate-role-library.md
│   ├── enterprise-digital-employee-loop.md
│   └── role-system.md
└── scripts/
    ├── create_loop_pack.py
    └── test_create_loop_pack.py
```

## Install Locally

Copy or clone this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/free2011-king/loop-build-skill.git ~/.codex/skills/loop-builder
```

If `~/.codex/skills/loop-builder` already exists, update it from this repository or copy the files over carefully.

## Use The Skill

Ask Codex to build or improve a Loop. Example prompts:

```text
Use loop-builder to create a software development Loop for this project.
```

```text
Update the Loop roles for this project and make sure the Loop Manager owns role health, retrospectives, and communication efficiency.
```

```text
Scaffold a Loop pack for a product discovery and delivery process.
```

## Generate A Loop Pack

```bash
python3 scripts/create_loop_pack.py "Example Loop" --out /tmp/example-loop --type software
```

Useful options:

- `--type software`: use software development lifecycle defaults.
- `--slug example-loop`: set the output folder name.
- `--force`: overwrite an existing generated folder.

The generated pack includes governance files such as `loop-design.md`, `document-index.md`, `project-metadata.md`, `loop-manager.md`, `role-registry.md`, `team-formation.md`, `implementation-covenant.md`, and role workspaces.

## Validate

Run the generator test:

```bash
python3 scripts/test_create_loop_pack.py
```

Run syntax checks:

```bash
PYTHONPYCACHEPREFIX=/tmp/loop-builder-pycache python3 -m py_compile scripts/create_loop_pack.py scripts/test_create_loop_pack.py
```

If you have the Codex skill validation utilities available, also run:

```bash
python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" .
```

## Maintenance Rules

- Keep `SKILL.md` concise and route detailed instructions through `references/`.
- Add new reference files only when progressive disclosure improves clarity or reduces runtime context.
- Before adding new generated documents, update `references/artifact-pack.md`, `scripts/create_loop_pack.py`, and `scripts/test_create_loop_pack.py` together.
- Preserve `如无必要，勿增实体`: do not add roles, documents, stages, gates, or abstractions unless they close the Loop, reduce real risk, preserve reusable learning, or satisfy a confirmed constraint.
- Keep early projects lightly staffed: Loop Manager is mandatory, other active roles usually start at 2-3, and specialist roles stay deferred until Loop Manager evidence justifies splitting, activating, merging, pausing, or closing roles.
- Keep `document-index.md` as the single generated document-control index for concrete Loop projects.
- Revisit candidate role requirements on the cadence defined in the skill, monthly by default when no cadence is set.
