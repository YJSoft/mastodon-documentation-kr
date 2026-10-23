---
title: 팔로우 요청 API 메서드
description: 팔로우 요청을 확인하고 관리합니다.
menu:
  docs:
    name: 팔로우 요청
    parent: methods-accounts
    identifier: methods-follow_requests
aliases: [
  "/methods/follow_requests",
  "/api/methods/follow_requests",
  "/methods/accounts/follow_requests",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 대기 중인 팔로우 요청 조회 {#get}

```http
GET /api/v1/follow_requests HTTP/1.1
```

**반환:** 배열: [Account]({{< relref "entities/account" >}})\
**OAuth:** 사용자 토큰 + `read:follows` 또는 `follow`\
**버전 이력:**\
0.0.0 - 추가

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

팔로우를 요청하는 Account를 limit=2로 가져오는 호출 예입니다.

```json
[
  {
    "id":"108119793981152178",
    "username":"spcpro3022",
    "acct":"spcpro3022@shitposter.club",
    "display_name":"spcpro3022",
    // ...
  },
  {
    "id":"106780475844882270",
    "username":"EricStoner",
    "acct":"EricStoner@freeatlantis.com",
    "display_name":"EricStoner",
    // ...
  }
]
```

FollowRequest ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/follow_requests?limit=2&max_id=7163058>; rel="next", <https://mastodon.example/api/v1/follow_requests?limit=2&since_id=7275607>; rel="prev"
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 팔로우 요청 수락 {#accept}

```http
POST /api/v1/follow_requests/:account_id/authorize HTTP/1.1
```

**반환:** [Relationship]({{< relref "entities/relationship" >}})\
**OAuth:** 사용자 토큰 + `write:follows` 또는 `follow`\
**버전 이력:**\
0.0.0 - 추가\
3.0.0 - 아무것도 반환하지 않는 대신 Relationship 반환

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:account_id
: {{<required>}} 문자열. 데이터베이스의 Account ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

이 계정과의 Relationship이 수정되어 해당 계정이 나를 `followed_by`하는 상태가 됩니다.

```json
{
  "id": "8889777",
  "following": false,
  "showing_reblogs": false,
  "followed_by": true,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-1}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found}

해당 계정 ID의 대기 중인 팔로우 요청이 없습니다.

```json
{
  "error": "Record not found"
}
```

---

## 팔로우 요청 거절 {#reject}

```http
POST /api/v1/follow_requests/:account_id/reject HTTP/1.1
```

**반환:** [Relationship]({{< relref "entities/relationship" >}})\
**OAuth:** 사용자 토큰 + `write:follows` 또는 `follow`\
**버전 이력:**\
0.0.0 - 추가\
3.0.0 - 아무것도 반환하지 않는 대신 Relationship 반환

#### 요청 {#request-2}

##### 경로 매개변수 {#path-parameters-1}

:account_id
: {{<required>}} 문자열. 데이터베이스의 Account ID입니다.

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

이 계정과의 Relationship은 바뀌지 않습니다.

```json
{
  "id": "8889777",
  "following": false,
  "showing_reblogs": false,
  "followed_by": true,
  "blocking": false,
  "blocked_by": false,
  "muting": false,
  "muting_notifications": false,
  "requested": false,
  "domain_blocking": false,
  "endorsed": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-2}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

해당 계정 ID의 대기 중인 팔로우 요청이 없습니다.

```json
{
  "error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/follow_requests_controller.rb" caption="app/controllers/api/v1/follow_requests_controller.rb" >}}
