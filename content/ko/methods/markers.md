---
title: 마커 API 메서드
description: 타임라인의 위치를 저장하고 복원합니다.
menu:
  docs:
    name: 마커
    parent: methods-timelines
    identifier: methods-markers
aliases: [
  "/methods/markers",
  "/api/methods/markers",
  "/methods/timelines/markers",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## 저장된 타임라인 위치 가져오기 {#get}

```http
GET /api/v1/markers HTTP/1.1
```

타임라인의 현재 위치를 가져옵니다.

**반환:** 문자열(열거형, `home` 또는 `notifications` 중 하나)을 키로, 해당 [Marker]({{< relref "entities/Marker" >}})를 값으로 하는 해시\
**OAuth:** 사용자 토큰 + `read:statuses`\
**버전 이력:**\
3.0.0 - 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 쿼리 매개변수 {#query-parameters}

timeline[]
: 문자열 배열. 마커를 가져올 타임라인을 지정합니다. 가능한 값은 `home`, `notifications`입니다. 생략하면 빈 객체를 반환합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

`?timeline[]=home&timeline[]=notifications`를 사용하는 요청입니다.

```json
{
  "notifications": {
    "last_read_id": "35098814",
    "version": 361,
    "updated_at": "2019-11-26T22:37:25.239Z"
  },
  "home": {
    "last_read_id": "103206604258487607",
    "version": 468,
    "updated_at": "2019-11-26T22:37:25.235Z"
  }
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

## 타임라인 위치 저장 {#create}

```http
POST /api/v1/markers HTTP/1.1
```

타임라인의 현재 위치를 저장합니다.

**반환:** 문자열(열거형, `home` 또는 `notifications` 중 하나)을 키로, 해당 [Marker]({{< relref "entities/Marker" >}})를 값으로 하는 해시\
**OAuth:** 사용자 토큰 + `write:statuses`\
**버전 이력:**\
3.0.0 - 추가

#### 요청 {#request-1}

##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

home[last_read_id]
: 문자열. 홈 타임라인에서 마지막으로 읽은 게시물의 ID입니다.

notifications[last_read_id]
: 문자열. 마지막으로 읽은 알림의 ID입니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

home[last_read_id]로 이 API를 호출하면 홈 타임라인 마커를 생성합니다.

```json
{
  "home": {
    "last_read_id": "103194548672408537",
    "version": 462,
    "updated_at": "2019-11-24T19:39:39.337Z"
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

### 409: 충돌 {#409-conflict}

수정 중인 객체가 오래된 상태이면 오류가 발생합니다.

```json
{
  "error": "Conflict during update, please try again"
}
```

---

## 함께 보기 {#see-also}

{{< page-relref ref="methods/timelines#home" caption="GET /api/v1/timelines/home (with `min_id` or `since_id` parameter)" >}}

{{< page-relref ref="methods/notifications#get" caption="GET /api/v1/notifications (with `min_id` or `since_id` parameter)" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/markers_controller.rb" caption="app/controllers/api/v1/markers_controller.rb" >}}
