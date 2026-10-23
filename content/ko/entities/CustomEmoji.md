---
title: 사용자 지정 이모지 (CustomEmoji)
description: 사용자 지정 이모지를 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
	"/entities/emoji",
  "/entities/Emoji",
	"/entities/customemoji",
  "/entities/CustomEmoji",
  "/api/entities/emoji",
  "/api/entities/Emoji",
	"/api/entities/customemoji",
  "/api/entities/CustomEmoji",
]
---

## 예시 {#example}

```json
{
  "shortcode": "blobaww",
  "url": "https://files.mastodon.social/custom_emojis/images/000/011/739/original/blobaww.png",
  "static_url": "https://files.mastodon.social/custom_emojis/images/000/011/739/static/blobaww.png",
  "visible_in_picker": true,
  "category": "Blobs"
}
```

## 속성 {#attributes}

### `shortcode` {#shortcode}

**설명:** 사용자 지정 이모지 이름입니다.\
**유형:** 문자열\
**버전 이력:**\
2.0.0 - 추가

### `url` {#url}

**설명:** 사용자 지정 이모지 링크입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
2.0.0 - 추가

### `static_url` {#static_url}

**설명:** 사용자 지정 이모지의 정적 사본 링크입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
2.0.0 - 추가

### `visible_in_picker` {#visible_in_picker}

**설명:** 이 이모지를 선택기에 표시할지, 목록에서 숨길지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.0.0 - 추가

### `category` {#category}

**설명:** 선택기에서 사용자 지정 이모지를 정렬하는 데 사용합니다.\
**유형:** {{<nullable>}} 문자열\
**버전 이력:**\
3.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/custom_emojis" caption="GET /api/v1/custom_emojis" >}}

{{< page-relref ref="entities/Status#emojis" caption="Status (`emojis` 속성)" >}}

{{< page-relref ref="entities/Announcement#emojis" caption="Announcement (`emojis` 속성)" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/custom_emoji_serializer.rb" caption="app/serializers/rest/custom_emoji_serializer.rb" >}}





