---
title: 푸시 API 메서드
description: >-
  Web Push API를 통해 서버 측 알림이 수신될 때 푸시 알림을 구독하고 받습니다.
menu:
  docs:
    name: 푸시
    parent: methods-notifications
    identifier: methods-push
aliases: [
  "/methods/push",
  "/api/methods/push",
  "/methods/notifications/push",
]
---

<style>
#TableOfContents ul ul ul {display: none}
</style>

## Web Push API 소개 {#about}

마스토돈은 [Web Push API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API)를 기본 지원합니다. 네이티브 앱에서도 같은 방식을 사용할 수 있습니다. 마스토돈은 Android와 Apple의 독점 알림 게이트웨이에 직접 연결하지 않으므로 이를 사용하려면 WebPush 표준과 해당 게이트웨이 사이를 변환하는 프록시 서버를 사용할 수 있습니다. 프록시 서버가 알림 내용에 접근할 수 없도록 구현할 수 있습니다. 예를 들어 [Mozilla의 참조 웹 푸시 서버](https://github.com/mozilla-services/autopush)나 마스토돈 커뮤니티가 이 목적으로 개발한 다음 릴레이를 참고하세요.

* [toot-relay](https://github.com/DagAgren/toot-relay)
* [SubwayTooterAppServerV2](https://github.com/tateisu/SubwayTooterAppServerV2)
* [metatext-apns](https://github.com/metabolist/metatext-apns)

---

## 푸시 알림 구독 {#create}

```http
POST /api/v1/push/subscription HTTP/1.1
```

알림을 받기 위한 Web Push API 구독을 추가합니다. 각 액세스 토큰에는 하나의 푸시 구독이 가능합니다. 새 구독을 생성하면 기존 구독은 삭제됩니다.

**반환:** [WebPushSubscription]({{< relref "entities/WebPushSubscription" >}})\
**OAuth:** 사용자 토큰 + `push`\
**버전 이력:**\
2.4.0 - 추가\
3.3.0 - `data[alerts][status]` 추가\
3.4.0 - `data[policy]` 추가\
3.5.0 - `data[alerts][update]` 및 `data[alerts][admin.sign_up]` 추가\
4.0.0 - `data[alerts][admin.report]` 추가\
4.3.0 - 요청 매개변수 검증 강화. 이전에 수락된 뒤 조용히 실패하던 유효하지 않은 엔드포인트 URL과 구독 키는 이제 오류 발생\
4.4.0 - `subscription[standard]` 추가\
4.5.0 (`mastodon` [API 버전]({{< relref "entities/Instance#api-versions" >}}) 7) - `data[alerts][quote]` 및 `data[alerts][quoted_update]` 추가

#### 요청 {#request}

##### 헤더 {#headers}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters}

subscription[endpoint]
: {{<required>}} 문자열. 알림 이벤트가 발생할 때 호출할 엔드포인트 URL입니다.

subscription[keys][p256dh]
: {{<required>}} 문자열. 사용자 에이전트 공개 키입니다. `prime256v1` 곡선을 사용하는 ECDH 키 쌍의 공개 키를 Base64로 인코딩한 문자열입니다.

subscription[keys][auth]
: {{<required>}} 문자열. 인증 시크릿입니다. 16바이트 무작위 데이터를 Base64로 인코딩한 문자열입니다.

subscription[standard]
: 불리언. 표준화된 webpush(RFC8030+RFC8291+RFC8292)를 따를지 여부입니다. 그렇지 않으면 레거시 webpush(미공개 버전, RFC8291의 4차 초안과 RFC8292의 1차 초안)를 따릅니다. 기본값은 false입니다.

data[alerts][mention]
: 불리언. 멘션 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][quote]
: 불리언. 인용 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][status]
: 불리언. 새로 구독한 계정의 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][reblog]
: 불리언. 부스트 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][follow]
: 불리언. 팔로우 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][follow_request]
: 불리언. 팔로우 요청 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][favourite]
: 불리언. 좋아요 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][poll]
: 불리언. 투표 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][update]
: 불리언. 게시물 편집 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][quoted_update]
: 불리언. 인용한 게시물의 편집 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][admin.sign_up]
: 불리언. 새 사용자 가입 알림을 받을지 여부입니다. 기본값은 false입니다. 적절한 권한을 가진 역할이 있어야 합니다.

data[alerts][admin.report]
: 불리언. 새 신고 알림을 받을지 여부입니다. 기본값은 false입니다. 적절한 권한을 가진 역할이 있어야 합니다.

data[policy]
: 문자열. `all`, `followed`, `follower`, `none` 사용자 중 누구의 푸시 알림을 받을지 지정합니다.

#### 응답 {#response}
##### 200: 성공 {#200-ok}

요청한 알림을 내 엔드포인트로 보낼 새 PushSubscription을 생성했습니다.

