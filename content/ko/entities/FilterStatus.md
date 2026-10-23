---
title: 필터 게시물 (FilterStatus)
description: 일치할 경우 필터 동작을 실행해야 하는 게시물 ID를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/filterstatus",
	"/entities/FilterStatus",
	"/api/entities/filterstatus",
	"/api/entities/FilterStatus",
]
---

## 예시 {#example}

```json
{
	"id": "1",
	"status_id": "109031743575371913"
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 FilterStatus ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.0.0 - 추가

### `status_id` {#keyword}

**설명:** 필터링할 Status의 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="api/guidelines#filters" caption="필터 구현 지침" >}}

{{< page-relref ref="methods/filters" caption="/api/v2/filters 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/filter_status_serializer.rb" caption="app/serializers/rest/filter_status_serializer.rb" >}}