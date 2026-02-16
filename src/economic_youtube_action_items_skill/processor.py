import re

from economic_youtube_action_items_skill.models import ActionItem


ACTION_KEYWORDS = [
    "해야",
    "확인",
    "체크",
    "매수",
    "매도",
    "비중",
    "watch",
    "check",
    "buy",
    "sell",
    "monitor",
    "rebalance",
]

HIGH_PRIORITY_MARKERS = ["즉시", "오늘", "바로", "immediately", "must", "urgent"]


def _priority_for(sentence: str) -> str:
    lowered = sentence.lower()
    if any(marker in lowered for marker in HIGH_PRIORITY_MARKERS):
        return "HIGH"
    if "if " in lowered or "면" in sentence:
        return "MEDIUM"
    return "LOW"


def _condition_for(sentence: str) -> str | None:
    lowered = sentence.lower()
    if "if " in lowered:
        return sentence[sentence.lower().index("if ") :].strip()
    if "면" in sentence:
        idx = sentence.index("면")
        return sentence[max(0, idx - 20) : idx + 1].strip()
    return None


def extract_action_items(transcript_text: str, max_items: int) -> list[ActionItem]:
    fragments = [frag.strip() for frag in re.split(r"[.!?\n]+", transcript_text) if frag.strip()]
    collected: list[ActionItem] = []
    seen: set[str] = set()

    for sentence in fragments:
        lowered = sentence.lower()
        if not any(keyword in lowered for keyword in ACTION_KEYWORDS):
            continue
        normalized = re.sub(r"\s+", " ", sentence).strip(" -•")
        if len(normalized) < 8 or normalized in seen:
            continue
        seen.add(normalized)
        collected.append(
            ActionItem(
                action=normalized,
                priority=_priority_for(normalized),
                condition=_condition_for(normalized),
            )
        )
        if len(collected) >= max_items:
            break

    return collected
