# economic-youtube-action-items-skill

경제 유튜브 영상에서 실행 가능한 액션 아이템을 영상 단위로 추출합니다.

각 영상 출력 블록은 다음 순서로 제공합니다.

1. 채널명
2. 영상 제목
3. 링크
4. 액션 아이템 리스트(우선순위 포함)

## Features

- 종료된 라이브 영상(`ended_live`) 분기
- 환경변수 기반 설정 (`EYT_ACTION_*`)
- Markdown / JSON 출력
- Contract v1 JSON Schema 포함

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
```

`.env`는 실행 시 자동 로드됩니다(`source .env` 불필요).

```bash
eyt-action-items generate \
  --video-url "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

채널 환경변수 기반 실행(채널명/채널코드/핸들):

```bash
export EYT_ACTION_TARGET_CHANNELS="UC_x5XG1OV2P6uZZ5FSM9Ttw,@mkbhd,한국경제TV"
export EYT_ACTION_CHANNEL_VIDEO_LIMIT=3
eyt-action-items generate
```

## Environment Variables

| Variable | Default | Description |
|---|---:|---|
| `EYT_ACTION_MIN_TRANSCRIPT_CHARS` | `700` | partial/complete 판단 기준 |
| `EYT_ACTION_ALLOW_PARTIAL` | `true` | 부분 자막 허용 여부 |
| `EYT_ACTION_MAX_ITEMS` | `7` | 영상당 최대 액션 아이템 수 |
| `EYT_ACTION_TRANSCRIPT_LANGUAGES` | `ko,en` | 자막 언어 우선순위 |
| `EYT_ACTION_TARGET_CHANNELS` | _empty_ | 채널 토큰 목록(쉼표 구분, 채널명/채널코드/핸들) |
| `EYT_ACTION_CHANNEL_VIDEO_LIMIT` | `5` | 채널별 수집 영상 수 |
| `EYT_ACTION_MOCK_TRANSCRIPT_TEXT` | _empty_ | 테스트용 강제 자막 |

## Test

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT
