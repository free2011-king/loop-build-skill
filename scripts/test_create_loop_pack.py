#!/usr/bin/env python3
"""Regression tests for create_loop_pack.py."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("create_loop_pack.py")


class CreateLoopPackTests(unittest.TestCase):
    def test_scaffold_contains_role_boundaries_and_readiness(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            out_dir = Path(temp_dir) / "loops"
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "Example Loop",
                    "--out",
                    str(out_dir),
                    "--type",
                    "product",
                    "--slug",
                    "example-loop",
                ],
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            loop_dir = out_dir / "example-loop"
            self.assertTrue(loop_dir.exists())

            demand_workspace = (loop_dir / "roles" / "demand-intake" / "workspace.md").read_text(
                encoding="utf-8"
            )
            loop_manager_workspace = (
                loop_dir / "roles" / "loop-manager" / "workspace.md"
            ).read_text(encoding="utf-8")
            loop_manager = (loop_dir / "loop-manager.md").read_text(encoding="utf-8")
            document_index = (loop_dir / "document-index.md").read_text(encoding="utf-8")
            loop_design = (loop_dir / "loop-design.md").read_text(encoding="utf-8")
            team_formation = (loop_dir / "team-formation.md").read_text(encoding="utf-8")
            candidate_roles = (loop_dir / "candidate-role-library.md").read_text(
                encoding="utf-8"
            )
            decision_conflict_log = (loop_dir / "decision-conflict-log.md").read_text(
                encoding="utf-8"
            )
            interaction_evidence_log = (loop_dir / "interaction-evidence-log.md").read_text(
                encoding="utf-8"
            )
            implementation_covenant = (loop_dir / "implementation-covenant.md").read_text(
                encoding="utf-8"
            )
            goal_dispatch_log = (loop_dir / "goal-dispatch-log.md").read_text(encoding="utf-8")
            implementation_plan = (loop_dir / "implementation-plan.md").read_text(encoding="utf-8")
            role_registry = (loop_dir / "role-registry.md").read_text(encoding="utf-8")
            weekly_review = (loop_dir / "weekly-review.md").read_text(encoding="utf-8")

            self.assertIn("Use `grill-me` before handoff", demand_workspace)
            self.assertNotIn("For demand intake role", loop_manager_workspace)
            self.assertIn("Do not rewrite demand-intake use cases", loop_manager_workspace)
            self.assertIn("Tool And Skill Readiness", loop_manager_workspace)
            self.assertIn("Must not do", loop_manager)
            self.assertTrue((loop_dir / "document-index.md").exists())
            self.assertIn("Document Index", document_index)
            self.assertIn("Document Budget By User / Owner", document_index)
            self.assertIn("Managed Document Index", document_index)
            self.assertIn("New Document Decision Log", document_index)
            self.assertIn("Merge / Archive Queue", document_index)
            self.assertIn("document-index.md", loop_design)
            self.assertIn("Tool and skill readiness", team_formation)
            self.assertIn("Initial Role Split Policy", team_formation)
            self.assertIn("Initial active roles: Loop Manager plus 2-3 other roles", team_formation)
            self.assertIn("Separate files/workspaces are allowed", team_formation)
            self.assertIn("Deferred Candidate Roles", team_formation)
            self.assertIn("Activation / Split Trigger", team_formation)
            self.assertIn("Candidate rows below are not active", team_formation)
            self.assertIn("Existing Role Selection", team_formation)
            self.assertIn("Excluded Candidate Roles", team_formation)
            self.assertIn("User Confirmation Of Role Selection", team_formation)
            self.assertIn("Project-Type Workflow Classification", team_formation)
            self.assertIn("Software development default workflow", team_formation)
            self.assertTrue((loop_dir / "roles" / "demand-intake" / "workspace.md").exists())
            self.assertTrue((loop_dir / "roles" / "loop-manager" / "workspace.md").exists())
            self.assertTrue((loop_dir / "roles" / "super-assistant" / "workspace.md").exists())
            self.assertFalse((loop_dir / "roles" / "product-workflow" / "workspace.md").exists())
            self.assertFalse((loop_dir / "roles" / "project-management" / "workspace.md").exists())
            self.assertFalse((loop_dir / "roles" / "development" / "workspace.md").exists())
            self.assertFalse((loop_dir / "roles" / "testing-evaluation" / "workspace.md").exists())
            self.assertIn("Product manager / workflow designer", candidate_roles)
            self.assertIn("2-3 other active roles", candidate_roles)
            self.assertIn("Staged Role Splitting", candidate_roles)
            self.assertIn("split or activate a specialized role", candidate_roles)
            self.assertIn("Product Manager Capability Pattern", candidate_roles)
            self.assertIn("User Need Completeness Checklist", candidate_roles)
            self.assertIn("Product Manager Handoff Gate", candidate_roles)
            self.assertIn("user evidence", candidate_roles)
            self.assertIn("Developer / implementer", candidate_roles)
            self.assertIn("Tester / evaluator", candidate_roles)
            self.assertIn("Skill / Tool / Knowledge Matching", candidate_roles)
            self.assertIn("| Loop Manager | loop-manager |", candidate_roles)
            self.assertIn("Project manager / delivery coordinator", candidate_roles)
            self.assertIn("role health checks", candidate_roles)
            self.assertIn("Project-Type Workflow Defaults", candidate_roles)
            self.assertIn("non-skippable workflow steps", candidate_roles)
            self.assertIn("Disagreement Resolution", candidate_roles)
            self.assertIn("Selection Workflow", candidate_roles)
            self.assertIn("Non-selected candidate roles", candidate_roles)
            self.assertIn("Claude Code Feature Development Role Patterns", candidate_roles)
            self.assertIn("Role Capability Source Tracking", candidate_roles)
            self.assertIn("ECC / Everything Claude Code", candidate_roles)
            self.assertIn("Proposed Requirement Change", candidate_roles)
            self.assertIn("Codebase explorer / implementation researcher", candidate_roles)
            self.assertIn("Software architect / technical designer", candidate_roles)
            self.assertIn("Security reviewer", candidate_roles)
            self.assertIn("Error-handling / reliability auditor", candidate_roles)
            self.assertIn("Dependency updater / migration helper", candidate_roles)
            self.assertIn("Extended Software Handoffs", candidate_roles)
            self.assertIn("Major or unresolved disagreements", decision_conflict_log)
            self.assertIn("Document / Material / Online Link", decision_conflict_log)
            self.assertIn("Decision Packet Template", decision_conflict_log)
            self.assertIn("Disagreement Handling", loop_manager_workspace)
            self.assertIn("Disagreement Escalation", loop_manager)
            self.assertIn("Interaction Message And Evidence", loop_manager_workspace)
            self.assertIn("Interaction Message Review", loop_manager)
            self.assertIn("Role health cadence", loop_manager)
            self.assertIn("Candidate role capability source tracking", loop_manager)
            self.assertIn("Resource Status", loop_manager)
            self.assertIn("Experience distillation check", loop_manager)
            self.assertIn("Role Change Broadcast", loop_manager)
            self.assertIn("notify every other active role", loop_manager)
            self.assertIn("Project-Type Workflow Rule", loop_manager)
            self.assertIn("Project Owner Status Sync", loop_manager)
            self.assertIn("Project-type workflow completeness", loop_manager)
            self.assertIn("fixed-time retrospectives", loop_manager)
            self.assertIn("Communication Efficiency And Role Optimization Review", loop_manager)
            self.assertIn("User-To-Role Communication Friction", loop_manager)
            self.assertIn("role responsibility/skill optimization", candidate_roles)
            self.assertIn("Loop Manager Fixed-Time Retrospective Pattern", candidate_roles)
            self.assertIn("communication-efficiency report", candidate_roles)
            self.assertIn("Communication Efficiency Review", weekly_review)
            self.assertIn("Role Responsibility And Skill Optimization", weekly_review)
            self.assertTrue((loop_dir / "implementation-covenant.md").exists())
            self.assertIn("Implementation Covenant", implementation_covenant)
            self.assertIn("Role Boundary Matrix", implementation_covenant)
            self.assertIn("Communication Content Requirements", implementation_covenant)
            self.assertIn("Message Type Rules", implementation_covenant)
            self.assertIn("Handoff Package Standard", implementation_covenant)
            self.assertIn("Boundary Violation Handling", implementation_covenant)
            self.assertIn("Covenant Review And Updates", implementation_covenant)
            self.assertIn("implementation-covenant.md", team_formation)
            self.assertIn("Implementation covenant rule", implementation_plan)
            self.assertIn("Implementation covenant exists before execution", candidate_roles)
            self.assertIn("Interaction Message And Evidence Log", interaction_evidence_log)
            self.assertIn("Message And Interaction Log", interaction_evidence_log)
            self.assertIn("Requested Action / Decision / Next Step", interaction_evidence_log)
            self.assertIn("unrecorded role messages", interaction_evidence_log)
            self.assertIn("role-change-broadcast", interaction_evidence_log)
            self.assertIn("role-status-sync", interaction_evidence_log)
            self.assertIn("Document / Material / Online Link", interaction_evidence_log)
            self.assertIn("Evidence Gap Queue", interaction_evidence_log)
            self.assertIn("document-index.md", loop_manager_workspace)
            self.assertIn("Goal Setting Dispatch Rule", loop_manager)
            self.assertIn("role-registry.md", loop_manager)
            self.assertIn("Registry Role ID", loop_manager)
            self.assertIn("Goal Contract", goal_dispatch_log)
            self.assertIn("Registry Role ID", goal_dispatch_log)
            self.assertIn("role-registry.md", goal_dispatch_log)
            self.assertIn("Dispatch Packet", goal_dispatch_log)
            self.assertIn("Project Type", goal_dispatch_log)
            self.assertIn("Workflow Stage", goal_dispatch_log)
            self.assertIn("Status Sync Cadence", goal_dispatch_log)
            self.assertIn("Completion Sync Required", goal_dispatch_log)
            self.assertIn("Blocked Dispatches", goal_dispatch_log)
            self.assertIn("Assigned Dispatch Packets", loop_manager_workspace)
            self.assertIn("Project-Type Workflow Requirement", loop_manager_workspace)
            self.assertIn("Project Owner Status Sync", loop_manager_workspace)
            self.assertTrue((loop_dir / "role-registry.md").exists())
            self.assertIn("Active Role Registry", role_registry)
            self.assertIn("Role Change Log", role_registry)
            self.assertIn("Health / Resource Status", role_registry)
            self.assertIn("Experience Distilled?", role_registry)
            self.assertIn("Notified Roles", role_registry)
            self.assertIn("Notification Record", role_registry)
            self.assertIn("personnel-session-change", role_registry)
            self.assertIn("Dispatch Ownership View", role_registry)
            self.assertIn("LM-001", role_registry)
            self.assertIn("DI-001", role_registry)


if __name__ == "__main__":
    unittest.main()
