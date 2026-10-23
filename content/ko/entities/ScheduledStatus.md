---
title: 예약 게시물 (ScheduledStatus)
description: 미래의 예약된 날짜에 게시할 게시물을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/scheduledstatus",
  "/entities/ScheduledStatus",
  "/api/entities/scheduledstatus",
  "/api/entities/ScheduledStatus",
]
---

## 예시 {#example}

`POST /api/v1/statuses?status=test post&scheduled_at=2022-09-29`의 반환값

```json
{
  "id": "1",
  "scheduled_at": "2022-09-29T00:00:00.000Z",
  "params": {
    "text": "test post",
    "media_ids": null,
    "sensitive": null,
    "spoiler_text": null,
    "visibility": null,
    "language": null,
    "scheduled_at": null,
    "poll": null,
    "idempotency": null,
    "with_rate_limit": false,
    "in_reply_to_id": null,
    "application_id": 3,
    "quoted_status_id": null,
    "quote_approval_policy": "followers"
  },
  "media_attachments": []
}
```

`GET /api/v1/scheduled_statuses`의 반환값:

```json
{
  "id": "1",
  "scheduled_at": "2022-09-29T00:00:00.000Z",
  "params": {
    "poll": null,
    "text": "test post",
    "language": null,
    "media_ids": null,
    "sensitive": null,
    "visibility": null,
    "idempotency": null,
    "scheduled_at": null,
    "spoiler_text": null,
    "application_id": 3,
    "in_reply_to_id": null,
    "with_rate_limit": false,
    "quoted_status_id": null,
    "quote_approval_policy": "followers"
  },
  "media_attachments": []
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 예약 게시물 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
2.7.0 - 추가

### `scheduled_at` {#scheduled_at}

**설명:** 게시물을 올릴 시각의 타임스탬프입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
2.7.0 - 추가

### `params` {#params}

**설명:** 게시물을 예약할 때 사용한 매개변수로, 게시물을 올릴 때 사용합니다.\
**유형:** 해시\
**버전 이력:**\
2.7.0 - 추가

#### `params[text]` {#params-text}

**설명:** 게시물 콘텐츠로 사용할 텍스트입니다.\
**유형:** 문자열\
**버전 이력:**\
2.7.0 - 추가

#### `params[poll]` {#params-poll}

**설명:** 게시물에 첨부할 투표입니다.\
**유형:** {{<nullable>}} 해시\
**버전 이력:**\
2.8.0 - 추가

##### `params[poll][options[]]` {#params-poll-options}

**설명:** 사용할 투표 선택지입니다.\
**유형:** 배열: 문자열\
**버전 이력:**\
2.8.0 - 추가

##### `params[poll][expires_in]` {#params-poll-expires_in}

**설명:** 투표가 종료되기 전까지 유지할 시간(초)입니다.\
**유형:** 정수\
**버전 이력:**\
2.8.0 - 추가

##### `params[poll][multiple]` {#params-poll-multiple}

**설명:** 투표에서 복수 선택을 허용할지 나타냅니다.\
**유형:** {{<optional>}} 불리언\
**버전 이력:**\
2.8.0 - 추가

##### `params[poll][hide_totals]` {#params-poll-hide_totals}

**설명:** 투표가 종료될 때까지 총 득표수를 숨길지 나타냅니다.\
**유형:** {{<optional>}} 불리언\
**버전 이력:**\
2.8.0 - 추가

#### `params[media_ids]` {#params-media_ids}

**설명:** 게시물에 첨부할 MediaAttachments의 ID입니다.\
**유형:** {{<nullable>}} 배열: 문자열\
**버전 이력:**\
2.7.0 - 추가

#### `params[sensitive]` {#params-sensitive}

**설명:** 게시물에 민감함 표시를 할지 나타냅니다.\
**유형:** {{<nullable>}} 불리언\
**버전 이력:**\
2.7.0 - 추가

#### `params[spoiler_text]` {#params-spoiler_text}

**설명:** 게시물의 콘텐츠 경고 또는 요약 텍스트입니다.\
**유형:** {{<nullable>}} 문자열\
**버전 이력:**\
2.7.0 - 추가

#### `params[visibility]` {#params-visibility}

**설명:** 게시물을 올린 후의 공개 범위입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`public` = 누구나 볼 수 있으며 공개 타임라인에 표시합니다.\
`unlisted` = 공개적으로 볼 수 있지만 공개 타임라인에는 포함하지 않습니다.\
`private` = 팔로워와 멘션된 사용자만 볼 수 있습니다.\
`direct` = 멘션된 사용자만 볼 수 있습니다.\
**버전 이력:**\
2.7.0 - 추가

#### `params[in_reply_to_id]` {#params-in_reply_to_id}

**설명:** 답글을 달 대상 Status의 ID입니다.\
**유형:** {{<nullable>}} 정수\
**버전 이력:**\
2.7.0 - 추가

#### `params[language]` {#params-language}

**설명:** 게시물에 사용할 언어입니다.\
**유형:** {{<nullable>}} 문자열 (ISO 639-1 두 글자 언어 코드)\
**버전 이력:**\
2.7.0 - 추가

#### `params[application_id]` {{%deprecated%}} {#params-application_id}

**설명:** 게시물을 올린 Application의 내부 ID입니다. 과거 버전과의 호환성을 위해서만 제공하며 무시해도 됩니다.\
**유형:** 정수\
**버전 이력:**\
2.7.0 - 추가

#### `params[scheduled_at]` {#params-scheduled_at}

**설명:** 게시물을 예약할 시각입니다. 게시물은 한 번만 예약하므로 null입니다.\
**유형:** {{<nullable>}} null\
**버전 이력:**\
2.7.0 - 추가

#### `params[idempotency]` {#params-idempotency}

**설명:** 중복 게시물을 방지하는 멱등성 키입니다.\
**유형:** {{<nullable>}} 문자열\
**버전 이력:**\
2.7.0 - 추가

#### `params[quoted_status_id]` {#params-quoted_status_id}

**설명:** 인용할 Status의 ID입니다.\
**유형:** {{<nullable>}} 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.5.0 - 추가

#### `params[quote_approval_policy]` {#params-quote_approval_policy}

**설명:** Status의 인용 정책입니다.\
**유형:** 문자열 (열거형, 다음 중 하나)\
`public` = 차단된 계정을 제외한 누구나 인용할 수 있습니다.\
`followers` = 팔로워와 작성자만 인용할 수 있습니다.\
`nobody` = 작성자만 인용할 수 있습니다.\
**버전 이력:**\
4.5.0 - 추가

#### `params[with_rate_limit]` {{%deprecated%}} {#params-with_rate_limit}

**설명:** 게시물 생성에 요청 빈도 제한이 적용되는지 나타냅니다. 과거 버전과의 호환성을 위해서만 제공하며 무시해도 됩니다.\
**유형:** 불리언\
**버전 이력:**\
2.7.0 - 추가

### `media_attachments` {#media_attachments}

**설명:** 게시물을 올릴 때 첨부할 미디어입니다.\
**유형:** 배열: [MediaAttachment]({{< relref "entities/MediaAttachment" >}})\
**버전 이력:**\
2.7.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/statuses#create" caption="POST /api/v1/statuses (`scheduled_at` 매개변수 사용)" >}}

{{< page-relref ref="methods/scheduled_statuses" caption="scheduled_statuses API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/scheduled_status_serializer.rb" caption="app/serializers/rest/scheduled_status_serializer.rb" >}}



