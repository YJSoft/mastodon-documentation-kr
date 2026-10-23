---
title: 차단 API 메서드
description: 차단 목록을 확인합니다. accounts/:id/{block,unblock}도 참고하세요.
menu:
  docs:
    name: 차단
    parent: methods-accounts
    identifier: methods-blocks
aliases: [
  "/methods/blocks",
  "/api/methods/blocks",
  "/methods/accounts/blocks",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 차단한 사용자 조회 {#get}

```http
GET /api/v1/blocks HTTP/1.1
```

차단한 계정을 반환합니다.

**반환:** 배열: [Account]({{< relref "entities/account" >}})\
**OAuth:** 사용자 토큰 + `read:blocks`\
**버전 이력:**\
0.0.0 - 추가\
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
: 정수. 반환할 최대 결과 수입니다. 기본값은 계정 40개이며 최대 80개입니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

limit=2인 호출 예입니다.

```json
[
  {
    "id": "585315",
    "username": "admin",
    "acct": "admin@happylittle.cloudns.cc",
    "display_name": "☁️  ⛅ Happy Little Clouds ⛅ ☁️",
    // ...
  },
  {
    "id": "650568",
    "username": "Nikolai_Kingsley",
    "acct": "Nikolai_Kingsley@dobbs.town",
    "display_name": "Rev.Dr. Nikolai Kingsley",
    // ...
  }
]
```

Block ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/blocks?limit=2&max_id=441449>; rel="next", <https://mastodon.example/api/v1/blocks?limit=2&since_id=444808>; rel="prev"
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

{{< page-relref ref="methods/accounts#block" caption="POST /api/v1/accounts/:id/block" >}}

{{< page-relref ref="methods/accounts#unblock" caption="POST /api/v1/accounts/:id/unblock" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/blocks_controller.rb" caption="app/controllers/api/v1/blocks_controller.rb" >}}
