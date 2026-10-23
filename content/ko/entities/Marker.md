---
title: 읽기 위치 (Marker)
description: 사용자 타임라인에서 마지막으로 읽은 위치를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/marker",
  "/entities/Marker",
  "/api/entities/marker",
  "/api/entities/Marker",
]
---

## 예시 {#example}

```json
{
  "last_read_id": "103194548672408537",
  "version": 462,
  "updated_at": "2019-11-24T19:39:39.337Z"
}
```

## 속성 {#attributes}

### `last_read_id` {#last_read_id}

**설명:** 가장 최근에 본 엔터티의 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
3.0.0 - 추가

### `version` {#version}

**설명:** 쓰기 충돌을 막는 잠금에 사용하는 증가 카운터입니다.\
**유형:** 정수\
**버전 이력:**\
3.0.0 - 추가

### `updated_at` {#updated_at}

**설명:** 마커를 설정한 시각의 타임스탬프입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
3.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/markers" caption="markers API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/marker_serializer.rb" caption="app/serializers/rest/marker_serializer.rb" >}}



