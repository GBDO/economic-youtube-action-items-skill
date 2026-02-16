import json

from economic_youtube_action_items_skill.models import BatchResult


def render_markdown(batch: BatchResult) -> str:
    lines: list[str] = [f"# Economic YouTube Action Items ({batch.run_id})"]
    for idx, result in enumerate(batch.results, start=1):
        lines.extend(
            [
                "",
                f"## {idx}. {result.video.channel_name}",
                f"### {result.video.title}",
                f"- 링크: {result.video.url}",
                f"- 상태: {result.status.value}",
                "#### 액션 아이템",
            ]
        )
        if result.action_items:
            for item in result.action_items:
                condition = f" (조건: {item.condition})" if item.condition else ""
                lines.append(f"- [{item.priority}] {item.action}{condition}")
        else:
            lines.append("- (추출된 액션 아이템 없음)")

    return "\n".join(lines).strip() + "\n"


def render_json(batch: BatchResult) -> str:
    return json.dumps(batch.to_dict(), ensure_ascii=False, indent=2)
