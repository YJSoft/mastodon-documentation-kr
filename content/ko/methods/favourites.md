---
title: 좋아요 API 메서드
description: 좋아요 목록을 확인합니다. statuses/:id/{favourite,unfavourite}도 참고하세요.
menu:
  docs:
    name: 좋아요
    parent: methods-accounts
    identifier: methods-favourites
aliases: [
  "/methods/favourites",
  "/api/methods/favourites",
  "/methods/accounts/favourites",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 좋아요한 게시물 조회 {#get}

```http
GET /api/v1/favourites HTTP/1.1
```

사용자가 좋아요한 게시물입니다.

**반환:** 배열: [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `read:favourites`\
**버전:**\
0.0.0 - 추가\
2.6.0 - `min_id` 추가\
3.3.0 - 이제 `min_id`와 `max_id` 동시 사용 가능

#### 요청 {#request}
##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters}

max_id 
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

since_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

min_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 게시물 20개이며 최대 40개입니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

limit=2인 호출 예입니다.

```json
[
  {
    "id": "103186075217296344",
    "created_at": "2019-11-23T07:35:52.000Z",
    "in_reply_to_id": null,
    "in_reply_to_account_id": null,
    "sensitive": false,
    "spoiler_text": "",
    "visibility": "unlisted",
    "language": "enCy",
    "uri": "https://cybre.space/users/haskal/statuses/103186075002013902",
    "url": "https://cybre.space/@haskal/103186075002013902",
    "replies_count": 0,
    "reblogs_count": 1,
    "favourites_count": 1,
    "favourited": true,
    "reblogged": false,
    "muted": false,
    "bookmarked": false,
    "content": "<p>the pirate gay</p>",
    "reblog": null,
    "account": {
      "id": "297420",
      "username": "haskal",
      "acct": "haskal@cybre.space",
      "display_name": "soft nb friend :blobcatsleep:",
      // ...
    },
    "media_attachments": [],
    "mentions": [],
    "tags": [],
    "emojis": [],
    "card": null,
    "poll": null
  },
  {
    "id": "103186044372624124",
    "created_at": "2019-11-23T07:28:03.000Z",
    // ...
    "content": "<p>cute,,,</p>",
    "reblog": null,
    "account": {
      "id": "297420",
      "username": "haskal",
      "acct": "haskal@cybre.space",
      "display_name": "soft nb friend :blobcatsleep:",
      "locked": false,
      "bot": false,
      // ...
    },
    // ...
  }
]
```

Favourite ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/favourites?limit=2&max_id=23716836>; rel="next", <https://mastodon.example/api/v1/favourites?limit=2&min_id=23716978>; rel="prev"
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/statuses#favourite" caption="POST /api/v1/statuses/:id/favourite" >}}

{{< page-relref ref="methods/statuses#unfavourite" caption="POST /api/v1/statuses/:id/unfavourite" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/favourites_controller.rb" caption="app/controllers/api/v1/favourites_controller.rb" >}}
