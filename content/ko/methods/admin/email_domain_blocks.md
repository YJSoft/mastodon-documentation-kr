---
title: 이메일 도메인 차단 API 메서드
description: 특정 이메일 도메인의 가입을 금지합니다.
menu:
  docs:
    name: 이메일 도메인 차단
    parent: methods-admin
    identifier: methods-admin-email_domain_blocks
aliases: [
	"/methods/admin/email_domain_blocks",
	"/api/methods/admin/email_domain_blocks",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 차단된 모든 이메일 도메인 조회 {#get}

```http
GET /api/v1/admin/email_domain_blocks HTTP/1.1
```

가입이 차단된 모든 이메일 도메인의 정보를 표시합니다.

**반환:** 배열: [Admin::EmailDomainBlock]({{< relref "entities/Admin_EmailDomainBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:read:email_domain_blocks`\
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
    "domain": "foo",
    "created_at": "2022-11-16T06:09:36.176Z",
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
        "accounts": "0",
        "uses": "0"
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
    ]
  },
  // ...
]
```

##### 403: 금지됨 {#403-forbidden}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 차단된 이메일 도메인 하나 가져오기 {#get-one}

```http
GET /api/v1/admin/email_domain_blocks/:id HTTP/1.1
```
가입이 차단된 이메일 도메인 하나의 정보를 표시합니다.

**반환:** [Admin::EmailDomainBlock]({{< relref "entities/Admin_EmailDomainBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:read:email_domain_blocks`\
**권한:** 차단 관리\
**버전 이력:**\
4.1.0 - 추가

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 DomainBlock ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

```json
{
  "id": "1",
  "domain": "foo",
  "created_at": "2022-11-16T06:09:36.176Z",
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
      "accounts": "0",
      "uses": "0"
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
  ]
}
```

##### 403: 금지됨 {#403-forbidden-1}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found}

지정한 ID의 EmailDomainBlock이 없습니다.

```json
{
	"error": "Record not found"
}
```

---

## 이메일 도메인의 가입 차단 {#create}

```http
POST /api/v1/admin/email_domain_blocks HTTP/1.1
```

가입 차단 이메일 도메인 목록에 도메인을 추가합니다.

**반환:** [Admin::EmailDomainBlock]({{< relref "entities/Admin_EmailDomainBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:write:email_domain_blocks`\
**권한:** 차단 관리\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-1}

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

domain
: {{<required>}} 문자열. 연합을 차단할 도메인입니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

이메일 도메인의 가입을 차단했습니다.

```json
{
  "id": "1",
  "domain": "foo",
  "created_at": "2022-11-16T06:09:36.176Z",
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
      "accounts": "0",
      "uses": "0"
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
  ]
}
```

##### 403: 금지됨 {#403-forbidden-2}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

도메인 매개변수가 제공되지 않았습니다.

```json
{
	"error": "Validation failed: Domain can't be blank"
}
```

또는 제공한 도메인에 유효하지 않은 문자가 포함되어 있습니다.

```json
{
  "error": "Validation failed: Domain is invalid, Domain is not a valid domain name"
}
```

---

## 이메일 도메인 차단 삭제 {#delete}

```http
DELETE /api/v1/admin/email_domain_blocks/:id HTTP/1.1
```

이메일 도메인 차단을 해제합니다.

**반환:** [Admin::EmailDomainBlock]({{< relref "entities/Admin_EmailDomainBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:write:email_domain_blocks`\
**권한:** 차단 관리\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-2}

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 데이터베이스의 DomainAllow ID입니다.

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

차단 목록에서 이메일 도메인을 제거했습니다.

```json
{}
```
##### 403: 금지됨 {#403-forbidden-3}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

지정한 ID의 EmailDomainBlock이 없습니다.

```json
{
	"error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/email_domain_blocks_controller.rb" caption="app/controllers/api/v1/admin/email_domain_blocks_controller.rb" >}}