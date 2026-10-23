# 한국어 번역 지침

영문 원문 `content/en`을 기준으로 같은 경로의 `content/ko`에 번역합니다. 원문의 설명, 조건, 경고, 버전 정보와 예제를 생략하거나 요약하지 않습니다. 본문은 읽기 쉬운 ‘합니다’체로 작성합니다. 원문의 오래된 내용은 번역 중 임의로 갱신하지 않습니다.

## 용어

용어 기준은 [Mastodon 공식 한국어 UI](https://github.com/mastodon/mastodon/blob/main/app/javascript/mastodon/locales/ko.json)와 [원문 작성 지침](DOCSTYLE.md)입니다.

| 원문 | 한국어 |
| --- | --- |
| Mastodon | 마스토돈 (제품명·코드에서는 Mastodon 유지 가능) |
| post, status, toot | 게시물 (API의 `Status`, `status`, `tootctl` 등은 유지) |
| server, instance | 서버 (API의 `Instance`, `instance` 등은 유지) |
| boost, reblog | 부스트 |
| favourite | 좋아요 |
| bookmark | 북마크 |
| follow / follower / following | 팔로우 / 팔로워 / 팔로잉 |
| mention | 멘션 |
| direct message, private mention | 개인 멘션 |
| public | 공개 |
| unlisted, quiet public | 조용한 공개 (API 값 `unlisted` 유지) |
| followers-only | 팔로워 전용 |
| content warning | 콘텐츠 경고 (CW) |
| sensitive content | 민감한 콘텐츠 |
| federation / fediverse | 연합 / 연합우주 |
| local / remote | 로컬 / 원격 |
| moderation / moderator | 중재 / 중재자 |
| mute / block | 뮤트 / 차단 |
| suspend / suspension | 정지 / 정지 |
| limit, silence (moderation) | 제한 (숨김) |
| quote post | 인용 게시물 |
| timeline | 타임라인 |
| profile / display name / username | 프로필 / 표시 이름 / 사용자명 |
| access token / scope | 액세스 토큰 / 범위 |
| endpoint / entity / attribute | 엔드포인트 / 엔터티 / 속성 |
| rate limit / pagination | 요청 빈도 제한 / 페이지네이션 |

## 보존할 요소

- 파일명, YAML의 `menu` 식별자·가중치, `aliases`, `url`, `translationKey` 등 라우팅 정보를 보존합니다. `title`, `description`, 표시용 `linkTitle`과 메뉴 이름은 번역합니다.
- 명시적 제목 앵커 `{#id}`와 HTML `id`는 바꾸지 않습니다. 코드 블록, 인라인 코드, HTTP 경로·메서드, JSON 키·값, 환경 변수와 CLI 명령을 보존합니다.
- Markdown 링크 목적지와 이미지 경로, Hugo shortcode 이름·구조를 보존합니다. 링크의 표시 문구, 이미지 대체 텍스트, `caption` 등 사람이 읽는 설명은 번역합니다.
- 원문의 자동 생성 제목 앵커를 참조하는 링크는 한국어 제목에서도 작동하도록 별도로 확인합니다.
- `ActivityPub`, `ActivityStreams`, `WebFinger`, `OAuth`, `JavaScript` 등 기술 이름의 공식 표기를 유지합니다.
- 직접 인용도 한국어로 옮기되 출처와 인용 형식을 유지합니다. 번역문은 원문과 같은 CC BY-SA 4.0 조건으로 제공합니다.

## 검증

전체 원문과 번역의 파일 대응, 코드 블록, 인라인 코드, 명시적 앵커, 링크 목적지와 shortcode 구조를 비교하고 Hugo Extended 0.152.2로 사이트를 빌드합니다. 번역 기준 원문 커밋은 `f9e4c011`입니다.
