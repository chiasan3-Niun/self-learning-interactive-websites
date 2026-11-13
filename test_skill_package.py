import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
SCRIPTS = ROOT / "scripts"


class SkillPackageTests(unittest.TestCase):
    def test_required_files_and_case_study_are_present(self):
        self.assertTrue((ROOT / "SKILL.md").is_file())
        self.assertTrue((ROOT / "README.md").is_file())
        self.assertIn("luanqun-bunun-animal-flashcards.netlify.app", (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertNotIn("snail-bunun-picturebooks.vercel.app", (ROOT / "README.md").read_text(encoding="utf-8"))

    def test_scan_and_manifest_scripts(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source"
            source.mkdir()
            (source / "教材.txt").write_text("asu", encoding="utf-8")
            (source / "ignore.exe").write_bytes(b"x")
            inventory = Path(temp) / "inventory.json"
            subprocess.run([sys.executable, str(SCRIPTS / "scan_assets.py"), str(source), "--output", str(inventory)], check=True)
            data = json.loads(inventory.read_text(encoding="utf-8"))
            self.assertEqual(data["files"][0]["path"], "教材.txt")
            self.assertTrue(data["warnings"])

    def test_site_checks_detect_missing_local_reference(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "index.html").write_text('<img src="missing.png">', encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPTS / "run_site_checks.py"), str(root)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing reference", result.stdout)


if __name__ == "__main__":
    unittest.main()
