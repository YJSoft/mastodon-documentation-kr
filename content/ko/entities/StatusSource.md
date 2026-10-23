---
title: 게시물 원본 (StatusSource)
description: 게시물의 원본을 일반 텍스트로 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/statussource",
  "/entities/StatusSource",
  "/api/entities/statussource",
  "/api/entities/StatusSource",
]
---

## 예시 {#example}

```json
{
  "id": "108942703571991143",
  "text": "this is a status that will be edited",
  "spoiler_text": ""
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 게시물 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
3.5.0 - 추가

### `text` {#text}

**설명:** 게시물 작성에 사용한 일반 텍스트입니다.\
**유형:** 문자열\
**버전 이력:**\
3.5.0 - 추가

### `spoiler_text` {#spoiler_text}

**설명:** 게시물의 제목 또는 콘텐츠 경고 작성에 사용한 일반 텍스트입니다.\
**유형:** 문자열\
**버전 이력:**\
3.5.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/statuses#source" caption="GET /api/v1/statuses/:id/source" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/status_source_serializer.rb" caption="app/serializers/rest/status_source_serializer.rb" >}}