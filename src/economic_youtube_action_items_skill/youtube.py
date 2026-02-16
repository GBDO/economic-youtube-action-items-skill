import re
from urllib.parse import parse_qs, urlparse


_YOUTUBE_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


def parse_video_id(url: str) -> str:
    parsed = urlparse(url)
    if parsed.hostname == "youtu.be":
        candidate = parsed.path.lstrip("/")
        if _YOUTUBE_ID_RE.match(candidate):
            return candidate

    query_id = parse_qs(parsed.query).get("v", [None])[0]
    if query_id and _YOUTUBE_ID_RE.match(query_id):
        return query_id

    for part in [p for p in parsed.path.split("/") if p]:
        if _YOUTUBE_ID_RE.match(part):
            return part

    raise ValueError(f"Unable to parse YouTube video id from URL: {url}")


def infer_was_live(url: str) -> bool:
    lowered = url.lower()
    return "/live/" in lowered or "live_stream" in lowered


def fetch_transcript(video_id: str, languages: list[str]) -> str | None:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi

        segments = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        text = " ".join(seg.get("text", "").strip() for seg in segments if seg.get("text"))
        return text.strip() or None
    except Exception:
        return None
