---
title: 리스트 API 메서드
description: >-
  리스트를 조회하고 관리합니다. 리스트 타임라인을 가져오려면 /api/v1/timelines/list/id도 참고하세요.
menu:
  docs:
    name: 리스트
    parent: methods-timelines
    identifier: methods-lists
aliases: [
  "/methods/lists",
  "/api/methods/lists",
  "/methods/timelines/lists",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 내 리스트 조회 {#get}

```http
GET /api/v1/lists HTTP/1.1
```

사용자가 소유한 모든 리스트를 가져옵니다.

**반환:** 배열: [List]({{< relref "entities/list" >}})\
**OAuth:** 사용자 토큰 + `read:lists`\
**버전 이력:**\
2.1.0 - 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

관련 API 호출의 매개변수로 `id`를 사용하세요.

```json
[
  {
    "id": "12249",
    "title": "Friends",
    "replies_policy": "followed",
    "exclusive": false
  },
  {
    "id": "13585",
    "title": "test",
    "replies_policy": "list",
    "exclusive": true
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

## 리스트 하나 표시 {#get-one}

```http
GET /api/v1/lists/:id HTTP/1.1
```

지정한 ID의 리스트를 가져옵니다.

**반환:** [List]({{< relref "entities/list" >}})\
**OAuth:** 사용자 토큰 + `read:lists`\
**버전 이력:**\
2.1.0 - 추가

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 리스트 ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

리스트 12249가 존재하며 내 소유입니다.

```json
{
  "id": "12249",
  "title": "Friends",
  "replies_policy": "followed",
  "exclusive": false
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

리스트가 없거나 내 소유가 아닙니다.

```json
{
  "error": "Record not found"
}
```

---

## 리스트 생성 {#create}

```http
POST /api/v1/lists HTTP/1.1
```

새 리스트를 생성합니다.

**반환:** [List]({{< relref "entities/list" >}})\
**OAuth:** 사용자 토큰 + `write:lists`\
**버전 이력:**\
2.1.0 - 추가\
3.3.0 - `replies_policy` 추가\
4.2.0 - `exclusive` 추가

#### 요청 {#request-2}
##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

title
: {{<required>}} 문자열. 생성할 리스트의 제목입니다.

replies_policy
: 문자열. `followed`, `list`, `none` 중 하나입니다. 기본값은 `list`입니다.

exclusive
: 불리언. 이 리스트의 구성원을 “홈” 피드에서 제거할지 여부입니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

`title`이 "test"인 예시 리스트를 생성했습니다.

```json
{
  "id": "13585",
  "title": "test",
  "replies_policy": "list",
  "exclusive": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-2}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

`title`이 없는 경우:

```json
{
  "error": "Validation failed: Title can't be blank"
}
```

`replies_policy`를 인식할 수 없는 경우:

```json
{
  "error": "'some' is not a valid replies_policy"
}
```
-->

---

## 리스트 수정 {#update}

```http
PUT /api/v1/lists/:id HTTP/1.1
```

리스트의 속성을 변경합니다.

**반환:** [List]({{< relref "entities/list" >}})\
**OAuth:** 사용자 토큰 + `write:lists`\
**버전 이력:**\
2.1.0 - 추가\
3.3.0 - `replies_policy` 추가
4.2.0 - `exclusive` 추가

#### 요청 {#request-3}

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 리스트 ID입니다.

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-1}

title
: {{<required>}} 문자열. 생성할 리스트의 제목입니다.

replies_policy
: 문자열. `followed`, `list`, `none` 중 하나입니다. 기본값은 `list`입니다.

exclusive
: 불리언. 이 리스트의 구성원을 “홈” 피드에서 제거할지 여부입니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

리스트 13585의 `title`을 "testing"으로 수정했습니다.

```json
{
  "id": "13585",
  "title": "test",
  "replies_policy": "list",
  "exclusive": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-3}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-1}

`title`이 없는 경우:

```json
{
  "error": "Validation failed: Title can't be blank"
}
```

`replies_policy`를 인식할 수 없는 경우:

```json
{
  "error": "'some' is not a valid replies_policy"
}
```

---

## 리스트 삭제 {#delete}

```http
DELETE /api/v1/lists/:id HTTP/1.1
```

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:lists`\
**버전 이력:**\
2.1.0 - 추가

#### 요청 {#request-4}

##### 경로 매개변수 {#path-parameters-2}

:id
: {{<required>}} 문자열. 리스트 ID입니다.

##### 헤더 {#headers-4}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-4}
##### 200: 성공 {#200-ok-4}

리스트를 삭제했습니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-4}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

리스트가 없거나 내 소유가 아닙니다.


```json
{
  "error": "Record not found"
}
```

---

## 리스트의 계정 조회 {#accounts}

```http
GET /api/v1/lists/:id/accounts HTTP/1.1
```

**반환:** 배열: [Account]({{< relref "entities/account" >}})\
**OAuth:** 사용자 토큰 + `read:lists`\
**버전 이력:**\
2.1.0 - 추가\
3.3.0 - 이제 `min_id`와 `max_id` 동시 사용 가능

#### 요청 {#request-5}

##### 경로 매개변수 {#path-parameters-3}

:id
: {{<required>}} 문자열. 리스트 ID입니다.

##### 헤더 {#headers-5}

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
: 정수. 최대 결과 수입니다. 기본값은 계정 40개이며 최대 80개입니다. 페이지네이션 없이 모든 계정을 가져오려면 0으로 설정하세요.

#### 응답 {#response-5}
##### 200: 성공 {#200-ok-5}

```json
[
  {
    "id": "952529",
    "username": "alayna",
    "acct": "alayna@desvox.es",
    // ...
  },
  {
    "id": "917388",
    "username": "cole",
    "acct": "cole@be.cutewith.me",
    // ...
  },
  {
    "id": "869022",
    "username": "alayna",
    "acct": "alayna@be.cutewith.me",
    // ...
  },
  {
    "id": "832844",
    "username": "a9",
    "acct": "a9@broadcast.wolfgirl.engineering",
    // ...
  },
  {
    "id": "482403",
    "username": "amic",
    "acct": "amic@nulled.red",
    // ...
  }
]
```

리스트에 어떤 Account가 포함되어 있는지 미리 알 수 없으므로 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <https://mastodon.example/api/v1/lists/12249/accounts?max_id=106931203247163945>; rel="next", <https://mastodon.example/api/v1/lists/12249/accounts?since_id=108632085572655915>; rel="prev"
```

##### 401: 인증되지 않음 {#401-unauthorized-5}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-2}

리스트가 없거나 내 소유가 아닙니다.


```json
{
  "error": "Record not found"
}
```

---

## 리스트에 계정 추가 {#accounts-add}

```http
POST /api/v1/lists/:id/accounts HTTP/1.1
```

지정한 리스트에 계정을 추가합니다. 사용자는 이 계정을 팔로우하고 있어야 합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:lists`\
**버전 이력:**\
2.1.0 - 추가

### 요청 {#request-6}

##### 경로 매개변수 {#path-parameters-4}

:id
: {{<required>}} 문자열. 리스트 ID입니다.

##### 헤더 {#headers-6}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-2}

account_ids[]
: {{<required>}} 문자열 배열. 리스트에 추가할 계정입니다.

#### 응답 {#response-6}
##### 200: 성공 {#200-ok-6}

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-6}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-3}

지정한 ID의 계정을 팔로우하지 않거나, 해당 ID의 리스트를 소유하지 않거나, 리스트/계정 ID가 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity-2}

제공한 ID 중 하나의 Account가 이미 리스트에 포함되어 있습니다.

```json
{
  "error": "Validation failed: Account has already been taken"
}
```

---

## 리스트에서 계정 제거 {#accounts-remove}

```http
DELETE /api/v1/lists/:id/accounts HTTP/1.1
```

지정한 리스트에서 계정을 제거합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:lists`\
**버전 이력:**\
2.1.0 - 추가

#### 요청 {#request-7}

##### 경로 매개변수 {#path-parameters-5}

:id
: {{<required>}} 문자열. 리스트 ID입니다.

##### 헤더 {#headers-7}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-3}

account_ids[]
: {{<required>}} 문자열 배열. 리스트에서 제거할 계정입니다.

#### 응답 {#response-7}
##### 200: 성공 {#200-ok-7}

리스트에서 Account를 제거했거나 이미 리스트에 없었습니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-7}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-4}

리스트가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/accounts#lists" caption="GET /api/v1/accounts/:id/lists" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/lists_controller.rb" caption="app/controllers/api/v1/lists_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/lists/accounts_controller.rb" caption="app/controllers/api/v1/lists/accounts_controller.rb" >}}
