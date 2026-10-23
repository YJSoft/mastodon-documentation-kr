---
title: 예약 게시물 API 메서드
description: 미래 시점에 게시하도록 예약한 게시물을 관리합니다.
menu:
  docs:
    name: 예약 게시물
    parent: methods-statuses
    identifier: methods-scheduled_statuses
aliases: [
  "/methods/scheduled_statuses",
  "/api/methods/scheduled_statuses",
  "/methods/statuses/scheduled_statuses",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 예약 게시물 조회 {#get}

```http
GET /api/v1/scheduled_statuses HTTP/1.1
```

**반환:** 배열: [ScheduledStatus]({{< relref "entities/scheduledstatus" >}})\
**OAuth:** 사용자 토큰 + `read:statuses`\
**버전 이력:**\
2.7.0 - 추가\
3.3.0 - 이제 `min_id`와 `max_id` 동시 사용 가능

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
: 정수. 반환할 최대 결과 수입니다. 기본값은 게시물 20개이며 최대 40개입니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

```json
[
  {
    "id": "3221",
    "scheduled_at": "2019-12-05T12:33:01.000Z",
    "params": {
      "poll": null,
      "text": "test content",
      "media_ids": null,
      "sensitive": null,
      "visibility": null,
      "idempotency": null,
      "scheduled_at": null,
      "spoiler_text": null,
      "application_id": 596551,
      "in_reply_to_id": null,
      "quoted_status_id": null,
      "quote_approval_policy": "followers"
    },
    "media_attachments": []
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

## 예약 게시물 하나 조회 {#get-one}

```http
GET /api/v1/scheduled_statuses/:id HTTP/1.1
```

**반환:** [ScheduledStatus]({{< relref "entities/scheduledstatus" >}})\
**OAuth:** 사용자 토큰 + `read:statuses`\
**버전 이력:**\
2.7.0 - 추가

#### 요청 {#request-1}

##### 경로 매개변수 {#path-parameters}

:id
: {{<required>}} 문자열. 데이터베이스의 ScheduledStatus ID입니다.

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

```json
{
  "id": "3221",
  "scheduled_at": "2019-12-05T12:33:01.000Z",
  "params": {
    "poll": null,
    "text": "test content",
    "media_ids": null,
    "sensitive": null,
    "visibility": null,
    "idempotency": null,
    "scheduled_at": null,
    "spoiler_text": null,
    "application_id": 596551,
    "in_reply_to_id": null,
    "quoted_status_id": null,
    "quote_approval_policy": "followers"
  },
  "media_attachments": []
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

ScheduledStatus가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

## 예약 게시물의 게시 날짜 수정 {#update}

```http
PUT /api/v1/scheduled_statuses/:id HTTP/1.1
```

**반환:** [ScheduledStatus]({{< relref "entities/scheduledstatus" >}})\
**OAuth:** 사용자 토큰 + `write:statuses`\
**버전 이력:**\
2.7.0 - 추가

#### 요청 {#request-2}

##### 경로 매개변수 {#path-parameters-1}

:id
: {{<required>}} 문자열. 데이터베이스의 ScheduledStatus ID입니다.

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

scheduled_at
: 문자열. 게시물을 게시할 [날짜와 시간](/api/datetime-format#datetime)입니다. 적어도 5분 이후여야 합니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

```json
{
  "id": "3221",
  "scheduled_at": "2019-12-05T13:33:01.000Z",
  "params": {
    "poll": null,
    "text": "test content",
    "media_ids": null,
    "sensitive": null,
    "visibility": null,
    "idempotency": null,
    "scheduled_at": null,
    "spoiler_text": null,
    "application_id": 596551,
    "in_reply_to_id": null,
    "quoted_status_id": null,
    "quote_approval_policy": "followers"
  },
  "media_attachments": []
}
```

##### 401: 인증되지 않음 {#401-unauthorized-2}

Authorization 헤더가 없거나 유효하지 않습니다.

```json
{
  "error": "The access token is invalid"
}
```

##### 404: 찾을 수 없음 {#404-not-found-1}

ScheduledStatus가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

##### 422: 처리할 수 없는 엔터티 {#422-unprocessable-entity}

```json
{
  "error": "Validation failed: Scheduled at The scheduled date must be in the future"
}
```

---

## 예약 게시물 취소 {#cancel}

```http
DELETE /api/v1/scheduled_statuses/:id HTTP/1.1
```

**반환:** 없음\
**OAuth:** 사용자 토큰 + `write:statuses`\
**버전 이력:**\
2.7.0 - 추가

#### 요청 {#request-3}

##### 경로 매개변수 {#path-parameters-2}

:id
: {{<required>}} 문자열. 데이터베이스의 ScheduledStatus ID입니다.

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-3}
##### 200: 성공 {#200-ok-3}

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

##### 404: 찾을 수 없음 {#404-not-found-2}

ScheduledStatus가 내 소유가 아니거나 존재하지 않습니다.

```json
{
  "error": "Record not found"
}
```

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/statuses#create" caption="POST /api/v1/statuses (`scheduled_at` parameter)" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/scheduled_statuses_controller.rb" caption="app/controllers/api/v1/scheduled_statuses_controller.rb" >}}
