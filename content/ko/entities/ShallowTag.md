---
title: 간략한 태그 (ShallowTag)
description: 해시태그의 최소 표현입니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/shallowtag",
  "/entities/ShallowTag",
  "/api/entities/shallowtag",
  "/api/entities/ShallowTag",
]
---

## 예시 {#example}

```json
{
  "name": "nowplaying",
  "url": "https://mastodon.social/tags/nowplaying"
}
```

## 속성 {#attributes}

### `name` {#name}

**설명:** # 기호 뒤의 해시태그 값입니다.\
**유형:** 문자열\
**버전 이력:**\
4.6.0 - 추가

### `url` {#url}

**설명:** 로컬 서버의 해시태그 링크입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
4.6.0 - 추가

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/shallow_tag_serializer.rb" caption="app/serializers/rest/shallow_tag_serializer.rb" >}}
