import os
from dataclasses import dataclass


def _bool_from_env(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


@dataclass(slots=True)
class Settings:
    min_transcript_chars: int = 700
    allow_partial: bool = True
    max_items: int = 7
    transcript_languages: str = "ko,en"
    mock_transcript_text: str | None = None

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            min_transcript_chars=max(100, int(os.getenv("EYT_ACTION_MIN_TRANSCRIPT_CHARS", "700"))),
            allow_partial=_bool_from_env(os.getenv("EYT_ACTION_ALLOW_PARTIAL"), True),
            max_items=min(20, max(1, int(os.getenv("EYT_ACTION_MAX_ITEMS", "7")))),
            transcript_languages=os.getenv("EYT_ACTION_TRANSCRIPT_LANGUAGES", "ko,en"),
            mock_transcript_text=os.getenv("EYT_ACTION_MOCK_TRANSCRIPT_TEXT") or None,
        )

    def languages(self) -> list[str]:
        return [item.strip() for item in self.transcript_languages.split(",") if item.strip()]
