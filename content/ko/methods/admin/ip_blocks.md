---
title: IP 차단 API 메서드
description: 특정 IP 주소 범위의 가입을 금지합니다.
menu:
  docs:
    name: IP 차단
    parent: methods-admin
    identifier: methods-admin-ip_blocks
aliases: [
	"/methods/admin/ip_blocks",
	"/api/methods/admin/ip_blocks",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 모든 IP 차단 조회 {#get}

```http
GET /api/v1/admin/ip_blocks HTTP/1.1
```

차단된 모든 IP 범위의 정보를 표시합니다.

**반환:** 배열: [Admin::IpBlock]({{< relref "entities/Admin_IpBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:read:ip_blocks`\
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
    "ip": "8.8.8.8/32",
    "severity": "no_access",
    "comment": "",
    "created_at": "2022-11-16T07:22:00.501Z",
    "expires_at": null
  },
  // ...
]
```

IpBlock ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <http://mastodon.example/api/v1/admin/ip_blocks?limit=2&max_id=2>; rel="next", <http://mastodon.example/api/v1/admin/ip_blocks?limit=2&since_id=1>; rel="prev"
```

##### 403: 금지됨 {#403-forbidden}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## IP 차단 하나 가져오기 {#get-one}

```http
GET /api/v1/admin/ip_blocks/:id HTTP/1.1
```

IP 차단 하나의 정보를 표시합니다.

**반환:** [Admin::IpBlock]({{< relref "entities/Admin_IpBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:read:ip_blocks`\
**권한:** 차단 관리\
**버전 이력:**\
4.0.0 - 추가

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 IpBlock ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

```json
{
  "id": "1",
  "ip": "8.8.8.8/32",
  "severity": "no_access",
  "comment": "",
  "created_at": "2022-11-16T07:22:00.501Z",
  "expires_at": null
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

지정한 ID의 IpBlock이 없습니다.

```json
{
	"error": "Record not found"
}
```

---

## IP 주소 범위의 가입 차단 {#create}

```http
POST /api/v1/admin/ip_blocks HTTP/1.1
```

IP 차단 목록에 IP 주소 범위를 추가합니다.

**반환:** [Admin::IpBlock]({{< relref "entities/Admin_IpBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:write:ip_blocks`\
**권한:** 차단 관리\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-1}

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

ip
: 문자열. 차단할 IP 주소와 접두사입니다. 기본값은 `0.0.0.0/32`입니다.

severity
: {{<required>}} 문자열. 이 IP 범위에 적용할 정책입니다: `sign_up_requires_approval`, `sign_up_block`, `no_access`.

comment
: 문자열. 이 IP 차단의 사유입니다.

expires_in
: 정수. 이 IP 차단이 만료될 때까지의 초 단위 시간입니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

IP의 가입을 차단했습니다.

```json
{
  "id": "1",
  "ip": "8.8.8.8/32",
  "severity": "no_access",
  "comment": "",
  "created_at": "2022-11-16T07:22:00.501Z",
  "expires_at": null
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

IP가 이미 차단되었거나 심각도가 제공되지 않았습니다.

```json
{
  "error": "Validation failed: Severity can't be blank, Ip has already been taken"
}
```

---

## 도메인 차단 수정 {#update}

```http
PUT /api/v1/admin/ip_blocks/:id HTTP/1.1
```

기존 IP 차단의 매개변수를 변경합니다.

**반환:** [Admin::IpBlock]({{< relref "entities/Admin_IpBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:write:ip_blocks`\
**권한:** 차단 관리\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-2}

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 데이터베이스의 IpBlock ID입니다.

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-1}

ip
: 문자열. 차단할 IP 주소와 접두사입니다. 기본값은 `0.0.0.0/32`입니다.

severity
: 문자열. 이 IP 범위에 적용할 정책입니다: `sign_up_requires_approval`, `sign_up_block`, `no_access`.

comment
: 문자열. 이 IP 차단의 사유입니다.

expires_in
: 정수. 이 IP 차단이 만료될 때까지의 초 단위 시간입니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

IP 차단을 수정했습니다.

```json
{
  "id": "1",
  "ip": "8.8.4.4/32",
  "severity": "no_access",
  "comment": "",
  "created_at": "2022-11-16T07:22:00.501Z",
  "expires_at": null
}
```

##### 403: 금지됨 {#403-forbidden-3}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## IP 차단 삭제 {#delete}

```http
DELETE /api/v1/admin/ip_blocks/:id HTTP/1.1
```

IP 범위의 차단을 해제합니다.

**반환:** [Admin::IpBlock]({{< relref "entities/Admin_IpBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:write:domain_blocks`\
**권한:** 차단 관리\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-3}

##### 경로 매개변수 {#path-parameters-2}

:id
: {{<required>}} 문자열. 데이터베이스의 DomainAllow ID입니다.

##### 헤더 {#headers-4}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-4}
##### 200: 성공 {#200-ok-4}

차단 목록에서 IP를 제거했습니다.

```json
{}
```
##### 403: 금지됨 {#403-forbidden-4}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

지정한 ID의 IpBlock이 없습니다.

```json
{
	"error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/ip_blocks_controller.rb" caption="app/controllers/api/v1/admin/ip_blocks_controller.rb" >}}