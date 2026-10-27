from pathlib import Path
import tempfile
import unittest

from scripts.validate_skills import privacy_issues, validate_skill


class ValidationTests(unittest.TestCase):
    def test_private_values_report_locations_without_values(self):
        secret = "ghp_" + "x" * 36
        email = "person@" + "private-company.test"
        result = privacy_issues(secret + "\n" + email)
        self.assertEqual(len(result), 2)
        self.assertNotIn(secret, "\n".join(result))
        self.assertNotIn(email, "\n".join(result))

    def test_synthetic_examples_are_allowed(self):
        self.assertEqual(privacy_issues("persona@example.com https://example.com"), [])

    def test_local_paths_are_flagged(self):
        self.assertTrue(privacy_issues("/" + "Users/" + "example/doc.txt"))

    def test_skill_structure_and_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample-skill"
            path.mkdir()
            entry = path / "SKILL.md"
            entry.write_text("---\nname: sample-skill\ndescription: Review a sample.\n---\nDo the task.\n")
            self.assertEqual(validate_skill(path), [])
            entry.write_text("---\nname: different-name\ndescription: ''\n---\nDo the task.\n")
            issues = validate_skill(path)
            self.assertEqual(len(issues), 2)
            entry.write_text("---\nname: [\n---\n")
            self.assertIn("invalid YAML frontmatter", validate_skill(path))


if __name__ == "__main__":
    unittest.main()
