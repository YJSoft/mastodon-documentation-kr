---
title: 계정 관계 (Relationship)
description: 팔로우, 차단, 뮤트 등 계정 간의 관계를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/relationship",
  "/entities/Relationship",
  "/api/entities/relationship",
  "/api/entities/Relationship",
]
---

## 예시 {#example}

```json
{
  "id": "1",
  "following": true,
  "showing_reblogs": true,
  "notifying": false,
  "followed_by": true,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "muting_expires_at": null,
  "requested": false,
  "requested_by": false,
  "domain_blocking": false,
  "endorsed": false,
  "note": ""
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 계정 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
0.6.0 - 추가

### `following` {#following}

**설명:** 이 사용자를 팔로우하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
0.6.0 - 추가

### `showing_reblogs` {#showing_reblogs}

**설명:** 이 사용자의 부스트를 홈 타임라인에서 받는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.1.0 - 추가

### `notifying` {#notifying}

**설명:** 이 사용자에 대한 알림을 켰는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.3.0 - 추가

### `languages` {#languages}

**설명:** 이 사용자의 게시물을 받아 볼 언어입니다.\
**유형:** {{<nullable>}} 배열: 문자열 (ISO 639-1 두 글자 언어 코드)\
**버전 이력:**\
4.0.0 - 추가

### `followed_by` {#followed_by}

**설명:** 이 사용자가 나를 팔로우하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
0.6.0 - 추가

### `blocking` {#blocking}

**설명:** 이 사용자를 차단하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
0.6.0 - 추가

### `blocked_by` {#blocked_by}

**설명:** 이 사용자가 나를 차단하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.8.0 - 추가

### `muting` {#muting}

**설명:** 이 사용자를 뮤트하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
1.1.0 - 추가

### `muting_notifications` {#muting_notifications}

**설명:** 이 사용자의 알림을 뮤트하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.1.0 - 추가

### `muting_expires_at` {#muting_expires_at}

**설명:** 있는 경우, 뮤트가 만료되는 날짜입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.6.0 - 추가

### `requested` {#requested}

**설명:** 이 사용자에 대한 대기 중인 팔로우 요청이 있는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
0.9.9 - 추가

### `requested_by` {#requested_by}

**설명:** 이 사용자가 나에게 팔로우를 요청했는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.1.0 - 추가

### `domain_blocking` {#domain_blocking}

**설명:** 이 사용자의 도메인을 차단하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
1.4.0 - 추가

### `endorsed` {#endorsed}

**설명:** 이 사용자를 내 프로필에 소개하는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.5.0 - 추가

### `note` {#note}

**설명:** 인증된 사용자가 이 계정에 대해 작성한 개인 메모입니다.\
**유형:** 문자열\
**버전 이력:**\
3.2.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/accounts#relationships" caption="GET /api/v1/accounts/relationships" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/relationship_serializer.rb" caption="app/serializers/rest/relationship_serializer.rb" >}}
