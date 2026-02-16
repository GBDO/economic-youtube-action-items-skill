import json
import unittest
from pathlib import Path


class ContractTest(unittest.TestCase):
    def test_contract_examples_validate(self) -> None:
        root = Path(__file__).resolve().parents[1]
        schema = json.loads((root / "contracts/v1/action_items.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(schema["title"], "Economic YouTube Action Items Result v1")

        examples = [
            root / "contracts/v1/examples/valid.complete.json",
            root / "contracts/v1/examples/valid.partial.json",
            root / "contracts/v1/examples/valid.ended_live.json",
        ]
        for example_path in examples:
            instance = json.loads(example_path.read_text(encoding="utf-8"))
            self.assertIn("run_id", instance)
            self.assertEqual(instance["repo"], "economic-youtube-action-items-skill")
            self.assertIsInstance(instance["results"], list)
            self.assertTrue(instance["results"])
            first = instance["results"][0]
            self.assertIn(first["status"], {"complete", "partial", "ended_live", "unavailable", "error"})
            self.assertIn("action_items", first)


if __name__ == "__main__":
    unittest.main()
