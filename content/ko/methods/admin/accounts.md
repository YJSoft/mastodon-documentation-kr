---
title: 관리자 계정 API 메서드
description: 계정에 대한 중재 조치를 수행합니다.
menu:
  docs:
    name: 계정
    parent: methods-admin
    identifier: methods-admin-accounts
aliases: [
  "/methods/admin/accounts",
  "/api/methods/admin/accounts",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 계정 조회(v1) {#v1}

```http
GET /api/v1/admin/accounts HTTP/1.1
```

모든 계정을 한 번에 최대 100개 조회하며, 필요하면 특정 필터 조건에 맞출 수 있습니다. 응답의 HTTP Link 헤더로 페이지네이션할 수 있습니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

**반환:** 배열: [Admin::Account]({{<relref "entities/Admin_Account">}})\
**OAuth:** 사용자 토큰 + `admin:read:accounts`\
**권한:** 사용자 관리\
**버전 이력:**\
2.9.1 - 추가\
3.3.0 - `sensitized` 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters}

local
: 불리언. 로컬 계정으로 필터링할지 여부입니다.

remote
: 불리언. 원격 계정으로 필터링할지 여부입니다.

active
: 불리언. 현재 활성 계정으로 필터링할지 여부입니다.

pending
: 불리언. 현재 승인 대기 중인 계정으로 필터링할지 여부입니다.

disabled
: 불리언. 현재 비활성화된 계정으로 필터링할지 여부입니다.

silenced
: 불리언. 현재 제한된 계정으로 필터링할지 여부입니다.

suspended
: 불리언. 현재 정지된 계정으로 필터링할지 여부입니다.

sensitized
: 불리언. 민감한 콘텐츠로 강제 지정된 계정으로 필터링할지 여부입니다.

username
: 문자열. 지정한 사용자명을 검색합니다.

display_name
: 문자열. 지정한 표시 이름을 검색합니다.

by_domain
: 문자열. 지정한 도메인으로 필터링합니다.

email
: 문자열. 이 이메일을 사용하는 사용자를 조회합니다.

ip
: 문자열. 이 IP 주소를 사용하는 사용자를 조회합니다.

staff
: 불리언. 운영진 계정으로 필터링할지 여부입니다.

max_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 작습니다. 결과의 상한을 설정합니다.

since_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 큽니다. 결과의 하한을 설정합니다.

min_id
: 문자열. 이 ID보다 바로 다음으로 새로운 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 계정 100개이며 최대 200개입니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

```json
[
  {
    "id": "108267707882207829",
    "username": "trwnh",
    "domain": null,
    "created_at": "2022-05-08T18:21:56.870Z",
    "email": "trwnh@mastodon.local",
    "ip": {
      "user_id": 2,
      "ip": "192.168.42.1",
      "used_at": "2022-05-08T18:21:56.944Z"
    },
    "role": "user",
    "confirmed": false,
    "suspended": false,
    "silenced": false,
    "disabled": false,
    "approved": true,
    "locale": "en",
    "invite_request": null,
    "ips": [
      {
        "ip": "192.168.42.1",
        "used_at": "2022-05-08T18:21:56.944Z"
      }
    ],
    "account": {
      "id": "108267707882207829",
      "username": "trwnh",
      "acct": "trwnh",
      // ...
    }
  },
  {
    "id": "108267695853695427",
    "username": "admin",
    "domain": null,
    "created_at": "2022-05-08T18:18:53.221Z",
    "email": "admin@mastodon.local",
    "ip": {
      "user_id": 1,
      "ip": "192.168.42.1",
      "used_at": "2022-09-08T16:10:38.621Z"
    },
    "role": "admin",
    "confirmed": true,
    "suspended": false,
    "silenced": false,
    "disabled": false,
    "approved": true,
    "locale": null,
    "invite_request": null,
    "ips": [
      {
        "ip": "192.168.42.1",
        "used_at": "2022-09-08T16:10:38.621Z"
      }
    ],
    "account": {
      "id": "108267695853695427",
      "username": "admin",
      "acct": "admin",
      // ...
    }
  }
]
```

##### 403: 금지됨 {#403-forbidden}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 계정 조회(v2) {#v2}

```http
GET /api/v2/admin/accounts HTTP/1.1
```

모든 계정을 한 번에 최대 100개 조회하며, 필요하면 특정 필터 조건에 맞출 수 있습니다. 응답의 HTTP Link 헤더로 페이지네이션할 수 있습니다. 자세한 내용은 [API 응답 페이지네이션]({{<relref "api/guidelines#pagination">}})을 참고하세요.

**반환:** 배열: [Admin::Account]({{<relref "entities/Admin_Account">}})\
**OAuth:** 사용자 토큰 + `admin:read:accounts`\
**권한:** 사용자 관리\
**버전 이력:**\
3.5.0 - 추가\
4.0.0 - `role_ids` 추가. 사용자 지정 역할 및 권한 지원

#### 요청 {#request-1}

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-1}

