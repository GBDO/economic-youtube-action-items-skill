import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from economic_youtube_action_items_skill.models import (
    ActionItem,
    ActionItemsResult,
    BatchResult,
    PartialInfo,
    ProcessingStatus,
    VideoDescriptor,
)
from economic_youtube_action_items_skill.render import render_markdown


class RenderTest(unittest.TestCase):
    def test_render_markdown_contains_action_items(self) -> None:
        batch = BatchResult(
            run_id="abc",
            generated_at="2026-02-16T00:00:00+00:00",
            results=[
                ActionItemsResult(
                    status=ProcessingStatus.COMPLETE,
                    video=VideoDescriptor(
                        video_id="dQw4w9WgXcQ",
                        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                        channel_name="Sample Channel",
                        title="Sample Title",
                        was_live=False,
                    ),
                    transcript_chars=1000,
                    partial=PartialInfo(is_partial=False),
                    action_items=[ActionItem(action="비중을 점검해야 한다", priority="MEDIUM")],
                    warnings=[],
                    error=None,
                )
            ],
        )
        markdown = render_markdown(batch)
        self.assertIn("Sample Channel", markdown)
        self.assertIn("[MEDIUM] 비중을 점검해야 한다", markdown)


if __name__ == "__main__":
    unittest.main()
