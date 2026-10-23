---
title: 북마크 API 메서드
description: 북마크를 확인합니다. statuses/:id/{bookmark,unbookmark}도 참고하세요.
menu:
  docs:
    name: 북마크
    parent: methods-accounts
    identifier: methods-bookmarks
aliases: [
  "/methods/bookmarks",
  "/api/methods/bookmarks",
  "/methods/accounts/bookmarks",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 북마크한 게시물 조회 {#get}

```http
GET /api/v1/bookmarks HTTP/1.1
```

사용자가 북마크한 게시물입니다.

**반환:** 배열: [Status]({{< relref "entities/status" >}})\
**OAuth:** 사용자 토큰 + `read:bookmarks`\
**버전 이력:**\
3.1.0 - 추가\
3.3.0 - 이제 `min_id`와 `max_id` 동시 사용 가능

### 요청 {#request}
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

```json
[
  {
    "id": "108724195870225687",
    "created_at": "2022-07-28T09:12:47.000Z",
    "in_reply_to_id": null,
    "in_reply_to_account_id": null,
    "sensitive": false,
    "spoiler_text": "",
    "visibility": "public",
    // ...
  },
  {
    "id": "108200780982641655",
    "created_at": "2022-04-26T22:41:28.492Z",
    "in_reply_to_id": "108200775562138405",
    "in_reply_to_account_id": "806143",
    "sensitive": false,
    "spoiler_text": "",
    "visibility": "public",
    // ...
  },
  // ...
]
```

Bookmark ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/bookmarks?max_id=23771>; rel="next", <https://mastodon.example/api/v1/bookmarks?min_id=370065>; rel="prev"
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

{{< page-relref ref="methods/statuses#bookmark" caption="POST /api/v1/statuses/:id/bookmark" >}}

{{< page-relref ref="methods/statuses#unbookmark" caption="POST /api/v1/statuses/:id/unbookmark" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/bookmarks_controller.rb" caption="app/controllers/api/v1/bookmarks_controller.rb" >}}
