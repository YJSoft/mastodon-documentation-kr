---
title: 그룹화된 알림 API 메서드
description: 계정이나 게시물의 활동에 대한 그룹화된 알림을 받습니다.
menu:
  docs:
    name: 그룹화된 알림
    parent: methods
    identifier: methods-grouped-notifications
aliases: [
  "/methods/grouped_notifications",
  "/api/methods/grouped_notifications",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

이 페이지는 다음 목적을 위해 서버 측에 구현한 그룹화된 알림에 관한 설명입니다.
- 클라이언트 간에 일관된 그룹화 제공
- 클라이언트가 새 그룹에 추가할 내용이 없는 페이지 전체를 탐색하는 문제 방지. 서버 측에서 이미 알림의 중복을 제거합니다.

큰 알림 그룹은 대체로 같은 계정을 포함하므로 그룹화되지 않은 알림과 API 형태가 조금 다릅니다. 계정을 루트 키로 옮기면 많은 중복을 피하여 서버 작업량과 네트워크 데이터 크기를 줄일 수 있습니다.

## 그룹화된 모든 알림 가져오기 {#get-grouped}

```http
GET /api/v2/notifications HTTP/1.1
```

사용자에 관한 그룹화된 알림을 반환합니다. 이 API는 다음/이전 페이지 링크가 담긴 Link 헤더를 반환합니다. 쿼리 매개변수와 `id` 값으로 링크를 동적으로 구성할 수도 있습니다.

서버는 비슷한 시간대에 같은 대상을 향해 발생한 동일 유형의 `favourite`, `follow`, `reblog`, `admin.sign_up` 알림에 같은 `group_key`를 부여합니다. 이 엔드포인트를 조회하면 `group_key`마다 객체 하나로 집계한 알림을 반환합니다. 향후 다른 유형도 그룹화될 수 있습니다. 클라이언트는 `grouped_types` 매개변수로 그룹화된 표시를 지원하는 유형을 명시해야 합니다.

필터링할 유형은 다음과 같습니다.
- `mention` = 누군가 게시물에서 나를 멘션함
- `status` = 알림을 활성화한 사람이 게시물을 작성함
- `reblog` = 누군가 내 게시물을 부스트함
- `follow` = 누군가 나를 팔로우함
- `follow_request` = 누군가 내게 팔로우를 요청함
- `favourite` = 누군가 내 게시물에 좋아요를 누름
- `poll` = 내가 투표했거나 생성한 투표가 종료됨
- `update` = 내가 부스트한 게시물이 편집됨
- `admin.sign_up` = 누군가 가입함(선택적으로 관리자에게 전송)
- `admin.report` = 새 신고가 제출됨

**반환:** [GroupedNotificationsResults](#GroupedNotificationsResults)\
**OAuth:** 사용자 토큰 + `read:notifications`\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가\
4.4.0 - 그룹화 알림 유형에 `admin.sign_up` 추가\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - 선택적 매개변수 `supported_types` 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters}

max_id
: 문자열. 반환 결과는 모두 이 알림 ID보다 엄격히 오래된 알림에 관한 것입니다. 결과의 상한을 설정합니다.

since_id
: 문자열. 반환 결과는 모두 이 알림 ID보다 엄격히 새로운 알림에 관한 것입니다. 결과의 하한을 설정합니다.

min_id
: 문자열. 이 알림 ID보다 바로 다음으로 새로운 알림 결과를 반환합니다. 이 ID에 커서를 설정하고 앞으로 페이지를 이동합니다.

limit
: 정수. 반환할 최대 결과 수입니다. 기본값은 알림 40개이며 최대 알림 그룹 80개입니다.

types[]
: 문자열 배열. 결과에 포함할 유형입니다.

exclude_types[]
: 문자열 배열. 결과에서 제외할 유형입니다.

account_id
: 문자열. 지정한 계정에서 받은 알림만 반환합니다.

expand_accounts
: 문자열. `full`(기본값) 또는 `partial_avatars`입니다. `partial_avatars`로 설정하면 일부 계정을 반환되는 `accounts` 목록에 완전히 표시하지 않고 축약된 형태로 `partial_accounts` 목록에 반환합니다. 알림 그룹의 가장 최근 계정은 항상 `accounts` 속성에 완전한 형태로 표시합니다.

grouped_types[]
: 문자열 배열. 그룹화할 수 있는 알림 유형을 제한합니다. 클라이언트가 일부 알림 유형의 그룹화를 지원하지 않을 때 사용하세요. 생략하면 서버가 지원하는 모든 유형(현재 `favourite`, `follow`, `reblog`, `admin.sign_up`)을 그룹화합니다. 그룹화를 원하지 않으면 [GET `/api/v1/notifications`]({{< relref "methods/notifications#get" >}})을 사용하세요. 이 매개변수가 없었다면 그룹화되었을 알림은 각각 고유한 `group_key`를 가진 단일 알림 그룹으로 반환됩니다. 해당 키는 `ungrouped-{notification_id}` 형태라고 가정할 수 있습니다. 스트리밍 API와 개별 알림 API는 이 매개변수를 인식하지 않으며 여기서 반환하는 것과 다를 수 있는 “정식” `group_key`를 항상 포함합니다. 따라서 그룹화하지 않을 이러한 알림에서는 일관성을 위해 `group_key`를 무시하고 `ungrouped-{notification_id}`를 사용해야 할 수 있습니다.

include_filtered
: 불리언. 사용자의 [NotificationPolicy]({{< relref "entities/NotificationPolicy" >}})로 필터링된 알림을 포함할지 여부입니다. 기본값은 false입니다.

supported_types[]
: 문자열 배열. 대체 표현이 있어도 사용하지 않을 알림 유형입니다. 어떤 알림이든 대체 표현을 받으려면 이 매개변수를 전달해야 합니다. 이 매개변수를 사용하면 유형이 `supported_types`에 포함되지 *않은* 알림에 사용 가능한 대체 표현이 있을 때 알림 그룹의 `fallback` 속성에 포함합니다.

#### 응답 {#response}

limit=2인 호출 예입니다.

```http
GET https://mastodon.social/api/v2/notifications?limit=2 HTTP/1.1
Authorization: Bearer xxx
```

##### 200: 성공 {#200-ok}

응답 본문에는 그룹화된 알림 한 페이지가 포함됩니다. HTTP Link 헤더로 추가 페이지네이션할 수 있습니다.

```http
Link: <https://mastodon.social/api/v2/notifications?limit=2&max_id=196012>; rel="next", <https://mastodon.social/api/v2/notifications?limit=2&min_id=196014>; rel="prev";
```

```json
{
  "accounts": [
    {
      "id": "16",
      "username": "eve",
      "acct": "eve",
      // …
    },
    {
      "id": "3547",
      "username": "alice",
      "acct": "alice",
      // …
    },
    {
      "id": "31460",
      "username": "bob",
      "acct": "bob",
      // …
    },
    {
      "id": "36509",
      "username": "mallory",
      "acct": "mallory",
      // …
    }
  ],
  "statuses": [
    {
      "id": "113010503322889311",
      "created_at": "2024-08-23T08:57:12.057Z",
      "account": {
        "id": "55911",
        "username": "user",
        "acct": "user",
        // …
      },
      // …
    },
    {
      "id": "113006771938929950",
      "created_at": "2024-08-22T17:08:15.654Z",
      "account": {
        "id": "55911",
        "username": "user",
        "acct": "user",
        // …
      },
      // …
    }
  ],
  "notification_groups": [
    {
      "group_key": "favourite-113010503322889311-479000",
      "notifications_count": 2,
      "type": "favourite",
      "most_recent_notification_id": 196014,
      "page_min_id": "196013",
      "page_max_id": "196014",
      "latest_page_notification_at": "2024-08-23T08:59:56.743Z",
      "sample_account_ids": [
        "16",
        "3547"
      ],
      "status_id": "113010503322889311"
    },
    {
      "group_key": "favourite-113006771938929950-478999",
      "notifications_count": 2,
      "type": "favourite",
      "most_recent_notification_id": 196012,
      "page_min_id": "196012",
      "page_max_id": "196012",
      "latest_page_notification_at": "2024-08-23T08:16:32.112Z",
      "sample_account_ids": [
        "31460",
        "36509"
      ],
      "status_id": "113006771938929950"
    }
  ]
}
```

##### 401: 인증되지 않음 {#401-unauthorized}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 알림 그룹 하나 가져오기 {#get-notification-group}

```http
GET /api/v2/notifications/:group_key HTTP/1.1
```

지정한 그룹 키를 가진 특정 알림 그룹의 정보를 조회합니다.

**반환:** [GroupedNotificationsResults](#GroupedNotificationsResults)\
**OAuth:** 사용자 토큰 + `read:notifications`\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - 선택적 매개변수 `supported_types` 추가

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:group_key
: {{<required>}} 문자열. 알림 그룹의 그룹 키입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters-1}

supported_types[]
: 문자열 배열. 대체 표현이 있어도 사용하지 않을 알림 유형입니다. 어떤 알림이든 대체 표현을 받으려면 이 매개변수를 전달해야 합니다. 이 매개변수를 사용하면 유형이 `supported_types`에 포함되지 *않은* 알림에 사용 가능한 대체 표현이 있을 때 알림 그룹의 `fallback` 속성에 포함합니다.

#### 응답 {#response-1}

##### 200: 성공 {#200-ok-1}

성공하면 알림 그룹 하나를 포함하는 [GroupedNotificationsResults](#GroupedNotificationsResults)를 반환합니다.

```json
{
  "accounts": [
    {
      "id": "16",
      "username": "eve",
      "acct": "eve",
      // …
    },
    {
      "id": "3547",
      "username": "alice",
      "acct": "alice",
      // …
    }
  ],
  "statuses": [
    {
      "id": "113010503322889311",
      "created_at": "2024-08-23T08:57:12.057Z",
      "account": {
        "id": "55911",
        "username": "user",
        "acct": "user",
        // …
      },
      // …
    }
  ],
  "notification_groups": [
    {
      "group_key": "favourite-113010503322889311-479000",
      "notifications_count": 2,
      "type": "favourite",
      "most_recent_notification_id": 196014,
      "sample_account_ids": [
        "16",
        "3547"
      ],
      "status_id": "113010503322889311"
    }
  ]
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

## 알림 그룹 하나 지우기 {#dismiss-group}

```http
POST /api/v2/notifications/:group_key/dismiss HTTP/1.1
```

서버에서 알림 그룹 하나를 지웁니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:notifications`\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### 요청 {#request-2}

##### 경로 매개변수 {#path-parameters-1}

:group_key
: {{<required>}} 문자열. 지울 알림의 그룹 키입니다.

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

#### 응답 {#response-2}

##### 200: 성공 {#200-ok-2}

요청이 성공하면 지정한 그룹 키의 알림을 지웁니다.

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

## 알림 그룹의 모든 알림에 해당하는 계정 가져오기 {#get-group-accounts}

```http
GET /api/v2/notifications/:group_key/accounts HTTP/1.1
```

**반환:** 배열: [Account]({{< relref "entities/Account" >}})\
**OAuth:** 사용자 토큰 + `write:notifications`\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### 요청 {#request-3}

##### 경로 매개변수 {#path-parameters-2}

:group_key
: {{<required>}} 문자열. 계정을 가져올 알림의 그룹 키입니다.

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user token>`을 제공해야 합니다.

#### 응답 {#response-3}

##### 200: 성공 {#200-ok-3}

```json
[
  {
    "id": "16",
    "username": "eve",
    "acct": "eve"
    // …
  },
  {
    "id": "3547",
    "username": "alice",
    "acct": "alice"
    // …
  }
]
```

##### 401: 인증되지 않음 {#401-unauthorized-3}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## 읽지 않은 알림 수 가져오기 {#unread-group-count}

```http
GET /api/v2/notifications/unread_count HTTP/1.1
```

현재 사용자의 읽지 않은 알림 그룹 수를 상한 내에서 가져옵니다.
[알림 읽음 마커]({{< relref "methods/markers" >}})보다 새로운 알림은 읽지 않은 것으로 간주합니다.
개수는 매개변수에 따라 달라지므로 매번 계산하며 비교적 느린 작업입니다(해당 알림 전체를 가져오는 것보다는 빠릅니다). 따라서 반환하는 알림 수에 상한이 있습니다.

**반환:** `count` 키 하나를 포함하는 해시\
**OAuth:** 사용자 토큰 + `read:notifications`\
**버전 이력**:\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### 요청 {#request-4}

##### 헤더 {#headers-4}

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

grouped_types[]
: 문자열 배열. 그룹화할 수 있는 알림 유형을 제한합니다. 클라이언트가 일부 알림 유형의 그룹화를 지원하지 않을 때 사용하세요. 생략하면 서버가 지원하는 모든 유형(현재 `favourite`, `follow`, `reblog`)을 그룹화합니다. 그룹화를 원하지 않으면 [GET `/api/v1/notifications/unread_count`]({{< relref "methods/notifications#unread-count" >}})를 사용하세요.

#### 응답 {#response-4}

##### 200: 성공 {#200-ok-4}

응답 본문에는 상한을 적용한 읽지 않은 알림 수가 포함됩니다.

```json
{
  "count": 42,
}
```

##### 401: 인증되지 않음 {#401-unauthorized-4}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

---

## `GroupedNotificationsResults` 엔터티 {#GroupedNotificationsResults}

### 속성 {#attributes}

#### `accounts` {#accounts}

**설명:** 그룹화된 알림에서 참조하는 계정입니다.\
**유형:** 배열: [Account]({{< relref "entities/Account" >}})\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `partial_accounts` {{%optional%}} {#partial_accounts-optional}

**설명:** 그룹화된 알림에서 참조하는 부분 계정입니다. `expand_accounts=partial_avatars`로 그룹화된 알림을 요청할 때만 반환합니다.\
**유형:** 배열: [PartialAccountWithAvatar]({{< relref "entities/Account#PartialAccountWithAvatar" >}})\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `statuses` {#statuses}

**설명:** 그룹화된 알림에서 참조하는 게시물입니다.\
**유형:** 배열: [Status]({{< relref "entities/Status" >}})\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `notification_groups` {#notification_groups}

**설명:** 그룹화된 알림 자체입니다.\
**유형:** 배열: [NotificationGroup](#NotificationGroup)\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

### 예제 {#examples}

TODO

---

## `NotificationGroup` 엔터티 {#NotificationGroup}

### 속성 {#attributes-1}

#### `group_key` {#group_key}

**설명:** 그룹화된 알림을 식별하는 그룹 키입니다. 내부를 해석하지 않는 불투명한 값으로 취급해야 합니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `notifications_count` {#notifications_count}

**설명:** 이 알림 그룹에 속하는 개별 알림의 총수입니다.\
**유형:** 정수\\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `type` {#type}

**설명:** 이 그룹의 알림을 발생시킨 이벤트 유형입니다.\
**유형:** 문자열 (열거형 중 하나)\
`mention` = 누군가 게시물에서 나를 멘션함\
`status` = 알림을 활성화한 사람이 게시물을 작성함\
`reblog` = 누군가 내 게시물을 부스트함\
`follow` = 누군가 나를 팔로우함\
`follow_request` = 누군가 내게 팔로우를 요청함\
`favourite` = 누군가 내 게시물에 좋아요를 누름\
`poll` = 내가 투표했거나 생성한 투표가 종료됨\
`update` = 내가 상호작용한 게시물이 편집됨\
`admin.sign_up` = 누군가 가입함(선택적으로 관리자에게 전송)\
`admin.report` = 새 신고가 제출됨\
`severed_relationships` = 중재 또는 차단 이벤트로 일부 팔로우 관계가 끊어짐\
`moderation_warning` = 중재자가 내 계정에 조치를 취하거나 경고를 보냄\
`quote` = 누군가 내 게시물을 인용함\
`quoted_update` = 내가 인용한 게시물이 편집됨\
`added_to_collection` = 누군가 나를 컬렉션에 추가함\
`collection_update` = 내가 추천된 컬렉션이 수정됨\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가\
4.5.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 7) - `quote` 및 `quoted_update` 추가\
4.6.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 10) - `added_to_collection` 및 `collection_update` 추가

#### `most_recent_notification_id` {#most_recent_notification_id}

**설명:** 그룹에서 가장 최근 알림의 ID입니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `page_min_id` {{%optional%}} {#page_min_id-optional}

**설명:** 현재 페이지에 표시된 이 그룹의 가장 오래된 알림 ID입니다. 알림 그룹을 페이지네이션할 때만 반환합니다. 새 알림을 폴링할 때 유용합니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `page_max_id` {{%optional%}} {#page_max_id-optional}

**설명:** 현재 페이지에 표시된 이 그룹의 가장 새로운 알림 ID입니다. 알림 그룹을 페이지네이션할 때만 반환합니다. 새 알림을 폴링할 때 유용합니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `latest_page_notification_at` {{%optional%}} {#latest_page_notification_at-optional}

**설명:** 현재 페이지에 있는 이 그룹의 가장 최근 알림이 생성된 날짜입니다. 알림 그룹을 페이지네이션할 때만 반환합니다.\
**유형:** 문자열 ([날짜와 시간](/api/datetime-format#datetime))\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `sample_account_ids` {#sample_account_ids}

**설명:** 이 그룹에서 가장 최근에 알림을 발생시킨 계정 중 일부의 ID입니다.\
**유형:** 문자열 배열\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `status_id` {{%optional%}} {#status_id-optional}

**설명:** 알림 대상인 [Status]({{< relref "entities/Status" >}})의 ID입니다. 알림의 `type`이 `favourite`, `reblog`, `status`, `mention`, `poll`, `update`, `quote`, `quoted_update`이면 첨부됩니다. `quoted_update`에서는 편집된 게시물 대신 그 게시물을 인용한 내 게시물이 첨부됩니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `report` {{%optional%}} {#report-optional}

**설명:** 알림 대상인 신고입니다. 알림의 `type`이 `admin.report`이면 첨부됩니다.\
**유형:** [Report]({{< relref "entities/Report" >}})\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `event` {{%optional%}} {#event-optional}

**설명:** 팔로우 관계를 끊은 이벤트의 요약입니다. 알림의 `type`이 `severed_relationships`이면 첨부됩니다.\
**유형:** [RelationshipSeveranceEvent]({{< relref "entities/RelationshipSeveranceEvent" >}})\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `moderation_warning` {{%optional%}} {#moderation_warning-optional}

**설명:** 알림을 발생시킨 중재 경고입니다. 알림의 `type`이 `moderation_warning`이면 첨부됩니다.\
**유형:** [AccountWarning]({{< relref "entities/AccountWarning" >}})\
**버전 이력:**\
4.3.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 2) - 추가

#### `fallback` {{%optional%}} {#fallback-optional}

**설명:** 클라이언트가 지원하지 않을 수 있는 일부 알림 유형에 제공되는 대체 정보입니다. 일부 알림 유형에서만 제공되며 조회 시 `supported_types` 매개변수를 사용해야 합니다.\
**유형:** [NotificationFallback]({{< relref "entities/NotificationFallback" >}})\
**버전 이력:**\
4.6.0 - 추가

#### `collection` {{%optional%}} {#collection-optional}

**설명:** 알림 대상인 컬렉션입니다. 알림의 `type`이 `added_to_collection` 또는 `collection_update`이면 첨부됩니다.\
**유형:** [Collection]({{< relref "entities/Collection" >}})\
**버전 이력:**\
4.6.0 - 추가

### 예제 {#examples-1}

TODO

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/notifications" caption="개별 알림 API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v2/notifications_controller.rb" caption="app/controllers/api/v2/notifications_controller.rb" >}}