origin
: 문자열. `local` 또는 `remote` 계정으로 필터링합니다.

status
: 문자열. `active`, `pending`, `disabled`, `silenced`, `suspended` 계정으로 필터링합니다.

permissions
: 문자열. `staff` 권한(신고를 관리할 수 있는 사용자)이 있는 계정으로 필터링합니다.

role_ids[]
: 문자열 배열. 이 역할을 가진 사용자로 필터링합니다.

invited_by
: 문자열. 이 ID의 계정이 초대한 사용자를 조회합니다.

username
: 문자열. 지정한 사용자명을 검색합니다.

display_name
: 문자열. 지정한 표시 이름을 검색합니다.

by_domain
: 문자열. 지정한 도메인으로 필터링합니다.

email
: 문자열. 이 이메일을 사용하는 사용자를 조회합니다.

ip
: 문자열. 이 IP 주소를 사용하는 사용자를 조회합니다.

max_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 작습니다. 결과의 상한을 설정합니다.

since_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 큽니다. 결과의 하한을 설정합니다.

min_id
: 문자열. 이 ID보다 바로 다음으로 새로운 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 계정 100개이며 최대 200개입니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

```json
[
  {
    "id": "108267695853695427",
    "username": "admin",
    "domain": null,
    "created_at": "2022-05-08T18:18:53.221Z",
    "email": "admin@mastodon.local",
    "ip": {
      "user_id": 1,
      "ip": "192.168.42.1",
      "used_at": "2022-09-08T16:10:38.621Z"
    },
    "role": {
		"id": 3,
		"name": "Owner",
		"color": "#3584e4",
		"position": 1000,
		"permissions": 1,
		"highlighted": true,
		"created_at": "2022-09-08T22:48:07.983Z",
		"updated_at": "2022-09-09T10:45:13.226Z"
	},
    "confirmed": true,
    "suspended": false,
    "silenced": false,
    "disabled": false,
    "approved": true,
    "locale": null,
    "invite_request": null,
    "ips": [
      {
        "ip": "192.168.42.1",
        "used_at": "2022-09-08T16:10:38.621Z"
      }
    ],
    "account": {
      "id": "108267695853695427",
      "username": "admin",
      "acct": "admin",
      // ...
    }
  }
]
```

##### 403: 금지됨 {#403-forbidden-1}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 특정 계정 조회 {#get-one}

```http
GET /api/v1/admin/accounts/:id HTTP/1.1
```

지정한 계정의 관리자 수준 정보를 조회합니다.

**반환:** [Admin::Account]({{<relref "entities/Admin_Account">}})\
**OAuth:** 사용자 토큰 + `admin:read:accounts`\
**권한:** 사용자 관리\
**버전 이력:**\
2.9.1 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-2}

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 Account ID입니다.

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

```json
{
	"id": "108267695853695427",
	"username": "admin",
	"domain": null,
	"created_at": "2022-05-08T18:18:53.221Z",
	"email": "admin@mastodon.local",
	"ip": {
		"user_id": 1,
		"ip": "192.168.42.1",
		"used_at": "2022-09-08T16:10:38.621Z"
	},
	"role": {
		"id": 3,
		"name": "Owner",
		"color": "",
		"position": 1000,
		"permissions": 1,
		"highlighted": true,
		"created_at": "2022-09-08T22:48:07.983Z",
		"updated_at": "2022-09-08T22:48:07.983Z"
	},
	"confirmed": true,
	"suspended": false,
	"silenced": false,
	"disabled": false,
	"approved": true,
	"locale": null,
	"invite_request": null,
	"ips": [
		{
			"ip": "192.168.42.1",
			"used_at": "2022-09-08T16:10:38.621Z"
		}
	],
	"account": {
		"id": "108267695853695427",
		"username": "admin",
		"acct": "admin",
		// ...
	}
}
```

