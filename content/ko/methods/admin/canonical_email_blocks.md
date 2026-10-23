---
title: 정규화 이메일 차단 API 메서드
description: 이메일 주소의 해시로 특정 주소를 차단합니다.
menu:
  docs:
    name: 정규화 이메일 차단
    parent: methods-admin
    identifier: methods-admin-canonical_email_blocks
aliases: [
  "/methods/admin/canonical_email_blocks",
  "/api/methods/admin/canonical_email_blocks",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 모든 정규화 이메일 차단 목록 조회 {#get}

```http
GET /api/v1/admin/canonical_email_blocks HTTP/1.1
```

**반환:** 배열: [Admin::CanonicalEmailBlock]({{< relref "entities/Admin_CanonicalEmailBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:read:canonical_email_blocks`\
**권한:** 차단 관리\
**버전 이력:**\
4.0.0 - 추가

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
: 정수. 반환할 최대 결과 수입니다. 기본값은 차단 100개이며 최대 200개입니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

```json
[
  {
    "id": "1",
    "canonical_email_hash": "b344e55d11b3fc25d0d53194e0475838bf17e9be67ce3e6469956222d9a34f9c"
  },
  // ...
]
```

CanonicalEmailBlock ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <http://mastodon.example/api/v1/admin/canonical_email_blocks?limit=2&max_id=2>; rel="next", <http://mastodon.example/api/v1/admin/canonical_email_blocks?limit=2&since_id=1>; rel="prev"
```

##### 403: 금지됨 {#403-forbidden}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 정규화 이메일 차단 하나 조회 {#get-one}

```http
GET /api/v1/admin/canonical_email_blocks/:id HTTP/1.1
```

**반환:** [Admin::CanonicalEmailBlock]({{< relref "entities/Admin_CanonicalEmailBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:read:canonical_email_blocks`\
**권한:** 차단 관리\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 Admin::CanonicalEmailBlock ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

```json
{
  "id": "1",
  "canonical_email_hash": "b344e55d11b3fc25d0d53194e0475838bf17e9be67ce3e6469956222d9a34f9c"
}
```

##### 403: 금지됨 {#403-forbidden-1}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found}

정규화 이메일 차단이 없거나 이미 삭제되었습니다.

```json
{
  "error": "Record not found"
}
```

---

## 테스트 {#test}

```http
POST /api/v1/admin/canonical_email_blocks/test HTTP/1.1
```

이메일 주소를 정규화하고 해시합니다.

**반환:** 배열: [Admin::CanonicalEmailBlock]({{< relref "entities/Admin_CanonicalEmailBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:read:canonical_email_blocks`\
**권한:** 차단 관리\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-2}

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

email
: {{<required>}} 문자열. 정규화하고 해시할 이메일입니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

일치하는 모든 정규화 이메일 차단이 반환됩니다.

```json
[
  {
    "id": "1",
    "canonical_email_hash": "b344e55d11b3fc25d0d53194e0475838bf17e9be67ce3e6469956222d9a34f9c"
  }
]
```

##### 403: 금지됨 {#403-forbidden-2}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 500: 서버 오류 {#500-server-error}
<!-- TODO: remove when https://github.com/mastodon/mastodon/issues/21774 is fixed -->
이메일이 제공되지 않았습니다.

---

## 정규화 이메일 차단 {#create}

```http
POST /api/v1/admin/canonical_email_blocks HTTP/1.1
```

**반환:** [Admin::CanonicalEmailBlock]({{< relref "entities/Admin_CanonicalEmailBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:write:canonical_email_blocks`\
**권한:** 차단 관리\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-3}

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-1}

email
: {{<required>}} 문자열. 정규화하고 해시하여 차단할 이메일입니다. 이 매개변수를 제공하면 `canonical_email_hash`를 무시합니다.

canonical_email_hash
: 문자열. 대조할 해시입니다. `email`을 제공하지 않으면 이 매개변수가 필수입니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

정규화 이메일을 차단했습니다.

```json
{
  "id": "1",
  "canonical_email_hash": "b344e55d11b3fc25d0d53194e0475838bf17e9be67ce3e6469956222d9a34f9c"
}
```

##### 403: 금지됨 {#403-forbidden-3}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

정규화 이메일 해시는 이미 차단되어 있습니다.

```json
{
  "error":"Validation failed: Canonical email hash has already been taken"
}
```

---

## 정규화 이메일 차단 삭제 {#delete}

```http
DELETE /api/v1/admin/canonical_email_blocks/:id HTTP/1.1
```

**반환:** [Admin::CanonicalEmailBlock]({{< relref "entities/Admin_CanonicalEmailBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:write:canonical_email_blocks`\
**권한:** 차단 관리\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-4}

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 데이터베이스의 Admin::CanonicalEmailBlock ID입니다.

##### 헤더 {#headers-4}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-4}
##### 200: 성공 {#200-ok-4}

정규화 이메일 차단을 삭제했습니다.

```json
{}
```

##### 403: 금지됨 {#403-forbidden-4}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

정규화 이메일 차단이 없거나 이미 삭제되었습니다.

```json
{
  "error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/canonical_email_blocks_controller.rb" caption="app/controllers/api/v1/admin/canonical_email_blocks_controller.rb" >}}