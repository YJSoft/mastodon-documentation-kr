---
title: 필터 결과 (FilterResult)
description: 키워드가 주어진 게시물과 일치한 필터를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/filterresult",
	"/entities/FilterResult",
  "/api/entities/filterresult",
	"/api/entities/FilterResult",
]
---

## 예시 {#example}

```json
{
  "filter": {
    "id": "3",
    "title": "Hide completely",
    "context": [
      "home"
    ],
    "expires_at": "2022-09-20T17:27:39.296Z",
    "filter_action": "hide"
  },
  "keyword_matches": [
    "bad word"
  ],
  "status_matches": [
    "109031743575371913"
  ]
}
```

## 속성 {#attributes}

### `filter` {#filter}

**설명:** 일치한 필터입니다.\
**유형:** [Filter]({{< relref "entities/Filter" >}})\
**버전 이력:**\
4.0.0 - 추가

### `keyword_matches` {#keyword_matches}

**설명:** 일치한 필터 내 키워드입니다.\
**유형:** {{<nullable>}} 배열: 문자열, 또는 null\
**버전 이력:**\
4.0.0 - 추가

### `status_matches` {#status_matches}

**설명:** 일치한 필터 내 게시물 ID입니다.\
**유형:** {{<nullable>}} 배열: 문자열, 또는 null\
**버전 이력:**\
4.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="api/guidelines#filters" caption="필터 구현 지침" >}}

{{< page-relref ref="methods/filters" caption="/api/v2/filters 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/filter_result_serializer.rb" caption="app/serializers/rest/filter_result_serializer.rb" >}}