##### 403: 금지됨 {#403-forbidden-2}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found}

계정이 존재하지 않습니다.

```json
{
	"error": "Record not found"
}
```

---

## 승인 대기 중인 계정 승인 {#approve}

```http
POST /api/v1/admin/accounts/:id/approve HTTP/1.1
```

지정한 로컬 계정이 현재 승인 대기 중이면 승인합니다.

**반환:** [Admin::Account]({{<relref "entities/Admin_Account">}})\
**OAuth:** 사용자 토큰 + `admin:write:accounts`\
**권한:** 사용자 관리\
**버전 이력:**\
2.9.1 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-3}

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 데이터베이스의 Account ID입니다.

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

계정이 승인되었습니다.

```json
{
  "id": "108965430868193066",
  "username": "goody",
  "domain": null,
  "created_at": "2022-09-08T23:42:04.731Z",
  // ...
  "approved": true,
  // ...
}
```

##### 403: 금지됨 {#403-forbidden-3}

인증된 사용자에게 권한이 없거나, Authorization 헤더가 없거나 유효하지 않거나, 계정이 현재 승인 대기 상태가 아닙니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

계정이 존재하지 않습니다.

```json
{
	"error": "Record not found"
}
```

---

## 승인 대기 중인 계정 거절 {#reject}

```http
POST /api/v1/admin/accounts/:id/reject HTTP/1.1
```

지정한 로컬 계정이 현재 승인 대기 중이면 거절합니다.

**반환:** [Admin::Account]({{<relref "entities/Admin_Account">}})\
**OAuth:** 사용자 토큰 + `admin:write:accounts`\
**권한:** 사용자 관리\
**버전 이력:**\
2.9.1 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-4}

##### 경로 매개변수 {#path-parameters-2}

:id
: {{<required>}} 문자열. 데이터베이스의 Account ID입니다.

##### 헤더 {#headers-4}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-4}
##### 200: 성공 {#200-ok-4}

```json
{
  "id": "108965436418975594",
  "username": "badguy",
  "domain": null,
  "created_at": "2022-09-08T23:43:29.427Z",
  "email": "badguy@mastodon.local",
  "ip": null,
  "role": {
    "id": -99,
    "name": "",
    "color": "",
    "position": -1,
    "permissions": 65536,
    "highlighted": false,
    "created_at": "2022-09-08T22:48:07.977Z",
    "updated_at": "2022-09-08T22:48:07.977Z"
  },
  "confirmed": true,
  "suspended": false,
  "silenced": false,
  "disabled": false,
  "approved": false,
  "locale": "en",
  "invite_request": "i am going to commit crimes",
  "ips": [],
  "account": {
    "id": "108965436418975594",
    "username": "badguy",
    "acct": "badguy",
    "display_name": "",
    "locked": false,
    "bot": false,
    "discoverable": null,
    "group": false,
    "created_at": "2022-09-08T00:00:00.000Z",
    "note": "",
    "url": "http://mastodon.local/@badguy",
    "avatar": "http://mastodon.local/avatars/original/missing.png",
    "avatar_static": "http://mastodon.local/avatars/original/missing.png",
    "header": "http://mastodon.local/headers/original/missing.png",
    "header_static": "http://mastodon.local/headers/original/missing.png",
    "followers_count": 0,
    "following_count": 0,
    "statuses_count": 0,
    "last_status_at": null,
    "emojis": [],
    "fields": []
  }
}
```

##### 403: 금지됨 {#403-forbidden-4}

인증된 사용자에게 권한이 없거나, Authorization 헤더가 없거나 유효하지 않거나, 계정이 현재 승인 대기 상태가 아닙니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found-2}

계정이 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

## 계정 삭제 {#delete}

```http
DELETE /api/v1/admin/accounts/:id HTTP/1.1
```

정지된 계정의 데이터를 영구적으로 삭제합니다.

**반환:** [Admin::Account]({{<relref "entities/Admin_Account">}})\
**OAuth:** 사용자 토큰 + `admin:write:accounts`\
**권한:** 사용자 데이터 삭제\
**버전 이력:**\
3.3.0 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-5}

##### 경로 매개변수 {#path-parameters-3}

:id
: {{<required>}} 문자열. 데이터베이스의 Account ID입니다.

##### 헤더 {#headers-5}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-5}
##### 200: 성공 {#200-ok-5}

