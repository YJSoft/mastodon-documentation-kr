---
title: 리스트 (List)
description: 인증된 사용자가 팔로우하는 사용자 일부로 구성된 리스트를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/list",
  "/entities/List",
  "/api/entities/list",
  "/api/entities/List",
]
---

## 예시 {#example}

```json
{
  "id": "12249",
  "title": "Friends",
  "replies_policy": "list",
  "exclusive": false
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 리스트 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
2.1.0 - 추가

### `title` {#title}

**설명:** 사용자가 지정한 리스트 제목입니다.\
**유형:** 문자열\
**버전 이력:**\
2.1.0 - 추가

### `replies_policy` {#replies_policy}

**설명:** 리스트에 표시할 답글입니다.\
**유형:** 문자열 (열거형 다음 중 하나)\
`followed` = 팔로우하는 모든 사용자에게 단 답글을 표시합니다.\
`list` = 리스트 구성원에게 단 답글을 표시합니다.\
`none` = 답글을 표시하지 않습니다.\
**버전 이력:**\
3.3.0 - 추가

### `exclusive` {#exclusive}

**설명:** 리스트 구성원을 “홈” 피드에서 제외할지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.2.0 - 추가

{{< page-relref ref="methods/accounts#lists" caption="GET /api/v1/accounts/:id/lists" >}}

{{< page-relref ref="methods/lists" caption="lists API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/list_serializer.rb" caption="app/serializers/rest/list_serializer.rb" >}}
