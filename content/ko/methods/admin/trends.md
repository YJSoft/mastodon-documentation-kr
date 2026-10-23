---
title: 관리자 인기 항목 API 메서드
description: 인기 링크, 게시물, 태그를 중재합니다.
menu:
  docs:
    name: 인기 항목
    parent: methods-admin
    identifier: methods-admin-trends
aliases: [
  "/methods/admin/trends",
  "/api/methods/admin/trends",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 인기 링크 조회 {#links}

```http
GET /api/v1/admin/trends/links HTTP/1.1
```

승인되지 않았거나 검토되지 않은 링크를 포함하여 다른 링크보다 많이 공유된 링크입니다.

**반환:** 배열: [Trends::Link]({{< relref "entities/PreviewCard#trends-link" >}})\
**OAuth:** 사용자 토큰 + `admin:read`\
**권한:** 분류 관리\
**버전 이력:**\
3.5.0 - 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

```json
[
  {
    "url": "https://twitter.com/arufa_faru/status/1594262272007753728",
    "title": "ARuFa on Twitter",
    "description": "“言葉をマネするぬいぐるみを改造してエレキギターを直接繋いでみました”",
    "type": "link",
    "author_name": "",
    "author_url": "",
    "provider_name": "Twitter",
    "provider_url": "",
    "html": "",
    "width": 400,
    "height": 225,
    "image": "https://media.chitter.xyz/cache/preview_cards/images/002/162/720/original/b5360261e8ce17fc.jpeg",
    "embed_url": "",
    "blurhash": "UNFiDM~o-oD%x[xtaxM|xaNHRkjsoft7ofWB",
    "history": [
      {
        "day": "1669507200",
        "accounts": "9",
        "uses": "9"
      },
      {
        "day": "1669420800",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1669334400",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1669248000",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1669161600",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1669075200",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1668988800",
        "accounts": "0",
        "uses": "0"
      }
    ]
  },
  // ...
]
```

##### 403: 금지됨 {#403-forbidden}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

## 인기 게시물 조회 {#statuses}

```http
GET /api/v1/admin/trends/statuses HTTP/1.1
```

승인되지 않았거나 검토되지 않은 게시물을 포함하여 다른 게시물보다 상호작용이 많은 게시물입니다.

**반환:** 배열: [Status]({{< relref "entities/Status" >}})\
**OAuth:** 사용자 토큰 + `admin:read`\
**권한:** 분류 관리\
**버전 이력:**\
3.5.0 - 추가

#### 요청 {#request-1}

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

```json
[
  {
    "id": "109415512969053017",
    "created_at": "2022-11-27T11:23:52.000Z",
    "in_reply_to_id": null,
    "in_reply_to_account_id": null,
    // ...
    "account": {
      "id": "109332240210946752",
      // ...
    },
    "media_attachments": [],
    "mentions": [],
    "tags": [],
    "emojis": [],
    "card": null,
    "poll": null
  },
  // ...
]
```

##### 403: 금지됨 {#403-forbidden-1}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

## 인기 태그 조회 {#tags}

```http
GET /api/v1/admin/trends/tags HTTP/1.1
```

승인되지 않았거나 검토되지 않은 태그를 포함하여 지난 일주일간 더 자주 사용된 태그입니다.

**반환:** 배열: [Admin::Tag]({{< relref "entities/Tag#admin" >}})\
**OAuth:** 사용자 토큰 + `admin:read`\
**권한:** 분류 관리\
**버전 이력:**\
3.5.0 - 추가\
4.0.0 - 버그로 인해 Tag 배열 반환\
4.1.0 - 버그 수정 <!-- TODO: https://github.com/mastodon/mastodon/pull/18943 -->

#### 요청 {#request-2}

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

```json
[
  {
    "id": "802",
    "name": "caturday",
    "url": "https://mastodon.example/tags/caturday",
    "history": [
      {
        "day": "1669507200",
        "accounts": "53",
        "uses": "56"
      },
      {
        "day": "1669420800",
        "accounts": "142",
        "uses": "171"
      },
      {
        "day": "1669334400",
        "accounts": "11",
        "uses": "11"
      },
      {
        "day": "1669248000",
        "accounts": "8",
        "uses": "9"
      },
      {
        "day": "1669161600",
        "accounts": "8",
        "uses": "20"
      },
      {
        "day": "1669075200",
        "accounts": "11",
        "uses": "11"
      },
      {
        "day": "1668988800",
        "accounts": "17",
        "uses": "22"
      }
    ],
    "trendable": true,
    "usable": true,
    "requires_review": false
  },
]
```

##### 403: 금지됨 {#403-forbidden-2}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/trends/links_controller.rb" caption="app/controllers/api/v1/admin/trends/links_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/trends/statuses_controller.rb" caption="app/controllers/api/v1/admin/trends/statuses_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/trends/tags_controller.rb" caption="app/controllers/api/v1/admin/trends/tags_controller.rb" >}}