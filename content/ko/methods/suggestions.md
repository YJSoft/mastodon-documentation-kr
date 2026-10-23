---
title: 팔로우 추천 API 메서드
description: >-
  이전의 긍정적인 상호작용을 바탕으로 서버가 생성한 팔로우 추천입니다.
menu:
  docs:
    name: 팔로우 추천
    parent: methods-accounts
    identifier: methods-suggestions
aliases: [
  "/methods/suggestions",
  "/api/methods/suggestions",
  "/methods/accounts/suggestions",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 팔로우 추천 조회(v2) {#v2}

```http
GET /api/v2/suggestions HTTP/1.1
```

운영진이 추천하거나 사용자가 과거에 긍정적으로 상호작용했지만 아직 팔로우하지 않은 계정입니다.

**반환:** 배열: [Suggestion]({{< relref "entities/Suggestion" >}})\
**OAuth:** 사용자 토큰 + `read`\
**버전 이력:**\
3.4.0 - 추가

#### 요청 {#request}
##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters}

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 계정 40개이며 최대 80개입니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

```json
[
  {
    "source": "past_interactions",
    "account": {
      "id": "784058",
      "username": "katie",
      "acct": "katie@pleroma.voidlurker.net"
      // ...
    }
  },
  // ...
  {
    "source": "global",
    "account": {
      "id": "108194863260762493",
      "username": "thunderbird",
      "acct": "thunderbird@mastodon.online"
      // ...
    }
  }
]
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 추천 제거 {#remove}

```http
DELETE /api/v1/suggestions/:account_id HTTP/1.1
```

팔로우 추천에서 계정을 제거합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `read`\
**버전 이력:**\
2.4.3 - 추가

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:account_id
: {{<required>}} 문자열. 데이터베이스의 Account ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

호출이 성공하면 빈 객체를 반환합니다. 제공한 계정 id가 유효하지 않거나 추천 계정이 아니어도 호출은 성공합니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-1}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 팔로우 추천 조회(v1) {{%deprecated%}} {#v1}

```http
GET /api/v1/suggestions HTTP/1.1
```

사용자가 과거에 긍정적으로 상호작용했지만 아직 팔로우하지 않은 계정입니다.

**반환:** 배열: [Account]({{< relref "entities/Account" >}})\
**OAuth:** 사용자 토큰 + `read`\
**버전 이력:**\
2.4.3 - 추가\
3.4.0 - 사용 중단 예정

#### 요청 {#request-2}
##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-1}

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 계정 40개이며 최대 80개입니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

```json
[
  {
    "id": "332766",
    "username": "kaniini",
    "acct": "kaniini@pleroma.site",
    // ...
  },
  {
    "id": "689455",
    "username": "interneteh",
    "acct": "interneteh@sunbeam.city",
    // ...
  },
  {
    "id": "764276",
    "username": "Dee",
    "acct": "Dee@fedi.underscore.world",
    // ...
  },
  // ...
]
```

##### 401: 인증되지 않음 {#401-unauthorized-2}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/accounts#follow" caption="POST /api/v1/accounts/:id/follow" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v2/suggestions_controller.rb" caption="app/controllers/api/v2/suggestions_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/suggestions_controller.rb" caption="app/controllers/api/v1/suggestions_controller.rb" >}}

