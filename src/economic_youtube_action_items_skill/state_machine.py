from economic_youtube_action_items_skill.models import PartialInfo, ProcessingStatus


def classify_transcript_state(
    *,
    was_live: bool,
    transcript_text: str | None,
    min_transcript_chars: int,
    allow_partial: bool,
) -> tuple[ProcessingStatus, PartialInfo, list[str]]:
    warnings: list[str] = []
    transcript = (transcript_text or "").strip()

    if not transcript:
        if was_live:
            warnings.append("Ended live video detected but transcript is unavailable.")
            return (
                ProcessingStatus.ENDED_LIVE,
                PartialInfo(is_partial=True, reason="live_ended_transcript_pending"),
                warnings,
            )
        warnings.append("Transcript is unavailable.")
        return ProcessingStatus.UNAVAILABLE, PartialInfo(is_partial=False), warnings

    length = len(transcript)
    if length < min_transcript_chars:
        ratio = round(length / float(min_transcript_chars), 3)
        warnings.append(
            "Partial transcript detected."
            if allow_partial
            else "Partial transcript detected but partial mode is disabled."
        )
        return (
            ProcessingStatus.PARTIAL,
            PartialInfo(is_partial=True, coverage_ratio=ratio, reason="below_min_chars"),
            warnings,
        )

    return ProcessingStatus.COMPLETE, PartialInfo(is_partial=False), warnings
