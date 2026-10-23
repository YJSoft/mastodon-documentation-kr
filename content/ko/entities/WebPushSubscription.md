---
title: 웹 푸시 구독 (WebPushSubscription)
description: 푸시 스트리밍 서버 구독을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/pushsubscription",
  "/entities/PushSubscription",
  "/entities/webpushsubscription",
  "/entities/WebPushSubscription",
  "/api/entities/pushsubscription",
  "/api/entities/PushSubscription",
  "/api/entities/webpushsubscription",
  "/api/entities/WebPushSubscription",
]
---

## 예시 {#example}

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

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 웹 푸시 구독 ID입니다.\
**유형:** 정수\
**버전 이력:**\
2.4.0 - 추가

### `endpoint` {#endpoint}

**설명:** 푸시 알림을 보낼 대상입니다.\
**유형:** 문자열 (URL)\
**버전 이력:**\
2.4.0 - 추가

### `standard` {#standard}

**설명:** 푸시 메시지가 표준 사양(RFC8030+RFC8291+RFC8292)을 따르는지 나타냅니다. 그렇지 않으면 구버전 사양(RFC8291의 4차 초안 및 RFC8292의 1차 초안)을 따릅니다.\
**유형:** 불리언\
**버전 이력:**\
4.4.0 - 추가

### `server_key` {#server_key}

**설명:** 스트리밍 서버의 VAPID 키입니다.\
**유형:** 문자열\
**버전 이력:**\
2.4.0 - 추가

### `alerts` {#alerts}

**설명:** `endpoint`로 전달할 알림입니다.\
**유형:** 해시\
**버전 이력:**\
2.4.0 - 추가\
2.8.0 - `alerts[poll]` 추가\
3.1.0 - `alerts[follow_request]` 추가\
3.3.0 - `alerts[status]` 추가\
3.5.0 - `alerts[update]`와 `alerts[admin.sign_up]` 추가\
4.0.0 - `alerts[admin.report]` 추가

#### `alerts[mention]` {#mention}

**설명:** 다른 사람이 게시물에서 나를 멘션하면 푸시 알림을 받을지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.4.0 - 추가

#### `alerts[status]` {#status}

**설명:** 구독한 계정이 게시물을 올리면 푸시 알림을 받을지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.3.0 - 추가

#### `alerts[reblog]` {#reblog}

**설명:** 다른 사람이 내 게시물을 부스트하면 푸시 알림을 받을지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.4.0 - 추가

#### `alerts[follow]` {#follow}

**설명:** 누군가 나를 팔로우하면 푸시 알림을 받을지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.4.0 - 추가

#### `alerts[follow_request]` {#follow_request}

**설명:** 누군가 나에게 팔로우를 요청하면 푸시 알림을 받을지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.1.0 - 추가

#### `alerts[favourite]` {#favourite}

**설명:** 다른 사람이 내 게시물에 좋아요를 누르면 푸시 알림을 받을지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.4.0 - 추가

#### `alerts[poll]` {#poll}

**설명:** 내가 참여하거나 만든 투표가 종료되면 푸시 알림을 받을지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
2.8.0 - 추가

#### `alerts[update]` {#update}

**설명:** 내가 상호작용한 게시물이 수정되면 푸시 알림을 받을지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.5.0 - 추가

#### `alerts[admin.sign_up]` {#admin-sign_up}

**설명:** 새 사용자가 가입하면 푸시 알림을 받을지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
3.5.0 - 추가

#### `alerts[admin.report]` {#admin-report}

**설명:** 새 신고가 접수되면 푸시 알림을 받을지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.0.0 - 추가

## 함께 보기 {#see-also}

{{< page-relref ref="methods/push" caption="push API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/web_push_subscription_serializer.rb" caption="app/serializers/rest/web_push_subscription_serializer.rb" >}}



