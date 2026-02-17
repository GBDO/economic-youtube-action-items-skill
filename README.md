# economic-youtube-action-items-skill

경제 유튜브 영상에서 실행 가능한 액션 아이템을 영상 단위로 추출합니다.

각 영상 출력 블록은 다음 순서로 제공합니다.

1. 채널명
2. 영상 제목
3. 링크
4. 액션 아이템 리스트(우선순위 포함)

## Features

- 종료된 라이브 영상(`ended_live`) 분기
- 자막 조회 SSL 인증 실패 시 `verify=False` 재시도(기본 활성화, 경고 출력)
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

로그/결과 파일은 **날짜 기준으로 자동 통합**됩니다.

- 로그: `action-items-YYYYMMDD.log`
- 결과: `action-items-YYYYMMDD.jsonl`

공통 디렉터리 예시:

```bash
export EYT_LOG_DIR=/tmp/eyt-logs
export EYT_RESULT_DIR=/tmp/eyt-results
```

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
| `EYT_ACTION_INSECURE_SSL_FALLBACK` | `true` | SSL 인증 실패 시 `verify=False` 재시도 허용 여부 |
| `EYT_ACTION_MAX_ITEMS` | `7` | 영상당 최대 액션 아이템 수 |
| `EYT_ACTION_TRANSCRIPT_LANGUAGES` | `ko,en` | 자막 언어 우선순위 |
| `EYT_ACTION_PROXY_HTTP_URL` | _empty_ | Generic proxy HTTP URL (`EYT_ACTION_PROXY_HTTPS_URL`와 함께 또는 단독 사용) |
| `EYT_ACTION_PROXY_HTTPS_URL` | _empty_ | Generic proxy HTTPS URL |
| `EYT_ACTION_WEBSHARE_PROXY_USERNAME` | _empty_ | Webshare proxy username (설정 시 Generic보다 우선) |
| `EYT_ACTION_WEBSHARE_PROXY_PASSWORD` | _empty_ | Webshare proxy password |
| `EYT_ACTION_WEBSHARE_PROXY_LOCATIONS` | _empty_ | Webshare location code 목록(쉼표 구분, 예: `us,kr`) |
| `EYT_ACTION_WEBSHARE_RETRIES_WHEN_BLOCKED` | `10` | Webshare 사용 시 차단 응답 재시도 횟수 |
| `EYT_ACTION_TRANSCRIPT_REQUEST_DELAY_MS` | `0` | 영상별 자막 조회 사이 지연(ms) |
| `EYT_ACTION_TARGET_CHANNELS` | _empty_ | 채널 토큰 목록(쉼표 구분, 채널명/채널코드/핸들) |
| `EYT_ACTION_CHANNEL_VIDEO_LIMIT` | `5` | 채널별 수집 영상 수 |
| `EYT_ACTION_LOG_DIR` | `logs` | 로그 디렉터리 (`EYT_LOG_DIR` 공통 변수도 지원) |
| `EYT_ACTION_RESULT_DIR` | `results` | 결과 파일 디렉터리 (`EYT_RESULT_DIR` 공통 변수도 지원) |
| `EYT_ACTION_MOCK_TRANSCRIPT_TEXT` | _empty_ | 테스트용 강제 자막 |

## Warning diagnostics

- 자막 조회 실패 시 결과 `warnings`에 예외 클래스 + 메시지가 포함됩니다.
- SSL 인증 실패로 `verify=False` 재시도를 수행한 경우, 해당 사실이 `warnings`에 기록됩니다.
- `IpBlocked`/`RequestBlocked`/`TooManyRequests`/HTTP `429` 징후가 감지되면 proxy 환경변수 설정 안내가 `warnings`에 추가됩니다.
- 채널 토큰 해석 실패는 `invalid handle format`, `could not resolve channel id`, `no uploads feed`처럼 원인별 메시지로 출력됩니다.

## Test

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT
