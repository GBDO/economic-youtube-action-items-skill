---
name: economic-youtube-action-items-skill
description: Extract action items from economic YouTube videos (including ended live videos). Use when the user wants per-video actionable checklists with channel/title/link context and environment-variable based configuration.
---

# Economic YouTube Action Items Skill

## Workflow

1. Read one or more YouTube URLs.
2. Build transcript text or classify ended-live/unavailable.
3. Extract normalized action items with priority labels.
4. Render checklist output by channel, title, and link.

## CLI

```bash
eyt-action-items generate \
  --video-url "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

## Environment Variables

- `EYT_ACTION_MIN_TRANSCRIPT_CHARS`
- `EYT_ACTION_ALLOW_PARTIAL`
- `EYT_ACTION_MAX_ITEMS`
- `EYT_ACTION_TRANSCRIPT_LANGUAGES`
- `EYT_ACTION_TARGET_CHANNELS`
- `EYT_ACTION_CHANNEL_VIDEO_LIMIT`
- `EYT_ACTION_LOG_DIR` / `EYT_LOG_DIR`
- `EYT_ACTION_RESULT_DIR` / `EYT_RESULT_DIR`
- `EYT_ACTION_MOCK_TRANSCRIPT_TEXT`
