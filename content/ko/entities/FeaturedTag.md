---
title: 추천 태그 (FeaturedTag)
description: 계정 프로필에 소개하는 해시태그를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/featuredtag",
	"/entities/FeaturedTag",
  "/api/entities/featuredtag",
	"/api/entities/FeaturedTag",
]
---

## 예시 {#example}

```json
{
  "id": "627",
  "name": "nowplaying",
  "url": "https://mastodon.social/@trwnh/tagged/nowplaying",
  "statuses_count": "70",
  "last_status_at": "2022-08-29"
}
```

## 속성 {#attributes}

### `id` {#id}

**설명:** 소개한 태그의 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
3.0.0 - 추가

### `name` {#name}

**설명:** 소개하는 해시태그의 이름입니다.\
**유형:** 문자열\
**버전 이력:**\
3.0.0 - 추가

### `url` {#url}

**설명:** 이 해시태그가 포함된 사용자의 모든 게시물 링크입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
3.3.0 - 추가

### `statuses_count` {#statuses_count}

**설명:** 이 해시태그가 포함된 작성 게시물 수입니다.\
**유형:** 문자열\
**버전 이력:**\
3.0.0 - 추가

### `last_status_at` {#last_status_at}

**설명:** 이 해시태그가 포함된 마지막 작성 게시물의 날짜입니다.\
**유형:** {{<nullable>}} 문자열 ([날짜](/api/datetime-format#date))\
**버전 이력:**\
3.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/featured_tags" caption="featured_tags API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/featured_tag_serializer.rb" caption="app/serializers/rest/featured_tag_serializer.rb" >}}
