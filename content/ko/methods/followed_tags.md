---
title: 팔로우한 태그 API 메서드
description: 팔로우한 해시태그를 확인합니다.
menu:
  docs:
    name: 팔로우한 태그
    parent: methods-accounts
    identifier: methods-followed_tags
aliases: [
  "/methods/followed_tags",
  "/api/methods/followed_tags",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 팔로우한 모든 태그 조회 {#get}

```http
GET /api/v1/followed_tags HTTP/1.1
```

팔로우한 해시태그를 나열합니다.

**반환:** 배열: [Tag]({{< relref "entities/Tag" >}})\
**OAuth:** 사용자 토큰 + `read:follows`\
**버전 이력:**\
4.0.0 - 추가\
4.1.0 - 페이지네이션 헤더 추가

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
: 정수. 반환할 최대 결과 수입니다. 기본값은 태그 100개이며 최대 200개입니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

팔로우한 해시태그 목록입니다.

```json
[
  {
    "id": "802",
    "name": "Caturday",
    "url": "http://mastodon.example/tags/caturday",
    "history": [
      {
        "day": "1668556800",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1668470400",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1668384000",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1668297600",
        "accounts": "1",
        "uses": "1"
      },
      {
        "day": "1668211200",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1668124800",
        "accounts": "0",
        "uses": "0"
      },
      {
        "day": "1668038400",
        "accounts": "0",
        "uses": "0"
      }
    ],
    "following": true
  },
  // ...
]
```

팔로우한 태그 컬렉션의 레코드를 페이지 단위로 탐색하려면 HTTP `Link` 헤더를 사용하여 더 오래되거나 새로운 결과를 가져와야 합니다. 결과의 `id` 속성은 태그의 팔로우 관계를 나타내는 레코드가 아닌 [Tag]({{< relref "entities/Tag" >}})를 가리킵니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <http://mastodon.example/api/v1/followed_tags?limit=1&max_id=2>; rel="next", <http://mastodon.example/api/v1/followed_tags?limit=1&since_id=2>; rel="prev"
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

{{< page-relref ref="methods/tags#follow" caption="POST /api/v1/tags/:id/follow" >}}

{{< page-relref ref="methods/tags#unfollow" caption="POST /api/v1/tags/:id/unfollow" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/followed_tags_controller.rb" caption="app/controllers/api/v1/followed_tags_controller.rb" >}}