계정 데이터가 삭제되었습니다.

```json
{
  "id": "108965430868193066",
  "username": "goody",
  "domain": null,
  "created_at": "2022-09-08T23:42:04.731Z",
  "email": "goody@mastodon.local",
  "ip": {
    "user_id": 3,
    "ip": "192.168.42.1",
    "used_at": "2022-09-08T23:42:04.761Z"
  },
  "role": {
    "id": -99,
    "name": "",
    "color": "",
    "position": -1,
    "permissions": 65536,
    "highlighted": false,
    "created_at": "2022-09-08T22:48:07.977Z",
    "updated_at": "2022-09-08T22:48:07.977Z"
  },
  "confirmed": true,
  "suspended": true,
  "silenced": false,
  "disabled": false,
  "approved": true,
  "locale": "en",
  "invite_request": "this is a compelling reason",
  "ips": [
    {
      "ip": "192.168.42.1",
      "used_at": "2022-09-08T23:42:04.761Z"
    }
  ],
  "account": {
    "id": "108965430868193066",
    "username": "goody",
    "acct": "goody",
    "display_name": "",
    "locked": false,
    "bot": false,
    "discoverable": false,
    "group": false,
    "created_at": "2022-09-08T00:00:00.000Z",
    "note": "",
    "url": "http://mastodon.local/@goody",
    "avatar": "http://mastodon.local/avatars/original/missing.png",
    "avatar_static": "http://mastodon.local/avatars/original/missing.png",
    "header": "http://mastodon.local/headers/original/missing.png",
    "header_static": "http://mastodon.local/headers/original/missing.png",
    "followers_count": 0,
    "following_count": 0,
    "statuses_count": 0,
    "last_status_at": null,
    "suspended": true,
    "emojis": [],
    "fields": []
  }
}
```

##### 403: 금지됨 {#403-forbidden-5}

인증된 사용자에게 권한이 없거나, Authorization 헤더가 없거나 유효하지 않거나, 계정이 이미 삭제되었습니다.

```json
{
  "error": "This action is not allowed"
}
```

---

## 계정에 조치 수행 {#action}

```http
POST /api/v1/admin/accounts/:id/action HTTP/1.1
```

계정에 조치를 수행하고 중재 기록에 남깁니다. 또한 이 계정에 대한 미해결 신고를 모두 해결합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `admin:write:accounts`\
**권한:** 사용자 관리, 신고 관리\
**버전 이력:**\
2.9.1 - 추가\
3.3.0 - 가능한 `type` 값으로 `sensitive` 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-6}

##### 경로 매개변수 {#path-parameters-4}

:id
: {{<required>}} 문자열. 데이터베이스의 Account ID입니다.

##### 헤더 {#headers-6}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

type
: {{<required>}} 문자열. 수행할 조치 유형입니다: `none`, `sensitive`, `disable`, `silence`, `suspend`.

report_id
: 문자열. 이 조치의 원인이 된 관련 신고의 ID입니다.

warning_preset_id
: 문자열. 미리 설정된 경고의 ID입니다.

text
: 문자열. 이 조치를 수행한 이유에 대한 추가 설명입니다.

send_email_notification
: 불리언. 위 정보를 포함한 이메일을 사용자에게 보낼지 여부입니다.

#### 응답 {#response-6}
##### 200: 성공 {#200-ok-6}

조치를 수행했습니다.

```json
{}
```

##### 403: 금지됨 {#403-forbidden-6}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found-3}

지정한 ID의 Account 또는 Report가 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 서버 오류 {#422-server-error}

`type`이 제공되지 않았거나 인식할 수 없습니다.

```json
{
  "error": "Record invalid"
}
```

---

## 현재 비활성화된 계정 활성화 {#enable}

```http
POST /api/v1/admin/accounts/:id/enable HTTP/1.1
```

현재 로그인이 비활성화된 로컬 계정을 다시 활성화합니다.

**반환:** [Admin::Account]({{<relref "entities/Admin_Account">}})\
**OAuth:** 사용자 토큰 + `admin:write:accounts`\
**권한:** 사용자 관리\
**버전 이력:**\
2.9.1 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-7}

##### 경로 매개변수 {#path-parameters-5}

:id
: {{<required>}} 문자열. 데이터베이스의 Account ID입니다.

##### 헤더 {#headers-7}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-7}
##### 200: 성공 {#200-ok-7}

