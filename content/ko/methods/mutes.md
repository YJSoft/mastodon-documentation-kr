---
title: 뮤트 API 메서드
description: 뮤트 목록을 확인합니다. accounts/:id/{mute,unmute}도 참고하세요.
menu:
  docs:
    name: 뮤트
    parent: methods-accounts
    identifier: methods-mutes
aliases: [
  "/methods/mutes",
  "/api/methods/mutes",
  "/methods/accounts/mutes",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 뮤트한 계정 조회 {#get}

```http
GET /api/v1/mutes HTTP/1.1
```

사용자가 뮤트한 계정입니다.

**반환:** 배열: [MutedAccount]({{<relref "entities/Account#MutedAccount">}})\
**OAuth:** 사용자 토큰 + `read:mutes` 또는 `follow`\
**버전 이력:**\
0.0.0 - 추가\
3.3.0 - `mute_expires_at` 추가

#### 요청 {#request}
##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters}

max_id 
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

since_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 계정 40개이며 최대 80개입니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

limit=2인 응답 예입니다.

```json
[
  {
    "id": "963076",
    "username": "Simia91",
    "acct": "Simia91",
    "display_name": "",
    // ...
  },
  {
    "id": "1001524",
    "username": "hakogamae",
    "acct": "hakogamae",
    "display_name": "Hakogamae 🔞",
    // ...
  }
]
```

Mute ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/mutes?limit=2&max_id=317646>; rel="next", <https://mastodon.example/api/v1/mutes?limit=2&since_id=317647>; rel="prev"
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

{{< page-relref ref="methods/accounts#mute" caption="POST /api/v1/accounts/:id/mute" >}}

{{< page-relref ref="methods/accounts#unmute" caption="POST /api/v1/accounts/:id/unmute" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/mutes_controller.rb" caption="app/controllers/api/v1/mutes_controller.rb" >}}