```json
{
  "id": 328183,
  "endpoint": "https://yourdomain.example/listener",
  "standard": true,
  "alerts": {
    "follow": true,
    "favourite": true,
    "reblog": true,
    "mention": true,
    "poll": true
  },
  "server_key": "BCk-QqERU0q-CfYZjcuB6lnyyOYfJ2AifKqfeGIm7Z-HiTU5T9eTG5GxVA0_OH5mMlI4UkkDTpaZwozy0TzdZ2M="
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

## 현재 구독 가져오기 {#get}

```http
GET /api/v1/push/subscription HTTP/1.1
```

현재 이 액세스 토큰에 연결된 PushSubscription을 조회합니다.

**반환:** [WebPushSubscription]({{< relref "entities/WebPushSubscription" >}})\
**OAuth:** 사용자 토큰 + `push`\
**버전 이력:**\
2.4.0 - 추가

#### 요청 {#request-1}
##### 헤더 {#headers-1}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-1}
##### 200: 성공 {#200-ok-1}

```json
{
  "id": 328183,
  "endpoint": "https://yourdomain.example/listener",
  "standard": true,
  "alerts": {
    "follow": true,
    "favourite": true,
    "reblog": true,
    "mention": true,
    "poll": true
  },
  "server_key": "BCk-QqERU0q-CfYZjcuB6lnyyOYfJ2AifKqfeGIm7Z-HiTU5T9eTG5GxVA0_OH5mMlI4UkkDTpaZwozy0TzdZ2M="
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

이 토큰의 PushSubscription이 없습니다.

```json
{
  "error": "Record not found"
}
```

---

## 알림 유형 변경 {#update}

```http
PUT /api/v1/push/subscription HTTP/1.1
```

현재 푸시 구독을 수정합니다. 데이터 부분만 수정할 수 있습니다. 기본 요소를 변경하려면 새 구독을 생성해야 합니다.

**반환:** [WebPushSubscription]({{< relref "entities/WebPushSubscription" >}})\
**OAuth:** 사용자 토큰 + `push`\
**버전 이력:**\
2.4.0 - 추가\
3.3.0 - `data[alerts][status]` 추가\
3.4.0 - `policy` 추가\
3.5.0 - `data[alerts][update]` 및 `data[alerts][admin.sign_up]` 추가\
4.0.0 - `data[alerts][admin.report]` 추가

#### 요청 {#request-2}

##### 헤더 {#headers-2}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

##### 폼 데이터 매개변수 {#form-data-parameters-1}

data[alerts][mention]
: 불리언. 멘션 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][status]
: 불리언. 새로 구독한 계정의 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][reblog]
: 불리언. 부스트 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][follow]
: 불리언. 팔로우 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][follow_request]
: 불리언. 팔로우 요청 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][favourite]
: 불리언. 좋아요 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][poll]
: 불리언. 투표 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][update]
: 불리언. 게시물 편집 알림을 받을지 여부입니다. 기본값은 false입니다.

data[alerts][admin.sign_up]
: 불리언. 새 사용자 가입 알림을 받을지 여부입니다. 기본값은 false입니다. 적절한 권한을 가진 역할이 있어야 합니다.

data[alerts][admin.report]
: 불리언. 새 신고 알림을 받을지 여부입니다. 기본값은 false입니다. 적절한 권한을 가진 역할이 있어야 합니다.

policy
: 문자열. `all`, `followed`, `follower`, `none` 사용자 중 누구의 푸시 알림을 받을지 지정합니다.

#### 응답 {#response-2}
##### 200: 성공 {#200-ok-2}

멘션 알림만 받도록 PushSubscription을 수정합니다.

```json
{
  "id": 328183,
  "endpoint": "https://yourdomain.example/listener",
  "standard": true,
  "alerts": {
    "follow": false,
    "favourite": false,
    "reblog": false,
    "mention": true,
    "poll": false
  },
  "server_key": "BCk-QqERU0q-CfYZjcuB6lnyyOYfJ2AifKqfeGIm7Z-HiTU5T9eTG5GxVA0_OH5mMlI4UkkDTpaZwozy0TzdZ2M="
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

이 토큰의 기존 PushSubscription이 없습니다.

```json
{
  "error": "Record not found"
}
```

---

## 현재 구독 제거 {#delete}

```http
DELETE /api/v1/push/subscription HTTP/1.1
```

현재 Web Push API 구독을 제거합니다.

**반환:** 없음\
**OAuth:** 사용자 토큰 + `push`\
**버전 이력:**\
2.4.0 - 추가

#### 요청 {#request-3}

##### 헤더 {#headers-3}

Authorization
: {{<required>}} 이 API 메서드에 접근하려면 이 헤더의 값으로 `Bearer <user_token>`을 제공해야 합니다.

#### 응답 {#response-3}

##### 200: 성공 {#200-ok-3}

PushSubscription을 삭제했거나 이전에 존재하지 않았습니다.

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

## 함께 보기 {#see-also}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/push/subscriptions_controller.rb" caption="app/controllers/api/v1/push/subscriptions_controller.rb" >}}