계정을 활성화했거나 이미 활성화된 상태입니다.

```json
{
	"id": "108965430868193066",
	"username": "goody",
	"domain": null,
	"created_at": "2022-09-08T23:42:04.731Z",
	// ...
	"disabled": false,
	// ...
}
```

##### 403: 금지됨 {#403-forbidden-7}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found-4}

계정이 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

## 계정 제한 해제 {#unsilence}

```http
POST /api/v1/admin/accounts/:id/unsilence HTTP/1.1
```

현재 제한된 계정이면 제한을 해제합니다.

**반환:** [Admin::Account]({{<relref "entities/Admin_Account">}})\
**OAuth:** 사용자 토큰 + `admin:write:accounts`\
**권한:** 사용자 관리\
**버전 이력:**\
2.9.1 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-8}

##### 경로 매개변수 {#path-parameters-6}

:id
: {{<required>}} 문자열. 데이터베이스의 Account ID입니다.

##### 헤더 {#headers-8}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-8}
##### 200: 성공 {#200-ok-8}

계정의 제한을 해제했거나 이미 제한되지 않은 상태입니다.

```json
{
  "id": "108965430868193066",
  "username": "goody",
  "domain": null,
  "created_at": "2022-09-08T23:42:04.731Z",
  // ...
  "silenced": false,
  // ...
}
```

##### 403: 금지됨 {#403-forbidden-8}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found-5}

계정이 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

## 계정 정지 해제 {#unsuspend}

```http
POST /api/v1/admin/accounts/:id/unsuspend HTTP/1.1
```

현재 정지된 계정의 정지를 해제합니다.

**반환:** [Admin::Account]({{<relref "entities/Admin_Account">}})\
**OAuth:** 사용자 토큰 + `admin:write:accounts`\
**권한:** 사용자 관리\
**버전 이력:**\
2.9.1 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-9}

##### 경로 매개변수 {#path-parameters-7}

:id
: {{<required>}} 문자열. 데이터베이스의 Account ID입니다.

##### 헤더 {#headers-9}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-9}
##### 200: 성공 {#200-ok-9}

계정의 정지를 해제했습니다.

```json
{
  "id": "108965430868193066",
  "username": "goody",
  "domain": null,
  "created_at": "2022-09-08T23:42:04.731Z",
  // ...
  "suspended": false,
  // ...
}
```

##### 403: 금지됨 {#403-forbidden-9}

인증된 사용자에게 권한이 없거나, Authorization 헤더가 없거나 유효하지 않거나, Account가 현재 정지 상태가 아닙니다.

```json
{
	"error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found-6}

계정이 존재하지 않습니다.

```json
{
	"error": "Record not found"
}
```

---

## 계정의 민감한 콘텐츠 표시 해제 {#unsensitive}

```http
POST /api/v1/admin/accounts/:id/unsensitive HTTP/1.1
```

이전에 민감한 콘텐츠로 지정된 계정이면 게시물을 민감한 콘텐츠로 표시하는 것을 중단합니다.

**반환:** [Admin::Account]({{<relref "entities/Admin_Account">}})\
**OAuth:** 사용자 토큰 + `admin:write:accounts`\
**권한:** 사용자 관리\
**버전 이력:**\
3.3.0 - 추가\
4.0.0 - 사용자 지정 역할 및 권한 지원

#### 요청 {#request-10}

##### 경로 매개변수 {#path-parameters-8}

:id
: {{<required>}} 문자열. 데이터베이스의 Account ID입니다.

##### 헤더 {#headers-10}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-10}
##### 200: 성공 {#200-ok-10}

계정의 민감한 콘텐츠 표시를 해제했거나 이미 표시되지 않은 상태입니다.

```json
{
  "id": "108965430868193066",
  "username": "goody",
  "domain": null,
  "created_at": "2022-09-08T23:42:04.731Z",
  // ...
  "sensitized": false,
  // ...
}
```

##### 403: 금지됨 {#403-forbidden-10}

인증된 사용자에게 권한이 없거나 Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "This action is not allowed"
}
```

##### 404: 찾을 수 없음 {#404-not-found-7}

계정이 존재하지 않습니다.

```json
{
	"error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/accounts_controller.rb" caption="app/controllers/api/v1/admin/accounts_controller.rb" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/admin/account_actions_controller.rb" caption="app/controllers/api/v1/admin/account_actions_controller.rb" >}}