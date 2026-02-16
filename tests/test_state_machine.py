import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from economic_youtube_action_items_skill.state_machine import classify_transcript_state


class StateMachineTest(unittest.TestCase):
    def test_ended_live_when_live_and_no_transcript(self) -> None:
        status, partial, warnings = classify_transcript_state(
            was_live=True,
            transcript_text="",
            min_transcript_chars=700,
            allow_partial=True,
        )
        self.assertEqual(status.value, "ended_live")
        self.assertTrue(partial.is_partial)
        self.assertTrue(warnings)

    def test_partial_for_short_transcript(self) -> None:
        status, partial, _warnings = classify_transcript_state(
            was_live=False,
            transcript_text="short text",
            min_transcript_chars=700,
            allow_partial=True,
        )
        self.assertEqual(status.value, "partial")
        self.assertIsNotNone(partial.coverage_ratio)


if __name__ == "__main__":
    unittest.main()
