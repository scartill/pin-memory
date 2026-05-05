import unittest
from pathlib import Path
import shutil
import tempfile
from pin_memory.server import MemoryManager


class TestMemoryManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        self.manager = MemoryManager()
        # Override directories to use our temp dir
        self.manager.global_dir = self.test_dir / "global"
        self.manager.workspaces_root = self.test_dir / "workspaces"
        self.manager.project_dir = self.test_dir / "project"

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_read_factoids_behavior(self):
        """Verify _read_factoids returns stripped content via _get_factoids."""
        target = self.test_dir / "test_read"
        target.mkdir()

        f1 = target / "fact1.md"
        f1.write_text("  content with spaces  ", encoding="utf-8")

        f2 = target / "fact2.md"
        f2.write_text("content2\n", encoding="utf-8")

        # _read_factoids should return list of stripped contents
        factoids = self.manager._read_factoids(target)
        self.assertEqual(factoids, ["content with spaces", "content2"])

    def test_get_factoids_behavior(self):
        """Verify _get_factoids strips content and handles names."""
        target = self.test_dir / "test_get"
        target.mkdir()

        f1 = target / "fact1.md"
        f1.write_text("  content with spaces  ", encoding="utf-8")

        # _get_factoids should return list of dicts with stripped content
        results = self.manager._get_factoids(target)
        self.assertEqual(results, [{"name": "fact1", "content": "content with spaces"}])

    def test_recall_uses_read_factoids(self):
        """Verify recall includes all factoids from global and project."""
        self.manager.global_dir.mkdir(parents=True)
        self.manager.project_dir.mkdir(parents=True)

        (self.manager.global_dir / "g1.md").write_text("global fact", encoding="utf-8")
        (self.manager.project_dir / "p1.md").write_text(
            "project fact", encoding="utf-8"
        )

        output = self.manager.recall()
        self.assertIn("global fact", output)
        self.assertIn("project fact", output)
        self.assertEqual(output, "global fact\n\nproject fact")


if __name__ == "__main__":
    unittest.main()
