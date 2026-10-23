---
title: 관리자 신고 API 메서드
description: 신고에 대한 중재 조치를 수행합니다.
menu:
  docs:
    name: 신고
    parent: methods-admin
    identifier: methods-admin-reports
aliases: [
  "/methods/admin/reports",
  "/api/methods/admin/reports",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 모든 신고 조회 {#get}

```http
GET /api/v1/admin/reports HTTP/1.1
```

모든 신고 정보를 조회합니다.

**반환:** 배열: [Admin::Report]({{< relref "entities/Admin_Report" >}})\
**OAuth:** 사용자 토큰 + `admin:read:reports`\
**권한:** 신고 관리\
**버전 이력:**\
2.9.1 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - `unresolved` 매개변수 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters}

resolved
: 불리언. 해결된 신고로 필터링할지 여부입니다.

unresolved
: 불리언. 미해결 신고로 필터링할지 여부입니다. 모든 신고를 가져오려면 `resolved`와 함께 사용하세요.

account_id
: 문자열. 이 계정이 제출한 신고로 필터링합니다.

target_account_id
: 문자열. 이 계정을 대상으로 하는 신고로 필터링합니다.

max_id 
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

since_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

min_id
: **내부 매개변수입니다.** 페이지네이션에는 HTTP `Link` 헤더를 사용하세요.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 신고 100개이며 최대 200개입니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

```json
[
	{
		"id": "3",
		"action_taken": false,
		"action_taken_at": null,
		"category": "spam",
		"comment": "",
		"forwarded": false,
		"created_at": "2022-09-09T21:19:23.085Z",
		"updated_at": "2022-09-09T21:19:23.085Z",
		"account": {
			"id": "108965218747268792",
			"username": "admin",
			"domain": null,
			"created_at": "2022-09-08T22:48:07.985Z",
			"email": "admin@mastodon.local",
			// ...
			"account": {
				"id": "108965218747268792",
				"username": "admin",
				"acct": "admin",
				// ...
			}
		},
		"target_account": {
			"id": "108965430868193066",
			"username": "goody",
			"domain": null,
			"created_at": "2022-09-08T23:42:04.731Z",
			"email": "goody@mastodon.local",
			// ...
			"account": {
				"id": "108965430868193066",
				"username": "goody",
				"acct": "goody",
				// ...
			}
		},
		"assigned_account": null,
		"action_taken_by_account": null,
		"statuses": [],
		"rules": []
	},
	// ...
]
```

Report ID는 일반적으로 API 응답에 노출되지 않으므로, 더 오래되거나 새로운 결과를 가져오려면 HTTP `Link` 헤더를 해석해야 합니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

```http
Link: <http://mastodon.example/api/v1/admin/reports?limit=2&max_id=2>; rel="next", <http://mastodon.example/api/v1/admin/reports?limit=2&since_id=1>; rel="prev"
```

##### 403: 금지됨 {#403-forbidden}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 신고 하나 조회 {#get-one}

```http
GET /api/v1/admin/reports/:id HTTP/1.1
```

**반환:** [Admin::Report]({{< relref "entities/Admin_Report" >}})\
**OAuth:** 사용자 토큰 + `admin:read:reports`\
**권한:** 신고 관리\
**버전 이력:**\
2.9.1 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 Report ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

```json
{
  "id": "2",
  "action_taken": true,
  "action_taken_at": "2022-09-09T21:38:54.679Z",
  "category": "spam",
  "comment": "",
  "forwarded": false,
  "created_at": "2022-09-09T21:19:44.021Z",
  "updated_at": "2022-09-09T21:38:54.681Z",
  "account": {
    "id": "108965218747268792",
    "username": "admin",
    "domain": null,
    "created_at": "2022-09-08T22:48:07.985Z",
    "email": "admin@mastodon.local",
    // ...
    "account": {
      "id": "108965218747268792",
      "username": "admin",
      "acct": "admin",
      // ...
    }
  },
  "target_account": {
    "id": "108965430868193066",
    "username": "goody",
    "domain": null,
    "created_at": "2022-09-08T23:42:04.731Z",
    "email": "goody@mastodon.local",
    // ...
    "account": {
      "id": "108965430868193066",
      "username": "goody",
      "acct": "goody",
      // ...
    }
  },
  "assigned_account": null,
  "action_taken_by_account": {
    "id": "108965218747268792",
    "username": "admin",
    "domain": null,
    "created_at": "2022-09-08T22:48:07.985Z",
    "email": "admin@mastodon.local",
    // ...
    "account": {
      "id": "108965218747268792",
      "username": "admin",
      "acct": "admin",
      // ...
    }
  },
  "statuses": [],
  "rules": []
}
```

##### 403: 금지됨 {#403-forbidden-1}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 신고 수정 {#update}

```http
PUT /api/v1/admin/reports/:id HTTP/1.1
```

신고의 메타데이터를 변경합니다.

**반환:** [Admin::Report]({{< relref "entities/Admin_Report" >}})\
**OAuth:** 사용자 토큰 + `admin:write:reports`\
**권한:** 신고 관리\
**버전 이력:**\
3.5.0 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-2}

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 데이터베이스의 Report ID입니다.

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

category
: 문자열. 신고 분류를 `spam`, `legal`, `violation`, `other` 중 하나로 변경합니다.

rule_ids[]
: 정수 배열. `violation` 분류의 신고에서는 위반한 규칙의 정확한 ID를 지정합니다. 규칙과 ID는 [GET /api/v1/instance/rules]({{< relref "methods/instance#rules" >}}) 및 [GET /api/v1/instance]({{< relref "methods/instance#v1" >}})에서 확인할 수 있습니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

