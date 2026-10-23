---
title: V1 알림 정책 (V1::NotificationPolicy)
description: 사용자의 알림 필터링 정책을 나타냅니다.
menu:
  docs:
    parent: entities
aliases: [
  "/entities/v1_NotificationPolicy",
]
---

{{< hint style="warning" >}}
이 버전의 알림 필터링 정책 API는 폐기 예정이며 어떤 릴리스에도 포함되지 않았습니다. [현재 버전]({{< relref "entities/NotificationPolicy">}})을 참고하세요.
{{</ hint >}}

## 속성 {#attributes}

### `filter_not_following` {#filter_not_following}

**설명:** 사용자가 팔로우하지 않는 계정의 알림을 필터링할지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.3.0 - 추가

### `filter_not_followers` {#filter_not_followers}

**설명:** 사용자를 팔로우하지 않는 계정의 알림을 필터링할지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.3.0 - 추가

### `filter_new_accounts` {#filter_new_accounts}

**설명:** 지난 30일 이내에 생성된 계정의 알림을 필터링할지 나타냅니다.\
**유형:** 불리언\
**버전 이력:**\
4.3.0 - 추가

### `filter_private_mentions` {#filter_private_mentions}

**설명:** 개인 멘션 알림을 필터링할지 나타냅니다. 사용자가 시작한 개인 멘션에 대한 답글과 사용자가 팔로우하는 계정은 필터링하지 않습니다.\
**유형:** 불리언\
**버전 이력:**\
4.3.0 - 추가

### `summary` {#summary}

**설명:** 필터링된 알림의 요약입니다.\
**유형:** 해시\
**버전 이력:**\
4.3.0 - 추가

### `summary[pending_requests_count]` {#pending_requests_count}

**설명:** 사용자에게 해제하지 않은 필터링된 알림을 보낸 서로 다른 계정 수입니다. 최대 100입니다.\
**유형:** 정수\
**버전 이력:**\
4.3.0 - 추가

### `summary[pending_notifications_count]` {#pending_notifications_count}

**설명:** 해제하지 않은 필터링된 알림의 총수입니다. 정확하지 않을 수 있습니다.\
**유형:** 정수\
**버전 이력:**\
4.3.0 - 추가

## 예시 {#example}

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

## 함께 보기 {#see-also}

{{< page-relref ref="entities/NotificationPolicy" caption="NotificationPolicy (출시된 버전)" >}}

{{< page-relref ref="methods/notifications" caption="notifications API 메서드" >}}

{{< caption-link url="https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/v1/notification_policy_serializer.rb" caption="app/serializers/rest/v1/notification_policy_serializer.rb" >}}
