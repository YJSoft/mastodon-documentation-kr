---
title: 반응 (Reaction)
description: 공지에 대한 이모지 반응을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/announcementreaction",
  "/entities/AnnouncementReaction",
  "/entities/reaction",
  "/entities/Reaction",
  "/api/entities/announcementreaction",
  "/api/entities/AnnouncementReaction",
  "/api/entities/reaction",
  "/api/entities/Reaction",
]
---

## 예시 {#example}

```json
[
    {
      "name": "bongoCat",
      "count": 9,
      "me": false,
      "url": "https://files.mastodon.social/custom_emojis/images/000/067/715/original/fdba57dff7576d53.png",
      "static_url": "https://files.mastodon.social/custom_emojis/images/000/067/715/static/fdba57dff7576d53.png"
    },
    {
      "name": "🤔",
      "count": 1,
      "me": true
    }
]
```

## 속성 {#attributes}

### `name` {#name}

**설명:** 반응에 사용한 이모지입니다. 유니코드 이모지 또는 사용자 지정 이모지의 단축 코드입니다.\
**유형:** 문자열\
**버전 이력:**\
3.1.0 - 추가

### `count` {#count}

**설명:** 이 반응을 추가한 총 사용자 수입니다.\
**유형:** 정수\
**버전 이력:**\
3.1.0 - 추가

### `me` {{%optional%}} {#me}

**설명:** 현재 인증된 사용자가 있는 경우, 해당 사용자가 이 반응을 추가했는지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.1.0 - 추가

### `url` {{%optional%}} {#url}

**설명:** 반응이 사용자 지정 이모지인 경우, 해당 이모지의 링크입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
3.1.0 - 추가

### `static_url` {{%optional%}} {#static_url}

**설명:** 반응이 사용자 지정 이모지인 경우, 애니메이션이 없는 버전의 링크입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
3.1.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/announcements#put-reactions" caption="공지에 반응 추가" >}}

{{< page-relref ref="methods/announcements#delete-reactions" caption="공지의 반응 삭제" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/reaction_serializer.rb" caption="app/serializers/rest/reaction_serializer.rb" >}}