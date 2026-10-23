---
title: 알림 요청 (NotificationRequest)
description: 특정 사용자가 보낸 필터링된 알림 그룹을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/NotificationRequest",
]
---

## 속성 {#attributes}

### `id` {#id}

**설명:** 데이터베이스의 알림 요청 ID입니다.\
**유형:** 문자열 (정수에서 변환하지만 숫자라는 보장은 없음)\
**버전 이력:**\
4.3.0 - 추가

### `created_at` {#created_at}

**설명:** 알림 요청의 타임스탬프로, 해당 사용자의 첫 번째 필터링된 알림이 생성된 시각입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.3.0 - 추가

### `updated_at` {#updated_at}

**설명:** 알림 요청의 마지막 갱신 시각을 나타내는 타임스탬프입니다.\
**유형:** 문자열 ([날짜와 시각](/api/datetime-format#datetime))\
**버전 이력:**\
4.3.0 - 추가

### `account` {#account}

**설명:** 필터링된 알림을 발생시킨 동작을 수행한 계정입니다.\
**유형:** [Account]({{< relref "entities/Account" >}})\
**버전 이력:**\
4.3.0 - 추가

### `notifications_count` {#notifications_count}

**설명:** 이 계정의 알림 중 필터링된 알림 수입니다.\
**유형:** 문자열\
**버전 이력:**\
4.3.0 - 추가

### `last_status` {{%optional%}} {#last_status}

**설명:** 이 계정의 필터링된 알림에 연결된 가장 최근 게시물입니다.\
**유형:** [Status]({{< relref "entities/Status" >}})\
**버전 이력:**\
4.3.0 - 추가

## 예시 {#example}

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

## 함께 보기 {#see-also}

{{< page-relref ref="methods/notifications" caption="notifications API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/notification_request_serializer.rb" caption="app/serializers/rest/notification_request_serializer.rb" >}}
