---
title: 도메인 허용 API 메서드
description: 특정 도메인과의 연합을 허용합니다.
menu:
  docs:
    name: 도메인 허용
    parent: methods-admin
    identifier: methods-admin-domain_allows
aliases: [
	"/methods/admin/domain_allows",
	"/api/methods/admin/domain_allows",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

이 엔드포인트는 지정한 도메인만 이 서버와 연합하도록 허용하는 규칙을 생성합니다. [LIMITED_FEDERATION_MODE](../../admin/config#limited_federation_mode)가 활성화된 경우에만 적용됩니다. [도메인 차단](./domain_blocks) 기능의 반대이며 와일드카드 도메인 차단을 재정의하는 데 사용할 수 없습니다.

## 허용된 모든 도메인 조회 {#get}

```http
GET /api/v1/admin/domain_allows HTTP/1.1
```

허용된 모든 도메인 정보를 표시합니다.

**반환:** 배열: [Admin::DomainAllow]({{< relref "entities/Admin_DomainAllow" >}})\
**OAuth:** 사용자 토큰 + `admin:read:domain_allows`\
**권한:** 연합 관리\
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
: 정수. 반환할 최대 결과 수입니다. 기본값은 허용 100개이며 최대 200개입니다.

#### 응답 {#response}

##### 200: 성공 {#200-ok}

```json
[
	{
		"id": "2",
		"domain": "mastodon",
		"created_at": "2022-09-14T21:24:15.360Z"
	},
	{
		"id": "1",
		"domain": "mastodon.social",
		"created_at": "2022-09-14T21:23:02.755Z"
	}
]
```

DomainAllow ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <http://mastodon.example/api/v1/admin/domain_allows?limit=2&max_id=2>; rel="next", <http://mastodon.example/api/v1/admin/domain_allows?limit=2&since_id=1>; rel="prev"
```

##### 403: 금지됨 {#403-forbidden}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 허용된 도메인 하나 가져오기 {#get-one}

```http
GET /api/v1/admin/domain_allows/:id HTTP/1.1
```
허용된 도메인 하나의 정보를 표시합니다.

**반환:** [Admin::DomainAllow]({{< relref "entities/Admin_DomainAllow" >}})\
**OAuth:** 사용자 토큰 + `admin:read:domain_allows`\
**권한:** 연합 관리\
**버전 이력:**\
4.0.0 - 추가

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 DomainAllow ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

```json
{
	"id": "1",
	"domain": "mastodon.social",
	"created_at": "2022-09-14T21:23:02.755Z"
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

지정한 ID의 DomainAllow가 없습니다.

```json
{
	"error": "Record not found"
}
```

---

## 도메인과의 연합 허용 {#create}

```http
POST /api/v1/admin/domain_allows HTTP/1.1
```

서버가 허용 목록 연합 모드일 때 사용할 연합 허용 도메인 목록에 도메인을 추가합니다.

**반환:** [Admin::DomainAllow]({{< relref "entities/Admin_DomainAllow" >}})\
**OAuth:** 사용자 토큰 + `admin:write:domain_allows`\
**권한:** 연합 관리\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-1}

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

domain
: {{<required>}} 문자열. 연합을 허용할 도메인입니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

도메인과의 연합을 허용했거나 이미 허용된 상태입니다.

```json
{
	"id": "1",
	"domain": "mastodon.social",
	"created_at": "2022-09-14T21:23:02.755Z"
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

도메인 매개변수가 제공되지 않았거나 유효하지 않습니다.

```json
{
	"error": "Validation failed: Domain can't be blank"
}
```

---

## 허용된 도메인 삭제 {#delete}

```http
DELETE /api/v1/admin/domain_allows/:id HTTP/1.1
```

허용 도메인 목록에서 도메인을 삭제합니다.

**반환:** [Admin::DomainAllow]({{< relref "entities/Admin_DomainAllow" >}})\
**OAuth:** 사용자 토큰 + `admin:write:domain_allows`\
**권한:** 연합 관리\
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

허용 도메인 목록에서 도메인을 제거했습니다.

```json
{
	"id": "4",
	"domain": "*",
	"created_at": "2022-09-14T21:32:44.945Z"
}
```
##### 403: 금지됨 {#403-forbidden-3}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

지정한 ID의 DomainAllow가 없습니다.

```json
{
	"error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/domain_allows_controller.rb" caption="app/controllers/api/v1/admin/domain_allows_controller.rb" >}}