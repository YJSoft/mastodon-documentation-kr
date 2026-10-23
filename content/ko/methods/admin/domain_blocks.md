---
title: 관리자 도메인 차단 API 메서드
description: 특정 도메인과의 연합을 금지합니다.
menu:
  docs:
    name: 도메인 차단
    parent: methods-admin
    identifier: methods-admin-domain_blocks
aliases: [
	"/methods/admin/domain_blocks",
	"/api/methods/admin/domain_blocks",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

이 엔드포인트는 지정한 도메인이 이 서버와 연합하지 못하도록 규칙을 생성합니다. [LIMITED_FEDERATION_MODE](../../admin/config#limited_federation_mode)가 비활성화된 경우에만 적용됩니다. [도메인 허용](./domain_allows) 기능의 반대입니다.

## 차단된 모든 도메인 조회 {#get}

```http
GET /api/v1/admin/domain_blocks HTTP/1.1
```

차단된 모든 도메인 정보를 표시합니다.

**반환:** 배열: [Admin::DomainBlock]({{< relref "entities/Admin_DomainBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:read:domain_blocks`\
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
: 정수. 반환할 최대 결과 수입니다. 기본값은 차단 100개이며 최대 200개입니다.

#### 응답 {#response}

##### 200: 성공 {#200-ok}

```json
[
  {
    "id": "1",
    "domain": "example.com",
    "digest": "a379a6f6eeafb9a55e378c118034e2751e682fab9f2d30ab13d2125586ce1947",
    "created_at": "2022-11-16T08:15:34.238Z",
    "severity": "noop",
    "reject_media": false,
    "reject_reports": false,
    "private_comment": null,
    "public_comment": null,
    "obfuscate": false
  },
  // ...
]
```

DomainBlock ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <http://mastodon.example/api/v1/admin/domain_blocks?limit=2&max_id=2>; rel="next", <http://mastodon.example/api/v1/admin/domain_blocks?limit=2&since_id=1>; rel="prev"
```

##### 403: 금지됨 {#403-forbidden}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 차단된 도메인 하나 가져오기 {#get-one}

```http
GET /api/v1/admin/domain_blocks/:id HTTP/1.1
```
차단된 도메인 하나의 정보를 표시합니다.

**반환:** [Admin::DomainBlock]({{< relref "entities/Admin_DomainBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:read:domain_blocks`\
**권한:** 연합 관리\
**버전 이력:**\
4.0.0 - 추가

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
  "domain": "example.com",
  "digest": "a379a6f6eeafb9a55e378c118034e2751e682fab9f2d30ab13d2125586ce1947",
  "created_at": "2022-11-16T08:15:34.238Z",
  "severity": "noop",
  "reject_media": false,
  "reject_reports": false,
  "private_comment": null,
  "public_comment": null,
  "obfuscate": false
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

지정한 ID의 DomainBlock이 없습니다.

```json
{
  "error": "Record not found"
}
```

---

## 도메인과의 연합 차단 {#create}

```http
POST /api/v1/admin/domain_blocks HTTP/1.1
```

연합 차단 도메인 목록에 도메인을 추가합니다.

**반환:** [Admin::DomainBlock]({{< relref "entities/Admin_DomainBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:write:domain_blocks`\
**권한:** 연합 관리\
**버전 이력:**\
4.0.0 - 추가

#### 요청 {#request-1}

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

domain
: {{<required>}} 문자열. 연합을 차단할 도메인입니다.

severity
: 문자열. 도메인에 `silence`, `suspend`, `noop` 중 어떤 조치를 적용할지 결정합니다. 기본값은 `silence`입니다.

reject_media
: 불리언. 미디어 첨부 파일을 거부할지 여부입니다. 기본값은 false입니다.

reject_reports
: 불리언. 이 도메인의 신고를 거부할지 여부입니다. 기본값은 false입니다.

private_comment
: 문자열. 관리자만 볼 수 있는 이 도메인 차단에 대한 비공개 메모입니다.

public_comment
: 문자열. 정보 페이지에 선택적으로 표시하는 이 도메인 차단에 대한 공개 메모입니다.

obfuscate
: 불리언. 공개 표시할 때 도메인을 일부 가릴지 여부입니다. 기본값은 false입니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

도메인과의 연합을 차단했습니다.

```json
{
  "id": "1",
  "domain": "example.com",
  "digest": "a379a6f6eeafb9a55e378c118034e2751e682fab9f2d30ab13d2125586ce1947",
  "created_at": "2022-11-16T08:15:34.238Z",
  "severity": "noop",
  "reject_media": false,
  "reject_reports": false,
  "private_comment": null,
  "public_comment": null,
  "obfuscate": false
}
```

##### 403: 금지됨 {#403-forbidden-2}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 422: 처리할 수 없는 엔터티 - 매개변수 누락 {#422-unprocessable-entity---missing-parameter}

도메인 매개변수가 제공되지 않았습니다.

```json
{
  "error": "Validation failed: Domain can't be blank"
}
```

##### 422: 처리할 수 없는 엔터티 - 기존 도메인 차단 {#422-unprocessable-entity---existing-domain-block}

기존 도메인 차단이 이미 이 도메인 매개변수에 적용됩니다.

```json
{
  "error": "You have already imposed stricter limits on example.com.",
  "existing_domain_block": {
    "id": "1",
    "domain": "example.com",
    "digest": "a379a6f6eeafb9a55e378c118034e2751e682fab9f2d30ab13d2125586ce1947",
    "created_at": "2022-11-16T08:15:34.238Z",
    "severity": "noop",
    "reject_media": false,
    "reject_reports": false,
    "private_comment": null,
    "public_comment": null,
    "obfuscate": false
  }
}
```

---

## 도메인 차단 수정 {#update}

```http
PUT /api/v1/admin/domain_blocks/:id HTTP/1.1
```

기존 도메인 차단의 매개변수를 변경합니다.

**반환:** [Admin::DomainBlock]({{< relref "entities/Admin_DomainBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:write:domain_blocks`\
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

##### 폼 데이터 매개변수 {#form-data-parameters-1}

severity
: 문자열. 도메인에 `silence`, `suspend`, `noop` 중 어떤 조치를 적용할지 결정합니다. 기본값은 `silence`입니다.

reject_media
: 불리언. 미디어 첨부 파일을 거부할지 여부입니다. 기본값은 false입니다.

reject_reports
: 불리언. 이 도메인의 신고를 거부할지 여부입니다. 기본값은 false입니다.

private_comment
: 문자열. 관리자만 볼 수 있는 이 도메인 차단에 대한 비공개 메모입니다.

public_comment
: 문자열. 정보 페이지에 선택적으로 표시하는 이 도메인 차단에 대한 공개 메모입니다.

obfuscate
: 불리언. 공개 표시할 때 도메인을 일부 가릴지 여부입니다. 기본값은 false입니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

도메인 차단을 수정했습니다.

```json
{
  "id": "1",
  "domain": "example.com",
  "digest": "a379a6f6eeafb9a55e378c118034e2751e682fab9f2d30ab13d2125586ce1947",
  "created_at": "2022-11-16T08:15:34.238Z",
  "severity": "noop",
  "reject_media": false,
  "reject_reports": false,
  "private_comment": null,
  "public_comment": null,
  "obfuscate": false
}
```

##### 403: 금지됨 {#403-forbidden-3}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

severity 매개변수를 제공했지만 허용된 값이 아닌 경우 요청이 실패합니다.

```json
{
  "error": "Validation failed: Severity is not included in the list"
}
```

---

## 도메인 차단 제거 {#delete}

```http
DELETE /api/v1/admin/domain_blocks/:id HTTP/1.1
```

도메인에 대한 차단을 해제합니다.

**반환:** [Admin::DomainBlock]({{< relref "entities/Admin_DomainBlock" >}})\
**OAuth:** 사용자 토큰 + `admin:write:domain_blocks`\
**권한:** 연합 관리\
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

차단 목록에서 도메인을 제거했습니다.

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

지정한 ID의 DomainBlock이 없습니다.

```json
{
  "error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/domain_blocks_controller.rb" caption="app/controllers/api/v1/admin/domain_blocks_controller.rb" >}}