신고 분류와 규칙 ID가 수정됩니다.

```json
{
  "id": "3",
  "action_taken": false,
  "action_taken_at": null,
  "category": "other",
  // ...
  "rules": []
}
```

##### 403: 금지됨 {#403-forbidden-2}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 신고를 자신에게 할당 {#assign_to_self}

```http
POST /api/v1/admin/reports/:id/assign_to_self HTTP/1.1
```

이 신고의 처리를 자신이 맡습니다.

**반환:** [Admin::Report]({{< relref "entities/Admin_Report" >}})\
**OAuth:** 사용자 토큰 + `admin:write:reports`\
**권한:** 신고 관리\
**버전 이력:**\
2.9.1 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-3}

##### 경로 매개변수 {#path-parameters-2}

:id
: {{<required>}} 문자열. 데이터베이스의 Report ID입니다.

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

신고가 나에게 할당되었거나 이미 나에게 할당된 상태입니다.

```json
{
  "id": "3",
  "action_taken": false,
  "action_taken_at": null,
  "category": "other",
  "comment": "",
  "forwarded": false,
  "created_at": "2022-09-09T21:21:01.204Z",
  "updated_at": "2022-09-11T14:39:01.531Z",
  // ...
  "assigned_account": {
    "id": "108965218747268792",
    "username": "admin",
    "domain": null,
    "created_at": "2022-09-08T22:48:07.985Z",
    "email": "admin@mastodon.local",
    // ...
    "account": {
      "id": "108965218747268792",
      "username": "admin",
      "acct": "admin",
      // ...
    }
  },
  "action_taken_by_account": null,
  "statuses": [],
  "rules": []
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

## 신고 할당 해제 {#unassign}

```http
POST /api/v1/admin/reports/:id/unassign HTTP/1.1
```

다른 사람이 맡을 수 있도록 신고 할당을 해제합니다.

**반환:** [Admin::Report]({{< relref "entities/Admin_Report" >}})\
**OAuth:** 사용자 토큰 + `admin:write:reports`\
**권한:** 신고 관리\
**버전 이력:**\
2.9.1 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-4}

##### 경로 매개변수 {#path-parameters-3}

:id
: {{<required>}} 문자열. 데이터베이스의 Report ID입니다.

##### 헤더 {#headers-4}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-4}
##### 200: 성공 {#200-ok-4}

신고가 더 이상 나에게 할당되어 있지 않거나 이미 누구에게도 할당되지 않은 상태입니다.

```json
{
  "id": "3",
  "action_taken": false,
  "action_taken_at": null,
  "category": "other",
  "comment": "",
  "forwarded": false,
  "created_at": "2022-09-09T21:21:01.204Z",
  "updated_at": "2022-09-11T14:39:01.531Z",
  // ...
  "assigned_account": null,
  "action_taken_by_account": null,
  "statuses": [],
  "rules": []
}
```

##### 403: 금지됨 {#403-forbidden-4}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 신고를 해결됨으로 표시 {#resolve}

```http
POST /api/v1/admin/reports/:id/resolve HTTP/1.1
```

추가 조치 없이 신고를 해결됨으로 표시합니다.

**반환:** [Admin::Report]({{< relref "entities/Admin_Report" >}})\
**OAuth:** 사용자 토큰 + `admin:write:reports`\
**권한:** 신고 관리\
**버전 이력:**\
2.9.1 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-5}

##### 경로 매개변수 {#path-parameters-4}

:id
: {{<required>}} 문자열. 데이터베이스의 Report ID입니다.

##### 헤더 {#headers-5}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-5}
##### 200: 성공 {#200-ok-5}

신고를 해결했거나 이미 해결된 상태입니다.

```json
{
  "id": "2",
  "action_taken": true,
  "action_taken_at": "2022-09-11T14:46:22.936Z",
  "category": "spam",
  "comment": "",
  "forwarded": false,
  "created_at": "2022-09-09T21:19:44.021Z",
  "updated_at": "2022-09-11T14:46:22.945Z",
  // ...
}
```

##### 403: 금지됨 {#403-forbidden-5}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```
---

## 종료된 신고 다시 열기 {#reopen}

```http
POST /api/v1/admin/reports/:id/reopen HTTP/1.1
```

현재 종료된 신고이면 다시 엽니다.

**반환:** [Admin::Report]({{< relref "entities/Admin_Report" >}})\
**OAuth:** 사용자 토큰 + `admin:write:reports`\
**권한:** 신고 관리\
**버전 이력:**\
2.9.1 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-6}

##### 경로 매개변수 {#path-parameters-5}

:id
: {{<required>}} 문자열. 데이터베이스의 Report ID입니다.

##### 헤더 {#headers-6}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-6}
##### 200: 성공 {#200-ok-6}

신고의 조치 완료 상태를 해제했거나 이미 조치가 없는 상태입니다.

```json
{
  "id": "2",
  "action_taken": false,
  "action_taken_at": null,
  "category": "spam",
  "comment": "",
  "forwarded": false,
  "created_at": "2022-09-09T21:19:44.021Z",
  "updated_at": "2022-09-11T14:42:21.855Z",
  // ...
}
```

##### 403: 금지됨 {#403-forbidden-6}

인증된 사용자에게 이 조치를 수행할 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/admin/accounts#action" caption="POST /api/v1/admin/accounts/:id/action" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/reports_controller.rb" caption="app/controllers/api/v1/admin/reports_controller.rb" >}}
