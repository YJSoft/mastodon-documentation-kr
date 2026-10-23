---
title: 사용자 지정 이모지 API 메서드
description: >-
  각 사이트는 프로필이나 게시물에 첨부할 자체 사용자 지정 이모지를 정의하고 업로드할 수 있습니다.
menu:
  docs:
    name: 사용자 지정 이모지
    parent: methods-instance
    identifier: methods-custom_emojis
aliases: [
  "/methods/custom_emojis",
  "/api/methods/custom_emojis",
  "/methods/instance/custom_emojis"
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 모든 사용자 지정 이모지 조회 {#get}

```http
GET /api/v1/custom_emojis HTTP/1.1
```

서버에서 사용할 수 있는 사용자 지정 이모지를 반환합니다.

**반환:** 배열: [CustomEmoji]({{< relref "entities/CustomEmoji" >}})\
**OAuth:** 공개\
**버전 이력:**\
2.0.0 - 추가\
3.0.0 - 응답에 선택적 `category` 추가

#### 응답 {#response}
##### 200: 성공 {#200-ok}

mastodon.social의 응답 예입니다.

```json
[
  {
    "shortcode": "aaaa",
    "url": "https://files.mastodon.social/custom_emojis/images/000/007/118/original/aaaa.png",
    "static_url": "https://files.mastodon.social/custom_emojis/images/000/007/118/static/aaaa.png",
    "visible_in_picker": true
  },
  {
    "shortcode": "AAAAAA",
    "url": "https://files.mastodon.social/custom_emojis/images/000/071/387/original/AAAAAA.png",
    "static_url": "https://files.mastodon.social/custom_emojis/images/000/071/387/static/AAAAAA.png",
    "visible_in_picker": true
  },

  // [...]

  {
    "shortcode": "blobaww",
    "url": "https://files.mastodon.social/custom_emojis/images/000/011/739/original/blobaww.png",
    "static_url": "https://files.mastodon.social/custom_emojis/images/000/011/739/static/blobaww.png",
    "visible_in_picker": true,
    "category": "Blobs"
  },

  // [...]

  {
    "shortcode": "yikes",
    "url": "https://files.mastodon.social/custom_emojis/images/000/031/275/original/yikes.png",
    "static_url": "https://files.mastodon.social/custom_emojis/images/000/031/275/static/yikes.png",
    "visible_in_picker": true
  },
  {
    "shortcode": "ziltoid",
    "url": "https://files.mastodon.social/custom_emojis/images/000/017/094/original/05252745eb087806.png",
    "static_url": "https://files.mastodon.social/custom_emojis/images/000/017/094/static/05252745eb087806.png",
    "visible_in_picker": true
  }
]
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/custom_emojis_controller.rb" caption="app/controllers/api/v1/custom_emojis_controller.rb" >}}
