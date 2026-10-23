---
title: 알림 API 메서드
description: 계정이나 게시물의 활동에 대한 알림을 받습니다.
menu:
  docs:
    name: 알림
    parent: methods
    identifier: methods-notifications
aliases: [
  "/methods/notifications",
  "/api/methods/notifications",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 모든 알림 가져오기 {#get}

```http
GET /api/v1/notifications HTTP/1.1
```

사용자에 관한 알림입니다. 이 API는 다음/이전 페이지 링크가 담긴 Link 헤더를 반환합니다. 쿼리 매개변수와 `id` 값으로 링크를 동적으로 구성할 수도 있습니다.

필터링할 유형은 다음과 같습니다.
- `mention` = 누군가 게시물에서 나를 멘션함
- `status` = 알림을 활성화한 사람이 게시물을 작성함
- `reblog` = 누군가 내 게시물을 부스트함
- `follow` = 누군가 나를 팔로우함
- `follow_request` = 누군가 내게 팔로우를 요청함
- `favourite` = 누군가 내 게시물에 좋아요를 누름
- `poll` = 내가 투표했거나 생성한 투표가 종료됨
- `update` = 내가 부스트한 게시물이 편집됨
- `added_to_collection` = 누군가 나를 컬렉션에 추가함
- `collection_update` = 내가 추천된 컬렉션이 수정됨
- `admin.sign_up` = 누군가 가입함(선택적으로 관리자에게 전송)
- `admin.report` = 새 신고가 제출됨

**반환:** 배열: [Notification]({{< relref "entities/Notification" >}})\
**OAuth:** 사용자 토큰 + `read:notifications`\
**버전 이력:**\
0.0.0 - 추가\
2.6.0 - `min_id` 추가\
2.9.0 - `account_id` 추가\
3.1.0 - `follow_request` 유형 추가\
3.3.0 - `status` 유형 추가. 이제 `min_id`와 `max_id` 동시 사용 가능\
3.5.0 - `types` 추가. `update` 및 `admin.sign_up` 유형 추가\
4.0.0 - `admin.report` 유형 추가\
4.1.0 - 알림 수 제한을 15개(최대 30개)에서 40개(최대 80개)로 변경\
4.3.0 - `include_filtered` 매개변수 추가\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - 선택적 매개변수 `supported_types` 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters}

max_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 작습니다. 결과의 상한을 설정합니다.

since_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 큽니다. 결과의 하한을 설정합니다.

min_id
: 문자열. 이 ID보다 바로 다음으로 새로운 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 알림 40개이며 최대 80개입니다.

types[]
: 문자열 배열. 결과에 포함할 유형입니다.

exclude_types[]
: 문자열 배열. 결과에서 제외할 유형입니다.

account_id
: 문자열. 지정한 계정에서 받은 알림만 반환합니다.

include_filtered
: 불리언. 사용자의 [NotificationPolicy]({{< relref "entities/NotificationPolicy" >}})로 필터링된 알림을 포함할지 여부입니다. 기본값은 false입니다.

supported_types[]
: 문자열 배열. 대체 표현이 있어도 사용하지 않을 알림 유형입니다. 어떤 알림이든 대체 표현을 받으려면 이 매개변수를 전달해야 합니다. 이 매개변수를 사용하면 유형이 `supported_types`에 포함되지 *않은* 알림에 사용 가능한 대체 표현이 있을 때 알림의 `fallback` 속성에 포함합니다.

#### 응답 {#response}

limit=2인 호출 예입니다.

```http
GET https://mastodon.social/api/v1/notifications?limit=2 HTTP/1.1
Authorization: Bearer <user_token>
```

##### 200: 성공 {#200-ok}

응답 본문에는 알림 한 페이지가 포함됩니다. HTTP Link 헤더로 추가 페이지네이션할 수 있습니다.

```http
Link: <https://mastodon.example/api/v1/notifications?max_id=34975535>; rel="next", <https://mastodon.example/api/v1/notifications?min_id=34975861>;
```

```json
[
  {
    "id": "34975861",
    "type": "mention",
    "created_at": "2019-11-23T07:49:02.064Z",
    "account": {
      "id": "971724",
      "username": "zsc",
      "acct": "zsc",
      // ...
    },
    "status": {
      "id": "103186126728896492",
      "created_at": "2019-11-23T07:49:01.940Z",
      "in_reply_to_id": "103186038209478945",
      "in_reply_to_account_id": "14715",
      // ...
      "content": "<p><span class=\"h-card\"><a href=\"https://mastodon.social/@trwnh\" class=\"u-url mention\">@<span>trwnh</span></a></span> sup!</p>",
      // ...
      "account": {
        "id": "971724",
        "username": "zsc",
        "acct": "zsc",
        // ...
      },
      // ...
      "mentions": [
        {
          "id": "14715",
          "username": "trwnh",
          "url": "https://mastodon.social/@trwnh",
          "acct": "trwnh"
        }
      ],
      // ...
    }
  },
  {
    "id": "34975535",
    "type": "favourite",
    "created_at": "2019-11-23T07:29:18.903Z",
    "account": {
      "id": "297420",
      "username": "haskal",
      "acct": "haskal@cybre.space",
      // ...
    },
    "status": {
      "id": "103186046267791694",
      "created_at": "2019-11-23T07:28:34.210Z",
      "in_reply_to_id": "103186044372624124",
      "in_reply_to_account_id": "297420",
      // ...
      "account": {
        "id": "14715",
        "username": "trwnh",
        "acct": "trwnh",
        // ...
      }
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

## 알림 하나 가져오기 {#get-one}

```http
GET /api/v1/notifications/:id HTTP/1.1
```

지정한 ID의 알림 정보를 조회합니다.

**반환:** [Notification]({{< relref "entities/Notification" >}})\
**OAuth:** 사용자 토큰 + `read:notifications`\
**버전 이력:**\
0.0.0 - 추가\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - 선택적 매개변수 `supported_types` 추가

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 Notification ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-1}

supported_types[]
: 문자열 배열. 대체 표현이 있어도 사용하지 않을 알림 유형입니다. 어떤 알림이든 대체 표현을 받으려면 이 매개변수를 전달해야 합니다. 이 매개변수를 사용하면 유형이 `supported_types`에 포함되지 *않은* 알림에 사용 가능한 대체 표현이 있을 때 알림의 `fallback` 속성에 포함합니다.

#### 응답 {#response-1}

##### 200: 성공 {#200-ok-1}

Notification 하나입니다.

```json
{
  "id": "34975861",
  "type": "mention",
  "created_at": "2019-11-23T07:49:02.064Z",
  "account": {
    "id": "971724",
    "username": "zsc",
    "acct": "zsc",
    // ...
  },
  "status": {
    "id": "103186126728896492",
    "created_at": "2019-11-23T07:49:01.940Z",
    "in_reply_to_id": "103186038209478945",
    "in_reply_to_account_id": "14715",
    // ...
    "content": "<p><span class=\"h-card\"><a href=\"https://mastodon.social/@trwnh\" class=\"u-url mention\">@<span>trwnh</span></a></span> sup!</p>",
    // ...
    "account": {
      "id": "971724",
      "username": "zsc",
      "acct": "zsc",
      // ...
    },
    // ...
    "mentions": [
      {
        "id": "14715",
        "username": "trwnh",
        "url": "https://mastodon.social/@trwnh",
        "acct": "trwnh"
      }
    ],
    // ...
  }
}
```

##### 401: 인증되지 않음 {#401-unauthorized-1}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 모든 알림 지우기 {#clear}

```http
POST /api/v1/notifications/clear HTTP/1.1
```

서버의 모든 알림을 지웁니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:notifications`\
**버전 이력:**\
0.0.0 - 추가

#### 요청 {#request-2}
##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-2}

##### 200: 성공 {#200-ok-2}

알림을 지웠습니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-2}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 알림 하나 지우기 {#dismiss}

```http
POST /api/v1/notifications/:id/dismiss HTTP/1.1
```

서버에서 알림 하나를 지웁니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:notifications`\
**버전 이력:**\
1.3.0 - 추가

#### 요청 {#request-3}

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 데이터베이스의 Notification ID입니다.

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-3}

##### 200: 성공 {#200-ok-3}

지정한 ID의 Notification을 지웠습니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-3}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 알림 하나 지우기 {{%removed%}} {#dismiss-deprecated}

```http
POST /api/v1/notifications/dismiss HTTP/1.1
```

서버에서 알림 하나를 지웁니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:notifications`\
**버전 이력**:\
0.0.0 - 사용 가능\
1.3.0 - [notifications/:id/dismiss](#dismiss)를 권장하며 사용 중단 예정\
3.0.0 - 제거

#### 요청 {#request-4}

##### 헤더 {#headers-4}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}
id
: {{<required>}} 문자열. 데이터베이스의 알림 ID입니다.

#### 응답 {#response-4}

##### 200: 성공 {#200-ok-4}

지정한 ID의 Notification을 지웠습니다.

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

---

## 읽지 않은 알림 수 가져오기 {#unread-count}

```http
GET /api/v1/notifications/unread_count HTTP/1.1
```

현재 사용자의 읽지 않은 알림 수를 상한 내에서 가져옵니다.
[알림 읽음 마커]({{< relref "methods/markers" >}})보다 새로운 알림은 읽지 않은 것으로 간주합니다.
개수는 매개변수에 따라 달라지므로 매번 계산하며 비교적 느린 작업입니다(해당 알림 전체를 가져오는 것보다는 빠릅니다). 따라서 반환하는 알림 수에 상한이 있습니다.

**반환:** `count` 키 하나를 포함하는 해시\
**OAuth:** 사용자 토큰 + `read:notifications`\
**버전 이력**:\
4.3.0 - 추가

#### 요청 {#request-5}

##### 헤더 {#headers-5}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-2}

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 알림 100개이며 최대 1000개입니다.

types[]
: 문자열 배열. 읽지 않은 알림 수에 포함할 알림 유형입니다.

exclude_types[]
: 문자열 배열. 읽지 않은 알림 수에서 제외할 알림 유형입니다.

account_id
: 문자열. 지정한 계정에서 받은 읽지 않은 알림만 셉니다.

#### 응답 {#response-5}

##### 200: 성공 {#200-ok-5}

응답 본문에는 상한을 적용한 읽지 않은 알림 수가 포함됩니다.

```json
{
  "count": 42,
}
```

##### 401: 인증되지 않음 {#401-unauthorized-5}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 알림 필터링 정책 가져오기 {#get-policy}

```http
GET /api/v2/notifications/policy HTTP/1.1
```

사용자의 알림 필터링 정책입니다.

**반환:** [NotificationPolicy]({{< relref "entities/NotificationPolicy" >}})\
**OAuth:** 사용자 토큰 + `read:notifications`\
**버전 이력:**\
4.3.0 - 추가

#### 요청 {#request-6}

##### 헤더 {#headers-6}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

#### 응답 {#response-6}

##### 200: 성공 {#200-ok-6}

응답 본문에는 사용자의 현재 알림 필터링 정책이 포함됩니다.

```json
{
  "for_not_following": "accept",
  "for_not_followers": "accept",
  "for_new_accounts": "accept",
  "for_private_mentions": "drop",
  "for_limited_accounts": "filter",
  "summary": {
    "pending_requests_count": 0,
    "pending_notifications_count": 0
  }
}
```

##### 401: 인증되지 않음 {#401-unauthorized-6}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

## 알림 필터링 정책 수정 {#update-the-filtering-policy-for-notifications}

```http
PATCH /api/v2/notifications/policy HTTP/1.1
```

사용자의 알림 필터링 정책을 수정합니다.

**반환:** [NotificationPolicy]({{< relref "entities/NotificationPolicy" >}})\
**OAuth:** 사용자 토큰 + `write:notifications`\
**버전 이력:**\
4.3.0 - 추가

#### 요청 {#request-7}

##### 헤더 {#headers-7}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

#### 폼 데이터 매개변수 {#form-data-parameters-1}

for_not_following
: 문자열. 사용자가 팔로우하지 않는 계정의 알림을 `accept`, `filter`, `drop` 중 어떻게 처리할지 결정합니다. `drop`은 기반 활동을 막지 않으면서 알림 객체 생성을 완전히 방지하고, `filter`는 필터링됨으로 표시하며, `accept`는 처리에 영향을 주지 않습니다.

for_not_followers
: 문자열. 사용자를 팔로우하지 않는 계정의 알림을 `accept`, `filter`, `drop` 중 어떻게 처리할지 결정합니다. `drop`은 기반 활동을 막지 않으면서 알림 객체 생성을 완전히 방지하고, `filter`는 필터링됨으로 표시하며, `accept`는 처리에 영향을 주지 않습니다.

for_new_accounts
: 문자열. 지난 30일 안에 생성된 계정의 알림을 `accept`, `filter`, `drop` 중 어떻게 처리할지 결정합니다. `drop`은 기반 활동을 막지 않으면서 알림 객체 생성을 완전히 방지하고, `filter`는 필터링됨으로 표시하며, `accept`는 처리에 영향을 주지 않습니다.

for_private_mentions
: 문자열. 개인 멘션 알림을 `accept`, `filter`, `drop` 중 어떻게 처리할지 결정합니다. `drop`은 기반 활동을 막지 않으면서 알림 객체 생성을 완전히 방지하고, `filter`는 필터링됨으로 표시하며, `accept`는 처리에 영향을 주지 않습니다. 사용자가 시작한 개인 멘션에 대한 답글과 사용자가 팔로우하는 계정은 이 값에 관계없이 항상 허용합니다.

for_limited_accounts
: 문자열. 중재자가 제한한 계정의 알림을 `accept`, `filter`, `drop` 중 어떻게 처리할지 결정합니다. `drop`은 기반 활동을 막지 않으면서 알림 객체 생성을 완전히 방지하고, `filter`는 필터링됨으로 표시하며, `accept`는 처리에 영향을 주지 않습니다.


#### 응답 {#response-7}

##### 200: 성공 {#200-ok-7}

응답 본문에는 사용자의 수정된 알림 필터링 정책이 포함됩니다.

```json
{
  "filter_not_following": false,
  "filter_not_followers": false,
  "filter_new_accounts": false,
  "filter_private_mentions": true,
  "summary": {
    "pending_requests_count": 0,
    "pending_notifications_count": 0
  }
}
```

##### 401: 인증되지 않음 {#401-unauthorized-7}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 모든 알림 요청 가져오기 {#get-requests}

```http
GET /api/v1/notifications/requests HTTP/1.1
```

사용자의 정책에 따라 필터링된 알림에 대한 알림 요청입니다. 이 API는 다음/이전 페이지 링크가 담긴 Link 헤더를 반환합니다.

**반환:** 배열: [NotificationRequest]({{< relref "entities/NotificationRequest" >}})\
**OAuth:** 사용자 토큰 + `read:notifications`\
**버전 이력:**\
4.3.0 - 추가

#### 요청 {#request-8}

##### 헤더 {#headers-8}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-3}

max_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 작습니다. 결과의 상한을 설정합니다.

since_id
: 문자열. 반환되는 모든 결과의 ID는 이 ID보다 큽니다. 결과의 하한을 설정합니다.

min_id
: 문자열. 이 ID보다 바로 다음으로 새로운 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 알림 요청 40개이며 최대 80개입니다.

#### 응답 {#response-8}

##### 200: 성공 {#200-ok-8}

응답 본문에는 알림 요청 한 페이지가 포함됩니다. HTTP Link 헤더로 추가 페이지네이션할 수 있습니다.

```http
Link: <https://mastodon.example/api/v1/notifications/requests?max_id=112456967201894256>; rel="next", <https://mastodon.example/api/v1/notifications/requests?min_id=112456967201894256>; rel="prev"
```

```json
[
  {
    "id": "112456967201894256",
    "created_at": "2024-05-17T14:45:41.171Z",
    "updated_at": "2024-05-17T14:45:41.171Z",
    "notifications_count": "1",
    "account": {
      "id": "971724",
      "username": "zsc",
      "acct": "zsc",
      // ...
    },
    "last_status": {
      "id": "103186126728896492",
      "created_at": "2019-11-23T07:49:01.940Z",
      "in_reply_to_id": "103186038209478945",
      "in_reply_to_account_id": "14715",
      // ...
      "content": "<p><span class=\"h-card\"><a href=\"https://mastodon.social/@trwnh\" class=\"u-url mention\">@<span>trwnh</span></a></span> sup!</p>",
      // ...
      "account": {
        "id": "971724",
        "username": "zsc",
        "acct": "zsc",
        // ...
      },
      // ...
      "mentions": [
        {
          "id": "14715",
          "username": "trwnh",
          "url": "https://mastodon.social/@trwnh",
          "acct": "trwnh"
        }
      ],
      // ...
    }
  }
]
```

##### 401: 인증되지 않음 {#401-unauthorized-8}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 알림 요청 하나 가져오기 {#get-one-request}

```http
GET /api/v1/notifications/requests/:id HTTP/1.1
```

지정한 ID의 알림 요청 정보를 조회합니다.

**반환:** [NotificationRequest]({{< relref "entities/NotificationRequest" >}})\
**OAuth:** 사용자 토큰 + `read:notifications`\
**버전 이력:**\
4.3.0 - 추가

#### 요청 {#request-9}

##### 경로 매개변수 {#path-parameters-2}

:id
: {{<required>}} 문자열. 데이터베이스의 Notification ID입니다.

##### 헤더 {#headers-9}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

#### 응답 {#response-9}

##### 200: 성공 {#200-ok-9}

알림 요청 하나입니다.

```json
  {
    "id": "112456967201894256",
    "created_at": "2024-05-17T14:45:41.171Z",
    "updated_at": "2024-05-17T14:45:41.171Z",
    "notifications_count": "1",
    "account": {
      "id": "971724",
      "username": "zsc",
      "acct": "zsc",
      // ...
    },
    "last_status": {
      "id": "103186126728896492",
      "created_at": "2019-11-23T07:49:01.940Z",
      "in_reply_to_id": "103186038209478945",
      "in_reply_to_account_id": "14715",
      // ...
      "content": "<p><span class=\"h-card\"><a href=\"https://mastodon.social/@trwnh\" class=\"u-url mention\">@<span>trwnh</span></a></span> sup!</p>",
      // ...
      "account": {
        "id": "971724",
        "username": "zsc",
        "acct": "zsc",
        // ...
      },
      // ...
      "mentions": [
        {
          "id": "14715",
          "username": "trwnh",
          "url": "https://mastodon.social/@trwnh",
          "acct": "trwnh"
        }
      ],
      // ...
    }
  }
```

##### 401: 인증되지 않음 {#401-unauthorized-9}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 알림 요청 하나 수락 {#accept-request}

```http
POST /api/v1/notifications/requests/:id/accept HTTP/1.1
```

알림 요청을 수락하여 해당 사용자의 필터링된 알림을 기본 알림에 다시 합치고 이후 알림을 모두 수락합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:notifications`\
**버전 이력:**\
4.3.0 - 추가

#### 요청 {#request-10}

##### 경로 매개변수 {#path-parameters-3}

:id
: {{<required>}} 문자열. 데이터베이스의 Notification ID입니다.

##### 헤더 {#headers-10}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

#### 응답 {#response-10}

##### 200: 성공 {#200-ok-10}

호출이 성공하면 빈 객체를 반환합니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-10}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 알림 요청 하나 지우기 {#dismiss-request}

```http
POST /api/v1/notifications/requests/:id/dismiss HTTP/1.1
```

알림 요청을 지워 숨기고 대기 중인 알림 요청 수에 포함되지 않게 합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:notifications`\
**버전 이력:**\
4.3.0 - 추가

#### 요청 {#request-11}

##### 경로 매개변수 {#path-parameters-4}

:id
: {{<required>}} 문자열. 데이터베이스의 Notification ID입니다.

##### 헤더 {#headers-11}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

#### 응답 {#response-11}

##### 200: 성공 {#200-ok-11}

호출이 성공하면 빈 객체를 반환합니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-11}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 여러 알림 요청 수락 {#accept-multiple-requests}

```http
POST /api/v1/notifications/requests/accept HTTP/1.1
```

여러 알림 요청을 수락하여 해당 사용자들의 필터링된 알림을 기본 알림에 다시 합치고 이후 알림을 모두 수락합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:notifications`\
**버전 이력:**\
4.3.0 - 추가

#### 요청 {#request-12}

##### 폼 데이터 매개변수 {#form-data-parameters-2}

:id[]
: {{<required>}} 문자열 배열. 데이터베이스의 알림 요청 ID입니다.

##### 헤더 {#headers-12}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

#### 응답 {#response-12}

##### 200: 성공 {#200-ok-12}

호출이 성공하면 빈 객체를 반환합니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-12}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 여러 알림 요청 지우기 {#dismiss-multiple-requests}

```http
POST /api/v1/notifications/requests/dismiss HTTP/1.1
```

여러 알림 요청을 지워 숨기고 대기 중인 알림 요청 수에 포함되지 않게 합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:notifications`\
**버전 이력:**\
4.3.0 - 추가

#### 요청 {#request-13}

##### 폼 데이터 매개변수 {#form-data-parameters-3}

:id[]
: {{<required>}} 문자열 배열. 데이터베이스의 알림 요청 ID입니다.

##### 헤더 {#headers-13}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

#### 응답 {#response-13}

##### 200: 성공 {#200-ok-13}

호출이 성공하면 빈 객체를 반환합니다.

```json
{}
```

##### 401: 인증되지 않음 {#401-unauthorized-13}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 수락한 알림 요청의 병합 여부 확인 {#requests-merged}

```http
GET /api/v1/notifications/requests/merged
```

수락한 알림 요청이 병합되었는지 확인합니다.
알림 요청을 수락하면 필터링된 알림을 일반 알림 목록으로 병합하는 백그라운드 작업을 예약합니다. 처리가 끝나면 클라이언트는 가능한 한 빨리 알림 목록을 새로고침해야 합니다. `notifications_merged` 스트리밍 이벤트로 이를 알리지만 이 엔드포인트로 폴링할 수도 있습니다.

***반환:** 불리언 속성 `merged` 하나가 있는 해시\
**OAuth:** 사용자 토큰 + `read:notifications`\
**버전 이력:**\
4.3.0 - 추가

#### 요청 {#request-14}

##### 헤더 {#headers-14}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

#### 응답 {#response-14}

##### 200: 성공 {#200-ok-14}

호출이 성공하면 알림이 병합되어 가져올 준비가 되었는지 반환합니다.

```json
{
  "merged": false
}
```

##### 401: 인증되지 않음 {#401-unauthorized-14}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/push" caption="푸시 API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/notifications_controller.rb" caption="app/controllers/api/v1/notifications_controller.rb" >}}
