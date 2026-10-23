---
title: OEmbed API 메서드
description: OEmbed 미리보기를 생성합니다.
menu:
  docs:
    name: OEmbed
    parent: methods
    identifier: methods-oembed
aliases: [
  "/methods/oembed",
  "/api/methods/oembed",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## OEmbed 정보를 JSON으로 가져오기 {#get}

```http
GET /api/oembed HTTP/1.1
```

**반환:** OEmbed 메타데이터\
**OAuth:** 공개\
**버전 이력:**\
1.0.0 - 추가

#### 요청 {#request}
##### 쿼리 매개변수 {#query-parameters}

url
: {{<required>}} 문자열. 게시물 URL입니다.

maxwidth
: 숫자. iframe 너비입니다. 기본값은 400입니다.

maxheight
: 숫자. iframe 높이입니다. 기본값은 null입니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

관련 iframe과 메타데이터를 포함하는 OEmbed "rich" 미리보기를 나타냅니다.

```json
{
  "type": "rich",
  "version": "1.0",
  "title": "New status by trwnh",
  "author_name": "infinite love ⴳ",
  "author_url": "https://mastodon.social/@trwnh",
  "provider_name": "mastodon.social",
  "provider_url": "https://mastodon.social/",
  "cache_age": 86400,
  "html": "<iframe src=\"https://mastodon.social/@trwnh/99664077509711321/embed\" class=\"mastodon-embed\" style=\"max-width: 100%; border: 0\" width=\"400\" allowfullscreen=\"allowfullscreen\"></iframe><script src=\"https://mastodon.social/embed.js\" async=\"async\"></script>",
  "width": 400,
  "height": null
}
```

##### 404: 찾을 수 없음 {#404-not-found}

지정한 URL에 해당하는 게시물이 없습니다.

```json
{
  "error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/oembed_controller.rb" caption="app/controllers/api/oembed_controller.rb" >}}
